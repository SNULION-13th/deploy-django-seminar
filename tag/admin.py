from django.contrib import admin

### 아래 추가 ###
from .models import Tag

admin.site.register(Tag)
