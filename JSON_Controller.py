import json

class JSONSearcher:
    def __init__(self, json_file):
        try:
            with open(json_file, 'r') as file:
                json_string = file.read()
            self.data = json.loads(json_string)
        except FileNotFoundError:
            print("The specified JSON file was not found.")
            self.data = {}
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            self.data = {}

    def search_field(self, target_key):
        result = self._search_recursive(self.data, target_key)
        return result

    def _search_recursive(self, current_data, target_key):
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                # Check for matching key
                if key == target_key:
                    field_name = value.get('field_name')
                    waiting_time = value.get('waiting_time')
                    return field_name, waiting_time
                
                # Check for 'sub_menu' and search within it if it exists
                if isinstance(value, dict) and 'sub_menu' in value:
                    result = self._search_recursive(value['sub_menu'], target_key)
                    if result:
                        return result
                    
                # Check if the value itself is a dict and search in that
                if isinstance(value, dict):
                    result = self._search_recursive(value, target_key)
                    if result:
                        return result
        
        return None  # Return None if the key is not found
    

