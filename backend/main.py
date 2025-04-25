from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from geojson import FeatureCollection
from bson.json_util import dumps

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient("mongodb://localhost:27017")
db = client["gisdb"]
collection = db["gebieden"]

@app.get("/gebieden")
def get_gebieden():
    features = list(collection.find())
    return FeatureCollection(features)
