import requests

target = input("Enter target: ")
file = open("YOUR FILE PATH\subdomains.txt")
c = file.read()
subdomains = c.splitlines()

# Colors
OKGREEN = '\033[92m'
ENDC = '\033[0m'

for subdomain in subdomains:
    url = f"http://{subdomain}.{target}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(OKGREEN + "[+] Discovered subdomain:", url + ENDC)
