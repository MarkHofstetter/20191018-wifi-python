def user_input_positive_number(question = 'Positive Zahl: '):
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            if user_input <= 0:
                print("Zahl muß größer 0 sein")
                continue
            break            
        except ValueError:
            print("ungültige Eingabe")
    return user_input


if __name__ == "__main__":
    a = user_input_positive_number()
    print(a)