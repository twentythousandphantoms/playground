package io.conduktor.demos.kafka;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoWithCallback {

    private static final Logger log = LoggerFactory.getLogger(ProducerDemoWithCallback.class.getSimpleName());

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

        // Set small batch size for tests
        properties.setProperty("batch.size", "400");
//        properties.setProperty("partitioner.class", RoundRobinPartitioner.class.getName());

        // create the Producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        // loop for batching
        for (int j=0; j<10; j++){

            // loop for sending messages in batch
            for (int i = 0; i < 30 ; i++) {
                // create a producer record
                ProducerRecord<String, String> producerRecord =
                        new ProducerRecord<>("demo_java", "hello world " + i);

                // send data
                producer.send(producerRecord, new Callback() {
                    @Override
                    public void onCompletion(RecordMetadata metadata, Exception exception) {
                        // executes every time a record is successfully sent or an exception is thrown
                        if (exception == null) {
                            // the record was successfully sent
                            log.info("Received new metadata. \n" +
                                    "Topic: " + metadata.topic() + "\n" +
                                    "Partition: " + metadata.partition() + "\n" +
                                    "Offset: " + metadata.offset() + "\n" +
                                    "Timestamp: " + metadata.timestamp());
                        } else {
                            log.error("Error while producing", exception);
                        }
                    }
                });
            }

            try {
                Thread.sleep(500);
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
