

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0003_poster_description_full'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='sku',
        ),
        migrations.AddField(
            model_name='poster',
            name='language',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='poster',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
