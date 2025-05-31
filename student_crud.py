from db_config import get_connection
from student import Student
from fpdf import FPDF

def add_student(student):
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO students (name, roll_no, course, marks, attendance, remarks) VALUES (%s, %s, %s, %s, %s, %s)",
                (student.name, student.roll_no, student.course, student.marks, student.attendance, student.remarks))
    con.commit()
    con.close()

def view_students():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    con.close()

def update_marks(roll_no, new_marks):
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE students SET marks = %s WHERE roll_no = %s", (new_marks, roll_no))
    con.commit()
    con.close()

def delete_student(roll_no):
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE roll_no = %s", (roll_no,))
    con.commit()
    con.close()

def search_by_roll(roll_no):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    result = cur.fetchone()
    if result:
        print(result)
    else:
        print("No student found.")
    con.close()

import csv

def export_to_csv(filename="students_export.csv"):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cur.description])  # headers
        writer.writerows(rows)

    print(f"Exported {len(rows)} records to {filename}")
    con.close()


def export_to_pdf(filename="students_report.pdf"):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    if not rows:
        print("No records to export.")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Student Progress Report", ln=True, align='C')
    pdf.ln(10)

    # Table Header
    headers = ['ID', 'Name', 'Roll No', 'Course', 'Marks', 'Attendance', 'Remarks']
    for header in headers:
        pdf.cell(28, 10, header, border=1)
    pdf.ln()

    # Table Rows
    for row in rows:
        for item in row:
            pdf.cell(28, 10, str(item), border=1)
        pdf.ln()

    pdf.output(filename)
    print(f"PDF exported successfully as '{filename}'")
