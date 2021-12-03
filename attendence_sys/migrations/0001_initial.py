# Generated by Django 3.0.5 on 2020-06-26 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('registration_id', models.CharField(max_length=200, null=True)),
                ('branch', models.CharField(choices=[
                                                        ('CMPE 200','CMPE 200'),
                                                        ('CMPE 202','CMPE 202'),
                                                        ('CMPE 203','CMPE 203'),
                                                        ('CMPE 206','CMPE 206'),
                                                        ('CMPE 207','CMPE 207'),
                                                        ('CMPE 208','CMPE 208'),
                                                        ('CMPE 209','CMPE 209'),
                                                        ('CMPE 212','CMPE 212'),
                                                        ('CMPE 213','CMPE 213'),
                                                        ('CMPE 214','CMPE 214'),
                                                        ('CMPE 217','CMPE 217'),
                                                        ('CMPE 219','CMPE 219'),
                                                        ('CMPE 220','CMPE 220'),
                                                        ('CMPE 221','CMPE 221'),
                                                        ('CMPE 225','CMPE 225'),
                                                        ('CMPE 226','CMPE 226'),
                                                        ('CMPE 227','CMPE 227'),
                                                        ('CMPE 232','CMPE 232'),
                                                        ('CMPE 234','CMPE 234'),
                                                        ('CMPE 235','CMPE 235'),
                                                        ('CMPE 236','CMPE 236'),
                                                        ('CMPE 237','CMPE 237'),
                                                        ('CMPE 238','CMPE 238'),
                                                        ('CMPE 239','CMPE 239'),
                                                        ('CMPE 240','CMPE 240'),
                                                        ('CMPE 241','CMPE 241'),
                                                        ('CMPE 242','CMPE 242'),
                                                        ('CMPE 243','CMPE 243'),
                                                        ('CMPE 244','CMPE 244'),
                                                        ('CMPE 245','CMPE 245'),
                                                        ('CMPE 249','CMPE 249'),
                                                        ('CMPE 250','CMPE 250'),
                                                        ('CMPE 251','CMPE 251'),
                                                        ('CMPE 252','CMPE 252'),
                                                        ('CMPE 255','CMPE 255'),
                                                        ('CMPE 256','CMPE 256'),
                                                        ('CMPE 257','CMPE 257'),
                                                        ('CMPE 258','CMPE 258'),
                                                        ('CMPE 260','CMPE 260'),
                                                        ('CMPE 261','CMPE 261'),
                                                        ('CMPE 262','CMPE 262'),
                                                        ('CMPE 264','CMPE 264'),
                                                        ('CMPE 265','CMPE 265'),
                                                        ('CMPE 266','CMPE 266'),
                                                        ('CMPE 270','CMPE 270'),
                                                        ('CMPE 271','CMPE 271'),
                                                        ('CMPE 272','CMPE 272'),
                                                        ('CMPE 273','CMPE 273'),
                                                        ('CMPE 274','CMPE 274'),
                                                        ('CMPE 275','CMPE 275'),
                                                        ('CMPE 276','CMPE 276'),
                                                        ('CMPE 277','CMPE 277'),
                                                        ('CMPE 278','CMPE 278'),
                                                        ('CMPE 279','CMPE 279'),
                                                        ('CMPE 281','CMPE 281'),
                                                        ('CMPE 282','CMPE 282'),
                                                        ('CMPE 283','CMPE 283'),
                                                        ('CMPE 284','CMPE 284'),
                                                        ('CMPE 285','CMPE 285'),
                                                        ('CMPE 286','CMPE 286'),
                                                        ('CMPE 287','CMPE 287'),
                                                        ('CMPE 290','CMPE 290'),
                                                        ('CMPE 294','CMPE 294'),
                                                        ('CMPE 295A','CMPE 295A'),
                                                        ('CMPE 295B','CMPE 295B'),
                                                        ('CMPE 297','CMPE 297'),
                                                        ('CMPE 298','CMPE 298'),
                                                        ('CMPE 299A','CMPE 299A'),
                                                        ('CMPE 299B','CMPE 299B'),
                                                        ('ENGR 200W','ENGR 200W'),
                                                        ('ISE 201','ISE 201'),
                                                        ('ISE 244','ISE 244')
                                                    ], max_length=100, null=True)),
                ('section', models.CharField(choices=[
                                                        ('01','01'),
                                                        ('02','02'),
                                                        ('03','03'),
                                                        ('04','04'),
                                                        ('05','05'),
                                                        ('06','06'),
                                                        ('07','07'),
                                                        ('08','08'),
                                                        ('09','09'),
                                                        ('10','10')
                                                    ], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=200, null=True)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendence_sys.Faculty')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendence_sys.Student')),
            ],
        ),
    ]
