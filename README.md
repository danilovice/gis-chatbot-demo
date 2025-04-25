# GIS Chatbot Demo

Combines Dify, FastAPI, MongoDB/PostGIS, and a Leaflet.js frontend for geographic AI queries.

## Requirements

Make sure that you have nodejs, git and dify installed. 

## Steps:

1: Clone the project: \
git clone github.com/danilovice/gis-chatbot-demo

2: Install the dependencies for the frontend \
cd /frontend \
npm install

3: Install the dependencies for the backend

**Optional but recommended: Create a virtual environment for Python**

cd /backend \
python -m venv .venv

.venv\Scripts\activate \
pip install -r requirements.txt

Or simply in VS Code: <https://code.visualstudio.com/docs/python/environments#:~:text=To%20create%20local%20environments%20in,environment%20types%3A%20Venv%20or%20Conda> 

4: Run the backend (FastAPI):

uvicorn main:app --reload

5: Start the frontend (Next.js):

npm run dev

6: Open the chatbot & map in the browser: http://localhost:3000

## TODO

Add the backend API to dify 