'''
Django command to wait for database to be available.
'''

import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''Django command to wait for database'''

    def handle(self, *args, **options):
        '''Entrypoint for command.
        '''

        # Display a message indiciating that the command is running.
        self.stdout.write('Waiting for database...')

        # Initialize a variable to indicate whether the database is ready.
        db_ready = False

        # Continue to check the database until it is ready.
        while not db_ready:
            try:
                # Attempt to check the database.
                self.check(databases=['default'])
                db_ready = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                # Wait 1 second.
                time.sleep(1)
        # Display a message indicating that the database is ready.
        self.stdout.write(self.style.SUCCESS('Database available!'))
