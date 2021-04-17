| Reference ID | Item | Cause | Effect | Probability A-E | Severity I-V | Detectability 1-6 | Risk Level 0-1 | Precautionary Action | Mitigation Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| E-1 | Evently No RxD | Invallid site executes Denial of Service (DoS) attack on Evently | Evently fails to recieve timly warnings from Django | C | I | 3 | Acceptable | Implement Prometheous to warn when message latency passes acceptable margins & implement TxD limits on clients | If precautionary actions fail, blacklist invallid client |
| P-1 | Pulsar No Service | Unknown causes without our jurisdiction | Django app loses access to ATC events from Pulsar | A | V | 1 | Acceptable | implement _sentry_ to monitor pulsar connection status | Contact Pulsar services to restore event stream |
| P-2 | Pulsar UnAuth Event | Invalid site sends invallid events to Pulsar | Django event handler crashes | D | V | 6 | UnAcceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |  
| P-3 | Pulsar UnAuth Ack | Invallid site ack Pulsar events | Events are not handled by Django, but instead by an invallid site | D | III | 5 | UnAcceptable |Use cookies | -_- |
| P-4 | Pulsar No Django RxD | Invallid site executes Man-in-the-Middle (MITM) attack on Pulsar | Pulsar does not recieve Django's Ack & Django never handles new events. Events eventually die due to TTL limitations | B | IV | 3 | UnAcceptable | Use cookies | block faulty clients |
| P-5 | Pulsar No Evently RxD | Invallid site executes Denial of Service (DoS) attack on Pulsar | Pulsar recieves delayed Evently events | B | I | 2 | Acceptable | Implement TxD limits on messengers | imeout voliating messenger & note messenger in .log |
| P-6 | Pulsar Bookie Outage | Invallid site executes Denial of Service (DoS) attack on Pulsar with invallid event schema | Pulsar Zookeeper Node continually restarts itself, causing a no service error | B | III | 1 | Acceptable | Restrict user access to Pulsar Admin and communication of admin auth keys | If error detected, close connection and change user credentials |
| P-7 | Duplicate Events | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event has a duplicate route for a plane | B | I | 3 | Acceptable | Implement Sentry to warn if MITM begins to notably affect system performance | Resecure whatever auth credential was used to conduct the attack |
| P-8 | Pulsar UnAuth Admin | Invalid site ends Pulsar bookies/brokers, revoking Topic Partition's respective Write/Read Abilities | Pulsar events fail to be processed |  B| III | 1 | Acceptable | Restrict user access to Pulsar Admin and communication of admin auth keys | If error detected, close connection and change user credentials |
| D-1 | Django UnAuth Admin | Invalid Server ID configuration | Django fails to pull from proper event stream host | B | IV | 1 | Acceptable | Restrict user access to Pulsar Admin and communication of admin auth keys | If error detected, close connection and change user credentials |
| D-2 | Django No Pulsar TxD | Invallid site executes Man-in-the-Middle (MITM) attack & sends currupt ack | Django fails to send proper event ack to Pulsar & endlessly consumes the same event | B | IV | 2 | UnAcceptable |Use cookies and sessions for site identification| Redirect to the correct site  |
| D-3 | Django No Evently TxD | Invallid site executes Man-in-the-Middle (MITM) attack & sends currupt warning | Django fails to send proper event warning to Evently | B | IV | 2 | UnAcceptable |Use cookies and sessions for site identification |Redirect to the correct site|
| D-4 | Pulsar Failure | Invallid site executes Cross-Site Scripting (XSS) attack from Django & removes events from Pulsar | Pulsar fails to store events | B | IV | 5 | UnAcceptable | Implement CRC auth and log event actions | Blacklist IP of attacker and resecure vulnerable page |
| D-5 | Django Failure | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Django fails to route events to proper event handler | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-6 | Django Warning Failure | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Evently | Django sends erroneous warnings to Evently | B | III | 3 | UnAcceptable | Use cookies and sessions for site identification | Redirect to the right site |
| D-7 | Django Null Dest. Airport | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant dest. airport | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-8 | Django Null Gate | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant gate | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-9 | Django Null Runway | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant runway | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-10 | Django Null Airline | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant airline | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-11 | Django Null Plane | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant plane | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| D-12 | Django Null Src. Airport | Invallid site executes Man-in-the-Middle (MITM) attack & sends mismatched event key-values to Django | Event nonexistant src. airport | B | I | 2 | Acceptable | Implement message inspection logic in Django | discard invallid mesages via immediate Pulsar ack & Write Caution in .log |
| 0 |  |  |  |  |  |  |  |  |  |
| DB-1 | Database | Database goes down | Application crushes | C| I | 1 | UnAcceptable |Gracefully handle errors untill either the same or a duplicate database is up and running | Restart both database and server |
| S-1 | server | Derver failure | Application inaccessible | C| I | 1 | UnAcceptable | Set notification for when server is down | Restart the server|