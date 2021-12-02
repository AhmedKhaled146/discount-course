print(" \" Welcome to our mid courses we have multi courses like : Pyhton, C++, C# And Ruby \"\n ########## PLZ Enter Your Information and choose Your course ##########  ")
name = str(input("what is Your name ? ")).capitalize()
age = int(input("what is Your age ? "))
counrty = str(input("what is Your country ? ").capitalize())
course = input("What Course You Will Choose ? ").capitalize()
price = float(500)
if age > 30:
    print(f" ############## Welcome master {name}. ############## ")
    if counrty == "Egypt" or "KSA" or "Mika":
        print(
            f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 30% Your total price is {(price * 70)/100}")
    elif counrty == "Marco" or "Qatar" or "Bahreen":
        print(
            f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 10% Your total price is {(price * 90)/100}")
    else:
        print(
            f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 5% Your total price is {(price * 95)/100}")
elif age < 30:
    check = input(" Are You a student ? Y/N :").capitalize()
    if check == "Y":
        print(f" ############## Welcome dear son {name} ############## ")
        if counrty == "Egypt" or "KSA" or "Mika":
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 45% Your total price is {(price * 55)/100}")
        elif counrty == "Marco" or "Qatar" or "Bahreen":
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 20% Your total price is {(price * 80)/100}")
        else:
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 5% Your total price is {(price * 95)/100}")
    elif check == "N":
        if counrty == "Egypt" or "KSA" or "Mika":
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 25% Your total price is {(price * 75)/100}")
        elif counrty == "Marco" or "Qatar" or "Bahreen":
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 15% Your total price is {(price * 85)/100}")
        else:
            print(
                f"Your country is : {counrty} , Your course you choise is {course} and Your discount is 5% Your total price is {(price * 95)/100}")
