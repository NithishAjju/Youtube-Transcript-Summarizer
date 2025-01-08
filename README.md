# 🎥 YouTube Transcript to Detailed Notes Converter

## 📌 **Project Overview**
This project provides an interactive web application built with **Streamlit** that extracts transcripts from YouTube videos and generates detailed, structured summaries using **Google's Gemini AI model**. Users can customize the language and length of the summaries, making it an adaptable tool for various use cases such as education, research, and content analysis.

---

## 🚀 **Key Features**
- **YouTube Transcript Extraction:** Automatically extracts transcripts from YouTube videos using the `youtube_transcript_api` library.
- **Language Support:** Summaries can be generated in multiple languages including **English, Spanish, French, German, Italian, and Portuguese**.
- **Customizable Summary Length:** Users can choose summary lengths ranging from **50 to 500 words**.
- **Interactive UI:** User-friendly interface built with **Streamlit**.
- **AI-Powered Summaries:** Uses **Google's Gemini Pro** model for precise and context-aware summaries.

---

## 🛠️ **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Python
- **AI Model:** Google Gemini Pro
- **APIs:** YouTube Transcript API
- **Environment Management:** dotenv

---

## 📂 **Project Structure**
```
📁 project_root
│── app.py          # Main application file
│── .env            # Environment variables (API Keys)
│── requirements.txt # Python dependencies
└── README.md       # Project documentation
```

---

## ⚙️ **Setup and Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add API Key:**
   Create a `.env` file in the project root and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser:
   - Default URL: `http://localhost:8501`

---

## 🎯 **How to Use the Application**

1. Enter a **YouTube video URL**.
2. Select a **language** for the summary.
3. Choose the desired **summary length** using the slider.
4. Click **"Get Detailed Notes"**.
5. Review the generated summary displayed on the interface.

---

## 📖 **Customization Options**
- **Languages Supported:** English, Spanish, French, German, Italian, Portuguese.
- **Summary Length:** Adjustable between 50 to 500 words.

---

## 🐍 **Dependencies**
Ensure the following Python libraries are installed:
```
streamlit
python-dotenv
google-generativeai
youtube-transcript-api
```

---

## 🛡️ **Error Handling**
- Invalid YouTube URLs are flagged with descriptive error messages.
- Clear guidance is provided when transcripts are unavailable.
- Fallbacks ensure the application remains stable during unexpected issues.

---

## 🤝 **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request.

---

## 📝 **License**
This project is licensed under the **MIT License**.

---

## 📧 **Contact**
For feedback, questions, or collaboration:
- **Email:** your.email@example.com
- **GitHub:** [Your GitHub Profile](https://github.com/yourusername)

---

⭐ **If you find this project helpful, don’t forget to star the repository!** ⭐

