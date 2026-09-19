# 📈 Asistente Virtual Financiero

Asistente interactivo por voz desarrollado en Python para el monitoreo de mercados financieros, cotizaciones de criptoactivos y tipos de cambio en tiempo real.

Este proyecto fue desarrollado como parte de las actividades prácticas de la asignatura **Ingeniería del Conocimiento** (Licenciatura en Informática y Desarrollo de Software - Universidad del Aconcagua)[cite: 1].

---

## 🚀 Características y Funcionalidades

- **Criptomonedas en tiempo real:** Consulta el valor spot en USD de Bitcoin, Ethereum, Solana, USDT, entre otras, consumiendo la API pública de CoinGecko.
- **Mercado bursátil (Acciones):** Consulta de precios y cálculo automatizado de la variación diaria porcentual (tendencia alcista/bajista) de acciones internacionales mediante `yfinance`[cite: 1, 2].
- **Tipo de cambio local:** Consulta en tiempo real de cotizaciones del mercado cambiario (Dólar Blue) a través de `DolarApi`[cite: 1].
- **Accesos directos:** Apertura asistida por voz de plataformas analíticas como TradingView y Binance[cite: 1].
- **Interacción por voz completa:** Reconocimiento de voz (STT) con ajuste de ruido ambiental y síntesis de voz (TTS) en español[cite: 1, 2].

---

## 🛠️ Tecnologías y Librerías

- **Python 3.10+**
- `pyttsx3`: Síntesis de voz fuera de línea (Text-to-Speech)[cite: 2].
- `SpeechRecognition`: Procesamiento y transcripción de comandos de voz (Speech-to-Text)[cite: 2].
- `yfinance`: Acceso y procesamiento de datos financieros de Yahoo Finance[cite: 2].
- `requests`: Consumo de APIs REST (CoinGecko y DolarApi)[cite: 1].
- `PyAudio`: Interfaz de hardware para captura de audio por micrófono.

---

## 📥 Instalación y Configuración

### 1. Clonar el repositorio
git clone https://github.com/AndresQuev/Asistente-Financiero.git
cd Asistente-Financiero

### 2. Crear y activar un entorno virtual (Recomendado)
# En Windows:
python -m venv .venv
.venv\Scripts\activate

### 3. Instalar las dependencias
pip install -r requirements.txt

> **Nota para Windows:** Si ocurre algún error al instalar PyAudio, puede solucionarse ejecutando `pip install pipwin` y luego `pipwin install pyaudio`.

---

## 🎙️ Comandos de Voz de Ejemplo

Una vez iniciado el script (`python main.py`), puedes interactuar con los siguientes comandos[cite: 1, 2]:

- **Criptomonedas:** *"Precio de bitcoin"*, *"Cuánto vale ethereum"*, *"Cotización de solana"*[cite: 1]
- **Acciones:** *"Precio de la acción de Apple"*, *"Cotización de Tesla"*, *"Acción de Mercado Libre"*[cite: 1, 2]
- **Divisas:** *"Precio del dólar"*, *"Tipo de cambio"*[cite: 1]
- **Plataformas:** *"Abrir TradingView"*, *"Abrir Binance"*[cite: 1]
- **Hora:** *"Qué hora es"*[cite: 2]
- **Finalizar:** *"Adiós"*, *"Terminar"*, *"Salir"*[cite: 2]

---

## 📂 Estructura del Repositorio

- `main.py`: Script principal del asistente y lógica de comandos[cite: 3].
- `requirements.txt`: Lista de dependencias de Python.
- `.gitignore`: Exclusión de entornos virtuales (`.venv`) y archivos locales.
- `README.md`: Documentación del proyecto.
