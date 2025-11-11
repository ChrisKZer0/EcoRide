#user name
user = input("What is your name? ")
print((f"Hello {user}. Welcomo to EcoRide").upper().center(30))

standard=100
premium=200

while True: 
    print("1. Bike hire")
    print("2. Rates")
    print("3. Payments")
    print("4. Leave")
    
    option=input("Select an option: ")

    if option=="1":

        optionuser=input("Which bike would you like? (standard/premium?) ").lower()

        if optionuser=="standard":
            bikevalue=standard
        elif optionuser=="premium":
            bikevalue=premium
        else:
            print("Select the correct option")
            continue

        while True:
            try:
                time=int(input("Enter the value in minutes "))
                
                if time<=0:
                    print("Invalid. Put a correct information")
                else:
                    break
            except ValueError:
                print("Error")
                continue

        total=bikevalue*time

        print("Payment method")
        print("Cash")
        print("Card")
        print("Points")

        payment=input("What is your payment method?: ").lower()

        descount=0
        forfeit=50
        backlong=0

        if time>60 and payment=="card":
            descount=total*0.10
        
        elif time<10 and payment=="points":
            descount=0

        day=input("Is weekend? yes/no ")
        
        if day=="yes" :
            backlong=total*0.05

        penalty=input("Was the bike returned on time? si/no ")

        if penalty=="no":
            ticket=forfeit+total

            

        totally=total-descount+backlong+forfeit
        print(f"You have to pay: {totally}")



        print(f"| {'Bike':15}| {optionuser.capitalize():<10}|")
        print(f"| {'Time':15}| {time:<10}|")
        print(f"| {'Total':15}| {total:<10}|")
        print(f"| {'Descount':15}| ${descount:<9,.0f}|".replace(',', '.'))
        print(f"| {'Forfeit':15}| {forfeit:<10}|")
        print(f"| {'Total to Pay':15}| \33[32m${totally:<9,.0f}\33[0m|".replace(',', '.'))
        





        









    
    elif option == "4":
        print("Thank you for visiting us.")
        break