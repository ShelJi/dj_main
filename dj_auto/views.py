from django.shortcuts import render


def import_data(request):
    return render(request, "dj_auto/import_data.html")