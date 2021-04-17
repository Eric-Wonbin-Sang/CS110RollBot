import gspread
import pyperclip
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from Classes import Student, Section, Manager

from General import Constants


def get_manager_list():
    return [
        Manager.Manager("Nihaal", section_id=1),
        Manager.Manager("Eric Sang", section_id=2),
        Manager.Manager("Vinay", section_id=3)
    ]


def get_student_list(main_sheet):
    student_list = []
    for data_dict in main_sheet.get_all_records():
        student_list.append(Student.Student(data_dict))
    return student_list


def get_section_list(student_list):
    section_list = []
    section_dict = {}
    for student in student_list:
        if student.section_id not in section_dict:
            section_dict[student.section_id] = [student]
        else:
            section_dict[student.section_id] += [student]
    for key, value in section_dict.items():
        section_list.append(Section.Section(key, value))
    return section_list


def main():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(Constants.api_json_path, scope)

    client = gspread.authorize(creds)
    sheet = client.open('CS110 Recitation Role Sheet')
    main_sheet = sheet.get_worksheet(0)

    manager_list = get_manager_list()
    student_list = get_student_list(main_sheet)
    section_list = get_section_list(student_list)

    for student in student_list:
        if student.lab == 2:
            print(student)


if __name__ == '__main__':
    main()

