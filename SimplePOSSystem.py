#Liam Browning

#defining the different menus to add to a total based on what number is inputted, then returning that number
def Appetizers():
    print("1. Mozz Sticks   $5.99 \n2. Fried Pickles   $5.99\n3. Quit")
    a = 0
    total = 0
    while a != 3:
        a = int(input("Input a number to add an item:\n "))
        if a == 1:
            total += 5.99
            print("1. Mozz Sticks   $5.99 \n2. Fried Pickles   $5.99\n3. Quit")
        elif a == 2:
            total += 5.99
            print("1. Mozz Sticks   $5.99 \n2. Fried Pickles   $5.99\n3. Quit")
        else:
            print("Enter a valid Number")
    else:
        return(float(total))

def Drinks():
    a = 0
    total = 0
    while a != 4:
        print("1. 20 oz   $2.99 \n2. 32 oz   $3.99\n3. Iced Tea   $2.99\n4. Quit")
        a = int(input("Input a number to add an item:\n "))
        if a == 1:
            total += 2.99
            
        elif a == 2:
            total += 3.99
            
        elif a == 3:
            total += 2.99
        else:
            print("Enter a valid number")    
    else:
        return(float(total))

def Entree():
    a = 0
    total = 0
    while a != 5:
        print("1. Steak   $14.99 \n2. Cheeseburger   $11.99\n3. Chicken Strips   $9.99\n4. Salmon   $19.99\n5. Quit")
        a = int(input("Input a number to add an item:\n "))
        if a == 1:
            total += 14.99
        elif a == 2:
            total += 11.99
            
        elif a == 3:
            total += 9.99
            
        elif a == 4:
            total += 19.99
        else:
            print("Enter a valid number")    
    else:
        return(float(total))

def Dessert():
    print("**Dessert**")
    a = 0
    total = 0
    while a != 4:
        print("1. Cheesecake   $7.99 \n2. Chocolate Cake   $8.99\n3. Ice Cream   $4.99\n4. Quit")
        a = int(input("Input a number to add an item:\n "))
        if a == 1:
            total += 7.99
            
        elif a == 2:
            total += 8.99
            
        elif a == 3:
            total += 4.99
        else:
            print("Enter a valid number")    
    else:
        return(float(total))
#Something necessary in Fast-Paced Restaurants is the need for hospitality staff to split the bill, so I added that in for ease of access.
def Calculator(total):
    print("**Splitting the Bill**")
    x = float(input("Input the amount of people splitting the bill: "))
    newtotal = total / x
    print("The new total is $", newtotal)
#Checkout just displays the change that you need to give the customer
def Checkout(total):
    print("Checkout")
    x = float(input("input the amount of cash given"))
    change = x - total
    print("Change: ", change)


#This is just the welcome screen, it displays every time you go back to the menu
def WelcomeScreen():
    print("Welcome to the Simple POS System")
    print("1. Appetizers\n2. Drinks\n3. Entree\n4. Dessert\n5. Calculator\n6. Checkout")
#setting the "choosing menu variable" to 0 and the Total to 0
def main():
    Total = 0
    x = 0
    #This while loop is similar to the other menu loops, I had it display a "Current Total" and when you input a number it selects the appropriate menu
    while x != 6:
        WelcomeScreen()
        print("Total is currently: ", Total)
        x = int(input("Input a number to select a menu: \n"))
        if x == 1:
            Appetizerstotal = Appetizers()
            Total += Appetizerstotal
        
        elif x == 2:
            DrinksTotal = Drinks()
            Total += DrinksTotal
        elif x == 3:
            EntreeTotal = Entree()
            Total += EntreeTotal
        elif x == 4:
            DessertTotal = Dessert()
            Total += DessertTotal
        elif x == 5:
            Calculator(Total)
        else:
            print("Enter a Valid Number")
    else:
#Im having this else loop run the checkout, with the current total
        Checkout(Total)

if __name__ == "__main__":
    main()
