from django.shortcuts import render
from django.views import View
from .utils import get_custom_models
from .models import Uploads
from django.conf import settings
# from django.base.management import call_command
from icecream import ic


class ImportData(View):
    def get(self, request):
        models = get_custom_models()
        context = {"models" : models}
        return render(request, "dj_auto/import_data.html", context)
    
    def post(self, request):
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")
        upload = Uploads.objects.create(uploaded_file=file_path, model_name=model_name)
        
        # construct full path
        relative_path = upload.uploaded_file.url
        base_url = settings.BASE_DIR
        
        actual_path = str(base_url) + str(relative_path)
        
        print(actual_path)
        
        
        models = get_custom_models()
        context = {"models" : models}
        return render(request, "dj_auto/import_data.html", context)