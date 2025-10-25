# RaspBerry Pi image für TW39 und V.10 Hardware

Passend zu den PCB Layouts in diesem Repository habe ich ein bootfähiges Image zusammengebaut mit den Eigenschaften

* 32bit (passt also für alle RPi inkl. ZeroW)
* Vorinstalliertes RPi-OS trixie (Debian 13 basierend)
* Vorinstalliertes und lauffähiges piTelex Release 2025-06
* Speicherkarte sollte 8GB oder größer sein

## Betriebssystem

Das image kann mittels [rpi-imager](https://www.raspberrypi.com/software/) auf die µSD-Karte geschrieben werden, bei Bedarf können hiermit auch vor dem Schreiben noch Einstellungen wie WLAN-Zugangsdaten oder hostname geändert werden (bitte nicht den usernamen ändern); alternativ geht natürlich auf linux-Rechnern auch

`dd if=/path/to/imagefile of=/dev/<Name des Blockgeräts>; sync`

Falls beim boot ein Netzwerk verfügbar ist (LAN), wird die Netzwerkeinbindung mit DHCP automatisch erledigt. Zugriff auf den RPi kann dann mittels ssh (Windows: `putty`) erfolgen. Ist kein LAN verfügbar, muss der erste Zugriff auf den RPi über Tastatur/Monitor erfolgen.  Voreingestellt ist

* hostname: pitelex
* user: pi
* passwort: telex

Mittels `sudo raspi-config` kann dann bei Bedarf der WLAN-Zugang, das Passwort, der hostname usw. angepasst werden.

## piTelex

### Erster Test

piTelex startet beim Boot automatisch (als systemd-Dienst, siehe https://github.com/fablab-wue/piTelex/wiki/SW_AutoStart). 
Die voreingestellte `telex.json` beinhaltet nur eine Minimal-Konfiguration aus Screen-, i-Telex- und log-Modul.

Mit Eingabe von `byobu<Enter>` an der Kommandozeile gelangt man in das laufende Screen-Modul und kann dort schonmal erste Verbindungstests durchführen:

`<ESC>AT<ENTER>` geht in die Wählbereitschaft, danach kann man eine i-telex-Nummer wählen. Ist der Teilnehmer erreichbar, sollte er sich mit der Datum-/Zeitgruppe melden. Die Verbindung wird mit `<ESC>ST<ENTER>` beendet. Mit `<F6>` verlässt man die `byobu`-Oberfläche und kehrt zur Konsole zurück.

### Fernschreibequipment anschließen

Für die Einbindung von Fernschreib-Hardware muss die `telex.json` entsprechend erweitert werden. Für die PCB-Layouts aus diesem Repository gibt es fertige telex.json-Varianten im Verzeichnis `/home/pi/piTelex-pool/config`. Um eine davon zu aktivieren, muss sie nur ins piTelex-Verzeichnis kopiert werden:

`cp ~/piTelex-pool/config/telex.json.XXXX ~/piTelex/telex.json`

Anschließend entweder piTelex neu starten: `sudo systemctl restart pitelex`

oder einfach neu booten: `sudo reboot`

## i-Telex

Senden von Telexen sollte bei bis hierher richtiger Konfiguration schonmal funktionieren.

Um für andere Teilnehmer erreichbar zu sein, braucht es einen Eintrag in den TNS. Hier helfen die Admins gerne weiter.
Die Daten müssen in der `telex.json`natürlich eingetragen werden, zum einen im Bereich i-Telex ( `"tns_dynip_number"` , `"tns_pin"`) und im Globalteil am Ende der `telex.json` die Option `"wru_id"`

Hat man keine IPv4-Adresse, muss man centralex verwenden: https://github.com/fablab-wue/piTelex/wiki/SW_DevITelexCentralex.
Zum Aktivieren genügt,es, im Bereich i-Telex der `telex.json` den Eintrag `"centralex": true,` hinzuzufügen.

## Download

Hier kommt der link zum Download für das Image: https://my.hidrive.com/share/rdk89-w562. (Die Datei ist zu groß für github...)

## Feedback

Rückmeldungen gerne an telex(at)freenet.de
