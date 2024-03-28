import csv
import requests
from datetime import datetime

class BinanceDataDownloader:
    
    def __init__(self, config):
        self.symbol = config['symbol']
        self.interval = config['interval']
        self.start_time = self.format_date(config['start_time'])
        self.end_time = self.format_date(config['end_time'])
        self.base_url = config['base_url']

    def format_date(self, date_str):
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        timestamp = int(datetime.timestamp(date_obj) * 1000)
        return timestamp

    def get_klines(self):
        params = {
            'symbol': self.symbol,
            'interval': self.interval,
            'startTime': self.start_time,
            'endTime': self.end_time
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def save_to_csv(self, data, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['time', 'open', 'high', 'low', 'volume'])
            for line in data:
                open_time = datetime.fromtimestamp(line[0]/1000).strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([open_time, line[1], line[2], line[3], line[5]])

