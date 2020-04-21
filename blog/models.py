from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def dateFormatter(self):
        year = self.pub_date.year
        month = self.pub_date.month
        date = self.pub_date.day
        return str(year) + '. ' + str(month) + '. ' + str(date)