while True:
    print("\n=== MENU PILIHAN ===")
    print("1. Barisan Fibonacci")
    print("2. M x N")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        n = int(input("Masukkan jumlah suku: "))
        a, b = 0, 1
        print("Barisan Fibonacci:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif pilih == "2":
        m = int(input("Masukkan nilai M: "))
        n = int(input("Masukkan nilai N: "))
        hasil = m * n
        print(f"Hasil {m} x {n} = {hasil}")

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")