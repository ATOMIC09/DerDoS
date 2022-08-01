<h1 align="center">Welcome to DDoS-GUI 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Basics of UDP Attacks with Sockets
<img src ="https://media.discordapp.net/attachments/778868879567880192/1003507956282830888/Screenshot_2022-08-01_104141.png" />

## ❗ Before using

```sh
pip install PyQt5
```

## ❓ How to use ?

Just click `run.py`

## 🤔 How to check if it can attack ?

Check in `Task Manager / Performance / Eternet`.
If the speed of `Send` is increased, it means it can attack.
But you need to make sure the target doesn't have a firewall on.

## 🛡 How to see if the target has Firewall on ?

Just use `ping <target_ip>` in command prompt
(e.g. `ping 25.7.233.218` to check if 25.7.233.218 is online or not)

If the packet loss is 100%, the target has a firewall on and you can't attack him. or even join his game server
<img src ="https://cdn.discordapp.com/attachments/778868879567880192/1003512650929557544/failmc.jpg" />


## 🚀 Example case
You can use the target IP in Hamachi to attack game servers such as Minecraft.

<img src ="https://cdn.discordapp.com/attachments/778868879567880192/1003510356364247070/ddos_test.png" />
