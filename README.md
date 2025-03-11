# email-finder
This script utilizes the Hunter.io API to find the full name and company associated with a given email address. It reads a list of emails from a file and retrieves the corresponding details.

## Features
- Uses the Hunter.io API to find associated names and companies for email addresses.
- Reads emails from a text file.
- Outputs results in a structured format.

## Requirements
- Python 3.x
- `requests` library
- A valid Hunter.io API key

## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
1. Replace `YOUR_HUNTER_API_KEY` in `email_finder.py` with your actual Hunter.io API key.
2. Place a list of email addresses in a `.txt` file (e.g., `emails.txt`).
3. Update the `file_path` variable in `email_finder.py` to the correct file path.
4. Run the script:
   ```sh
   python email_finder.py
   ```

## File Format
The script expects a plain text file with one email address per line, for example:
```
john.doe@example.com
jane.smith@company.com
```

## Notes
- Ensure you have a valid Hunter.io API key.
- The script currently has a hardcoded API request and should be updated for flexibility.

## License
This project is available for personal and educational use. Please credit the original developer.

## Disclaimer
Usage of this script should comply with Hunter.io's API terms and any applicable privacy laws.

