### 2. `README_advanced_ssh_brute.md`


# Advanced SSH Security Suite

An optimized multi-functional tool designed for high-performance SSH credential testing.
This version supports **multi-threaded scanning** and **on-the-fly password generation**
to evaluate server resilience against automated attacks.

## Features
* **Single User Mode**: Standard wordlist attack against a specific account.
* **Multi-threaded Mode**: Utilizes `concurrent.futures` to test user/password combinations rapidly.
* **Credential Generator**: Uses `itertools` to generate and test character permutations.
* **Auto-Logging**: Successfully discovered credentials are saved to `success.txt`.

## Installation
```
pip install paramiko
pip install tqdm
