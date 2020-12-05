from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import os

# Create your models here.

class Score(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def owner_name(self):
        return self.owner.username

    def __unicode__(self):
        return '%s - %d' % (self.owner.username,self.score)

#필요에 따라
class Savegame(models.Model):
    def update_filename(instance,filename):
        #MEDIA_ROOT/savegames/ownername/uuid에 저장된다
        path="savegames/"
        format="%s%s" %(instance.owner.pk,str(uuid.uuid4))# 범용고유식별자
        return os.path.join(path,format)

    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to=update_filename)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    type=models.CharField(max_length=100)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.updated)

class SavegameAdmin(admin.ModelAdmin):
    fields = ('owner', 'name', 'file')
    list_display = ['id', 'owner', 'name', 'created', 'updated']


#admin에 등록
admin.site.register(Score)
admin.site.register(Savegame, SavegameAdmin)
