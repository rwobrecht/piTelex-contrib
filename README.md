# Willkommen zum piTelex-contrib

Hier sammle ich Anpassungen und anderes, was ich rund um piTelex mal entwickelt habe, in der Hoffnung, dass der eine oder andere piTelex-Nutzer mit der einen oder anderen Sache etwas anfangen kann, und -nicht zu vergessen- damit ich die Sachen bei Bedarf auch selbst wiederfinde :-)


## 1) Hardware für TW39
* #### Version 1
  Erster Versuch, simple einseitige Leiterbahnführung im 1/10-Zoll Raster, passend auch für LoRa-Platinen
    * [TW39-Platine](TW39/V1/TW39-mit-Powersave) für einen RaspBerry Pi Zero W mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung.
    * [TW39-Stromversorgung](TW39/V1/Stromversorgung-für-TW39-mit-Powersave) dazu passend, mit Powersave-Unterstützung. 
  
* #### Version 2 --> Für Neubauten besser V3 nehmen wegen I2C-Bus <--
  Gegenüber V1 kompakteres Layout und verbesserte Anordnung der Stecker, funktional identisch mit V1
  
    * [TW39-Platine](TW39/V2/TW39-mit-Powersave) für einen RaspBerry Pi mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung.
    * [TW39-Stromversorgung](TW39/V2/Stromversorgung-für-TW39-mit-Powersave) dazu passend, mit Powersave-Unterstützung.

* ### Version 3
  <u>**Gegenüber V2 geänderte GPIO-belegung(!)**</u>, damit I2C zugänglich bleibt (Pins 3 und 5); funktional identisch mit V1/V2
    * [TW39-Platine](TW39/V3/TW39-mit-Powersave) für einen RaspBerry Pi mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung.
    * [TW39-Stromversorgung](TW39/V3/Stromversorgung-für-TW39-mit-Powersave) dazu passend, mit Powersave-Unterstützung.


## 2) piTelex als Fernschaltgerät-Ersatz für Linienstrommaschinen
* [TW39-Platine](TW39/Ohne-FSG/TW39-ohne-FSG-mit-Powersave) für einen RaspBerry Pi als vollwertiger FSG-Ersatz mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung
* [TW39-Stromversorgung](TW39/Ohne-FSG//Stromversorgung-für-TW39-ohne-FSG-mit-Powersave) mit reduzierter Linienspannung, dazu passend. 


## 3) Hardware für V.10

* [V.10-Platine](V10/V.10-3-mit-Powersave) für die Anbindung von TeKaDe Fs200/FS220 mit Powersave-Funktion
* [V.10-Stromversorgung](V10/V.10-3-Stromversorgung-mit-Powersave) dazu passend, mit Powersave-Unterstützung für die 230V-Versorgung.

**Fragen oder Anregungen gerne an `telex(at)freenet.de`.**

**Da bei meinem PCB Hersteller immer eine Mindestabnahme gilt, und ich selber die Platinen nicht alle "verbrauchen" kann, gebe ich vorhandenes Material gerne weiter. Bei Interesse einfach nachfragen!**


## 4) RPi-Image dazu passend

Zu den o.a. Hardware-Varianten gibt es ein [passendes Software-Image](./soft/README.md) für RaspBerry Pi's. Es enthält ein fertig vorinstalliertes und lauffähiges piTelex.
