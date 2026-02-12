import re

def i_speak_french(speech: str) -> str:
    # Parlez-vous français ? :)
    sentences = re.split(r'[.!?]+', speech)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    translated_sentences = []
    for sentence in sentences:
        words = sentence.split()
        count = len(words)
        if count == 0:
            continue
        
        baguette_words = ["baguette"] * count
        baguette_words[0] = "Baguette"
        
        translated_sentence = " ".join(baguette_words) + " Encore!"
        translated_sentences.append(translated_sentence)
    
    return " ".join(translated_sentences)