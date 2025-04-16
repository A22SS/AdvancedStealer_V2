import os
from pathlib import Path
import json

class DataAggregator:
    exfil_data_directory = Path.cwd() / "exfil_data"

    @staticmethod
    def aggregate(data_dict):
        if not DataAggregator.exfil_data_directory.exists():
            os.makedirs(DataAggregator.exfil_data_directory)
        aggregated_file = DataAggregator.exfil_data_directory / "aggregated_data.json"
        new_data = {}
        for source, data in data_dict.items():
            if isinstance(data, dict):
                new_data.update(data)
            else:
                new_data[source] = data
        if aggregated_file.exists():
            with open(aggregated_file, 'r') as file:
                previous_data = json.load(file)
            previous_data.update(new_data)
            previous_data = dict(list(previous_data.items())[-100:])
        else:
            previous_data = new_data
        with open(aggregated_file, 'w') as file:
            json.dump(previous_data, file, indent=4)
        with open(aggregated_file, 'r') as file:
            return file.read()

aggregator = DataAggregator()
