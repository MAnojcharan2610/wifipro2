Wifite
======

This repo is a complete re-write of [`wifite`](https://github.com/derv82/wifite), a Python script for auditing wireless networks.

Wifite runs existing wireless-auditing tools for you. Stop memorizing command arguments & switches!

Wifite is designed to use all known methods for retrieving the password of a wireless access point (router).  These methods include:
1. WPS: The [Offline Pixie-Dust attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack)
1. WPS: The [Online Brute-Force PIN attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Online_brute-force_attack)
2. WPA: The [WPA Handshake Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
3. WPA: The [PMKID Hash Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
4. WEP: Various known attacks against WEP, including *fragmentation*, *chop-chop*, *aireplay*, etc.

Run wifite, select your targets, and Wifite will automatically start trying to capture or crack the password.
