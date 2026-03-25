from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    # Khởi tạo tham số DH với key_size là 2048 bits
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    # Tạo khóa bí mật (private key) từ tham số
    private_key = parameters.generate_private_key()
    # Trích xuất khóa công khai (public key) từ khóa bí mật
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # 1. Tạo tham số chung
    parameters = generate_dh_parameters()
    
    # 2. Tạo cặp khóa cho Server
    private_key, public_key = generate_server_key_pair(parameters)

    # 3. Xuất khóa công khai ra file .pem để gửi cho Client
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

if __name__ == "__main__":
    main()