#!/usr/bin/env python3
"""
DOCX zu TXT Konverter
Konvertiert DOCX-Dateien in TXT-Dateien mit Windows-Zeilenumbrüchen (CRLF)
"""

import os
import sys
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("Fehler: Das Modul 'python-docx' ist nicht installiert.")
    print("Bitte installieren Sie es mit: pip install python-docx")
    sys.exit(1)


def docx_to_txt(docx_path, txt_path=None):
    """
    Konvertiert eine DOCX-Datei in eine TXT-Datei

    Args:
        docx_path: Pfad zur DOCX-Datei
        txt_path: Pfad zur TXT-Ausgabedatei (optional, wird automatisch generiert wenn nicht angegeben)
    """
    try:
        # DOCX-Datei einlesen
        doc = Document(docx_path)

        # Text aus allen Absätzen extrahieren
        text_content = []
        for paragraph in doc.paragraphs:
            text_content.append(paragraph.text)

        # Mit Windows-Zeilenumbrüchen (CRLF) zusammenfügen
        full_text = '\r\n'.join(text_content)

        # TXT-Pfad generieren, falls nicht angegeben
        if txt_path is None:
            txt_path = Path(docx_path).with_suffix('.txt')

        # TXT-Datei schreiben (UTF-8 mit BOM für Windows-Kompatibilität)
        with open(txt_path, 'w', encoding='utf-8-sig', newline='') as f:
            f.write(full_text)

        print(f"Erfolgreich konvertiert: {docx_path} -> {txt_path}")
        return True

    except Exception as e:
        print(f"Fehler beim Konvertieren von {docx_path}: {e}")
        return False


def convert_directory(directory_path, output_dir=None):
    """
    Konvertiert alle DOCX-Dateien in einem Verzeichnis

    Args:
        directory_path: Pfad zum Verzeichnis mit DOCX-Dateien
        output_dir: Optionales Ausgabeverzeichnis für TXT-Dateien
    """
    directory = Path(directory_path)

    if not directory.exists():
        print(f"Fehler: Verzeichnis '{directory_path}' existiert nicht.")
        return

    # Alle DOCX-Dateien finden
    docx_files = list(directory.glob('*.docx'))

    if not docx_files:
        print(f"Keine DOCX-Dateien in '{directory_path}' gefunden.")
        return

    print(f"{len(docx_files)} DOCX-Datei(en) gefunden.\n")

    # Ausgabeverzeichnis erstellen, falls angegeben
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for docx_file in docx_files:
        if output_dir:
            txt_file = Path(output_dir) / docx_file.with_suffix('.txt').name
        else:
            txt_file = None

        if docx_to_txt(docx_file, txt_file):
            success_count += 1

    print(f"\n{success_count} von {len(docx_files)} Datei(en) erfolgreich konvertiert.")


def main():
    """Hauptfunktion"""
    if len(sys.argv) < 2:
        print("Verwendung:")
        print("  Einzelne Datei:  python docx_to_txt.py <datei.docx>")
        print("  Verzeichnis:     python docx_to_txt.py <verzeichnis>")
        print("  Mit Ausgabeort:  python docx_to_txt.py <quelle> <ausgabeverzeichnis>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    path = Path(input_path)

    if path.is_file() and path.suffix.lower() == '.docx':
        # Einzelne Datei konvertieren
        docx_to_txt(input_path, output_path)
    elif path.is_dir():
        # Verzeichnis konvertieren
        convert_directory(input_path, output_path)
    else:
        print(f"Fehler: '{input_path}' ist keine gültige DOCX-Datei oder kein Verzeichnis.")
        sys.exit(1)


if __name__ == '__main__':
    main()
