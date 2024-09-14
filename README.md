
# AccuKnox

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.





## What This Code Proves:

- Synchronous Signal Execution:
    
    1)The view prints the message "Instance saved. Waiting for signal..." only after the signal is processed.
    
    2)If signals were asynchronous, this message would be printed immediately without waiting for the signal handler to complete.

 - Signal and View Running in the Same Thread:

     1)Both the view and the signal handler print the thread ID using threading.get_ident(). If they print the same ID, this proves they are running in the same thread.

- Signal and View in the Same Database Transaction:

    1)The transaction.atomic() block ensures that any exception raised inside (like the one in the signal handler) causes the transaction to roll back. After running the code, the database should not contain the new MyModel instance if the transaction is rolled back successfully due to the exception in the signal handler.

    
## Screenshots

![Screenshot 1](https://github.com/Khushi-Bhatia/ResumeProcessor/blob/master/Screenshots/Screenshot%201.jpg)

![class Rectangle output- ](https://github.com/Khushi-Bhatia/ResumeProcessor/blob/master/Screenshots/Screenshot%201.jpg)



