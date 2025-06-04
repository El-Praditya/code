import zipfile

def brute_force(zip_path, wordlist):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print("[!] File ZIP tidak ditemukan.")
        return

    with open(wordlist, "r") as file:
        for line in file:
            password = line.strip()
            try:
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"[✓] Password ditemukan: {password}")
                return
            except:
                print(f"[x] Salah: {password}")
    
    print("[-] Gagal menemukan password yang cocok.")

# Jalankan brute force
brute_force("target.zip", "wordlist.txt")
