import pickle
import csv
import mysql.connector
import matplotlib.pyplot as plt
from collections import Counter

# ---------------- File paths ----------------
CUSTOMERS_FILE = "customers.dat"
MOVIES_FILE = "movies.csv"
BILLING_FILE = "billing.dat"

# ---------------- MySQL Connection ----------------
def get_mysql_connection(db_name=None):
    """
    Connects to MySQL server. If db_name is provided, connects to that database.
    """
    conn_params = {
        "host": "localhost",
        "user": "root",
        "password": "your_mysql_password"  # 
    }
    if db_name:
        conn_params["database"] = db_name
    return mysql.connector.connect(**conn_params)

def create_billing_db_and_table():
    """
    Creates database 'movie_rental_db' and table 'rentals' if not exist.
    """
    # Connect without specifying DB to create it if missing
    
    conn = get_mysql_connection()
    cursor = conn.cursor()
    
    # Create database
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS movie_rental_db")
    cursor.execute("USE movie_rental_db")
    
    # Create rentals table
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rentals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id VARCHAR(50),
            customer_name VARCHAR(100),
            movies TEXT,
            total_price INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# ---------------- Helper functions ----------------
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

def load_billing():
    try:
        with open(BILLING_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return []

def save_billing(bills):
    with open(BILLING_FILE, "wb") as f:
        pickle.dump(bills, f)

# ---------------- Pretty print ----------------
def print_customers_table(customers):
    print("\n{:<5} {:<20} {:<12} {:<25} {:<25} {:<12} {:<8} {:<10}".format(
        "ID", "Name", "Phone", "Email", "Address", "DOB", "Gender", "Membership"))
    print("-"*120)
    for c in customers:
        print("{:<5} {:<20} {:<12} {:<25} {:<25} {:<12} {:<8} {:<10}".format(
            c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7]))

def print_movies_table(movies):
    print("\n{:<5} {:<25} {:<10} {:<6} {:<7} {:<20} {:<12} {:<8} {:<6} {:<6}".format(
        "ID", "Title", "Genre", "Year", "Price", "Director", "Language", "Duration", "Rating", "Copies"))
    print("-"*130)
    for m in movies[1:] if movies and movies[0][0] == "ID" else movies:
        print("{:<5} {:<25} {:<10} {:<6} {:<7} {:<20} {:<12} {:<8} {:<6} {:<6}".format(
            m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9]))

