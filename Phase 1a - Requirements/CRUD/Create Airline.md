| Function | Create - Airline |
| --------------- | --------------- |
| Description | An authenticated user creates a new airline. |
| Inputs | Host Airport (x1), Airline Name (x1) |
| Source | User |
| Outputs | An airline persisted to the database |
| Action | The system takes two pieces of information: the host airport and airline name. It first checks to ensure the airport exists and then it confirms the airline to be saved does not already exist. If both required checks are valid, the airline is persisted to the database (with a unique identifier being assigned to it). The user creating the airline is also recorded. |
| Requires | Host Airport, Airline Name |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport airline count has increased by one, and a airline with the given name now exists for the given airport. |
| Side Effects | None |