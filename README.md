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

> Basics of UDP Attacks with Sockets
<img src ="https://github.com/ATOMIC09/DerDoS/assets/66838025/45a09a70-d769-4e89-b328-9fdb44f7fee4" />

## ❗ Before using
If you want to use an executable file, go to the `Releases` tab. or click **here**
- [Download for Windows (v1.1)](https://github.com/ATOMIC09/DerDoS/releases/download/v1.1/DerDos-1.1-windows-x86_64.exe)
- [Download for Mac (Intel) (v1.0)](https://github.com/ATOMIC09/DerDoS/releases/download/V1.0/DerDos-1.0-mac-x86_64.dmg)

But if you want to try .py version

Type
```sh
pip install PyQt5
```
in `Command Prompt` or `PowerShell` to install the library that needed to show the GUI

## ❓ How to use .py version ?
Just run `main.py`

## 🤔 How to check if it can attack ?

Check-in `Task Manager > Performance > Ethernet`.
If the speed of `Send` is increased, it means it can attack.
But you need to make sure the target doesn't have a firewall on.

## 🛡 How to see if the target has a Firewall on ?

Just use `ping <target_ip>` in command prompt
(e.g. `ping 25.7.233.218` to check if 25.7.233.218 is online or not)
If the packet loss is 100%, the target has a firewall on and you can't attack. or even join the game server

<img src ="https://raw.githubusercontent.com/ATOMIC09/DerDoS/main/pyinstaller/asset/mc_firewall_on.jpg" />


## 🚀 Example case
You can use the target IP in Hamachi to attack game servers such as Minecraft.

<img src ="https://raw.githubusercontent.com/ATOMIC09/DerDoS/main/pyinstaller/asset/example_case.png" />
