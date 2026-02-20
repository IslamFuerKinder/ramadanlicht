# Ramadanlicht Webseite — Anleitung

## Link zur Webseite
https://mustafalehmann.github.io/ramadanlicht/

## Projektstruktur

```
webseite/
├── index.html                        ← Die Webseite
├── logo.png                          ← WhatsApp-Kanal Logo
├── ANLEITUNG.md                      ← Diese Datei
└── pdfs/
    └── Tag_01_Die_verlorene_Muenze.pdf   ← Geschichten als PDF
```

## Neue Geschichte hinzufügen

### 1. PDF in den Ordner legen
Die PDF-Datei in `webseite/pdfs/` kopieren. Dateiname-Schema:
```
Tag_02_Adams_grosser_Moment.pdf
Tag_03_Das_geteilte_Brot.pdf
...
```

### 2. index.html aktualisieren
In `index.html` bei der entsprechenden Geschichte `datei: null` durch den Dateinamen ersetzen:

**Vorher:**
```javascript
{ tag: 2,  titel: "Adams großer Moment",  datei: null },
```

**Nachher:**
```javascript
{ tag: 2,  titel: "Adams großer Moment",  datei: "Tag_02_Adams_grosser_Moment.pdf" },
```

### 3. Änderungen auf GitHub hochladen
Im Terminal (im Ordner `webseite`) folgende Befehle ausführen:
```bash
cd C:/Users/musti/Projekt/Geschichten/webseite
git add .
git commit -m "Tag X hinzugefügt"
git push
```

Die Webseite aktualisiert sich nach 1-2 Minuten automatisch.

## GitHub Pages Einrichtung (bereits erledigt)

1. GitHub-Account: MustafaLehmann
2. Repository: https://github.com/MustafaLehmann/ramadanlicht
3. GitHub Pages aktiviert unter Settings → Pages → Branch: main
4. Git-Konfiguration für dieses Repository:
   - E-Mail: f.lehmann.hannover@gmail.com
   - Name: MustafaLehmann

## Kosten
- Hosting: kostenlos (GitHub Pages)
- Domain: kostenlos (mustafalehmann.github.io)
