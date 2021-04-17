| Function | List - Plane |
| --------------- | --------------- |
| Description | An authenticated user asks for all planes that belong to a specific airline. |
| Inputs | Airline Name(1x) |
| Source | User |
| Outputs | A list of Planes in a specified airline. |
| Action | The system takes the airline that was entered and then ensures that the airline exists. If it does, then the system searches the database for all planes that are in the specified airline and outputs a list of the planes and information about the planes. Otherwise the system outputs an empty list. |
| Requires | The name of the airline |
| Precondition | None |
| Postcondition | The user has a list of all of the planes in a given airline. |
| Side Effects | None|