from api import admin
from django.contrib.auth.models import User
from .models import *
from rest_framework.permissions import IsAdminUser

admin.site.register(
    User, None, permission_classes=(admin.HasPermissionAccess, IsAdminUser)
)
admin.site.register(TestModel)
