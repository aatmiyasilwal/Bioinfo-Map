import heapq
import streamlit as st
from data import campusGraph, campusMappings, campusReversedMappings
from levenshtein import StringComparer

def find_shortest_paths(graph, start, end, num_paths=3):
    """ Finds up to `num_paths` shortest paths between `start` and `end` in a weighted graph. """
    pq = []
    heapq.heappush(pq, (0, [start]))
    found_paths = []
    
    while pq and len(found_paths) < num_paths:
        cost, path = heapq.heappop(pq)
        current = path[-1]
        
        if current == end:
            found_paths.append((cost, path))
            continue
        
        for neighbor, weight in graph[current]:
            if neighbor not in path:
                new_cost = cost + weight
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, new_path))
    
    return found_paths

def main():
    """ Main function to handle user input and find the shortest paths. """
    comparer = StringComparer()
    hkuPlaces = list(campusMappings.keys())
    
    # Theme toggle using Streamlit's built-in functionality
    st.sidebar.title("Settings")
    theme_option = st.sidebar.radio("Select Theme", ("Light", "Dark"))
    
    if theme_option == "Dark":
        st.markdown(
            """
            <style>
            .reportview-container {
                background: #2b2b2b;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    
    # Centered title using HTML
    st.markdown("<h1 style='text-align: center;'>Navigating HKU</h1>", unsafe_allow_html=True)
    
    # Input forms for start and end places
    start_place = st.text_input("Enter the starting place:")
    end_place = st.text_input("Enter the ending place:")
    
    if st.button("Find Paths"):
        # Check for valid start place
        if start_place.upper() in campusGraph:
            start_place = start_place.upper()
        else:
            temp_start = comparer.checkString(start_place, hkuPlaces)
            if temp_start == "":
                st.markdown("> Invalid start")
                return
            else:
                start_place = campusMappings[temp_start]
        
        # Check for valid end place
        if end_place.upper() in campusGraph:
            end_place = end_place.upper()
        else:
            temp_end = comparer.checkString(end_place, hkuPlaces)
            if temp_end == "":
                st.markdown("> Invalid end")
                return
            else:
                end_place = campusMappings[temp_end]
        
        # Find the shortest paths
        shortest_paths = find_shortest_paths(campusGraph, start_place, end_place)
        
        # Display the results
        if shortest_paths:
            st.markdown("### The shortest paths are:")
            for cost, path in shortest_paths:
                # Create buttons for each node in the path with arrows connecting them visually
                path_display = " ➡️ ".join([f"<button style='margin: 0 5px;'>{campusReversedMappings[i]}</button>" for i in path])
                st.markdown(f"{path_display}", unsafe_allow_html=True)
                st.markdown(f"##### Time Taken: {cost} minutes", unsafe_allow_html=True)
        else:
            st.markdown("> No paths found between the specified places.")

# if __name__ == "__main__":
main()