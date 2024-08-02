# Redismini

# Was macht das Programm?

Redismini ist ein einfacher Key-Value-Store, ähnlich wie Redis.
Besteht aus zwei Teilen: einem Server (server.py) und einem Client (client.py).
Der Server empfängt Befehle von Clients, um Werte zu speichern und abzurufen.
Der Server kann prüfen, ob ein bestimmter Schlüssel existiert und Schlüssel löschen.
Der Client verbindet sich mit dem Server und schickt Befehle.

# Wofür ist es gut?
Geeignet für kleine Projekte zur schnellen und einfachen Speicherung und Abrufung von Daten.

# Wie funktioniert das?

Key-Value-Store
Speichert Daten als Sammlung von Schlüssel-Wert-Paaren.
Jeder Wert ist mit einem eindeutigen Schlüssel verbunden.
Befehl SET key value: Speichert value unter dem Schlüssel key.
Befehl GET key: Gibt den Wert zurück, der unter key gespeichert ist.

# Client-Server-Architektur

Besteht aus Server und einem oder mehreren Clients.
Server wartet auf Anfragen von Clients und beantwortet sie.
Clients senden Anfragen an den Server und warten auf Antworten.
Beispiel: client.execute('SET', 'key1', 'value1') sendet eine Anfrage an den Server, um den Wert value1 unter key1 zu speichern.

# MIT-Lizenz

