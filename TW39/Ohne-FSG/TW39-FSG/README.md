# Museumstaugliches piTelex-FSG

## Die Motivation

In Museen und bei manchen Ausstellungen sind elektrotechnische Selbstbaugeräte ohne Zertifizierung nach diversen Normen nicht zugelassen. Dies betrifft insbesondere die Netzspannungsebene. Geräte, die nur [Kleinspannung](https://de.wikipedia.org/wiki/Kleinspannung) verwenden (max 50V~ / 120V=) können da ein Ausweg sein.

## Die Idee

Sozusagen als "proof of concept" habe ich ein piTelex aufgebaut, das als FSG-Ersatz für eine Linienstrommaschine arbeitet. 
Die Stromversorgung wird durch ein zertifiziertes Steckernetzteil "erledigt", die Linienspannung von 24V/40mA wird über einen preiswerten Stepup-Wandler bereitgestellt. Das Ein- und Ausschalten der 230V für die FS-Maschine erledigt eine WLAN-Steckdose, es kann aber auch eine drahtgebundene Schaltsteckdose angeschlossen werden; dazu ist der GPIO-Pin "pin_power" auf eine Buchse herausgeführt. Damit sind sämtliche berührungsgefährliche Spannungen "zertifiziert ausgelagert".

## Der Aufbau

Folgende Haupt-Bestandteile habe ich verwendet:

 * Gehäuse: https://donau-elektronik.de/Artikel/Gehaeuse/Gehaeuseserie-KGB/3304/KGB21-Euro-Box-mittel-150x146x60-schwarz
     * Hier konnte ich bis auf einen alle vorhandenen Schraubsockel verwenden - das war praktisch...
     * Die Schnapp-Befestigung von Ober- und Unterschale ist was für geduldige Gemüter :-(
       
 * Feldfernsprecher-Wählzusatz: https://www.kleinanzeigen.de/s-anzeige/amtszusatz-waehlzusatz-neu-ovp-fuer-feldfernsprecher-ff-ob-zb/2921692000-234-8355
     * die Preise gehen von 10€ bis fast 100€, das ist unglaublich...
     * Die Erdtaste habe ich umfunktioniert zum Abruf des Software-KG, weil meine Maschine keinen Kennungsgeber hat
       
 * tasmota-fähige WLAN-Steckdose: NOUS AT1T https://www.idealo.at/preisvergleich/OffersOfProduct/202229762_-a1t-nous.html
 * Leuchtdrucktaster (24V-LED): https://heschen.com/de/collections/push-button-switch
 * Steckernetzteil 5V/2,4A https://www.berrybase.de/steckernetzteil-5v-dc-2-4a-12w-hohlstecker-5-5x2-1mm
 * Stepup-Wandler 5->24V https://www.pollin.de/p/daypower-step-up-schaltregler-modul-m-su-xl6019-810813
 * ADo-8UP Einsatz
 * RPi Zero 2W:  https://www.berrybase.de/raspberry-pi-zero-2-wh
 * PiTelex Adapter Board nach https://github.com/rwobrecht/piTelex-contrib/tree/main/TW39/Ohne-FSG/TW39-ohne-FSG-mit-Powersave
 * Software von https://github.com/rwobrecht/piTelex-contrib/blob/main/soft/ mit
   * RPi OS 13.2 trixie 32bit lite
   * piTelex Release 2025-12a von https://github.com/fablab-wue/piTelex/releases/tag/2025-12a



## Ein paar Fotos

<img src=img/TW39-FSG.1.jpg width=40%><img src=img/TW39-FSG.2.jpg width=40%>

<img src=img/TW39-FSG.4.jpg width=40%><img src=img/TW39-FSG.5.jpg width=40%>

<img src=img/TW39-FSG.3.jpg width=40%>

### [... und ein Video...](img/TW39-FSG.mp4)



## Die telex.json

```json
{
  "devices": {
    "screen": {
      "type": "screen",
      "enable": true,
      "show_BuZi": true,
      "show_info": false,
      "show_ctrl": true,
      "show_capital": false
    },
    "RPiTTY": {
      "type": "RPiTTY",
      "enable": true,
      "mode": "TW39", 	             # mode = "TWM" für Tastaturwahl
      "pin_txd": 22,
      "txd_powersave": true,
      "pin_rxd": 27,
      "pin_relay": 14,               # Leistungsrelais (Signal RLY)
      "pin_number_switch": -1,       # -1: Verwende Definition in "RPiCtrl", 0 für Tastaturwahl
      "baudrate": 50,
      "loopback": true,
    },
    "RPiCtrl": {
      "type": "RPiCtrl",
      "enable": true,
      "pin_number_switch": 13,        # 0 für Tastaturwahl
      "inv_number_switch": false,
      "pin_button_AT": 26,
      "pin_button_ST": 21,
      "pin_button_LT": 19,
      "pin_button_U3": 20,            # U3 standardmäßig vorbelegt mit "#" d.i. die eigene Kennung
      "pin_LED_A": 11,
      "pin_LED_WB": 5,
      "pin_LED_LT": 9,
      "pin_LED_Z": 6,
      "LED_Z_heartbeat": 6,           # Tastverhältnis off/on = 6:1
      "delay_AT": 0.5,                  # Gimmick: Zeitverzögerung in s simuliert Elektromechanik :-)
      "delay_ST": 1
    },
   "shellcmd": {
      "type": "shellcmd",
      "enable": true,
      "LUT": {
        "A": "curl -s -o /dev/null http://wlan-steckdose1.fritz.box/cm?cmnd=Power%20On",
        "Z": "curl -s -o /dev/null http://wlan-steckdose1.fritz.box/cm?cmnd=Power%20Off"
      }
    },
    "i-Telex": {
      "type": "i-Telex",
      "enable": true,
      "port": 2344,
      "tns_dynip_number": 123456,
      "tns_pin": 12345
    },
    "archive": {
      "type": "archive",
      "enable": true,
      "path": "/home/pi/piTelex-archive/"
    },   
    "log": {
      "type": "log",
      "enable": true,
      "filename": "/home/pi/piTelex-log/transcript.log"
    }
  },
  "wru_id": "123456 dummy d",          # Software-Kennung
  "errorlog_path": "/home/pi/piTelex-log/",
  "power_button_timeout": 7200,        # Nach 7200s Inaktivität wird die Maschine abgeschaltet
  "wru_replace_always": true,          # Immer Software-KG nutzen (nur für Maschine ohne KG)
  "dial_timeout": 0,                   # Standard-Wahlverfahren
  "continue_with_no_printer": false    # Ohne funktionierenden Drucker keine Verbindung annehmen
}

```

## 

