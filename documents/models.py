from pathlib import Path

from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to="uploads/", max_length=100,
                            validators=[FileExtensionValidator(['pdf', 'jpeg', 'png', 'gif', 'tiff'])])

    def get_file_name(self):
        return Path(self.file.url).name

    def __str__(self):
        return self.get_file_name()
