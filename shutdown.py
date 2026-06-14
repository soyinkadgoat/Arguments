def ShutDown():
    print("Computer shut down successfully.")

def DontShutDown():
    print("Shutdown successfully aborted.")

def DisplayError():
    print("Sorry")

shutdown = input("Do you want to shutdown your computer?: ")

if shutdown.lower() == 'yes':
    ShutDown()
elif shutdown.lower() == 'no':
    DontShutDown()
else:
    DisplayError()