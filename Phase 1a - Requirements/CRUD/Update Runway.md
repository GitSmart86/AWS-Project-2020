| Function | Update - Runway |
| --------------- | --------------- |
| Description | An authenticated user edits a runway for an existing airport. |
| Inputs | Airport (x1), Runway Name (x1), Size (x1) |
| Source | User |
| Outputs | A Runway's attribute(s) is changed and Persisted to the Database |
| Action | The system takes two pieces of information: the airport and runway name. It first checks to ensure the airport exists, and then it confirms the runway to be edited does exist. If both required checks are valid, the runway's new attribute(s) is persisted to the database (with a unique identifier remaining unchanged). The user editing the runway is also recorded. |
| Requires | Airport, Runway Name, Runway Size |
| Precondition | An authorized user is logged in and a preexisting runway exists. |
| Postcondition | None |
| Side Effects | None |
