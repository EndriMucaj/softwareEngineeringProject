
Projekti funksionon në tri faza kryesore:

Scraping: Merr titujt e lajmeve live nga faqja e BBC-së.

NLP (Natural Language Processing): Përdor inteligjencën artificiale (spaCy) për të "lexuar" titujt dhe për të gjetur emrat e vendeve.

Weather Integration: Për çdo vend të gjetur, kërkon në OpenWeatherMap për temperaturën (në Celsius) dhe përshkrimin e motit.

Struktura e Dosjeve
Plaintext
project/
│
├── main.py              # Skedari kryesor që kontrollon rrjedhën
├── scraper.py           # Moduli që bën scraping e BBC News
├── weather_api.py       # Moduli për gjetjen e vendeve dhe thirrjen e API-së
├── data/
│   ├── news.csv         # Titujt e ruajtur fillestarë
│   └── final_data.csv   # Rezultati përfundimtar me Lajmin + Vendin + Motin
└── README.md            # Dokumentacioni (ky skedar)

Kërkesat (Installation)
Për të ekzekutuar këtë projekt, duhet të kesh Python të instaluar dhe të shkarkosh libraritë e mëposhtme:

Bash
pip install requests pandas beautifulsoup4 spacy
python -m spacy download en_core_web_sm

Përdorimi
Konfigurimi: Sigurohu që API_KEY në weather_api.py të jetë i saktë.

Ekzekutimi: Hap terminalin në dosjen e projektit dhe shkruaj:

Bash
python main.py
Rezultati: Pas përfundimit, kontrollo dosjen data/ për të parë skedarin final_data.csv.

Si funksionon kodi?
Logic Check: Nëse një titull thotë "Battle between Israel and Iran", skripti do të gjenerojë dy rreshta: një për motin në Izrael dhe një për motin në Iran.

Missing Locations: Nëse titulli nuk përmban asnjë vend (psh. "Tesla cuts car models"), kolona e vendndodhjes do të shënojë: no country/city mentioned in the news headline.

Units: Të gjitha temperaturat janë në Celsius (metric).

Teknologjitë e përdorura
Python 3.13

BeautifulSoup4: Për nxjerrjen e të dhënave nga HTML.

Pandas: Për menaxhimin e të dhënave dhe krijimin e CSV-së.

spaCy: Për njohjen e entiteteve emërore (NER).

OpenWeather API: Për të dhënat e motit në kohë reale.