import os
import shutil
from openpyxl import load_workbook

parent_directory = "/Users/josetiznado/Documents"
base_directory = "/Users/josetiznado/Desktop/Job_Projects"
target_directory = ""

def move_file(file):
    global target_directory
    file_prefix = str(file)[:4]
    target_directory = f'{base_directory}/{file_prefix}/Purchasing/MTRs'

    if os.path.isdir(target_directory):
        os.chdir(target_directory)

    shutil.move(file_path, target_directory)

def create_hyperlink(file_path, file_name):
    spreadsheet = f'{os.path.dirname(target_directory)}/Hyperlinks.xlsx'
    wb = load_workbook(spreadsheet)
    sheet = wb.active

    for cell in sheet['A']:
        if cell.value == os.path.splitext(file_name)[0]:
            sheet.cell(row = cell.row, column = cell.column).value = '=HYPERLINK("{}", "{}")'.format(file_path, file_name)

    wb.save(spreadsheet)

if __name__ == '__main__':
    files = os.listdir(parent_directory)

    for file in files:
        if file == ".DS_Store":
            continue

        file_path = f'{parent_directory}/{file}'

        if os.path.isdir(file_path):
            continue

        move_file(file)

        new_file_path = f'{target_directory}/{file}'

        create_hyperlink(new_file_path, file)