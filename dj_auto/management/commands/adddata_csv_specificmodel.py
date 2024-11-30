from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv


class Command(BaseCommand):
    help = 'Add data to specific model from CSV, it requires file_path and model_name'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Enter the file path')
        parser.add_argument('model_name', type=str, help='Enter the model name')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"].capitalize()
        
        self.stdout.write(f"Processing CSV file at: {file_path}")
        self.stdout.write(f"Target model: {model_name}")
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        
        self.stdout.write(f"app_config: {app_config}")
            
        if not model:
            raise CommandError(f"{model_name} is not exists")

        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                
                model_fields = [field.name for field in model._meta.get_fields()]
                for data in reader:
                    filtered_data = {key: value for key, value in data.items() if key in model_fields}
                    model.objects.create(**filtered_data)
            
            self.stdout.write(self.style.SUCCESS("Datas imported"))
        
        except FileNotFoundError:
            raise CommandError(f"The file at {file_path} was not found.")
        except Exception as e:
            raise CommandError(f"An error occurred: {str(e)}")
        
        
# import csv
# from django.core.management.base import BaseCommand, CommandError
# from django.apps import apps


# class Command(BaseCommand):
#     help = 'Imports data into a specific model from a CSV file. Requires file_path and model_name.'

#     def add_arguments(self, parser):
#         parser.add_argument(
#             'file_path', type=str, help='Path to the CSV file to be imported.'
#         )
#         parser.add_argument(
#             'model_name', type=str, help='Name of the model to import data into.'
#         )

#     def handle(self, *args, **kwargs):
#         # Retrieve the arguments
#         file_path = kwargs['file_path']
#         model_name = kwargs['model_name'].capitalize()

#         self.stdout.write(f"Processing CSV file at: {file_path}")
#         self.stdout.write(f"Target model: {model_name}")

#         # Get the model from the app
#         model = None
#         for app_config in apps.get_app_configs():
#             try:
#                 model = apps.get_model(app_config.label, model_name)
#                 break
#             except LookupError:
#                 continue

#         if not model:
#             raise CommandError(f"Model '{model_name}' does not exist.")
        
#         # Read the CSV and import data
#         try:
#             with open(file_path, 'r', encoding='utf-8-sig') as file:
#                 reader = csv.DictReader(file)

#                 # Check if CSV columns match model fields
#                 model_fields = [field.name for field in model._meta.get_fields()]
#                 for data in reader:
#                     # Validate the CSV columns against model fields
#                     filtered_data = {key: value for key, value in data.items() if key in model_fields}

#                     # Create model instance and save
#                     model.objects.create(**filtered_data)

#                 self.stdout.write(self.style.SUCCESS("Data imported successfully."))

#         except FileNotFoundError:
#             raise CommandError(f"The file at {file_path} was not found.")
#         except Exception as e:
#             raise CommandError(f"An error occurred: {str(e)}")
