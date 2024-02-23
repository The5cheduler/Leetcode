class TimeMap:
    def __init__(self):
        """
        Initialize an empty dictionary to store key-value pairs.
        """
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Add a new key-value pair to the store.

        Args:
            key (str): The key for the value.
            value (str): The value to be stored.
            timestamp (int): The timestamp associated with the value.

        Returns:
            None
        """
        if key not in self.store:
            # Create an empty list for the key if it doesn't exist
            self.store[key] = []
        # Append the new value with its timestamp to the list
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve the value associated with the key at the given timestamp.

        Args:
            key (str): The key for the value.
            timestamp (int): The timestamp to search for.

        Returns:
            str: The value associated with the key at the given timestamp, or an empty string if no value exists.
        """
        values = self.store.get(key, [])
        # Get the list of values for the given key, or an empty list if key doesn't exist 

        if not values:
            return ""  # If no values exist for the key, return an empty string

        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1  # Move the left pointer to the right
            else:
                right = mid - 1  # Move the right pointer to the left

        return values[right][1] if right >= 0 else ""
        # Return the value at the right pointer index, or an empty string if right pointer is negative
