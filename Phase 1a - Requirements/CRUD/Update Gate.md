| Function | Update - Gate |
| --------------- | --------------- |
| Description | An authenticated user edits a gate for an existing airport. |
| Inputs | Airport (x1), Gate Name (x1), Size (x1) |
| Source | User |
| Outputs | A gate's attribute(s) is changed and persisted to the database |
| Action | The system takes two pieces of information: the airport and gate name. It first checks to ensure the airport exists, and then it confirms the gate to be edited does exist. If both required checks are valid, the gate's new attribute(s) is persisted to the database (with a unique identifier remaining unchanged). The user editing the gate is also recorded. |
| Requires | Airport, Gate Name, Gate Size |
| Precondition | An authorized user is logged in and a preexisting gate exists. |
| Postcondition | None |
| Side Effects | None |