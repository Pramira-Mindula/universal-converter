# 🌍 Universal Converter

<p align="center">
  <b>A modern, interactive conversion web app built with Django + Tailwind CSS</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/TailwindCSS-UI-38B2AC?style=for-the-badge&logo=tailwind-css" />
  <img src="https://img.shields.io/badge/API-ExchangeRate-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" />
</p>

---

## ✨ Features

### 💱 Real-Time Currency Conversion
- Live exchange rates via API
- Top 10 popular currencies
- No hardcoded rates
- Dynamic dropdown population

### 📏 Length Conversion
- Meter ↔ Kilometer

### 🌡 Temperature Conversion
- Celsius ↔ Fahrenheit

### ⚡ Instant Conversion (AJAX)
- Converts while typing
- No page reload
- No submit button needed

### 🧠 Smart UX
- Swap button (⇄)
- Prevents same unit selection
- Remembers last selected conversion type (localStorage)

### 🎨 Modern UI
- Split-screen layout
- Rounded rectangle container
- Gradient background
- Tailwind CSS styling
- Live result panel on right side

---

## 🛠 Tech Stack

| Layer      | Technology |
|------------|------------|
| Backend    | Django (Python) |
| Frontend   | HTML + Tailwind CSS |
| API        | ExchangeRate API |
| AJAX       | JavaScript Fetch API |
| Storage    | Browser LocalStorage |

---

## 📂 Project Structure
```
mysite/
    ├── manage.py
    ├── db.sqlite3
    ├── currency/
    |   ├── templates/
    |   |     ├── currency/
    |   |     |     ├── home.html
    │   ├── views.py
    │   ├── models.py
    │   ├── urls.py
    │   └── ...
    └── mysite/
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
        └── ...

```


---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/universal-converter.git
cd universal-converter
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
```

### 3️⃣ Install Dependencies
```
pip install django requests
```

### 4️⃣ Run Development Server
```
python manage.py runserver
```

### Open
```
http://127.0.0.1:8000/
```

### 🔌 API Used
```
https://open.er-api.com/v6/latest/USD
```

## 🧠 How It Works

### 🔹 Frontend
- User selects conversion type and units.
- JavaScript sends request using fetch().
- Result updates instantly in right panel.

### 🔹 Backend
- home() renders UI.
- convert() returns JSON response.
- Currency conversion fetches live API data.

## 🔥 Future Improvements
- Add currency flags
- Add conversion history (database)
- Cache exchange rates
- Add loading animation
- Add dark mode toggle
-  Deploy to production (Render / Railway)

## 👨‍💻 Author

Pramira Mindula
GitHub: https://github.com/Pramira-Mindula

## ⭐ If you like this project
- Give it a star on GitHub!
