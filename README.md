# GIS Chatbot Demo

Combineert Dify, FastAPI, MongoDB/PostGIS en een Leaflet.js frontend voor geografische AI-query's.

## Stappen:

1: Clone het project: \
git clone github.com/danilovice/gis-chatbot-demo

2: Installeer de dependencies voor de frontend \
cd /frontend \
npm install

3: Installeer de dependencies voor de backend

**optioneel maar aanbevolen: Creëer een virtueel environment voor python**

cd /backend \
python -m venv .venv

.venv\Scripts\activate \
pip install -r requirements.txt

of eenvoudig in vs code: <https://code.visualstudio.com/docs/python/environments#:~:text=To%20create%20local%20environments%20in,environment%20types%3A%20Venv%20or%20Conda> 

4: Run backend (FastAPI):

uvicorn main:app --reload

5: Start frontend (Next.js):

npm run dev

6: Open chatbot & kaart in browser: http://localhost:3000