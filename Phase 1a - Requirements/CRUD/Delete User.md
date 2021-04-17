| Function | Delete - User |
| --------------- | --------------- |
| Description | An authorized admin user deletes a new user, or if no admin users exist, a non-authenticated user deletes a new user. |
| Inputs | user name (x1), user type (x1) |
| Source | User |
| Outputs | A User removed from the Database |
| Action | The system takes two pieces of information: the user name and user type. It first checks to ensure the user name does not exist and then it confirms that the deleting user is an authorized admin user. However, if the database currently contains no admin users, it forgoes the requirement of the deleting user being an admin user. If both required inputs are valid, The user is removed from the database. The user deleting the old user is also recorded. |
| Requires | user, user name |
| Precondition | An authorized user is logged in, or no admin users exist in the database. |
| Postcondition | The user runway count has decreased by one, and a runway with the given name no longer exists for the given user. |
| Side Effects | None |