# ---------------- Customers Menu ----------------
def customers_menu():
    while True:
        print("\nCUSTOMERS MENU")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. View All Customers")
        print("4. Search Customer by ID")
        print("5. Modify Customer")
        print("6. Search Customer by Phone")
        print("7. Search Customer by Email")
        print("8. Filter Customers by Address")
        print("9. Filter Customers by Gender")
        print("10. Filter Customers by Membership Type")
        print("11. Sort Customers by Name")
        print("12. Back to Main Menu")

        ch = input("Enter choice: ")
        customers = load_customers()

        if ch == "1":
            cid = input("Enter Customer ID: ")
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            dob = input("Enter Date of Birth (DD/MM/YYYY): ")
            gender = input("Enter Gender: ")
            membership = input("Enter Membership Type (Regular/Premium): ")
            customers.append([cid, name, phone, email, address, dob, gender, membership])
            save_customers(customers)
            print("Customer added successfully.")

        elif ch == "2":
            cid = input("Enter Customer ID to delete: ")
            customers = [c for c in customers if c[0] != cid]
            save_customers(customers)
            print("Customer deleted if existed.")

        elif ch == "3":
            if customers:
                print_customers_table(customers)
            else:
                print("No customers to display.")

        elif ch == "4":
            cid = input("Enter Customer ID to search: ")
            result = [c for c in customers if c[0] == cid]
            if result:
                print_customers_table(result)
            else:
                print("Customer not found.")

        elif ch == "5":
            cid = input("Enter Customer ID to modify: ")
            found = False
            for i in range(len(customers)):
                if customers[i][0] == cid:
                    name = input("Enter new Name: ")
                    phone = input("Enter new Phone: ")
                    email = input("Enter new Email: ")
                    address = input("Enter new Address: ")
                    dob = input("Enter new Date of Birth (DD/MM/YYYY): ")
                    gender = input("Enter new Gender: ")
                    membership = input("Enter new Membership Type (Regular/Premium): ")
                    customers[i] = [cid, name, phone, email, address, dob, gender, membership]
                    found = True
                    break
            save_customers(customers)
            if found:
                print("Customer modified.")
            else:
                print("Customer not found.")

        elif ch == "6":
            phone = input("Enter Phone number to search: ")
            result = [c for c in customers if c[2] == phone]
            if result:
                print_customers_table(result)
            else:
                print("No customer found with this phone number.")

        elif ch == "7":
            email = input("Enter Email to search: ")
            result = [c for c in customers if c[3].lower() == email.lower()]
            if result:
                print_customers_table(result)
            else:
                print("No customer found with this email.")

        elif ch == "8":
            addr = input("Enter part of address to filter: ")
            result = [c for c in customers if addr.lower() in c[4].lower()]
            if result:
                print_customers_table(result)
            else:
                print("No customer found at this address.")

        elif ch == "9":
            gender = input("Enter Gender to filter: ")
            result = [c for c in customers if c[6].lower() == gender.lower()]
            if result:
                print_customers_table(result)
            else:
                print("No customer found with this gender.")

        elif ch == "10":
            membership = input("Enter Membership Type to filter (Regular/Premium): ")
            result = [c for c in customers if c[7].lower() == membership.lower()]
            if result:
                print_customers_table(result)
            else:
                print("No customer found with this membership type.")

        elif ch == "11":
            customers.sort(key=lambda x: x[1].lower())
            save_customers(customers)
            print("Customers sorted by name.")
            print_customers_table(customers)

        elif ch == "12":
            break
        else:
            print("Invalid choice.")

