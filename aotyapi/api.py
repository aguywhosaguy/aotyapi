from client import AOTYClient
import time
import json
from bs4 import BeautifulSoup


def main():
    client = AOTYClient()
    return client.critic_year_list(1995)



"""
def main(pages: int = 100):
    file = open("critics.json", "a")     
    file.write("    ALL = 0")
    client = AOTYClient()

    for i in range(1, pages + 1):
        publisher = client.get_critic(i)

        if publisher:
            publisher = publisher.replace(" ", "_")
            publisher = publisher.replace(".", "")
            file.write(f"\n    {publisher.upper()} = {i}")

    file.close()
"""

if __name__ == "__main__":
   print(main())
