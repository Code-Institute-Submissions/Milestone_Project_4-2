

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='disc_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='poster',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poster',
            name='publisher',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]