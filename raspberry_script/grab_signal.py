import signal 
import time   


###########################################################

Sentry2 = True
# Create a Signal Handler for Signals.SIGINT:  CTRL + C
def SignalHandler_SIGTERM(SignalNumber,Frame):
    global Sentry2
    Sentry2 = False

signal.signal(signal.SIGTERM,SignalHandler_SIGTERM)

while Sentry2: #exit loop when Sentry = False
    print('SIGTERM continous event Eg,Read from sensor')
    time.sleep(1)

print('Out of the while loop')
print('Clean up code Here')
