| Function | List - Gate |
| --------------- | --------------- |
| Description | An authenticated user asks for a list of all of the gates in an airport. |
| Inputs | Airport Name(1x) |
| Source | User |
| Outputs | A list of the gates in the specified airport. |
| Action | The system takes the airport that was entered and then ensures that the airport exists. If it does, then the system searches the database for all gates that are in the specified airport and outputs a list of the gates and information about the gates. Otherwise the system outputs an empty list. |
| Requires | The name of the airport |
| Precondition | None |
| Postcondition | The user has a list of all of the gates in an airport. |
| Side Effects |None |