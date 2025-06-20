Hardware die benötigt wird, mit folgender Software

1. Raspberry PI --> Git Integration
2. Bash Integration vonnöten --> Startverhalten des PI damit bestimmen

Virtual Environment erstellen


Uhrzeit vonnöten --> über feste Uhrzeiten das Gießen bestimmen, über den Feuchtigkeitssensor im idealfall neu antriggern (import time wichtig)
Fernbedingung per App ?
Wichtig: E-Mail verschicken --> Vorschlag mit einer API

Idee mit API folgend Aufgebaut:

    import requests

    #Funktion mit E-Mail senden
    def send_mail():
        Domain = "raspbimail.de" #Zugang zur Website für API Zugriff
        Api_Key = "passwort" #Für jeden Zugriff wird ein spezieller Key benötigt


    return requests.post(
        f"https://....",
        authenticator = ("api", Api_Key),
        mail_data = {"from":
                    "to":
                    "Subject": "Status Gießvorgang",
                    "text": 
        } 
    )