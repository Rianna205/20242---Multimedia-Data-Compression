import numpy as np
import soundfile as sf
import pywt

# 📥 Load audio
audio, sr = sf.read("recorded file.wav")
if audio.ndim > 1:
    audio = audio[:, 0]  # Convert to mono

# 🧹 Trim to power of 2
length = 2 ** int(np.floor(np.log2(len(audio))))
audio = audio[:length]

# 🌊 WPT Decomposition
wp = pywt.WaveletPacket(data=audio, wavelet='db4', maxlevel=5, mode='symmetric')
nodes = wp.get_level(5, order='freq')
paths = [node.path for node in nodes]
coeffs = [np.array(node.data, dtype=np.float32) for node in nodes]

# 🔢 Quantization setup
flat = np.concatenate(coeffs)
step = (np.max(flat) - np.min(flat)) / 256

# 🔢 Quantize each coefficient array
quantized = [np.round(c / step).astype(np.int16) for c in coeffs]

# 💾 Save
np.savez("compressed_wpt.npz", quantized=quantized, step=step, sr=sr, paths=np.array(paths))
print("✅ WPT compression saved to compressed_wpt.npz")
