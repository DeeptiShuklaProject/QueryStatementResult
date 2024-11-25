# from django.db import models
# from django.db import connection
# from decimal import Decimal
# from datetime import date, datetime

# class ProblemStatement(models.Model):
#     statement = models.TextField()  # The problem statement
#     query = models.TextField()      # SQL query
#     result = models.JSONField(blank=True, null=True)  # Stores the result of the query as JSON
#     level = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
#     tag = models.ManyToManyField('Tag')  # Related tags for classification
    

#     def execute_sql_query(self, query):
#         """
#         Executes the query and returns the result as a list of dict (JSON format).
#         Converts Decimal to float and date to string for JSON serialization.
#         """
#         with connection.cursor() as cursor:
#             cursor.execute(query)
#             columns = [col[0] for col in cursor.description]
#             results = [
#                 {
#                     col: (
#                         float(value) if isinstance(value, Decimal) else 
#                         value.isoformat() if isinstance(value, (date, datetime)) else 
#                         value
#                     ) for col, value in zip(columns, row)
#                 }
#                 for row in cursor.fetchall()
#             ]
#         return results

#     def save(self, *args, **kwargs):
#         # Before saving, execute the query and update the result field
#         try:
#             self.result = self.execute_sql_query(self.query)
#         except Exception as e:
#             self.result = {'error': str(e)}  # Handle query errors
#         super(ProblemStatement, self).save(*args, **kwargs)

#     def __str__(self):
#         return f"Problem: {self.statement}, Level: {self.level}"

# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name
from django.db import models
from django.db import connection
from decimal import Decimal
from datetime import date, datetime


class MasterData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    data = models.JSONField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProblemStatement(models.Model):
    statement = models.TextField()  # The problem statement
    sql_query = models.TextField()  # SQL query
    pandas_query = models.TextField(blank=True, null=True)  # Pandas query
    pyspark_query = models.TextField(blank=True, null=True)  # PySpark query
    result = models.JSONField(blank=True, null=True)  # Stores the result of the query as JSON
    level = models.CharField(
        max_length=50,
        choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
    )
    tags = models.ManyToManyField(Tag)  # Related tags for classification
    output = models.TextField(blank=True, null=True)  # Output of the query
    master_data = models.ForeignKey(
        MasterData,
        on_delete=models.CASCADE,
        default=1,  # Replace 1 with the ID of a valid MasterData object in your database
    )

    def execute_sql_query(self, query):
        """
        Executes the query and returns the result as a list of dict (JSON format).
        Converts Decimal to float and date to string for JSON serialization.
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [
                {
                    col: (
                        float(value) if isinstance(value, Decimal) else
                        value.isoformat() if isinstance(value, (date, datetime)) else
                        value
                    ) for col, value in zip(columns, row)
                }
                for row in cursor.fetchall()
            ]
        return results

    def save(self, *args, **kwargs):
        # Before saving, execute the query and update the result field
        try:
            self.result = self.execute_sql_query(self.sql_query)
        except Exception as e:
            self.result = {'error': str(e)}  # Handle query errors
        super(ProblemStatement, self).save(*args, **kwargs)

    def __str__(self):
        return f"Problem: {self.statement}, Level: {self.level}"
