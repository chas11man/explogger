from django.db import models

FS_CHOICES = (
    (1.0, '1'),
    (1.2, '1.2'),
    (1.4, '1.4'),
    (1.7, '1.7'),
    (2.0, '2'),
    (2.3, '2.3'),
    (2.8, '2.8'),
    (3.4, '3.4'),
    (4.0, '4'),
    (4.7, '4.7'),
    (5.6, '5.6'),
    (6.7, '6.7'),
    (8.0, '8'),
    (9.5, '9.5'),
    (11.0, '11'),
    (13.0, '13'),
    (16.0, '16'),
    (19.0, '19'),
    (22.0, '22'),
    (27.0, '27'),
    (32.0, '32'),
    (38.0, '38'),
    (45.0, '45'),
)

SS_CHOICES = (
    ('4000', '4000'),
    ('3000', '3000'),
    ('1000', '1000'),
    ('500', '500'),
    ('250', '250'),
    ('125', '125'),
    ('100', '100'),
    ('60', '60'),
    ('30', '30'),
    ('15', '15'),
    ('8', '8'),
    ('4', '4'),
    ('2', '2'),
    ('1"', '1"'),
    ('2"', '2"'),
    ('4"', '4"'),
    ('8"', '8"'),
    ('15"', '15"'),
    ('30"', '30"'),
    ('B', 'Bulb'),
)


class Camera(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    shutter_speed_min = models.CharField(max_length=4, choices=SS_CHOICES)
    shutter_speed_max = models.CharField(max_length=4, choices=SS_CHOICES)


class Lens(models.Model):
    brand = models.CharField(max_length=40)
    f_stop_min = models.FloatField(null=True, choices=FS_CHOICES)
    f_stop_max = models.FloatField(null=True, choices=FS_CHOICES)
    focal_len_min = models.SmallIntegerField(null=True)
    focal_len_max = models.SmallIntegerField(blank=True, null=True)


class Film(models.Model):
    name = models.CharField(max_length=40, blank=True)
    iso = models.CharField(max_length=4)
    exposure_count = models.SmallIntegerField()


class Exposure(models.Model):
    camera = models.ForeignKey(Camera)
    film = models.ForeignKey(Film)
    lens = models.ForeignKey(Lens)
    f_stop = models.FloatField(null=True, choices=FS_CHOICES)
    shutter_speed = models.CharField(max_length=4, choices=SS_CHOICES)
    focal_len = models.SmallIntegerField(null=True)