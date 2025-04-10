/* I used chat gpt to create the database and populate the tables.
The link for the conversation is right here: https://chatgpt.com/share/67f81f8c-cb44-8006-9def-c3d6c387d59f */
USE CollegeMarketplace;


-- -----------------------------------------------------
-- Insert sample Users
-- -----------------------------------------------------
INSERT INTO Users (name, email, password)
VALUES
('Alice Johnson', 'alice@example.com', 'hashed_pw1'),
('Bob Smith', 'bob@example.com', 'hashed_pw2'),
('Charlie Brown', 'charlie@example.com', 'hashed_pw3'),
('Diana Prince', 'diana@example.com', 'hashed_pw4'),
('Ethan Hall', 'ethan@example.com', 'hashed_pw5'),
('Fiona Davis', 'fiona@example.com', 'hashed_pw6');

-- -----------------------------------------------------
-- Insert sample Categories
-- -----------------------------------------------------
INSERT INTO Categories (name)
VALUES
('Textbooks'),
('Clothes'),
('Furniture'),
('Electronics');

-- -----------------------------------------------------
-- Insert sample Listings
-- -----------------------------------------------------
INSERT INTO Listings (user_id, title, description, price, category_id)
VALUES
(1, 'Calculus Textbook', 'Used but in good condition. Stewart edition.', 40.00, 1),
(2, 'Sofa', 'Grey, 3-seater. Minor wear.', 120.00, 3),
(3, 'iPhone XR', 'Fully functional, minor scratches.', 200.00, 4),
(4, 'Winter Jacket', 'North Face, size M.', 75.00, 2),
(5, 'MacBook Air', '2019 model, 128GB SSD.', 450.00, 4),
(2, 'Microeconomics Book', 'Great for ECON101', 35.00, 1),
(3, 'LED Desk Lamp', 'Touch sensitive with 3 brightness settings.', 15.00, 4),
(6, 'Vintage T-Shirt', 'Graphic tee from 90s.', 20.00, 2),
(5, 'Bookshelf', 'Tall IKEA bookshelf.', 55.00, 3),
(1, 'Psychology Textbook', 'Required for PSY101', 50.00, 1),
(4, 'Bluetooth Speaker', 'JBL, water resistant.', 60.00, 4),
(6, 'Denim Jacket', 'Levi’s, size L.', 30.00, 2),
(1, 'Coffee Table', 'Wooden, minimal scratches.', 35.00, 3),
(2, 'Linear Algebra Book', 'Great condition, barely used.', 45.00, 1),
(3, 'Gaming Mouse', 'Logitech G502 Hero', 25.00, 4);

-- -----------------------------------------------------
-- Insert sample Messages
-- -----------------------------------------------------
INSERT INTO Messages (sender_id, receiver_id, listing_id, message_text)
VALUES
(2, 1, 1, 'Hi! Is the calculus book still available?'),
(1, 2, 1, 'Yes, it is! Want to meet on campus?'),
(3, 2, 2, 'Can you deliver the sofa to the dorms?'),
(2, 3, 2, 'Sure, I can do that this weekend.'),
(4, 5, 5, 'Is the MacBook still under warranty?'),
(5, 4, 5, 'No, warranty expired last year.'),
(6, 1, 10, 'Can I get the psychology book for $40?'),
(1, 6, 10, 'I can do $45, final offer.');
