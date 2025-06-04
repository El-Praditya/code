# Jika mengalami kesulitan, temui aku di medium 
# https://medium.com/@leerlryzck9/bypassing-rar-passwords-using-brute-force-method-4a6ada33f6c5

import rarfile

def brute_force_rar(rar_path, wordlist_path):
    try:
        rf = rarfile.RarFile(rar_path)
    except FileNotFoundError:
        print("[!] File RAR tidak ditemukan.")
        return
    except rarfile.BadRarFile:
        print("[!] File bukan RAR atau rusak.")
        return

    with open(wordlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            try:
                rf.extractall(pwd=password)
                print(f"[✓] Password ditemukan: {password}")
                return
            except rarfile.BadRarFile:
                print(f"[x] Salah: {password}")
            except Exception as e:
                print(f"[!] Error: {e}")
    
    print("[-] Gagal menemukan password.")

brute_force_rar("Secret.rar", "pass.txt") #edit yang ini
