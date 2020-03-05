# Generated by Django 3.0.3 on 2020-03-05 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50, null=True)),
                ('is_in_promotion', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bundles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('image_url', models.CharField(max_length=2000, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='HarvestYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'harvest_years',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'measures',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('small_image', models.CharField(max_length=2000, null=True)),
                ('big_image1', models.CharField(max_length=2000, null=True)),
                ('big_image2', models.CharField(max_length=2000, null=True)),
                ('big_image3', models.CharField(max_length=2000, null=True)),
                ('energy', models.CharField(max_length=10, null=True)),
                ('carbonydrate', models.CharField(max_length=10, null=True)),
                ('protein', models.CharField(max_length=10, null=True)),
                ('fat', models.CharField(max_length=10, null=True)),
                ('mineral', models.CharField(max_length=100, null=True)),
                ('vitamin', models.CharField(max_length=100, null=True)),
                ('is_in_stock', models.CharField(max_length=30, null=True)),
                ('is_on_sale', models.BooleanField(default=False)),
                ('discount_rate', models.CharField(max_length=50, null=True)),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('ingredient', models.CharField(max_length=2000, null=True)),
                ('thumbnail_url', models.CharField(max_length=2000, null=True)),
                ('company', models.CharField(max_length=45, null=True)),
                ('posting_date', models.CharField(max_length=45, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('direction', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'recipes',
            },
        ),
        migrations.CreateModel(
            name='RecipeRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Recipe')),
            ],
            options={
                'db_table': 'recipe_recommendations',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'sorts',
            },
        ),
        migrations.CreateModel(
            name='SimilarProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_product', to='products.Product')),
                ('to_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_product', to='products.Product')),
            ],
            options={
                'db_table': 'similar_products',
                'unique_together': {('from_product', 'to_product')},
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('is_on_display', models.BooleanField(default=True)),
                ('recipe', models.ManyToManyField(through='products.RecipeRecommendation', to='products.Recipe')),
            ],
            options={
                'db_table': 'recommendations',
            },
        ),
        migrations.AddField(
            model_name='reciperecommendation',
            name='recommendation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Recommendation'),
        ),
        migrations.CreateModel(
            name='RecipeKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Keyword')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Recipe')),
            ],
            options={
                'db_table': 'recipe_keywords',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'product_categories',
            },
        ),
        migrations.CreateModel(
            name='ProductBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Bundle')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'product_bundles',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='bundle',
            field=models.ManyToManyField(through='products.ProductBundle', to='products.Bundle'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(through='products.ProductCategory', to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='harvest_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.HarvestYear'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Measure'),
        ),
        migrations.AddField(
            model_name='product',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Recipe'),
        ),
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Season'),
        ),
        migrations.AddField(
            model_name='product',
            name='similar_product',
            field=models.ManyToManyField(through='products.SimilarProduct', to='products.Product'),
        ),
    ]
