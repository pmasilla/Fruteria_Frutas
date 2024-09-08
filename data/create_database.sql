BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Productos" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"precio_unitario"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (1,'Manzana',0.5);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (2,'Plátano',0.3);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (3,'Naranja',0.7);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (4,'Uvas',1.2);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (5,'Lechuga',0.9);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (6,'Zanahoria',0.4);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (7,'Tomate',0.8);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (8,'Patata',0.6);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (9,'Cebolla',0.5);
INSERT INTO "Productos" ("id","nombre","precio_unitario") VALUES (10,'Pimiento',1.0);

COMMIT;