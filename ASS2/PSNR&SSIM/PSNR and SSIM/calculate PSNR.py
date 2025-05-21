import re

def compute_avg_psnr_from_log(filename):
    psnr_values = []

    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'psnr_avg:([0-9.]+)', line)
            if match:
                value = float(match.group(1))
                psnr_values.append(value)
            elif 'psnr_avg:inf' in line:
                continue

    if psnr_values:
        avg_psnr = sum(psnr_values) / len(psnr_values)
        return avg_psnr
    else:
        return None

# Ví dụ dùng
avg = compute_avg_psnr_from_log('psnr5.log')
if avg:
    print(f"Average PSNR: {avg:.2f} dB")

