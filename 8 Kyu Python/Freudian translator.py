def to_freud(sentence):
  #your code here
    words = sentence.split()
    new_sentence = "sex " * len(words)
    return new_sentence.strip()