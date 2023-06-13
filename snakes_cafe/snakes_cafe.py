print("$ python snakes_cafe.py")
print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type 'quit' **")
print("")
print("Appetizers")
print("----------")
print("Wings")
print("Cookies")
print("Spring Rolls")
print("")
print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")
print("")
print("Desserts")
print("-------")
print("Ice Cream")
print("Cake")
print("Pie")
print("")
print("Drinks")
print("-------")
print("Coffee")
print("Tea")
print("Unicorn Tears")
print("")
print("***********************************")
print("** What would you like to order? **")
print("***********************************")
print(">")

def order():
    orders = {}
    while True:
        order = input(">")
        if order == "quit":
            break
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
        print(f"\n** Thanks for ordering! {orders[order]} orders(s) of {order} will be right up! **\n")
    print("Exiting")

if __name__ == "__main__":
    order()
