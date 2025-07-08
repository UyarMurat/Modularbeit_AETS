import RPi.GPIO as GPIO
import time

# Konfiguration
PUMP_GPIO = 17         # GPIO-Pin an dem das Relais/Pumpe angeschlossen ist
MEASURE_TIME = 10      # Zeit in Sekunden, wie lange die Pumpe laufen soll

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_GPIO, GPIO.OUT)

try:
    input(f"Bereit zum Messen? Stelle ein Gefäß unter die Pumpe und drücke Enter...")
    
    print(f"Pumpe startet für {MEASURE_TIME} Sekunden...")
    GPIO.output(PUMP_GPIO, GPIO.HIGH)  # Pumpe EIN
    time.sleep(MEASURE_TIME)
    GPIO.output(PUMP_GPIO, GPIO.LOW)   # Pumpe AUS
    print("Pumpe gestoppt.")

    print(f"\nJetzt misst du die Wassermenge (in ml), die in {MEASURE_TIME} Sekunden gepumpt wurde.")
    print("Teile dann einfach ml durch Sekunden, um die Förderrate zu berechnen (ml/s).")

finally:
    GPIO.cleanup()