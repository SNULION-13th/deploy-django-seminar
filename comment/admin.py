from django.contrib import admin

# Register your models here.
### 아래 추가 ###
from .models import Comment

admin.site.register(Comment)