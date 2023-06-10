import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="제어공학기말",
)

st.header("제어공학기말 202021025 임수창")
st.subheader("2번문제:")
st.subheader('''다음 전달함수 G(s) = 100 / (s+2)(s+3)일때  폐루프 전달함수를 구하고 unit step 입력의 응답곡선을 그리고, 주파수 응답을 보드선도로 그리시오. 이것을 자신의 학번 이름을 streamlit을 통해 Web에 배포 하시오. 
''')
st.subheader('''===================================================''')
st.subheader('''폐루프 전달함수M(s)를 구하는 과정:''')
st.subheader('''폐루프 전달함수 M(s)는 G(s)/1+G(s)H(s)이고, H(s)는 1이라고 본다. 그러면 M(s)=100/s**2+5s+106이 된다''')
if st.button("응답곡선 코드 보기"):
    code='''
    import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

st.set_page_config(
    page_title="제어공학기말",
)

st.header("응답곡선")

num = [100]
den = [1, 5, 106]

ltf = signal.TransferFunction(num, den)

t = np.linspace(0, 5, 1000)
u = np.ones_like(t)

t, y, _ = signal.lsim(ltf, u, t)

fig, ax = plt.subplots()
ax.plot(t, y)
ax.set(xlabel='Time', ylabel='Output', title='Step Response')
ax.grid(True)

st.pyplot(fig)
'''
st.code(code, language="python")
