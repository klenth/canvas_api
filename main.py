import json
from canvas_api import CanvasContext
from canvas_api.model import *

def get_context():
    credentials = None
    with open('canvas_credentials.json', 'r') as f:
        credentials = json.load(f)
    return CanvasContext(**credentials)

def main():
    with get_context() as cc:
        courses = cc.course_list(include=['term', 'total_students', 'syllabus_body'])
        print(f'{len(courses)} courses downloaded:')
        print(repr(courses))
        for course in courses:
            print(repr(course.as_dict(include_extra_fields=True)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
