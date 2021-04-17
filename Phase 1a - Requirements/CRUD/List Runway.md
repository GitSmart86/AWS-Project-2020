| Function | List - Runway |
| --------------- | --------------- |
| Description | An authenticated user asks for all runways that belong to a specific airport. |
| Inputs | Airport Name(1x) |
| Source | User |
| Outputs | A list of runways in a specified airport. |
| Action | The system takes the airport that was entered and then ensures that the airport exists. If it does, then the system searches the database for all runways that are in the specified airport and outputs a list of the runways and information about the runways. Otherwise the system outputs an empty list. |
| Requires | The name of the airport |
| Precondition | None |
| Postcondition | The user has a list of all of the runways in a given airport. |
| Side Effects | None|