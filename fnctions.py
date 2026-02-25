def remove_polish_chars(text):
    if not isinstance(text, str):
        return text
        
    # Definiujemy mapowanie: co zamienić na co
    polish_chars = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
    ascii_chars  = "acelnoszzACELNOSZZ"
    
    # Tworzymy tablicę translacji
    trans_table = str.maketrans(polish_chars, ascii_chars)
    
    # Wykonujemy zamianę
    return text.translate(trans_table)


def split_name_standard(full_name):
    if not full_name:
        return "", ""
    
    # 1. Usuwamy zbędne spacje (np. podwójne spacje w środku, spacje na końcach)
    clean_name = " ".join(full_name.split())
    
    # 2. Dzielimy tekst tylko przy PIERWSZEJ spacji
    parts = clean_name.split(" ", 1)
    
    first_name = parts[0]
    
    # Jeśli tablica ma 2 elementy, drugi to nazwisko. Jeśli 1, nazwiska brak.
    last_name = parts[1] if len(parts) > 1 else ""
    
    return first_name, last_name
