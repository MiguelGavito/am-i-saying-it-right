// frontend/src/App.tsx
import React, { useState } from "react";

const App: React.FC = () => {
  const [inputWord, setInputWord] = useState("");
  const [transcription, setTranscription] = useState<
    { character: string; color: string }[]
  >([]);
  const [loading, setLoading] = useState(false);

  const fetchTranscription = async (word: string) => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/api/transcription", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ word }),
      });
      const data = await response.json();
      setTranscription(data.transcription);
    } catch (error) {
      console.error("Error al obtener la transcripción:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchTranscription(inputWord);
  };

  return (
    <div className="App">
      <h1>Pronunciación AFI con Colores</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ingresa una palabra"
          value={inputWord}
          onChange={(e) => setInputWord(e.target.value)}
        />
        <button type="submit">Buscar</button>
      </form>

      {loading && <p>Cargando transcripción...</p>}

      <div className="transcription">
        {transcription.map((item, index) => (
          <span
            key={index}
            style={{ color: item.color, fontSize: "1.5em", margin: "0 5px" }}
          >
            {item.character}
          </span>
        ))}
      </div>
    </div>
  );
};

export default App;
