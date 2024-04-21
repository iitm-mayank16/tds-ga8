import streamlit as st

# Function to find the largest among three numbers
def FindLargestNumber(numbers):
    return max(numbers)

def main():
    st.title("Find the Largest Number")
    st.write("Please input three numbers.")

    # Input fields for three numbers
    numbers = [st.number_input(f"Number {i + 1}:", step=1.0) for i in range(3)]

    # Button to find the largest number
    if st.button("Find Largest"):
        largest = FindLargestNumber(numbers)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
