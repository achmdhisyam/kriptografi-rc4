# algoritma Key Scheduling
def ksa(key_bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

#pseudo random generation algorithm
def prga(S, text_length):
    i = 0
    j = 0
    keystream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystream.append(k)
    return keystream

def enkripsi(plaintext, key):
    pt_bytes = [ord(char) for char in plaintext]
    key_bytes = [ord(char) for char in key]
    S = ksa(key_bytes)
    keystream = prga(S, len(pt_bytes))
    ciphertext_bytes = [p ^ k for p, k in zip(pt_bytes, keystream)]
    return ''.join(f'{b:02x}' for b in ciphertext_bytes)

def dekripsi(ciphertext_hex, key):
    ct_bytes = [int(ciphertext_hex[i:i+2], 16) for i in range(0, len(ciphertext_hex), 2)]
    key_bytes = [ord(char) for char in key]
    S = ksa(key_bytes)
    keystream = prga(S, len(ct_bytes))
    plaintext_bytes = [c ^ k for c, k in zip(ct_bytes, keystream)]
    return ''.join(chr(b) for b in plaintext_bytes)

if __name__ == "__main__":
    print("APLIKASI KRIPTOGRAFI")
    print("1. Enkripsi (Teks jadi Kode Sandi)")
    print("2. Dekripsi (Kode Sandi menjadu Teks)")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        teks_asli = input("\nMasukkan Teks Asli (Plaintext): ")
        kunci = input("Masukkan Kunci (Key): ")
        
        hasil_enkripsi = enkripsi(teks_asli, kunci)
        print(f"Hasil Enkripsi (Hex): {hasil_enkripsi}")
        
    elif pilihan == "2":
        teks_sandi = input("\nMasukkan Kode Sandi (Hex): ")
        kunci = input("Masukkan Kunci (Key): ")
        
        try:
            hasil_dekripsi = dekripsi(teks_sandi, kunci)
            print(f"Hasil Dekripsi (Teks): {hasil_dekripsi}")
        except ValueError:
            print("\nError: Format kode sandi Hex tidak valid!")
            
    else:
        print("\nPilihan menu tidak tersedia!")