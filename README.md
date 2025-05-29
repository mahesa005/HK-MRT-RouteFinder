# HK-MTR-RouteFinder

A simple command-line tool that uses **Breadth-First Search (BFS)** to find the minimum number of stops between any two stations in the Hong Kong MTR network.

---

## How It Works

1. **Load** a JSON file defining the network as nodes (stations) and their neighbours (direct connections).  
2. **Run** BFS from your chosen start station until it reaches the target.  
3. **Output**:  
   - **Total stops needed** (number of edges/hops)  
   - **Station path** (sequence of station names)

---

## Usage

Open your terminal in the project folder and run:

```bash
py route_finder.py
```
---
This program was created for the Discrete Mathematics (IF1220) course paper.
By: Mahesa Fadhillah Andre (13523140)
