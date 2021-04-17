| Function | Create - Plane |
| --------------- | --------------- |
| Description | An authenticated user creates a new plane for an existing airline. |
| Inputs | Plane (x1), Size (x1), Max Population (x1), Mother Airline (x1), Mother Airport (x1), Mother Airport Gate (x1) |
| Source | User |
| Outputs | A Plane Persisted to the Database |
| Action | The system takes three pieces of information: the plane, mother airline, mother airport, and mother gate. It first checks to ensure that the mother airline, airport, and gate exists, and then it confirms that the afore mentioned mother attributes are not already occupied. If both checks are valid, the plane is persisted to the database and the given mother gate is updated to be docking the newly created plane (with a unique identifier being assigned to it). The user creating the runway is also recorded. |
| Requires | plane, plane size, plane max population, mother airline, mother airport, mother gate |
| Precondition | An authorized user is logged in. |
| Postcondition | The airline's plane count count has increased by one, and the mother gate is now docking the newly created plane. |
| Side Effects | None |