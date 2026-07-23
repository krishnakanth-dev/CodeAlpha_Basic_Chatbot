from datetime import datetime

print("=" * 50)
print("        CODEALPHA BASIC CHATBOT")
print("=" * 50)

print("""
Available Commands:
1. hello
2. how are you
3. time
4. date
5. calculate
6. help
7. bye
""")

while True:

    user_input = input("\nYou: ").lower()

    if user_input == "hello":
        print("Bot: Hi! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I'm doing well. Thanks for asking!")

    elif user_input == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current Time is {current_time}")

    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's Date is {current_date}")

    elif user_input == "calculate":

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            print("\nChoose Operation")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            choice = input("Enter Choice: ")

            if choice == "1":
                result = num1 + num2
            elif choice == "2":
                result = num1 - num2
            elif choice == "3":
                result = num1 * num2
            elif choice == "4":
                if num2 == 0:
                    print("Bot: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Bot: Invalid Operation.")
                continue

            print(f"Bot: Result = {result}")

        except ValueError:
            print("Bot: Please enter valid numbers.")

    elif user_input == "help":

        print("""
Available Commands:

hello         - Greeting
how are you   - Ask chatbot status
time          - Show current time
date          - Show current date
calculate     - Perform calculations
help          - Show commands
bye           - Exit chatbot
""")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")