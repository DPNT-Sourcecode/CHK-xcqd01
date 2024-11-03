

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(skus)
    total_price = 0
    for sku in skus:
        if sku not in ['A', 'B', 'C']:
            return -1
        total_price += get_price(sku)
    return total_price

def get_price(sku):
    if(sku == 'A'):
        return 50
    elif(sku == 'B'):
        return 30
    elif(sku == 'C'):
        return 20


