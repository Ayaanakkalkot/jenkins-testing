import re
import dns.resolver

def is_valid_email_with_mx(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False

    domain = email.split('@')[1]

    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except Exception:
        return False

if __name__ == "__main__":
    with open('emails.txt') as f:
        emails = [line.strip() for line in f.readlines()]

    for email in emails:
        print(f"{email} -> {'Valid' if is_valid_email_with_mx(email) else 'Invalid'}")
