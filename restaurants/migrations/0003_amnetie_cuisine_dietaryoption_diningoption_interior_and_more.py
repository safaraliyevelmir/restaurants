# Generated by Django 4.2.1 on 2023-07-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_rename_nane_restaurant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amnetie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DietaryOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DiningOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='restaurants/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviews_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='service_status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='amenitie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_amnetie', to='restaurants.amnetie'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_cuisine', to='restaurants.cuisine'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='dietary_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_dietary', to='restaurants.dietaryoption'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='dining_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_diening', to='restaurants.diningoption'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='interior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_interior', to='restaurants.interior'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='payment_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_payment', to='restaurants.paymentoption'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='service_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_service', to='restaurants.serviceoption'),
        ),
    ]