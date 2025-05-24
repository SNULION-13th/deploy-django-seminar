from django.contrib import admin

### 아래 추가 ###
from .models import Like, Post

admin.site.register(Post)
admin.site.register(Like)

