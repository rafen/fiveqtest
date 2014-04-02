# -*- coding: utf-8 -*-
import datetime
import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from devotional.models import Devotional


DEFAULT_YEAR = getattr(settings, 'DEFAULT_YEAR', 2014)


class Command(BaseCommand):
    args = '<csv_file>'
    help = 'Specify a CSV file from where to imports the devotionals'

    def handle(self, *args, **options):
        if len(args) == 1:
            try:
                reader = csv.reader(open(args[0], 'rb'))
            except Exception as e:
                raise CommandError('Could not find  "%s" error: %s' % (args[0], e))
        else:
            raise CommandError('Please specify a file as an argument')


        cnt = 0
        for index, row in enumerate(reader):
            # Skip first row
            if index == 0:
                continue

            month = int(row[1])
            day = int(row[2])

            try:
                date = datetime.date(DEFAULT_YEAR, month, day)
            except ValueError as e:
                self.stdout.write('Error: Data in row %s not imported. Error: %s \n\n' \
                                    % (cnt, e))


            # Create object in database
            dev, created = Devotional.objects.get_or_create(title=row[0], date=date, body=row[3])

            cnt += 1
            self.stdout.write('Created devotional ID: %s\n\n' % dev.id)

        self.stdout.write('%s devotionals created.\n' % cnt)