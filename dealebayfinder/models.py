# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="user.png")

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username} : {self.content}'
    
class ListaBusquedas2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_busqueda = models.IntegerField(db_column='ID_BUSQUEDA')  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=30)  # Field name made lowercase.
    item = models.CharField(db_column='ITEM', max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_BUSQUEDAS2'
    def __str__(self):
        return f'{self.item}'


class Search2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_busqueda = models.IntegerField(db_column='ID_BUSQUEDA')  # Field name made lowercase.
    item_id = models.BigIntegerField(db_column='ITEM_ID')  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=30)  # Field name made lowercase.
    busqueda = models.CharField(db_column='BUSQUEDA', max_length=30)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=255)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imagen = models.CharField(db_column='IMAGEN', max_length=255)  # Field name made lowercase.
    rejected = models.IntegerField(db_column='REJECTED')  # Field name made lowercase.
    shippingcurr = models.CharField(db_column='shippingCurr', max_length=30)  # Field name made lowercase.
    shippingvalue = models.DecimalField(db_column='shippingValue', max_digits=10, decimal_places=2)  # Field name made lowercase.
    shippingtype = models.CharField(db_column='shippingType', max_length=30)  # Field name made lowercase.
    shippinglocation = models.CharField(db_column='shippingLocation', max_length=255)  # Field name made lowercase.
    sellerusername = models.CharField(db_column='sellerUserName', max_length=80)  # Field name made lowercase.
    feedbackscore = models.IntegerField(db_column='feedbackScore')  # Field name made lowercase.
    positivefeedbackpercent = models.DecimalField(db_column='positiveFeedbackPercent', max_digits=10, decimal_places=2)  # Field name made lowercase.
    feedbackratingstar = models.CharField(db_column='feedbackRatingStar', max_length=80)  # Field name made lowercase.
    topratedseller = models.CharField(db_column='topRatedSeller', max_length=30)  # Field name made lowercase.
    shape = models.CharField(max_length=100)
    modified_item = models.CharField(max_length=100)
    country_region_manufacture = models.CharField(max_length=100)
    fineness = models.CharField(max_length=100)
    precious_metal_content_per_unit = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    thickness = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    actual_weight = models.CharField(max_length=100)
    mpn = models.CharField(max_length=100)
    year_field = models.CharField(db_column='year_', max_length=30)  # Field renamed because it ended with '_'.
    brand_mint = models.CharField(max_length=100)
    composition = models.CharField(max_length=100)
    total_precious_metal_content = models.CharField(max_length=100)
    purity = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    certification = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    denomination = models.CharField(max_length=100)
    description = models.TextField()
    featuredr = models.CharField(db_column='featuredR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typee = models.CharField(max_length=255, blank=True, null=True)
    preciousmetalcontent = models.CharField(db_column='preciousMetalContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemssold = models.CharField(db_column='itemsSold', max_length=20, blank=True, null=True)  # Field name made lowercase.
    internalcategory = models.CharField(db_column='internalCategory', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postedweight = models.DecimalField(db_column='postedWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sellerreputation = models.CharField(db_column='sellerReputation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    priceperoz = models.DecimalField(db_column='pricePerOz', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    typeofbid = models.CharField(db_column='typeOfBid', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEARCH2'
    def __str__(self):
        return f'{self.busqueda}'


class Seller2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    selleruserid = models.CharField(db_column='sellerUserId', unique=True, max_length=80, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=80)
    address = models.TextField()
    phonenumber = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    facebook = models.CharField(max_length=80)
    instagram = models.CharField(max_length=80)
    specializedin = models.CharField(db_column='specializedIn', max_length=200)  # Field name made lowercase.
    weboffebay = models.CharField(db_column='webOffEbay', max_length=200)  # Field name made lowercase.
    feedbackscore = models.IntegerField(db_column='feedbackScore')  # Field name made lowercase.
    positivefeedbackpercent = models.DecimalField(db_column='positiveFeedbackPercent', max_digits=10, decimal_places=2)  # Field name made lowercase.
    feedbackratingstar = models.CharField(db_column='feedbackRatingStar', max_length=120)  # Field name made lowercase.
    newuser = models.CharField(db_column='newUser', max_length=80)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='registrationDate', max_length=150)  # Field name made lowercase.
    topratedseller = models.CharField(db_column='topRatedSeller', max_length=80)  # Field name made lowercase.
    ebaystoreseller = models.CharField(db_column='eBayStoreSeller', max_length=255)  # Field name made lowercase.
    sellerbusinesstype = models.CharField(db_column='sellerBusinessType', max_length=80)  # Field name made lowercase.
    othersells = models.TextField(db_column='otherSells', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SELLER2'
    def __str__(self):
        return f'{self.selleruserid}'
    
    


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    n_usuario = models.CharField(db_column='N_USUARIO', unique=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DealebayfinderPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    content = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dealebayfinder_post'



class DealebayfinderProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dealebayfinder_profile'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class ViableItems10Off(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_search = models.IntegerField(db_column='ID_SEARCH', blank=True, null=True)  # Field name made lowercase.
    item_id = models.BigIntegerField(db_column='ITEM_ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    selleruserid = models.CharField(db_column='SELLERUSERID', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'viable_items_10_off'
    def __str__(self):
        return f'{self.title}'
