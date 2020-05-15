import optparse
import requests

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_domain", help="Enter a domain")
    options = parse_object.parse_args()[0]

    if not options.target_domain:
        print("You must write a domain")
    
    return options
# Colors
OKGREEN = '\033[92m'
ENDC = '\033[0m'

print(OKGREEN +"SubdomainFinder started to research..."+ENDC)
target_info = user_input()
target = target_info.target_domain
file = open("YOUR_FILE_PATH_HERE\SubdomainFinder\\subdomains.txt") #CHANGE_THIS
c = file.read()
subdomains = c.splitlines()


def find_subdomains(target):
    for subdomain in subdomains:
        url = f"http://{subdomain}.{target}"
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(OKGREEN + "\n[+] Discovered subdomain:", url + ENDC)
            print (OKGREEN + url + "'s status code => "+ str(r.status_code) + ENDC)

            with open("YOUR_FILE_PATH_HERE\discovered.txt","a") as discovered_file: #CHANGE_THIS
                discovered_file.write("\n" + url)
                discovered_file.close()

find_subdomains(target)
print(OKGREEN+"\nGood Luck's ;) My Twitter => @sercan_yilmaz_"+ENDC)
