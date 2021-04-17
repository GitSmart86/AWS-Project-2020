#                                                      At Gate 

|Function|Report plane arrival at gate|
|:-------|:----------|
|Description|A user with the right permissions changes a plane's current location in the system to indicate that the plane has arrived at the Gate |
|Input |Airplane Name, Airport Name, Gate Name|
|Source | User|
|Output |A new plane location is reflected in the system|
|Action|The authenticated user changes the plane's current location in the system to indicate arrival at gate|  
|Requires|Airport Name, Gate Name, Airplane Name|
|Precondition|User needs to be logged in. Airplane should be at gate for this change to be made. 
|Postcondition|The planes's current location in the system is changed. 
|side effects|This particular gate cannot be assigned to another plane until the current plane leaves|
