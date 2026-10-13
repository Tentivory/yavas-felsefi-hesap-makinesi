#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yavaş Felsefi Hesap Makinesi
Her işlem için varoluşsal sorgulama yapar.
"""

import time
import random
import sys

# Gizli mesaj: Bürokrasi bazen yavaşlatır ama felsefe hızlandırır. (saklı siyasi gönderme)
felsefi_sorular = [
    "Neden bu sayıyı seçtin? Varoluşsal bir anlamı var mı?",
    "Toplama işlemi gerçekten gerekli mi, yoksa sadece alışkanlık mı?",
    "Bu sonucun evrendeki yeri nedir?",
    "Eğer bu işlemi yapmasaydık, zaman akışı değişir miydi?",
    "Sıfır nedir? Yokluk mu, yoksa potansiyel mi?"
]

def yavas_hesapla(a, b, islem):
    print(f"\nHesaplama başlıyor: {a} {islem} {b}")
    print("Felsefi analiz yapılıyor...")
    
    for i in range(3):
        print(f"  {random.choice(felsefi_sorular)}")
        time.sleep(random.uniform(1.5, 3.0))  # Yavaş olsun
    
    if islem == '+':
        sonuc = a + b
    elif islem == '-':
        sonuc = a - b
    elif islem == '*':
        sonuc = a * b
    elif islem == '/':
        if b == 0:
            print("Sıfıra bölmek... Bu bir varoluşsal kriz!")
            return None
        sonuc = a / b
    else:
        print("Bilinmeyen işlem. Belki de işlem yapmamak en felsefi çözüm.")
        return None
    
    print(f"\nSonuç: {sonuc}")
    print("Bu sonuç seni tatmin etti mi? Yoksa daha derin anlamlar mı arıyorsun?")
    return sonuc

def main():
    print("=== YAVAŞ FELSEFİ HESAP MAKİNESİ ===")
    print("Basit işlemler için bile sabır gerekir. Hazır mısın?\n")
    
    try:
        a = float(input("İlk sayı: "))
        islem = input("İşlem (+, -, *, /): ").strip()
        b = float(input("İkinci sayı: "))
        
        yavas_hesapla(a, b, islem)
    except ValueError:
        print("Sayı girmen gerekiyordu. Felsefe bile sayıları sever.")
    except KeyboardInterrupt:
        print("\n\nHesaplama iptal edildi. Belki de hiç hesap yapmamak en iyisiydi.")

if __name__ == "__main__":
    main()
