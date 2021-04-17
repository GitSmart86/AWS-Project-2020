| Function | Update - Plane |
| --------------- | --------------- |
| Description | An authenticated user edits a plane for an existing airline. |
| Inputs | Plane (x1), Size (x1), Max Population (x1), Mother Airline (x1), Mother Airport (x1), Mother Airport Gate (x1) |
| Source | User |
| Outputs | A Plane's attribute(s) is changed and Persisted to the Database |
| Action | The system takes three pieces of information: the plane, mother airline, mother airport, and mother gate. It first checks to ensure that the mother airline, airport, and gate exists, and then it confirms that the afore mentioned mother attributes are occupied by the same given plane. If both checks are valid, the plane's new attribute(s) is persisted to the database (with a unique identifier being remaining unchanged). The user editing the runway is also recorded. |
| Requires | plane, plane size, plane max population, mother airline, mother airport, mother gate |
| Precondition | An authorized user is logged in and a preexisting plane exists. |
| Postcondition | None |
| Side Effects | None |