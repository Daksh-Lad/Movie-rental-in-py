import mysql.connector

# MySQL connection function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # change to your MySQL username
        password="",   # change to your MySQL password
        database="rentals"
    )

# ---------------- Customers Menu ----------------
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
        db = connect_db()
        cur = db.cursor()

        if ch == "1":
            cid = input("Enter Customer ID: ")
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (cid, name, phone))
            db.commit()
            print("Customer added successfully.")

        elif ch == "2":
            cid = input("Enter Customer ID to delete: ")
            cur.execute("DELETE FROM customers WHERE cid=%s", (cid,))
            db.commit()
            print("Customer deleted if existed.")

        elif ch == "3":
            cur.execute("SELECT * FROM customers")
            for row in cur.fetchall():
                print(row)

        elif ch == "4":
            cid = input("Enter Customer ID to search: ")
            cur.execute("SELECT * FROM customers WHERE cid=%s", (cid,))
            data = cur.fetchone()
            if data:
                print(data)
            else:
                print("Customer not found.")

        elif ch == "5":
            cid = input("Enter Customer ID to modify: ")
            name = input("Enter new Name: ")
            phone = input("Enter new Phone: ")
            cur.execute("UPDATE customers SET name=%s, phone=%s WHERE cid=%s", (name, phone, cid))
            db.commit()
            print("Customer modified.")

        elif ch == "6":
            db.close()
            break
        else:
            print("Invalid choice.")

        db.close()

# ---------------- Movies Menu ----------------
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
        db = connect_db()
        cur = db.cursor()

        if ch == "1":
            mid = input("Enter Movie ID: ")
            title = input("Enter Title: ")
            price = input("Enter Rental Price: ")
            cur.execute("INSERT INTO movies VALUES (%s, %s, %s)", (mid, title, price))
            db.commit()
            print("Movie added successfully.")

        elif ch == "2":
            mid = input("Enter Movie ID to delete: ")
            cur.execute("DELETE FROM movies WHERE mid=%s", (mid,))
            db.commit()
            print("Movie deleted if existed.")

        elif ch == "3":
            cur.execute("SELECT * FROM movies")
            for row in cur.fetchall():
                print(row)

        elif ch == "4":
            mid = input("Enter Movie ID to search: ")
            cur.execute("SELECT * FROM movies WHERE mid=%s", (mid,))
            data = cur.fetchone()
            if data:
                print(data)
            else:
                print("Movie not found.")

        elif ch == "5":
            mid = input("Enter Movie ID to modify: ")
            title = input("Enter new Title: ")
            price = input("Enter new Rental Price: ")
            cur.execute("UPDATE movies SET title=%s, price=%s WHERE mid=%s", (title, price, mid))
            db.commit()
            print("Movie modified.")

        elif ch == "6":
            db.close()
            break
        else:
            print("Invalid choice.")

        db.close()

# ---------------- Billing Menu ----------------
def billing_menu():
    while True:
        print("\nBILLING MENU")
        print("1. New Rental")
        print("2. Back to Main Menu")

        ch = input("Enter choice: ")
        db = connect_db()
        cur = db.cursor()

        if ch == "1":
            cur.execute("SELECT * FROM customers")
            customers = cur.fetchall()
            if not customers:
                print("No customers found.")
                db.close()
                continue

            cur.execute("SELECT * FROM movies")
            movies = cur.fetchall()
            if not movies:
                print("No movies found.")
                db.close()
                continue

            cid = input("Enter Customer ID: ")
            cur.execute("SELECT * FROM customers WHERE cid=%s", (cid,))
            customer = cur.fetchone()
            if not customer:
                print("Customer not found.")
                db.close()
                continue

            print("\nAvailable Movies:")
            for m in movies:
                print(m[0], "-", m[1], "- Rs.", m[2])

            rented_movies = []
            total_price = 0

            while True:
                mid = input("Enter Movie ID to rent (or 'done' to finish): ")
                if mid.lower() == "done":
                    break
                cur.execute("SELECT * FROM movies WHERE mid=%s", (mid,))
                movie = cur.fetchone()
                if movie:
                    rented_movies.append(movie[1])
                    total_price += int(movie[2])
                else:
                    print("Invalid Movie ID.")

            if rented_movies:
                cur.execute(
                    "INSERT INTO billing (cid, customer_name, movies, total_price) VALUES (%s, %s, %s, %s)",
                    (cid, customer[1], ", ".join(rented_movies), total_price)
                )
                db.commit()
                print("Total Price: Rs.", total_price)
                print("Rental saved successfully.")

        elif ch == "2":
            db.close()
            break
        else:
            print("Invalid choice.")

        db.close()

# ---------------- Reports Menu ----------------
def reports_menu():
    while True:
        print("\nREPORTS MENU")
        print("1. List Customers")
        print("2. List Movies")
        print("3. List Rentals")
        print("4. Back to Main Menu")

        ch = input("Enter choice: ")
        db = connect_db()
        cur = db.cursor()

        if ch == "1":
            cur.execute("SELECT * FROM customers")
            for row in cur.fetchall():
                print(row)
        elif ch == "2":
            cur.execute("SELECT * FROM movies")
            for row in cur.fetchall():
                print(row)
        elif ch == "3":
            cur.execute("SELECT * FROM billing")
            for row in cur.fetchall():
                print(row)
        elif ch == "4":
            db.close()
            break
        else:
            print("Invalid choice.")

        db.close()

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
