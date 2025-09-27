def login (username, password):
    """
    Simulates a login function that checks if the provided username and password
    match predefined credentials.

    Args:
        username (str): The username to check.
        password (str): The password to check.  
    Returns:
        bool: True if credentials match, False otherwise.
    """
    predefined_username = "admin"
    predefined_password = "password123"
    
    if username == predefined_username and password == predefined_password:
        return True
    else:
        return False