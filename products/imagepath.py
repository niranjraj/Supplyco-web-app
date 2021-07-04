import random,os
from uuid  import uuid4



def get_filename(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)
    if (instance.pk):
        new_filename=instance.pk 
    else :
        new_filename=uuid4().hex
    final_name = f"{new_filename}{ext}"
    return f"products/{final_name}"