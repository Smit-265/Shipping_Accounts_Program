users_list = ["john", "dave", "kevin", "xavier", "dominic"]

#Function for already have an account and after creating an account
def already_acc(name):
    print("\n\nHello " + name.title() + ", Welcome into your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100:      $5.10 each")
    print("Shipping orders 101 to 500:    $5.00 each")
    print("Shipping orders 501 to 1000:   $4.95 each")
    print("Shipping orders over 1000:     $4.85 each")
    
    quantity = int(input("\nHow many items would you like to ship : "))
    if quantity <= 100:
        cost = 5.10
    elif quantity <= 500:
        cost = 5.00
    elif quantity <= 1000:
        cost = 4.95
    else:
        cost = 4.80       
        
    #Display final cost
    bill = quantity*cost
    bill = round(bill, 2)
    print("To ship " + str(quantity) + " items it will cost you $" + str(bill) + " at $" + str(cost) + " per item.")
    
    #Place the order if the user desires
    choice = input("\nWould you like to place this order (y/n) : ").lower().strip()
    if choice.startswith('y'):
        print("Okay, Shipping your " + str(quantity) + " items.")
    else:
        print("Okay, No order is being placed at this time.")
        
#Function to create an account         
def create_acc():
   create_username = input("\nEnter username to create your account : ").lower().strip()
   users_list.append(create_username)
   print("Cogratulations..Your account is created!")
   return create_username
   
#Function if don't want to create an account
def dont_create_acc():
    print("Okay..Goodbye!")

#Getting user input. if user already have an account or wants to create an account      
ask_for_acc = input("if you have account then type (y).\nif you want to create account then type (c)\nto exit type (q) : ").lower().strip()
if ask_for_acc.startswith('y'):
    username = input("\nEnter your Username : ").lower().strip()
    if username not in users_list:
        ask_again = input("\nSorry, You don't have an account.!\nif you want to create account type (y)\nif you don't want to create account type (n) : ").lower().strip()
        if ask_again.startswith('y'):
            create_acc()
        else:
            dont_create_acc()      
    if username in users_list:
        already_acc(username)
        
#For create an account           
if ask_for_acc.startswith('c'):
    username = create_acc()
    already_acc(username)
    
#For exit and if don't want to create an account
if ask_for_acc.startswith('q'):
    dont_create_acc()
