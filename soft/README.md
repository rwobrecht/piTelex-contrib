# RaspBerry Pi image für TW39 und V.10 Hardware
### Version vom 17.11.25 / gepatcht für ssh/password auth 25.11.25

Passend  zu den PCB Layouts in diesem Repository habe ich ein bootfähiges Image zusammengebaut mit den Eigenschaften

* 32bit (passt also für alle RPi inkl. ZeroW)
* Vorinstalliertes RPi-OS trixie (Debian 13 basierend)
* Vorinstalliertes und lauffähiges piTelex Release 2025-06
* µSD-Speicherkarte sollte 8GB oder größer sein

> [!TIP]
>
> Das Image kann natürlich auch mit anderer Hardware genutzt werden. Die mitgelieferten Beispiel-Konfigurationsdateien müssen dann lediglich an die verwendete Hardware angepasst werden.

---

## Betriebssystem

* Das image herunterladen (Downloadlink s.u.) und mittels [rpi-imager](https://www.raspberrypi.com/software/) analog zur [Anleitung im piTelex-wiki]( https://github.com/fablab-wue/piTelex/wiki/SW_imager) auf die µSD-Karte schreiben. 

>[!IMPORTANT]
> * Bitte die aktuelle Version des Imagers verwenden (>= 2.0.2).
> * Als Betriebssystem "Eigenes Image" anklicken (ganz runterscrollen) und das heruntergeladene image auswählen
> * Anpassungen des image (hostname, passwort, wlan,...) werden vom rpi-imager neuerdings bei Fremdimages leider nicht mehr unterstützt. Das muss dann nach dem ersten Einloggen mi dem RPi- Konfigurationstool `raspi-config` erfolgen (s.u.)

* Den RPi mit der so beschriebenen Karte booten.

* Falls beim boot ein Netzwerk verfügbar ist (LAN), wird die Netzwerkeinbindung mit DHCP automatisch erledigt. 
Der Zugriff auf den RPi kann dann mittels ssh (Windows: `putty`) erfolgen. 

* Ist kein LAN verfügbar, muss der erste Zugriff auf den RPi über Tastatur/Monitor erfolgen.

Für den Erstzugriff  sind folgende Einstellungen fest vorgegeben:

    * hostname: pitelex
    * user: pi  (muss zwingend "pi" sein und bleiben)
    * passwort: telex


- _**Bei Bedarf**_  können mit Hilfe des Konfigurationswerkzeugs
      `sudo raspi-config`
  
    * die Spracheinstellung, <br>_(Achtung: Bei der deutschen Tastatur liegt wegen der voreingestellten Standard-Lokale das `-` zunächst auf dem `ß` ...)_
    * der Rechnername,
    * das Passwort für den user pi,
    * die WLAN-SSID und das WLAN-Passwort
  
  konfiguriert werden.
- Die `root` -Partition ist knapp 4G groß und hat noch ca 800MB freien Platz. <br>
  _**Bei Bedarf**_  kann sie über sudo raspi-config
  im Menü `Advanced / Expand filesystem` vergrößert werden.

   

---


## piTelex

### Erster Test

**piTelex startet bei jedem Boot automatisch** als [systemd-Dienst](https://github.com/fablab-wue/piTelex/wiki/SW_AutoStart). 
Die voreingestellte `telex.json` beinhaltet nur eine Minimal-Konfiguration aus Screen-, i-Telex- und log-Modul.

Mit Eingabe von `byobu<Enter>` an der Kommandozeile gelangt man in das laufende [Screen-Modul](https://github.com/fablab-wue/piTelex/wiki/SW_DevScreen) und kann dort schonmal erste Verbindungstests durchführen:

* `<ESC>AT<ENTER>` geht in die Wählbereitschaft, danach kann man eine i-telex-Nummer eingeben.

* Ist der Teilnehmer erreichbar, sollte er sich mit der Datum-/Zeitgruppe melden.

* Eingabe von `@` sollte die Kennung des erreichten Teilnehmers zurückliefern, `#` die eigene Kennung (bis dato "12345 dummy d").

* An der Konsole getippter Text erscheint in rot und wird an die Gegenstelle gesendet. Von der Gegenstelle empfangener Text wird in schwarz bzw. weiß (je nach Konsole) wiedergegeben. 

* Mit `<ESC>ST<ENTER>` wid die Verbindung beendet.

* Mit `<F6>` verlässt man die `byobu`-Oberfläche und kehrt zur Konsole zurück.




### Fernschreibequipment anschließen

Für die Einbindung von Fernschreib-Hardware muss die `telex.json` entsprechend erweitert werden. Für die PCB-Layouts aus diesem Repository und für die SEU-M gibt es fertige telex.json-Varianten im Verzeichnis `/home/pi/piTelex-pool/config`. Um eine davon zu aktivieren, muss sie nur ins piTelex-Verzeichnis kopiert werden:

```bash
 cp ~/piTelex-pool/config/telex.json.XXXX ~/piTelex/telex.json
```

Anschließend entweder piTelex neu starten: 
    `sudo systemctl restart pitelex`
oder einfach neu booten: 
    `sudo reboot`

>[!NOTE]
>Sollte piTelex durch Fehlbedienung oder fehlerhafte `telex.json` beendet werden, versucht der systemd, den Dienst erneut nach 10 Sekunden zu starten. Wenn das gelingt, kann man auch wieder mit `byobu` das Screen-interface bedienen. Wenn nichts mehr hilft, hilft ein reboot; ggf. vorher eine funktionierende Variante der telex.json aktivieren... :-)
>
>Bitte **nicht** versuchen, `telex.py` "zu Fuß" zu starten, das überkreuzt sich mit dem systemd-Dienst und führt zu Fehlermeldungen, aber nicht zum Funktionieren :-)
---

## i-Telex

Senden von Telexen sollte bei bis hierher richtiger Konfiguration schonmal funktionieren.

Um für andere Teilnehmer erreichbar zu sein, braucht es einen Eintrag in den TNS. Hier helfen die Admins gerne weiter.
Die Daten müssen in der `telex.json`natürlich eingetragen werden, zum einen im Bereich i-Telex ( `"tns_dynip_number"` , `"tns_pin"`) und im Globalteil am Ende der `telex.json` die Option `"wru_id"`

Hat man keine IPv4-Adresse, muss man [centralex](https://github.com/fablab-wue/piTelex/wiki/SW_DevITelexCentralex) verwenden.
Zum Aktivieren genügt,es, im Bereich i-Telex der `telex.json` den Eintrag 

```json
  "centralex": true, 
```

hinzuzufügen.

---

## Download

### Update 02.01.2026

Es gibt ein neues Image mit aktualisiertem Betriebssystem (13.2) und dem neuen piTelex (2025-12):<br> [piTelex-2025-12_RPi.trixie-13.2-32bit-5G-260102.img.gz](https://mega.nz/file/1CtRUS6I#pVH1AhT80d8YevGjlHbM6CR7CRaaOCiU8coKFEG89I8)

Das alte Image ist noch verfügbar unter <br>[piTelex-2025-06_RPi.trixie-32bit-5G-251123.img.gz](https://mega.nz/file/hLlQWLiD#MkVyDqVeCHbYmpAjTb7-vlEV0U97UYQeqwxxEhi64NU) .
>[!NOTE]
>Die Dateien sind zu groß für github, sie liegen daher in meiner Cloud bei **mega.nz**

---

## Disclaimer

Ich hoffe, das Image funktioniert nicht nur bei mir, sondern auch bei anderen. Klar ist, dass es nur eine Basisfunktionalität für piTelex mitbringen kann. Für fortgeschrittenere Konfigurationen ist Lesen der passenden Wiki-Seiten Pflicht.

Und wie immer gilt: Benutzung der Software erfolgt auf eigene Gefahr...



## Feedback

Rückmeldungen gerne an telex(at)freenet.de oder in telexforum.de
