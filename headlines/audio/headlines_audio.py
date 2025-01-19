from gtts import gTTS
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity stories for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries with pauses between stories
summaries = """
1. Chinese Hackers Breach U.S. Treasury Department:
Chinese state-sponsored hackers exploited vulnerabilities in third-party software to gain access to the U.S. Treasury's systems, including those used by Treasury Secretary Janet Yellen. This breach highlights the risks posed by supply chain attacks and the importance of vetting cybersecurity vendors.

... 

2. Walmart Spark Accounts Hacked in Fraud Scheme:
Cybercriminals have been stealing Walmart Spark account credentials to make unauthorized purchases, leading to financial losses for customers. Victims have discovered mysterious charges on their bank accounts.

... 

3. Australia's New Cyber Laws Spark Debate:
Australia's new cybersecurity laws require companies to report ransomware payments, creating legal challenges and raising privacy concerns. The laws also empower a review board to investigate cyber incidents.

... 

4. President Biden’s Final Cybersecurity Executive Order:
In his last days in office, President Biden issued an executive order to improve cybersecurity for federal contractors, focusing on secure software development and addressing emerging threats like AI and quantum computing.

... 

5. Rising Threat of AI-Driven Phishing Campaigns:
Security researchers warn of a surge in AI-generated phishing emails, which are increasingly sophisticated and harder to detect. These attacks often bypass traditional email security filters.

... 

6. Cybersecurity Lessons from CES 2025:
The Consumer Electronics Show (CES) 2025 revealed a growing focus on IoT security, with vendors showcasing new products designed to secure smart home devices. However, experts caution that vulnerabilities in older devices remain a significant threat.
"""

# Combine the intro and summaries
full_text = f"{intro_text}\n\n{summaries}"

# Construct the output filename
output_file = f"CyberSecurityStories-{output_date}.mp3"

# Create the audio file
try:
    print("Generating audio file...")
    audio = gTTS(text=full_text, lang='en', slow=False)
    audio.save(output_file)
    print(f"Audio file successfully created: {output_file}")
except Exception as e:
    print(f"An error occurred while generating the audio file: {e}")
