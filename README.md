# Problem Statement and Tag API

This Django project provides API endpoints to manage `ProblemStatement` and `Tag` models and allows downloading SQL queries as CSV files with different configurations.



## Setup

1. Clone this repository and navigate to the project directory.
git clone https://github.com/DeeptiShuklaProject/QueryStatementResult.git

2. Install the dependencies:

    pip install -r requirements.txt

3. Run migrations:
    
    python manage.py migrate
 
4. Start the Django development server:
   
    python manage.py runserver


## Models

### ProblemStatement

This model represents a problem statement with the following fields:
- **statement**: The statement of the problem.
- **query**: SQL query associated with the problem.
- **level**: Difficulty level of the problem.
- **tags**: Foreign key relation to `Tag`.





## CSV Export

This project includes two views for exporting SQL queries in CSV format, providing different configurations for `Tag` data.

### Exporting CSV with Tag IDs

This view exports SQL queries with associated tag IDs.

- **URL**: when you visit /download-csv/, the browser will automatically download the generated CSV file.
- **Description**: Generates a CSV file with the following columns: `Statement`, `Query`, `Level`, `Tag IDs`.
  

