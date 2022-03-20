#!/usr/bin/python

from threading import Thread
from rich import print
from rich.progress import track
import requests, sys, getopt

class ResolveSubdomains(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        count = 0
        print("[cyan] ___      _    ___                 _           ___ _         _\n/ __|_  _| |__|   \ ___ _ __  __ _(_)_ _  ___ | __(_)_ _  __| |___ _ _ \n\__ \ || | '_ \ |) / _ \ '  \/ _` | | ' \(_-< | _|| | ' \/ _` / -_) '_|\n|___/\_,_|_.__/___/\___/_|_|_\__,_|_|_||_/__/ |_| |_|_||_\__,_\___|_|\n\n _____         _\n|_   _|__  ___| |\n  | |/ _ \/ _ \ |\n  |_|\___/\___/_| By Dox-Dev (https://github.com/dox-dev[cyan])\n\n")

        for i in track(lines):
            request_url = 'https://' + i.strip() + '.' + url
            try:
                request = requests.get(request_url)
                if request.status_code == 200:
                    print("{} resolves with success! [green]✔".format(request_url))
                    count += 1
                    do_step(i)
            except:
                pass
        print("\n{} Subdomains Found\n".format(count))


if __name__ == "__main__":
    cli_arguments = sys.argv
    if len(cli_arguments) != 2:
        print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")
        sys.exit(2)

    argument_list = cli_arguments[1:]
    short_args = "hu:"
    long_args = ["help", "url="]

    try:
        arguments, values = getopt.getopt(argument_list, short_args, long_args)
    except:
        print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print("\n[bold]Usage:[/bold] python main.py --url=\"Destinated_URL\"\n")

        elif current_argument in ("-u", "--url"):
            url = str(current_value)
            file = open('subdomains.txt', 'r')
            lines = file.readlines()

            thread = ResolveSubdomains()
            thread.start()
            thread.join()