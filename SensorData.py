import firebase_admin
import time
import keyboard

from firebase_admin import credentials,db
cd = credentials.Certificate("C:/Users/HP/Downloads/sensordb-500ca-firebase-adminsdk-svquu-db21988abe.json")

firebase_admin.initialize_app(cd, { 'databaseURL': 'https://sensordb-500ca.firebaseio.com/'})

while 1:
    
    #i=0.5
    #while i<=1:
        #time.sleep(i)
    
    ref = db.reference('Senso')
    data = ref.get()

    print(data)

    if(int(data['yAccel']) < -4):
        keyboard.press_and_release('up')
    elif(int(data['yAccel']) > 4):
        keyboard.press_and_release('down')
    elif(int(data['xAccel']) > 4):
        keyboard.press_and_release('left')
    elif(int(data['xAccel']) < -4):
        keyboard.press_and_release('right') 
             
    time.sleep(0.5)
    #    print(i)
    #   i= i + 0.5
