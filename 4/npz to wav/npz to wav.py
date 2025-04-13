import numpy as np
import soundfile as sf
import pywt

try:
    # Load WPT compressed data
    print("Loading compressed data...")
    data = np.load("compressed_wpt.npz", allow_pickle=True)
    print("File keys:", data.files)
    
    quantized = data["quantized"]
    step = data["step"]
    sr = int(data["sr"])
    paths = data["paths"]
    
    print(f"SR: {sr}, Step: {step}, Paths: {paths[:3]}... (total: {len(paths)})")
    
    # Convert quantized coefficients back to float values
    coeffs = [q.astype(np.float32) * step for q in quantized]
    print("Coeffs shapes:", [c.shape for c in coeffs])
    
    # Rebuild WPT tree
    print("Rebuilding wavelet tree...")
    wp = pywt.WaveletPacket(data=None, wavelet='db4', mode='symmetric')
    
    for path, c in zip(paths, coeffs):
        wp[path] = c
    
    # Reconstruct signal
    print("Reconstructing signal...")
    reconstructed = wp.reconstruct(update=True)
    
    # Normalize to avoid clipping
    reconstructed = reconstructed / np.max(np.abs(reconstructed))
    
    # Save as WAV
    print("Saving WAV file...")
    sf.write("reconstructed_wpt.wav", reconstructed.astype(np.float32), sr)
    print("Successfully reconstructed and saved!")

except Exception as e:
    print(f" Error: {str(e)}")
    import traceback
    traceback.print_exc()