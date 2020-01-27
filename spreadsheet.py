import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet(object):

    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'], scope)
        self.gs = gspread.authorize(credentials)

    def open_sheet(self, filename):
        self.sheet = self.gs.open(filename).sheet1

    def get_col_length(self, row=1):
        return len(self.sheet.col_values(row))

    def update_column(self, line, values):
        cells = self.sheet.range(line, 1, line, len(values))
        for i in range(len(cells)):
            cells[i].value = values[i]
            self.sheet.update_cells(cells)
