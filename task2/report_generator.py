from fpdf import FPDF

# Read data from file
students = []
marks = []

with open("data.txt", "r") as file:
    for line in file:
        name, score = line.split()
        students.append(name)
        marks.append(int(score))

# Analysis
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Student Marks Report", ln=True, align="C")
pdf.ln(10)

for i in range(len(students)):
    pdf.cell(200, 10, txt=f"{students[i]} : {marks[i]}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Marks: {total_marks}", ln=True)
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)

pdf.output("report.pdf")

print("PDF Report Generated Successfully")
