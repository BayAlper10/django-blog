
from __future__ import unicode_literals

from django.contrib import admin

from blog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
