| Function      | Warning - Wrong Runway |
| ------------- | ---------------------- |
| Description   | An airplane is assigned to a runway too small for its size. |
| Inputs        | None |
| Source        | None |
| Outputs       | Alarm Notification |
| Action        | An airplane is assigned to takeoff/land on a given airport's runway. The system checks to confirm that given runway is >= in size to the given plane. If confirmation fails, this given plane is not assigned to the runway in question, and an alerting notification is posted and logged. |
| Requires      | Airplane, Intended Runway |
| Precondition  | None |
| Postcondition | Alarm notification is posted and logged. |
| Side Effects  | None |
