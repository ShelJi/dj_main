from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import datetime
import csv
from icecream import ic
ic.disable()


class Command(BaseCommand):
    help = "Export the datas of any model to CSV"
    
    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="Give the model name")
        
    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                ic(app_config.label)
                model = apps.get_model(app_config.label, model_name)
                break
            
            except LookupError:
                continue
        
        ic(model)
        
        if not model:
            CommandError(f"{model_name} does not exists in installed apps")
            
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_path = f"{model_name}_dumpdata_{timestamp}.csv"
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([field.name for field in model._meta.fields])
            
            data = model.objects.all()
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
                
        self.stdout.write(self.style.SUCCESS("Datas Exported"))