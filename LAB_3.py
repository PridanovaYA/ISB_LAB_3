import os

settings= {
    'initial_file':'path/to/inital/file.txt',
    'encrypted_file':'path/to/encrypted/file.txt',
    'decrypted_file':'path/to/decrypted/file.txt',
    'symmetric_key':'path/to/symmetric/key.txt',
    'public_key':'path/to/public/key.pem',
    'secret_key':'path/to/secret/key.pem',
}

def hybrid_system_key_generation(settings: dict)->None:
    """генерация ключа симметричного алгоритма шифрования"""
    key = os.urandom(16)
    print('ключ')
    print(key)

hybrid_system_key_generation(settings)