| Function | Create - Runway |
| --------------- | --------------- |
| Description | An authenticated user creates a new runway for an existing airport. |
| Inputs | Airport (x1), Runway Name (x1), Size (x1) |
| Source | User |
| Outputs | A Runway Persisted to the Database |
| Action | The system takes two pieces of information: the airport and runway name. It first checks to ensure the airport exists and then it confirms the runway to be saved does not already exist. If both required checks are valid, the runway is persisted to the database (with a unique identifier being assigned to it). The user creating the runway is also recorded. |
| Requires | Airport, Runway Name, Runway Size |
| Precondition | An authorized user is logged in. |
| Postcondition | The airport runway count has increased by one, and a runway with the given name now exists for the given airport. |
| Side Effects | None |