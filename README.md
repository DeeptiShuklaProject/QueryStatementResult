# Problem Statement and Tag API

This Django project provides API endpoints to manage `ProblemStatement` and `Tag` models and allows downloading SQL queries as CSV files with different configurations.



## Setup

1. Clone this repository and navigate to the project directory.
git clone https://github.com/DeeptiShuklaProject/QueryStatementResult.git

2. Install the dependencies:

    pip install -r requirements.txt

3. Run migrations:
    python manage.py makemigrations
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

### API Roots
{
    "problem-statements": "http://127.0.0.1:8000/api/problem-statements/",
    "tags": "http://127.0.0.1:8000/api/tags/",
    "master-data": "http://127.0.0.1:8000/api/master-data/"
}






  

