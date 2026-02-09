# Museumstaugliche Stromversorgung für piTelex

## Hintergrund

Gemäß § 3 der Verordnung über elektrische  Betriebsmittel (1. ProdSV) dürfen neue elektrische Betriebsmittel nur  dann in Verkehr gebracht werden, wenn sie den aktuellen Stand der  Sicherheitstechnik in der Europäischen Gemeinschaft erfüllen. Sie müssen bei ordnungsgemäßer Installation, Instandhaltung und bestimmungsgemäßer Verwendung die Gesundheit und Sicherheit von Menschen, Tieren sowie  Gütern nicht gefährden.

Einige Museen bestehen peinlich genau auf die Einhaltung der Sicherheitsbestimmungen und lassen Selbstbaugeräte ohne Zertifizierung nach den geltenden Vorschriften nicht zu.

**Wer also sein piTelex-System mit selbstgebautem Netzteil versorgt, könnte im Falle eines Vorfalls haftbar gemacht werden, wenn nachgewiesen wird, dass einschlägige Vorschriften nicht eingehalten wurden.**

## Konzept

Abhilfe bietet die Verwendung industriell gefertigter und zertifizierter/zugelassener Stromversorgungen. Diese bieten i.R. auch Schutz gegen Überstrom, Überspannung, Übertemperatur und Kurzschluss. im piTelex-Eigenbau selbst dürfen dann keine berührungsgefährlichen Spannungen verwendet werden.

