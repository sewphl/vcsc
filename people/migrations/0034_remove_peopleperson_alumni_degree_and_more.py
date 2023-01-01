# Generated by Django 4.1.4 on 2022-12-30 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0033_alter_peopleperson_current_employer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peopleperson',
            name='alumni_degree',
        ),
        migrations.RemoveField(
            model_name='peopleperson',
            name='alumni_year',
        ),
        migrations.AddField(
            model_name='peopleperson',
            name='alumni_degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.peopledegreealumni'),
        ),
        migrations.AddField(
            model_name='peopleperson',
            name='alumni_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.peoplegradyearalumni'),
        ),
    ]