import streamlit as st

def div(num1,num2):
    if num2 == 0:
        st.error('Cannot divide by zero! Please enter a non-zero value for the second number.')
    else:
        result = num1 / num2
        st.success(f'Result: {result}')