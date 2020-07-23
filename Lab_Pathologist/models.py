# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import Permission, User

# # Create your models here.
# class LabPathologist(models.Model):
# 	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
# 	venue  		= models.CharField(max_length=500)
# 	title       = models.CharField(max_length=500)
# 	description = models.TextField(max_length=500, blank=True)
# 	event_date  = models.DateField(null=True, blank=True)
# 	event_time  = models.TimeField(null=True, blank=True)
# 	link_url    = models.CharField(max_length=500, null=True, blank=True)
# 	image       = models.ImageField(upload_to = 'all_events/', blank=True)
# 	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
# 	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)


# 	def __str__(self):
# 		return self.title + ' - ' + self.venue

# 	class Meta:
# 		ordering = ["-timestamp", "-updated"]