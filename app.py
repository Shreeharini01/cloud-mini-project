import streamlit as st
import pandas as pd

st.title("Student Marks Data Visualization")

students = ["Maths", "Science", "English", "Python", "AI"]
marks = []

for subject in students:
    mark = st.number_input(f"Enter marks for {subject}", 0, 100)
    marks.append(mark)

data = pd.DataFrame({
    "Subjects": students,
    "Marks": marks
})

st.subheader("Marks Table")
st.dataframe(data)

st.subheader("Bar Chart")
st.bar_chart(data.set_index("Subjects"))

st.subheader("Line Chart")
st.line_chart(data.set_index("Subjects"))

average = sum(marks) / len(marks)

st.write("Average Marks:", average)

if average >= 50:
    st.success("Result: Pass")
else:
    st.error("Result: Fail")