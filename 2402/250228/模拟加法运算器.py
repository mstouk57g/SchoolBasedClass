while True:
    first_number = int(input(""))
    mathcomplice = str(input())
    second_number = int(input(""))
    if mathcomplice == "+":
        answer = first_number + second_number
    elif mathcomplice == "-":
        answer = first_number - second_number
    elif mathcomplice == "*":
        answer = first_number * second_number
    elif mathcomplice == "/" and second_number != 0:
        answer = first_number / second_number
    print(f"{first_number}+{second_number}={answer}")
