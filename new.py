def process_image(path, key, mode='encrypt'):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())
        
        for index, value in enumerate(image):
            if mode == 'encrypt':
                image[index] = value ^ key
            elif mode == 'decrypt':
                image[index] = value ^ key
        
        if mode == 'encrypt':
            new_path = path[:-4] + "_encrypted" + path[-4:]
        elif mode == 'decrypt':
            new_path = path[:-4] + "_decrypted" + path[-4:]
        
        with open(new_path, 'wb') as fout:
            fout.write(image)

        if mode == 'encrypt':
            print('Encryption Done. Encrypted image saved as:', new_path)
        elif mode == 'decrypt':
            print('Decryption Done. Decrypted image saved as:', new_path)
    
    except FileNotFoundError:
        print("File not found:", path)
    except PermissionError:
        print("Permission denied:", path)
    except Exception as e:
        print('Error:', str(e))


if __name__ == "__main__":
    try:
        path = input(r'Enter path of Image : ')
        key = int(input('Enter Key for encryption/decryption of Image : '))
        
        print('The path of file:', path)
        print('Key:', key)
        
        mode = input("Enter 'encrypt' or 'decrypt' mode: ").lower()
        
        if mode not in ['encrypt', 'decrypt']:
            raise ValueError("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        
        process_image(path, key, mode)

    except ValueError as ve:
        print(ve)
