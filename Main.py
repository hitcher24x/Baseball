from Baseball import Baseball, Cnp
import configparser
import time

# reads configuration
configuration=configparser.ConfigParser()
configuration.read("parameters.cfg")

# parsing the parameters:
begin=int(configuration.get("Parameters","begin"))
end=int(configuration.get("Parameters","end"))
threshold=int(configuration.get("Parameters","threshold"))

# Runs the program with a timer
start= time.time()
baseball=Baseball(begin,end,threshold)
baseball.start_program()
print ("Program Ran in", round(time.time() - start,3), "seconds")
