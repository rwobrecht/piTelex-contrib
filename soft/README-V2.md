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

Das image wird mittels [rpi-imager](https://www.raspberrypi.com/software/) analog zur [Anleitung im piTelex-wiki]( https://github.com/fablab-wue/piTelex/wiki/SW_imager) auf die µSD-Karte geschrieben. Dabei sind folgende Voreinstellungen nötig:

    * hostname: (nach Bedarf)
    * user: pi  (muss zwingend "pi" sein)
    * passwort: (nach Bedarf)
    * Bei Bedarf noch die WLAN-Zugangsdaten und locale-Einstellung
    * im Reiter "Dienste": ssh aktivieren mit Passwort-Auth

Falls beim boot ein Netzwerk verfügbar ist (LAN), wird die Netzwerkeinbindung mit DHCP automatisch erledigt. Zugriff auf den RPi kann dann mittels ssh (Windows: `putty`) erfolgen. Ist kein LAN verfügbar und kein WLAN konfiguriert, muss der erste Zugriff auf den RPi über Tastatur/Monitor erfolgen.

>[!IMPORTANT]
> Dieses Image ist mit der Einstellung `PasswordAuthentication yes` für den ssh-Zugang versehen.
>
>Wegen eines bugs im rpi-imager 1.9.6 kann es passieren, dass  entgegen der Einstellungen im imager das passwort-Auth nicht funktioniert.
>
>__WORKAROUND:__
>
> * entweder das erste login mit Tastatur und Monitor durchführen und mittels `sudo raspi-config` SSH einschalten:
>   
>      <img src="/img/rpi-cfg-3-IF.png" width="33%">
>      <img src="/img/rpi-cfg-I1.png" width="33%">
>      <img src="/img/rpi-cfg-ssh.png" width="33%">
>
> *  oder die frisch mit dem image beschriebene µSD-Karte im PC öffnen und in der zweiten Partition (`rootfs`) die Datei `/etc/ssh/sshd_config` in einen Texteditor der Wahl laden, die Zeile `PasswordAuthentication no` suchen und in `PasswordAuthentication yes` ändern. Darauf achten, dass die Zeile nicht mit `#` beginnt (Kommentarzeichen), sonst ist die Einstellung wirkungslos. Die Datei speichern (möglicherweise sind Admin-Rechte zum Speichern erforderlich). Die so gepatchte µSD-Karte sollte dann das Einloggen mit SSH/Passwort erlauben.<img src="/img/sshd_config.png" width="50%"> 
>
>

---


## piTelex

### Erster Test

**piTelex startet beim Boot automatisch** als [systemd-Dienst](https://github.com/fablab-wue/piTelex/wiki/SW_AutoStart). 
Die voreingestellte `telex.json` beinhaltet nur eine Minimal-Konfiguration aus Screen-, i-Telex- und log-Modul.

Mit Eingabe von `byobu<Enter>` an der Kommandozeile gelangt man in das laufende [Screen-Modul](https://github.com/fablab-wue/piTelex/wiki/SW_DevScreen) und kann dort schonmal erste Verbindungstests durchführen:

* `<ESC>AT<ENTER>` geht in die Wählbereitschaft, danach kann man eine i-telex-Nummer eingeben.

* Ist der Teilnehmer erreichbar, sollte er sich mit der Datum-/Zeitgruppe melden.

* Eingabe von `@` sollte die Kennung des erreichten Teilnehmers zurückliefern, `#` die eigene Kennung (bis dato "123456 dummy d").

* An der Konsole getippter Text erscheint in rot und wird an die Gegenstelle gesendet. Von der Gegenstelle empfangener Text wird in schwarz bzw. weiß (je nach Konsole) wiedergegeben. 

* Mit `<ESC>ST<ENTER>` wid die Verbindung beendet.

* Mit `<F6>` verlässt man die `byobu`-Oberfläche und kehrt zur Konsole zurück.

Sollte piTelex durch Fehlbedienung o.ä. beendet werden, startet der systemd den Dienst erneut nach 10 Sekunden. Dann kann man auch wieder mit `byobu` das Screen-interface bedienen. Wenn nichts mehr hilft, hilft ein reboot :-)


### Fernschreibequipment anschließen

Für die Einbindung von Fernschreib-Hardware muss die `telex.json` entsprechend erweitert werden. Für die PCB-Layouts aus diesem Repository und für die SEU-M gibt es fertige telex.json-Varianten im Verzeichnis `/home/pi/piTelex-pool/config`. Um eine davon zu aktivieren, muss sie nur ins piTelex-Verzeichnis kopiert werden:

```bash
 cp ~/piTelex-pool/config/telex.json.XXXX ~/piTelex/telex.json
```

Anschließend entweder piTelex neu starten: 
    `sudo systemctl restart pitelex`
oder einfach neu booten: 
    `sudo reboot`

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

Hier kommt der link zum Download für das Image: [piTelex-2025-06_RPi.trixie-32bit-5G-251123.img.gz](https://my.hidrive.com/lnk/H86hvNZwl).  (Die Datei ist zu groß für github...)

---

## Disclaimer

Ich hoffe, das Image funktioniert nicht nur bei mir, sondern auch bei anderen. Klar ist, dass es nur eine Basisfunktionalität für piTelex mitbringen kann. Für fortgeschrittenere Konfigurationen ist Lesen der passenden Wiki-Seiten Pflicht.

Und wie immer gilt: Benutzung der Software erfolgt auf eigene Gefahr...



## Feedback

Rückmeldungen gerne an telex(at)freenet.de oder in telexforum.de
