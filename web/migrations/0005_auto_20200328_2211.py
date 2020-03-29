# Generated by Django 3.0.4 on 2020-03-28 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_adicionar_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='adicionar',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Status'),
        ),
    ]
