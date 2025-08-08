CREATE DATABASE movierental;
USE movierental;
CREATE TABLE billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    date_of_purchase DATE,
    customer_number VARCHAR(20),
    customer_phone VARCHAR(15),
    movie_name VARCHAR(100),
    price DECIMAL(10, 2)
);
