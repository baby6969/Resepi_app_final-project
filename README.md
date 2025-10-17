# Recipe API - Django REST Framework

A comprehensive recipe management API built with Django REST Framework, featuring user authentication, recipe CRUD operations, and advanced search capabilities.

## 🚀 Features

- **User Authentication**: Token-based authentication with registration and login
- **Recipe Management**: Full CRUD operations for recipes
- **Category & Ingredient Management**: Organize recipes with categories and ingredients
- **Advanced Search**: Search recipes by ingredients, categories, or text
- **Owner Permissions**: Users can only edit their own recipes
- **Pagination**: Efficient data loading with pagination support
- **MySQL Database**: Production-ready database configuration

## 📋 API Endpoints

### Authentication
- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login (returns token)
- `GET /api/users/me/` - Get current user profile

### Recipes
- `GET /api/recipes/` - List all recipes (paginated)
- `POST /api/recipes/` - Create new recipe (authenticated)
- `GET /api/recipes/{id}/` - Get recipe details
- `PUT /api/recipes/{id}/` - Update recipe (owner only)
- `PATCH /api/recipes/{id}/` - Partial update (owner only)
- `DELETE /api/recipes/{id}/` - Delete recipe (owner only)
- `GET /api/recipes/search/` - Search recipes

### Categories & Ingredients
- `GET /api/recipes/categories/` - List all categories
- `POST /api/recipes/categories/` - Create category
- `GET /api/recipes/ingredients/` - List all ingredients
- `POST /api/recipes/ingredients/` - Create ingredient

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- pip

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd Resepi_app_final-project
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment variables**
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

5. **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Optional: create admin user
```

6. **Run the server**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📖 API Usage Examples

### 1. User Registration
**Endpoint:** `POST http://localhost:8000/api/users/register/`

```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "max",
    "email": "max@gmail.com",
    "password": "admin"
  }'
```

**Response:** User created with ID and token

### 2. User Login
**Endpoint:** `POST http://localhost:8000/api/users/login/`

```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "max",
    "password": "admin"
  }'
```

**Response:** `{"token": "6d15a841d9c937655f865f411edd5a0f1ca19978"}`

### 3. Get User Profile
**Endpoint:** `GET http://localhost:8000/api/users/me/`

```bash
curl -X GET http://localhost:8000/api/users/me/ \
  -H "Authorization: Token 6d15a841d9c937655f865f411edd5a0f1ca19978"
```

### 4. Create Recipe (Authenticated)
**Endpoint:** `POST http://127.0.0.1:8000/api/recipes/`

```bash
curl -X POST http://127.0.0.1:8000/api/recipes/ \
  -H "Authorization: Token 6d15a841d9c937655f865f411edd5a0f1ca19978" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Spaghetti Bolognese",
    "description": "Classic Italian pasta with rich tomato meat sauce.",
    "instructions": "1. Boil pasta. 2. Cook sauce. 3. Mix together.",
    "categories": [
      {"name": "Italian"},
      {"name": "Pasta"}
    ],
    "ingredients": [
      {"name": "Tomato"},
      {"name": "Beef"},
      {"name": "Onion"}
    ]
  }'
```

### 5. List All Recipes
**Endpoint:** `GET http://127.0.0.1:8000/api/recipes/`

```bash
curl -X GET http://127.0.0.1:8000/api/recipes/
```

### 6. Search Recipes

#### Search by Category
```bash
curl "http://127.0.0.1:8000/api/recipes/search/?category=pasta"
```

#### Search by Ingredient
```bash
curl "http://127.0.0.1:8000/api/recipes/search/?ingredient=tomato"
```

#### Free Text Search
```bash
curl "http://127.0.0.1:8000/api/recipes/search/?q=tomato"
```

### 7. Categories Management
**List Categories:** `GET http://127.0.0.1:8000/api/recipes/categories/`
**Create Category:** `POST http://127.0.0.1:8000/api/recipes/categories/` (Authenticated)

### 8. Ingredients Management
**List Ingredients:** `GET http://127.0.0.1:8000/api/recipes/ingredients/`
**Create Ingredient:** `POST http://127.0.0.1:8000/api/recipes/ingredients/` (Authenticated)

## 🔧 Project Structure

```
Resepi_app_final-project/
├── Resepi_app/
│   ├── recipes/           # Recipe app
│   │   ├── models.py     # Recipe, Category, Ingredient models
│   │   ├── views.py      # API views
│   │   ├── serializers.py # Data serialization
│   │   ├── urls.py       # Recipe URLs
│   │   └── permissions.py # Custom permissions
│   ├── users/            # User app
│   │   ├── models.py     # User models
│   │   ├── views.py      # User views
│   │   ├── serializers.py # User serialization
│   │   └── urls.py       # User URLs
│   ├── Resepi_app/       # Main project
│   │   ├── settings.py   # Django settings
│   │   └── urls.py       # Main URL configuration
│   └── manage.py         # Django management
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔐 Authentication

The API uses Django REST Framework's Token Authentication:

1. **Register** a new user at `/api/users/register/`
2. **Login** at `/api/users/login/` to get your token
3. **Include the token** in all authenticated requests:
   ```
   Authorization: Token your_token_here
   ```

## 🔍 Search Features

The search endpoint supports multiple query parameters:

- `ingredient=tomato` - Find recipes containing "tomato"
- `category=italian` - Find recipes in "italian" category
- `q=pasta` - Free text search across title, description, instructions
- Combine parameters: `?ingredient=beef&category=main&q=spicy`

## 📊 Pagination

List endpoints support pagination:

- `GET /api/recipes/?page=1&page_size=10`
- Default page size: 10
- Maximum page size: 100

## 🛡️ Permissions

- **Public**: Read access to recipes, categories, ingredients
- **Authenticated**: Create recipes, categories, ingredients
- **Owner Only**: Edit/delete your own recipes
- **Admin**: Full access to all resources

## 🗄️ Database Models

### Recipe
- `user` (ForeignKey to User)
- `title` (CharField)
- `description` (TextField)
- `instructions` (TextField)
- `categories` (ManyToMany to Category)
- `ingredients` (ManyToMany to Ingredient)
- `created_at` (DateTimeField)

### Category
- `name` (CharField)

### Ingredient
- `name` (CharField)

## 🚀 Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Configure proper database credentials
3. Set up static file serving
4. Use a production WSGI server (e.g., Gunicorn)
5. Configure reverse proxy (e.g., Nginx)

## 📝 Requirements

```
Django==5.2.7
djangorestframework==3.16.1
mysqlclient==2.2.7
python-dotenv==1.0.0

```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request


## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the Django REST Framework documentation
- Review the API endpoints using the examples above

---

**Happy Cooking! 🍳**