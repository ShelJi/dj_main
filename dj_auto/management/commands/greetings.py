from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "says hello to the user"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="give your name")
    
    def handle(self, *args, **kwargs):
        self.stdout.write(f"hello {kwargs['name']}")
        self.stderr.write(f"hello {kwargs['name']}")
        self.stdout.write(self.style.WARNING(f"hello {kwargs['name']}"))
        self.stdout.write(self.style.SUCCESS(f"hello {kwargs['name']}"))