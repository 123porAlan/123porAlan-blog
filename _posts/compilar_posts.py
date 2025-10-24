import os

# --- Configuración ---

# 1. ¡IMPORTANTE! Cambia esto al nombre exacto de este archivo .py
SCRIPT_NAME = 'compilar.py' 

# 2. El archivo .txt que se creará en esta misma carpeta
OUTPUT_FILE = 'corpus_para_ia.txt'

# 3. El script buscará posts en el directorio actual ('.')
POSTS_DIRECTORY = '.' 

# 4. Un separador claro entre cada post
SEPARATOR = "\n\n========== NUEVO POST ==========\n\n"

# ---------------------

def extract_content_from_post(file_path):
    """
    Lee un archivo de post, quita el 'YAML Front Matter' (el bloque entre ---) 
    y devuelve solo el contenido de texto.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # El Front Matter de Jekyll siempre está al inicio entre '---'
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) > 2:
                return parts[2].strip()
        
        # Si no empieza con '---', es un archivo sin Front Matter
        return content.strip()
        
    except Exception as e:
        print(f"  [Advertencia] No se pudo procesar {file_path}: {e}")
        return None

def main():
    print(f"Iniciando compilación desde el directorio actual...")
    
    all_posts_content = []
    count = 0

    # Iteramos sobre todos los archivos en el directorio actual
    for filename in sorted(os.listdir(POSTS_DIRECTORY)):
        
        # --- Lógica para ignorar archivos ---
        # 1. Ignoramos el propio script
        if filename == SCRIPT_NAME:
            print(f"Ignorando script: {filename}")
            continue
            
        # 2. Ignoramos el archivo de salida para no procesarlo
        if filename == OUTPUT_FILE:
            print(f"Ignorando archivo de salida: {filename}")
            continue
        # -------------------------------------

        # Nos aseguramos de que solo procese archivos de post
        if filename.endswith('.md') or filename.endswith('.markdown'):
            print(f"Procesando: {filename}")
            
            # Como estamos en '.', el path es solo el nombre del archivo
            content = extract_content_from_post(filename)
            
            if content:
                all_posts_content.append(content)
                count += 1
    
    if count == 0:
        print("\nNo se encontraron posts (.md o .markdown) para procesar.")
        return

    # Escribimos todo el contenido compilado en el archivo de salida
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(SEPARATOR.join(all_posts_content))
        
        print(f"\n¡Éxito! ✨")
        print(f"Se combinaron {count} posts en el archivo: '{OUTPUT_FILE}'")
        print("El archivo se guardó en esta misma carpeta.")
    
    except Exception as e:
        print(f"\n[ERROR] No se pudo escribir en el archivo de salida {OUTPUT_FILE}: {e}")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
