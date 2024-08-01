-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema page_turners
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `page_turners` ;

-- -----------------------------------------------------
-- Schema page_turners
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `page_turners` DEFAULT CHARACTER SET utf8 ;
USE `page_turners` ;

-- -----------------------------------------------------
-- Table `page_turners`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `page_turners`.`users` ;

CREATE TABLE IF NOT EXISTS `page_turners`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `admin` TINYINT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `page_turners`.`books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `page_turners`.`books` ;

CREATE TABLE IF NOT EXISTS `page_turners`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL DEFAULT NULL,
  `genre` VARCHAR(255) NULL DEFAULT NULL,
  `author` VARCHAR(255) NULL DEFAULT NULL,
  `price` DECIMAL(6,2) NULL DEFAULT NULL,
  `quantity_in_stock` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT  NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_books_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `page_turners`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `page_turners`.`orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `page_turners`.`orders` ;

CREATE TABLE IF NOT EXISTS `page_turners`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `total` DECIMAL(6,2) NULL DEFAULT NULL,
  `book_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_orders_books1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_orders_users1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `page_turners`.`books` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_users1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `page_turners`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
