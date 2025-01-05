import pandas as pd
from django.core.management.base import BaseCommand
from hr.models import Actions
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'actions.csv')
        try:
            df = pd.read_csv(data_dir, encoding='windows-1256')
            # df['enamel'] = df['enamel'].fillna(value="waleed"),
            # df['job'] = df['job'].fillna(value="wale"),
            # df['active'] = df['active'].fillna(value=0),
            # df['salary'] = df['salary'].fillna(value=0),
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Cannot read data'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error reading'))

        for _,row in df.iterrows():
            Actions.objects.create(
                action_name = row['actions'],
            )
        self.stdout.write(self.style.SUCCESS('completed suucessfuly with no errors'))
        return

