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
  
INSERT INTO `sistema_productividad`.`departamentos` (`nombre`) VALUES ('Desarrollo');
INSERT INTO `sistema_productividad`.`departamentos` (`nombre`) VALUES ('Marketing');
INSERT INTO `sistema_productividad`.`departamentos` (`nombre`) VALUES ('Recursos Humanos');
INSERT INTO `sistema_productividad`.`departamentos` (`nombre`) VALUES ('Ventas');
INSERT INTO `sistema_productividad`.`departamentos` (`nombre`) VALUES ('Finanzas');

INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('Carlos Negro', 'Backend Developer', '4500', '1');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('Ana Díaz', 'Diseñadora UX ', '4100', '1');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('Luis García', 'Especialista SEO', '3800', '2');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('María Torres', 'RRHH Junior', '3500', '3');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('José Pérez', 'Ejecutivo de ventas', '4200', '4');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('Valentina Rodríguez', 'Analista Financiera', '4700', '5');
INSERT INTO `sistema_productividad`.`empleados` (`nombre`, `cargo`, `salario`, `depId`) VALUES ('Raul Gonzalez', 'Diseñador UX', '4100', '2');

INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Desarrollar módulo de autenticación', '2025-07-10', '2025-07-14', 'completada', '1');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Diseñar prototipo para mobile', '2025-07-12', '2025-07-17', 'en progreso', '2');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Optimizar campaña de Google Ads', '2025-07-08', '2025-07-11', 'completada', '3');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Actualizar políticas internas', '2025-07-05', '2025-07-09', 'pendiente', '2');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Contactar 15 nuevos clientes', '2025-07-06', '2025-07-10', 'completada', '5');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Auditar gastos trimestrales', '2025-07-07', '2025-07-13', 'en progreso', '3');
INSERT INTO `sistema_productividad`.`tareas` (`descripcion`, `fechaAsignacion`, `fechaEntrega`, `estado`, `empleadoId`) VALUES ('Mejorar tiempos de carga del sitio', '2025-07-15', '2025-07-20', 'pendiente', '1');