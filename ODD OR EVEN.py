# PYTHON PROGRAM TO CHECK WHETHER THE NUMBER IS ODD OR EVEN
def odd_or_even():
    num=int(input("ENTER THE NUMBER:"))

    if(num%2==0):
        print("The number is {} even".format(num))
    else:
        print("The number is {} odd".format(num))
    odd_or_even()

    
odd_or_even()
