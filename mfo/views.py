from django.shortcuts import render
import os
from django.http import JsonResponse
from .config import BASE_DIR

# Create your views here.


def load_file_system(request):

    current_dir = request.GET.get('new_dir')
    child_dirs = []
    child_files = []
    if current_dir is None or current_dir == 'undefined' or current_dir == BASE_DIR:
        current_dir = BASE_DIR
    else:
        child_dirs.append(('..', os.path.split(current_dir)[0]))
    tmp = os.listdir(current_dir)
    for item in tmp:
        if item[0] != '.' and os.path.isdir(os.path.join(current_dir, item)):
            child_dirs.append((item, os.path.join(current_dir, item)))
        elif item[0] != '.':
            child_files.append((item, os.path.join(current_dir, item)))
    data = {
        'current_dir': current_dir,
        'child_dirs': child_dirs,
        'child_files': child_files
    }
    return JsonResponse(data)


def index(request):
    return render(request, 'mfo/index.html')
