# uml-generator-for-python-classes

This script implements a lightweight tracing utility to visualize the sequence of function and class calls during program execution. 
It is especially useful for understanding or debugging the flow of method calls in object-oriented code. 
Initial code was learned from Stackoverflow, later i did minor tweaking to make it more user friendly.

Key Components
SequenceOn class
Logs the flow of function calls between classes.

Uses Python’s sys._getframe() to inspect who is calling what.

Prints out helpful trace messages showing:

The caller and callee class names

The function name

Whether the call is coming from a different class (++ marker)

Also supports note() to print custom messages and __del__() to log when a class is done.

SequenceOff class
A placeholder class that disables all tracing.

Has the same interface as SequenceOn but does nothing.

Useful for toggling trace logging on/off globally.

Example Usage

Seq = SequenceOn  # Enable logging
# Seq = SequenceOff  # Disable logging

s = Seq()
s.note("Custom log message")


In Action
When run, the program defines classes A and B.
It calls methods that create SequenceOn instances, and the tracing system logs the sequence of calls and returns like so:

Your IDE console shows below, Now go to ------ >  https://www.plantuml.com/ , And copy paste printed IDE console from below to plantuml site

autonumber
 -> A ++ :funcA
A -> B ++ :funcB1
A -> B ++ :funcB2
note over B:calling private method
B -> B :__funcB22
A <-- B -- 

