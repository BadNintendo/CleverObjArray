# CleverObjectArray

## Overview

The `CleverObjectArray` class provides an object array that can be indexed and manipulated just like a typical array. This class allows for the addition, deletion, and searching of entries, ensuring efficient handling of data in object format while maintaining index-based sorting when necessary.

## Class Definition

```python
class CleverObjectArray:
    def __init__(self):
        self.data = []
        self.index_map = {}

    def add(self, name=None, value=None):
        index = len(self.data) + 1
        entry = {"index": index, "date": 'dd/mm/yy', "name": name, "value": value}
        self.data.append(entry)
        if name:
            self.index_map[name] = index
        return entry

    def delete(self, name=None, index=None):
        if name:
            index = self.index_map.get(name, None)
            if index is None:
                return f"Error: '{name}' not found."
        if index is None or index > len(self.data):
            return f"Error: Invalid index '{index}'."
        self.data.pop(index - 1)
        return f"Deleted entry with index '{index}'."

    def find_by_index(self, index):
        if index <= len(self.data):
            return self.data[index - 1]
        return f"Error: Invalid index '{index}'."

    def __repr__(self):
        return str(self.data)
```

## Methods

### `__init__`

- Initializes the `CleverObjectArray` class.
- `self.data`: A list to store the object entries.
- `self.index_map`: A dictionary to map names to their respective indexes.

### `add`

- Adds an entry to the object array.
- Parameters:
  - `name` (optional): The name of the entry.
  - `value` (optional): The value of the entry.
- Returns the added entry.

### `delete`

- Deletes an entry from the object array by name or index.
- Parameters:
  - `name` (optional): The name of the entry to delete.
  - `index` (optional): The index of the entry to delete.
- Returns a message indicating the result of the deletion.

### `find_by_index`

- Finds an entry by its index.
- Parameters:
  - `index`: The index of the entry to find.
- Returns the entry if found, or an error message if the index is invalid.

### `__repr__`

- Returns a string representation of the object array.

## Usage Examples

### Adding Entries

```python
obj_arr = CleverObjectArray()
print(obj_arr.add("one", "everything"))  # Add entry with name and value
print(obj_arr.add("two", "nothing"))     # Add another entry
```

### Deleting Entries

```python
print(obj_arr.delete(name="one"))  # Delete entry by name
print(obj_arr.delete(index=2))     # Delete entry by index
```

### Finding Entries

```python
print(obj_arr.find_by_index(1))    # Find entry by index
```

### Displaying All Entries

```python
print(obj_arr)  # Display all entries in the object array
```

## Additional Handling

### Updating Entries

You can extend the class to update entries by name or index.

```python
def update(self, name=None, index=None, value=None):
    if name:
        index = self.index_map.get(name, None)
        if index is None:
            return f"Error: '{name}' not found."
    if index is None or index > len(self.data):
        return f"Error: Invalid index '{index}'."
    self.data[index - 1]['value'] = value
    return self.data[index - 1]
```

Usage:

```python
print(obj_arr.update(name="two", value="something"))  # Update entry by name
print(obj_arr.update(index=1, value="anything"))      # Update entry by index
```

### Searching by Name

You can add a method to search entries by name.

```python
def find_by_name(self, name):
    index = self.index_map.get(name, None)
    if index is None:
        return f"Error: '{name}' not found."
    return self.data[index - 1]
```

Usage:

```python
print(obj_arr.find_by_name("two"))  # Find entry by name
```
