from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def handle_uploaded_file(file):
    file_path = default_storage.save('uploads/' + file.name, ContentFile(file.read()))
    return default_storage.url(file_path)
