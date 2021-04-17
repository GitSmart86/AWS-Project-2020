| Function | Delete - Gate |
| --------------- | --------------- |
| Description | An authenticated user deletes a new gate for an existing airport. |
| Inputs | Airport (x1), Gate Name (x1), Size (x1) |
| Source | User |
| Outputs | A gate removed from the database |
| Action | The system takes two pieces of information: the airport and gate name. It first checks to ensure the airport exists and then it confirms the gate to be saved does exist. If both required checks are valid, the gate is removed from the database. The user deleting the gate is also recorded. |
| Requires | Airport, Gate Name, Gate Size |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport gate count has decreased by one, and a gate with the given name no longer exists for the given airport. |
| Side Effects | None |