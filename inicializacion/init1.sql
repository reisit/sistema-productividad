CREATE DATABASE IF NOT EXISTS sistema_productividad;
USE sistema_productividad;

CREATE TABLE `sistema_productividad`.`departamentos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `sistema_productividad`.`empleados` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `cargo` VARCHAR(45) NULL,
  `salario` INT NULL,
  `depId` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `departamentos_idx` (`depId` ASC) VISIBLE,
  CONSTRAINT `departamentos`
    FOREIGN KEY (`depId`)
    REFERENCES `sistema_productividad`.`departamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `sistema_productividad`.`tareas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `fechaAsignacion` DATE NULL,
  `fechaEntrega` DATE NULL,
  `estado` ENUM('pendiente', 'en progreso', 'completada') NULL,
  `empleadoId` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `empleados_idx` (`empleadoId` ASC) VISIBLE,
  CONSTRAINT `empleados`
    FOREIGN KEY (`empleadoId`)
    REFERENCES `sistema_productividad`.`empleados` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
