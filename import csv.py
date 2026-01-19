import csv

FILENAME = "scores.csv"

def add_score(username, score):
    with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer .writerow({username, score})
    pass

def show_scores():
    with open("scores.csv", "r") as file:
        contents = file.read()
        print(contents.strip())
    pass


def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
