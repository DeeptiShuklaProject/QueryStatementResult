# from rest_framework import viewsets
# from .models import ProblemStatement, Tag
# from .serializers import ProblemStatementSerializer, TagSerializer

# class ProblemStatementViewSet(viewsets.ModelViewSet):
#     queryset = ProblemStatement.objects.all()
#     serializer_class = ProblemStatementSerializer


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# import csv
# from django.http import HttpResponse
# from .models import ProblemStatement

# def export_csv(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="sql_queries.csv"'

#     # Create a CSV writer
#     writer = csv.writer(response)

#     # Write the headers
#     writer.writerow(['Statement', 'Query', 'Level', 'Tag IDs'])

#     # Fetch all records
#     sql_queries = ProblemStatement.objects.all()

#     # Write data rows
#     for query in sql_queries:
#         writer.writerow([query.statement, query.query, query.level, query.tag_ids])

#     return response

# # views.py
# from django.http import HttpResponse
# import csv
# from myapp.models import ProblemStatement

# def download_csv(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="sql_queries.csv"'

#     # Create a CSV writer
#     writer = csv.writer(response)

#     # Write the headers
#     writer.writerow(['Statement', 'Query', 'Level', 'Tag Names'])

#     # Fetch all ProblemStatements
#     problem_statements = ProblemStatement.objects.all()

#     # Write data rows
#     for problem in problem_statements:
#         tags = ', '.join(tag.name for tag in problem.tag.all())
#         writer.writerow([problem.statement, problem.query, problem.level, tags])

#     return response

from rest_framework import viewsets
from .models import ProblemStatement, Tag, MasterData
from .serializers import ProblemStatementSerializer, TagSerializer, MasterDataSerializer

class ProblemStatementViewSet(viewsets.ModelViewSet):
    """ViewSet for ProblemStatement model."""
    queryset = ProblemStatement.objects.all()
    serializer_class = ProblemStatementSerializer


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for Tag model."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MasterDataViewSet(viewsets.ModelViewSet):
    """ViewSet for MasterData model."""
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer


import csv
from django.http import HttpResponse

def export_csv(request):
    """
    Export ProblemStatement data as a CSV file.
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="problem_statements.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the headers
    writer.writerow(['Statement', 'SQL Query', 'Pandas Query', 'PySpark Query', 'Level', 'Tags', 'Master Data'])

    # Fetch all ProblemStatements
    problem_statements = ProblemStatement.objects.all()

    # Write data rows
    for problem in problem_statements:
        # Get tag names
        tags = ', '.join(tag.name for tag in problem.tag.all())
        # Get MasterData title
        master_data_title = problem.master_data.title if problem.master_data else "N/A"

        # Write row data
        writer.writerow([
            problem.statement,
            problem.sql_query,
            problem.pandas_query,
            problem.pyspark_query,
            problem.level,
            tags,
            master_data_title
        ])

    return response

from django.http import HttpResponse
import csv
from .models import ProblemStatement

def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sql_queries.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the headers
    writer.writerow(['Statement', 'Query', 'Level', 'Tag Names'])

    # Fetch all ProblemStatements
    problem_statements = ProblemStatement.objects.all()

    # Write data rows
    for problem in problem_statements:
        tags = ', '.join(tag.name for tag in problem.tag.all())
        writer.writerow([problem.statement, problem.query, problem.level, tags])

    return response
