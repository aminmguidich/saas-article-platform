from django.db import migrations
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    def create_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        if User.objects.exists():
            return
        
        superuser = User.objects.create_superuser(
            username ="admin",
            email = "example@exemple.com",
            password = "admin",
            last_login=timezone.now()
        )
        superuser.save()
    operations = [
        migrations.RunPython(create_superuser),
    ]
