from gtts import gTTS
from datetime import datetime

# Get today's date in the desired format
current_date = datetime.now().strftime("%B %d, %Y")  # Example: January 17, 2025
output_date = datetime.now().strftime("%m-%d-%Y")    # Example: 01-17-2025

# Intro text
intro_text = f"Welcome to the CyberSecurity stories for {current_date}. Here are today's top cybersecurity headlines."

# Cybersecurity summaries with pauses between stories
summaries = """

We will start with Network Security    

1. Stealthy 'Magic Packet' Malware Targets Juniper VPN Gateways
Researchers have uncovered a sophisticated "magic packet" malware targeting Juniper VPN gateways, exploiting undocumented features to maintain persistent and covert access. The malware uses specially crafted packets to activate malicious capabilities, avoiding traditional detection methods. This advanced threat could allow attackers to compromise sensitive network communications. Organizations using Juniper VPNs are urged to monitor network traffic for anomalies and apply available patches.... 

...

2. SonicWall Critical Bug
A critical vulnerability in SonicWall appliances impacts the SSL-VPN and web management interfaces, tracked as CVE-2025-XXXX. This flaw allows remote attackers to execute arbitrary code without authentication, making it a significant security concern. SonicWall has released a patch to address the issue, and administrators are strongly advised to update affected devices immediately to prevent exploitation.

... 

3. QNAP Fixes Six rsync Vulnerabilities in HBS NAS Backup App
QNAP has resolved six critical vulnerabilities in the Hybrid Backup Sync (HBS) app used for NAS devices. The flaws include command injection, privilege escalation, and directory traversal vulnerabilities, potentially allowing attackers to compromise backups or access sensitive data. QNAP advises users to install the latest HBS updates to mitigate risks.

... 

4. Critical Palo Alto Firewall Vulnerabilities
Multiple vulnerabilities have been disclosed in Palo Alto Networks firewalls, including a critical remote code execution (RCE) flaw with a CVSS score of 9.8. Attackers can exploit these issues to bypass authentication, execute arbitrary code, and gain control over systems. Organizations using Palo Alto firewalls should immediately apply patches to safeguard their networks.

... 

In Phishing News - - - 

1. Tycoon 2FA Phishing Kit Using Specially Crafted Code
A new phishing kit called "Tycoon" is leveraging adversary-in-the-middle (AiTM) techniques to bypass two-factor authentication (2FA). By intercepting credentials and session tokens, this kit enables attackers to compromise accounts with enhanced security measures. Organizations are advised to adopt FIDO2-based MFA solutions and educate users about phishing risks.

... 

2. Fake Microsoft Teams Page Drops Malware on Windows
Cybercriminals are using a fake Microsoft Teams login page to distribute malware on Windows systems. Victims are lured into downloading malicious files disguised as login tools, leading to credential theft and unauthorized access. Employees should verify URLs, avoid downloading suspicious files, and use official Microsoft apps for secure access.

... 

In our last topic for the day lets look at Ransomware & Compromise

1. FBI: North Korean IT Workers Steal Source Code to Extort Employers
The FBI warns about North Korean IT workers infiltrating international companies under fake identities. These actors gain access to source code repositories and critical systems, later using this access to extort employers with threats of data exposure. Businesses are urged to implement thorough vetting processes and monitor for suspicious activities within their teams.

...

2. Ransomware Attacking VMware ESXi Hosts
A ransomware campaign is targeting VMware ESXi hosts, exploiting unpatched vulnerabilities to encrypt virtual machines. This approach can disrupt entire infrastructures, demanding ransoms for decryption keys. Administrators should ensure ESXi systems are fully patched and utilize immutable backups to mitigate potential damage.

...

3. $4.88M Was the Average Cost of a Data Breach in 2024
A 2024 report reveals the average cost of a data breach was an astounding $4.88 million, highlighting the growing financial and reputational risks of cyberattacks. The report emphasizes the importance of employee training, robust incident response plans, and advanced threat detection tools in reducing breach costs and impacts.
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
