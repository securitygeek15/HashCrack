import hashlib


def hash_cracker(hash_to_crack, dictionary):
    for word in dictionary:
        word = word.strip()
        md5_hash = hashlib.md5(word.encode()).hexdigest()
        sha1_hash = hashlib.sha1(word.encode()).hexdigest()
        sha256_hash = hashlib.sha256(word.encode()).hexdigest()
        sha512_hash = hashlib.sha512(word.encode()).hexdigest()
        sha3_256_hash = hashlib.sha3_256(word.encode()).hexdigest()
        sha3_512_hash = hashlib.sha3_512(word.encode()).hexdigest()
        blake2b_hash = hashlib.blake2b(word.encode()).hexdigest()
        blake2s_hash = hashlib.blake2s(word.encode()).hexdigest()

        if (md5_hash == hash_to_crack or sha1_hash == hash_to_crack or
                sha256_hash == hash_to_crack or sha512_hash == hash_to_crack or
                sha3_256_hash == hash_to_crack or sha3_512_hash == hash_to_crack or
                blake2b_hash == hash_to_crack or blake2s_hash == hash_to_crack):
            print("Found match!")
            print("Plaintext:", word)
            return

    print("Hash not found in dictionary.")


def main():
    hash_to_crack = input("Enter the hash to crack: ").strip()
    dictionary_path = input("Enter the path to the dictionary file: ").strip()

    with open(dictionary_path, "r") as file:
        dictionary = file.readlines()

    hash_cracker(hash_to_crack, dictionary)


if __name__ == "__main__":
    main()
