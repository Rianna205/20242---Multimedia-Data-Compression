% Folder path containing the .wav and .mp3 files
inputFolder = 'D:\sosanhmp3vswav';

% Paths to input files (đã sửa lỗi chính tả)
wavFile = fullfile(inputFolder, 'input01.mp3');
mp3File = fullfile(inputFolder, 'input02.wav');

% Load audio data
[original, Fs1] = audioread(wavFile);
[decoded, Fs2] = audioread(mp3File);

% Resample if necessary
if Fs1 ~= Fs2
    decoded = resample(decoded, Fs1, Fs2);
end

% Match length
minLen = min(size(original,1), size(decoded,1));
original = original(1:minLen, :);
decoded  = decoded(1:minLen, :);

% Calculate MSE and PSNR
mse = mean((original - decoded).^2, 'all');
peak = max(abs(original), [], 'all');
psnrValue = 10 * log10(peak^2 / mse);

% Show result
fprintf('PSNR = %.2f dB\n', psnrValue);

% Time vector
t = (0:minLen-1) / Fs1;

% Plot waveform and spectrum only
figure('Name', 'Analysis for input01 vs input02', 'NumberTitle', 'off');

% Waveform plot
subplot(2,1,1);
plot(t, original, 'b'); hold on;
plot(t, decoded, 'r');
title('Waveform'); legend('input01 (.mp3)', 'input02 (.wav)');
xlabel('Time (s)'); ylabel('Amplitude');

% Frequency spectrum plot
subplot(2,1,2);
N = length(original);
f = Fs1*(0:(N/2))/N;
Y1 = abs(fft(original(:,1), N));
Y2 = abs(fft(decoded(:,1), N));
plot(f, Y1(1:N/2+1), 'b'); hold on;
plot(f, Y2(1:N/2+1), 'r');
title('Frequency Spectrum'); legend('input01', 'input02');
xlabel('Frequency (Hz)'); ylabel('Magnitude');

sgtitle(['PSNR = ', num2str(psnrValue, '%.2f'), ' dB']);
