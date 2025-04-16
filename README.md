<h1 align="left">Welcome to DerDoS's Source Code 👀</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.2-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: GPLv3" src="https://img.shields.io/badge/License-GPLv3-yellow.svg" />
  </a>
  <a href="https://github.com/ATOMIC09/DerDoS/tags">
      <img alt="Download" src="https://img.shields.io/github/downloads/ATOMIC09/DerDoS/total" />
  </a>
</p>

> Basics of UDP Attacks with Sockets, Use for educational purposes only.
<img src ="https://github.com/user-attachments/assets/8aa32acc-4422-448f-9ee8-c30d17ff4993" />
<br>
<br>

## ❗ Before using
If you want to use an executable file, go to the `Releases` tab. or click **here**
- [`Download for Windows (v1.2)`](https://github.com/ATOMIC09/DerDoS/releases/download/v1.2/DerDos-1.2-windows-x86_64.exe)
- [`Download for Mac (Intel) (v1.2)`](https://github.com/ATOMIC09/DerDoS/releases/download/v1.2/DerDos-1.2-mac-x86_64.dmg)
- [`Download for Mac (Apple Silicon) (v1.1)`](https://github.com/ATOMIC09/DerDoS/releases/download/v1.1/DerDos-1.1-mac-arm64.dmg)

<br>

## 🍎 Want to build for macOS yourself ? 
You can use the script in `derdos_builder/build_mac/run_mac_builder.sh` (Make sure you are running the script within `derdos_builder/build_mac/`)

### Required libraries
- Pyinstaller *(Python 3 required)*
- PyQt6 *(Python 3 required)*
- appdmg *(NodeJs required)*

(`run_mac_builder.sh` will install these automatically)

### An example of building the app on macOS 14
https://github.com/ATOMIC09/DerDoS/assets/66838025/3dacbfbd-1db5-42f5-a19d-4d21368227f8

<br>

## 🪟 Want to build for Windows yourself ? 
You can use the script in `derdos_builder/build_mac/run_windows_builder.sh` (Make sure you are running the script within `derdos_builder/build_windows/`)

### Required libraries
- PyQt6 *(Python 3 required)*
- Nuitka *(Python 3 required)*

(`run_windows_builder.bat` will install these automatically)

### An example of building the app on Windows 11
https://github.com/ATOMIC09/DerDoS/assets/66838025/0dccc110-1c75-4078-8783-ac846aab90ea

<br>

## ❓ How to use .py version ?
*This section was tested on Windows 11*

Type
```sh
pip install PyQt6
```
in `Command Prompt` or `PowerShell` to install the library that needed to show the GUI

(If you got '`...`' is not recognized as an internal or external command. It means that `...` program is not in your environment PATH)

Then run `main.py`

<br>

## 🤔 How to check if it can attack ?

Check-in `Task Manager > Performance > Ethernet`.
If the speed of `Send` is increased, it means it can attack.
But you need to make sure the target doesn't have a firewall on.

<br>

## 🛡 How to see if the target has a Firewall on ?

Just use `ping <target_ip>` in command prompt
(e.g. `ping 25.7.233.218` to check if 25.7.233.218 is online or not)
If the packet loss is 100%, the target has a firewall on and you can't attack. or even join the game server

<img src ="https://raw.githubusercontent.com/ATOMIC09/DerDoS/main/derdos_builder/asset/mc_firewall_on.jpg" />
<br>

## 🚀 Example case
You can use the target IP in Hamachi to attack game servers such as Minecraft.

<img src ="https://github.com/user-attachments/assets/00da0874-3276-409f-bf6c-1e1a406473ac" />
