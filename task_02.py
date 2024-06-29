from PIL import Image
import numpy as np

# Encrypt_image() to encrypt the image
def encrypt_image(image_path,output_path,key):
    # Opening the image
    with Image.open(image_path) as img:
        img_array = np.array(img)

        # Encrypting image XOR with key
        encrypted_array = img_array ^ key

        # Saving the encrypted image in the output path
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_path)


# Decrypt_image() to decrypt the encrypted image
def decrypt_image(image_path,output_path,key):
    # Opening the encrypted image
    with Image.open(image_path) as img:
        img_array = np.array(img)
        # Decrypting the encrypted image XOR with key
        decrypted_array = img_array ^ key

        # Saving the decrypted image in the output path
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save(output_path)


# Define paths and encryption key
# Change the input image path as per your image path
input_image_path = 'D:\Coding\Python\Prodigy Infotech Tasks\Image.jpg'
encrypted_image_path = 'D:\Coding\Python\Prodigy Infotech Tasks\Encrypted Image.jpg'
decrypted_image_path = 'D:\Coding\Python\Prodigy Infotech Tasks\Decrypted Image.jpg'

# Choose any integer for encryption
encryption_key = 143  

'''
# You can take input for the encryption key from the user
encryption_key = int(input("Enter the encryption key: "))

'''

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)
print(f'Image encrypted and saved to {encrypted_image_path}')

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
print(f'Image decrypted and saved to {decrypted_image_path}')
