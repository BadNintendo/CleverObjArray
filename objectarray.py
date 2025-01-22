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

# Usage example
obj_arr = CleverObjectArray()
print(obj_arr.add("one", "everything"))  # Add entry
print(obj_arr.add("two", "nothing"))     # Add entry
print(obj_arr.find_by_index(1))          # Find by index
print(obj_arr.delete(name="one"))        # Delete by name
print(obj_arr)                           # Display all entries
