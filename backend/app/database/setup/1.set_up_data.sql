-- bedrijf
INSERT INTO "public"."bedrijf" ("bedrijfs_naam") VALUES ('ICTU');
INSERT INTO "public"."bedrijf" ("bedrijfs_naam") VALUES ('De Nederlandsche Bank');
INSERT INTO "public"."bedrijf" ("bedrijfs_naam") VALUES ('Volkswagen Pon');
INSERT INTO "public"."bedrijf" ("bedrijfs_naam") VALUES ('DataDolphins');

-- functie
INSERT INTO "public"."functie" ("functie") VALUES ('Full Stack Python Ontwikkelaar');
INSERT INTO "public"."functie" ("functie") VALUES ('Data Scientist');
INSERT INTO "public"."functie" ("functie") VALUES ('Full Stack Data Specialist');
INSERT INTO "public"."functie" ("functie") VALUES ('BI Developer');
INSERT INTO "public"."functie" ("functie") VALUES ('Business Manager');

-- gebruiker
INSERT INTO "public"."gebruiker" ("achternaam", "voornaam", "id_functie", "ts_create", "id_bedrijf") VALUES ('Malik','Bushra','4','2023-03-29 13:19:37.421579','3');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Amir','Kalloe','2023-03-29 13:19:37.421579','1','1');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Mitchel','Stokkermans','2023-03-29 13:19:37.421579','2','4');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Esmee','Kramer','2023-03-29 13:19:37.421579','2','3');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Cas','Hastrich','2023-03-29 13:19:37.421579','5','4');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Arjan','Bontsema','2023-03-29 13:19:37.421579','2','2');
INSERT INTO "public"."gebruiker" ("voornaam", "achternaam", "ts_create", "id_functie", "id_bedrijf") VALUES ('Steve','Zindel','2023-03-29 13:19:37.421579','3','4');
