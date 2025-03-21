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

Story  1. CISA Tags NAKIVO Backup Flaw as Actively Exploited in Attacks  
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has issued an alert regarding an actively exploited vulnerability in NAKIVO Backup & Replication software. The flaw allows attackers to gain unauthorized access to backup environments, potentially leading to data theft or ransomware attacks. Threat actors are targeting unpatched instances to disrupt business continuity and compromise stored backups. Organizations using NAKIVO are strongly advised to apply patches immediately and enhance monitoring for suspicious activity.  


---

Story  2. Ukraine’s Defense Sector Targeted in DarkCrystal RAT Attack  
Cybersecurity researchers have detected a cyberattack campaign targeting Ukraine’s defense sector using the DarkCrystal Remote Access Trojan (RAT). The malware, attributed to Russian-affiliated hackers, enables full system control, credential theft, and espionage. The attack leverages phishing emails and malicious attachments to infiltrate government networks. Security analysts warn that these cyber operations aim to gather intelligence and disrupt Ukraine’s defense efforts.  


---

Story  3. RansomHub Ransomware Uses New "Betruger" Multi-Function Backdoor  
The RansomHub ransomware gang has introduced a new backdoor named "Betruger," enabling advanced persistence and stealth in corporate networks. This multi-function backdoor allows cybercriminals to evade detection while stealing data and deploying ransomware. Security researchers note that RansomHub is using more sophisticated tactics, making it harder for organizations to defend against attacks. Experts advise businesses to strengthen endpoint protection and implement proactive threat-hunting measures.  


---

Story  4. Veeam Faces Criticism Over Response to Critical Vulnerability  
Veeam, a leading backup and disaster recovery provider, is facing backlash for its delayed response to a critical vulnerability in its software. Security researchers and industry experts argue that the company failed to act swiftly in addressing the flaw, leaving many organizations exposed to cyber threats. The vulnerability allows unauthorized access to backup environments, making it a prime target for ransomware groups. Users are urged to apply security patches immediately and monitor for suspicious activity.  


---

Story  5. Is It Time to Retire One-Off Pen Tests for Continuous Security Testing?  
Cybersecurity experts are questioning the effectiveness of traditional one-time penetration testing in today’s evolving threat landscape. With cyber threats constantly changing, a shift toward continuous security testing is being advocated to provide real-time insights into vulnerabilities. Continuous testing enables organizations to detect and address weaknesses before attackers can exploit them. Many companies are now integrating automated security solutions and red teaming exercises to enhance their security posture.  


---

Story  6. Brand Impersonation Accounts for 51% of Browser-Based Phishing Attacks  
A new study reveals that over half of browser-based phishing attacks rely on brand impersonation, tricking users into believing they are interacting with legitimate companies. Cybercriminals create fake login pages for services like Microsoft 365, PayPal, and banking platforms to steal credentials. These attacks exploit browser vulnerabilities and evade traditional email security filters. Users are urged to verify URLs carefully and enable multi-factor authentication (MFA) to protect their accounts.  


---

Story  7. New Steganographic Malware Hides Malicious Code in JPEG Files  
A newly discovered malware strain is using steganography to embed malicious payloads inside JPEG image files. This technique allows hackers to evade security tools by hiding malware within seemingly harmless images. Once opened, the malware executes commands that steal data or grant attackers remote access. Security experts advise users to be cautious when downloading images from untrusted sources and to keep their security software updated.  


---

Story  8. How Threat Hunters Enrich Indicators of Compromise with Context  
Threat-hunting teams are increasingly focusing on contextualizing Indicators of Compromise (IoCs) to improve cybersecurity defenses. By correlating IoCs with attack patterns, security professionals can detect malicious activity earlier and respond more effectively. Advanced threat intelligence tools now integrate machine learning and automation to enhance detection capabilities. Organizations are encouraged to adopt proactive threat-hunting strategies to stay ahead of cyber threats.  


---

Story  9. How to Protect Your Business from Cyberattacks  
A recent cybersecurity guide highlights key strategies businesses can use to defend against modern cyber threats. Recommendations include implementing zero-trust security models, strengthening endpoint protections, and conducting employee security awareness training. As cybercriminals continue to exploit human and technical vulnerabilities, proactive risk management is essential. Organizations are urged to regularly update security policies and invest in advanced threat detection solutions.  


---

Story  10. Zero-Hour Phishing Attacks Exploiting Browser Vulnerabilities  
A wave of zero-hour phishing attacks is targeting browser vulnerabilities, bypassing traditional security measures. These attacks exploit flaws in web browsers to execute malicious scripts that steal user credentials and session tokens. Cybercriminals are using these techniques to gain access to corporate networks and cloud services. Security professionals advise users to keep browsers updated and enable enhanced phishing protection settings.  


---

Story  11. Chinese "Salt Typhoon" Hackers Exploiting Microsoft Exchange Vulnerabilities  
A Chinese state-sponsored hacking group, dubbed "Salt Typhoon," has been exploiting vulnerabilities in Microsoft Exchange servers to gain persistent access to corporate and government networks. These attacks focus on espionage, data theft, and establishing footholds for future cyber operations. Security researchers warn that unpatched Exchange servers remain prime targets for this threat actor. Organizations are strongly advised to apply security patches and enhance monitoring for unauthorized access attempts.  


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
