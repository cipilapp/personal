--
-- PostgreSQL database dump
--

\restrict 0fcVM0tm66czfTLMGT51YXrbqODCDU7ST9m7yDaaS1QmAFmw51n7MmFhmnFrpex

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2025-09-12 00:48:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS "db_logisticSimulator";
--
-- TOC entry 4897 (class 1262 OID 16407)
-- Name: db_logisticSimulator; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "db_logisticSimulator" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';


ALTER DATABASE "db_logisticSimulator" OWNER TO postgres;

\unrestrict 0fcVM0tm66czfTLMGT51YXrbqODCDU7ST9m7yDaaS1QmAFmw51n7MmFhmnFrpex
\connect "db_logisticSimulator"
\restrict 0fcVM0tm66czfTLMGT51YXrbqODCDU7ST9m7yDaaS1QmAFmw51n7MmFhmnFrpex

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4898 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16414)
-- Name: gruas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gruas (
    id integer NOT NULL,
    modelo character varying(50),
    fabricante character varying(50),
    tipo character varying(30),
    capacidad_kg integer,
    pluma_min_m numeric(5,2),
    pluma_max_m numeric(5,2),
    torque_max_knm numeric(6,2),
    altura_max_m numeric(5,2),
    radio_operacion_m numeric(5,2),
    certificacion character varying(50)
);


ALTER TABLE public.gruas OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16413)
-- Name: gruas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.gruas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gruas_id_seq OWNER TO postgres;

--
-- TOC entry 4899 (class 0 OID 0)
-- Dependencies: 217
-- Name: gruas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.gruas_id_seq OWNED BY public.gruas.id;


--
-- TOC entry 4742 (class 2604 OID 16417)
-- Name: gruas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gruas ALTER COLUMN id SET DEFAULT nextval('public.gruas_id_seq'::regclass);


--
-- TOC entry 4891 (class 0 OID 16414)
-- Dependencies: 218
-- Data for Name: gruas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.gruas (id, modelo, fabricante, tipo, capacidad_kg, pluma_min_m, pluma_max_m, torque_max_knm, altura_max_m, radio_operacion_m, certificacion) VALUES (1, 'LTM 1100', 'Liebherr', 'Telescópica', 100000, 11.00, 52.00, 3450.00, 48.00, 42.00, 'ONAC');
INSERT INTO public.gruas (id, modelo, fabricante, tipo, capacidad_kg, pluma_min_m, pluma_max_m, torque_max_knm, altura_max_m, radio_operacion_m, certificacion) VALUES (2, 'GMK 3050', 'Grove', 'Articulada', 50000, 9.50, 38.00, 2100.00, 35.00, 30.00, 'ANSI');
INSERT INTO public.gruas (id, modelo, fabricante, tipo, capacidad_kg, pluma_min_m, pluma_max_m, torque_max_knm, altura_max_m, radio_operacion_m, certificacion) VALUES (3, 'GR-350XL', 'Tadano', 'RT', 35000, 7.00, 31.00, 1800.00, 28.00, 25.00, 'ISO 9927');
INSERT INTO public.gruas (id, modelo, fabricante, tipo, capacidad_kg, pluma_min_m, pluma_max_m, torque_max_knm, altura_max_m, radio_operacion_m, certificacion) VALUES (4, 'TRT 35', 'Terex', 'Terreno Dif', 35000, 8.00, 30.00, 1750.00, 27.00, 24.00, 'ASME B30.5');


--
-- TOC entry 4900 (class 0 OID 0)
-- Dependencies: 217
-- Name: gruas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.gruas_id_seq', 4, true);


--
-- TOC entry 4744 (class 2606 OID 16419)
-- Name: gruas gruas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gruas
    ADD CONSTRAINT gruas_pkey PRIMARY KEY (id);


-- Completed on 2025-09-12 00:48:00

--
-- PostgreSQL database dump complete
--

\unrestrict 0fcVM0tm66czfTLMGT51YXrbqODCDU7ST9m7yDaaS1QmAFmw51n7MmFhmnFrpex

