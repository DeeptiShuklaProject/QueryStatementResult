# # myapp/management/commands/generate_sql_data.py
# from django.core.management.base import BaseCommand
# from faker import Faker
# from myapp.models import ProblemStatement, Tag

# class Command(BaseCommand):
#     help = 'Generate 100 dummy ProblemStatement records'

#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         levels = ['easy', 'medium', 'hard']
        
#         # Get or create some tags to use
#         tag1, _ = Tag.objects.get_or_create(name="SQL")
#         tag2, _ = Tag.objects.get_or_create(name="RDBMS")
#         tag3, _ = Tag.objects.get_or_create(name="Python")

#         print("Starting data generation...")

#         for i in range(100):
#             # Create ProblemStatement object first
#             problem_statement = ProblemStatement.objects.create(
#                 statement=fake.sentence(),
#                 query="SELECT * FROM table_name;",  # Example SQL query
#                 level=fake.random.choice(levels),
#             )

#             # Assign the ManyToMany field (tags) using set or add methods
#             problem_statement.tag.set([tag1, tag2])  # You can set multiple tags at once

#             # Save the object after setting tags
#             problem_statement.save()

#             print(f"Created ProblemStatement {i+1}: {problem_statement.statement}")

#         print("Data generation completed.")

import csv
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import ProblemStatement, Tag

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
            # Create ProblemStatement object first
            problem_statement = ProblemStatement.objects.create(
                statement=fake.sentence(),
                query="SELECT * FROM table_name;",  # Example SQL query
                level=fake.random.choice(levels),
            )

            # Assign the ManyToMany field (tags) using set or add methods
            problem_statement.tag.set([tag1, tag2])  # You can set multiple tags at once

            # Save the object after setting tags
            problem_statement.save()

            print(f"Created ProblemStatement {i+1}: {problem_statement.statement}")

        print("Data generation completed.")
        
        # Generate CSV file after data creation
        self.export_to_csv()

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
