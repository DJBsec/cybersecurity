from gtts import gTTS
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity stories for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries with pauses between stories
summaries = """

Story 1: Lazarus Group Targets Developers with Infostealer Malware

The North Korean-linked Lazarus Group has initiated a campaign targeting software developers using infostealer malware. They employ social engineering tactics, such as fake job interviews and compromised NPM packages, to trick developers into executing malicious scripts. The malware utilizes obfuscation techniques like Base64 encoding and zlib compression to conceal its code. Key components include a Python script that decodes and executes the malware, leading to the theft of sensitive information from developers' systems.

Story 2: SonicWall Firewall Vulnerability Exploited Post PoC Release

Attackers are actively exploiting an authentication bypass vulnerability in SonicWall firewalls following the release of a proof-of-concept (PoC) exploit. This flaw affects the SSLVPN authentication mechanism in specific SonicOS versions, allowing remote attackers to hijack active SSL VPN sessions without authentication. SonicWall has urged users to promptly update their firmware to mitigate this threat.

Story 3: PirateFi Game on Steam Distributes Vidar Malware

A free-to-play game named PirateFi was found distributing the Vidar infostealing malware to unsuspecting users on the Steam platform. Available between February 6th and 12th, the game was downloaded by up to 1,500 users. Steam has notified potentially affected users, advising them to run full system scans and consider reinstalling Windows as a precaution.

Story 4: New Phishing Kit Bypasses Two-Factor Authentication

A phishing kit named Astaroth has been identified targeting Gmail, Yahoo, and Microsoft accounts. It bypasses two-factor authentication (2FA) by acting as a man-in-the-middle, capturing tokens, credentials, and session cookies in real-time. This method renders traditional phishing defenses less effective, highlighting the need for enhanced security measures.

Story 5: North Korean IT Workers Infiltrate International Companies

North Korean IT workers have been securing remote positions in international companies using false identities. This practice violates international sanctions and poses significant cybersecurity risks, including data theft and the installation of backdoors on compromised systems. The Insikt Group reports that these operatives use sophisticated malware and front companies to evade detection.

Story 6: PostgreSQL Bug Exploited in US Treasury Attack

A high-severity SQL injection vulnerability in the PostgreSQL interactive tool was exploited alongside a zero-day in BeyondTrust software to breach the US Treasury in December. Researchers from Rapid7 disclosed that the PostgreSQL flaw was crucial to the attack, emphasizing the need for timely patching and vigilance against complex exploit chains.
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
