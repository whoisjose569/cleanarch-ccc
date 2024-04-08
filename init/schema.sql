CREATE DATABASE IF NOT EXISTS ccc_database;

CREATE TABLE IF NOT EXISTS `ccc_database`.`family`(
    id BIGINT NOT NULL AUTO_INCREMENT,
    family_name VARCHAR(100) NOT NULL,
    family_address VARCHAR(255),
    phone VARCHAR(25),
    email VARCHAR(100),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS `ccc_database`.`monthly_income`(
    id BIGINT NOT NULL AUTO_INCREMENT,
    family_id INT NOT NULL,
    income DECIMAL(10,2) NOT NULL,
    date VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (family_id) REFERENCES family(id)
);

CREATE TABLE IF NOT EXISTS `ccc_database`.`paid_bills`(
    id BIGINT NOT NULL AUTO_INCREMENT,
    family_id INT NOT NULL,
    type VARCHAR(100) NOT NULL,
    value DECIMAL(10,2) NOT NULL,
    payment_date VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (family_id) REFERENCES family(id)
);