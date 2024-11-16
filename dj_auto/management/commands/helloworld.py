from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints hello"
    
    def handle(self, *args, **kwargs):
        self.stdout.write("hello")