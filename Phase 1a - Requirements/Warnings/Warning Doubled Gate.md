| Function      | Warning - Doubled Gate |
| ------------- | -------------------- |
| Description   | An airplane is assigned to a runway that is currently already in use. |
| Inputs        | None |
| Source        | None |
| Outputs       | Alarm Notification |
| Action        | An airplane is assigned to dock at a given airport's gate. The system checks to confirm that the selected runway is not already in use by any another plane. If confirmation fails, this given plane is not assigned to the gate in question, and an alerting notification is posted and logged. |
| Requires      | Airplane, Intended Gate |
| Precondition  | None |
| Postcondition | Alarm notification is posted and logged. |
| Side Effects  | None |
