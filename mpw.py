import math

# Function to convert Maidenhead grid locator to latitude and longitude
def grid_to_latlon(grid):
    print(f"Converting grid locator: {grid}")  # Debugging statement
    grid = grid.strip().upper()
    if len(grid) < 4 or not grid.isalnum():
        raise ValueError("Invalid Maidenhead grid locator.")
    
    # Calculate longitude
    lon = (ord(grid[0]) - ord('A')) * 20 - 180 + (int(grid[2]) * 2)
    # Calculate latitude
    lat = (ord(grid[1]) - ord('A')) * 10 - 90 + int(grid[3])
    
    print(f"Converted {grid} to lat: {lat}, lon: {lon}")  # Debugging statement
    return lat, lon

# Haversine formula to calculate distance between two lat/lon points in miles
def haversine(lat1, lon1, lat2, lon2):
    print(f"Calculating distance between ({lat1}, {lon1}) and ({lat2}, {lon2})")  # Debugging statement
    R = 3958.8  # Radius of Earth in miles
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    
    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    print(f"Calculated distance: {distance} miles")  # Debugging statement
    return distance

# Function to calculate miles per watt
def miles_per_watt(distance, power):
    print(f"Calculating miles per watt with distance: {distance} miles and power: {power} watts")  # Debugging statement
    return distance / power

# Main script
def main():
    print("QRP Miles per Watt Calculator")
    
    # Get user input for Maidenhead grid locators and power
    grid1 = input("Enter your Maidenhead grid locator: ").strip()
    grid2 = input("Enter the other station's Maidenhead grid locator: ").strip()
    power = float(input("Enter your transmission power in watts: "))
    
    # Convert grids to lat/lon and calculate distance
    try:
        lat1, lon1 = grid_to_latlon(grid1)
        lat2, lon2 = grid_to_latlon(grid2)
        distance = haversine(lat1, lon1, lat2, lon2)
    except ValueError as e:
        print(e)
        return
    
    # Calculate miles per watt
    mpw = miles_per_watt(distance, power)
    
    # Display results
    print(f"Distance between the two stations: {distance:.2f} miles")
    print(f"Miles per Watt: {mpw:.2f} miles/watt")

if __name__ == "__main__":
    main()
