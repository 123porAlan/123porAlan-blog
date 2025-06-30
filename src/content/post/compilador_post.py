import os
import glob
import yaml

def get_all_tags(folder_path):
    """Extrae todas las etiquetas únicas de los posts"""
    md_files = glob.glob(os.path.join(folder_path, "*.md"))
    tags = set()
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    try:
                        metadata = yaml.safe_load(frontmatter)
                        if metadata and 'tags' in metadata:
                            tags.update(metadata['tags'])
                    except yaml.YAMLError as e:
                        print(f"Error en {os.path.basename(file_path)}: {e}")
    
    return sorted(tags)

def compile_posts_by_tag(folder_path, tag, output_file):
    """Compila posts con una etiqueta específica"""
    md_files = glob.glob(os.path.join(folder_path, "*.md"))
    selected_posts = []
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    try:
                        metadata = yaml.safe_load(frontmatter)
                        if metadata and 'tags' in metadata and tag in metadata['tags']:
                            selected_posts.append(content)
                    except yaml.YAMLError as e:
                        print(f"Error en {os.path.basename(file_path)}: {e}")

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("\n\n---\n\n".join(selected_posts))
    
    return len(selected_posts)

def show_menu(tags):
    """Muestra el menú interactivo"""
    print("\n🟢 Etiquetas disponibles:")
    for i, tag in enumerate(tags, 1):
        print(f"{i}. {tag}")
    
    while True:
        try:
            choice = int(input("\n► Selecciona una etiqueta (número): "))
            if 1 <= choice <= len(tags):
                return tags[choice-1]
            print(f"⚠️ Ingresa un número entre 1 y {len(tags)}")
        except ValueError:
            print("⚠️ Debes ingresar un número válido")

def main():
    # Configuración (ajusta esta ruta)
    posts_folder = "/home/alanbellon/.my_blog/123porAlan-blog/src/content/post"
    
    # Obtener todas las etiquetas
    tags = get_all_tags(posts_folder)
    
    if not tags:
        print("❌ No se encontraron etiquetas en los posts")
        return
    
    # Mostrar menú
    selected_tag = show_menu(tags)
    
    # Generar nombre de archivo
    output_file = f"{selected_tag.lower().replace(' ', '-')}.txt"
    
    # Compilar posts
    count = compile_posts_by_tag(posts_folder, selected_tag, output_file)
    
    if count > 0:
        print(f"\n✅ ¡Hecho! {count} posts con la etiqueta '{selected_tag}'")
        print(f"📄 Archivo generado: {output_file}")
    else:
        print(f"\n⚠️ No hay posts con la etiqueta '{selected_tag}'")

if __name__ == "__main__":
    main()
