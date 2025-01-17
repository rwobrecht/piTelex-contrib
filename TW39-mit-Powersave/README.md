## Platine für piTelex TW39



Vor ein paar Jahren habe ich begonnen, mich mit i-telex zu beschäftigen. Anfangs war ich nicht sicher, ob i-telex das tool war, das ich gesucht hatte: 
ich wollte einfach einen alten Fernschreiber wieder zum Laufen bekommen. Vor diesem Hintergrund habe ich die Anschaffungskosten für eine i-telex-Station gescheut und stattdessen piTelex ausprobiert, das versprach, 
kostengünstiger zu sein, allerdings auch einen geringeren Leistungsumfang bietet und voraussetzt, dass man Spaß hat am Elektronikbasteln und über Grundkenntnisse in python und linux verfügt.

<img src="KiCad/TW39-mit-Powersave_Ansicht-Platine-3D-bestückt.jpg" width="70%" >
Die hier beschriebene Platine habe ich aus den im [piTelex-Wiki](https://github.com/fablab-wue/piTelex/wiki) gezeigten Grundschaltungen dann entwickelt, weil ich mit der angebotenen Eagle-Platine nicht wirklich klarkam.

Die Platine ist weder besonders kompakt noch besonders raffiniert layoutet, und sie verwendet statt der ULN...-Treiber-ICs vier einfache NPN-Transistoren. 
Diese Schaltung funktioniert in sechs meiner sieben piTelex-Stationen seit Jahren problemlos (Die siebte Station ist eine piTelex V.10 Station, die eine FS220 ohne FSG ins i-telex Netz bringt).

<img src="KiCad/TW39-mit-Powersave_Ansicht_Leiterbahnen.png" width="50%" align="right">
Das Platinenlayout ist auf Einfachheit hin getrimmt. Man kann sie zweilagig herstellen, aber auch als einlagig kupferkaschierte Platine ausführen, dann müssen lediglich drei Drahtbrücken eingesetzt werden, 
die ansonsten durch die zweite Kupferlage realisiert werden. Die Leitungsführung ist in Standradrastermaß von 1/10 Zoll gehalten, so dass das Layout unverändert auch auf einer 
handelsüblichen Punktrasterplatine ganz "zu Fuß" umgesetzt werden kann. Besonderes Augenmerk habe ich auf ausreichende Leiterbahnabstände im Hochspannnungsbereich gelegt. 
Wenn man die Schaltung auf einer Punktrasterplatine aufbaut, müssen die nicht verwendeten Lötstützpunkte im Bereich der Linienstromversorgung weggefräst werden, denn die 0,4mm "Luft" 
zwischen zwei Lötstützpunkten sind bei 120V Speisespannung sicher nicht ausreichend.


Die Schaltung verwendet **nicht** die Standard-GPIOs von piTelex, daher füge ich eine passende `telex.json` Datei mit den korrekten GPIO-Nummern bei.

```JSON
      "RPiTTY": {
      "type": "RPiTTY",         # standard TW39 (current loop) CCU and teletype
      "enable": true,
      "mode": "TW39",
      "pin_txd": 2,
      "pin_rxd": 5,
      "pin_relay": 13,          # GPIO of loop relay (for changing polarity)
      "pin_number_switch": -1,  # -1 = use definition in "RPiCtrl"
      "txd_powersave": true     # switch off loop current in sleep mode
    },
    "RPiCtrl": {
      "type": "RPiCtrl",
      "enable": true,
      "pin_number_switch": 6,   # GPIO of pin to monitor for dial pulses
      "pin_button_PT": 21,      # GPIO for power button
      "pin_LED_WB": 16,         # GPIO for LED indicating dial mode (Wählbereitschaft)
      "pin_LED_A": 20,          # GPIO for LED indicating active connection
      "pin_LED_Z": 12,          # GPIO for LED indicating Standby/Sleep
      "LED_Z_heartbeat": 2,     # duty cycle of hearbeat in ZZ mode: 0.5s on / 1s off
      "pin_power": 26,          # GPIO for power relay (switching mains)
      "inv_power": false
    },
(...)
#
  "power_off_delay": 3,         # wait # seconds after poweroff condition 
#                               # before switching off mains
#
  "power_button_timeout": 7200, # switch off mainsain any case after # seconds
#
  "wru_id": "123456 dummy d",
  "wru_replace_always": false,
  "continue_with_no_printer": false,
  "dial_timeout": 0
}

```
