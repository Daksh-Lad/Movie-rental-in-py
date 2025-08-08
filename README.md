# ABC Online Movie Rental

A simple Python-based prototype for an online movie rental system.  
This project manages customers and movies locally using binary (`.dat`) and CSV files,  
while billing information is stored in a MySQL database.

## Features
- **Customer Management** – Add and list customers.
- **Movie Management** – Add and list available movies.
- **Billing (MySQL)** – Store billing details including:
  - Date of purchase
  - Customer number
  - Customer phone number
  - Movie name
  - Price
- **Reports** – Display customers and movies.
- **Persistent Storage** – Uses `pickle` for customers, CSV for movies, and MySQL for billing.

## Requirements
- Python 3.x
- MySQL Server
- Required Python libraries:
  - `mysql-connector-python`

## MySQL Setup
Run the following command in MySQL before using the program:

```sql
CREATE DATABASE movierental;
USE movierental;
CREATE TABLE billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_of_purchase DATE,
    customer_number VARCHAR(20),
    phone_number VARCHAR(20),
    movie_name VARCHAR(100),
    price DECIMAL(10,2)
);
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movierental.git
   ```
2. Install dependencies:
   ```bash
   pip install mysql-connector-python
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## File Structure
```
movierental/
│
├── customers.dat       # Stores customer data
├── movies.csv          # Stores movie data
├── main.py             # Main Python program
├── README.md           # Project documentation
```

## License
This project is for educational purposes only.
