# ⌨️​ Keylogger

This project is an advanced, stealth-focused keylogger designed for persistent execution and covert data exfiltration. It mimics real-world APT (Advanced Persistent Threat) techniques to demonstrate how malicious actors can maintain access to a compromised system while minimizing detection.

The keylogger operates silently in the background, capturing user keystrokes and transmitting them in real-time to a remote recipient via email. It is engineered for stealth, persistence, and automation, making it an ideal tool for cybersecurity research, adversary simulation, and penetration testing.

# 🔑​ Key Features

🔹 Persistent Execution & Evasion

- Automatically launches on system startup by modifying the Windows registry.

- Disguised as a legitimate system process (services.exe) to blend in with standard Windows services.

- No user notifications, GUI, or visible logs—ensuring minimal footprint.

🔹 Real-Time Keylogging & Exfiltration

- Captures every keystroke and stores them in memory without writing logs to disk.

- Sends timed reports via email (default: every 20 seconds) only when user activity is detected.

- Supports customizable reporting intervals and SMTP configurations for exfiltration flexibility.

🔹 Minimal Privilege Requirements

- Can be executed by non-administrator users, making it effective in real-world attack scenarios.

- No additional dependencies required for deployment—compiled into a standalone executable.

🔹 Easy Deployment & Social Engineering Compatibility

- The executable can be delivered via phishing emails or social engineering tactics.

- Compatible with Windows 7, 8, 10, and 11 (tested on multiple environments).

- Can be further obfuscated and packed to avoid detection by traditional antivirus solutions.

# 🔧​ Development & Persistence

The keylogger was initially developed in Python and later converted into an executable (services.exe) for seamless deployment. It leverages Windows registry modifications to ensure automatic execution after reboot, requiring no user intervention.

The executable is designed to appear as a legitimate Windows system process, reducing suspicion and detection by naive users or non-technical staff.

# 📧​ Exfiltration Mechanism

The collected keystrokes are sent via SMTP email transmission, ensuring continuous exfiltration without storing logs locally. The email configuration supports:

- Custom SMTP servers (default: Outlook, but configurable for Gmail or private mail servers).

- Adjustable sending intervals for stealth and efficiency.

- Secure authentication methods (app passwords recommended for Gmail accounts).

# 🔎 Evasion Techniques

To minimize detection, the program:

- Runs in the background with no visible windows, pop-ups, or logs.

- Uses a system-like process name (services.exe) to avoid immediate suspicion.

- Can be further obfuscated with tools like PyInstaller encryption or ResourceHacker for icon customization.

# 🔒​ Security & Privacy Considerations

This project was developed for cybersecurity research, penetration testing, and red team exercises. It provides insights into how attackers can maintain access to a system and exfiltrate data while avoiding detection.

🔸 Defensive Strategies & Detection Methods

- Behavioral analysis of registry modifications and persistence mechanisms.

- Email traffic monitoring to detect abnormal outbound transmissions.

- Threat hunting for unsigned executables mimicking system processes.

🔸 Mitigation Techniques

- Implementing stricter execution policies via Windows Defender Application Control (WDAC).

- Monitoring registry changes for unauthorized persistence entries.

- Using behavior-based antivirus solutions that flag keylogging activities.

# 📋​ Project Requirements & Compliance

The project meets the following security research requirements:

✅ Silent Installation

- Can be deployed without the user’s awareness.

- Does not require administrative privileges for execution.

✅ Persistence & Stealth

- Automatically resumes operation after system reboot.

- Mimics legitimate processes to avoid detection.

✅ Keylogging & Data Exfiltration

- Records keystrokes and transmits them remotely.

- Does not store logs locally, reducing forensic traceability.

✅ Covert Information Transmission

- Sends logs discreetly via email to a designated address.

- Supports encrypted SMTP connections to enhance stealth.

✅ Anti-Detection & Anonymity Measures

Attackers can remain anonymous using:

- Tor network for exfiltration.

- Temporary email addresses for receiving logs.

- Public Wi-Fi hotspots to avoid network tracking.

✅ Windows Compatibility

- Fully operational on Windows 7, 8, 10, and 11.

- Tested on both updated and outdated Windows versions to ensure functionality.

# 📝​ Conclusion

The Stealth Keylogger is a fully operational tool designed to demonstrate keylogging, persistence, and covert exfiltration techniques. It provides valuable insights into adversarial tactics, helping security professionals improve threat detection, response strategies, and endpoint security measures.

