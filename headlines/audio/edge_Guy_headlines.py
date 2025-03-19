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


Story 1. Google Acquires Wiz for Record $32 Billion in Largest Cybersecurity Deal Ever
Google has announced the acquisition of cloud security firm Wiz for a record-breaking $32 billion, making it the largest cybersecurity deal in history. Wiz, known for its advanced cloud-native security platform, helps companies identify and mitigate vulnerabilities across multi-cloud environments. This acquisition strengthens Google Cloud’s security offerings and positions it as a leading player in the cloud security market. Analysts expect this move to intensify competition with Microsoft and AWS in the cybersecurity space.  


---

Story 2. Scammers Distribute Ad Fraud Apps with 60 Million Downloads on Google Play
Security researchers have uncovered a large-scale ad fraud scheme involving dozens of malicious Android apps with over 60 million downloads from Google Play. These apps secretly performed ad fraud in the background, draining user data and device resources while generating illegal revenue for scammers. Google has since removed the fraudulent apps, but many users remain affected. Experts advise Android users to carefully review app permissions and avoid downloading unknown applications.  


---

Story 3. Critical Vulnerability in AMI MegaRAC BMC Allows Server Takeover
A newly disclosed vulnerability in AMI MegaRAC Baseboard Management Controllers (BMC) could allow attackers to take over servers remotely. This critical flaw affects data centers and cloud infrastructure, posing a serious risk to enterprises using the vulnerable technology. Attackers could exploit the flaw to gain root access, disrupt operations, or install persistent backdoors. Organizations are urged to patch affected systems immediately to mitigate the risk of exploitation.  


---

Story 4. InfoStealer Malware Attacks Surged in 2024, Flashpoint Report Finds
A new report from Flashpoint reveals that infostealer malware attacks surged throughout 2024, with cybercriminals increasingly targeting login credentials, financial data, and personal information. These malware strains, often delivered via phishing campaigns and malicious downloads, have been a primary driver of account takeovers and identity theft. The report highlights how the dark web marketplace for stolen data is fueling cybercrime. Security experts recommend enabling multi-factor authentication (MFA) and using endpoint detection tools to defend against these threats.  


---

Story 5. Nation-State Actors and Cybercrime Gangs Abusing Malicious LNK Files
Threat intelligence reports indicate that both state-sponsored hackers and cybercriminal gangs are increasingly using malicious LNK (Windows shortcut) files to distribute malware. These files, often disguised as legitimate documents, enable attackers to execute code remotely, steal sensitive information, and establish persistence on compromised systems. Recent campaigns have leveraged this technique for espionage, ransomware, and data exfiltration. Organizations are advised to restrict LNK execution in email attachments and implement strict security controls.  


---

Story 6. Black Basta Ransomware Gang’s Leaked Chat Logs Reveal Ties to Russian Officials
Leaked internal chat logs from the Black Basta ransomware gang suggest connections to Russian government officials. The logs reveal discussions about attack strategies, ransom negotiations, and possible state protection for cybercriminal activities. If confirmed, these findings further link ransomware operations to Russian intelligence services. This leak may provide valuable intelligence for law enforcement agencies investigating ransomware networks.  


---

Story 7. 8-Year-Old Windows Shortcut Zero-Day Exploited in Recent Attacks
A newly discovered cyberattack campaign is exploiting an 8-year-old zero-day vulnerability in Windows shortcut (LNK) files. Despite Microsoft’s past attempts to mitigate such threats, attackers have found new ways to weaponize the flaw, allowing them to execute malicious code with minimal user interaction. The vulnerability is being actively exploited in targeted attacks against businesses and government entities. Security researchers recommend disabling shortcut execution for untrusted sources and applying available patches.  


---

Story 8. Bybit Hack: A Sophisticated Multi-Stage Attack Compromised Cryptocurrency Exchange
The recent cyberattack on the Bybit cryptocurrency exchange involved a sophisticated multi-stage intrusion that allowed attackers to steal millions in digital assets. Hackers leveraged social engineering, zero-day exploits, and advanced obfuscation techniques to bypass security measures. Bybit has since tightened its security protocols, but the breach highlights the growing risks for crypto exchanges. Users are advised to enable two-factor authentication and use hardware wallets for enhanced security.  


---

Story 9. ChatGPT SSRF Bug Becomes a Favorite Attack Vector for Hackers
Hackers have quickly adopted a newly discovered Server-Side Request Forgery (SSRF) vulnerability in ChatGPT, exploiting it in real-world attacks. The flaw, CVE-2025-XXXX, allows attackers to manipulate AI-generated responses and access restricted internal services. Cybercriminals are using this technique to extract sensitive data and bypass security measures in AI-integrated platforms. OpenAI and security experts are working on a fix, but organizations using AI-powered applications should monitor for suspicious activity.  




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
