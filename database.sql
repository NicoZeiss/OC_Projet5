CREATE DATABASE IF NOT EXISTS projet5;
USE projet5;


CREATE TABLE IF NOT EXISTS Categories (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS Products (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	code BIGINT(13) UNSIGNED NOT NULL,
	name VARCHAR(40) NOT NULL,
	store VARCHAR(20),
	cat_id SMALLINT UNSIGNED NOT NULL,
	grade CHAR(1),
	product_url TEXT,
	PRIMARY KEY (id),
	CONSTRAINT fk_cat_id FOREIGN KEY (cat_id) REFERENCES Categories(id)
)
ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS Favorite (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	code BIGINT(13) UNSIGNED NOT NULL,
	name VARCHAR(40) NOT NULL,
	store VARCHAR(20) NOT NULL,
	cat_id SMALLINT UNSIGNED NOT NULL,
	grade CHAR(1),
	product_url TEXT,
	PRIMARY KEY (id)
)
ENGINE=INNODB;