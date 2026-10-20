html
<p align="center">
  <a href="https://t.me/rejerks">
    <img src="https://img.shields.io/badge/Telegram-@rejerks-blue?style=for-the-badge&logo=telegram" alt="Telegram">
  </a>
  <a href="https://t.me/parithings">
    <img src="https://img.shields.io/badge/Telegram-@parithings-blue?style=for-the-badge&logo=telegram" alt="Telegram Group">
  </a>
</p>
Another key point: the Shields.io badge URL must include the complete three components label-message-color, otherwise it will render as a broken image. Your badge URL form

Complete README.md
markdown
# Dad Joke API

<p align="center">
  <a href="https://t.me/rejerks">
    <img src="https://img.shields.io/badge/Telegram-@rejerks-blue?style=for-the-badge&logo=telegram" alt="Telegram">
  </a>
  <a href="https://t.me/parithings">
    <img src="https://img.shields.io/badge/Telegram-@parithings-blue?style=for-the-badge&logo=telegram" alt="Telegram Group">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/wlzbi-exe/dad-joke-api?style=for-the-badge&logo=github" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/wlzbi-exe/dad-joke-api?style=for-the-badge&logo=github" alt="GitHub forks">
  <img src="https://img.shields.io/github/last-commit/wlzbi-exe/dad-joke-api?style=for-the-badge&logo=github" alt="GitHub last commit">
  <img src="https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel" alt="Vercel">
</p>

> A simple, deployable Dad Joke API service that returns random dad jokes via HTTP.

---

## 📖 Overview

This project is a lightweight Dad Joke API. It uses a built-in HTTP server to fetch and return Dad jokes, comes with a simple front-end page, and supports one-click deployment to Vercel via `vercel.json`.

The repository structure is as follows:
dad-joke-api/
├── api/ # HTTP server logic, responsible for fetching and returning jokes
├── public/ # Front-end static page
└── vercel.json # Vercel deployment configuration

text

## ✨ Features

- **Simple and easy to use**: No complex dependencies required; the HTTP server is built-in
- **Ready to use out of the box**: Includes a front-end page for direct access and testing
- **Vercel deployment**: Provides `vercel.json` configuration, one-click deployment to Vercel
- **Lightweight**: Minimal file structure, no redundant modules

## 🚀 Deployment

### Deploy to Vercel

1. Fork this repository
2. Import the repository in [Vercel](https://vercel.com)
3. Vercel will automatically recognize `vercel.json` and complete the deployment

### Run Locally

```bash
git clone https://github.com/wlzbi-exe/dad-joke-api.git
cd dad-joke-api
# Start according to the server startup method in the api directory
Note: The repository currently does not provide a specific startup command or dependency description. You can check the api directory for entry files, or add the startup method yourself.

🛠️ Usage
After starting the service, access the API endpoint to get a random Dad joke. The specific endpoint path depends on the route defined in the api directory.

bash
# Example (the actual path is subject to the code)
curl http://localhost:3000/api/joke
📬 Contact
<p align="center"> <a href="https://t.me/rejerks"> <img src="https://img.shields.io/badge/Telegram-@rejerks-blue?style=for-the-badge&logo=telegram" alt="Telegram"> </a> <a href="https://t.me/parithings"> <img src="https://img.shields.io/badge/Telegram-@parithings-blue?style=for-the-badge&logo=telegram" alt="Telegram Group"> </a> </p>
📄 License
This project currently does not declare a license. For detailed information, please refer to the repository files or contact the author.

text

**Key fix:** All badges have been changed from Markdown syntax to HTML tags (`<a><img></a>`), and the centering is handled by `<p align="center">`. Copy this version to GitHub, and the badges should display and center properly. If they still don't appear, try opening the badge URL directly in your browser to confirm whether the network can access `img.shields.io`.
