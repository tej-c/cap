# Generated by Django 3.0.7 on 2020-06-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tej', '0008_remove_archivearticledefaultemplate_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='defaultemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='ArchiveArticledefaultemplate',
        ),
        migrations.DeleteModel(
            name='TemplateviewArticledefaultemplate',
        ),
    ]
