| Function      | Warning - Wrong Airport |
| ------------- | ----------------------- |
| Description   | An airplane is sent to an airport that does not host the airplane's owner airliner. |
| Inputs        | None |
| Source        | None |
| Outputs       | Alarm Notification |
| Action        | An airplane is assigned to a destination airport. The system checks to confirm that the given airport hosts the given airplanes's owner airline. If confirmation fails, this given plane is not assigned to the destination airport in question, and an alerting notification is posted and logged. |
| Requires      | Airplane, Intended Airport |
| Precondition  | None |
| Postcondition | Alarm notification is posted and logged. |
| Side Effects  | None |