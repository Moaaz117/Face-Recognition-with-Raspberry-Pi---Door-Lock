from gpiozero import Servo
from time import sleep

# GPIO17 pinini kullanarak servo motoru başlatıyoruz
servo = Servo(18)


# Servo motoru 180 derece hareket ettirme
while True:
    servo.value = -1 #kapatma
    sleep(1)
    servo.value = 1 #açma
    sleep(1)

