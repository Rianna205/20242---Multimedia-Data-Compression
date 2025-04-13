<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>20242 — Nén Dữ Liệu Đa Phương Tiện</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f7f9fb;
      color: #333;
      line-height: 1.6;
    }
    .container {
      max-width: 900px;
      margin: auto;
      padding: 2rem;
    }
    h1, h2 {
      color: #2b6777;
    }
    h1 {
      font-size: 2.5rem;
    }
    h2 {
      border-bottom: 2px solid #c8d8e4;
      padding-bottom: 0.3rem;
      margin-top: 2rem;
    }
    ul, ol {
      padding-left: 1.5rem;
    }
    code {
      background-color: #e8f0fe;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background-color: #e8f0fe;
      padding: 1rem;
      overflow-x: auto;
      border-radius: 6px;
      font-size: 0.95rem;
    }
    a {
      color: #1464c1;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .badge {
      background-color: #52ab98;
      color: white;
      border-radius: 12px;
      padding: 0.2em 0.6em;
      font-size: 0.85em;
      margin-left: 0.3em;
    }
    @media (max-width: 600px) {
      .container {
        padding: 1rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📦 20242 — Nén Dữ Liệu Đa Phương Tiện</h1>
    <p>Dự án môn học <strong>Nén Dữ Liệu Đa Phương Tiện</strong> (Mã học phần: 20242) tập trung vào việc ghi âm, phân tích phổ, nén dữ liệu, đánh giá chất lượng và tạo MIDI bằng Python &amp; MATLAB.</p>

    <h2>🧰 Công Nghệ Sử Dụng</h2>
    <ul>
      <li>Python <span class="badge">88.6%</span></li>
      <li>MATLAB <span class="badge">11.4%</span></li>
    </ul>

    <h2>🗂️ Nội Dung Dự Án</h2>
    <ol>
      <li><strong>Ghi Âm:</strong> Lưu đầu vào micro dưới dạng WAV.</li>
      <li><strong>Phân Tích Phổ:</strong> Sử dụng MATLAB để hiển thị phổ tần số.</li>
      <li><strong>Nén Âm Thanh:</strong> Áp dụng các thuật toán để giảm kích thước.</li>
      <li><strong>So Sánh với MP3:</strong> Sử dụng PSNR để đánh giá chất lượng.</li>
      <li><strong>Tạo và Trộn MIDI:</strong> Kết hợp MIDI thành bản nhạc mới.</li>
    </ol>

    <h2>📁 Cấu Trúc Thư Mục</h2>
    <pre><code>
20242---Multimedia-Data-Compression/
├── audio_recording/
│   └── record_audio.py
├── spectrum_analysis/
│   └── show_spectrum.m
├── audio_compression/
│   └── compress_audio.py
├── quality_comparison/
│   └── compare_psnr.py
├── midi_creation/
│   └── create_and_mix_midi.py
└── README.md
    </code></pre>

    <h2>🚀 Hướng Dẫn Sử Dụng</h2>
    <ol>
      <li><strong>Cài Đặt Môi Trường:</strong>
        <ul>
          <li>Cài đặt Python 3.x và MATLAB.</li>
          <li>Cài các thư viện Python:
            <pre><code>pip install numpy scipy matplotlib pydub</code></pre>
          </li>
        </ul>
      </li>
      <li>Chạy <code>record_audio.py</code> để ghi âm.</li>
      <li>Chạy <code>show_spectrum.m</code> trong MATLAB để phân tích phổ.</li>
      <li>Chạy <code>compress_audio.py</code> để nén âm thanh.</li>
      <li>Chạy <code>compare_psnr.py</code> để so sánh chất lượng.</li>
      <li>Chạy <code>create_and_mix_midi.py</code> để tạo &amp; trộn MIDI.</li>
    </ol>

    <h2>📈 Kết Quả</h2>
    <ul>
      <li>Giảm đáng kể kích thước âm thanh.</li>
      <li>Đánh giá chất lượng với PSNR.</li>
      <li>Tạo bản nhạc mới bằng MIDI tự động.</li>
    </ul>

    <h2>📄 Giấy Phép</h2>
    <p>Dự án được phát hành theo giấy phép MIT. Xem tệp <code>LICENSE</code> để biết thêm.</p>

    <h2>📬 Liên Hệ</h2>
    <p>Được thực hiện bởi <a href="https://github.com/Rianna205" target="_blank">Rianna205</a>. Mọi phản hồi đều rất đáng quý!</p>
  </div>
</body>
</html>
ss
