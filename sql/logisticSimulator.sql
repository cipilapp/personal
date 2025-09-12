-- Database: db_logisticSimulator

-- DROP DATABASE IF EXISTS "db_logisticSimulator";

CREATE DATABASE "db_logisticSimulator"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Colombia.1252'
    LC_CTYPE = 'Spanish_Colombia.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


CREATE TABLE gruas (
    id SERIAL PRIMARY KEY,
    modelo VARCHAR(50),
    fabricante VARCHAR(50),
    tipo VARCHAR(30),
    capacidad_kg INT,
    pluma_min_m DECIMAL(5,2),
    pluma_max_m DECIMAL(5,2),
    torque_max_kNm DECIMAL(6,2),
    altura_max_m DECIMAL(5,2),
    radio_operacion_m DECIMAL(5,2),
    certificacion VARCHAR(50)
);

INSERT INTO gruas (
    modelo, fabricante, tipo, capacidad_kg, pluma_min_m, pluma_max_m, torque_max_kNm, altura_max_m, radio_operacion_m, certificacion
) VALUES
('LTM 1100', 'Liebherr', 'Telescópica', 100000, 11.0, 52.0, 3450, 48.0, 42.0, 'ONAC'),
('GMK 3050', 'Grove', 'Articulada', 50000, 9.5, 38.0, 2100, 35.0, 30.0, 'ANSI'),
('GR-350XL', 'Tadano', 'RT', 35000, 7.0, 31.0, 1800, 28.0, 25.0, 'ISO 9927'),
('TRT 35', 'Terex', 'Terreno Dif', 35000, 8.0, 30.0, 1750, 27.0, 24.0, 'ASME B30.5');
