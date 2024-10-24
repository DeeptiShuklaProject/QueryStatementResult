from rest_framework import viewsets
from .models import ProblemStatement, Tag
from .serializers import ProblemStatementSerializer, TagSerializer

class ProblemStatementViewSet(viewsets.ModelViewSet):
    queryset = ProblemStatement.objects.all()
    serializer_class = ProblemStatementSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


import csv
from django.http import HttpResponse
from .models import ProblemStatement

def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sql_queries.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the headers
    writer.writerow(['Statement', 'Query', 'Level', 'Tag IDs'])

    # Fetch all records
    sql_queries = ProblemStatement.objects.all()

    # Write data rows
    for query in sql_queries:
        writer.writerow([query.statement, query.query, query.level, query.tag_ids])

    return response

# views.py
from django.http import HttpResponse
import csv
from myapp.models import ProblemStatement

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
