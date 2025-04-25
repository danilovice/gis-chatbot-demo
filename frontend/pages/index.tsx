import React from "react";
import dynamic from "next/dynamic";
import Head from "next/head";

const Map = dynamic(() => import("./components/GISMap"), { ssr: false });

export default function Home() {
  return (
    <>
      <Head>
        <title>GIS Chatbot Demo</title>
      </Head>
      <header style={{ textAlign: "center", padding: "1rem", background: "#e0f7fa" }}>
        <h1>GIS Chatbot met AI</h1>
        <p>Zoek gebieden op de kaart!</p>
      </header>
      <main style={{ display: "flex", justifyContent: "center", padding: "2rem" }}>
        <div style={{ width: "80%", height: "500px" }}>
          <Map />
        </div>
      </main>
    </>
  );
}
