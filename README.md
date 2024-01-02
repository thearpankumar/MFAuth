# Multi-Factor Authentication [MFA] Implementation

The following project is the Implementation of Multi-Factor Authentication [MFA] as a part of Team Centinals SRM.

Notion: [Notion Page for Project Report](https://deadgawk.notion.site/Multi-Factor-Authentication-MFA-f8b7b4db6fc0451da2f8170b30277636?pvs=4)

## Overview

This project focuses on implementing Multi-Factor Authentication (MFA) using various authentication factors, with a specific emphasis on Time-Based One-Time Passwords (TOTP). The goal is to enhance the security of user authentication by combining multiple factors, making unauthorized access more challenging.

# Tools and Software Used

- **Node.js:** JavaScript runtime for server-side development.
- **npm:** Package manager for Node.js packages.
- **JavaScript:** Programming language for both front-end and back-end development.
- **Firebase:** Web front-end application platform.
- **Speakeasy:** Library for implementing Time-Based One-Time Passwords (TOTP).
- **JWT (JSON Web Tokens):** Used for user authentication.
- **Insomnia:** Building, designing, testing better APIs through spec-first development driven by an APIOps CI/CD pipelines.
- **HOTP:** HMAC-based One-Time Password
- **OAuth:** Framework for secure authorization of third-party applications.
- **RFC 6238** Internet Engineering Task Force (IETF) standard defining the Time-Based One-Time Password (TOTP) algorithm.
- **CSPRNG** A type of random number generator designed for cryptographic use, ensuring unpredictability and resistance to prediction or reproduction.


## Install

    
    git clone https://github.com/Gaoh19/MFAuth.git
    cd MFAuth
  
### TOTP

    cd ImplementTOTP

**For JavaScript TOTP:**
    
    npm install
    npm run dev

Use Insomia for testing Auth.

**For Python:**

    python pyTOTP.py

Scan QR using Authenicator application for verification

Thanks
------

Thanks to [Susam][PN] for helping me with TOTP Implementation. I referred to his TOTP implementation at [https://github.com/susam/mintotp/blob/main/mintotp.py][PNTOTP] while writing my own.

[PN]: https://github.com/susam
[PNTOTP]: https://github.com/susam/mintotp/blob/main/mintotp.py
