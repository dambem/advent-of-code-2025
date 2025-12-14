def read_file(file_path:str, suffix:str='X') -> list[str]:
    """
    Reads a string file_path and return a list of str per new line. Suffix enforced.
    
    Args:
        file_path (str): local element filepath 
        suffix (str): string to append each file.
    Returns:
        list[str]: list of strings containing file contents.
    """
    with open(f'input/{file_path}', 'r') as file:
        return file.readlines()