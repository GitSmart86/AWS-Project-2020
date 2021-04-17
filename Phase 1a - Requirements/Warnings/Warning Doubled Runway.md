| Function      | Warning - Doubled Runway |
| ------------- | -------------------- |
| Description   | An airplane is assigned to a runway that is currently already in use. |
| Inputs        | None |
| Source        | None |
| Outputs       | Alarm Notification |
| Action        | An airplane is assigned to takeoff/land on a given airport's runway. The system checks to confirm that the selected runway is not and will not be in use by any another plane during this given plane's takeoff/landing. If confirmation fails, this given plane is not assigned to the runway in question, and an alerting notification is posted and logged. |
| Requires      | Airplane, Intended Runway |
| Precondition  | None |
| Postcondition | Alarm notification is posted and logged. |
| Side Effects  | None |
