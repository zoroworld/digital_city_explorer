BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("name")
);
CREATE TABLE IF NOT EXISTS "locations" (
	"id"	INTEGER NOT NULL,
	"latitude"	FLOAT NOT NULL,
	"longitude"	FLOAT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "pois" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	"description"	VARCHAR,
	"category_id"	INTEGER,
	"location_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("category_id") REFERENCES "categories"("id"),
	FOREIGN KEY("location_id") REFERENCES "locations"("id")
);
INSERT INTO "categories" VALUES (1,'park');
INSERT INTO "categories" VALUES (2,'restaurant');
INSERT INTO "categories" VALUES (3,'museum');
INSERT INTO "categories" VALUES (4,'shopping');
INSERT INTO "categories" VALUES (5,'temple');
INSERT INTO "locations" VALUES (1,22.5806,88.4666);
INSERT INTO "locations" VALUES (2,22.5448,88.3426);
INSERT INTO "locations" VALUES (3,22.558,88.35);
INSERT INTO "locations" VALUES (4,22.5726,88.3639);
INSERT INTO "locations" VALUES (5,22.573,88.361);
INSERT INTO "locations" VALUES (6,22.56,88.37);
INSERT INTO "locations" VALUES (7,22.59,88.4);
INSERT INTO "locations" VALUES (8,22.565,88.355);
INSERT INTO "locations" VALUES (9,22.57,88.36);
INSERT INTO "locations" VALUES (10,22.58,88.47);
INSERT INTO "locations" VALUES (11,22.54,88.33);
INSERT INTO "locations" VALUES (12,22.55,88.34);
INSERT INTO "locations" VALUES (13,22.5605,88.3605);
INSERT INTO "locations" VALUES (14,22.575,88.365);
INSERT INTO "locations" VALUES (15,22.585,88.375);
INSERT INTO "locations" VALUES (16,22.595,88.385);
INSERT INTO "locations" VALUES (17,22.605,88.395);
INSERT INTO "locations" VALUES (18,22.615,88.405);
INSERT INTO "locations" VALUES (19,22.625,88.415);
INSERT INTO "locations" VALUES (20,22.635,88.425);
INSERT INTO "pois" VALUES (1,'Eco Park','Large urban park',1,1);
INSERT INTO "pois" VALUES (2,'Park Street Restaurant','Famous dining place',2,2);
INSERT INTO "pois" VALUES (3,'Indian Museum','Historic museum',3,3);
INSERT INTO "pois" VALUES (4,'South City Mall','Shopping destination',4,4);
INSERT INTO "pois" VALUES (5,'Kalighat Temple','Religious temple',5,5);
INSERT INTO "pois" VALUES (6,'Central Park','Green park',1,6);
INSERT INTO "pois" VALUES (7,'BBQ Nation','Buffet restaurant',2,7);
INSERT INTO "pois" VALUES (8,'Science City','Science museum',3,8);
INSERT INTO "pois" VALUES (9,'Quest Mall','Luxury shopping mall',4,9);
INSERT INTO "pois" VALUES (10,'Dakshineswar Temple','Famous temple',5,10);
INSERT INTO "pois" VALUES (11,'Millennium Park','Riverfront park',1,11);
INSERT INTO "pois" VALUES (12,'Arsalan Restaurant','Biryani place',2,12);
INSERT INTO "pois" VALUES (13,'Victoria Memorial','Historic monument',3,13);
INSERT INTO "pois" VALUES (14,'Forum Mall','Shopping complex',4,14);
INSERT INTO "pois" VALUES (15,'Birla Temple','Marble temple',5,15);
INSERT INTO "pois" VALUES (16,'Salt Lake Park','Local park',1,16);
INSERT INTO "pois" VALUES (17,'Oh! Calcutta','Traditional cuisine',2,17);
INSERT INTO "pois" VALUES (18,'Marble Palace','Art museum',3,18);
INSERT INTO "pois" VALUES (19,'City Centre Mall','Popular mall',4,19);
INSERT INTO "pois" VALUES (20,'ISKCON Temple','Spiritual temple',5,20);
CREATE INDEX IF NOT EXISTS "ix_categories_id" ON "categories" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_locations_id" ON "locations" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_pois_id" ON "pois" (
	"id"
);
COMMIT;
