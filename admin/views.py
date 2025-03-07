# filepath: /home/inna/Documents/Repo/tenisapp/admin/views.py
import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from admin.forms import CSVUploadForm
from categories.models import Category, UserCategory
from users.models import Profile

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                category = Category.objects.filter(
                    name=row['categoria'],
                ).first()
                print(category.__dict__)
                if not category:
                    messages.error(request, _(
                        'Category does not exist'))
                    continue
                identificator = Profile.objects.filter(
                    identification_number=row['cedula'],
                ).first()
                if identificator:
                    messages.error(request, _(
                        'User with this identification '
                        'already exists'))
                    continue
                user = Profile.objects.create(
                    first_name=row['nombre'],
                    last_name=row['apellido'],
                    username=row['cedula'],
                    identification_number=row['cedula'],
                    age=row['edad'],
                )
                UserCategory.objects.create(
                    user=user,
                    category=category,
                    points=0
                )
            messages.success(request, _(
                'CSV file uploaded successfully'))
            return redirect('admin:upload_csv')
    else:
        form = CSVUploadForm()
    return render(request, 'admin/upload_csv.html', {'form': form})
