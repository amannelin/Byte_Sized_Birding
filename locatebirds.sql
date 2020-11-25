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
haiwoo	Dryobates villosus	Hairy Woodpecker	hairy+woodpecker	https://www.xeno-canto.org/568349/embed?simple=1
amecro	Corvus brachyrhynchos	American Crow	american+crow	https://www.xeno-canto.org/597661/embed?simple=1
whbnut	Sitta carolinensis	White-breasted Nuthatch	white-breasted+nuthatch	https://www.xeno-canto.org/580359/embed?simple=1
houfin	Haemorhous mexicanus	House Finch	house+finch	https://www.xeno-canto.org/573017/embed?simple=1
cangoo	Branta canadensis	Canada Goose	canada+goose	https://www.xeno-canto.org/603501/embed?simple=1
mallar3	Anas platyrhynchos	Mallard	mallard	https://www.xeno-canto.org/598281/embed?simple=1
rocpig	Columba livia	Rock Pigeon	rock+pigeon	\N
norcar	Cardinalis cardinalis	Northern Cardinal	northern+cardinal	https://www.xeno-canto.org/601752/embed?simple=1
pilwoo	Dryocopus pileatus	Pileated Woodpecker	pileated+woodpecker	https://www.xeno-canto.org/599834/embed?simple=1
daejun	Junco hyemalis	Dark-eyed Junco	dark-eyed+junco	https://www.xeno-canto.org/570869/embed?simple=1
lessca	Aythya affinis	Lesser Scaup	lesser+scaup	\N
buffle	Bucephala albeola	Bufflehead	bufflehead	https://www.xeno-canto.org/361920/embed?simple=1
rudduc	Oxyura jamaicensis	Ruddy Duck	ruddy+duck	https://www.xeno-canto.org/591765/embed?simple=1
pibgre	Podilymbus podiceps	Pied-billed Grebe	pied-billed+grebe	https://www.xeno-canto.org/600726/embed?simple=1
y00475	Fulica americana	American Coot	american+coot	https://www.xeno-canto.org/575486/embed?simple=1
laugul	Leucophaeus atricilla	Laughing Gull	laughing+gull	https://www.xeno-canto.org/572825/embed?simple=1
libher	Egretta caerulea	Little Blue Heron	little+blue+heron	https://www.xeno-canto.org/598018/embed?simple=1
margod	Limosa fedoa	Marbled Godwit	marbled+godwit	https://www.xeno-canto.org/563172/embed?simple=1
rudtur	Arenaria interpres	Ruddy Turnstone	ruddy+turnstone	https://www.xeno-canto.org/593288/embed?simple=1
moudov	Zenaida macroura	Mourning Dove	mourning+dove	https://www.xeno-canto.org/572383/embed?simple=1
whtspa	Zonotrichia albicollis	White-throated Sparrow	white-throated+sparrow	https://www.xeno-canto.org/467709/embed?simple=1
rethaw	Buteo jamaicensis	Red-tailed Hawk	red-tailed+hawk	https://www.xeno-canto.org/519775/embed?simple=1
yebsap	Sphyrapicus varius	Yellow-bellied Sapsucker	yellow-bellied+sapsucker	https://www.xeno-canto.org/418337/embed?simple=1
hoomer	Lophodytes cucullatus	Hooded Merganser	hooded+merganser	https://www.xeno-canto.org/346072/embed?simple=1
herthr	Catharus guttatus	Hermit Thrush	hermit+thrush	https://www.xeno-canto.org/544580/embed?simple=1
orcwar	Leiothlypis celata	Orange-crowned Warbler	orange-crowned+warbler	https://www.xeno-canto.org/591824/embed?simple=1
yerwar	Setophaga coronata	Yellow-rumped Warbler	yellow-rumped+warbler	\N
towwar	Setophaga townsendi	Townsend's Warbler	townsend's+warbler	https://www.xeno-canto.org/597954/embed?simple=1
rinduc	Aythya collaris	Ring-necked Duck	ring-necked+duck	https://www.xeno-canto.org/100902/embed?simple=1
passer1	Passeriformes sp.	passerine sp.	passerine+sp.	\N
norfli	Colaptes auratus	Northern Flicker	northern+flicker	https://www.xeno-canto.org/603653/embed?simple=1
wiltur	Meleagris gallopavo	Wild Turkey	wild+turkey	https://www.xeno-canto.org/539775/embed?simple=1
annhum	Calypte anna	Anna's Hummingbird	anna's+hummingbird	https://www.xeno-canto.org/549602/embed?simple=1
wesgul	Larus occidentalis	Western Gull	western+gull	https://www.xeno-canto.org/562633/embed?simple=1
bcnher	Nycticorax nycticorax	Black-crowned Night-Heron	black-crowned+night-heron	\N
nutwoo	Dryobates nuttallii	Nuttall's Woodpecker	nuttall's+woodpecker	https://www.xeno-canto.org/482294/embed?simple=1
stejay	Cyanocitta stelleri	Steller's Jay	steller's+jay	https://www.xeno-canto.org/603262/embed?simple=1
ribgul	Larus delawarensis	Ring-billed Gull	ring-billed+gull	https://www.xeno-canto.org/533687/embed?simple=1
baleag	Haliaeetus leucocephalus	Bald Eagle	bald+eagle	https://www.xeno-canto.org/344281/embed?simple=1
brncre	Certhia americana	Brown Creeper	brown+creeper	https://www.xeno-canto.org/497492/embed?simple=1
tuftit	Baeolophus bicolor	Tufted Titmouse	tufted+titmouse	https://www.xeno-canto.org/591473/embed?simple=1
whcspa	Zonotrichia leucophrys	White-crowned Sparrow	white-crowned+sparrow	https://www.xeno-canto.org/515386/embed?simple=1
norsho	Spatula clypeata	Northern Shoveler	northern+shoveler	https://www.xeno-canto.org/586812/embed?simple=1
grhowl	Bubo virginianus	Great Horned Owl	great+horned+owl	https://www.xeno-canto.org/587910/embed?simple=1
gresca	Aythya marila	Greater Scaup	greater+scaup	https://www.xeno-canto.org/322883/embed?simple=1
hergul	Larus argentatus	Herring Gull	herring+gull	https://www.xeno-canto.org/603672/embed?simple=1
comloo	Gavia immer	Common Loon	common+loon	https://www.xeno-canto.org/488030/embed?simple=1
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

