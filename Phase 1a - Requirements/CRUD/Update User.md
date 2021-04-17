| Function | Update - User |
| --------------- | --------------- |
| Description | An authorized admin user edits another user, or if no admin users exist, a non-authenticated user edits another user. |
| Inputs | user name (x1), user type (x1) |
| Source | User |
| Outputs | A User's attribute(s) is changed and Persisted to the Database |
| Action | The system takes two pieces of information: the user name and user type. It first checks to ensure the edited user does exist, and then it confirms that the creating user is an authorized admin user. However, if the database currently contains no admin users, it forgoes the requirement of the creating user being an admin user. If both required inputs are valid, The user's new attribute(s) is persisted to the database (with a unique identifier being remaining unchanged). The user editing the new user is also recorded. |
| Requires | user, user name |
| Precondition | ( An authorized user is logged in, or no admin users exist in the database ) and second user to be edited also exists |
| Postcondition | None |
| Side Effects | None |