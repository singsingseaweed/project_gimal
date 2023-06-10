import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

st.set_page_config(
    page_title="제어공학기말",
)

st.header("주파수응답")
st.subheader("2번문제 streamlit 으로 공유")

num = [100]
den = [1, 5, 106]

ltf = signal.TransferFunction(num, den)

w, mag, phase = signal.bode(ltf)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w, mag)
ax1.set(xlabel='Frequency [rad/s]', ylabel='Magnitude [dB]', title='Bode Plot - Magnitude')
ax1.grid(True)

ax2.semilogx(w, phase)
ax2.set(xlabel='Frequency [rad/s]', ylabel='Phase [degrees]', title='Bode Plot - Phase')
ax2.grid(True)

fig.tight_layout()
st.pyplot(fig)
