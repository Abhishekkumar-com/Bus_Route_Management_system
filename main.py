from collections import deque

# Bus network stored as a dictionary of dictionaries (stop -> {neighbor: distance_km})
# Roads work in both directions
BUS_NETWORK = {
    "Durg": {"Bhilai": 10, "Raipur": 40, "Rajnandgaon": 45},
    "Bhilai": {"Durg": 10, "Raipur": 30},
    "Raipur": {"Bhilai": 30, "Durg": 40, "Bilaspur": 110, "Dhamtari": 80},
    "Bilaspur": {"Raipur": 110},
    "Dhamtari": {"Raipur": 80},
    "Rajnandgaon": {"Durg": 45},
    "Jagdalpur": {"Kondagaon": 75},
    "Kondagaon": {"Jagdalpur": 75},
}

FARE_PER_KM = 1.50


def show_all_stops():
    print("\nAvailable Bus Stops:")
    print(", ".join(BUS_NETWORK.keys()))


def show_connections():
    stop = input("Stop: ").strip()
    if stop not in BUS_NETWORK:
        print(f"Stop '{stop}' not found.")
        return

    connections = [f"{neighbor} ({dist} km)" for neighbor, dist in BUS_NETWORK[stop].items()]
    print(f"{stop} connects to: {', '.join(connections)}")


def bfs_shortest_stops(start, end):
    """Finds the route with the fewest stops using Breadth-First Search (BFS)."""
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current_stop = path[-1]

        if current_stop == end:
            return path

        for neighbor in BUS_NETWORK[current_stop]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


def find_route():
    source = input("From: ").strip()
    destination = input("To: ").strip()

    if source not in BUS_NETWORK:
        print(f"Stop '{source}' not found.")
        return
    if destination not in BUS_NETWORK:
        print(f"Stop '{destination}' not found.")
        return

    if source == destination:
        print("Source and destination are the same. Distance: 0 km.")
        print("Fare: Rs. 0.00")
        return

    route = bfs_shortest_stops(source, destination)
    if route is None:
        print(f"No route available between {source} and {destination}.")
        return

    total_distance = sum(
        BUS_NETWORK[route[i]][route[i + 1]] for i in range(len(route) - 1)
    )
    total_fare = total_distance * FARE_PER_KM

    print(f"Route: {' -> '.join(route)}")
    print(f"Stops: {len(route)} | Distance: {total_distance} km | Fare: Rs. {total_fare:.2f}")


def main():
    while True:
        print("\n--- Bus Route Management System ---")
        print("1. Show all stops")
        print("2. Show connections")
        print("3. Find route")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_all_stops()
        elif choice == "2":
            show_connections()
        elif choice == "3":
            find_route()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()