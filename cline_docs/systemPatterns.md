# System Patterns

## Architecture
- Single Python script architecture
- Utilizes Folium for map generation
- Generates static HTML output

## Key Technical Decisions
1. Use of Folium library
   - Built on Leaflet.js
   - Provides Python interface for map creation
   - Generates interactive HTML/JavaScript output

2. Data Structure
   - Location data stored as tuples
   - Each tuple contains (name, latitude, longitude)
   - Simple and efficient data structure for iteration

3. Map Generation Pattern
   - Initialize base map with Dubai center coordinates
   - Iterate through location data
   - Add markers programmatically
   - Save output as HTML file

## Best Practices
- Clear separation of data and map generation logic
- Consistent coordinate format
- Descriptive location names
- Efficient iteration for marker placement
