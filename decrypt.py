from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

with open("private_key.pem", "rb") as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None
    )

with open("encrypted_message.bin", "rb") as file:
    ciphertext = file.read()

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:")
print(plaintext.decode("utf-8"))






