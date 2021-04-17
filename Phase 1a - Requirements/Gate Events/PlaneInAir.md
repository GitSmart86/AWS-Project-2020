# Plane in Air 

|Function|Report plane's departure|
|:-------|:----------|
|Description|A user with the right permissions changes a plane's current location in the system to indicate that the plane is in the air |
|Input |Current Airport Name, Destination Airport Name, Plane's Current Location|
|Source | User|
|Output |A new plane location is reflected in the system, with the plane name and destination indicated|
|Action|The user changes the planes current location in the system to indicate that it is in the air. The system allows the user to check the plane n air checkbox. The planes current location value changes to plane in air.|  
|Requires|Current Airport Name, Destination Airport Name, Plane's Current Location|
|Precondition|The user needs to be logged in. Airplane should be off in the air for this change to be made.  
|Postcondition|The planes's current location in the system is changed. 
|side effects|The gate and runway at the airport the plane is coming from can now be reassigned to other planes|
