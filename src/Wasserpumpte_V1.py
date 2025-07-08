# V1 mit input

import RPi.GPIO as GPIO

PIN = 17
state = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, state)

print("Drücke ENTER zum Umschalten, STRG+C zum Beenden")

try:
    while True:
        input()  # wartet auf ENTER
        state = not state
        GPIO.output(PIN, state)
        print(f"GPIO17 ist jetzt {'HIGH' if state else 'LOW'}")

except KeyboardInterrupt:
    print("Beende...")
finally:
    GPIO.cleanup()