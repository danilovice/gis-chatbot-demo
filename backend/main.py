from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from geojson import FeatureCollection
from bson.json_util import dumps
import os
from dotenv import load_dotenv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# MongoDB client
app = FastAPI()
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["gisdb"]

@app.get("/gebieden/{naam}")
def get_gebied(naam: str):
    result = db.gebieden.find_one({"naam": naam}, {"_id": 0})
    return result if result else {"error": "Gebied niet gevonden"}

@app.get("/gebieden/within_radius/")
def get_gebieden_within_radius(lng: float, lat: float, radius_km: float):
    """ Zoek gebieden binnen een bepaalde straal """

    features = list(db.gebieden.find({
        "geom": {
            "$geoWithin": {
                "$centerSphere": [[lng, lat], radius_km / 6378.1]
            }
        }
    }, {"_id": 0}))  # _id weglaten voor nette output
    return FeatureCollection(features)

@app.get("/gebieden/nearest/")
def get_nearest_gebied(lng: float, lat: float, max_distance_km: float = 100):
    """ Zoek het dichtstbijzijnde gebied binnen max_distance_km """
    max_distance_meters = max_distance_km * 1000
    gebied = db.gebieden.find_one({
        "geom": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [lng, lat]
                },
                "$maxDistance": max_distance_meters
            }
        }
    }, {"_id": 0})

    return {"gebied": gebied}