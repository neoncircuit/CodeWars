def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    for i in vowels:
        st = st.replace(i, "!")
    return st
