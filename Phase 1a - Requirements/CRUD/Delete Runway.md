| Function | Delete - Runway |
| --------------- | --------------- |
| Description | An authenticated user deletes a new runway for an existing airport. |
| Inputs | Airport (x1), Runway Name (x1), Size (x1) |
| Source | User |
| Outputs | A Runway removed from the Database |
| Action | The system takes two pieces of information: the airport and runway name. It first checks to ensure the airport exists and then it confirms the runway to be saved does not already exist. If both required checks are valid, the runway is removed from the database. The user deleting the runway is also recorded. |
| Requires | Airport, Runway Name, Runway Size |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport runway count has decreased by one, and a runway with the given name no longer exists for the given airport. |
| Side Effects | None |