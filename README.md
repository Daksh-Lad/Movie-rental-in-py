# Movie-rental-in-py


🎬 ABC Online Movie Rental
A simple Python + MySQL program for managing a small movie rental system.
This is a school project demonstrating file handling in Python, basic database connectivity with MySQL, and menu-driven programming.

📂 Features
Customers — Add and list customers (stored in a .dat binary file).

Movies — Add and list movies (stored in a .csv file).

Billing (MySQL) — Store billing records in MySQL with:

Purchase date

Customer number

Customer phone number

Movie name

Price

Reports — View customer and movie records.

🗂 File Structure
bash
Copy
Edit
.
├── main.py           # Main program file
├── customers.dat     # Binary file storing customer details
├── movies.csv        # CSV file storing movie details
├── README.md         # This file
🛠 Requirements
Python 3.x

MySQL Server

Python library: mysql-connector-python

Install MySQL connector:

bash
Copy
Edit
pip install mysql-connector-python
🗄 MySQL Setup
Run this in your MySQL terminal to create the database and billing table:

sql
Copy
Edit
CREATE DATABASE movierental;
USE movierental;

CREATE TABLE billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_date DATE,
    customer_number VARCHAR(50),
    phone_number VARCHAR(15),
    movie_name VARCHAR(100),
    price DECIMAL(10,2)
);
▶️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/movierental.git
Navigate to the folder:

bash
Copy
Edit
cd movierental
Run the program:

bash
Copy
Edit
python main.py
📌 Notes
Only billing is stored in MySQL.

Customers are stored in a binary .dat file.

Movies are stored in a .csv file.

