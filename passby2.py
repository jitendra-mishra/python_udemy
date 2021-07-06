class Sale:

    def __init__(self, amount):
        self.amount = amount


def find_total(sales_list):
    total = 0
    for sale in sales_list:
        print("New Sale")
        print(sale.amount)
        total += sale.amount
    return total


january_sales = [Sale(200), Sale(100), Sale(40)]
print(f"Total={find_total(january_sales)}")
