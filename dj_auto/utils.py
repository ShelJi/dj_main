from django.apps import apps


def get_custom_models():
    default_models = ["LogEntry","Permission","Group","User","ContentType","Session","Uploads"]
    
    # models = apps.get_models(app_label="dj_auto")
    models = apps.get_models()
    
    model_name = []
    for model in models:
        if model.__name__ not in default_models:
            model_name.append(model.__name__)
    
    return model_name