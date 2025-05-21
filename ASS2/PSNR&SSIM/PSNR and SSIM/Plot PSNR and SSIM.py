import matplotlib.pyplot as plt

# Dữ liệu đầu vào
labels = ['Video1', 'Video2', 'Video3', 'Video4', 'Video5']
psnr_values = [26.85, 27.74, 25.29, 26.77, 27.43]
ssim_values = [0.9451, 0.9426, 0.9405, 0.9355, 0.9256]

# Thiết lập kích thước
plt.figure(figsize=(12, 5))

# -------- Biểu đồ PSNR --------
plt.subplot(1, 2, 1)
plt.bar(labels, psnr_values, color='skyblue')
plt.title('PSNR comparision')
plt.xlabel('Video')
plt.ylabel('PSNR (dB)')
plt.ylim(min(psnr_values) - 0.2, max(psnr_values) + 0.2)
for i, v in enumerate(psnr_values):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center')

# -------- Biểu đồ SSIM --------
plt.subplot(1, 2, 2)
plt.bar(labels, ssim_values, color='salmon')
plt.title('SSIM comparision')
plt.xlabel('Video')
plt.ylabel('SSIM')
plt.ylim(min(ssim_values) - 0.001, 1.0)
for i, v in enumerate(ssim_values):
    plt.text(i, v + 0.0005, f"{v:.4f}", ha='center')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
