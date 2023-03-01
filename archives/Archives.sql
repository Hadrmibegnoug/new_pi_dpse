create table if not exists `candidats_admin` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `series` VARCHAR(255) NOT NULL,
    `genre` VARCHAR(255),
    `presents` VARCHAR(255) NOT NULL,
    `nb_admis` INTEGER(255) NULL,
    `pourcentage_admis` DECIMAL(),
    `total` INTEGER(255),
     PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `candidats_effectif`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `wilaya` VARCHAR(255) NOT NULL,
    `effectif` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `taux_reuss`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `series` VARCHAR(255) NOT NULL,
    `candidats` INTEGER(255) NOT NULL,
    `types_candidats` VARCHAR(255) NOT NULL,
    `admis` INTEGER(255) NOT NULL,
    `taux_reuss` DECIMAL(),
     PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF EXISTS `repartition_or_etg`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `filiere` VARCHAR(255) NOT NULL,
    `pays` INTEGER(255) NOT NULL,
    `candidats` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF EXISTS `effectif_etb_g_m_et`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `etablissements` VARCHAR(255) NOT NULL,
    `etrangers` INTEGER(255) NOT NULL,
    `nationaux` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF EXISTS `effectifM_inst_n_g`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF EXISTS `effectifM_inst_n_g_FM`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `effectifM_inst_n_g_ESP_NV`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `effectifM_inst_n_g_ENS`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `effectifM_inst_d_n_g`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
    `domaine` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `effectifM_d_g_n_FM`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
    `domaine` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;

CREATE TABLE IF EXISTS `effectifM_d_g`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `domaine` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `repartition_bourc_benf`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `nb_boursiers` INTEGER(255) NOT NULL,
    `nb_etudiants` INTEGER(255) NOT NULL,
    `pourcentages` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `Montants_bource`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `montants` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `sortants_d_i_g`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `diplome` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `sortants_dsp`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `domaine_specilise` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `etudiants_boursiers_etg_n_g_pa`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `niveaux` VARCHAR(255) NOT NULL,
    `pays_acceuil` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `etudiants_boursiers_etg_cyc_pa`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `effectifs` INTEGER(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `cycles` VARCHAR(255) NOT NULL,
    `pays_acceuil` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `etudiantsMetg_bourses_equipements`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `cycles` VARCHAR(255) NOT NULL,
    `effectifs` INTEGER(255) NOT NULL,
    `taux` VARCHAR(255) NOT NULL,
    `pays` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `Transport`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `pays` VARCHAR(255) NOT NULL,
    `nb_montant` INTEGER(255) NOT NULL,
    `nb_nbr` INTEGER(255) NOT NULL,
    `nb_total` INTEGER(255) NOT NULL,
    `v_montant` INTEGER(255) NOT NULL,
    `v_nbr` INTEGER(255) NOT NULL,
    `v_total` INTEGER(255) NOT NULL,
    `t_montant` INTEGER(255) NOT NULL,
    `t_nbr` INTEGER(255) NOT NULL,
    `t_total` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `repartition_ensg_etb`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `etablissements` VARCHAR(255) NOT NULL,
    `institutions` INTEGER(255) NOT NULL,
    `frequence` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `ensg_perm_trage`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `tranche_age` VARCHAR(255) NOT NULL,
    `effectif` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `repartition_ensg_grade`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `etablissements` VARCHAR(255) NOT NULL,
    `grade` VARCHAR(255) NOT NULL,
    `effectif` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `ensg_perm_di_g_etb`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `etablissements` VARCHAR(255) NOT NULL,
    `diplome` VARCHAR(255) NOT NULL,
    `genre` INTEGER(255) NOT NULL,
    `effectif` INTEGER(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;



CREATE TABLE IF EXISTS `ensg_perm_do_g_etb`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `domaine` VARCHAR(255) NOT NULL,
    `frequence` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;


CREATE TABLE IF EXISTS `ensg_perm_inst_do_di`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `institutions` VARCHAR(255) NOT NULL,
    `domaine` VARCHAR(255) NOT NULL,
    `diplome` VARCHAR(255) NOT NULL,
    `frequence` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;



CREATE TABLE IF EXISTS `repartition_pers_cnou`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `fonction` VARCHAR(255) NOT NULL,
    `genre` VARCHAR(255) NOT NULL,
    `total` VARCHAR(255) NOT NULL,
     PRIMARY KEY (`id`)
)ENGINE = InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
