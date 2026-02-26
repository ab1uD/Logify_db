from .seed import (
    create_user, get_all_users, update_user, delete_user,
    create_animal, get_all_animals, update_animal, delete_animal,
    create_sighting, get_all_sightings, update_sighting, delete_sighting,
    create_feedback, get_all_feedback, update_feedback, delete_feedback
)


def menu_header(title):
    print("\n" + "=" * 60)
    print(f"{title}".center(60))
    print("=" * 60)


#  USER MENU

def user_menu():
    while True:
        menu_header("USER MENU")
        print("1. Create User")
        print("2. View All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            create_user(username, email, password)

        elif choice == "2":
            get_all_users()

        elif choice == "3":
            id = int(input("User ID to update: "))
            username = input("New Username: ")
            email = input("New Email: ")
            password = input("New Password: ")
            update_user(id, username, email, password)

        elif choice == "4":
            id = int(input("User ID to delete: "))
            delete_user(id)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#  ANIMAL MENU 

def animal_menu():
    while True:
        menu_header("ANIMAL MENU")
        print("1. Create Animal")
        print("2. View All Animals")
        print("3. Update Animal")
        print("4. Delete Animal")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("Animal Name: ")
            gender = input("Gender (M/F): ")
            create_animal(name, gender)

        elif choice == "2":
            get_all_animals()

        elif choice == "3":
            id = int(input("Animal ID to update: "))
            name = input("New Name: ")
            gender = input("New Gender (M/F): ")
            update_animal(id, name, gender)

        elif choice == "4":
            id = int(input("Animal ID to delete: "))
            delete_animal(id)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#  SIGHTING MENU 

def sighting_menu():
    while True:
        menu_header("SIGHTING MENU")
        print("1. Create Sighting")
        print("2. View All Sightings")
        print("3. Update Sighting")
        print("4. Delete Sighting")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ")

        if choice == "1":
            user_id = int(input("User ID: "))
            animal_id = int(input("Animal ID: "))
            description = input("Description: ")
            location = input("Location: ")
            age_est = int(input("Age Estimate: "))
            create_sighting(user_id, animal_id, description, location, age_est)

        elif choice == "2":
            get_all_sightings()

        elif choice == "3":
            id = int(input("Sighting ID to update: "))
            user_id = int(input("New User ID: "))
            animal_id = int(input("New Animal ID: "))
            desc = input("New Description: ")
            loc = input("New Location: ")
            age = int(input("New Age Estimate: "))
            update_sighting(id, user_id, animal_id, desc, loc, age)

        elif choice == "4":
            id = int(input("Sighting ID to delete: "))
            delete_sighting(id)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#  FEEDBACK MENU 

def feedback_menu():
    while True:
        menu_header("FEEDBACK MENU")
        print("1. Create Feedback")
        print("2. View All Feedback")
        print("3. Update Feedback")
        print("4. Delete Feedback")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ")

        if choice == "1":
            s_id = int(input("Sighting ID: "))
            msg = input("Message: ")
            create_feedback(s_id, msg)

        elif choice == "2":
            get_all_feedback()

        elif choice == "3":
            id = int(input("Feedback ID to update: "))
            s_id = int(input("New Sighting ID: "))
            msg = input("New Message: ")
            update_feedback(id, s_id, msg)

        elif choice == "4":
            id = int(input("Feedback ID to delete: "))
            delete_feedback(id)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#  MAIN MENU 

def main_menu():
    while True:
        menu_header("LOGIFY - WILDLIFE TRACKING SYSTEM")
        print("1. Manage Users")
        print("2. Manage Animals")
        print("3. Manage Sightings")
        print("4. Manage Feedback")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            animal_menu()
        elif choice == "3":
            sighting_menu()
        elif choice == "4":
            feedback_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()

