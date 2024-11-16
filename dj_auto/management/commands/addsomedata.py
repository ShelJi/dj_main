from django.core.management.base import BaseCommand
from dj_auto.models import Student


class Command(BaseCommand):
    help = "add data to the model"
    
    def handle(self, *args, **kwargs) -> None:
        dataset = [{"name" : "shelj", "rool_no" : 81, "age" : 70},
                   {"name" : "joe", "rool_no" : 91, "age" : 5}]
        for data in dataset:
            if not Student.objects.filter(rool_no= data["rool_no"]).exists:
                Student.objects.create(name= data["name"], rool_no= data["rool_no"], age= data["age"])
            else:
                self.stdout.write(f"rool no {data['rool_no']} already exists")
        self.stdout.write("Data inserted")