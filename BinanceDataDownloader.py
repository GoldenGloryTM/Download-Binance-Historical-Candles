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
    
    def format_values(self, data):
        formatted_data = []
        for line in data:
            formatted_line = [
                datetime.fromtimestamp(line[0] / 1000).strftime('%d/%m/%Y %H:%M:%S'),
                "{:.2f}".format(float(line[1])),
                "{:.2f}".format(float(line[2])),
                "{:.2f}".format(float(line[3])),
                "{:.2f}".format(float(line[4])),
                "{:.0f}".format(float(line[5]))
            ]
            formatted_data.append(formatted_line)
        return formatted_data
    

    def get_klines(self):
        params = {
            'symbol': self.symbol,
            'interval': self.interval,
            'startTime': self.start_time,
            'endTime': self.end_time
        }
        response = requests.get(self.base_url, params=params)
        #return response.json()
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener los datos: {response.status_code}")
            return[]

    def save_to_csv(self, data, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['time', 'open', 'high', 'low', 'close', 'volume'])
            writer.writerows(data)