# ---------------- Movies Menu ----------------
def movies_menu():
    while True:
        print("\nMOVIES MENU")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. View All Movies")
        print("4. Search Movie by ID")
        print("5. Modify Movie")
        print("6. Find Movies by Price Range")
        print("7. Find Movies by Genre")
        print("8. Find Movies by Year")
        print("9. Find Movies by Director")
        print("10. Find Movies by Language")
        print("11. Find Movies by Rating")
        print("12. Find Available Movies")
        print("13. Sort Movies by Title")
        print("14. Back to Main Menu")

        ch = input("Enter choice: ")
        movies = load_movies()
        movies_data = movies[1:] if movies and movies[0][0] == "ID" else movies

        if ch == "1":
            mid = input("Enter Movie ID: ")
            title = input("Enter Title: ")
            genre = input("Enter Genre: ")
            year = input("Enter Year of Release: ")
            price = input("Enter Rental Price: ")
            director = input("Enter Director: ")
            language = input("Enter Language: ")
            duration = input("Enter Duration (minutes): ")
            rating = input("Enter Rating (e.g., PG, 13+, R): ")
            copies = input("Enter Number of Copies Available: ")
            movies_data.append([mid, title, genre, year, price, director, language, duration, rating, copies])
            if movies and movies[0][0] == "ID":
                save_movies([movies[0]] + movies_data)
            else:
                save_movies(movies_data)
            print("Movie added successfully.")

        elif ch == "2":
            mid = input("Enter Movie ID to delete: ")
            movies_data = [m for m in movies_data if m[0] != mid]
            if movies and movies[0][0] == "ID":
                save_movies([movies[0]] + movies_data)
            else:
                save_movies(movies_data)
            print("Movie deleted if existed.")

        elif ch == "3":
            if movies_data:
                print_movies_table(movies)
            else:
                print("No movies to display.")

        elif ch == "4":
            mid = input("Enter Movie ID to search: ")
            result = [m for m in movies_data if m[0] == mid]
            if result:
                print_movies_table([movies[0]] + result if movies and movies[0][0] == "ID" else result)
            else:
                print("Movie not found.")

        elif ch == "5":
            mid = input("Enter Movie ID to modify: ")
            found = False
            for i in range(len(movies_data)):
                if movies_data[i][0] == mid:
                    title = input("Enter new Title: ")
                    genre = input("Enter new Genre: ")
                    year = input("Enter new Year: ")
                    price = input("Enter new Price: ")
                    director = input("Enter new Director: ")
                    language = input("Enter new Language: ")
                    duration = input("Enter new Duration: ")
                    rating = input("Enter new Rating: ")
                    copies = input("Enter new Copies Available: ")
                    movies_data[i] = [mid, title, genre, year, price, director, language, duration, rating, copies]
                    found = True
                    break
            if movies and movies[0][0] == "ID":
                save_movies([movies[0]] + movies_data)
            else:
                save_movies(movies_data)
            print("Movie modified." if found else "Movie not found.")

        elif ch == "6":
            min_price = int(input("Enter minimum price: "))
            max_price = int(input("Enter maximum price: "))
            result = [m for m in movies_data if int(m[4]) >= min_price and int(m[4]) <= max_price]
            if result:
                print_movies_table([movies[0]] + result if movies and movies[0][0] == "ID" else result)
            else:
                print("No movies found in this price range.")

        
        
        elif ch == "7":
            genre = input("Enter Genre to search: ")
            result = [m for m in movies if genre.lower() in m[2].lower()]
            if result:
                print_movies_table(result)
            else:
                print("No movies found in this genre.")

        elif ch == "8":
            year = input("Enter Year to search: ")
            result = [m for m in movies if m[3] == year]
            if result:
                print_movies_table(result)
            else:
                print("No movies found for this year.")

        elif ch == "9":
            director = input("Enter Director to search: ")
            result = [m for m in movies if director.lower() in m[5].lower()]
            if result:
                print_movies_table(result)
            else:
                print("No movies found by this director.")

        elif ch == "10":
            language = input("Enter Language to search: ")
            result = [m for m in movies if language.lower() in m[6].lower()]
            if result:
                print_movies_table(result)
            else:
                print("No movies found in this language.")

        elif ch == "11":
            rating = input("Enter Rating to search: ")
            result = [m for m in movies if rating.lower() == m[8].lower()]
            if result:
                print_movies_table(result)
            else:
                print("No movies found with this rating.")

        elif ch == "12":   
            
            movies_data = movies[1:] if movies and movies[0][0] == "ID" else movies
            result = [m for m in movies_data if int(m[9]) > 0]
            if result:

                print_movies_table([movies[0]] + result if movies and movies[0][0] == "ID" else result)
            else:
                print("No movies currently available.")


        elif ch == "13":
            movies.sort(key=lambda x: x[1].lower())
            save_movies(movies)
            print("Movies sorted by title.")
            print_movies_table(movies)

        elif ch == "14":
            break
        else:
            print("Invalid choice.")



