#user name
user = input("What is your name? ")
print(("\n" + f"Hello {user}! Welcome to EcoRide").upper().center(30))

standard=100
premium=200

while True: 
    print("\n" + "1. Bike hire")
    print("2. Rates")
    print("3. Payments")
    print("4. Leave")
    
    option=input("\n" + "Select an option: ")

    if option=="1":

        optionuser=input("\n" + "Which bike would you like? (standard/premium?) ").lower()

        if optionuser=="standard":
            bikevalue=standard
        elif optionuser=="premium":
            bikevalue=premium
        else:
            print("\n" + "\33[31mSelect the correct option\33[0m")
            continue

        while True:
            try:
                time=int(input("\n" + "Enter the value in minutes "))
                
                if time<=0:
                    print("\n" + "Invalid. Put a correct information")
                else:
                    break
            except ValueError:
                print("\33[31mError\33[0m")
                continue

        total=bikevalue*time

        print("\n" + "Payment method")
        print("\n" + "Cash")
        print("Card")
        print("Points")

        payment=input("\n" + "What is your payment method?: ").lower()

        descount=0
        forfeit=50
        backlong=0

        if time>60 and payment=="card":
            descount=total*0.10
        
        elif time<10 and payment=="points":
            descount=0

        day=input("\n" + "Is weekend? yes/no ")
        
        if day=="yes" :
            backlong=total*0.05

        penalty=input("\n" + "Was the bike returned on time? yes/no ")

        if penalty=="no":
            ticket=forfeit+total

            
        totally=total-descount+backlong+forfeit

        print("-" * 30 )
        print((f"You have to pay: \33[32m${totally}\33[0m").center(30))
        print("-" * 30 )

    
        print(f"| {'Bike':15}| {optionuser.capitalize():<10}|")
        print(f"| {'Time':15}| {time:<10}|")
        print(f"| {'Total':15}| {total:<10}|")
        print(f"| {'Descount':15}| ${descount:<9,.0f}|".replace(',', '.'))
        print(f"| {'Forfeit':15}| {forfeit:<10}|")

        print("-" * 30 )
        print(f"| {'Total to Pay':15}| \33[32m${totally:<9,.0f}\33[0m|".replace(',', '.'))
        print("-" * 30  +"\n")

    elif option=="2":
            print(("\n" + f"\33[32mStandard bike {standard} for minute\33[0m").upper().center(30))
            print("\n" + "-Ideal for short trips")
            print("-Comfortable, durable, and easy to use")
            print("-Includes basic maintenance, adjusted brakes, and safety lights")

            print(("\n" + f"\33[32mPremium bike {premium} for minute\33[0m").upper().center(30))
            print("\n" + "-Greater comfort, with advanced gear shifting")
            print("-Includes complete maintenance, insurance, and additional accessories")

    elif option=="3":
        if optionuser is None:
            print("\n" + "You need first select the bike for pay")
            continue

        print("-" * 30 )
        print(("Calculation of the amount payable ").center(30))
        print("-" * 30  +"\n")

        print(f"Type of bike {optionuser}")
        print(f"Price of service {total}")
        print(f"Time of use {time}")
        print(f"Payment method {payment}")

        print("-" * 30 )
        print((f"Totality \33[32m${totally}\33[0m").center(30))
        print("-" * 30  +"\n")

        pay=input("\n" + "Would you like to proceed with the payment? yes/no ")

        if pay=="yes":
            print("\n" + "Payment made successfully, we hope you come back soon.")
            optionuser=None
            total=None
            time=0
            payment=None
            totally=0
        else:
            print("\n" + "Review your request, otherwise the process will be canceled.")

    elif option == "4":
            print(("\33[34mThank you for visiting us.\33[0m").upper().center(30))
            break
    
    else:
        print("\n" + "\33[31mInvalid option. Please try again.\33[0m")