from django.core.management.base import BaseCommand, CommandParser
from dj_auto.models import Student
import csv


class Command(BaseCommand):
    help = "add datas from csv to models"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument("file_path", type=str, help="give the path of the file")
        
    def handle(self, *args, **kwargs) -> None:
        with open(kwargs["file_path"], 'r', encoding='utf-8-sig') as file:
            datas = csv.DictReader(file)
            for data in datas:
                # print(data["age"])
                # print(data["name"])
                # print(data)
                if not Student.objects.filter(rool_no = data["rool_no"]).exists:
                    Student.objects.create(**data)
                else:
                    self.stdout.write(self.style.WARNING(f"{data["rool_no"]} Rool no already exists"))
            self.stdout.write(self.style.SUCCESS("Datas imported"))
                