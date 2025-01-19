import os

def validate_api_key(api_key: str) -> bool:
    """
    Validate the provided API key format.

    Args:
        api_key (str): The API key to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return api_key and len(api_key) > 20

def load_config(file_path: str) -> dict:
    """
    Load configuration from a file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: The loaded configuration.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file {file_path} not found.")
    with open(file_path, 'r') as file:
        return json.load(file)
