<h1 align="left">Welcome to DerDoS's Source Code 👀</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://github.com/ATOMIC09/DerDoS/tags">
      <img alt="Download" src="https://img.shields.io/github/downloads/ATOMIC09/DerDoS/total" />
  </a>
</p>

> Basics of UDP Attacks with Sockets, Use for educational purposes only.
<img src ="https://github.com/ATOMIC09/DerDoS/assets/66838025/45a09a70-d769-4e89-b328-9fdb44f7fee4" />
<br>
<br>

## ❗ Before using
If you want to use an executable file, go to the `Releases` tab. or click **here**
- [`Download for Windows (v1.1)`](https://github.com/ATOMIC09/DerDoS/releases/download/v1.1/DerDos-1.1-windows-x86_64.exe)
- [`Download for Mac (Intel) (v1.1)`](https://github.com/ATOMIC09/DerDoS/releases/download/v1.1/DerDos-1.1-mac-x86_64.dmg)

<br>

## 🍎 Want to build for macOS yourself ? 
You can use the script in `derdos_builder/build_mac/run_mac_builder.sh`

### Required libraries
- [`pyinstaller`](https://pypi.org/project/pyinstaller/)
- [`appdmg`](https://www.npmjs.com/package/appdmg)

### An example of building the app on macOS 14
https://github.com/ATOMIC09/DerDoS/assets/66838025/3dacbfbd-1db5-42f5-a19d-4d21368227f8

<br>

## ❓ How to use .py version ?
*This section was tested on Windows 11*

Type
```sh
pip install PyQt5
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

<img src ="https://raw.githubusercontent.com/ATOMIC09/DerDoS/main/derdos_builder/asset/example_case.png" />
