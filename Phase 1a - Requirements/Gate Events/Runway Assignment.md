# Runway Assignment 

|Function|Assign Runway|
|:-------|:----------|
|Description|A user with the right permissions assigns a runway to a plane|
|Input |Airplane Name, Aiport Name, Runway Name|
|Source | User|
|Output |Runway assignment persisted to the database|
|Action|The user enters three peieces of information. The runway to be assigned, the airplane to which it is to be  be assingned, and the airport. The system checks to ensure that this runway has not already been assigned to another plane for use at the exact same time.if so, the runway  assignment is persisted to the database with a unique identifier.The user assigning  the runway is recorded as well.  
|Requires|Airport Name, Runway Name, Airplane Name|
|Precondition|The user needs to be logged in. The airplane should be headed to the airport for be assigned a gate. 
|Postcondition|The number of available runways at that perticular airport, and at  that particular time  has decreased by one, and a new runway assignment has been added. 
|Side effects|This particular runway cannot be assigned to another plane for the exact sane time|
