while True:

    # Ask user to enter country currency code 
    choose_currency=input("enter currency code (Usd , Pkr , Ind ,Euro) : ")

    # store the value of usd in different fields 
    pk=283.53
    ind=87.56
    europe=0.86
    dictionary={
        "pk":"Pkr",
        "ind":"Ind",
        "euro":"Euro"
    }

    match choose_currency:
    # -----for Usd to other currencies-----
        case "Usd":
            try:

                a=input("enter currency code you want to convert from usd ")
                b=float(input("enter amount"))
                if a ==dictionary["pk"]:
                    print(b,"Us Dollar$= ",b*pk," Pkr")
                elif a==dictionary["ind"]:
                    print(b,"Us Dollar$ = ",b*ind," Ind rupees")
                elif a==dictionary["euro"]:
                    print(b,"Usd To Euro= ",b*europe," Euro")
                else:
                    print("INVALID INPUT! PLEASE enter correct country code")

            except:
                print("INVALID INPUT! PLEASE TRY AGAIN")

    # ------------for Pkr to usd----------
        case "Pkr":
            try :
                p=float(input("enter how much Pakistani rupees do you wanna covert to dollar "))
                print(p,"Pakistani Rupess =",p/pk,"USD$",end=" ")
            except:
                print("INVALID INPUT! PLEASE TRY AGAIN")
            

            
    
    # ---------For Ind rupees to pkr----------

        case "Ind":
            try :
                i=float(input("enter how much Indian rupees do you wanna covert to dollar "))
                print(i,"Indian rupees =",i/ind,"USD$",end=" ")
            except:
                print("INVALID INPUT! PLEASE TRY AGAIN")
    # -----------For Euro--------------------

        case "Euro":
            try:

                e=float(input("enter how much Euros do you wanna covert to dollar "))
                print(e,"Euro =",e/europe,"USD$",end=" ")
            except:
                print("INVALID INPUT! PLEASE TRY AGAIN")
    

        case _:
            print("choose currency code correctly (Usd , Pkr , Ind ,Euro)")
    print("\n\n")
    q=input("Do you wanna continue the Currency converter program (Yes) or (No)")
    match q:
            case "Yes":
                print("\n")
                continue

            case "No":
                 print("\n\n")
                 print("Program has been stopped")

                 break
            case _:
                print("\n\n")
                print("You gave a wrong command \nProgram has been stopped")
                
                break
             

