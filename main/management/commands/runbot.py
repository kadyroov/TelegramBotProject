from django.core.management.base import BaseCommand
from main.bot import run_bot


class Command(BaseCommand):
    help = "Run Bot"

    def handle(self, *args, **kwargs):
        run_bot()