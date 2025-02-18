from gtts import gTTS
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity News for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries with pauses between stories
summaries = """

**Story 1: Hackers Exploit Microsoft Teams Meeting Invites for Phishing Attacks**

Cybercriminals, identified as the Storm-2372 group, are conducting sophisticated phishing attacks by abusing Microsoft Teams meeting invites. Active since August 2024, these attackers impersonate officials from organizations like the U.S. Department of State and the European Parliament. They lure victims into authenticating through Microsoft's Device Code workflow, enabling unauthorized access to Microsoft 3 6 5 accounts without requiring passwords or multi-factor authentication. This method leverages legitimate Microsoft infrastructure, making detection challenging. 

**Story 2: Russian Threat Actors Target Microsoft 3 6 5 Accounts via Device Code Authentication**

Security researchers have uncovered multiple Russian threat actors conducting social engineering and spear-phishing campaigns aimed at compromising Microsoft 3 6 5 accounts. These groups exploit the Device Code Authentication feature, directing victims to legitimate Microsoft URLs and prompting them to enter device codes. Once authenticated, attackers gain unauthorized access to accounts, bypassing traditional security measures. The campaigns have proven highly effective, surpassing traditional phishing methods in success rates. 

**Story 3: Ransomware-as-a-Service Fuels Fourfold Increase in Attacks**

The rise of Ransomware-as-a-Service (RaaS) platforms has led to a significant increase in ransomware attacks, with incidents quadrupling over the past year. These platforms enable even low-skilled attackers to launch sophisticated campaigns by providing ready-made ransomware tools. The growing sophistication, agility, and evasive nature of these attacks pose substantial challenges to cybersecurity defenses. Organizations are urged to adopt advanced security measures to combat this escalating threat. 

**Story 4: CISA Issues 20 Advisories on Industrial Control System Vulnerabilities**

The Cybersecurity and Infrastructure Security Agency (CISA) has released twenty new advisories addressing critical vulnerabilities in Industrial Control Systems (ICS). The advisories cover products from vendors such as Siemens, ORing, mySCADA, and Mitsubishi Electric. Each advisory details specific vulnerabilities that could allow attackers to disrupt operations, gain unauthorized access, or execute malicious code. Organizations using these systems are strongly advised to apply recommended patches and mitigation strategies to secure their infrastructure. 

**Story 5: EarthKapre APT Employs Weaponized PDFs to Compromise Windows Systems**

The advanced persistent threat group known as EarthKapre, also referred to as RedCurl, has been targeting private-sector organizations, especially in the legal sector. They employ phishing emails disguised as job applications containing malicious PDF attachments. These PDFs lead victims to download files that, once executed, initiate a multi-stage malware infection. The attack chain includes sophisticated techniques like DLL side-loading and multi-stage encryption, aiming to exfiltrate sensitive data and conduct corporate espionage. 

**Story 6: XELERA Ransomware Targets Job Seekers with Malicious Word Documents**

A new ransomware campaign dubbed "XELERA" is specifically targeting job seekers by distributing malicious Word documents disguised as job offers from reputable organizations. Upon opening these documents, an infection chain is triggered, leading to the deployment of ransomware that encrypts the victim's data. The attackers demand a ransom in cryptocurrency for data recovery. This campaign underscores the importance of vigilance and caution when handling unsolicited job offers and attachments. 

**Story 7: 'whoAMI' Attack Exploits AWS AMI Name Confusion for Remote Code Execution**

Cybersecurity researchers have identified a novel attack, termed "whoAMI," that exploits name confusion in Amazon Web Services (AWS) Amazon Machine Images (AMIs). Attackers publish malicious AMIs with names matching legitimate ones. If developers do not specify the owner when searching for AMIs, they might inadvertently use the malicious image. This can grant attackers remote code execution within the victim's AWS environment. AWS has addressed this issue, and users are advised to specify image owners explicitly to prevent such attacks. 
"""

# Combine the intro and summaries
full_text = f"{intro_text}\n\n{summaries}"

# Construct the output filename
output_file = f"E:\\GIT\\djbsec.github.io\\assets\\audio\\news\\CyberSecurityNews-{output_date}.mp3"

# Create the audio file
try:
    print("Generating audio file...")
    audio = gTTS(text=full_text, lang='en', slow=False)
    audio.save(output_file)
    print(f"Audio file successfully created: {output_file}")
except Exception as e:
    print(f"An error occurred while generating the audio file: {e}")
