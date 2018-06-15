# Generated by Django 2.0.2 on 2018-05-15 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0014_auto_20180514_2004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RunType',
            new_name='SampleType',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run_type',
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sequencing.SampleType'),
        ),
        migrations.AlterModelTable(
            name='sampletype',
            table='sequencing_sample_type',
        ),
    ]