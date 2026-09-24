# Willkommen zu meinem piTelex-contrib

Hier sammle ich Anpassungen und anderes, was ich rund um piTelex mal entwickelt habe, in der Hoffnung, dass der eine oder andere piTelex-Nutzer mit der einen oder anderen Sache etwas anfangen kann, und -nicht zu vergessen- damit ich die Sachen bei Bedarf auch selbst wiederfinde :-)

## piTelex-Hardware für TW39


- #### Kombi-Platine für Linienstrommaschinen mit und ohne Fernschaltgerät

  jumper-konfigurierbar für Betrieb mit/ohne FSG

  - [TW39-Platine](TW39/Kombiversion/TW39-mit-Powersave) für einen RaspBerry Pi mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung.
  - [TW39-Stromversorgung](TW39/Kombiversion/Stromversorgung-für-TW39-mit-Powersave) dazu passend, mit Powersave-Unterstützung.
  - [Aufbaubeispiel mit Steckernetzteil und Kleinspannung](TW39/Kombiversion/Aufbaubeispiel/README.md)



- #### als Fernschaltgerät-Ersatz für Linienstrommaschinen mit 24V-LED-Treiber

  * [TW39-Platine](TW39/Ohne-FSG/TW39-ohne-FSG-mit-Powersave) für einen RaspBerry Pi als vollwertiger FSG-Ersatz mit Powersave-Funktion sowohl für die 230V-Versorgung als auch für die Linienstromversorgung

  * [TW39-Stromversorgung](TW39/Ohne-FSG//Stromversorgung-für-TW39-ohne-FSG-mit-Powersave) mit reduzierter Linienspannung, dazu passend. 

  * [Aufbaubeispiel mit Steckernetzteil und Kleinspannung](TW39/Ohne-FSG/Aufbaubeispiel/)

- #### [Adapterplatinchen zum Anschluss eines Tastwahlblocks](TW39/TWB/)



- ####  für V.10
  * [V.10-Platine](V10/V.10-3-mit-Powersave) für die Anbindung von TeKaDe FS200/FS220 mit Powersave-Funktion

  * [V.10-Stromversorgung](V10/V.10-3-Stromversorgung-mit-Powersave) dazu passend, mit Powersave-Unterstützung für die 230V-Versorgung.

  * [Aufbaubeispiel](V10/Aufbaubeispiel/README.md)





**Fragen oder Anregungen gerne an `telex(at)freenet.de`.**

**Da bei meinem PCB Hersteller immer eine Mindestabnahme gilt, und ich selber die Platinen nicht alle "verbrauchen" kann, gebe ich vorhandenes Material gerne weiter. Bei Interesse einfach nachfragen!**




## Software: RPi-Image mit piTelex

- #### RPi-Image mit piTelex

  Zu den o.a. Hardware-Varianten  [passendes Software-Image](./soft/rpi-image/README.md) für RaspBerry Pi's. Es enthält ein fertig vorinstalliertes und lauffähiges piTelex.
  

- #### Device modul für LCD1602 Display

  Statt der LEDs ein [zweizeiliges LCD](./soft/LCD1602/README.md)  **mit Rufnummernanzeige**



## HOWTOS und so...

Unter [HOWTO](HOWTO) ...passenderweise :-)