> [!NOTE]
>
> **Kleinspannung (Extra Low Voltage, ELV):**
>
> Kleinspannung bezeichnet eine Spannung, die die Grenzwerte für den Spannungsbereich I nach IEC 61140 nicht überschreitet:
>
> - Wechselspannung (AC): Maximal 50 V
> - Gleichspannung (DC): Maximal 120 V
>
> Diese Spannungen gelten als nicht lebensbedrohlich bei direktem Kontakt und  erfüllen die Sicherheitsanforderungen für viele Anwendungen 
> (siehe auch den [wikipedia](https://de.wikipedia.org/wiki/Kleinspannung) -Artikel hierzu) .

**piTelex mit RPi SBC benötigen grundsätzlich eine stabile 5V-Versorgung für den RPi. Ein möglicher Weg ist also die Verwendung eines zugelassenen 5V-Steckernetzteils mit ausreichender Leistung, aus dem dann die weiteren benötigten Spannungen erzeugt werden.** 





## Umsetzung



### piTelex mit V.10-Platine

Hier wird mittels RS232-Treiber-IC MAX232 die +/- 9V Spannung erzeugt; diese ist definitiv nicht berührungsgefährlich. Also kein Handlungsbedarf.



### piTelex mit  TW39-Platine 

Das FSG verlangt eine deutlich höhere Spannung. Mindestens 60V Linienspannung sind erforderlich, oft auch mehr, da einzelne FSG etwas spannunghungriger sind (Beispiel: Siemens t68) . Diese Spannungen fallen zwar immer noch unter die SELV-Definition (s.o.), aber die industriell verfügbaren Hochsetzsteller sind in diesem Bereich schon rar. Im Forum gab es den [Vorschlag](https://www.telexforum.de/forum/thread/5507-t68d-wiederbelebung/?postID=52720#post52720), als Spannungsversorgung einen NCH6100HV Step-Up Converter für  Nixie-Röhren zu verwenden. (12V Eingangsspannung und einstellbare  Ausgangsspannung). Diesen Wandler gibt es für unter 10 Euro, aber man benötigt eine Speisespannung von 12V und damit ein 12V-Netzteil **und** ein 5V-Netzteil oder einen weiteren Step-Down-Wandler von 12V auf 5V.

Es gibt aber mittlerweile einen Nachfolgetyp (NCH6300HV), der zwar teurer ist (etwa 20 Euro), aber dafür mit 5V Eingangsspannung auskommt und somit die 12V-Versorgung erübrigt. Außerdem besitzt er eine höhere Maximalleistung von etwa 10W. Die Ausgangsspannung kann von 100V an aufwärts eingestellt werden, 100V sind aber mehr als genug.

> Die vom Linienkreis benötigte Leistung beträgt $P_{Linie}=100V * 40mA = 4W$ . 
> Bei einem Wirkungsgrad des Hochsetzstellers von $\eta_{Wandler} = 0,8$ muss die 5V-Versorgung also hierfür $P_{Wandler}= P_{Linie}/\eta_{Wandler}= 5W$ zur Verfügung stellen, was einem Strombedarf des Wandlers von $I_{Wandler}=P_{Wandler} / 5V = 1A$ entspricht. 

Mit einem 5V/3A-Netzteil ist man bei einer Stromaufnahme des RPi Zero2W von etwa 1 A  dabei auf der sicheren Seite.

>[!CAUTION]
>
> **Wichtig:** beide o.a. DC-DC-Wandler sind ausgangsseitig nicht kurzschlussfest. Es empfiehlt sich also dringend, den Linienstromkreis beispielsweise mit einer flinken 60mA-Sicherung zu schützen.  



### piTelex als FSG-Ersatz für TW39

#### Linienspannung

Zusätzlich zu den 5V= wird eine Linienspannung für den FS benötigt. Da kein FSG gespeist werden muss, sondern nur der Empfangsmagnet des FS , ist hier eine Spannung von $U_{Linie}=24V_=$ ausreichend. Dafür kann ein einfacher Hochsetzsteller (DC-DC - Wandler) verwendet werden, findet man bei Pollin oder Reichelt oder Conrad etc für unter 10 Euro, z.B. [hier](https://www.pollin.de/p/daypower-step-up-schaltregler-modul-m-su-xl6019-810813) oder [hier]( https://www.reichelt.de/de/de/shop/produkt/dc_dc-wandler_am1s_1_w_24_v_42_ma_sil-4-35027) oder ...

> Die vom Linienkreis benötigte Leistung beträgt $P_{Linie}=24V * 40mA = 0,96W$ . 
> Bei einem angenommenen Wirkungsgrad des Hochsetzstellers von $\eta_{Wandler}=0,8$ muss die 5V-Versorgung also hierfür $P_{Wandler}= P_{Linie}/\eta_{Wandler}= 1,42 W$ zur Verfügung stellen, was einem Strom von $I_{Wandler}=P_{Wandler} / 5V = 0,24 A$ entspricht.

Das ist bei Verwendung eines 2A-Netzteils und einer Stromaufnahme des RPi Zero2W von etwa 1 A vernachlässigbar.



#### Motorspannung

Zum Schalten der Netzspannung für den Fernschreiber / das Fernschaltgerät im Rahmen einer Stromsparschaltung können WLAN-Schaltsteckdosen oder auch drahtgebundene Schaltsteckdosen im Originalzustand verwendet werden (nicht z.B. WLAN-Steckdose öffnen und TASMOTA flashen, dadurch verliert das Gerät die Zertifizierung!) Links hierzu:

1. Mit Draht ginge z.B. das hier:
   https://www.olimex.com/Products/Duino/Shields/PWR-SWITCH/ 
   oder das hier:
   https://www.vocomo.de/de/Trigger-Schalt-Steckdose-V1.html
   oder das hier:
   https://www.antrax.de/produkt/switchbox-plus/

   Den Schalteingang der Dosen verbindet man mit dem als "pin_power" in telex.json konfigurierten GPIO, 
   siehe https://github.com/fablab-wue/piTelex/wiki/SW_MainsPower#hardware-solution

   

2. Werksseitig Tasmota-fähige Steckdosen findet man beispielsweise unter dieser Adresse:
   https://templates.blakadder.com/preflashed-stand.html

   Die Ansteuerung mit piTelex ist unter https://github.com/fablab-wue/piTelex/wiki/SW_MainsPower#software-solution erläutert.
