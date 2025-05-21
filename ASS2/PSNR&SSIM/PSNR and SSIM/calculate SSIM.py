import re

def parse_ssim_log(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        match = re.search(r'All:([0-9.]+)', content)
        if match:
            ssim_value = float(match.group(1))
            print(f" Average SSIM: {ssim_value:.4f}")
            return ssim_value
        else:
            print("SSIM not found.")
            return None
    except Exception as e:
        print(f" Error: {e}")
        return None

parse_ssim_log('ssim5.log')
