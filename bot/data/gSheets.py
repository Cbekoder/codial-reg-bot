import gspread
from google.oauth2.service_account import Credentials
from gspread import SpreadsheetNotFound

SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file('codial-gsheet.json', scopes=SCOPE)
client = gspread.authorize(creds)

spreadsheet = client.open("codial-registration")
worksheet = spreadsheet.sheet1

# spreadsheet.share('cbekoder@gmail.com', perm_type='user', role='writer')

def write_to_google_sheets(user_data):
    worksheet.append_row(user_data)

