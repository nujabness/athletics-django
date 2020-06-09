INSERT INTO athletes_athlete (id, prenom_athlete, nationalite_athlete_id, sexe_athlete_id, nom_athlete) VALUES (1, 'Mohammed', 1, 1, 'EL ASSOURI');
INSERT INTO athletes_athlete (id, prenom_athlete, nationalite_athlete_id, sexe_athlete_id, nom_athlete) VALUES (2, 'Shahzaib', 1, 1, 'TAHIR');

INSERT INTO epreuves_epreuve (id, nom_epreuve, phase_epreuve_id, type_epreuve_id) VALUES (1, 'SAUT EN HAUTEUR', 1, 4);
INSERT INTO epreuves_epreuve (id, nom_epreuve, phase_epreuve_id, type_epreuve_id) VALUES (2, 'SAUT EN LONGUEURE', 2, 4);
INSERT INTO epreuves_epreuve (id, nom_epreuve, phase_epreuve_id, type_epreuve_id) VALUES (3, '100m', 4, 3);
INSERT INTO epreuves_epreuve (id, nom_epreuve, phase_epreuve_id, type_epreuve_id) VALUES (4, '400m', 5, 2);

INSERT INTO medailles_medaille (id, link_medaille, nom_medaille) VALUES (1, 'https://image.flaticon.com/icons/svg/625/625394.svg', 'OR');
INSERT INTO medailles_medaille (id, link_medaille, nom_medaille) VALUES (2, 'https://image.flaticon.com/icons/svg/625/625395.svg', 'ARGENT');
INSERT INTO medailles_medaille (id, link_medaille, nom_medaille) VALUES (3, 'https://image.flaticon.com/icons/svg/625/625396.svg', 'BRONZE');
INSERT INTO medailles_medaille (id, link_medaille, nom_medaille) VALUES (4, 'https://image.flaticon.com/icons/svg/625/625397.svg', 'PAS DE MEDAILLE');

INSERT INTO nationalites_nationalite (id, nom_nationalite, link_nationalite) VALUES (1, 'Français', 'https://image.flaticon.com/icons/svg/197/197560.svg');
INSERT INTO nationalites_nationalite (id, nom_nationalite, link_nationalite) VALUES (2, 'Belgique', 'https://image.flaticon.com/icons/png/512/197/197583.png');
INSERT INTO nationalites_nationalite (id, nom_nationalite, link_nationalite) VALUES (3, 'Brésile', 'https://image.flaticon.com/icons/svg/197/197386.svg');
INSERT INTO nationalites_nationalite (id, nom_nationalite, link_nationalite) VALUES (4, 'Japon', 'https://image.flaticon.com/icons/svg/197/197604.svg');
INSERT INTO nationalites_nationalite (id, nom_nationalite, link_nationalite) VALUES (5, 'Espagne', 'https://image.flaticon.com/icons/svg/197/197593.svg');

INSERT INTO participations_participation (id, resultat, athlete_id, epreuve_id, medaille_id) VALUES (1, '8s', 1, 3, 1);
INSERT INTO participations_participation (id, resultat, athlete_id, epreuve_id, medaille_id) VALUES (2, '30m', 2, 2, 2);

INSERT INTO epreuves_phase (id, nom_phase) VALUES (1, 'FINALE');
INSERT INTO epreuves_phase (id, nom_phase) VALUES (2, 'DEMI-FINALE');
INSERT INTO epreuves_phase (id, nom_phase) VALUES (3, 'QUART-DE-FINALE');
INSERT INTO epreuves_phase (id, nom_phase) VALUES (4, '8e-DE-FINALE');

INSERT INTO athletes_sexe (id, nom_sexe) VALUES (1, 'HOMME');
INSERT INTO athletes_sexe (id, nom_sexe) VALUES (2, 'FEMME');

INSERT INTO epreuves_type (id, nom_type) VALUES (1, 'LANCE');
INSERT INTO epreuves_type (id, nom_type) VALUES (2, 'COURSE');
INSERT INTO epreuves_type (id, nom_type) VALUES (3, 'SPRINT');
INSERT INTO epreuves_type (id, nom_type) VALUES (4, 'SAUT');
INSERT INTO epreuves_type (id, nom_type) VALUES (5, 'DECATHLON');