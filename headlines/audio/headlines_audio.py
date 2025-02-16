from gtts import gTTS
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity stories for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries with pauses between stories
summaries = """

Here are concise summaries of the provided cybersecurity stories:

**Story 1: Storm-2372 Conducts Device Code Phishing Campaign**

Microsoft has identified an ongoing phishing campaign by the threat actor group Storm-2372, active since August 2024. The attackers impersonate prominent individuals on platforms like WhatsApp, Signal, and Microsoft Teams to build trust with targets. They then send fake Teams meeting invitations, prompting recipients to enter authentication codes on legitimate Microsoft login pages. This process allows the attackers to capture access tokens, granting unauthorized access to victims' emails and cloud storage without needing passwords or multi-factor authentication. 

**Story 2: New Go-Based Malware Exploits Telegram as C2 Channel**

Researchers have discovered a new backdoor malware written in Go that utilizes Telegram as its command-and-control (C2) channel. Although still under development, the malware is fully operational, capable of executing PowerShell commands, establishing persistence, and self-deletion. By leveraging Telegram's API, the malware communicates with attackers, posing significant challenges for cybersecurity defenses due to the use of legitimate cloud-based applications for malicious activities. 

**Story 3: LA County's Strategy to Combat Phishing Through Employee Training**

Los Angeles County has implemented a comprehensive training program to educate and retrain its workforce in identifying and combating phishing attacks. The initiative focuses on raising awareness about phishing tactics, promoting best practices for email security, and conducting regular simulations to test employees' responses to potential threats. This proactive approach aims to strengthen the county's cybersecurity posture by empowering employees to recognize and report phishing attempts effectively.

**Story 4: Hackers Exploit Authentication Bypass in Palo Alto Networks PAN-OS**

Attackers are actively exploiting a recently patched authentication bypass vulnerability (CVE-2025-0108) in Palo Alto Networks' PAN-OS firewalls. This flaw allows unauthenticated users to access certain PHP scripts via the management web interface, potentially compromising system integrity and confidentiality. Administrators are strongly advised to update their systems to the latest firmware versions to mitigate this security risk. 

**Story 5: Suspected Russian Spies Caught Spoofing Teams Invites**

Suspected Russian cyber spies have been detected sending fraudulent Microsoft Teams meeting invitations to infiltrate networks of government and business entities. By posing as trusted contacts, these attackers trick recipients into providing authentication tokens, granting unauthorized access to sensitive information such as emails and cloud data. This campaign, attributed to the group known as Storm-2372, has been active since August 2024 and highlights the need for heightened vigilance against sophisticated phishing tactics.  
"""

# Combine the intro and summaries
full_text = f"{intro_text}\n\n{summaries}"

# Construct the output filename
output_file = f"E:\CyberSecurityStories-{output_date}.mp3"

# Create the audio file
try:
    print("Generating audio file...")
    audio = gTTS(text=full_text, lang='en', slow=False)
    audio.save(output_file)
    print(f"Audio file successfully created: {output_file}")
except Exception as e:
    print(f"An error occurred while generating the audio file: {e}")
