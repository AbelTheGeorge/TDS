import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title('Find the Largest Number')

# Input numbers
num1 = st.number_input('Enter first number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)
num3 = st.number_input('Enter third number', value=0.0)

if st.button('Find Largest'):
    largest = find_largest(num1, num2, num3)
    st.write(f'The largest number among {num1}, {num2}, and {num3} is {largest}')
