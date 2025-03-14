import streamlit as st

class NumberMatchingProgram:
    def __init__(self):
        self.core36 = []
        self.matchCounts = {}
        self.topMatchList = []

    def add_number(self, new_number):
        if new_number == "0":
            new_number = "0"
        elif new_number == "00":
            new_number = "00"
        else:
            new_number = new_number.zfill(2)

        if not new_number.isdigit() or int(new_number) < 0 or int(new_number) > 99:
            st.error("Please enter a valid number (0-99).")
            return

        if len(self.core36) >= 36:
            removed_number = self.core36.pop(0)
            self.matchCounts[removed_number] -= 1
            if self.matchCounts[removed_number] < 3:
                if removed_number in self.topMatchList:
                    self.topMatchList.remove(removed_number)
                    st.write(f"Warning: Number {removed_number} now matches less than three times. Current count: {self.matchCounts[removed_number]}")

        self.core36.append(new_number)

        if new_number not in self.matchCounts:
            self.matchCounts[new_number] = 0
        self.matchCounts[new_number] += 1

        if self.matchCounts[new_number] == 3:
            self.topMatchList.append(new_number)

program = NumberMatchingProgram()

st.title("Number Matching Program")

user_input = st.text_input("Enter a number (0-99):")

if user_input:
    try:
        program.add_number(user_input)
        st.write(f"Current core36: {', '.join(program.core36)}")
        if program.topMatchList:
            st.write(f"Top Matches: {', '.join(f'**{num}**' for num in program.topMatchList)}")
    except ValueError:
        st.error("Invalid input. Please enter a number.")