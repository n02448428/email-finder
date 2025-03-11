import requests

# Input Hunter.io API key here
HUNTER_API_KEY = 'YOUR_HUNTER_API_KEY'

# Function to find full name and company for an email
def find_name_and_company(email):
    url = f"https://api.hunter.io/v2/email-finder"
    params = {
        "email": email,
        "api_key": "https://api.hunter.io/v2/email-finder?domain=reddit.com&first_name=Alexis&last_name=Ohanian&api_key=4546d03828668b713ec77c9d7324bccdcdf8d4e3"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data.get("data"):
        full_name = data["data"].get("first_name", '') + " " + data["data"].get("last_name", '')
        company = data["data"].get("organization", '')
        return full_name, company
    else:
        return None, None

# Function to read emails from a .txt file
def read_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file.readlines()]
    return emails

# Path to your .txt file with emails
file_path = 'emails.csv'

# Get emails from the file
emails = read_emails_from_file(file_path)

# Get full names and companies for each email
for email in emails:
    full_name, company = find_name_and_company(email)
    if full_name and company:
        print(f"Email: {email}\nFull Name: {full_name}\nCompany: {company}\n")
    else:
        print(f"Email: {email} - No data found.\n")
