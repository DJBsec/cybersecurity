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


Story  1. Phishing-Based Attacks Have Risen 140% Year Over Year
A new report highlights a staggering 140% increase in phishing-based attacks compared to the previous year. Cybercriminals are leveraging advanced social engineering tactics, AI-generated messages, and brand impersonation to trick victims into divulging credentials. The financial sector, healthcare, and government agencies have been among the most targeted. Security experts emphasize the importance of user education, multi-factor authentication (MFA), and improved email filtering to mitigate these growing threats.  

---

Story  2. Attackers Embedding Malicious Word Files Inside PDFs to Evade Detection
Cybercriminals have developed a new attack technique that embeds malicious Microsoft Word files inside PDFs, allowing them to bypass traditional security filters. When victims open the seemingly harmless PDF, the hidden Word document automatically executes malware, granting attackers access to the system. This method effectively evades email security solutions that scan for standalone Word file threats. Users are advised to be cautious when opening unexpected PDF attachments and keep their software updated.  


---

Story  3. Threat Actors Exploiting Legacy Drivers to Evade Security Tools
Hackers are increasingly exploiting outdated and vulnerable drivers to bypass modern security defenses. Known as Bring Your Own Vulnerable Driver (BYOVD) attacks, this technique allows cybercriminals to disable endpoint detection and response (EDR) systems, gaining deeper access to compromised networks. Security researchers warn that legacy drivers, even if digitally signed, pose a significant threat if left unpatched. Organizations should enforce strict driver policies and use allowlists to prevent unauthorized installations.  


---

Story  4. Microsoft Exchange Online Outage Disrupts Outlook Web Users
Microsoft Exchange Online experienced a major outage, leaving Outlook Web users unable to access their emails. The issue, which lasted several hours, affected customers worldwide, with Microsoft attributing it to an unexpected infrastructure issue. The downtime frustrated businesses and individuals relying on cloud-based email services for daily operations. Microsoft has since restored service and is investigating the root cause to prevent future incidents.  


---

Story  5. Critical Fortinet Vulnerability Draws Fresh Attention from Attackers
A critical vulnerability in Fortinet’s network security devices has gained renewed interest from cybercriminals looking to exploit unpatched systems. The flaw, which allows remote code execution, could enable attackers to take full control of affected devices. Security experts warn that many organizations have yet to apply the necessary patches, leaving them vulnerable to potential breaches. Fortinet urges all users to update their devices immediately and monitor for suspicious activity.  

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
