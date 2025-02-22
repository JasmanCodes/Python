import fileinput

def menu():
    print('-------------------------------------')
    print(' Inventory Management Menu ')
    print('-------------------------------------')
    print('(1) Add new item to inventory')
    print('(2) Remove item from inventory')
    print('(3) Update inventory')
    print('(4) Search item in inventory')
    print('(5) Print inventory report')
    print('(0) Quit')
    choice=int(input("enter your choice: "))
    selectitems(choice)

def selectitems(choice):
    if choice == 1:
        addItems()
    elif choice == 2:
        removeItems()
    elif choice == 3:
        updateItems()
    elif choice == 4:
        searchItems()
    elif choice == 5:
        printInvent()
    elif choice == 0:
        exit()

def addItems():
    Infile = open('Inventory.txt','a')
    print("Adding Inventory")
    print("-----------------")
    item_desc=input("enter the name of the item: ")
    item_qty=input("enter the quantity of the items: ")
    Infile.write(item_desc + '\n')
    Infile.write(item_qty + '\n')
    Infile.close()
    op = int(input("enter 1 to continue or 0 to exit: "))
    if op == 1:
        menu()
    else:
        exit()

def removeItems():
    print("Removing Inventory")
    print("-----------------")
    item_desc=input("enter the item name to remove from inventory: ")
    file = fileinput.input('Inventory.txt',inplace=True)

    for line in file:
        if item_desc in line:
            next(file,None)
        else:
            print(line.strip('\n'),end='\n')
            
    op = int(input("enter 1 to continue or 0 to exit: "))
    if op == 1:
        menu()
    else:
        exit()


def searchItems():
    print("Searching Inventory")
    print("-------------------")
    item_desc = input("enter the name of the items: ")
    
    f = open('Inventory.txt','r')
    search = f.readlines()
    f.close()
    for i,line in enumerate(search):
        if item_desc in line:
            for b in search[i:i+1]:
                print('Item:      ',b,end='')
            for c in search[i+1:i+2]:
                print('Quantity: ',c,end='')
                print('-----------')
    
    op = int(input("enter 1 to continue or 0 to exit: "))
    if op == 1:
        menu()
    else:
        exit()

def updateItems():
    print("Updating Inventory")
    print("------------------")
    item_desc = input("enter the item to update: ")
    item_qty = int(input("enter the updated quantity. Enter - for less: "))
    
    with open('Inventory.txt', 'r') as f:
        filedata = f.readlines()
    
    for i, line in enumerate(filedata):
        if item_desc in line:
            current_qty = int(filedata[i+1].strip())
            if item_qty < 0:
                new_qty = max(current_qty + item_qty, 0)
            else:
                new_qty = current_qty + item_qty
            filedata[i+1] = str(new_qty) + '\n'
            break
    
    with open('Inventory.txt', 'w') as f:
        f.writelines(filedata)
    
    op = int(input("enter 1 to continue or 0 to exit: "))
    if op == 1:
        menu()
    else:
        exit()

def printInvent():
    Infile = open('Inventory.txt','r')
    item_desc = Infile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_desc != '':
        item_qty = Infile.readline()
        item_desc = item_desc.rstrip('\n')
        item_qty=item_qty.rstrip('\n')
        print('Item:   ',item_desc)
        print('quantity:  ',item_qty)
        item_desc = Infile.readline()
    Infile.close()
    op = int(input("enter 1 to continue or 0 to exit: "))
    if op == 1:
        menu()
    else:
      exit()

menu()