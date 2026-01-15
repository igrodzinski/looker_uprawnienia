import os

# --- KONFIGURACJA ---
folder_path = './twoj_folder'
target_filename = 'plik.py'  # nazwa pliku do znalezienia
user_email = 'przyklad@mail.com'
# --------------------

def process_file():
    old_path = os.path.join(folder_path, target_filename)
    
    if not os.path.exists(old_path):
        print("Nie znaleziono pliku.")
        return

    # 1. Edycja zawartości (zamiana "looker_mail")
    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("looker_mail", user_email)
    
    with open(old_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # 2. Zmiana nazwy pliku (dodanie maila przed rozszerzeniem)
    name_part, ext = os.path.splitext(target_filename)
    new_filename = f"{name_part}_{user_email}{ext}"
    new_path = os.path.join(folder_path, new_filename)
    
    os.rename(old_path, new_path)
    print(f"Gotowe! Plik zapisany jako: {new_filename}")

if __name__ == "__main__":
    process_file()
