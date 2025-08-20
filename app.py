import os
import sqlite3
import urllib.parse

# High Vulnerability: SQL Injection
def vulnerable_sql_injection(user_input):
    # Vulnerable to SQL Injection
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
    return cursor.fetchall()

# Medium Vulnerability: Insecure URL Handling
def insecure_url_handling(url):
    # Vulnerable to open redirects (insecure URL parsing)
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.netloc:
        print(f"Redirecting to {url}")
    else:
        print("Invalid URL")

# Low Vulnerability: Hardcoded sensitive data
def hardcoded_credentials():
    # Vulnerable to leaking sensitive data
    username = "admin"
    password = "password123"  # Hardcoded password
    print(f"Username: {username}, Password: [REDACTED]")

if __name__ == "__main__":
    # Example of high vulnerability: SQL Injection
    user_input = "admin' OR '1'='1"  # Simulate an SQL injection attack
    print(vulnerable_sql_injection(user_input))
    
    # Example of medium vulnerability: Insecure URL Handling
    url = "http://example.com/redirect?url=http://evil.com"
    insecure_url_handling(url)
    
    # Example of low vulnerability: Hardcoded sensitive data
    hardcoded_credentials()
