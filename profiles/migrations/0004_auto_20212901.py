

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_total_savings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='default_zip_or_post',
        ),
    ]
