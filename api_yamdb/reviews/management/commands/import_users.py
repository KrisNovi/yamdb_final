from csv import DictReader
from django.conf import settings
import os.path
from django.core.management import BaseCommand

from reviews.models import User


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from csv"

    def handle(self, *args, **options):
        # Show this when the data already exist in the database
        if User.objects.exists():
            print('category data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # Show this before loading the data into the database
        print("Loading users data")

        # Code to load the data into database
        for row in DictReader(
            open(os.path.join(settings.BASE_DIR, 'static', 'users.csv'))
        ):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                confirmation_code=''
            )
            user.save()
