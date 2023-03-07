# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class etu9(models.Model):

    annee_scolaire = models.CharField(max_length=255)
    institutions = models.CharField(max_length=255)
    nb1 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'Montants_bource'


class Transport(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'Transport'


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
        app_label='dpse'
        db_table = 'archives'









class cand2(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'candidats_admin'


class cand1(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    wilaya = models.CharField(max_length=255)
    effectif = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'candidats_effectif'


class Cycles(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label='dpse'
        db_table = 'cycles'











class Headertablemap(models.Model):
    id = models.BigAutoField(primary_key=True)
    header = models.TextField()
    table_name = models.CharField(max_length=255)

    class Meta:
        app_label='dpse'
        db_table = 'headertablemap'

class etu7(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    domaine = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'effectifM_d_g'


class etu6(models.Model):
    institutions = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()
    nb17 = models.IntegerField()
    nb18 = models.IntegerField()
    nb19 = models.IntegerField()
    nb20 = models.IntegerField()
    domaine = models.CharField(max_length=255)

    class Meta:
        app_label='dpse'
        db_table = 'effectifM_d_g_n_FM'


class EffectifmInstDNG(models.Model):
    institutions = models.CharField(max_length=255)
    effectifs = models.IntegerField()
    genre = models.CharField(max_length=255)
    niveaux = models.CharField(max_length=255)
    domaine = models.CharField(max_length=255)

    class Meta:
        app_label='dpse'
        db_table = 'effectifM_inst_d_n_g'


class etu2(models.Model):
    institutions = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()
    nb17 = models.IntegerField()
    nb18 = models.IntegerField()
    nb19 = models.IntegerField()
    nb20 = models.IntegerField()


    class Meta:
        app_label='dpse'
        db_table = 'effectifM_inst_n_g'


class etu5(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()    

    class Meta:
        app_label='dpse'
        db_table = 'effectifM_inst_n_g_ENS'


class etu4(models.Model):
    institutions = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()


    class Meta:
        app_label='dpse'
        db_table = 'effectifM_inst_n_g_ESP_NV'


class etu3(models.Model):
    institutions = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()
    nb17 = models.IntegerField()
    nb18 = models.IntegerField()
    nb19 = models.IntegerField()
    nb20 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'effectifM_inst_n_g_FM'


class etu1(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    etablissements = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'effectif_etb_g_m_et'


class ensg4(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    etablissements = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()
    nb17 = models.IntegerField()
    nb18 = models.IntegerField()
    nb19 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'ensg_perm_di_g_etb'


class ensg5(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    domaine = models.CharField(max_length=255)
    nb1 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'ensg_perm_do_g_etb'


class ensg6(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    institutions = models.CharField(max_length=255)
    domaine = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'ensg_perm_inst_do_di'


class ensg2(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    tranche_age = models.CharField(max_length=255)
    nb1 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'ensg_perm_trage'


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
        app_label='dpse'
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
        app_label='dpse'
        db_table = 'etudiants'


class bour3(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'etudiantsMetg_bourses_equipements'


class bour2(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'etudiants_boursiers_etg_cyc_pa'


class bour1(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    niveaux = models.CharField(max_length=255)
    ALGERIE = models.IntegerField(blank=True, null=True)
    ALLEMAGNE = models.IntegerField(blank=True, null=True)
    CANADA = models.IntegerField(blank=True, null=True)
    COTE_D_IVOIRE = models.IntegerField(blank=True, null=True)
    EGYPTE = models.IntegerField(blank=True, null=True)
    FRANCE = models.IntegerField(blank=True, null=True)
    MALI = models.IntegerField(blank=True, null=True)
    MAROC = models.IntegerField(blank=True, null=True)
    SENEGAL = models.IntegerField(blank=True, null=True)
    TUNISIE = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label='dpse'
        db_table = 'etudiants_boursiers_etg_n_g_pa'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        app_label='dpse'
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
        app_label='dpse'
        db_table = 'inscrire'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'migrations'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label='dpse'
        db_table = 'password_reset_tokens'


class PasswordResets(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label='dpse'
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
        app_label='dpse'
        db_table = 'personal_access_tokens'


class etu8(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    institutions = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
\
    class Meta:
        app_label='dpse'
        db_table = 'repartition_bourc_benf'


class ensg1(models.Model):
    etablissements = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    
    class Meta:
        app_label='dpse'
        db_table = 'repartition_ensg_etb'


class ensg3(models.Model):
    annee_scolaire = models.CharField(max_length=255) 
    etablissements = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    class Meta:
        app_label='dpse'
        db_table = 'repartition_ensg_grade'


class cand4(models.Model):
    filiere = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'repartition_or_etg'


class cnou(models.Model):
    annee_scolaire =models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'repartition_pers_cnou'


class sort1(models.Model):
    institutions = models.CharField(max_length=255)
    annee_scolaire = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()
    nb9 = models.IntegerField()
    nb10 = models.IntegerField()
    nb11 = models.IntegerField()
    nb12 = models.IntegerField()
    nb13 = models.IntegerField()
    nb14 = models.IntegerField()
    nb15 = models.IntegerField()
    nb15 = models.IntegerField()
    nb16 = models.IntegerField()
  

    class Meta:
        app_label='dpse'
        db_table = 'sortants_d_i_g'


class sort2(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    domaine_specilise = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    
    class Meta:
        app_label='dpse'
        db_table = 'sortants_dsp'


class cand3(models.Model):
    annee_scolaire = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    nb1 = models.IntegerField()
    nb2 = models.IntegerField()
    nb3 = models.IntegerField()
    nb4 = models.IntegerField()
    nb5 = models.IntegerField()
    nb6 = models.IntegerField()
    nb7 = models.IntegerField()
    nb8 = models.IntegerField()

    class Meta:
        app_label='dpse'
        db_table = 'taux_reuss'


class TbArchives(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label='dpse'
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
        app_label='dpse'
        db_table = 'users'
