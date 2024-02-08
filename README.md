## For backend setup go to "remarcable" directory

### `cd remarcable`

### 1. Set up Virtual Environment

### `python -m venv venv`
### `source venv/bin/activate`

### 2. Install Dependencies

### `pip install -r requirements.txt`

### 3. Apply Migrations

### `python manage.py migrate`

### 4. Import products

### `python import_products.py`

### 5. Start the project

### `python manage.py runserver`

## For frontend setup go to "frontend" directory

### `cd frontend`

### 1. Download dependencies

### `npm install`

### 2. Start the project

### `npm start`

Open [http://127.0.0.1:3000](http://127.0.0.1:3000) to view it in your browser.
