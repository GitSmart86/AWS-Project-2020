| Function | Create - Gate |
| --------------- | --------------- |
| Description | An authenticated user creates a new gate for an existing airport. |
| Inputs | Airport (x1), Gate Name (x1), Size (x1) |
| Source | User |
| Outputs | A gate persisted to the database |
| Action | The system takes two pieces of information: the airport and gate name. It first checks to ensure the airport exists and then it confirms the gate to be saved does not already exist. If both required checks are valid, the gate is persisted to the database (with a unique identifier being assigned to it). The user creating the gate is also recorded. |
| Requires | Airport, Gate Name, Gate Size |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport gate count has increased by one, and a gate with the given name now exists for the given airport. |
| Side Effects | None |