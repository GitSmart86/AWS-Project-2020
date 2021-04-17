# Gate Assignment 

|Function|Assign Gate|
|:-------|:----------|
|Description|A user with the right permissions assigns a gate to a plane|
|Input |Airplane Name, Airport Name, Gate Name|
|Source | User|
|Output |Gate assignment persisted to the database|
|Action|The user enters three peieces of information. The gate to be assigned, the airplane to which it is to be assingned, and the airport. The system checks to ensure that this gate has not already been assigned.if so, the gate assignment is persisted to the database.The user assigning the gate is recorded as well.  
|Requires|Airport Name, Gate Name, Airplane Name|
|Precondition|User needs to be logged in. Airplane should be headed to airport for it to be assigned a gate. 
|Postcondition|The number of available gates at that perticular airport has decreased by one, and a new gate assignment has been added. 
|side effects|This particular gate cannot be assigned to another plane in the same time period|
