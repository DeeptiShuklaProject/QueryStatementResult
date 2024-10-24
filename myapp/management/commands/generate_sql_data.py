
import csv
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import ProblemStatement, Tag
import random

class Command(BaseCommand):
    help = 'Generate 100 dummy ProblemStatement records and export them to a CSV file'

    def handle(self, *args, **kwargs):
        fake = Faker()
        levels = ['easy', 'medium', 'hard']
        
        # Get or create some tags to use
        tag1, _ = Tag.objects.get_or_create(name="SQL")
        tag2, _ = Tag.objects.get_or_create(name="RDBMS")
        tag3, _ = Tag.objects.get_or_create(name="Python")

        print("Starting data generation...")

        for i in range(100):
            # Randomly select a difficulty level for each problem
            selected_level = random.choice(levels)
            query = self.generate_sql_query(selected_level)

            # Create ProblemStatement object
            problem_statement = ProblemStatement.objects.create(
                statement=fake.sentence(),
                query=query,
                level=selected_level,  # Assign the chosen level
            )

            # Assign the ManyToMany field (tags) using set or add methods
            problem_statement.tag.set([tag1, tag2])  # You can set multiple tags at once

            # Save the object after setting tags
            problem_statement.save()

            print(f"Created ProblemStatement {i+1}: {problem_statement.statement}, Level: {selected_level}")

        print("Data generation completed.")
        
        # Generate CSV file after data creation
        self.export_to_csv()

    def generate_sql_query(self, level):
        """
        Generates a variety of SQL queries based on the difficulty level.
        """

        # Easy queries
        easy_queries = [
            "SELECT * FROM employees;",  # Basic SELECT query
            "SELECT name, age FROM students WHERE age > 18;",  # SELECT with WHERE clause
            "SELECT product_name, price FROM products WHERE price < 100;",  # SELECT with condition
            "SELECT COUNT(*) FROM orders;",  # Simple aggregate query
            "SELECT name FROM customers ORDER BY name ASC;"  # SELECT with ORDER BY
        ]

        # Medium queries
        medium_queries = [
            "SELECT department, COUNT(*) FROM employees GROUP BY department;",  # GROUP BY
            "SELECT category, AVG(price) FROM products GROUP BY category;",  # GROUP BY with AVG
            "SELECT name FROM students WHERE age BETWEEN 18 AND 25;",  # WHERE with BETWEEN
            "SELECT employee_name, salary FROM employees WHERE salary > 50000 ORDER BY salary DESC;",  # SELECT with ORDER BY and condition
            "SELECT country, SUM(sales) FROM sales GROUP BY country HAVING SUM(sales) > 1000;"  # GROUP BY with HAVING clause
        ]

        # Hard queries
        hard_queries = [
            """
            SELECT e.name, e.salary, d.name as department_name
            FROM employees e
            JOIN departments d ON e.department_id = d.id
            WHERE e.salary > (SELECT AVG(salary) FROM employees)
            ORDER BY e.salary DESC;
            """,  # Subquery with JOIN and ORDER BY
            """
            SELECT c.name, COUNT(o.id) AS order_count
            FROM customers c
            LEFT JOIN orders o ON c.id = o.customer_id
            GROUP BY c.name
            HAVING COUNT(o.id) > 5;
            """,  # JOIN with GROUP BY and HAVING
            """
            SELECT product_name, price FROM products
            WHERE price = (SELECT MAX(price) FROM products);
            """,  # Subquery to find max price
            """
            SELECT d.department_name, AVG(e.salary) AS avg_salary
            FROM employees e
            JOIN departments d ON e.department_id = d.id
            GROUP BY d.department_name
            ORDER BY avg_salary DESC;
            """,  # JOIN with GROUP BY and ORDER BY
            """
            WITH top_salaries AS (
                SELECT employee_id, salary, RANK() OVER (ORDER BY salary DESC) AS rank
                FROM employees
            )
            SELECT * FROM top_salaries WHERE rank <= 3;
            """  # Common Table Expression (CTE) with ranking
        ]

        # Return query based on difficulty level
        if level == 'easy':
            return random.choice(easy_queries)
        elif level == 'medium':
            return random.choice(medium_queries)
        elif level == 'hard':
            return random.choice(hard_queries)

    def export_to_csv(self):
        # Path to save the CSV file
        file_path = r'D:\problemstatement\myapp\management\commands\sql_queries_data\sql_queries.csv'

        # Open the file and write to CSV
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # Write the headers
            csvwriter.writerow(['Statement', 'Query', 'Level', 'Tag Names'])

            # Fetch all ProblemStatements
            problem_statements = ProblemStatement.objects.all()

            # Write each ProblemStatement's data to the CSV
            for problem in problem_statements:
                # Get related tag names
                tags = ', '.join(tag.name for tag in problem.tag.all())
                csvwriter.writerow([problem.statement, problem.query, problem.level, tags])

        print(f"CSV file '{file_path}' generated successfully!")
