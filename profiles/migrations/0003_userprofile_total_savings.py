

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_total_savings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='total_savings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
