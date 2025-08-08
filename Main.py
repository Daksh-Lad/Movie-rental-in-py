import pickle
import csv

# -------------------------
# File paths
# -------------------------
CUSTOMERS_FILE = "customers.dat"
MOVIES_FILE = "movies.csv"

# -------------------------
# Helper functions
# -------------------------
def load_customers():
    try:
        with open(CUSTOMERS_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return []

def save_customers(customers):
    with open(CUSTOMERS_FILE, "wb") as f:
        pickle.dump(customers, f)

def load_movies():
    try:
        with open(MOVIES_FILE, "r", newline="") as f:
            return list(csv.reader(f))
    except:
        return []

def save_movies(movies):
    with open(MOVIES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(movies)

# -------------------------
# Customers Menu
# -------------------------
def customers_menu():
    while True:
        print("\nCUSTOMERS MENU")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. Visualise All Customers")
        print("4. Search Customer")
        print("5. Modify Customer")
        print("6. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            customers = load_customers()
            cid = input("Enter Customer ID: ")
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            customers.append([cid, name, phone])
            save_customers(customers)
            print("Customer added successfully.")

        elif ch == "2":
            customers = load_customers()
            cid = input("Enter Customer ID to delete: ")
            customers = [c for c in customers if c[0] != cid]
            save_customers(customers)
            print("Customer deleted if existed.")

        elif ch == "3":
            customers = load_customers()
            for c in customers:
                print(c)

        elif ch == "4":
            customers = load_customers()
            cid = input("Enter Customer ID to search: ")
            found = False
            for c in customers:
                if c[0] == cid:
                    print(c)
                    found = True
                    break
            if not found:
                print("Customer not found.")

        elif ch == "5":
            customers = load_customers()
            cid = input("Enter Customer ID to modify: ")
            found = False
            for i in range(len(customers)):
                if customers[i][0] == cid:
                    name = input("Enter new Name: ")
                    phone = input("Enter new Phone: ")
                    customers[i] = [cid, name, phone]
                    found = True
                    break
            save_customers(customers)
            if found:
                print("Customer modified.")
            else:
                print("Customer not found.")

        elif ch == "6":
            break
        else:
            print("Invalid choice.")

# -------------------------
# Movies Menu
# -------------------------
def movies_menu():
    while True:
        print("\nMOVIES MENU")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. Visualise All Movies")
        print("4. Search Movie")
        print("5. Modify Movie")
        print("6. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            movies = load_movies()
            mid = input("Enter Movie ID: ")
            title = input("Enter Title: ")
            price = input("Enter Rental Price: ")
            movies.append([mid, title, price])
            save_movies(movies)
            print("Movie added successfully.")

        elif ch == "2":
            movies = load_movies()
            mid = input("Enter Movie ID to delete: ")
            movies = [m for m in movies if m[0] != mid]
            save_movies(movies)
            print("Movie deleted if existed.")

        elif ch == "3":
            movies = load_movies()
            for m in movies:
                print(m)

        elif ch == "4":
            movies = load_movies()
            mid = input("Enter Movie ID to search: ")
            found = False
            for m in movies:
                if m[0] == mid:
                    print(m)
                    found = True
                    break
            if not found:
                print("Movie not found.")

        elif ch == "5":
            movies = load_movies()
            mid = input("Enter Movie ID to modify: ")
            found = False
            for i in range(len(movies)):
                if movies[i][0] == mid:
                    title = input("Enter new Title: ")
                    price = input("Enter new Rental Price: ")
                    movies[i] = [mid, title, price]
                    found = True
                    break
            save_movies(movies)
            if found:
                print("Movie modified.")
            else:
                print("Movie not found.")

        elif ch == "6":
            break
        else:
            print("Invalid choice.")

# -------------------------
# Billing Menu (Placeholder)
# -------------------------
def billing_menu():
    while True:
        print("\nBILLING MENU")
        print("1. Ask how many movies rented")
        print("2. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            qty = int(input("Enter number of movies rented: "))
            print("Movies rented:", qty)
        elif ch == "2":
            break
        else:
            print("Invalid choice.")

# -------------------------
# Reports Menu
# -------------------------
def reports_menu():
    while True:
        print("\nREPORTS MENU")
        print("1. List Customers")
        print("2. List Movies")
        print("3. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            customers = load_customers()
            for c in customers:
                print(c)
        elif ch == "2":
            movies = load_movies()
            for m in movies:
                print(m)
        elif ch == "3":
            break
        else:
            print("Invalid choice.")

# -------------------------
# Main Menu
# -------------------------
while True:
    print("\nABC MENU")
    print("1. Customers")
    print("2. Movies")
    print("3. Billing")
    print("4. Reports")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        customers_menu()
    elif choice == "2":
        movies_menu()
    elif choice == "3":
        billing_menu()
    elif choice == "4":
        reports_menu()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
