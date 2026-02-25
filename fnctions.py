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
