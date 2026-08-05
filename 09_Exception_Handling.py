#Exceotion Handline and File Processing
#Exception Handling: It is a mechanism used to detect, manage & respond to runtime errors that occur during program execution. Instead of terminating the program abruptly when an error occurs, Python prides structured exception-handling constructs that allow programs to continue operating graducally, provide meaningful error messages, perform cleanup activities and maintain application stability.    # Exception handling improves the program reliability , robustness, maintainability and user experiences by ensureing that unexpected situation are handled in a controlled manner.
# What is exception?An exception is an event that occurs during program execution & interrupts the normal flow of instructions.Exceptios typically arise when an operation can't be completed sucessfully due to any reason (invalid input, unavailable resource, incorrect data types)
# When an exception occurs, python creates an exception object & searches for an appropriate handler. If handler is found during the search, program execution stips and an error message is displayed.
# Benefits of Exception Handling
    # PRevent abrupt termination of programs.
    # Improves reliability of the application
    # Provide meaningful & user friendly error reporting.
    # Enables graceful recovery from erros.
    # Facilitates debugging & maintenance.
    # Supports resource cleanup & system stability
    # Improves user experience by hadling failures appropriately.
# Components of structured exception handling in Python
    # Try: Try block contains code that may potentially generate an exception during the program execution. 
    # Except Statement:The except block handles exceptions that occur within a corresponding try block.
    # Finally Statement: The finally block contains code that executes regardless of whether an exception occurs.
    # Raise Statment: The raise statement is used to deliberately generate an exception.
#Common Exceptions: 
    # ValueError
    # TypeError
    # IndexError
    # FileNotFoundError
