from datetime import datetime

def is_today(date): 
    # your code here
    today = datetime.now().date()
    if date.date() == today:
        return True
    else: 
        return False
