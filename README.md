<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/akshith98/HoneyTel">
  </a>

  <h3 align="center">Honeytel</h3>

 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


HonyTel is a honeypot and monitering tool. HonyTel opens "trigger" ports on the host         
that an attacker would connect to. HonyTel for now only has a telnet honeypot. This            
honeypot can log attacker commands and moniter potential port scans. 


### Built With

* [Python3]()




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.




### Prerequisites

Python3 

### Supported OS

Linux

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/akshith98/HoneyTel.git
   ```
   
2. Create a ```/opt/honeytel/tel.log ``` file on your server



<!-- USAGE EXAMPLES -->
## Usage

Run Program As Administrator
   ```sh
   sudo python3 honeytal.py
   ```
Output (default ports):

```
$ sudo python3 honeytel.py

 [*] UDP serving at Port: 123
 [*] UDP serving at Port: 5060
 [*] UDP serving at Port: 5061
 [*] UDP serving at Port: 3478


 [*] TCP serving at Port: 22
 [*] TCP serving at Port: 1433
 [*] TCP serving at Port: 8080
 [*] TCP serving at Port: 21
 [*] TCP serving at Port: 5060
 [*] TCP serving at Port: 5061
 [*] TCP serving at Port: 5900
 [*] TCP serving at Port: 25
 [*] TCP serving at Port: 110
 [*] TCP serving at Port: 1723
 [*] TCP serving at Port: 1337
 [*] TCP serving at Port: 10000
 [*] TCP serving at Port: 5800
 [*] TCP serving at Port: 44443
 [*] TCP serving at Port: 16993
 [*] TCP serving at Port: 23
 
honeypot has been visited by 10.0.0.34
```

Attacker Input:

```
$ telnet 10.0.0.34
Trying 10.0.0.34...
Connected to 10.0.0.34.
Escape character is '^]'.
Username: Password: root
OK
Telnet>end
ERROR : Unrecognized command
Telnet>logout
Connection closed by foreign host.

```

Log file ```/opt/honeytel/tel.log``` output:

```
06/05/2021 17:26:55.913 [173919] INFO: - 0.0.0.0:23 socket started..
06/05/2021 17:27:09.640 [173919] INFO: - 10.0.0.34:54712 connected to proxy socket
06/05/2021 17:27:09.640 [173919] INFO: - <built-in function id> - 10.0.0.34:54712 client username entered :  !"'# 
06/05/2021 17:27:16.564 [173919] INFO: - <built-in function id> - 10.0.0.34:54712 client password entered : root
 
06/05/2021 17:27:24.100 [173919] INFO: - <built-in function id> - 10.0.0.34:54712 client command entered : end
 
06/05/2021 17:27:28.459 [173919] INFO: - <built-in function id> - 10.0.0.34:54712 client command entered : logout
 
06/05/2021 17:27:28.459 [173919] INFO: - 10.0.0.34:54712 disconnected
```

Exit Program: Ctr-C to end porgram and close all ports



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/akshith98/HoneyTel](https://github.com/akshith98/HoneyTel)








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[image]: https://github.com/akshith98/SC-clone/blob/main/Usage-Image.png

