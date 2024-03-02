import RPi.GPIO as GPIO  
if GPIO.RPI_REVISION == 1:  
    ports = [0, 1, 21]  
elif GPIO.RPI_REVISION == 2:  
    ports = [2, 3, 27]  
else:  
    ports = ["whatever the new changes will be"]  
print "Your Pi is a Revision %s, so your ports are: %s" % (GPIO.RPI_REVISION, ports)
