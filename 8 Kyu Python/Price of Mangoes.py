def mango(quantity, price):
    mangoes_to_pay_for = (quantity // 3) * 2 + (quantity % 3)
    return mangoes_to_pay_for * price