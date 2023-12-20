def opposite_index_select(lst, index):
    # Calculate the opposite index
    opposite_index = len(lst) - 1 - index
    
    # Check if the opposite index is within the valid range
    if 0 <= opposite_index < len(lst):
        # Return the element at the opposite index
        return lst[opposite_index]
    else:
        # Handle the case when the opposite index is out of range
        return None
    
# Example usage
my_list = [1, 2, 3, 4, 5, 6]

index_to_select = 0
selected_element = opposite_index_select(my_list, index_to_select)

if selected_element is not None:
    print(f"Element at index {index_to_select}: {selected_element}")
else:
    print(f"Invalid index: {index_to_select}")

