import csv

PRODUCTS = []

def show_menu():
    print("Welcome to Mahtab's store")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Show list")
    print("5. Search")
    print("6. Buy")
    print("7. Save and Exit")



def load_data_from_file():
    print("Loading ...")
    f = open("database.csv", 'r')

    for row in f:
        info = row[:-1].split(',')
        new_dic = {'code':info[0], 'name':info[1], 'price':info[2], 'count':info[3]}
        PRODUCTS.append(new_dic)

    print("Database loaded. App is ready to use.")



def add():
    show_list()
    temp_code = input("Enter the code of the product: ")
    temp_name = input("Enter the name of the product: ")
    temp_price = input("Enter the price of the product: ")
    temp_count = input("Enter the number of the product: ")

    new_product = {'code':temp_code, 'name':temp_name, 'price':temp_price, 'count':temp_count}
    
    if not any(product['name'] == temp_name for product in PRODUCTS):
        PRODUCTS.append(new_product)
        show_list()
    else:
        print("This product is already available.")



def edit():
    show_list()
    name = input("Enter the name of the product you want to edit: ")
    flag = False

    for product in PRODUCTS:
        if product['name'] == name:
            flag = True
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))

            print("Which parts do you want to edit? ")
            print("1. Code")
            print("2. Price")
            print("3. Count")
            part_choice = int(input("--> "))
            
            if part_choice == 1:
                product['code'] = input("Enter the code: ")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
            elif part_choice == 2:
                product['price'] = input("Enter the price: ")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
            elif part_choice == 3:
                product['count'] = input("Enter the number: ")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
            else:
                print("That's wrong! Try again.")

    if flag == False:
        print("The product was NOT found to edit.") 



def delete():
    show_list()
    name = input("Enter the name of the product you want to delete: ")
    flag = False

    for product in PRODUCTS:
        if product['name'] == name:
            flag = True
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))

            char_choice = input("Are you sure? y/n ").lower()

            if char_choice == 'y':
                PRODUCTS.remove(product)
                show_list()
            elif char_choice == 'n':
                break
            else:
                print("Your request has not been defined!")
                break

    if flag == False:
        print("The product was NOT found to delete.") 



def show_list():
    print("code\tname\tprice\tcount".expandtabs(12))

    for product in PRODUCTS:
        print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))



def search():
    name = input("Enter the name of the product you want: ")
    flag = False

    for product in PRODUCTS:
        if product['name'] == name:
            flag = True
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
            print("The product was found.") 
        
    if flag == False:
        print("The product was NOT found.")




def buy():
    show_list()
    shopping_basket = []
    sum_price = 0

    while True:
        name = input("Which items do you want to buy? ")
        flag = False

        for product in PRODUCTS:
            if product['name'] == name:
                flag = True
                number = input("How many do you need? ")

                if int(number) <= int(product['count']):
                    sum_price = sum_price + (int(number) * int(product['price']))
                    new_shopping =  {'code':product['code'], 'name':product['name'], 'price':product['price'], 'count':number}

                    flag_item = False
                    for item in shopping_basket:
                        if name == item['name']:
                            flag_item = True
                            item['count'] = str(int(item['count']) + int(number))
                            
                    if flag_item == False:
                        shopping_basket.append(new_shopping)

                    product['count'] = str(int(product['count']) - int(number))
                    
                    if int(product['count']) == 0:
                        PRODUCTS.remove(product)
                else:
                    print("This number of the product is NOT available.")

        
        if flag == False:
            print("The product was NOT found.")

        char_choice = input("Do you wanna countinue? y/n ").lower()

        if char_choice == 'n':
            if sum_price != 0:
                print("Your Bill:")
                print("code\tname\tprice\tcount".expandtabs(12))

                for item in shopping_basket:
                    print(f"{item['code']}\t{item['name']}\t{item['price']}\t{item['count']}".expandtabs(12))
                print("Total amount =", sum_price)
                break
            else:
                break
        elif char_choice == 'y':
            continue
        else:
            print("Your request has not been defined!")
            break



def save():
    cv_col = ['code','name','price','count']

    try:
        with open("database.csv", 'w', newline = '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cv_col)
            writer.writerows(PRODUCTS)
    except IOError:
        print("I/O error")
  


load_data_from_file()

while True:
    
    show_menu()
    choice = int(input("Enter your choice --> "))


    if choice == 1:
        add()

    elif choice == 2:
        edit()

    elif choice == 3:
        delete()

    elif choice == 4:
        show_list()

    elif choice == 5:
        search()
            
    elif choice == 6:
        buy()

    elif choice == 7:
        save()
        break
    
    else:
        print("Try again!")

