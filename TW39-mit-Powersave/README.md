## Platine für piTelex TW39



Vor ein paar Jahren habe ich begonnen, mich mit i-telex zu beschäftigen. Anfangs war ich nicht sicher, ob i-telex das tool war, das ich gesucht hatte: 
ich wollte einfach einen alten Fernschreiber wieder zum Laufen bekommen. Vor diesem Hintergrund habe ich die Anschaffungskosten für eine i-telex-Station gescheut und stattdessen piTelex ausprobiert, das versprach, 
kostengünstiger zu sein, allerdings auch einen geringeren Leistungsumfang bietet und voraussetzt, dass man Spaß hat am Elektronikbasteln und über Grundkenntnisse in python und linux verfügt.

Die hier beschriebene Platine habe ich aus den im piTelex-Wiki gezeigten Grundschaltungen dann entwickelt, weil ich mit der angebotenen Eagle-Platine nicht wirklich klarkam.

Die Platine ist weder besonders kompakt noch besonders raffiniert layoutet, und sie verwendet statt der ULN...-Treiber-ICs vier einfache NPN-Transistoren. 
Diese Schaltung funktioniert in sechs meiner sieben piTelex-Stationen seit Jahren problemlos (Die siebte Station ist eine piTelex V.10 Station, die eine FS220 ohne FSG ins i-telex Netz bringt).

Das Platinenlayout ist auf Einfachheit hin getrimmt. Man kann sie zweilagig herstellen, aber auch als einlagig kupferkaschierte Platine ausführen, dann müssen lediglich drei Drahtbrücken eingesetzt werden, 
die ansonsten durch die zweite Kupferlage realisiert werden. Die Leitungsführung ist in Standradrastermaß von 1/10 Zoll gehalten, so dass das Layout unverändert auch auf einer 
handelsüblichen Punktrasterplatine ganz "zu Fuß" umgesetzt werden kann. Besonderes Augenmerk habe ich auf ausreichende Leiterbahnabstände im Hochspannnungsbereich gelegt. 
Wenn man die Schaltung auf einer Punktrasterplatine aufbaut, müssen die nicht verwendeten Lötstützpunkte im Bereich der Linienstromversorgung weggefräst werden, denn die 0,4mm "Luft" 
zwischen zwei Lötstützpunkten sind bei 120V Speisespannung sicher nicht ausreichend.

Die Schaltung verwendet **nicht** die Standard-GPIOs von piTelex, daher füge ich eine passende `telex.json` Datei mit den korrekten GPIO-Nummern bei.
