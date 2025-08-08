import csv
import pickle
import os

# ------------------ Customers (Binary File) ------------------

customer_file = "customers.dat"

def add_customer():
    customer = {}
    customer["id"] = input("Enter Customer ID: ")
    customer["name"] = input("Enter Customer Name: ")
    customer["email"] = input("Enter Customer Email: ")
    customer["phone"] = input("Enter Customer Phone: ")
    
    customers = []
    if os.path.exists(customer_file):
        with open(customer_file, "rb") as f:
            customers = pickle.load(f)
    customers.append(customer)
    
    with open(customer_file, "wb") as f:
        pickle.dump(customers, f)
    print("Customer added successfully.")

def delete_customer():
    cid = input("Enter Customer ID to delete: ")
    if os.path.exists(customer_file):
        with open(customer_file, "rb") as f:
            customers = pickle.load(f)
        customers = [c for c in customers if c["id"] != cid]
        with open(customer_file, "wb") as f:
            pickle.dump(customers, f)
        print("Customer deleted successfully.")
    else:
        print("No customer records found.")

def visualise_customers():
    if os.path.exists(customer_file):
        with open(customer_file, "rb") as f:
            customers = pickle.load(f)
        for c in customers:
            print("ID:", c["id"], "Name:", c["name"], "Email:", c["email"], "Phone:", c["phone"])
    else:
        print("No customer records found.")

def search_customer():
    cid = input("Enter Customer ID to search: ")
    if os.path.exists(customer_file):
        with open(customer_file, "rb") as f:
            customers = pickle.load(f)
        for c in customers:
            if c["id"] == cid:
                print("ID:", c["id"], "Name:", c["name"], "Email:", c["email"], "Phone:", c["phone"])
                return
        print("Customer not found.")
    else:
        print("No customer records found.")

def modify_customer():
    cid = input("Enter Customer ID to modify: ")
    if os.path.exists(customer_file):
        with open(customer_file, "rb") as f:
            customers = pickle.load(f)
        for c in customers:
            if c["id"] == cid:
                c["name"] = input("Enter new name: ")
                c["email"] = input("Enter new email: ")
                c["phone"] = input("Enter new phone: ")
                with open(customer_file, "wb") as f:
                    pickle.dump(customers, f)
                print("Customer modified successfully.")
                return
        print("Customer not found.")
    else:
        print("No customer records found.")

def customers_menu():
    while True:
        print("\n--- Customers Menu ---")
        print("1. Add")
        print("2. Delete")
        print("3. Visualise")
        print("4. Search")
        print("5. Modify")
        print("6. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            visualise_customers()
        elif choice == "4":
            search_customer()
        elif choice == "5":
            modify_customer()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

# ------------------ Movies (CSV File) ------------------

movies_file = "movies.csv"

def add_movie():
    movie_id = input("Enter Movie ID: ")
    title = input("Enter Title: ")
    genre = input("Enter Genre: ")
    price = input("Enter Price: ")
    
    with open(movies_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([movie_id, title, genre, price])
    print("Movie added successfully.")

def list_movies():
    if os.path.exists(movies_file):
        with open(movies_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print("ID:", row[0], "Title:", row[1], "Genre:", row[2], "Price:", row[3])
    else:
        print("No movies found.")

def movies_menu():
    while True:
        print("\n--- Movies Menu ---")
        print("1. Add Movie")
        print("2. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_movie()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

# ------------------ Billing (MySQL Placeholder) ------------------

def billing_menu():
    while True:
        print("\n--- Billing Menu ---")
        print("1. Purchase Movies")
        print("2. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            num = int(input("Enter number of movies purchased: "))
            print("[MySQL INSERT operation will be here later]")
            print("Billing completed for", num, "movies.")
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

# ------------------ Reports ------------------

def reports_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. List Customers")
        print("2. List Movies")
        print("3. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            visualise_customers()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

# ------------------ Main Menu ------------------

def main_menu():
    while True:
        print("\n=== ABC Online Movie Rental ===")
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
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

# Run program
main_menu()
