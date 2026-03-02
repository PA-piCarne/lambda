from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('estudiante', 'Estudiante'), ('profesor', 'Profesor')], max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=150)),
                ('edad', models.PositiveIntegerField()),
                ('telefono', models.CharField(max_length=30)),
                ('nota_contabilidad', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('nota_programacion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('nota_lenguaje_comunicacion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_estudiante', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilProfesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=120)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_profesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
