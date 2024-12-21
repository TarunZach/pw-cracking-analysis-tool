import hashlib

# creating rainbow table
def generate_rainbow_table_from_file(input_file, output_file, hash_function):
    unique_passwords = set()

    # sorting the password
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

#******************* cracking part ****************
# load the rainbow table from a file
def load_rainbow_table(rainbow_table_file):
    rainbow_table = {} 
    with open(rainbow_table_file, 'r') as file:
        for line in file:
            password, hashed = line.strip().split(':')  # Split the password and hash
            rainbow_table[hashed] = password  # Store the hash as the key and password as the value
    return rainbow_table

# crack target hashes using the rainbow table
def crack_hashes(hashes_file, rainbow_table, output_file):
    with open(hashes_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            target_hash = line.strip()  # Remove any spaces or newlines
            if target_hash in rainbow_table:  # Check if the hash exists in the rainbow table
                password = rainbow_table[target_hash]
                outfile.write(f"{target_hash}:{password}\n")
                print(f"Hash {target_hash} cracked → Password: {password}")
            else:
                outfile.write(f"{target_hash}:NOT FOUND\n")
                print("Hash not found in the table.")


# main for creating rainbow table
input_file= "input_passwords.txt" 
rainbow_table_file= "rainbow_table_file.txt"  
hash_function = hashlib.md5 

generate_rainbow_table_from_file(input_file, rainbow_table_file, hash_function)

# main for cracking part
hashes_file = "target_hashes.txt"  # target hashes
output_file = "cracked_hashes.txt"  # results

rainbow_table = load_rainbow_table(rainbow_table_file)  # Load the rainbow table into a dictionary
crack_hashes(hashes_file, rainbow_table, output_file)  # Crack and save the results
