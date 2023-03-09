import requests
import json
import re
from typing import List
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import asyncio
import aiohttp

def print_banner():
    print("""
     
     
     
     ⣷⣄⣸⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠋⠉⠀⠀⠀⣿⡇⢀⡴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣎⠙⠦⣀⠀⠀⣠⠀⠀⢀⣆⠀⠀⣠⠖⢉⣼⠏⠀⠀⠀⠀⠀⣿⠗⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡿⠛⠛⠛⠛⠶⠶⠛⠉⠻⣿⡀⠀⢸⡿⠋⠉⠳⠶⠞⠋⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀
⠀    ⠀⠀⠀⠘⣿⣿⣷oggun⠀⠀⠀⠀⢿⡇⠀⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⣀⡀⠘⣇⠀⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⢠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣤⣀⣀⣠⡤⢾⣇⡀⠀⠀⠀⢿⣿⣿⣿⠶⣤⣀⣀⣠⣴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣄⠀⠉⠛⡆⠀⠀⢸⡟⠛⠁⢀⣼⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⡉⠉⠘⣧⡳⣄⣀⣙⠲⠶⠞⢁⣀⡴⣫⡾⠈⠋⣰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡄⠀⢷⠹⣶⠯⣭⣍⣉⣭⡭⢷⣼⢡⠇⠀⣰⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡀⠈⢧⣝⣀⣀⣀⣀⣀⣀⣘⣡⠞⠀⢸⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⣀⣬⣭⣭⣭⣭⣭⣄⡀⠀⠀⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⡀⠀⢀⣀⠀⠀⢀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     
     
     
                          by Tadash10                                                    
    """)

def menu():
    print("Select an option:")
    print("1. Check API status")
    print("2. Check for SQL injection vulnerability")
    print("3. Check for cross-site scripting (XSS) vulnerability")
    print("4. Check for broken access control")
    print("5. Check for insecure deserialization")
    print("0. Exit")

def check_api_status(api_url: str, headers: dict) -> None:
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    with session.get(api_url, headers=headers) as response:
        if response.ok:
            print("API is up and running.")
        else:
            print("API is down.")

async def check_sql_injection(api_url: str, headers: dict) -> None:
    sql_injection_payloads = ["' OR 1=1;--", "'; DROP TABLE users;--"]
    async with aiohttp.ClientSession() as session:
        for payload in sql_injection_payloads:
            async with session.get(api_url + f"?q={payload}", headers=headers) as response:
                if "error" in await response.text():
                    print(f"SQL injection vulnerability detected with payload: {payload}")

def check_xss_vulnerability(api_url: str, headers: dict) -> None:
    xss_payloads = ["<script>alert('XSS')</script>", "<img src='invalid-image' onerror=alert('XSS')>"]
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    for payload in xss_payloads:
        with session.get(api_url + f"?q={payload}", headers=headers) as response
