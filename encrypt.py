from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

with open("public_key.pem", "rb") as file:
    public_key = serialization.load_pem_public_key(
        file.read()
    )

message = input("Enter the message: ")
ciphertext = public_key.encrypt(
    message.encode("utf-8"),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("encrypted_message.bin", "wb") as file:
    file.write(ciphertext)

print("Message successfully encrypted.")
print("Output: encrypted_message.bin")

