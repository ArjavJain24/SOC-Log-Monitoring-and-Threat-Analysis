import re
from collections import Counter

LOG_FILE = "../logs/sample_auth.log"

failed_logins = []
ip_addresses = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins.append(line)
            ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
            if ip:
                ip_addresses.append(ip[0])

print("Total Failed Login Attempts:", len(failed_logins))

ip_count = Counter(ip_addresses)
print("\nTop Suspicious IPs:")
for ip, count in ip_count.items():
    if count > 2:
        print(f"{ip} -> {count} attempts")