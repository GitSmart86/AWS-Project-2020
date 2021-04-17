| Function | Delete - Airline |
| --------------- | --------------- |
| Description | An authenticated user deletes a new airline. |
| Inputs | Host Airport (x1), Airline Name (x1) |
| Source | User |
| Outputs | An airline removed from the database |
| Action | The system takes two pieces of information: the host airport and airline name. It first checks to ensure the airport exists and then it confirms the airline to be saved does exist. If both required checks are valid, the airline is removed from the database. The user deleting the airline is also recorded. |
| Requires | Host Airport, Airline Name |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport airline count has decreased by one, and a airline with the given name no longer exists for the given airport. |
| Side Effects | None |