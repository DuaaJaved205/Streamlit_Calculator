

import streamlit as st
from add import add
from subtract import sub
from multiply import mul
from divide import div


st.title('Duaa Javed Calcultor')

#Enter first number
num1 = st.number_input('Enter first number:')

#Select an operator
operator = st.selectbox('Select operation:', ['+',   '-',   '*',   '/' ])

# Enter second number
num2 = st.number_input('Enter second number:')

if st.button('Calculate'):
        if operator == '+':
            result = add(num1,num2)
            st.success(f'Result: {result}')

        elif operator == '-':
            result = sub(num1,num2)
            st.success(f'Result: {result}')

        elif operator == '*':
            result = mul(num1,num2)
            st.success(f'Result: {result}')

        elif operator == '/':
            div(num1,num2)

