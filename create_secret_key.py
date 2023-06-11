import os

def create_key():
    return os.urandom(24).hex()


if __name__ == '__main__':
    print(create_key())