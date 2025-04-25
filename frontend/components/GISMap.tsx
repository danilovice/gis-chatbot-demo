import React from "react";
import { MapContainer, TileLayer, GeoJSON } from "react-leaflet";
import { useEffect, useState } from "react";

export default function GISMap() {
  const [geoData, setGeoData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/gebieden")
      .then(res => res.json())
      .then(setGeoData);
  }, []);

  return (
    <MapContainer center={[52.1, 5.1] as [number, number]} zoom={8} style={{ height: "100%", width: "100%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {geoData && <GeoJSON data={geoData} />}
    </MapContainer>
  );
}
