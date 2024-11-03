

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C', 'D']
    total_price = 0
    total_A = 0
    total_B = 0

    if not isinstance(skus, str) or not all(char in valid_skus for char in skus):
        return -1

    for sku in skus:
        if sku == 'A':
            total_A += 1
        elif sku == 'B':
            total_B += 1
        total_price += get_price(sku)

        if total_A == 3:
            total_price -= 20
            total_A = 0
        if total_B == 2:
            total_price -= 15
            total_B = 0
    return total_price

def get_price(sku):
    if(sku == 'A'):
        return 50
    elif(sku == 'B'):
        return 30
    elif(sku == 'C'):
        return 20
    elif(sku == 'D'):
        return 15



