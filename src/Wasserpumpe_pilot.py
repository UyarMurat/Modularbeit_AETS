# Mit Tastendruck Pin auf High setzen, nochmaliges Drücken auf Low (Toggle-Effekt)
# Pin 17

import RPi.GPIO as GPIO
import time
import keyboard

# Pin-Konfiguration
Output_Pin = 17

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(Output_Pin, GPIO.OUT)

# Zustand zu Beginn
state = False
GPIO.output(Output_Pin, state)

#print("Aktion: Drücke die W-Taste zum Umschalten von GPIO 17 (STRG+C zum Beenden)")

try:
    while True:
        if keyboard.is_pressed('w'):
            state = not state
            GPIO.output(Output_Pin, state)
            #print(f"Pin 17 ist jetzt auf {'HIGH' if state else 'LOW'}")

            # Warten, bis die Taste losgelassen wird
            while keyboard.is_pressed('w'):
                time.sleep(0.05)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nBeende Programm...")

finally:
    GPIO.cleanup()