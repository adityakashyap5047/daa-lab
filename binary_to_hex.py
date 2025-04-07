### Function for converting binary to hexadecimal
def binary_to_hex(binary_str):
    """
    Convert a binary string to its hexadecimal representation.

    Args:
        binary_str (str): A string representing a binary number (e.g., '1010').

    Returns:
        str: The hexadecimal representation of the binary number.
    """
    # Convert binary string to integer
    decimal_value = int(binary_str, 2)
    
    # Convert integer to hexadecimal string and remove '0x' prefix
    hex_value = hex(decimal_value)[2:].upper()
    
    return hex_value

if __name__ == "__main__":
    # Example usage
    binary_input = input("Enter a binary number: ")
    hex_output = binary_to_hex(binary_input)
    print(f"Hexadecimal representation: {hex_output}")