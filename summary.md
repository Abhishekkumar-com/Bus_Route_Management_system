```markdown
# Technical Summary & Viva Notes — Bus Route Management System (PS No. 82)

## 1. Data Structure Choice
- *Dictionary of Dictionaries (BUS_NETWORK):* Represents an adjacency list for an undirected weighted graph. Checking if a stop exists or fetching its direct neighbors takes $O(1)$ average time.
- *Bidirectional Edges:* Every road (e.g., Durg-Bhilai: 10) is stored in both directions so routes work both ways.

## 2. Why BFS (Breadth-First Search)?
- Since the problem asks for the *route with the fewest stops*, BFS explores the network level-by-level using a FIFO queue (collections.deque) and a visited set, guaranteeing the minimum-stop path in $O(V + E)$ time without infinite loops.

## 3. Key Test Cases Covered
1. *Normal Input:* Show connections for Raipur displays Bhilai (30 km), Bilaspur (110 km), Dhamtari (80 km), Durg (40 km).
2. *Boundary Input:* Finding route from Durg to Durg returns 0 km and Rs. 0.00 fare immediately.
3. *Invalid Inputs:*
   - Durg to Jagdalpur detects disconnected graph components (Jagdalpur-Kondagaon is isolated) and outputs No route available.
   - Searching for Delhi cleanly outputs Stop 'Delhi' not found.
4. *Multi-Stop Route:* Bhilai -> Raipur -> Bilaspur spans 3 stops, 140 km (30 + 110), and costs Rs. 210.00 (140 * 1.50).