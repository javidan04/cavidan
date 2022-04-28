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


class News(models.Model):
    title = models.TextField()
    contetn = models.IntegerField()
    categori = models.CharField(max_length=255)
    alt_categori = models.CharField(max_length=255)
    img = models.TextField()
    w = models.CharField(max_length=255)
    link = models.TextField()
    data = models.CharField(max_length=255)
    movzu = models.CharField(max_length=255)
    neg = models.IntegerField()
    poz = models.IntegerField()
    ney = models.IntegerField()
    time = models.IntegerField()
    tarix = models.DateTimeField()
    statuss = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class Newsconfig(models.Model):
    newsconfig_host = models.TextField(db_column='newsConfig_host')  # Field name made lowercase.
    newsconfig_category = models.TextField(db_column='newsConfig_category', blank=True, null=True)  # Field name made lowercase.
    newsconfig_title = models.TextField(db_column='newsConfig_title', blank=True, null=True)  # Field name made lowercase.
    newsconfig_content = models.TextField(db_column='newsConfig_content', blank=True, null=True)  # Field name made lowercase.
    newsconfig_img = models.TextField(db_column='newsConfig_img', blank=True, null=True)  # Field name made lowercase.
    newsconfig_content_date_time = models.TextField(db_column='newsConfig_content_date_time', blank=True, null=True)  # Field name made lowercase.
    newsconfig_content_video = models.TextField(db_column='newsConfig_content_video', blank=True, null=True)  # Field name made lowercase.
    newsconfig_content_img = models.TextField(db_column='newsConfig_content_img', blank=True, null=True)  # Field name made lowercase.
    newsconfig_img_static_text = models.TextField(db_column='newsConfig_img_static_text', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()
    status = models.IntegerField()
    date_format = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsConfig'


class NewsconfigBackup(models.Model):
    newsconfig_host = models.TextField(db_column='newsConfig_host')  # Field name made lowercase.
    newsconfig_category = models.TextField(db_column='newsConfig_category')  # Field name made lowercase.
    newsconfig_title = models.TextField(db_column='newsConfig_title')  # Field name made lowercase.
    newsconfig_content = models.TextField(db_column='newsConfig_content')  # Field name made lowercase.
    newsconfig_img = models.TextField(db_column='newsConfig_img')  # Field name made lowercase.
    newsconfig_content_date_time = models.TextField(db_column='newsConfig_content_date_time')  # Field name made lowercase.
    newsconfig_content_video = models.TextField(db_column='newsConfig_content_video')  # Field name made lowercase.
    newsconfig_content_img = models.TextField(db_column='newsConfig_content_img')  # Field name made lowercase.
    newsconfig_img_static_text = models.TextField(db_column='newsConfig_img_static_text', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newsConfig_backup'


class Newslistconfig(models.Model):
    newslistconfig_host = models.TextField(db_column='newsListConfig_host')  # Field name made lowercase.
    newslistconfig_newslistlink = models.TextField(db_column='newsListConfig_newsListLink', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_newslist = models.TextField(db_column='newsListConfig_newsList', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_link = models.TextField(db_column='newsListConfig_link', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_title = models.TextField(db_column='newsListConfig_title', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_img = models.TextField(db_column='newsListConfig_img', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_category = models.TextField(db_column='newsListConfig_category', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_img_static_text = models.TextField(db_column='newsListConfig_img_static_text', blank=True, null=True)  # Field name made lowercase.
    newslistconfig_link_static_text = models.TextField(db_column='newsListConfig_link_static_text', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()
    status = models.IntegerField()
    allow = models.IntegerField()
    readcount = models.IntegerField(db_column='readCount')  # Field name made lowercase.
    newslistconfig_content_date_time = models.TextField(db_column='newsListConfig_content_date_time', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsListConfig'


class NewsAllSon(models.Model):
    title = models.TextField()
    contetn = models.TextField()
    categori = models.CharField(max_length=255)
    categori_id = models.IntegerField()
    alt_categori = models.CharField(max_length=255)
    img = models.TextField()
    host = models.CharField(max_length=255)
    link = models.TextField()
    media_img = models.TextField()
    media_video = models.TextField()
    data = models.CharField(max_length=255)
    time = models.IntegerField()
    tarix = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'news_all_son'


class WebScrapingData(models.Model):
    host = models.CharField(max_length=255)
    link = models.TextField()
    title = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    subcategory = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    main_image = models.CharField(max_length=255, blank=True, null=True)
    content_image = models.TextField(blank=True, null=True)
    content_video = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    content_date_time = models.CharField(max_length=100, db_collation='utf8_unicode_ci', blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'web_scraping_data'


    @property
    def content_with_more(self):
        if len(self.content) < 380:
            return self.content
        else:
            return f"{self.content[:380]}..."


class WebScrapingLink(models.Model):
    host = models.CharField(max_length=255)
    link = models.TextField()
    title = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    subcategory = models.CharField(max_length=255, blank=True, null=True)
    main_image = models.CharField(max_length=255, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    content_date_time = models.CharField(max_length=100, db_collation='utf8_unicode_ci', blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_scraping_link'
