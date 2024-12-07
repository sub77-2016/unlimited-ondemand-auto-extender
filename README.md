# SIM24 Auto Extender

Dieses Tool automatisiert das Nachbuchen von Datenvolumen bei SIM24-Unlimited-Tarifen. Bei diesen Tarifen muss nach Verbrauch der ersten 50GB das Datenvolumen manuell in 2GB-Schritten nachgebucht werden. Dieser Prozess wird durch dieses Script vollautomatisch erledigt.

## Features

- Automatische Anmeldung im SIM24-Portal
- Kontinuierliche Überwachung des Datenvolumens
- Automatisches Nachbuchen bei Bedarf
- Ausführliche Logging-Funktionen
- Dockerisierte Lösung für einfache Installation

## Voraussetzungen

- Docker auf dem System installiert
- SIM24 Account-Zugangsdaten
- Ein aktiver SIM24-Unlimited-Tarif

## Installation & Einrichtung

1. Image herunterladen:
```bash
docker pull ghcr.io/danielwte/sim24-auto-extender:latest
```

2. Container starten:
```bash
docker run -d \
  -e USERNAME="sim24-username" \
  -e PASSWORD="sim24-password" \
  -e CHECK_INTERVAL=300 \
  --name sim24-auto-extender \
  ghcr.io/danielwte/sim24-auto-extender:latest
```

### Umgebungsvariablen

- `USERNAME`: Der SIM24 Benutzername
- `PASSWORD`: Das SIM24 Passwort
- `CHECK_INTERVAL`: Prüfintervall in Sekunden (Standard: 300)

## Logs einsehen

Die Logs können wie folgt eingesehen werden:
```bash
docker logs sim24-auto-extender
```

## Container-Verwaltung

Container neustarten:
```bash
docker restart sim24-auto-extender
```

Container stoppen:
```bash
docker stop sim24-auto-extender
```

Container entfernen:
```bash
docker rm sim24-auto-extender
```

## Automatischer Start nach Systemneustart

Für einen automatischen Start nach einem Systemneustart:
```bash
docker run -d \
  --restart unless-stopped \
  -e USERNAME="sim24-username" \
  -e PASSWORD="sim24-password" \
  -e CHECK_INTERVAL=300 \
  --name sim24-auto-extender \
  ghcr.io/danielwte/sim24-auto-extender:latest
```

## Sicherheit

- Die Zugangsdaten werden nur innerhalb des Containers verwendet
- Es werden keine Daten persistent gespeichert
- Die Kommunikation erfolgt direkt mit dem SIM24-Portal

## Disclaimer

Dieses Tool ist ein inoffizielles Hilfsprogramm und steht in keiner Verbindung zu SIM24. Die Nutzung erfolgt auf eigene Verantwortung.