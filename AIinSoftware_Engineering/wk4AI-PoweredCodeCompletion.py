#The AI Suggested code 

def sort_dict_list(dict_list, sort_key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): Key in the dictionaries to sort by.
        reverse (bool): If True, sort in descending order. Default is False.

    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        # Sort the list using the specified key
        sorted_list = sorted(dict_list, key=lambda x: x[sort_key], reverse=reverse)
        return sorted_list
    except KeyError:
        print(f"Error: Key '{sort_key}' not found in one or more dictionaries.")
        return dict_list

# Example usage:
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort by 'age'
sorted_data = sort_dict_list(data, "age")
print(sorted_data)



def sort_dict_list(dict_list, sort_key):
sorted_data = sort_dict_list(data, "age")
print(sorted_data)

#my code 

def sort_dict_list(dict_list, sort_key, reverse=False):
    return sorted(dict_list, key=lambda x: x[sort_key], reverse=reverse)

"""
Both versions run at the same speed
Use the docstring version in production or collaborative projects.
Use the minimal version for quick scripts, personal projects, or coding challenges. 
