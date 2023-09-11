package io.conduktor.demos.kafka;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoWithKeys {

    private static final Logger log = LoggerFactory.getLogger(ProducerDemoWithKeys.class.getSimpleName());

    public static void main(String[] args) {
        log.info("I am a Kafka Producer!");

        // create Producer Properties
        Properties properties = new Properties();

        // Connect to local Kafka
//        properties.setProperty("bootstrap.servers", "localhost:9092");

        // Connect to Conduktor Playground
        properties.setProperty("bootstrap.servers", "cluster.playground.cdkt.io:9092");
        properties.setProperty("security.protocol", "SASL_SSL");
//        properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"\" password=\"\";");
        properties.setProperty("sasl.mechanism", "PLAIN");

        // Set producer properties
        properties.setProperty("key.serializer", StringSerializer.class.getName());
        properties.setProperty("value.serializer", StringSerializer.class.getName());


        // create the Producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);


        for (int j=0; j<2; j++) {
            // loop for sending messages
            for (int i = 0; i < 10 ; i++) {

                String topic = "demo_java";
                String key = "id_" + i;
                String value = "hello world " + i;

                // create a producer record
                ProducerRecord<String, String> producerRecord =
                        new ProducerRecord<>(topic, key, value);

                // send data
                producer.send(producerRecord, new Callback() {
                    @Override
                    public void onCompletion(RecordMetadata metadata, Exception exception) {
                        // executes every time a record is successfully sent or an exception is thrown
                        if (exception == null) {
                            // the record was successfully sent
                            log.info("Key: " + key + " | Partition: " + metadata.partition());
                        } else {
                            log.error("Error while producing", exception);
                        }
                    }
                });
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // tell the producer to send all the data and block until it's done -- synchronous
        producer.flush();

        // flush and close producer
        producer.close();
    }
}
