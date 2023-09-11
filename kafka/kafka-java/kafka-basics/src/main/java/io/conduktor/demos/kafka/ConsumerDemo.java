package io.conduktor.demos.kafka;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

public class ConsumerDemo {

    private static final Logger log = LoggerFactory.getLogger(ConsumerDemo.class.getSimpleName());

    public static void main(String[] args) {
        log.info("I am a Kafka Consumer!");

        String groupId = "my-java-consumer";
        String topic = "demo_java";

        // create Producer Properties
        Properties properties = new Properties();

        // Connect to local Kafka
//        properties.setProperty("bootstrap.servers", "localhost:9092");

        // Connect to Conduktor Playground
        properties.setProperty("bootstrap.servers", "cluster.playground.cdkt.io:9092");
        properties.setProperty("security.protocol", "SASL_SSL");
//        properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"\" password=\"\";");
        properties.setProperty("sasl.mechanism", "PLAIN");

        // Create consumer properties
        properties.setProperty("key.deserializer", StringDeserializer.class.getName());
        properties.setProperty("value.deserializer", StringDeserializer.class.getName());
        properties.setProperty("group.id", groupId);
        properties.setProperty("auto.offset.reset", "earliest");

        // create the Consumer
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

        // subscribe consumer topic(s)
        consumer.subscribe(Arrays.asList(topic));

        // poll for new data
        while (true) {
            log.info("Polling for new data...");
            ConsumerRecords<String, String> records =
                consumer.poll(Duration.ofMillis(1000));

            for (ConsumerRecord<String, String> record : records) {
                log.info("Key: " + record.key() + " | Value: " + record.value());
                log.info("Partition: " + record.partition() + " | Offset: " + record.offset());
            }
        }
    }
}
