import hashlib

# function for creating rainbow table
def generate_rainbow_table_from_file(input_file, output_file, hash_function):
    unique_passwords = set()  # for deleting the duplicate password

    # reading the password file for sorting the password
    with open(input_file, 'r') as infile:
        for line in infile:
            password = line.strip()  #delete space 
            if password:  # chech if the next line is empty 
                unique_passwords.add(password)

    # write hashed password to seperate file 
    with open(output_file, 'w') as outfile:
        for password in unique_passwords:
            hashed = hash_function(password.encode()).hexdigest()
            outfile.write(f"{password}:{hashed}\n")

# main
input_file = "input_passwords.txt" 
output_file = "rainbow_table_file.txt"  
hash_function = hashlib.md5 

generate_rainbow_table_from_file(input_file, output_file, hash_function)