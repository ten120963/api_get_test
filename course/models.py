from django.db import models

class Course(models.Model):
	course_id = models.CharField(max_length=10)

	def __str__(self):
		return str(self.course_id)
