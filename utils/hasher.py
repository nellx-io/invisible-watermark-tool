import hashlib

def hash_creator_id(creator_id: str) -> str:
    """
    Hashes the creator ID using SHA-256 for use as an invisible watermark.

    Args:
        creator_id (str): The plain text creator ID from config.

    Returns:
        str: SHA-256 hashed version of the creator ID.
    """
    return hashlib.sha256(creator_id.encode('utf-8')).hexdigest()
