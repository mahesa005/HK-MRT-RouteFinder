from models.node import Node
from collections import deque
from utils.station_loader import load_station_nodes

# def main():
    # stations = load_station_nodes("hk-metro-nodes.json")
    # print(f"Loaded {len(stations)} stations")
    
    # # Print beberapa stasiun untuk testing
    # for i, station in enumerate(stations):
    #     print(f"\n {i+1}. Station: {station.val}")
    #     print(f"Neighbours ({len(station.neighbours)}):")
    #     for j, neighbor in enumerate(station.neighbours):
    #         print(f"  - {neighbor.val}")

def bfs_search(start: Node, end: Node):
    visited = set({start})
    queue = deque([start])
    path = []
    stop_ctr = 0
    parent = {start: None}

    while queue:
            current = (queue).popleft()
            if current.val == end.val:
                while current:
                    path.append(current)
                    current = parent.get(current)
                    stop_ctr += 1
                
                path.reverse()
                return path, stop_ctr
            
            else:
                for n in current.neighbours:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
                        parent[n] = current
    
    return path, stop_ctr

def find_station_by_name(stations, name):
    """Find a station in the list by its name."""
    for station in stations:
        if station.val.lower() == name.lower():
            return station
    return None

def main():
    file_name = input("Enter JSON file name: ")
    stations = load_station_nodes(file_name)
    if not stations:
        print("No stations loaded. Please check your JSON file.")
        return
    
    print(f"Successfully loaded {len(stations)} stations.")

    start_name = input("\nInput start station: ")
    end_name = input("\nInput end station: ")

     # Find station objects by name
    start_station = find_station_by_name(stations, start_name)
    end_station = find_station_by_name(stations, end_name)

    # Validate user input
    if not start_station:
        print(f"Error: Start station '{start_name}' not found.")
        return
    if not end_station:
        print(f"Error: End station '{end_name}' not found.")
        return
    
    result = bfs_search(start_station, end_station)

    # Display results
    if isinstance(result, tuple) and len(result) == 2:
        path, stop_count = result
        print(f"\nRoute from {start_name} to {end_name}:")
        print(f"Total Stations visited: {stop_count}")
        print("Stops:")
        for i, station in enumerate(path):
            print(f"{i+1}. {station.val}")
    else:
        print("Could not find a route between the specified stations.")


        

if __name__ == "__main__":
    main()