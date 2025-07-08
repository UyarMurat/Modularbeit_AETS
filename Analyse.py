import json
import statistics
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


#.env-Datei laden
load_dotenv()

#Umgebungsvariablen lesen
absender_email = os.environ.get("MAIL_USER")
passwort = os.environ.get("MAIL_PASS")

empfaenger_email = ["ssaglam@hm.edu", "i.selimi@hm.edu", "muyar@hm.edu"]


#Variante 1: Speichern der Messdaten in Form einer JSON, diese werden initial eingelesen für die Berechnung der Varianz
with open('messdata.json', 'r') as file:
    data_obj = json.load(file)
#print(data_obj)

#Variante 2: Speichern der Messdaten in Form einer Textdatei oder als csv --> noch offen

#Berechnen der Varianz, anhand der Gießmengen von bis zu 6 durchgeführten Bewässerungen, von der JSON File
#extrahieren der ml-Werte
ml_values = []
for eintrag in data_obj["Messtage"]:
    for key, value in eintrag.items():
        if key == "ml":
            zahl = int(value.replace("ml", ""))
            ml_values.append(zahl)

#Berechnung der Varianz
varianz = statistics.variance(ml_values)
#print(f"ml-Werte: {ml_values}")
#print(f"Standardvarianz der ml-werte: {varianz}")

#Berechnung der Standardabweichung
standardabweichung = statistics.stdev(ml_values)
#print(f"Standardabweichung: {standardabweichung}")


#Daten für den Bericht -- Messdaten
bericht = f"""\
Messdaten Report – Strelitzia

ml-Werte: {ml_values}
Varianz: {varianz:.2f}
Standardabweichung: {standardabweichung:.2f}
"""
#Vorbereitung der Mail
msg = MIMEMultipart()
msg["From"] = absender_email
msg["To"] = ", ".join(empfaenger_email)
msg["Subject"] = "Bewässerungsreport – Strelitzia"
msg.attach(MIMEText(bericht, "plain"))

# Versand über gmail
smtp_server = "smtp.gmail.com"
smtp_port = 465

try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # SSL direkt
    print(f"Passwort geladen: {passwort is not None}")
    print(f"Benutzer: {absender_email}")
    server.login(absender_email, passwort)
    server.send_message(msg)
    server.quit()
    print("✅ E-Mail erfolgreich gesendet.")
except Exception as e:
    print("❌ Fehler beim E-Mail-Versand:")
    print(e)