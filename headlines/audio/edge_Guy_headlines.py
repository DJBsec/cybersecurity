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


##Story 1: CISA Warns of Active Exploitation of Palo Alto PAN-OS Vulnerability

The Cybersecurity and Infrastructure Security Agency (CISA) has issued an urgent alert regarding the active exploitation of a high-severity authentication bypass vulnerability (CVE-2025-0108) in Palo Alto Networks' PAN-OS. This flaw allows unauthenticated attackers to bypass authentication controls and execute specific PHP scripts, potentially compromising system integrity. Organizations using affected PAN-OS versions are strongly advised to apply the latest patches and restrict management interface access to trusted internal IP addresses. The EPSS Score for these vulnerabilities is - 
EPSS Score for CVE-2025-0111 is 0.04%
EPSS Score for CVE-2025-0108 is 0.04%
EPSS Score for CVE-2024-9474 is 97.48%

## Story 2: SonicWall SonicOS SSLVPN Zero-Day Actively Exploited

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has issued a warning about a critical zero-day vulnerability (CVE-2024-53704) in SonicWall's SonicOS. This flaw allows remote attackers to hijack active SSL VPN sessions without credentials and is currently being exploited in the wild. CISA mandates that federal agencies patch affected systems by March 11, 2025, and recommends immediate remediation for all organizations using SonicWall devices. 
EPSS Score for CVE-2024-53704 is 0.05%

## Story 3: Juniper Networks Patches Critical Authentication Bypass

Juniper Networks has released patches for a critical vulnerability (CVE-2025-21589) affecting its Session Smart Router (SSR) devices. Discovered during internal security testing, this flaw allows network-based attackers to bypass authentication and gain administrative control over the devices. Administrators are advised to update to the latest firmware versions to secure their networks against potential exploits. 

## Story 4: OpenSSH Fixes Flaws Enabling MitM and DoS Attacks

OpenSSH has addressed two vulnerabilities that could facilitate man-in-the-middle (MitM) and denial-of-service (DoS) attacks. Researchers from Qualys identified these flaws, which, when combined, could allow attackers to bypass server key verification in OpenSSH clients. Users are encouraged to update their OpenSSH installations to prevent potential exploitation. :contentReference[oaicite:0]{index=0}

## Story 5: Ransomware Attack Shuts Down Five Michigan Casinos

A ransomware attack has forced the closure of five Kewadin Casinos across Michigan, affecting locations in Manistique, Hessel, St. Ignace, Christmas, and Sault Ste. Marie. While hotels remain open to current guests, new check-ins are suspended. The Sault Tribe of Chippewa Indians, which operates the casinos, is working with third-party experts to restore systems and investigate the breach. 

## Story 6: Chinese Hackers Exploit Microsoft App-V Tool to Evade Detection

The Chinese advanced persistent threat group "Mustang Panda" has been observed abusing Microsoft's Application Virtualization (App-V) Injector utility to inject malicious payloads into legitimate processes. This technique helps the attackers evade detection by antivirus software. The group primarily targets government entities in the Asia-Pacific region through spear-phishing campaigns. 

## Story 7: Weaponized PDFs Deliver Lumma InfoStealer to Educational Institutions

A new campaign targeting educational institutions involves the distribution of weaponized PDF documents embedded with Lumma InfoStealer malware. These malicious PDFs contain LNK files that, when executed, initiate a multi-stage infection process to steal sensitive data. Educational organizations are advised to implement robust cybersecurity measures to defend against such threats. 

## Story 8: New Snake Keylogger Variant Targets Windows Systems

A new variant of the Snake Keylogger malware is infecting Windows users, particularly in Asia and Europe. This version utilizes the AutoIt scripting language to deploy itself, adding obfuscation layers to evade detection. Once installed, it logs keystrokes, captures screenshots, and steals clipboard data, compromising user credentials and sensitive information. 

## Story 9: Venture Capital Firm Insight Partners Suffers Cyberattack

New York-based venture capital and private equity firm Insight Partners has disclosed a cyberattack on its systems. The breach, resulting from a sophisticated social engineering attack on January 16, 2025, prompted the firm to engage third-party cybersecurity experts and notify law enforcement. While the investigation is ongoing, there is no evidence of continued unauthorized access. 
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
