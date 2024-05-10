import time
import colorama
from colorama import init, Fore, Style
import webbrowser

init(autoreset=True)

def print_eagle_frame():
    print(f"{Fore.YELLOW}{Style.BRIGHT}   \\***********()()()()8888888888********{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}   -\\888888 888888 88    88     888     88  8888         8888   88     8888")
    print(f"{Fore.YELLOW}{Style.BRIGHT}  --<88   88     88    88    88 88   88  88  88       88 88  8 88     88")
    print(f"{Fore.RED}{Style.BRIGHT}   /88   888888 88    88   88  88  88  88888888     88    88   88    88")
    print(f"{Fore.RED}{Style.BRIGHT}  /88       88 88    88  88   88 88  88      88   88           88   88")
    print(f"{Fore.GREEN}{Style.BRIGHT} <88   888888 88888888 88    8888  88        88 888            88 8888")
    print(f"{Fore.BLUE}{Style.BRIGHT}  \\66***[&][&][&][&][&][&]<{Style.RESET_ALL}BY JONATHAN NYAWARA{Fore.BLUE}{Style.BRIGHT}>[&][&][&][&][&][&]***99")
    print(f"{Fore.BLUE}{Style.BRIGHT}   \\")
    print(f"{Fore.BLUE}{Style.BRIGHT}    >{Style.RESET_ALL}")

def animate_eagle(duration, wings_flap_interval):
    start_time = time.time()
    while time.time() - start_time < duration:
        print_eagle_frame()
        time.sleep(wings_flap_interval)
        print("\033[H\033[J")  # Clear terminal screen for the next frame

if __name__ == "__main__":
    duration = 10  # total duration of animation in seconds
    wings_flap_interval = 0.5  # time interval between wing flaps in seconds

    animate_eagle(duration, wings_flap_interval)

# Input Target
search = input("Hostname/IP/Website:")
# Open Web-Page By From Censys/DNSTrails Input Search-Engine
url = f"https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q={search}"
url2 = f"https://securitytrails.com/domain/{search}"
url3 = f"https://shodan.io/domain/{search}"
url4 = f"https://zoomeye.org/domain/{search}"
url5 = f"https://greynoise.io//domain/{search}"
url6 = f"https://flowgpt.com/chat//domain/{search}"
url7 = f"https://hunter.io//domain/{search}"
# Function To Open The Pages In The Browser
webbrowser.open(url, new=1)
webbrowser.open(url2, new=2)
webbrowser.open(url3, new=3)
webbrowser.open(url4, new=4)
webbrowser.open(url5, new=5)
webbrowser.open(url6, new=6)
webbrowser.open(url7, new=7)
