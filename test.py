from dotenv import load_dotenv
import os

load_dotenv()  # .env-Datei laden

absender_email = os.getenv("MAIL_USER")
passwort = os.getenv("MAIL_PASS")

print(f"Passwort geladen: {passwort is not None}")
print(f"Benutzer: {absender_email}")