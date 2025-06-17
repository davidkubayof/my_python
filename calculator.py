def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "אי אפשר לחלק באפס!"
    return x / y

def main():
    print("מחשבון פשוט")
    print("בחר פעולה:")
    print("1. חיבור")
    print("2. חיסור")
    print("3. כפל")
    print("4. חילוק")

    choice = input("הכנס את הבחירה שלך (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("הכנס מספר ראשון: "))
            num2 = float(input("הכנס מספר שני: "))
        except ValueError:
            print("יש להזין מספרים בלבד.")
            return

        if choice == '1':
            print("תוצאה:", add(num1, num2))
        elif choice == '2':
            print("תוצאה:", subtract(num1, num2))
        elif choice == '3':
            print("תוצאה:", multiply(num1, num2))
        elif choice == '4':
            print("תוצאה:", divide(num1, num2))
    else:
        print("בחירה לא חוקית")

if __name__ == "__main__":
    main()
