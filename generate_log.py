import random
random.seed(42)  # same file every time

attackers = ["203.0.113.5", "203.0.113.9", "198.51.100.7"]
normal = [f"192.168.1.{i}" for i in range(20, 40)]

lines = []
for ip in attackers:
    lines += [f"{ip} Failed login"] * random.randint(15, 30)
for ip in normal:
    lines += [f"{ip} Successful login"] * random.randint(5, 20)
    lines += [f"{ip} Failed login"] * random.randint(0, 2)

while len(lines) < 1000:
    lines.append(f"{random.choice(normal)} Successful login")

random.shuffle(lines)
open("test_1000.log", "w").write("\n".join(lines))
print(len(lines), "lines written")