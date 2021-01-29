

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_auto_20212901'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='description_full',
            field=models.TextField(blank=True, null=True),
        ),
    ]
