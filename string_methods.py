def choice(val):
    if val==1:
        count_no_of_vowels(string)
    elif val==2:
        sum_of_digits(string)
    elif val==3:
        special_char_count(string)
    print("-"*72)
        
def count_no_of_vowels(string):
    count=0
    for alphabet in string:
        if alphabet.lower() in ["a","e","i","o","u"]:
            count+=1
    print("                 Total no of vowels :",count)
    
def sum_of_digits(string):
    total=0
    for char in string:
        if char.isnumeric():
            total+=int(char)
        else:
            continue
    print("                      Sum of digits :",total)

def special_char_count(string):
    total=0
    for char in string:
        if char.isalnum():
            continue
        else:
            total+=1
    print("             Total no of characters :",total)

print("|-------------------------EXPERIMENT NO.23-----------------------------|")
print("|        REMOVING A SPECIFIED CHARACTER FROM THE STRING                |")
print("|----------------------------------------------------------------------|")
string=input("                     Enter a string : ")
print("*"*72)
val=int(input("                   Enter your choice: "))
while val!=4:
    choice(val)
    print("1. Count number of vowels")
    print("2. Find sum of digits")
    print("3. Count special characters")
    print("4. Exit")
    val=int(input("                   Enter your choice: "))
