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

Story 1: Salt Typhoon Deploys 'JumbledPath' Malware to Spy on U.S. Telecom Providers
The Chinese state-sponsored hacking group known as Salt Typhoon has been identified deploying a custom malware strain dubbed 'JumbledPath' to infiltrate U.S. telecommunications providers. This sophisticated malware enables the group to intercept communications and exfiltrate sensitive data, posing significant threats to national security and critical infrastructure. The campaign underscores the persistent vulnerabilities within the telecom sector and the advanced capabilities of nation-state actors in cyber espionage. 

Story 2: PCI DSS 4.0 Mandates DMARC Implementation by March 31
The Payment Card Industry Data Security Standard (PCI DSS) version 4.0 has introduced a new requirement for organizations to implement Domain-based Message Authentication, Reporting, and Conformance (DMARC) by March 31. This mandate aims to enhance email security by preventing domain spoofing and phishing attacks, thereby protecting cardholder data from unauthorized access. Organizations are urged to configure DMARC policies appropriately to comply with the standard and strengthen their cybersecurity posture. 

Story 3: Surge in Fake CAPTCHA Attacks Exploiting User Trust
Cybersecurity experts have observed a significant increase in attacks utilizing fake CAPTCHA verifications to deceive users into clicking on malicious links or downloading malware. These deceptive tactics exploit the common trust users place in CAPTCHA systems, leading to unauthorized access and data breaches. Users are advised to remain vigilant and verify the authenticity of CAPTCHA prompts, especially when encountered on unfamiliar websites. 

Story 4: Evolving Mobile Phishing Threats Exploit Platform Vulnerabilities
Recent research indicates that mobile phishing attacks are becoming increasingly sophisticated, exploiting specific vulnerabilities inherent to mobile platforms. Attackers are leveraging SMS, QR codes, and mobile-optimized websites to deliver phishing content, making detection more challenging. The reduced screen size and limited URL visibility on mobile devices contribute to the success of these attacks, emphasizing the need for enhanced mobile security measures. 

Story 5: Proof-of-Concept Exploit Released for Ivanti Endpoint Manager Vulnerabilities
A proof-of-concept (PoC) exploit has been publicly released for multiple critical vulnerabilities in Ivanti Endpoint Manager. These flaws allow unauthenticated attackers to execute arbitrary code and gain control over affected systems. Organizations utilizing this platform are strongly advised to apply the available patches immediately to mitigate potential exploitation risks. 

Story 6: Internal Chat Logs of Black Basta Ransomware Gang Leaked
Internal chat logs belonging to the Black Basta ransomware group have been leaked online, providing insights into the gang's operations, negotiation tactics, and organizational structure. The leak, which includes discussions about ransom demands and victim interactions, offers a rare glimpse into the inner workings of a prominent cybercriminal organization. This exposure could potentially aid law enforcement agencies in their efforts to combat ransomware activities. 

Story 7: Medusa Ransomware Gang Demands $2 Million from UK Health Provider
The Medusa ransomware group has demanded a $2 million ransom from HCRG Care Group, a UK-based private health and social services provider. The attackers claim to have exfiltrated 2.275 terabytes of sensitive data, including personal identification documents and staff records. HCRG is currently investigating the incident and has implemented containment measures to prevent further unauthorized access. 

Story 8: 'Zhong' Malware Exploits AnyDesk to Target Fintech and Cryptocurrency Sectors
A newly identified malware strain, dubbed 'Zhong,' has been observed exploiting the AnyDesk remote desktop tool to infiltrate systems within the fintech and cryptocurrency industries. The malware employs social engineering tactics, such as phishing emails with malicious attachments, to gain initial access. Once inside, it steals credentials and establishes persistent remote access, posing significant risks to financial data security. 

Story 9: DeepSeek Found Sharing User Data with ByteDance
Investigations have revealed that the AI application DeepSeek has been transmitting user data to ByteDance, the parent company of TikTok, without user consent. This unauthorized data sharing raises serious privacy concerns, especially given ByteDance's previous controversies regarding data handling practices. Users are advised to exercise caution and consider removing the DeepSeek app from their devices to protect their personal information. 

Story 10: Citrix NetScaler Vulnerability Allows Unauthorized Command Execution
A high-severity vulnerability has been identified in Citrix NetScaler, potentially allowing authenticated attackers to execute unauthorized commands on affected systems. This flaw, resulting from improper privilege management, could lead to full system compromise if exploited. Administrators are urged to apply the latest patches promptly to secure their networks against potential threats. 

Story 11: APT-C-28 Group Deploys Fileless RokRat Malware in New Cyber Attack
The APT-C-28 threat group, also known as ScarCruft, has launched a new cyber espionage campaign utilizing a fileless version of the RokRat malware. This sophisticated attack involves phishing emails containing malicious LNK files that execute obfuscated PowerShell scripts, enabling the group to steal sensitive information without leaving traditional malware footprints. Organizations are advised to implement advanced threat detection mechanisms to identify and mitigate such stealthy attacks. 


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