# ---------------- Billing Menu ----------------
def billing_menu():
    # make sure database and table exist
    create_billing_db_and_table()

    while True:
        print("\nBILLING MENU")
        print("1. New Rental")
        print("2. Back to Main Menu")
        ch = input("Enter choice: ")

        if ch == "1":
            customers = load_customers()
            movies = load_movies()
            # Skip header row if present
            movies_data = movies[1:] if movies and movies[0][0] == "ID" else movies

            if not customers:
                print("No customers found. Please add customers first.")
                continue
            if not movies_data:
                print("No movies found. Please add movies first.")
                continue

            cid = input("Enter Customer ID: ")
            customer = next((c for c in customers if c[0] == cid), None)
            if not customer:
                print("Customer not found.")
                continue

            print("\nAvailable Movies:")
            for m in movies_data:
                print(m[0], "-", m[1], "- Rs.", m[4])

            rented_movies = []
            total_price = 0
            while True:
                mid = input("Enter Movie ID to rent (or 'done' to finish): ")
                if mid.lower() == "done":
                    break
                found_movie = next((m for m in movies_data if m[0] == mid), None)
                if found_movie:
                    rented_movies.append(found_movie[1])
                    try:
                        total_price += int(found_movie[4])
                    except ValueError:
                        print(f"Invalid price for movie {found_movie[1]}, skipping...")
                else:
                    print("Invalid Movie ID.")

            if rented_movies:
                # Save to MySQL
                conn = get_mysql_connection("movie_rental_db")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO rentals (customer_id, customer_name, movies, total_price) VALUES (%s,%s,%s,%s)",
                    (cid, customer[1], ", ".join(rented_movies), total_price)
                )
                conn.commit()
                cursor.close()
                conn.close()

                print("Total Price: Rs.", total_price)
                print("Rental saved successfully.")
            else:
                print("No movies rented.")

        elif ch == "2":
            break
        else:
            print("Invalid choice.")
# ---------------- Graphs and Reports ----------------

def graph_customers_membership():
    customers = load_customers()
    if not customers:
        print("No customers to display graph.")
        return
    membership_counts = Counter(c[7] for c in customers)
    plt.figure(figsize=(6,6))
    plt.pie(membership_counts.values(), labels=membership_counts.keys(), autopct="%1.1f%%", startangle=90, colors=["skyblue","orange"])
    plt.title("Customer Distribution by Membership Type")
    plt.show()

def graph_movies_genre():
    movies = load_movies()
    if not movies:
        print("No movies to display graph.")
        return
    genre_counts = Counter(m[2] for m in movies)
    plt.figure(figsize=(8,5))
    plt.bar(genre_counts.keys(), genre_counts.values(), color="lightgreen")
    plt.xlabel("Genres")
    plt.ylabel("Number of Movies")
    plt.title("Movies Available by Genre")
    plt.xticks(rotation=45)
    plt.show()

def graph_movies_price():
    movies = load_movies()
    if not movies:
        print("No movies to display graph.")
        return
    prices = [int(m[4]) for m in movies]
    plt.figure(figsize=(8,5))
    plt.hist(prices, bins=10, color="salmon", edgecolor="black")
    plt.xlabel("Price (₹)")
    plt.ylabel("Number of Movies")
    plt.title("Price Distribution of Movies")
    plt.show()

def reports_menu():
    while True:
        print("\nREPORTS MENU")
        print("1. List Customers")
        print("2. List Movies")
        print("3. List Rentals")
        print("4. Customer Membership Graph")
        print("5. Movies Genre Graph")
        print("6. Movies Price Distribution Graph")
        print("7. Back to Main Menu")
        ch = input("Enter choice: ")
        if ch == "1":
            customers = load_customers()
            if customers:
                print_customers_table(customers)
            else:
                print("No customers found.")
        elif ch == "2":
            movies = load_movies()
            if movies:
                print_movies_table(movies)
            else:
                print("No movies found.")
        elif ch == "3":
            conn = get_mysql_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT customer_name, movies, total_price FROM rentals")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            if rows:
                for r in rows:
                    print("Customer:", r[0], "| Movies:", r[1], "| Total: Rs.", r[2])
            else:
                print("No rentals found.")
        elif ch == "4":
            graph_customers_membership()
        elif ch == "5":
            graph_movies_genre()
        elif ch == "6":
            graph_movies_price()
        elif ch == "7":
            break
        else:
            print("Invalid choice.")


# ---------------- Main Menu ----------------
while True:
    print("\nPicture Perfect Rentals")
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
