# RocketSploit

**Overview**: RocketSploit is a Capture The Flag (CTF) website containing multiple web-based challenges with intentionally vulnerable code. Players are tasked with finding hidden flags by exploiting security flaws.

## Mission Statement
Welcome to **A.S.T.R.A.** (Astronomical Security & Technological Recon Agency). You've detected anomalous traffic on a routine rocket ship information portal. Your objective: investigate and neutralize potential threats within the website. The operation starts now—good luck!

## Challenges

### Beginner Challenges

#### Flag #1
- **Prompt**: Your first task at ASTRA is to investigate the source code for any information that might have been inadvertently left behind.
- **Answer**: The flag is hidden in 3 parts across the HTML, CSS, and JavaScript files.

#### Flag #2
- **Prompt**: While exploring the website, you notice suspicious network traffic and think it might be a good idea to investigate.
- **Answer**: The flag is hidden in the HTTP header.

#### Flag #3
- **Prompt**: ASTRA gives out very delicious cookies to all of its employees. Maybe you should grab one.
- **Answer**: The flag is a base64 encoded cookie.

### Medium Challenges

#### Flag #4
- **Prompt**: ASTRA received an anonymous POST on RocketGram, indicating that the website is just a decoy for the actual Cyberware Blackmarket.
- **Answer**: Send a POST request to the server using the JavaScript Console, Python, or BurpSuite.

#### Flag #5
- **Prompt**: Congratulations, you've made it onto the site but are now faced with a login page preventing further access. You recall that the RocketGram POST mentioned a user named "CryptoMongoose."
- **Answer**: Use SQL injection with the provided username to gain access.

### Hard Challenges

#### Flag #6
- **Prompt**: 
- **Answer**: Use cross-site scripting (XSS) to steal the admin's cookie and gain access to another page.

#### Flag #7
- **Prompt**: Now that you're in the site, it's time to disrupt their operations. You need to get access to the `vault.txt` file. Hint: You notice something weird every time you switch to the home tab on the website.
- **Answer**: The home tab links to a vulnerable intermediate page that uses a query string to determine which page to open. Instead of `jumbo.html`, type `../../vault.txt`.

## Disclaimer
This repository is not actively managed and is for demonstrative purposes only. Deploy at your own risk. The website is intended for educational purposes and should not be used in a production environment.

## Future Plans
- Add a man-in-the-middle attack scenario.
- Include multiple cookies; the user must figure out which one contains the flag.
- Simplify directory traversal challenges.
- Temporarily switch to a blank black page before redirecting to the home page.
