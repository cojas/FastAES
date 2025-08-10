class DecryptionError(Exception):
    """
    Decryption error
    """
    content: bytes

    def __init__(self, content: bytes) -> None: ...

    def __str__(self) -> str: ...


class FastAES:
    """
    Fast AES implementation
    """
    salt: bytes

    def __init__(self) -> None: ...

    def set_key(self, seed: bytes) -> None:
        """
        Generate AES key based on random seed
        """
        ...

    def encrypt(self, content: bytes) -> bytes:
        """
        Encrypt content
        """
        ...

    def decrypt(self, content: bytes) -> bytes:
        """
        Decrypt content
        """
        ...
