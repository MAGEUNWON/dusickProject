# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Chantime(models.Model):
    no = models.AutoField(primary_key=True)
    data = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chantime'


class Companylist(models.Model):
    no = models.AutoField(primary_key=True)
    market = models.CharField(max_length=8, blank=True, null=True)
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=50, blank=True, null=True)
    startday = models.DateField(blank=True, null=True)
    realsearch = models.CharField(db_column='realSearch', max_length=1, blank=True, null=True)  # Field name made lowercase.
    flotationny = models.CharField(db_column='flotationNY', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companylist'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Kosdak000250D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000250_d'


class Kosdak000250F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_000250_f'


class Kosdak000250M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000250_m'


class Kosdak000250R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000250_r'


class Kosdak000440D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000440_d'


class Kosdak000440F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_000440_f'


class Kosdak000440M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000440_m'


class Kosdak000440R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_000440_r'


class Kosdak001000D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001000_d'


class Kosdak001000F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_001000_f'


class Kosdak001000M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001000_m'


class Kosdak001000R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001000_r'


class Kosdak001540D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001540_d'


class Kosdak001540F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_001540_f'


class Kosdak001540M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001540_m'


class Kosdak001540R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001540_r'


class Kosdak001810D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001810_d'


class Kosdak001810F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_001810_f'


class Kosdak001810M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001810_m'


class Kosdak001810R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001810_r'


class Kosdak001840D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001840_d'


class Kosdak001840F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_001840_f'


class Kosdak001840M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001840_m'


class Kosdak001840R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_001840_r'


class Kosdak002230D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002230_d'


class Kosdak002230F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_002230_f'


class Kosdak002230M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002230_m'


class Kosdak002230R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002230_r'


class Kosdak002290D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002290_d'


class Kosdak002290F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_002290_f'


class Kosdak002290M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002290_m'


class Kosdak002290R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002290_r'


class Kosdak002680D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002680_d'


class Kosdak002680F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_002680_f'


class Kosdak002680M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002680_m'


class Kosdak002680R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002680_r'


class Kosdak002800D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002800_d'


class Kosdak002800F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_002800_f'


class Kosdak002800M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002800_m'


class Kosdak002800R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_002800_r'


class Kosdak003100D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003100_d'


class Kosdak003100F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_003100_f'


class Kosdak003100M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003100_m'


class Kosdak003100R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003100_r'


class Kosdak003310D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003310_d'


class Kosdak003310F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_003310_f'


class Kosdak003310M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003310_m'


class Kosdak003310R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003310_r'


class Kosdak003380D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003380_d'


class Kosdak003380F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_003380_f'


class Kosdak003380M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003380_m'


class Kosdak003380R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003380_r'


class Kosdak003800D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003800_d'


class Kosdak003800F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_003800_f'


class Kosdak003800M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003800_m'


class Kosdak003800R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_003800_r'


class Kosdak004590D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004590_d'


class Kosdak004590F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_004590_f'


class Kosdak004590M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004590_m'


class Kosdak004590R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004590_r'


class Kosdak004650D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004650_d'


class Kosdak004650F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_004650_f'


class Kosdak004650M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004650_m'


class Kosdak004650R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004650_r'


class Kosdak004780D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004780_d'


class Kosdak004780F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_004780_f'


class Kosdak004780M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004780_m'


class Kosdak004780R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_004780_r'


class Kosdak005160D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005160_d'


class Kosdak005160F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005160_f'


class Kosdak005160M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005160_m'


class Kosdak005160R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005160_r'


class Kosdak005290D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005290_d'


class Kosdak005290F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005290_f'


class Kosdak005290M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005290_m'


class Kosdak005290R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005290_r'


class Kosdak005670D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005670_d'


class Kosdak005670F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005670_f'


class Kosdak005670M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005670_m'


class Kosdak005670R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005670_r'


class Kosdak005710D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005710_d'


class Kosdak005710F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005710_f'


class Kosdak005710M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005710_m'


class Kosdak005710R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005710_r'


class Kosdak005860D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005860_d'


class Kosdak005860F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005860_f'


class Kosdak005860M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005860_m'


class Kosdak005860R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005860_r'


class Kosdak005990D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005990_d'


class Kosdak005990F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_005990_f'


class Kosdak005990M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005990_m'


class Kosdak005990R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_005990_r'


class Kosdak006050D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006050_d'


class Kosdak006050F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006050_f'


class Kosdak006050M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006050_m'


class Kosdak006050R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006050_r'


class Kosdak006140D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006140_d'


class Kosdak006140F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006140_f'


class Kosdak006140M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006140_m'


class Kosdak006140R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006140_r'


class Kosdak006580D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006580_d'


class Kosdak006580F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006580_f'


class Kosdak006580M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006580_m'


class Kosdak006580R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006580_r'


class Kosdak006620D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006620_d'


class Kosdak006620F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006620_f'


class Kosdak006620M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006620_m'


class Kosdak006620R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006620_r'


class Kosdak006730D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006730_d'


class Kosdak006730F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006730_f'


class Kosdak006730M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006730_m'


class Kosdak006730R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006730_r'


class Kosdak006910D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006910_d'


class Kosdak006910F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006910_f'


class Kosdak006910M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006910_m'


class Kosdak006910R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006910_r'


class Kosdak006920D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006920_d'


class Kosdak006920F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_006920_f'


class Kosdak006920M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006920_m'


class Kosdak006920R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_006920_r'


class Kosdak007330D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007330_d'


class Kosdak007330F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007330_f'


class Kosdak007330M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007330_m'


class Kosdak007330R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007330_r'


class Kosdak007370D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007370_d'


class Kosdak007370F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007370_f'


class Kosdak007370M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007370_m'


class Kosdak007370R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007370_r'


class Kosdak007390D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007390_d'


class Kosdak007390F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007390_f'


class Kosdak007390M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007390_m'


class Kosdak007390R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007390_r'


class Kosdak007530D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007530_d'


class Kosdak007530F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007530_f'


class Kosdak007530M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007530_m'


class Kosdak007530R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007530_r'


class Kosdak007680D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007680_d'


class Kosdak007680F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007680_f'


class Kosdak007680M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007680_m'


class Kosdak007680R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007680_r'


class Kosdak007720D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007720_d'


class Kosdak007720F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007720_f'


class Kosdak007720M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007720_m'


class Kosdak007720R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007720_r'


class Kosdak007770D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007770_d'


class Kosdak007770F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007770_f'


class Kosdak007770M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007770_m'


class Kosdak007770R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007770_r'


class Kosdak007820D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007820_d'


class Kosdak007820F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_007820_f'


class Kosdak007820M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007820_m'


class Kosdak007820R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_007820_r'


class Kosdak008290D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008290_d'


class Kosdak008290F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_008290_f'


class Kosdak008290M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008290_m'


class Kosdak008290R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008290_r'


class Kosdak008370D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008370_d'


class Kosdak008370F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_008370_f'


class Kosdak008370M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008370_m'


class Kosdak008370R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008370_r'


class Kosdak008470D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008470_d'


class Kosdak008470F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_008470_f'


class Kosdak008470M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008470_m'


class Kosdak008470R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008470_r'


class Kosdak008830D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008830_d'


class Kosdak008830F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_008830_f'


class Kosdak008830M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008830_m'


class Kosdak008830R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_008830_r'


class Kosdak009300D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009300_d'


class Kosdak009300F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_009300_f'


class Kosdak009300M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009300_m'


class Kosdak009300R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009300_r'


class Kosdak009520D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009520_d'


class Kosdak009520F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_009520_f'


class Kosdak009520M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009520_m'


class Kosdak009520R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009520_r'


class Kosdak009620D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009620_d'


class Kosdak009620F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_009620_f'


class Kosdak009620M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009620_m'


class Kosdak009620R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009620_r'


class Kosdak009730D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009730_d'


class Kosdak009730F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_009730_f'


class Kosdak009730M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009730_m'


class Kosdak009730R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009730_r'


class Kosdak009780D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009780_d'


class Kosdak009780F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_009780_f'


class Kosdak009780M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009780_m'


class Kosdak009780R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_009780_r'


class Kosdak010170D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010170_d'


class Kosdak010170F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_010170_f'


class Kosdak010170M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010170_m'


class Kosdak010170R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010170_r'


class Kosdak010240D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010240_d'


class Kosdak010240F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_010240_f'


class Kosdak010240M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010240_m'


class Kosdak010240R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010240_r'


class Kosdak010280D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010280_d'


class Kosdak010280F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_010280_f'


class Kosdak010280M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010280_m'


class Kosdak010280R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010280_r'


class Kosdak010470D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010470_d'


class Kosdak010470F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_010470_f'


class Kosdak010470M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010470_m'


class Kosdak010470R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_010470_r'


class Kosdak011040D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011040_d'


class Kosdak011040F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_011040_f'


class Kosdak011040M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011040_m'


class Kosdak011040R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011040_r'


class Kosdak011080D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011080_d'


class Kosdak011080F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_011080_f'


class Kosdak011080M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011080_m'


class Kosdak011080R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011080_r'


class Kosdak011320D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011320_d'


class Kosdak011320F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_011320_f'


class Kosdak011320M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011320_m'


class Kosdak011320R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011320_r'


class Kosdak011370D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011370_d'


class Kosdak011370F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_011370_f'


class Kosdak011370M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011370_m'


class Kosdak011370R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011370_r'


class Kosdak011560D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011560_d'


class Kosdak011560F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_011560_f'


class Kosdak011560M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011560_m'


class Kosdak011560R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_011560_r'


class Kosdak012340D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012340_d'


class Kosdak012340F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_012340_f'


class Kosdak012340M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012340_m'


class Kosdak012340R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012340_r'


class Kosdak012620D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012620_d'


class Kosdak012620F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_012620_f'


class Kosdak012620M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012620_m'


class Kosdak012620R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012620_r'


class Kosdak012700D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012700_d'


class Kosdak012700F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_012700_f'


class Kosdak012700M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012700_m'


class Kosdak012700R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012700_r'


class Kosdak012790D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012790_d'


class Kosdak012790F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_012790_f'


class Kosdak012790M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012790_m'


class Kosdak012790R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012790_r'


class Kosdak012860D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012860_d'


class Kosdak012860F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_012860_f'


class Kosdak012860M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012860_m'


class Kosdak012860R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_012860_r'


class Kosdak013030D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013030_d'


class Kosdak013030F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013030_f'


class Kosdak013030M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013030_m'


class Kosdak013030R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013030_r'


class Kosdak013120D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013120_d'


class Kosdak013120F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013120_f'


class Kosdak013120M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013120_m'


class Kosdak013120R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013120_r'


class Kosdak013310D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013310_d'


class Kosdak013310F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013310_f'


class Kosdak013310M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013310_m'


class Kosdak013310R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013310_r'


class Kosdak013720D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013720_d'


class Kosdak013720F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013720_f'


class Kosdak013720M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013720_m'


class Kosdak013720R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013720_r'


class Kosdak013810D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013810_d'


class Kosdak013810F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013810_f'


class Kosdak013810M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013810_m'


class Kosdak013810R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013810_r'


class Kosdak013990D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013990_d'


class Kosdak013990F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_013990_f'


class Kosdak013990M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013990_m'


class Kosdak013990R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_013990_r'


class Kosdak014100D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014100_d'


class Kosdak014100F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014100_f'


class Kosdak014100M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014100_m'


class Kosdak014100R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014100_r'


class Kosdak014190D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014190_d'


class Kosdak014190F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014190_f'


class Kosdak014190M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014190_m'


class Kosdak014190R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014190_r'


class Kosdak014200D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014200_d'


class Kosdak014200F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014200_f'


class Kosdak014200M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014200_m'


class Kosdak014200R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014200_r'


class Kosdak014470D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014470_d'


class Kosdak014470F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014470_f'


class Kosdak014470M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014470_m'


class Kosdak014470R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014470_r'


class Kosdak014570D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014570_d'


class Kosdak014570F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014570_f'


class Kosdak014570M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014570_m'


class Kosdak014570R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014570_r'


class Kosdak014620D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014620_d'


class Kosdak014620F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014620_f'


class Kosdak014620M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014620_m'


class Kosdak014620R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014620_r'


class Kosdak014940D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014940_d'


class Kosdak014940F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014940_f'


class Kosdak014940M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014940_m'


class Kosdak014940R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014940_r'


class Kosdak014970D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014970_d'


class Kosdak014970F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_014970_f'


class Kosdak014970M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014970_m'


class Kosdak014970R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_014970_r'


class Kosdak015710D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015710_d'


class Kosdak015710F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_015710_f'


class Kosdak015710M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015710_m'


class Kosdak015710R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015710_r'


class Kosdak015750D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015750_d'


class Kosdak015750F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_015750_f'


class Kosdak015750M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015750_m'


class Kosdak015750R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_015750_r'


class Kosdak016100D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016100_d'


class Kosdak016100F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016100_f'


class Kosdak016100M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016100_m'


class Kosdak016100R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016100_r'


class Kosdak016250D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016250_d'


class Kosdak016250F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016250_f'


class Kosdak016250M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016250_m'


class Kosdak016250R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016250_r'


class Kosdak016600D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016600_d'


class Kosdak016600F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016600_f'


class Kosdak016600M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016600_m'


class Kosdak016600R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016600_r'


class Kosdak016670D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016670_d'


class Kosdak016670F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016670_f'


class Kosdak016670M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016670_m'


class Kosdak016670R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016670_r'


class Kosdak016790D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016790_d'


class Kosdak016790F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016790_f'


class Kosdak016790M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016790_m'


class Kosdak016790R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016790_r'


class Kosdak016920D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016920_d'


class Kosdak016920F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_016920_f'


class Kosdak016920M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016920_m'


class Kosdak016920R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_016920_r'


class Kosdak017000D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017000_d'


class Kosdak017000F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017000_f'


class Kosdak017000M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017000_m'


class Kosdak017000R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017000_r'


class Kosdak017250D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017250_d'


class Kosdak017250F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017250_f'


class Kosdak017250M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017250_m'


class Kosdak017250R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017250_r'


class Kosdak017480D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017480_d'


class Kosdak017480F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017480_f'


class Kosdak017480M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017480_m'


class Kosdak017480R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017480_r'


class Kosdak017510D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017510_d'


class Kosdak017510F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017510_f'


class Kosdak017510M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017510_m'


class Kosdak017510R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017510_r'


class Kosdak017650D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017650_d'


class Kosdak017650F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017650_f'


class Kosdak017650M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017650_m'


class Kosdak017650R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017650_r'


class Kosdak017890D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017890_d'


class Kosdak017890F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_017890_f'


class Kosdak017890M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017890_m'


class Kosdak017890R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_017890_r'


class Kosdak018000D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018000_d'


class Kosdak018000F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018000_f'


class Kosdak018000M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018000_m'


class Kosdak018000R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018000_r'


class Kosdak018120D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018120_d'


class Kosdak018120F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018120_f'


class Kosdak018120M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018120_m'


class Kosdak018120R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018120_r'


class Kosdak018290D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018290_d'


class Kosdak018290F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018290_f'


class Kosdak018290M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018290_m'


class Kosdak018290R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018290_r'


class Kosdak018310D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018310_d'


class Kosdak018310F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018310_f'


class Kosdak018310M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018310_m'


class Kosdak018310R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018310_r'


class Kosdak018620D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018620_d'


class Kosdak018620F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018620_f'


class Kosdak018620M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018620_m'


class Kosdak018620R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018620_r'


class Kosdak018680D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018680_d'


class Kosdak018680F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018680_f'


class Kosdak018680M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018680_m'


class Kosdak018680R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018680_r'


class Kosdak018700D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018700_d'


class Kosdak018700F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_018700_f'


class Kosdak018700M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018700_m'


class Kosdak018700R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_018700_r'


class Kosdak019010D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019010_d'


class Kosdak019010F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019010_f'


class Kosdak019010M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019010_m'


class Kosdak019010R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019010_r'


class Kosdak019210D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019210_d'


class Kosdak019210F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019210_f'


class Kosdak019210M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019210_m'


class Kosdak019210R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019210_r'


class Kosdak019540D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019540_d'


class Kosdak019540F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019540_f'


class Kosdak019540M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019540_m'


class Kosdak019540R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019540_r'


class Kosdak019550D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019550_d'


class Kosdak019550F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019550_f'


class Kosdak019550M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019550_m'


class Kosdak019550R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019550_r'


class Kosdak019570D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019570_d'


class Kosdak019570F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019570_f'


class Kosdak019570M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019570_m'


class Kosdak019570R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019570_r'


class Kosdak019590D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019590_d'


class Kosdak019590F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019590_f'


class Kosdak019590M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019590_m'


class Kosdak019590R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019590_r'


class Kosdak019660D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019660_d'


class Kosdak019660F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019660_f'


class Kosdak019660M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019660_m'


class Kosdak019660R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019660_r'


class Kosdak019770D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019770_d'


class Kosdak019770F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019770_f'


class Kosdak019770M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019770_m'


class Kosdak019770R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019770_r'


class Kosdak019990D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019990_d'


class Kosdak019990F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_019990_f'


class Kosdak019990M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019990_m'


class Kosdak019990R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_019990_r'


class Kosdak020180D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020180_d'


class Kosdak020180F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_020180_f'


class Kosdak020180M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020180_m'


class Kosdak020180R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020180_r'


class Kosdak020400D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020400_d'


class Kosdak020400F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_020400_f'


class Kosdak020400M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020400_m'


class Kosdak020400R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020400_r'


class Kosdak020710D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020710_d'


class Kosdak020710F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_020710_f'


class Kosdak020710M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020710_m'


class Kosdak020710R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_020710_r'


class Kosdak021040D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021040_d'


class Kosdak021040F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021040_f'


class Kosdak021040M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021040_m'


class Kosdak021040R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021040_r'


class Kosdak021045D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021045_d'


class Kosdak021045F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021045_f'


class Kosdak021045M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021045_m'


class Kosdak021045R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021045_r'


class Kosdak021080D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021080_d'


class Kosdak021080F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021080_f'


class Kosdak021080M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021080_m'


class Kosdak021080R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021080_r'


class Kosdak021320D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021320_d'


class Kosdak021320F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021320_f'


class Kosdak021320M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021320_m'


class Kosdak021320R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021320_r'


class Kosdak021650D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021650_d'


class Kosdak021650F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021650_f'


class Kosdak021650M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021650_m'


class Kosdak021650R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021650_r'


class Kosdak021880D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021880_d'


class Kosdak021880F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_021880_f'


class Kosdak021880M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021880_m'


class Kosdak021880R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_021880_r'


class Kosdak022100D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022100_d'


class Kosdak022100F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_022100_f'


class Kosdak022100M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022100_m'


class Kosdak022100R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022100_r'


class Kosdak022220D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022220_d'


class Kosdak022220F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_022220_f'


class Kosdak022220M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022220_m'


class Kosdak022220R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_022220_r'


class Kosdak023160D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023160_d'


class Kosdak023160F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023160_f'


class Kosdak023160M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023160_m'


class Kosdak023160R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023160_r'


class Kosdak023410D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023410_d'


class Kosdak023410F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023410_f'


class Kosdak023410M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023410_m'


class Kosdak023410R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023410_r'


class Kosdak023440D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023440_d'


class Kosdak023440F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023440_f'


class Kosdak023440M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023440_m'


class Kosdak023440R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023440_r'


class Kosdak023460D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023460_d'


class Kosdak023460F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023460_f'


class Kosdak023460M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023460_m'


class Kosdak023460R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023460_r'


class Kosdak023600D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023600_d'


class Kosdak023600F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023600_f'


class Kosdak023600M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023600_m'


class Kosdak023600R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023600_r'


class Kosdak023760D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023760_d'


class Kosdak023760F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023760_f'


class Kosdak023760M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023760_m'


class Kosdak023760R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023760_r'


class Kosdak023770D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023770_d'


class Kosdak023770F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023770_f'


class Kosdak023770M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023770_m'


class Kosdak023770R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023770_r'


class Kosdak023790D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023790_d'


class Kosdak023790F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023790_f'


class Kosdak023790M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023790_m'


class Kosdak023790R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023790_r'


class Kosdak023900D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023900_d'


class Kosdak023900F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023900_f'


class Kosdak023900M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023900_m'


class Kosdak023900R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023900_r'


class Kosdak023910D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023910_d'


class Kosdak023910F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_023910_f'


class Kosdak023910M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023910_m'


class Kosdak023910R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_023910_r'


class Kosdak024060D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024060_d'


class Kosdak024060F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024060_f'


class Kosdak024060M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024060_m'


class Kosdak024060R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024060_r'


class Kosdak024120D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024120_d'


class Kosdak024120F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024120_f'


class Kosdak024120M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024120_m'


class Kosdak024120R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024120_r'


class Kosdak024740D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024740_d'


class Kosdak024740F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024740_f'


class Kosdak024740M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024740_m'


class Kosdak024740R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024740_r'


class Kosdak024800D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024800_d'


class Kosdak024800F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024800_f'


class Kosdak024800M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024800_m'


class Kosdak024800R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024800_r'


class Kosdak024810D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024810_d'


class Kosdak024810F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024810_f'


class Kosdak024810M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024810_m'


class Kosdak024810R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024810_r'


class Kosdak024830D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024830_d'


class Kosdak024830F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024830_f'


class Kosdak024830M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024830_m'


class Kosdak024830R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024830_r'


class Kosdak024840D(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024840_d'


class Kosdak024840F(models.Model):
    no = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    settlementmonth = models.IntegerField(db_column='settlementMonth', blank=True, null=True)  # Field name made lowercase.
    facevalue = models.IntegerField(db_column='faceValue', blank=True, null=True)  # Field name made lowercase.
    sharecapital = models.IntegerField(db_column='shareCapital', blank=True, null=True)  # Field name made lowercase.
    authorize = models.IntegerField(blank=True, null=True)
    creditratio = models.FloatField(db_column='creditRatio', blank=True, null=True)  # Field name made lowercase.
    cap = models.IntegerField(blank=True, null=True)
    foreignburnoutrate = models.FloatField(db_column='foreignBurnoutRate', blank=True, null=True)  # Field name made lowercase.
    subprice = models.IntegerField(db_column='subPrice', blank=True, null=True)  # Field name made lowercase.
    pre = models.FloatField(db_column='PRE', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    ev = models.FloatField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.IntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    operatingincome = models.IntegerField(db_column='operatingIncome', blank=True, null=True)  # Field name made lowercase.
    pretaxincome = models.IntegerField(db_column='pretaxIncome', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'kosdak_024840_f'


class Kosdak024840M(models.Model):
    no = models.AutoField(primary_key=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024840_m'


class Kosdak024840R(models.Model):
    no = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    cumulativevolume = models.IntegerField(db_column='cumulativeVolume', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kosdak_024840_r'


class Kosdak024850D(models.Model):
    no = models.AutoField(primary_key=True)
