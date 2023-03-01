# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archives(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_inscription = models.CharField(db_column='N°_inscription', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nni = models.CharField(db_column='NNI', max_length=255)  # Field name made lowercase.
    n_de_bac = models.CharField(db_column='N°_de_BAC', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_et_prenom = models.CharField(db_column='Nom_et_prenom', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='GENRE', max_length=255)  # Field name made lowercase.
    date_de_naissance = models.DateField(db_column='date_DE_NAISSANCE')  # Field name made lowercase.
    nationalite = models.CharField(db_column='NATIONALITE', max_length=255)  # Field name made lowercase.
    annee_universitaire_de_première_inscription_dans_le_cycle = models.CharField(db_column='ANNEE_UNIVERSITAIRE_DE_première_inscription_DANS_LE_CYCLE', max_length=255)  # Field name made lowercase.
    niveau = models.CharField(db_column='Niveau', max_length=255)  # Field name made lowercase.
    annee_universitaire_de_première_inscription_dans_ce_niveau = models.CharField(db_column='ANNEE_UNIVERSITAIRE_DE_première_inscription_DANS_ce_niveau', max_length=255)  # Field name made lowercase.
    nom_du_tronc_filirere_field = models.CharField(db_column='NOM_DU_(TRONC/FILIRERE)', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    formation = models.CharField(db_column='FORMATION', max_length=255)  # Field name made lowercase.
    redoublant = models.CharField(db_column='Redoublant', max_length=255)  # Field name made lowercase.
    boursier_ou_beneficiants_d_aide = models.CharField(db_column="BOURSIER_OU_BENEFICIANTS_D'AIDE", max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transfere = models.CharField(db_column='TRANSFERE', max_length=255)  # Field name made lowercase.
    année_universitaire_de_la_première_inscription_à_l_établissement = models.CharField(db_column="année_universitaire_de_la_première_inscription_à_l'établissement", max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    etablissement_de_provenance = models.CharField(max_length=255)
    langue_de_formation = models.CharField(db_column='LANGUE_DE_FORMATION', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archives'


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


class Cycles(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cycles'


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


class Etablissements(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    abrev = models.CharField(max_length=255)
    tutelle = models.CharField(max_length=255, blank=True, null=True)
    cotutelle = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    privee = models.IntegerField()
    identifiant = models.ForeignKey('self', models.DO_NOTHING, db_column='identifiant', blank=True, null=True)
    id_cycle = models.ForeignKey(Cycles, models.DO_NOTHING, db_column='id_cycle')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etablissements'


class Etudiants(models.Model):
    id = models.BigAutoField(primary_key=True)
    nni = models.CharField(db_column='NNI', max_length=255)  # Field name made lowercase.
    n_de_bac = models.CharField(db_column='N°_de_BAC', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_et_prenom = models.CharField(db_column='Nom_et_prenom', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='GENRE', max_length=255)  # Field name made lowercase.
    date_de_naissance = models.DateField(db_column='date_DE_NAISSANCE')  # Field name made lowercase.
    nationalite = models.CharField(db_column='NATIONALITE', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etudiants'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Inscrire(models.Model):
    id = models.BigAutoField(primary_key=True)
    année_scolaire = models.CharField(max_length=255)
    id_etudiant = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='id_etudiant')
    id_etablissement = models.ForeignKey(Etablissements, models.DO_NOTHING, db_column='id_etablissement')
    n_inscription = models.CharField(db_column='N°_inscription', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    annee_universitaire_de_première_inscription_dans_le_cycle = models.CharField(db_column='ANNEE_UNIVERSITAIRE_DE_première_inscription_DANS_LE_CYCLE', max_length=255)  # Field name made lowercase.
    niveau = models.CharField(db_column='Niveau', max_length=255)  # Field name made lowercase.
    annee_universitaire_de_première_inscription_dans_ce_niveau = models.CharField(db_column='ANNEE_UNIVERSITAIRE_DE_première_inscription_DANS_ce_niveau', max_length=255)  # Field name made lowercase.
    nom_du_tronc_filirere_field = models.CharField(db_column='NOM_DU_(TRONC/FILIRERE)', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    formation = models.CharField(db_column='FORMATION', max_length=255)  # Field name made lowercase.
    redoublant = models.CharField(db_column='Redoublant', max_length=255)  # Field name made lowercase.
    boursier_ou_beneficiants_d_aide = models.CharField(db_column="BOURSIER_OU_BENEFICIANTS_D'AIDE", max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transfere = models.CharField(db_column='TRANSFERE', max_length=255)  # Field name made lowercase.
    année_universitaire_de_la_première_inscription_à_l_établissement = models.CharField(db_column="année_universitaire_de_la_première_inscription_à_l'établissement", max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    etablissement_de_provenance = models.CharField(max_length=255)
    langue_de_formation = models.CharField(db_column='LANGUE_DE_FORMATION', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscrire'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class PasswordResets(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class TbArchives(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_archives'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    two_factor_secret = models.TextField(blank=True, null=True)
    two_factor_recovery_codes = models.TextField(blank=True, null=True)
    two_factor_confirmed_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
