import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables for API keys
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to extract the video ID from the YouTube URL
def extract_video_id(youtube_video_url):
    try:
        # Extract video ID after v= and before any other query parameters like &t=
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        return video_id
    except Exception as e:
        raise ValueError("Invalid YouTube URL.")

# Function to extract transcript of the YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        raise ValueError("Could not retrieve transcript. Please make sure the video has captions.")

# Function to generate the summary using Google Gemini Pro
def generate_gemini_content(transcript_text, language, summary_length):
    model = genai.GenerativeModel("gemini-pro")
    
    # Language-specific instructions
    language_instructions = {
        "English": "Please provide the summary in English.",
        "Spanish": "Por favor, proporcione el resumen en español.",
        "French": "Veuillez fournir le résumé en français.",
        "German": "Bitte geben Sie die Zusammenfassung auf Deutsch an.",
        "Italian": "Si prega di fornire il riassunto in italiano.",
        "Portuguese": "Por favor, forneça o resumo em português."
    }
    
    # Default to English if language not supported
    language_instruction = language_instructions.get(language, "Please provide the summary in English.")
    
    # Length-specific formatting and structure guidelines
    length_specific_instructions = {
        "short": """
Format the summary in approximately 50-100 words:
- Begin with a one-sentence overview that captures the video's core message
- Follow with 2-3 key takeaways
- Use concise, impactful language
- Focus only on the most crucial points
""",
        "medium": """
Format the summary in approximately 100-300 words:
- Start with a comprehensive overview paragraph
- Include 4-5 main points with brief supporting details
- Add relevant examples where appropriate
- Highlight any practical applications or key insights
- Maintain a clear narrative flow
""",
        "long": """
Format the summary in approximately 300-500 words:
- Begin with an executive summary paragraph
- Break down the content into clearly defined sections
- Include detailed examples and case studies mentioned
- Capture nuanced arguments and counterpoints
- Add context and background information where relevant
- Conclude with key implications or action items
- Use subheadings to organize major themes
"""
    }
    
    # Determine length category based on user's selection
    if summary_length <= 100:
        length_format = length_specific_instructions["short"]
    elif summary_length <= 300:
        length_format = length_specific_instructions["medium"]
    else:
        length_format = length_specific_instructions["long"]
    
    # Enhanced prompt template
    detailed_prompt = f"""
You are an expert content summarizer specializing in creating precise, length-optimized summaries. Analyze this video transcript and create a summary following these specific guidelines:

{length_format}

Key Requirements:
1. Target Length: Aim for approximately {summary_length} words
2. Writing Style:
   - Use active voice and clear, professional language
   - Break complex ideas into digestible segments
   - Maintain the original speaker's tone while being concise
   - Include specific numbers, data points, or statistics mentioned
   - Preserve any unique terminology or specialized concepts
   
3. Content Organization:
   - Prioritize information based on significance and relevance
   - Maintain logical flow between ideas
   - Highlight unexpected insights or novel perspectives
   - Include real-world applications when mentioned
   
4. Quality Standards:
   - Ensure factual accuracy
   - Avoid redundancy
   - Maintain objective tone unless specifically highlighting opinions
   - Preserve technical precision while being accessible
If you can't find any of the above mentioned context in the transcripts dont display those points in the final summary.

Transcript to Summarize:
{transcript_text}
"""
    
    # Combine language instruction with the detailed prompt
    final_prompt = f"{language_instruction}\n\n{detailed_prompt}"
    
    # Generate content using the Gemini model
    response = model.generate_content(final_prompt)
    return response.text



# Frontend layout and UI components
st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥", layout="centered")

# Title and instructions
st.title("YouTube Transcript to Detailed Notes Converter")
st.write("""
    **Instructions:**
    1. Paste a YouTube video link into the input box below.
    2. Click on "Get Detailed Notes" to generate a summary of the video based on its transcript.
    3. You can then read the detailed summary!
""")

# Input for YouTube video link
youtube_link = st.text_input("Enter YouTube Video URL", "")

# Show video thumbnail and fetch summary if button is clicked
if youtube_link:
    try:
        video_id = extract_video_id(youtube_link)
        image_url = f"http://img.youtube.com/vi/{video_id}/0.jpg"

        # Apply a CSS class to center the image
        st.markdown(
            """
            <style>
                .center-img {
                    display: flex;
                    justify-content: center;
                }
            </style>
            """, unsafe_allow_html=True)
        # Use the CSS class in the HTML for the image
        st.markdown(
            f'<div class="center-img"><img src="{image_url}" width="600" height="500" /></div>',
            unsafe_allow_html=True)
    except ValueError as e:
        st.error(str(e))

# Language selection for summary
language_options = ["English", "Spanish", "French", "German", "Italian", "Portuguese"]  # Add more options as needed
language = st.selectbox("Language", language_options)

# Slider to adjust the summary length (words)
summary_length = st.slider("Length of the summary", 50, 500, 250)

# Display button to trigger processing
if st.button("Get Detailed Notes"):

    # Show a loading spinner while processing
    with st.spinner("Processing..."):
        try:
            transcript_text = extract_transcript_details(youtube_link)

            if transcript_text:
                # Generate summary based on transcript text, selected language, and summary length
                summary = generate_gemini_content(transcript_text, language, summary_length)
                st.markdown("## Detailed Notes:")
                st.write(summary)
            else:
                st.warning("No transcript found for this video.")

        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error("Something went wrong. Please try again.")

    # Clear button after processing
    if st.button("Clear"):
        st.experimental_rerun()
