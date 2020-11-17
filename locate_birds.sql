--
-- PostgreSQL database dump
--

-- Dumped from database version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: birds; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.birds (
    "speciesCode" character varying NOT NULL,
    "sciName" character varying NOT NULL,
    "comName" character varying,
    "searchTag" character varying,
    call1 character varying
);


ALTER TABLE public.birds OWNER TO vagrant;

--
-- Name: locations; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.locations (
    location_id integer NOT NULL,
    location_name character varying,
    address character varying NOT NULL,
    latitude double precision NOT NULL,
    longitude double precision NOT NULL,
    radius integer,
    "time" integer,
    num_results integer
);


ALTER TABLE public.locations OWNER TO vagrant;

--
-- Name: locations_location_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.locations_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_location_id_seq OWNER TO vagrant;

--
-- Name: locations_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.locations_location_id_seq OWNED BY public.locations.location_id;


--
-- Name: searches; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.searches (
    search_id integer NOT NULL,
    location_id integer,
    bird_id character varying
);


ALTER TABLE public.searches OWNER TO vagrant;

--
-- Name: searches_search_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.searches_search_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.searches_search_id_seq OWNER TO vagrant;

--
-- Name: searches_search_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.searches_search_id_seq OWNED BY public.searches.search_id;


--
-- Name: locations location_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.locations ALTER COLUMN location_id SET DEFAULT nextval('public.locations_location_id_seq'::regclass);


--
-- Name: searches search_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.searches ALTER COLUMN search_id SET DEFAULT nextval('public.searches_search_id_seq'::regclass);


--
-- Data for Name: birds; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.birds ("speciesCode", "sciName", "comName", "searchTag", call1) FROM stdin;
rebwoo	Melanerpes carolinus	Red-bellied Woodpecker	red-bellied+woodpecker	https://www.xeno-canto.org/563618/embed?simple=1
dowwoo	Dryobates pubescens	Downy Woodpecker	downy+woodpecker	https://www.xeno-canto.org/590054/embed?simple=1
blujay	Cyanocitta cristata	Blue Jay	blue+jay	https://www.xeno-canto.org/592263/embed?simple=1
bkcchi	Poecile atricapillus	Black-capped Chickadee	black-capped+chickadee	https://www.xeno-canto.org/590964/embed?simple=1
rebnut	Sitta canadensis	Red-breasted Nuthatch	red-breasted+nuthatch	https://www.xeno-canto.org/599843/embed?simple=1
eursta	Sturnus vulgaris	European Starling	european+starling	\N
amerob	Turdus migratorius	American Robin	american+robin	https://www.xeno-canto.org/573924/embed?simple=1
cedwax	Bombycilla cedrorum	Cedar Waxwing	cedar+waxwing	https://www.xeno-canto.org/598824/embed?simple=1
houspa	Passer domesticus	House Sparrow	house+sparrow	https://www.xeno-canto.org/600976/embed?simple=1
amegfi	Spinus tristis	American Goldfinch	american+goldfinch	https://www.xeno-canto.org/582147/embed?simple=1
\.


--
-- Data for Name: locations; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.locations (location_id, location_name, address, latitude, longitude, radius, "time", num_results) FROM stdin;
\.


--
-- Data for Name: searches; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.searches (search_id, location_id, bird_id) FROM stdin;
\.


--
-- Name: locations_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.locations_location_id_seq', 1, false);


--
-- Name: searches_search_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.searches_search_id_seq', 1, false);


--
-- Name: birds birds_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.birds
    ADD CONSTRAINT birds_pkey PRIMARY KEY ("speciesCode");


--
-- Name: birds birds_sciName_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.birds
    ADD CONSTRAINT "birds_sciName_key" UNIQUE ("sciName");


--
-- Name: locations locations_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_pkey PRIMARY KEY (location_id);


--
-- Name: searches searches_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.searches
    ADD CONSTRAINT searches_pkey PRIMARY KEY (search_id);


--
-- Name: searches searches_bird_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.searches
    ADD CONSTRAINT searches_bird_id_fkey FOREIGN KEY (bird_id) REFERENCES public.birds("speciesCode");


--
-- Name: searches searches_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.searches
    ADD CONSTRAINT searches_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.locations(location_id);


--
-- PostgreSQL database dump complete
--

