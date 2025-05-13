# performance test Forlan Ordoñez

# empty list to store products
inventory = []


# --Functions--
# --functions validate errors--

# whole
def wholeNumber(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print('Please enter a number!')
            
# decimals
def decimalNumber(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print('Please enter a number!')

# text
def verifyText(message):
    while True:
        value = input(message)
        if value.strip() != '':
            return value
        else:
            print('Please enter text!')
            
            
# --FUNCTION TO ADD PRODUCT--

def addProduct(inventory, product, price, amount ):
    
    for item in inventory: # validate if the product is already in inventory 
        if product in item:
            print(f'The product {product} is already in inventory')
            return
    
    dictionary = {product: (price, amount)} # create dictionary and one tuple for price and quantity
    inventory.append(dictionary) # add list
    
    print(f'\nThe product {product} was added successfully!') # message


# --FUNCTION TO CONSULT PRODUCT--
   
def consultProduct(inventory, productSearched):
    
    if not inventory:
        print("Empty inventory!")
        return
   
    found = False # flag to check if the product was found

    # loop through the list of dictionaries and search for the product
    for item in inventory:
        if productSearched in item:
            price, amount = item[productSearched] # get price and quantity of the product
            print(f'\nProduct: {productSearched}')
            print(f'Price: ${price}')
            print(f'Available quantity: {amount}')
            found = True
            break # exit loop once product is found

    # if the product was not found, show message
    if not found:
        print(f'\nThe product "{productSearched}" is not in the inventory.')


# --FUNCTION TO UPDATE PRICE--
def updatePrice(inventory, productSearch, new_price):
    if not inventory:
        print("Empty inventory!")
        return

    for item in inventory: # loop through inventory items
        if productSearch in item:
            current_price, amount = item[productSearch]
            print(f'\nProduct: {productSearch}')
            print(f'Old price: ${current_price}')

            # update the price keeping the current quantity
            item[productSearch] = (new_price, amount)

            print(f'\nThe price of "{productSearch}" was successfully updated to ${new_price}')
            break
    else:
        print(f'\nThe product "{productSearch}" is not in the inventory.')


# --FUNCTION TO DELETE PRODUCT--
def deleteProduct(inventory, productSearch):
    if not inventory:
        print("Empty inventory!")
        return

    # loop through the list of dictionaries to find and delete the product
    for item in inventory:
        if productSearch in item:
            inventory.remove(item)
            print(f'\nThe product "{productSearch}" was successfully deleted from the inventory.')
            break
    else:
        print(f'\nThe product "{productSearch}" is not in the inventory.')


# --TOTAL INVENTORY VALUE--
def totalInventory(inventory):
    total = sum(price * amount for item in inventory for price, amount in item.values())
    print(f'\nTotal inventory value: ${total:.2f}')  


#MENU
def menu():
    print('\n--INVENTORY STORE--\n')
    print('1) Add product')
    print('2) Consult product')
    print('3) Update product price')
    print('4) Delete product')
    print('5) Total value')
    print('6) Exit\n')


# we call the functions
while True: # a while loop to add an unlimited number of products until exiting the loop
    menu()
    try:
        option = input('Enter an option: ')
        option = int(option)
    except ValueError:
        print('ERROR 404 Please enter a number')
        continue
    #

    if option == 1:
        product = verifyText('Enter the product name: ').lower()
        price = decimalNumber(f'Enter the price: ')
        amount = wholeNumber(f'Enter the quantity: ')
            
        # HERE GOES THE FUNCTION TO ADD
        addProduct(inventory, product, price, amount)
            
    elif option == 2:
        if not inventory: # validate if inventory is empty
            print('Empty inventory!')
        else:
            print('\nProducts in inventory\n') # display available products
            for i in inventory:
                for nameProduct in i.keys():
                    print(f'- {nameProduct}')

                # here the function is called
                
            product_search = input('\nEnter the name of the product to search: ').lower()
            consultProduct(inventory, product_search)
            
    elif option == 3:
        # display products
        print('\nProducts in inventory\n') # display available products
        for i in inventory:
            for nameProduct in i.keys():
                print(f'- {nameProduct}')
                
        productSearch = input('\nEnter the name of the product to update its price: ').lower()

        # validate that the new price is a number
        while True:
            try:
                new_price = float(input('Enter the new price: '))
                break
            except ValueError:
                print('ERROR! Please enter a valid number for the price')

        updatePrice(inventory, productSearch, new_price)
        
    elif option == 4:
        # display products before deleting
        print('\nAvailable products\n')
        for item in inventory:
            for nameProduct in item.keys():
                print(f'- {nameProduct}')

        # data input
        productSearch = input('\nEnter the name of the product to delete: ').lower()
        deleteProduct(inventory, productSearch)
    
    elif option == 5:
        totalInventory(inventory)
        
    elif option == 6:
        print('\nGoodbye!')
        break

