from django.contrib import admin

### 아래 추가 ###
from .models import Comment

admin.site.register(Comment)
