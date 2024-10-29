import csv
from django.core.management.base import BaseCommand
from calc.models import Customer
class Command(BaseCommand):
    help = 'Import student data from a CSV file'
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')
    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
    # Open the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
    # Iterate over each row in the CSV
            for row in reader:
    # Create a new Customer object and save it to the database
                Customer.objects.create(
                    name=row['name'],
                    age=row['age']
                    )
        self.stdout.write(self.style.SUCCESS('Successfully imported student data'))