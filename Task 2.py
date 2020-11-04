def show_menu():
    print("Choose an operation")
    print("[1] Check If Prime Number")
    print("[2] Check Palindrome")
    print("[3] Exit")


def checkif_prime():
    if num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(num, "is a prime number")

    else:
        print(num, "is not a prime number")


def checkif_palindrome():
    if word == word[::-1]:
        print(word, "Is A Palindrome")
    else:
        print(word, "Is Not A Palindrome")


show_menu()
Ans = int(input())
while Ans != 3 :

    if Ans == 1:
        num = int(input("Enter Number"))
        checkif_prime()
        show_menu()
    elif Ans == 2:
        word = str(input("Enter String"))
        checkif_palindrome()
        show_menu()
    else:
        print("Invalid Input")
    Ans = int(input())
