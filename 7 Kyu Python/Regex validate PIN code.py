def validate_pin(pin):
    #return true or false
    return (len(pin) == 4 or len(pin) == 6) and pin.isnumeric()
