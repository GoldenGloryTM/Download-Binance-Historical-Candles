# main.py
import config
from BinanceDataDownloader import BinanceDataDownloader

# Inicializa el descargador con la configuración
downloader = BinanceDataDownloader(config.config)

# Obtiene los datos de las velas (klines)
klines_data = downloader.get_klines()

# Descarga de un solo simbolo.
filename = f"database/{config.config['symbol']}_{config.config['interval']}.csv"

# Guarda los datos en un archivo CSV con el nuevo nombre
downloader.save_to_csv(klines_data, filename)

print(f"Los datos se han descargado correctamente y se han guardado en {filename}")
