def report_format(func):
    def wrapper(*args, **kwargs):
        print("*#*" * 10)
        func(*args, **kwargs)
        print("*#*" * 10)
    return wrapper


class AttendanceReport:
    template = "Attendance Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return f"Template: {self.template}\nTitle: {self.title}\nContent: {self.content}"


@report_format
def display(report):
    print(report)


report = AttendanceReport(
    "Student Attendance",
    "Total Students: 50\nPresent: 45\nAbsent: 5"
)

display(report)
