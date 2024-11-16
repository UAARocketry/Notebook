Diagrams are in PlantUML format

To view diagrams, go to: https://app.diagrams.net/
Click the insert ('+') button on the right side of the tool bar
Hover over 'Advanced' at the end of the list
Click 'PlantUML...'
Replace text with desired diagram 
Click 'Insert'



### V1
@startuml
title LOX-IPA System Diagram

node "LOX Tank (50 psi)" as LOX
node "IPA Tank (50 psi)" as IPA
node "Helium Tank" as He
component "Check Valve (LOX)" as CV1
component "Control Valve (LOX)" as CV2
component "LOX Pump" as P1
component "Check Valve (IPA)" as CV3
component "Control Valve (IPA)" as CV4
component "IPA Pump" as P2
component "Injector" as IN
component "Combustion Chamber (300 psi)" as CC
component "Exhaust" as EX
component "Relief Valve (LOX)" as RV1
component "Relief Valve (IPA)" as RV2
component "Temperature Sensor" as T1
component "Pressure Transducer (LOX)" as PT1
component "Pressure Transducer (IPA)" as PT2
component "Pressure Transducer (Injector)" as PT3

LOX --> CV1
CV1 --> CV2
CV2 --> P1
P1 --> IN
IPA --> CV3
CV3 --> CV4
CV4 --> P2
P2 --> IN
He --> LOX
He --> IPA
IN --> CC
CC --> EX
CC --> RV1
CC --> RV2
CC --> T1
IN --> PT3
LOX --> PT1
IPA --> PT2
@enduml


### V2
@startuml
title Liquid Bi-Propellant Feed System

node "LOX Tank (600 psi)" as LOX
node "IPA Tank (600 psi)" as IPA
node "Helium Tank" as He
component "Manual Valve (LOX)" as MV1
component "Manual Valve (IPA)" as MV2
component "Solenoid Valve (LOX)" as SV1
component "Solenoid Valve (IPA)" as SV2
component "Inline Regulator (LOX)" as Reg1
component "Inline Regulator (IPA)" as Reg2
component "Check Valve (LOX)" as CV1
component "Check Valve (IPA)" as CV2
component "Relief Valve (LOX)" as RV1
component "Relief Valve (IPA)" as RV2
component "Pressure Transducer (LOX)" as PT1
component "Pressure Transducer (IPA)" as PT2
component "LOX Pump" as P1
component "IPA Pump" as P2
component "Injector" as IN
component "Combustion Chamber (300 psi)" as CC
component "Exhaust" as EX

LOX --> MV1
MV1 --> SV1
SV1 --> Reg1
Reg1 --> CV1
CV1 --> P1
P1 --> IN

IPA --> MV2
MV2 --> SV2
SV2 --> Reg2
Reg2 --> CV2
CV2 --> P2
P2 --> IN

He --> LOX : Pressurization
He --> IPA : Pressurization

IN --> CC
CC --> EX
CC --> RV1
CC --> RV2
CC --> PT1 : Monitoring
CC --> PT2 : Monitoring
@enduml