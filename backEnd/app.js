/*import React, { useState } from 'react';
import './app.css';

function App() {
  const [inputWord, setInputWord] = useState('');
  const [transcription, setTranscription] = useState([]);
  const [loading, setLoading] = useState(false);

  // Simula una llamada al backend para obtener la transcripción AFI y los colores
  const fetchTranscription = async (word) => {
    setLoading(true);

    // Simulación de datos devueltos por la API
    const simulatedResponse = [
      { character: "h", color: "green" },
      { character: "ə", color: "yellow" },
      { character: "l", color: "red" },
      { character: "oʊ", color: "yellow" }
    ];

    // Simular un pequeño retraso
    setTimeout(() => {
      setTranscription(simulatedResponse);
      setLoading(false);
    }, 500);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputWord.trim()) {
      fetchTranscription(inputWord);
    }
  };

  return (
    <div className="app">
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
            style={{ color: item.color, fontSize: '1.5em', margin: '0 5px' }}
          >
            {item.character}
          </span>
        ))}
      </div>
    </div>
  );
}

export default app;
*/
const fonemasIngles = [
    'iː', 'ɪ', 'e', 'æ', 'ɑː', 'ɒ', 'ɔː', 'ʊ', 'uː', 'ʌ', 'ə',  // Vocales
    'aɪ', 'eɪ', 'aʊ', 'ɔɪ', 'əʊ', 'oʊ',  // Diptongos
    'p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 
    's', 'z', 'ʃ', 'ʒ', 'tʃ', 'dʒ', 'm', 'n', 'ŋ', 
    'l', 'r', 'j', 'w', 'h'  // Consonantes
];
const fonemaEspanol = [
    'a', 'e', 'i', 'o', 'u',  // Vocales
    'p', 'b', 't', 'd', 'k', 'g', 'f', 's', 'x', 'ʝ', 'ʎ', 
    'm', 'n', 'ɲ', 'r', 'ɾ', 'l', 'ʃ', 'tʃ', 'θ', 
    'β', 'ð', 'ɣ'  // Consonantes
];

const form =document.getElementById('transcripcion-form');
const resultado = document.getElementById('resultado');

form.addEventListener('submit', function(event){
    event.preventDefault();
    const palabra = document.getElementById('palabra').value;
    transcribir(palabra);
});

function transcribir(palabra) {
    const fonemasPalabra = palabra.split(''); // Simula que cada letra es un fonema
    let transcripcion = '';

    fonemasPalabra.forEach(fonema => {
        if (fonemasEspanol.includes(fonema)) {
            transcripcion += `<span class="igual">${fonema}</span>`;
        } else {
            transcripcion += `<span class="diferente">${fonema}</span>`;
        }
    });

    resultado.innerHTML = transcripcion;
}

// Función que determina si el fonema existe en español
function esIgualAEspanol(fonema) {
    const iguales = fonemaEspanol;
    return iguales.includes(fonema);
}

// Función que determina si el fonema es similar al español
function esSimilarAEspanol(fonema) {
    const similares = ['ʃ', 'ʒ', 'ð', 'θ', 'ŋ', 'v', 'z'];
    return similares.includes(fonema);
}

