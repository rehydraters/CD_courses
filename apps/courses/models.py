from __future__ import unicode_literals

from django.db import models

# Create your models here.
class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Course name must be at least 6 characters long."
        if len(postData['desc']) < 16:
            errors['desc'] = "Course description must be at least 16 characters long."
        return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = courseManager()