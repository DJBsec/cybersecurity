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

**Story 1: $4.5M Grant Bolsters UA Little Rock's Cybersecurity Education**

The University of Arkansas at Little Rock has received a $4.5 million grant to enhance its cybersecurity education programs. This funding aims to develop advanced curricula, provide scholarships, and establish partnerships with industry leaders to prepare students for the growing demand in the cybersecurity sector. The initiative underscores the university's commitment to addressing the national shortage of cybersecurity professionals. citeturn0search0

**Story 2: Ukraine Launches Major Cyber Attack on Russian Gas Infrastructure**

Ukrainian cyber forces have reportedly initiated a significant cyber attack targeting Russia's gas infrastructure. This offensive aims to disrupt the operational capabilities of Russian energy facilities, marking a strategic move in the ongoing cyber warfare between the two nations. The attack highlights the escalating use of cyber operations in geopolitical conflicts. 

**Story 3: Hidden Malware in WordPress Websites Allows Remote Code Execution**

Security researchers have uncovered a sophisticated malware campaign targeting WordPress websites. Attackers are embedding malicious code within the 'mu-plugins' directory, enabling remote execution of code, full server compromise, data theft, and persistent control over infected sites. Website owners are urged to implement file integrity monitoring and enforce strict security measures to mitigate this threat. 

**Story 4: Dutch Police Seize 127 Servers of Bulletproof Hosting Service Zservers**

Dutch authorities have seized 127 servers belonging to the bulletproof hosting provider Zservers/XHost. This action follows sanctions imposed by the US, UK, and Australia against the service for supporting Russian ransomware operations, particularly the LockBit group. The crackdown aims to disrupt cybercriminal infrastructure and deter future illicit activities. 

**Story 5: New Data-Stealing Malware Exploits Microsoft Outlook**

A newly identified family of data-stealing malware is leveraging Microsoft Outlook to compromise systems. The malware initiates attacks through stolen credentials, exploiting Outlook's features to disseminate malicious content and exfiltrate sensitive information. Organizations are advised to strengthen email security protocols and monitor for unusual activities within their networks. citeturn0search3

**Story 6: RansomHub Ransomware Expands to Multiple Operating Systems**

The RansomHub ransomware group has evolved its tactics to target a range of operating systems, including Windows, VMware ESXi, Linux, and FreeBSD. By developing platform-specific encryption methods and exploiting known vulnerabilities, the group has significantly broadened its attack surface. Entities across various sectors are urged to apply security patches promptly and implement robust defense strategies. 

**Story 7: The High-Stakes Disconnect in ICS/OT Security**

Recent incidents have exposed a critical gap in securing Industrial Control Systems (ICS) and Operational Technology (OT) environments. Traditional IT security measures often fall short in these settings, necessitating specialized controls and dedicated budgets to protect critical infrastructure. Implementing tailored cybersecurity strategies is essential to address the unique challenges posed by ICS/OT systems. 

**Story 8: Ransomware Gangs Accelerate Encryption Timelines**

New research indicates that ransomware groups are reducing the time between initial network infiltration and system encryption to an average of 17 hours. This rapid execution leaves organizations with a narrow window to detect and respond to attacks. Enhanced monitoring and swift incident response protocols are critical to mitigating the impact of such accelerated ransomware operations. 

**Story 9: Microsoft Uncovers New XCSSET macOS Malware Variant**

Microsoft has identified a new variant of the XCSSET malware targeting macOS systems. This iteration employs advanced obfuscation techniques, updated persistence methods, and novel infection strategies, enhancing its ability to steal data from applications like Notes and exfiltrate system information. Users are encouraged to maintain up-to-date security measures to defend against this evolving threat. 

**Story 10: X Blocks Signal Contact Links, Flags Them as Malicious**

The social media platform X (formerly Twitter) has begun blocking links to "Signal.me," a URL used by the Signal encrypted messaging service to share contact information. Attempts to post these links result in error messages citing spam or malicious content concerns. This development affects users' ability to share Signal contact links on the platform, prompting discussions about content moderation practices. 
"""

# Combine the intro and summaries
full_text = f"{intro_text}\n\n{summaries}"

# Construct the output filename
output_file = f"E:\\GIT\\djbsec.github.io\\assets\\audio\\news\\CyberSecurityNews-{output_date}.mp3"

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
