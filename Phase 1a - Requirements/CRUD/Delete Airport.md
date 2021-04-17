| Function | Delete - Airports |
| --------------- | --------------- |
| Description | An authenticated user deletes a new airport. |
| Inputs | Airport Name (x1) |
| Source | User |
| Outputs | An Airport removed from the Database |
| Action | The system takes one piece of information: the airport name. It confirms that the airport name exists, and it then confirms that the current user is an ATC user. If both required checks are valid, the airport is removed from the database. The user deleting the airport is also recorded. All of the children attributes and objects of the airport are also deleted, cascading style. |
| Requires | Airport Name |
| Precondition | An authorized user is logged in. |
| Postcondition | The net airport count has decreased by one, and an airport with the given location coordinates no longer exists. |
| Side Effects |  |