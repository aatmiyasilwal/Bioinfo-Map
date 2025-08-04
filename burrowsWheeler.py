def burrowsWheeler(file, string):
    # Step 1: Read content from the file
    with open(file, 'r') as f:
        text = f.read().strip()  # Read and strip any extra whitespace/newlines

    # Step 2: Apply Burrows-Wheeler Transform
    def bwt(s):
        """ Perform Burrows-Wheeler Transform on string s. """
        n = len(s)
        # Create a list of all rotations of s
        rotations = [s[i:] + s[:i] for i in range(n)]
        # Sort the rotations
        rotations.sort()
        # Construct the BWT result
        bwt_result = ''.join(rotation[-1] for rotation in rotations)
        return bwt_result, rotations

    # Step 3: Perform BWT on the text
    bwt_result, rotations = bwt(text)

    # Step 4: Search for the pattern in BWT using a simple approach
    def search_pattern(bwt_result, pattern):
        """ Search for a pattern in BWT result and return index if found. """
        # Count occurrences of each character in BWT result
        count = {}
        for char in bwt_result:
            count[char] = count.get(char, 0) + 1
        
        # Create a cumulative count dictionary
        total = 0
        cumulative_count = {}
        for char in sorted(count.keys()):
            cumulative_count[char] = total
            total += count[char]

        # Perform backward search
        top = 0
        bottom = len(bwt_result) - 1

        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                if symbol in bwt_result[top:bottom + 1]:
                    top_index = bwt_result.find(symbol, top)
                    bottom_index = bwt_result.rfind(symbol, top, bottom + 1)

                    if top_index == -1 or bottom_index == -1:
                        return -1  # Pattern not found

                    top = cumulative_count[symbol] + (top_index - bwt_result.count(symbol, 0, top))
                    bottom = cumulative_count[symbol] + (bottom_index - bwt_result.count(symbol, 0, bottom + 1))
                else:
                    return -1  # Pattern not found
            else:
                return top  # Found pattern

        return -1  # Pattern not found

    # Step 5: Find the index of the line containing the pattern
    index_found = search_pattern(bwt_result, string)

    if index_found != -1:
        return f"The string '{string}' was found at index {index_found}."
    else:
        return f"The string '{string}' was not found."

# Example usage:
result = burrowsWheeler('COMP3353/Individual_Project/placeNames.txt', 'Centennial')
print(result)