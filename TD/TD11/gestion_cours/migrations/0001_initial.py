# Generated by Django 3.2.9 on 2021-12-14 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre', models.CharField(max_length=2)),
                ('batiment', models.CharField(max_length=2)),
                ('salle', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('INE', models.IntegerField()),
                ('niveau', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Intervenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('telephone', models.CharField(max_length=15)),
                ('Bureau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnes', to='gestion_cours.bureau')),
            ],
        ),
        migrations.AddConstraint(
            model_name='etudiant',
            constraint=models.UniqueConstraint(fields=('INE',), name="Contrainte d'unicité d'un étudiant"),
        ),
        migrations.AddConstraint(
            model_name='bureau',
            constraint=models.UniqueConstraint(fields=('centre', 'batiment', 'salle'), name="Contrainte d'unicité du bureau"),
        ),
        migrations.AddConstraint(
            model_name='intervenant',
            constraint=models.UniqueConstraint(fields=('nom', 'prenom'), name="Contrainte d'unicité d'une personne"),
        ),
    ]
