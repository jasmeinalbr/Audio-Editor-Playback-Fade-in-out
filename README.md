# 🎧 Audio Editor & Playback with Fade In/Out

A simple web-based audio player and editor built using **Streamlit**, allowing users to:

- Upload `.mp3` or `.wav` files
- Adjust playback speed
- Add fade-in / fade-out effects
- Adjust volume
- Visualize waveform
- Download the modified audio

---

## 🚀 Features

✅ Upload `.wav` / `.mp3` audio  
✅ Playback speed control (0.5x to 3x)  
✅ Optional fade in / fade out effect  
✅ Volume control slider  
✅ Waveform visualization using `librosa`  
✅ Download the edited audio  

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Librosa](https://librosa.org/)
- [PyDub](https://github.com/jiaaro/pydub)
- [Matplotlib](https://matplotlib.org/)
- Python 3.11+

---

## 🔧 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/jasmeinalbr/Audio-Editor-Playback-Fade-in-out.git
   cd Audio-Editor-Playback-Fade-in-out
   
2. **(Optional) Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate # atau venv\Scripts\activate di Windows
3. **Install dependencies**
   ```
   bash pip install -r
   requirements.txt
4. **Run the app**
   ```bash
   streamlit run app.py
