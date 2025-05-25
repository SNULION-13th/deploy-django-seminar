from django.contrib import admin

# Register your models here.
### 아래 추가 ###
from .models import Tag

admin.site.register(Tag)