def correct_polish_letters(st): 
    # your code here
    translation_table = str.maketrans(
        "ąćęłńóśźż", 
        "acelnoszz"
    )
    return st.translate(translation_table)