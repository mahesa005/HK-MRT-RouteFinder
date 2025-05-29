import json
import sys
from pathlib import Path

# Tambahkan direktori src ke Python path
current_script_path = Path(__file__).resolve()
project_src_directory = current_script_path.parent.parent  # src folder
sys.path.append(str(project_src_directory))

# Sekarang bisa import menggunakan absolute path
from models.node import Node

def load_json_from_data_folder(json_filename):
    try:
        # Get absolute path of current file
        current_script_path = Path(__file__).resolve()

        # Get main project folder directory
        project_folder_directory = current_script_path.parent.parent.parent

        # Get data folder directory
        json_file_path = project_folder_directory /'data'/ json_filename

        with open(json_file_path, 'r') as f:
            data = json.load(f)

        return data    
    
    except FileNotFoundError:
        print(f"Error: JSON file not found in {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON file: {json_file_path}. Make sure JSON format is valid.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def load_station_nodes(json_filename):
    station_data = load_json_from_data_folder(json_filename)

    if not isinstance(station_data, list):
        print(f"Error: Expected a list of stations from JSON, but got {type(station_data)}.")
        return []

    station_dict = {}  

    for raw_station in station_data:
        if isinstance(raw_station, dict) and 'name' in raw_station:
            station_name = raw_station['name']
            new_station = Node()
            new_station.val = station_name
            new_station.neighbours = []
            station_dict[station_name] = new_station
    
    
    for raw_station in station_data:
        if isinstance(raw_station, dict):
            current_station_name = raw_station['name']
            current_station = station_dict[current_station_name]
            
            if 'neighbours' in raw_station and isinstance(raw_station['neighbours'], list):
                for neighbour_station in raw_station['neighbours']:
                    neighbour_station_name = neighbour_station['name']
                    if neighbour_station_name in station_dict:
                        current_station.neighbours.append(station_dict[neighbour_station_name])
    return list(station_dict.values())