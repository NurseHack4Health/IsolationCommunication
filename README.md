# IsolationCommunication

Creating virtual communication to end isolation anxiety in the care of COVID-19 patients. Currently nurses are using dry-erase boards or walkie talkies to communicate their needs when in a negative pressure room. 


Would like to find a solution through the use of existing infrastructure for nurses to be able to communicate virtually/hands free to their coworkers outside the room, and with themselves.


## App Description

App leverages power platform to create a unified, native UI for windows device, and a wed ui for Linux, Android or iOS/MacOS devices, and will leverage an azure function for cheap, and excellent speech to text capabilities, even *with* surgical masks as tested.

## Use

Import this package into [Powerapps](https://powerapps.microsoft.com/en-us/)

A guide is [available here](https://powerapps.microsoft.com/en-us/blog/powerapps-packaging/)

## ToDo (for real use)

1. Implement STT function on Azure
2. Additional testing in N95 masks
2. Save Notes in database
3. Database for login/LDAP integration for staff logins

... In general, this is (mostly) a wireframe, with some parts of the backend code implemented in the "Historical code section", but it's recommeded that you implement this in a more Azure native manner - rather than relying on python pacakages.

A SIP based IP calling server would likely need to be implemented too - unless we're only hooking this into Teams as just an in-organisation chat tool.

## Historical code and notes

A python based backend and **very** light UI has been implemented (only the TTS portion functions for now, but each function has working code in "methods.py", it just needs to be implemented.

Run ui.py to see the prototype.

CMU Sphinx is used for offline STT, Microsoft Zira/Alex is used for TTS (without extended GPU training, they're the best windows native options), a sample email to mailtrap as an mvp for a notetaking application.

