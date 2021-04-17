# At runway 

|Function|Report a plane's arrival at runway|
|:-------|:----------|
|Description|A user with the right permissions changes a plane's current location in the system to indicate that the plane has hit the runway |
|Input |Airplane Name, Airport Name, Runway Name, Arrival Time|
|Source | user|
|Output |A new plane location is reflected in the system|
|Action|The user changes the plane's current location in the system to indicate that it has arrived at the runway|  
|Requires|Airport, Runway Name, Airplane Name|
|Precondition|The user should be logged into the system. The airplane should be at the runway for this change to be made| 
|Postcondition|The planes's current location in the system is changed. 
|side effects|This particular runway cannot be used by another plane before the current plane one is off|
