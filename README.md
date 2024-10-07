
# SMOT Socials Project

## 1. Clone the Repository

```bash
git clone https://github.com/NwaforChukwuebuka/smot-socials.git
cd smot-socials
```

## 2. Set Up the Django Backend

### 2.1 Install Python Dependencies

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   pip install -r requirements.txt
   ```

### 2.2 Install PostgreSQL

1. Install PostgreSQL:
   
   - On **Ubuntu/Debian**:
     ```bash
     sudo apt update
     sudo apt install postgresql postgresql-contrib
     ```
   - On **macOS** (via Homebrew):
     ```bash
     brew install postgresql
     ```

2. Start PostgreSQL:
   - On **Linux/macOS**:
     ```bash
     sudo service postgresql start
     ```

### 2.3 Create a PostgreSQL Database

1. Log in to the PostgreSQL prompt:
   ```bash
   sudo -u postgres psql
   ```

2. Create the database and user:
   ```sql
   CREATE DATABASE yourdbname;
   CREATE USER yourdbuser WITH PASSWORD 'yourpassword';
   GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourdbuser;
   ```

### 2.4 Run Migrations and Create Superuser

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Start the Django server:
   ```bash
   python manage.py runserver
   ```

## 3. Set Up the React Frontend

1. Navigate to the frontend directory and install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the React development server:
   ```bash
   npm start
   ```
   The React app will run on `http://localhost:3000`.

## 4. Set Up Environment Variables

1. Install `python-decouple`:
   ```bash
   pip install python-decouple
   ```

2. Create a `.env` file in your Django project root ( ask me for its contents).

3. Create a `.gitignore` file in your Django project root ( ask me for its contents)

