| Function | Delete - Plane |
| --------------- | --------------- |
| Description | An authenticated user deletes a new plane for an existing airline. |
| Inputs | Plane (x1) |
| Source | User |
| Outputs | A Plane removed from the Database |
| Action | The system takes three pieces of information: the plane, mother airline, mother airport, and mother gate. It first checks to ensure that the mother airline, airport, and gate exists, and then it confirms that the afore mentioned mother attributes are not already occupied. If both checks are valid, the plane is removed from the database and the given mother gate is updated to be docking the newly created plane. The user deleting the runway is also recorded. |
| Requires | plane |
| Precondition | An authorized user is logged in. |
| Postcondition | The airline's plane count count has decreased by one. |
| Side Effects | None |