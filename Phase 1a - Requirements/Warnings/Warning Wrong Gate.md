| Function      | Warning - Wrong Gate |
| ------------- | -------------------- |
| Description   | An airplane is assigned to a gate too small for its size. |
| Inputs        | None |
| Source        | None |
| Outputs       | Alarm Notification |
| Action        | An airplane is assigned to dock at a given airport's gate. The system checks to confirm that given gate is >= in size to the given plane. If confirmation fails, this given plane is not assigned to the gate in question, and an alerting notification is posted and logged. |
| Requires      | Airplane, Intended Gate |
| Precondition  | None |
| Postcondition | Alarm notification is posted and logged. |
| Side Effects  | None |
