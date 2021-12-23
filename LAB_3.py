import os
import rsa as rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as padding1

settings = {
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
    """генерация пары ключей для асимметричного алгоритма шифрования"""
    keys = rsa.generate_private_key( public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    """сериализация открытого ключа в файл"""
    public_pem = 'public.pem'
    with open(public_pem, mode='wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    settings['public_key'] = public_pem

    """сериализация закрытого ключа в файл"""
    private_pem = 'private.pem'
    with open(private_pem, mode='wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
    settings['secret_key'] = private_pem

    """зашифрование ключа симметричного шифрования открытым ключом"""
    symmetric_key_enc = public_key.encrypt(key, padding1.OAEP(mgf=padding1.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    print('зашифрованный ключ')
    print(symmetric_key_enc)

    """сериализация ключа симмеричного алгоритма в файл"""
    file_name = 'symmetric.txt'
    with open(file_name, mode='wb') as key_file:
        key_file.write(symmetric_key_enc)
    settings['symmetric_key'] = file_name


hybrid_system_key_generation(settings)