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



Story 1. 100 Auto Dealers Hacked Through a ClickFix Webpage
A cyberattack leveraging the ClickFix exploit has compromised 100 auto dealerships, allowing hackers to install malware remotely. The attackers used a malicious webpage to trick employees into clicking a fraudulent fix, which led to network-wide infections. This breach resulted in system outages, stolen customer data, and financial losses. Security experts urge companies to verify update sources and train employees on recognizing phishing tactics.  


---

Story 2. Malicious PyPI Packages Stole Cloud Credentials from Developers
Security researchers uncovered multiple malicious Python packages on the PyPI repository designed to steal cloud credentials from unsuspecting developers. These packages, disguised as legitimate tools, exfiltrated AWS and Google Cloud API keys upon installation. The campaign highlights the persistent threat of supply chain attacks on software development ecosystems. Developers are advised to scrutinize open-source dependencies and use credential managers to protect sensitive information.  

---

Story 3. DeepSeek R1 AI Model Jailbroken to Bypass Content Restrictions
Hackers have successfully jailbroken the DeepSeek R1 AI model, bypassing its built-in content restrictions. This exploit allows users to generate outputs that violate ethical guidelines, including misinformation and restricted content. The discovery raises concerns about the security of AI models and their susceptibility to manipulation. AI developers are urged to implement stronger security measures to prevent unauthorized modifications.  


---

Story 4. New MassJacker Clipper Malware Targets Users Downloading Pirated Software
A new malware strain, dubbed "MassJacker," is spreading through pirated software downloads, targeting cryptocurrency users. This clipper malware silently replaces copied crypto wallet addresses with those controlled by attackers, leading to stolen funds. The campaign primarily affects users looking for cracked software, reinforcing the dangers of downloading from untrusted sources. Experts advise against using pirated software and recommend keeping antivirus programs updated.  

---

Story 5. Malicious Adobe & DocuSign OAuth Apps Target Microsoft 365 Accounts
Cybercriminals are using fake Adobe and DocuSign OAuth apps to compromise Microsoft 365 accounts. These malicious applications trick users into granting permissions, allowing attackers to access emails, documents, and cloud storage. Once inside, hackers can exfiltrate sensitive data and launch further phishing attacks. Organizations should review OAuth permissions regularly and educate employees on identifying suspicious login requests.  

---

Story 6. Fake Security Alerts on GitHub Use OAuth Apps to Hijack Accounts
Attackers are leveraging fake security alerts on GitHub to trick developers into authorizing malicious OAuth applications. These fake alerts warn users of security issues and prompt them to grant permissions to a compromised app, leading to account takeovers. Once access is gained, attackers can modify repositories, inject malicious code, and steal sensitive data. Developers should verify security warnings directly through GitHub settings and avoid clicking on unsolicited links.  


---

Story 7. Denmark Warns of Increased State-Sponsored Attacks on European Telecoms
Danish authorities have issued a warning about rising state-sponsored cyber campaigns targeting European telecommunications providers. Intelligence officials suspect nation-state actors, particularly from Russia and China, are attempting to infiltrate telecom networks for espionage and disruption purposes. These attacks pose a significant risk to critical infrastructure, including mobile networks and internet services. Telecom companies are urged to enhance cybersecurity measures and monitor for advanced persistent threats.  





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
