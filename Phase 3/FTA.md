# FTA

Fault Tree Analysis for ATC

</br>

## ATC

| Fault Name | Fault Description |
| :--------- | :---------------- |
| Bad Evently Data | If data does not match Pulsar schema, it is sent to different BookKeeper node (bookie) and is not accessible |
| Message Expiration | If messages that have an expiration are still unacknowledged after exedding TTL, they are deleted from queue |
| Cumulative Consumer Failure | If consumer acknowledges messages cumulatively and fails, messages could be read twice |
| Failure to Acknowledge | If ATC does not acknowledge that it consumed a message from Pulsar, it could read that message again |
| Wrong Event Stream Host | Invalid Server ID configuration prevents ATC from pulling from proper event stream host |
| Corrupt Warnings | MITM attack sends corrupt warnings to Evently |
| Events Routed to Wrong Event Handler | MITM attack sends mismatched event-key values to ATC |
| Django Null Destination Airport | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Destination Airport |
| Django Null Gate | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Gate |
| Django Null Runway | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Runway |
| Django Null Airline | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Airline |
| Django Null Plane | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Plane |
| Django Null Source Airport | MITM attack sends mismatched event-key values to ATC. Event Nonexistant Source Airport |

</br>

## Pulsar 

| Fault Name | Fault Description |
| :--------- | :---------------- |
| Pulsar cannot connect to Zookeeper | If a Pulsar node loses connection to Zookeeper, it stops accepting I/O and restarts |
| Broker cannot connect to Zookeeper | If broker loses connection to Zookeeper, it restarts and another broker takes over which could lead to duplicate messages |
| Bookie Outage Duplicates Messages | If enough bookies fail, message duplication occurs |
| Topic Partition cannot write | If enough bookies fail, topic partition loses write ability |
| Topic Partition cannot read | If no brokers are available, topic partition loses read ability |
| Django Event Handler Crashes | Invalid site sends invalid events to Pulsar | 
| Event Store Failure | XSS attack removes events from Pulsar |
| ATC Consumption Failure | Invalid site consumes Pulsar messages instead of ATC |
| Cannot Receive Evently Events | DOS attack on Pulsar |

</br>

## Evently

| Fault Name | Fault Description |
| :--------- | :---------------- |
| ATC Warning Failure | DOS attack prevents Evently from receiving ATC warnings |