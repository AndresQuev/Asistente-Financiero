Markdown# 📈 Asistente Virtual Financiero

Asistente interactivo por voz desarrollado en Python para el monitoreo de mercados financieros, cotizaciones de criptoactivos y tipos de cambio en tiempo real. 

Este proyecto fue desarrollado como parte de las actividades prácticas de la asignatura **Ingeniería del Conocimiento** (Licenciatura en Informática y Desarrollo de Software - Universidad del Aconcagua).

---

## 🚀 Características y Funcionalidades

- **Criptomonedas en tiempo real:** Consulta el valor spot en USD de Bitcoin, Ethereum, Solana, USDT, entre otras, consumiendo la API pública de CoinGecko.
- **Mercado bursátil (Acciones):** Consulta de precios y cálculo automatizado de la variación diaria porcentual (tendencia alcista/bajista) de acciones internacionales mediante `yfinance`.
- **Tipo de cambio local:** Consulta en tiempo real de cotizaciones del mercado cambiario (Dólar Blue) a través de `DolarApi`.
- **Accesos directos:** Apertura asistida por voz de plataformas analíticas como TradingView y Binance.
- **Interacción por voz completa:** Reconocimiento de voz (STT) con ajuste de ruido ambiental y síntesis de voz (TTS) en español.

---

## 🛠️ Tecnologías y Librerías

- **Python 3.10+**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/): Síntesis de voz fuera de línea (Text-to-Speech).
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/): Procesamiento y transcripción de comandos de voz (Speech-to-Text).
- [`yfinance`](https://pypi.org/project/yfinance/): Acceso y procesamiento de datos financieros de Yahoo Finance.
- [`requests`](https://pypi.org/project/requests/): Consumo de APIs REST (CoinGecko y DolarApi).
- [`PyAudio`](https://pypi.org/project/PyAudio/): Interfaz de bajo nivel para la captura de audio por micrófono.

---

## 📥 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/AndresQuev/Asistente-Financiero.git](https://github.com/AndresQuev/Asistente-Financiero.git)
   cd Asistente-Financiero
Crear y activar un entorno virtual (recomendado):Bash# En Windows
python -m venv .venv
.venv\Scripts\activate
Instalar las dependencias:Bashpip install -r requirements.txt
Nota para Windows: Si se presenta algún inconveniente al instalar PyAudio, puede instalarse mediante pip install pipwin seguido de pipwin install pyaudio.🎙️ Comandos de Voz de EjemploUna vez iniciado el script (python main.py), puedes interactuar diciendo:CategoríaEjemplo de comandoCripto"Precio de bitcoin", "Cuánto vale ethereum", "Cotización de solana"Acciones"Precio de la acción de Apple", "Cotización de Tesla", "Acción de Mercado Libre"Divisas"Precio del dólar", "Tipo de cambio"Plataformas"Abrir TradingView", "Abrir Binance"Utilidades"Qué hora es"Finalizar"Adiós", "Terminar", "Salir"📂 Estructura del RepositorioPlaintext├── main.py              # Script principal del asistente y lógica de comandos
├── requirements.txt     # Lista de paquetes y dependencias
├── .gitignore           # Exclusión de entornos virtuales y archivos locales
└── README.md            # Documentación del proyecto
