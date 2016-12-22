import RPi.GPIO as GPIO #to use GPIO for relay control
import datetime, time #to keep track of time


CHECK_WAIT = 60 # 60 seconds = 1 minutes to check for time
GPI_OUT_PIN = 14 #GPIO out pin in BCM mode. GPIO pin number.

#BELOEW ARE TIMES FOR THE LIGHTS:
#Uses 24 hour clock
OFF_TIME = 22
ON_TIME_H = 16 #time to turn on hour
ON_TIME_M = 30 #time on off on minute


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPI_OUT_PIN,GPIO.OUT)

def get_cur_min():
        temp_t = datetime.datetime.now().time()
        return temp_t.minute

def get_cur_hour():
        temp_t = datetime.datetime.now().time()
        return temp_t.hour

def get_cur_second():
        temp_t = datetime.datetime.now().time()
        return temp_t.second
try:
        while(True):

                if(get_cur_hour() < OFF_TIME and (get_cur_hour() >= ON_TIME_H and get_cur_min() >=30)):
                        #print ("on " + str(get_cur_min()))#set GPIO to on #for debugging
                        GPIO.output(GPI_OUT_PIN,0)
                if(get_cur_hour() >= OFF_TIME or get_cur_hour() < ON_TIME_H):
                        #print("0ff " + str(get_cur_min())) #set GPIO to off #for debugging
                        GPIO.output(GPI_OUT_PIN,1)
                #print (get_cur_second()) #for debugging
                time.sleep(CHECK_WAIT) #check every CHECK_WAIT
except KeyboardInterrupt:
        GPIO.cleanup() #clean up the ports after keyboard interupt
