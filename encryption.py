from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
print("KEY:", key.decode())

enc_sonar = fernet.encrypt(b"your-sonar-token")
enc_hf = fernet.encrypt(b"your-hf-token")

print("ENC_SONAR:", enc_sonar.decode())
print("ENC_HF:", enc_hf.decode())
