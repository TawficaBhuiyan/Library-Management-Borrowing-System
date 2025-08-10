📚 Library Management & Borrowing System – Django REST API
A Library Management System built with Django & Django REST Framework, featuring user authentication, book browsing, borrowing/returning functionality, admin controls, and penalty tracking.

🚀 Features
User Authentication – Register & login using JWT tokens.

Books Browsing – Search & filter by author or category.

Borrowing System

Limit: Max 3 active borrows per user.

Automatic 14-day due date.

Atomic inventory updates to avoid race conditions.

Return System – Early return supported, penalty points for late returns.

Penalty Tracking – 1 point/day late.

Admin Controls – Manage books, authors, and categories.

API Rate Limiting – 100 requests/day per user.

🛠️ Technologies Used
Python 3.11+

Django 5.2

Django REST Framework

djangorestframework-simplejwt – JWT Authentication

django-filter – API filtering

SQLite – Default database

📦 Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/TawficaBhuiyan/Library-Management-Borrowing-System.git
cd Library-Management-Borrowing-System

2️⃣ Create & Activate Virtual Environment
windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Create Admin User
python manage.py createsuperuser

6️⃣ Start the Server
python manage.py runserver

API Base URL: http://127.0.0.1:8000/api/

📄 API Documentation & Postman Collection
📂 File: /postman/Library API.postman_collection.json
🔗 Direct Import Link: [Library API Postman Collection](https://bhuiyantawfica-6894740.postman.co/workspace/fec7e347-8333-4389-8b1b-f1a74a707048/documentation/47473556-555b534e-1d94-4a0c-8700-348b232c54ad)


How to Import in Postman:

File → Import → Upload .json file, or

Use "Import from URL" with the above link.

📚 API Endpoints
Endpoint	Method	Description	Access
/api/register/	POST	Register a new user	Public
/api/login/	POST	Obtain JWT token	Public
/api/books/	GET	List books (filter by author/category)	Public
/api/books/{id}/	GET	Retrieve book details	Public
/api/books/	POST	Create a new book	Admin only
/api/books/{id}/	PUT	Update book details	Admin only
/api/books/{id}/	DELETE	Delete a book	Admin only
/api/authors/	GET	List authors	Admin only
/api/categories/	GET	List categories	Admin only
/api/borrow/	POST	Borrow a book	Authenticated users
/api/borrow/	GET	List active borrows	Authenticated users
/api/return/	POST	Return a borrowed book	Authenticated users
/api/users/{id}/penalties/	GET	Get penalty points	Admin or self

🔄 Borrowing & Return Logic
Borrowing:

Checks available copies.

Creates borrow record with 14-day due date.

Atomically decreases available copies.

Returning:

Records return date.

Atomically increases available copies.

If late → 1 penalty point per overdue day.

⚠️ Assumptions & Known Limitations
Logout handled client-side by deleting JWT token (no server blacklisting).

No email notifications for due dates/penalties.

SQLite is used for simplicity — production should use PostgreSQL/MySQL.

No frontend — backend API only.

Rate limit: 100 requests/day (configurable).

🗂 ER Diagram
📂 /Diagram/ER_Diagram.draw.io.png
Shows:

User (normal & admin)

Author

Category

Book

Borrow

📜 License
Educational use only.

📬 Contact
Tawfica Bhuiyan
📧 Email: bhuiyantawfica@gmail.com
💻 GitHub: TawficaBhuiyan

