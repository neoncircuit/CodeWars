def period_is_late(last, today, cycle_length):
    delta = (today - last).days
    return delta > cycle_length