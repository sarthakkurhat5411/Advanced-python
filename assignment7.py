import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

text = """
Contact us at support@example.com
or rahul_23@gmail.com
You can also email newsletter+promo@my-site.org
"""

emails = re.findall(EMAIL_PATTERN, text)

print("Email addresses found:")
for email in emails:
    print(email)

print("Total emails:", len(emails))