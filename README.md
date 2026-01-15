# CS-4700-project1

# Plan

Go through documentation to connect to server and diff ports, setup communication between client and server and get IDs and setup stubs
Condition support for ports (abstract?)

Helper methods for each message response from server
- hello: 
- start: 
- guess: random best word guess (likely just random word because most words in list aren't real words)
- retry: alphabet list of characters, if 0 remove char from alphabet list, if 2 keep char for next guess, if 1 shift to right (edge move to start), loop until bye, limit, or error
- bye: 

Makefile with flags to test
