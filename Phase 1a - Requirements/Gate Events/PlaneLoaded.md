# Plane Loaded 

|Function|Plane loaded status check|
|:-------|:----------|
|Description|A user with the right permissions changes a plane's current status to plane loaded |
|Input |Plane loaded status check|
|Source | User|
|Output |The plane's status in the system indicates that it is loaded|
|Action|The user logs in to the system and pulls up informaton for that perticular plane. The user then changes the status field by  checking the plane loaded status. |  
|Requires|Airport Name, Gate Name, Airplane Name, Number of Passengers|
|Precondition|The user needs to be logged in. The  airplane should be at the runway for this change to be made. 
|Postcondition|The planes's current location in the system is changed| 
|side effects|NA|
