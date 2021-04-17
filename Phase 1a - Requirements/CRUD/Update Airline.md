| Function | Update - Airline |
| --------------- | --------------- |
| Description | An authenticated user edits an airline. |
| Inputs | Host Airport (x1), Airline Name (x1) |
| Source | User |
| Outputs | An airline's attribute(s) is changed and persisted to the database |
| Action | The system takes two pieces of information: the host airport and airline name. It first checks to ensure the airport exists and then it confirms the airline to be edited does exist. If both required checks are valid, the airline's new attribute(s) is persisted to the database (with a unique identifier remaining unchanged). The user editing the airline is also recorded. |
| Requires | Host Airport, Airline Name |
| Precondition | An authorized user is logged in and a preexisting airplane exists. |
| Postcondition | None |
| Side Effects | None |