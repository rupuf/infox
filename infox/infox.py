#!/usr/bin/env python3
import os, requests, phonenumbers
from phonenumbers import geocoder, carrier, timezone

def banner():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, "logo.txt"), "r", encoding="utf-8") as f:
        print(f.read())

def phone_info():
    number = input("\nEnter phone number with country code (e.g. +919876543210): ").strip()
    try:
        parsed = phonenumbers.parse(number, None)
        print("\n[+] Valid Number:", phonenumbers.is_valid_number(parsed))
        print("[+] Location:", geocoder.description_for_number(parsed, "en"))
        print("[+] Carrier:", carrier.name_for_number(parsed, "en"))
        print("[+] Time Zone:", timezone.time_zones_for_number(parsed))
    except Exception:
        print("[-] Invalid Number!")

def ip_info():
    ip = input("\nEnter IP (or press Enter for your IP): ").strip() or ""
    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url, timeout=10).json()
        if data.get("status") == "success":
            print("\n[+] IP:", data.get("query"))
            print("[+] ISP:", data.get("isp"))
            print("[+] Country:", data.get("country"))
            print("[+] Region:", data.get("regionName"))
            print("[+] City:", data.get("city"))
            print("[+] Lat, Lon:", data.get("lat"), ",", data.get("lon"))
            print("[+] Timezone:", data.get("timezone"))
        else:
            print("[-] Invalid IP or API error!")
    except Exception:
        print("[-] Network error!")

def menu():
    while True:
        banner()
        print("[1] Phone Number Info")
        print("[2] IP Finder")
        print("[x] Exit")
        choice = input("Choose option: ").strip().lower()
        if choice == "1": phone_info()
        elif choice == "2": ip_info()
        elif choice == "x":
            print("Exiting..."); break
        else: print("Invalid choice!")

if __name__ == "__main__":
    menu()
