import config
from BinanceDataDownloader import BinanceDataDownloader

# Inicializa el descargador con la configuración
downloader = BinanceDataDownloader(config.config)

raw_data = downloader.get_klines()

filename = f"database/{config.config['symbol']}_{config.config['interval']}.csv"

if raw_data:
    formatted_data = downloader.format_values(raw_data)
    downloader.save_to_csv(formatted_data, filename)
    print(f"Los datos se han descargado correctamente y se han guardado en {filename}")