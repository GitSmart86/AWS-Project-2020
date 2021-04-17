| Function | Create - Airports |
| --------------- | --------------- |
| Description | An authenticated user creates a new airport. |
| Inputs | Airport Name (x1), Location Coordinates (x1) |
| Source | User |
| Outputs | An Airport Persisted to the Database |
| Action | The system takes one piece of information: the airport name. It confirms that the airport name and its corresponding coordinates do not already exist, and it then confirms that the current user is an ATC user. If both required checks are valid, the airport is persisted to the database (with a unique identifier being assigned to it). The user creating the airport is also recorded. The new airport can have its airlines, gates, and planes added by utilizing the other respective CRUD functions available for this system. |
| Requires | Airport Name, Location Coordinates |
| Precondition | An authorized user is logged in. |
| Postcondition | The net airport count has increased by one, and an airport with the given location coordinates now exists. |
| Side Effects |  |