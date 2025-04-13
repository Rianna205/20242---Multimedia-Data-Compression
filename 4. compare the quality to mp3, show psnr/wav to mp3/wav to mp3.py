from pydub import AudioSegment

wav_path = "D:/HUY HOANG/Study/2024.2/nen va ma hoa du lieu da phuong tien/wav to mp3/reconstructed_wpt.wav"
mp3_path = "D:/HUY HOANG/Study/2024.2/nen va ma hoa du lieu da phuong tien/wav to mp3/reconstructed_wpt.mp3"

audio = AudioSegment.from_wav(wav_path)
audio.export(mp3_path, format="mp3", bitrate="128k")

print(f"Converted {wav_path} to MP3 with 128kbps bitrate.")