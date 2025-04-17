# CampusCart

CampusCart is a full-stack web app that helps college students buy and sell used items like textbooks, furniture, clothes, and electronics. It offers a streamlined experience for signing up, browsing listings, messaging sellers, and managing item data with both SQL and DynamoDB.

---

## Technology Used 

**Frontend**
- HTML (Bootstrap)

**Backend**
- Python (Flask)
- SQL

**Databases Used**
- Amazon RDS (MySQL) for users, listings, categories, and messages tables.
- Amazon DynamoDB for additional user data; crud compliant.

**Hosting**
- Hosted on AWS EC2
- Flask server running with `nohup` for persistant hosting.

---

## Features

- User registration & login (stored in both MySQL & DynamoDB)
- Item listings page (joined with categories and seller names)
- Email and item poster contact informaton for sales.
- Logout button (redirects to homepage)
- Sign up button (directs user to sign up page; data stored in DynamoDB table)
- Sign In page (directs user to listings page after validated)

---

## SQL & DynamoDB Integration

- Users are stored in both MySQL and DynamoDB
- MySQL handles all relationships and foreign keys
- DynamoDB handles non-relational user info

---

## 🚀 How to Run It

1. SSH into your EC2 instance
2. Locate project directory
3. Run:
   ```
   nohup python3 flaskapp.py &
   ```
4. Visit your EC2 public IP at port 8080:
   ```
   http://http://44.212.64.10:8080 ; this is what it is hosted on for me!
   ```

---

## Folder Structure

```
Cs-178-Project1/
  -"CM sql DB and pop/
    -data.sql
    -schema.sql
    -re-schema.sql
  -templates/
    -about.html
    -index.html
    -signup.html
    -login.html
    -listings.html
  -creds.py
  -dbcode.py
  -dynamoCode.py
  -flaskapp.py
  -.gitignore
  -requirements.txt
```
---

## Author
Quinn Ertz
4-17-25


