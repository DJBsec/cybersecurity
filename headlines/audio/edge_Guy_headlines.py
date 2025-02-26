import edge_tts
import asyncio
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: February 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 02-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity News for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries
summaries = """


**Microsoft Fixes Entra ID Authentication Issue Caused by DNS Change**

   Microsoft has resolved an issue that led to Entra ID DNS authentication failures affecting services utilizing Seamless Single Sign-On and Entra Connect Sync. The problem originated from a recent DNS modification intended to remove duplicate IPv6 CNAMEs, which inadvertently deleted a crucial domain used in the authentication process. This caused authentication requests to fail between 17:18 and 18:35 UTC on February 25, 2025. Microsoft has since reverted the change, restoring full service functionality. citeturn0search0

**GitVenom Campaign Abusing Thousands of GitHub Repositories to Infect Users**

   A sophisticated malware campaign, dubbed "GitVenom," has been exploiting GitHub's open-source platform to distribute malicious code through thousands of fraudulent repositories. Active since at least 2023, the attackers have created repositories masquerading as legitimate projects, such as automation tools and cryptocurrency utilities. These repositories contain hidden malicious code designed to steal cryptocurrencies and provide remote access to compromised systems. The campaign has primarily impacted users in Russia, Brazil, and Turkey. citeturn0search30

**New Auto-Color Linux Backdoor Targets North American Governments and Universities**

   Researchers have identified a previously undocumented Linux backdoor named 'Auto-Color,' which was active in attacks between November and December 2024. This malware specifically targeted universities and government organizations in North America and Asia. 'Auto-Color' is noted for its evasive capabilities, allowing it to maintain prolonged access to infected systems and making it challenging to detect and remove. citeturn0search1

**Windows 10 KB5052077 Update Fixes Broken SSH Connections**

   Microsoft has released the optional KB5052077 preview cumulative update for Windows 10 version 22H2, addressing nine issues, including a fix for a known problem that disrupted SSH connections. The issue, acknowledged in November 2024, caused the OpenSSH service to fail to start on certain devices, preventing SSH connections. This update aims to resolve the problem, restoring normal SSH functionality for affected users. citeturn0search2

**Belarus-Linked Ghostwriter Uses Macropack-Obfuscated Excel Macros to Deploy Malware**

   The Belarus-aligned threat actor known as Ghostwriter has launched a new campaign targeting opposition activists in Belarus and Ukrainian military and government organizations. The attackers employ malware-laden Microsoft Excel documents with obfuscated macros to deliver a variant of the PicassoLoader malware. This campaign, active since November-December 2024, aims to establish persistent access and conduct cyber-espionage activities against the targeted entities. citeturn0search3

**16 Malicious Chrome Extensions Infected Over 3.2 Million Users**

   A coordinated campaign involving at least 16 malicious Chrome extensions has compromised over 3.2 million users worldwide. These extensions, posing as legitimate tools like screen capture utilities and ad blockers, manipulated browser security settings to execute advertising fraud and manipulate search engine results. Despite their removal from the Chrome Web Store, users who have not manually uninstalled these extensions remain at risk. citeturn0search4

**Have I Been Pwned Adds 284M Accounts Stolen by Infostealer Malware**

   The data breach notification service 'Have I Been Pwned' has incorporated over 284 million accounts compromised by information-stealing malware. These accounts were discovered in a 1.5TB collection of stealer logs shared on a Telegram channel known as "ALIEN TXTBASE." The data includes 23 billion rows with 493 million unique website and email address pairs, highlighting the extensive reach of infostealer malware in recent cyber incidents. citeturn0search5

**Max Severity RCE Vulnerability in All Versions of MITRE Caldera**

   A critical remote code execution vulnerability, identified as CVE-2025-27364, has been discovered in all versions of MITRE's Caldera platform, an open-source adversary emulation tool used for red-teaming exercises. The flaw, which has a maximum severity score of 10, allows attackers to execute arbitrary code without user interaction or special privileges. MITRE recommends that all Caldera users immediately update to the latest version to mitigate potential exploitation risks. citeturn0search6

**LockBit Taunts FBI Director Kash Patel with Alleged "Classified" Leak Threat**

   The ransomware group LockBit has issued a provocative message to newly appointed FBI Director Kash Patel, claiming possession of "classified information" that could "destroy" the agency if leaked. This message, published on LockBit's dark web leak site, appears to be an attempt to intimidate and challenge U.S. law enforcement agencies. The authenticity and potential impact of the alleged information remain unverified. citeturn0search7

**UAC-0212 Hackers Launching Destructive Attacks Targeting Critical Infrastructure**

    A sophisticated threat group identified as UAC-0212 has intensified efforts to compromise critical infrastructure systems in Ukraine. Active since July 2024, their attacks focus on sectors such as energy, water supply, grain logistics, and transportation. Utilizing supply-chain compromises, the group deploys destructive payloads and advanced persistence mechanisms to disrupt industrial control systems and operational technology, posing significant risks to national security and public safety. citeturn0search9

"""

# Combine the intro and summaries
full_text = f"{intro_text}\n\n{summaries}"

# Construct the output filename
output_file = f"F:\\GIT\\djbsec.github.io\\assets\\audio\\news\\CyberSecurityNews-{output_date}.mp3"

async def generate_audio():
    try:
        print("Generating audio file using Edge TTS...")

        # ✅ Use edge_tts instead of edge_headlines
        communicate = edge_tts.Communicate(full_text, "en-US-GuyNeural")

        # Save the generated speech as an MP3 file
        await communicate.save(output_file)

        print(f"Audio file successfully created: {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the audio file: {e}")

# Run the async function
asyncio.run(generate_audio())
