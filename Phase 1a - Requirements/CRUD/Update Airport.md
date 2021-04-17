| Function | Update - Airports |
| --------------- | --------------- |
| Description | An authenticated user edits an airport. |
| Inputs | Airport Name (x1), Location Coordinates (x1) |
| Source | User |
| Outputs | An Airport's attribute(s) is changed and Persisted to the Database |
| Action | The system takes one piece of information: the airport name. It confirms that the airport name and its corresponding coordinates do already exist, and it then confirms that the current user is an ATC user. If both required checks are valid, the airport's new attribute(s) is persisted to the database (with a unique identifier remaining the unchanged). The user editing the airport is also recorded. The new airport can have its airlines, gates, and planes edited by utilizing the other respective CRUD functions available for this system. |
| Requires | Airport Name, Location Coordinates |
| Precondition | An authorized user is logged in and a preexisting airport exists. |
| Postcondition | None |
| Side Effects |  |