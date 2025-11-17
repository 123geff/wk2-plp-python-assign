def sum_of_integers():
    numbers = input("Enter integers separated by spaces: ")
    num_list = [int(x) for x in numbers.split()]
    print("The sum of the numbers is:", sum(num_list))
    print()


def favorite_books():
    favorite_books = ("The Bible", "The Alchemist", "Rich Dad Poor Dad", "Think and Grow Rich", "Atomic Habits")
    print("My favorite books are:")
    for book in favorite_books:
        print(book)
    print()


def person_info():
    person = {}
    person["name"] = input("Enter your name: ")
    person["age"] = int(input("Enter your age: "))
    person["favorite_color"] = input("Enter your favorite color: ")
    print("Person information:", person)
    print()


def set_intersection():
    set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
    set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))
    common_elements = set1.intersection(set2)
    print("Common elements in both sets:", common_elements)
    print()


def odd_length_words():
    words = ["apple", "banana", "grape", "mango", "peach", "orange"]
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print("Words with odd number of characters:", odd_length_words)
    print()


def main():
    while True:
        print("=== PYTHON MENU PROGRAM ===")
        print("1. Create list of integers and compute sum")
        print("2. Display favorite books")
        print("3. Store person information in a dictionary")
        print("4. Find common elements in two sets")
        print("5. Filter words with odd number of characters")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sum_of_integers()
        elif choice == "2":
            favorite_books()
        elif choice == "3":
            person_info()
        elif choice == "4":
            set_intersection()
        elif choice == "5":
            odd_length_words()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
