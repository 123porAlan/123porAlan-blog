#!/usr/bin/env python3
"""MD2TXT - Herramienta para concatenar archivos .md en un archivo .txt"""

import os
from datetime import datetime

def print_banner():
    print(r"""
__  __           _             
|  \/  | __ _ ___| | _____ _ __ 
| |\/| |/ _` / __| |/ / _ \ '__|
| |  | | (_| \__ \   <  __/ |   
|_|  |_|\__,_|___/_|\_\___|_|   
    """)

def main():
    print_banner()
    input_dir = os.path.normpath(input("Ingrese la ruta de la carpeta a escanear (iniciando desde C://): "))
    output_dir = os.path.normpath(input("Ingrese la ruta del directorio donde guardar el archivo .txt (iniciando desde C://): "))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"md2txt_{timestamp}.txt"
    output_path = os.path.join(output_dir, output_name)

    md_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".md"):
                md_files.append(os.path.join(root, file))

    if not md_files:
        print(f"No se encontraron archivos .md en {input_dir}")
        return

    with open(output_path, "w", encoding="utf-8") as outfile:
        for md_file in md_files:
            outfile.write(f"\n\n# Archivo: {os.path.basename(md_file)}\n\n")
            try:
                with open(md_file, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
            except Exception as e:
                print(f"Error al leer {md_file}: {e}")

    print(f"\nSe han procesado {len(md_files)} archivos y el resultado se guardó en:\n{output_path}")

if __name__ == "__main__":
    main()
