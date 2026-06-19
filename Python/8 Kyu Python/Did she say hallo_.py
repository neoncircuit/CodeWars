def validate_hello(greetings):
    greetings = greetings.lower()
    valid_greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(greeting in greetings for greeting in valid_greetings)