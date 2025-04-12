import streamlit as st
import librosa
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt
from io import BytesIO

# Konfigurasi halaman
st.set_page_config(page_title="Audio Playback", layout="centered")

# Title di tengah
st.markdown("<h1 style='text-align: center;'>🎵 Audio Playback & Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Upload audio
st.markdown("### 📤  Upload file audio kamu")
uploaded_file = st.file_uploader("", type=["wav", "mp3"])
st.markdown("---")

st.markdown("### ⚙️  Pengaturan Audio")

# Pilih kecepatan
st.markdown("#### ⚡  Kecepatan Playback")
speed = st.selectbox("", [0.5, 1.0, 1.5, 2.0, 3.0], index=1)

# Slider volume
st.markdown("#### 🔊  Volume")
volume = st.slider("Volume", min_value=0.0, max_value=1.0, value=1.0, step=0.1)

# Toggle fade
st.markdown("#### 🌫️  Efek Tambahan")
fade = st.checkbox("Tambahkan efek Fade In / Fade Out")

if uploaded_file is not None:
    # Load audio
    y, sr = librosa.load(uploaded_file, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)

    # Tampilkan info dasar
    st.markdown("---")
    st.markdown("### ℹ️  Informasi Audio")
    st.markdown(f"- **Durasi:** {duration:.2f} detik\n- **Sample Rate:** {sr} Hz")

    # Fungsi untuk ubah kecepatan
    def change_speed(audio_segment, speed=1.0):
        new_frame_rate = int(audio_segment.frame_rate * speed)
        return audio_segment._spawn(audio_segment.raw_data, overrides={
            "frame_rate": new_frame_rate
        }).set_frame_rate(audio_segment.frame_rate)

    # Normalisasi
    y_int16 = np.int16(y / np.max(np.abs(y)) * 32767)

    # Convert ke pydub
    audio_seg = AudioSegment(
        y_int16.tobytes(),
        frame_rate=sr,
        sample_width=2,
        channels=1
    )

    # Ubah kecepatan
    if speed != 1.0:
        audio_seg = change_speed(audio_seg, speed)

    # Tambah fade
    if fade:
        fade_in_duration = 2000
        fade_out_duration = 3000
        audio_seg = audio_seg.fade_in(fade_in_duration).fade_out(fade_out_duration)

    # Export ke buffer
    buffer = BytesIO()
    audio_seg.export(buffer, format="wav")
    buffer.seek(0)

    # Player audio
    st.markdown("###  ▶️ Audio Playback")
    st.audio(buffer, format="audio/wav")
    st.markdown("---")

    # Visualisasi
    st.subheader("📊  Waveform Audio")
    fig, ax = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set_xlabel("Waktu (detik)")
    ax.set_ylabel("Amplitudo")
    ax.set_title("Visualisasi Waveform")
    st.pyplot(fig)

    # Spacer + tombol download di tengah
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.download_button("⬇️ Download Hasil Edit", data=buffer, file_name="modified_audio.wav", mime="audio/wav")
