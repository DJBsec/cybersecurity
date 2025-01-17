from gtts import gTTS
from datetime import datetime
from pydub import AudioSegment
from pydub.generators import Silence

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity stories for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries for the podcast
stories = [
    "Chinese state-sponsored hackers exploited vulnerabilities in third-party software to gain access to the U.S. Treasury's systems, including those used by Treasury Secretary Janet Yellen. This breach highlights the risks posed by supply chain attacks and the importance of vetting cybersecurity vendors.",
    "Cybercriminals have been stealing Walmart Spark account credentials to make unauthorized purchases, leading to financial losses for customers. Victims have discovered mysterious charges on their bank accounts.",
    "Australia's new cybersecurity laws require companies to report ransomware payments, creating legal challenges and raising privacy concerns. The laws also empower a review board to investigate cyber incidents.",
    "In his last days in office, President Biden issued an executive order to improve cybersecurity for federal contractors, focusing on secure software development and addressing emerging threats like AI and quantum computing.",
    "Security researchers warn of a surge in AI-generated phishing emails, which are increasingly sophisticated and harder to detect. These attacks often bypass traditional email security filters.",
    "The Consumer Electronics Show (CES) 2025 revealed a growing focus on IoT security, with vendors showcasing new products designed to secure smart home devices. However, experts caution that vulnerabilities in older devices remain a significant threat.",
]

# Generate audio for the intro
print("Generating audio for the intro...")
intro_audio = gTTS(text=intro_text, lang='en', slow=False)
intro_audio.save("intro.mp3")

# Generate audio for each story
story_audio_files = []
for idx, story in enumerate(stories, start=1):
    print(f"Generating audio for story {idx}...")
    story_audio = gTTS(text=f"Story {idx}: {story}", lang='en', slow=False)
    story_file = f"story_{idx}.mp3"
    story_audio.save(story_file)
    story_audio_files.append(story_file)

# Combine audio with pauses using pydub
final_audio = AudioSegment.from_file("intro.mp3")

# Add each story with a 2-second pause in between
for story_file in story_audio_files:
    story_segment = AudioSegment.from_file(story_file)
    pause = Silence(duration=2000)  # 2-second pause
    final_audio += story_segment + pause

# Export the combined audio
output_file = f"CyberSecurityStories-{output_date}.mp3"
final_audio.export(output_file, format="mp3")
print(f"Final audio file created: {output_file}")
