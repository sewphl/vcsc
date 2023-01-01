# Generated by Django 4.1.4 on 2022-12-29 17:07

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subbanners', '0002_subbannerpage_lead_text_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subbannerpage',
            name='lead_text_p',
        ),
        migrations.AddField(
            model_name='subbannerpage',
            name='banner_lead_text',
            field=models.CharField(blank=True, help_text='Subheading text under banner title', max_length=140),
        ),
        migrations.AlterField(
            model_name='subbannerpage',
            name='lead_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Short lead text, if needed'),
        ),
    ]