import csv

from django.core.management.base import BaseCommand
from tqdm import tqdm

from tasks.models import Task


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('output', nargs=None, type=str)

    def handle(self, *args, **options):
        with open(options['output'], 'w', encoding='utf-8') as out:
            writer = csv.writer(out)
            for task in tqdm(Task.objects.all()):
                writer.writerow([
                    task.name,
                    task.answers.count(),
                    task.done,
                    task.student
                ])

        self.stdout.write(
            self.style.SUCCESS(
                f"Exported all tasks to {options['output']}"))
