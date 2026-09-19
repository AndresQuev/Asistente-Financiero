import datetime
import pyttsx3
import requests
import speech_recognition as sr
import webbrowser
import yfinance as yf

# ==========================================
# CONFIGURACIÓN DEL MOTOR DE VOZ (TTS)
# ==========================================
engine = pyttsx3.init()
engine.setProperty("rate", 160)     # Velocidad de habla equilibrada
engine.setProperty("volume", 0.9)   # Volumen de 0.0 a 1.0

# Buscar y asignar voz en español de forma dinámica
voces = engine.getProperty("voices")
for voz in voces:
    if "spanish" in voz.name.lower() or "es" in voz.id.lower() or "helena" in voz.name.lower():
        engine.setProperty("voice", voz.id)
        break

def hablar(mensaje: str):
    """Sintetiza voz a partir de texto utilizando la instancia global de pyttsx3."""
    print(f"Asistente: {mensaje}")
    engine.say(mensaje)
    engine.runAndWait()

# ==========================================
# RECONOCIMIENTO DE VOZ (STT)
# ==========================================
def transformar_audio_texto() -> str:
    """Captura el audio del micrófono y lo transcribe a texto mediante SpeechRecognition."""
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(origen, duration=0.6)  # Calibrar ruido ambiente
        print("\nEscuchando comando financiero...")
        try:
            audio = r.listen(origen, timeout=6, phrase_time_limit=8)
            pedido = r.recognize_google(audio, language="es-ES")
            print(f"Dijiste: {pedido}")
            return pedido.lower()
        except sr.WaitTimeoutError:
            return "sigo esperando"
        except sr.UnknownValueError:
            print("No se entendió el audio.")
            return "sigo esperando"
        except sr.RequestError:
            print("Error de conexión con el servicio de reconocimiento.")
            return "sigo esperando"
        except Exception as e:
            print(f"Error inesperado en audio: {e}")
            return "sigo esperando"

# ==========================================
# FUNCIONES MODULARES DEL DOMINIO FINANCIERO[cite: 1]
# ==========================================
def consultar_cripto(pedido: str):
    """Consulta el precio spot en USD de criptomonedas populares vía CoinGecko."""
    mapa_criptos = {
        "bitcoin": "bitcoin",
        "btc": "bitcoin",
        "ethereum": "ethereum",
        "eth": "ethereum",
        "solana": "solana",
        "tether": "tether",
        "usdt": "tether"
    }

    cripto_encontrada = None
    for clave, id_coingecko in mapa_criptos.items():
        if clave in pedido:
            cripto_encontrada = id_coingecko
            break

    if not cripto_encontrada:
        hablar("No identifiqué la criptomoneda. Puedes consultar por Bitcoin, Ethereum, Solana o Tether.")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto_encontrada}&vs_currencies=usd"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        respuesta = requests.get(url, headers=headers, timeout=5)
        datos = respuesta.json()
        if cripto_encontrada in datos:
            precio = datos[cripto_encontrada]["usd"]
            hablar(f"El valor actual de {cripto_encontrada.capitalize()} es de {precio} dólares.")
        else:
            hablar("No se encontraron cotizaciones en este momento.")
    except Exception:
        hablar("Ocurrió un error al conectar con el servidor de cotizaciones cripto.")

def consultar_accion(pedido: str):
    """Obtiene el último precio y la variación diaria de una acción mediante yfinance."""
    cartera = {
        "apple": "AAPL",
        "amazon": "AMZN",
        "google": "GOOGL",
        "tesla": "TSLA",
        "microsoft": "MSFT",
        "mercado libre": "MELI"
    }

    ticker = None
    empresa = None
    for nombre, t in cartera.items():
        if nombre in pedido:
            ticker = t
            empresa = nombre
            break

    if not ticker:
        ticker = pedido.split()[-1].upper()
        empresa = ticker

    try:
        activo = yf.Ticker(ticker)
        historial = activo.history(period="2d")
        if len(historial) >= 2:
            cierre_previo = historial["Close"].iloc[-2]
            ultimo = historial["Close"].iloc[-1]
            variacion = round(((ultimo - cierre_previo) / cierre_previo) * 100, 2)
            tendencia = "subió" if variacion >= 0 else "bajó"
            hablar(f"La acción de {empresa.upper()} cotiza a {round(ultimo, 2)} dólares y {tendencia} un {abs(variacion)} por ciento hoy.")
        elif not historial.empty:
            ultimo = historial["Close"].iloc[-1]
            hablar(f"La acción de {empresa.upper()} cotiza a {round(ultimo, 2)} dólares.")
        else:
            hablar(f"No obtuve datos de cotización para {empresa}.")
    except Exception:
        hablar(f"Hubo un fallo al obtener la información bursátil de {empresa}.")

def cotizacion_dolar():
    """Consulta la cotización del dólar en el mercado argentino."""
    url = "https://dolarapi.com/v1/dolares/blue"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            datos = res.json()
            compra = datos.get("compra")
            venta = datos.get("venta")
            hablar(f"El dólar blue cotiza a {compra} pesos para la compra y {venta} pesos para la venta.")
        else:
            hablar("No pude obtener los datos del tipo de cambio.")
    except Exception:
        hablar("Hubo un error de conexión al consultar el tipo de cambio.")

# ==========================================
# UTILIDADES GENERALES
# ==========================================
def pedir_hora():
    """Informa la hora actual[cite: 2]."""
    ahora = datetime.datetime.now()
    hablar(f"Son las {ahora.hour} horas con {ahora.minute} minutos.")

def saludo_inicial():
    """Saludo de apertura según el momento del día[cite: 2]."""
    hora = datetime.datetime.now().hour
    if hora < 6 or hora > 20:
        momento = "Buenas noches"
    elif 6 <= hora < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"
    hablar(f"{momento}. Tu terminal de asistencia financiera está lista. ¿Qué mercado deseas revisar?")

# ==========================================
# BUCLE PRINCIPAL DE COMANDOS[cite: 2]
# ==========================================
def centro_pedido():
    saludo_inicial()
    activo = True

    while activo:
        pedido = transformar_audio_texto()

        if pedido == "sigo esperando":
            continue

        # Comandos Cripto
        if any(c in pedido for c in ["cripto", "bitcoin", "ethereum", "solana", "tether", "usdt"]):
            consultar_cripto(pedido)

        # Comandos Acciones / Bolsa
        elif "acción" in pedido or "accion" in pedido or "cotización" in pedido or "cotizacion" in pedido:
            consultar_accion(pedido)

        # Comandos Mercado Cambiario / Divisas
        elif "dólar" in pedido or "dolar" in pedido or "tipo de cambio" in pedido:
            cotizacion_dolar()

        # Abrir plataformas financieras
        elif "tradingview" in pedido:
            hablar("Abriendo TradingView")
            webbrowser.open("https://www.tradingview.com")
        elif "binance" in pedido:
            hablar("Abriendo Binance")
            webbrowser.open("https://www.binance.com")

        # Utilidades básicas
        elif "hora" in pedido:
            pedir_hora()

        # Salida
        elif "adiós" in pedido or "terminar" in pedido or "salir" in pedido:
            hablar("Sesión finalizada. Hasta la próxima.")
            activo = False

if __name__ == "__main__":
    centro_pedido()