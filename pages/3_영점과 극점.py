import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

st.set_page_config(
    page_title="제어공학기말",
)

st.header("영점과 극점")



num = [100]
den = [1, 5, 106]

zeros, poles, _ = signal.tf2zpk(num, den)

fig, ax = plt.subplots()
ax.plot(np.real(zeros), np.imag(zeros), 'o', label='Zeros')
ax.plot(np.real(poles), np.imag(poles), 'x', label='Poles')
ax.set(xlabel='Real', ylabel='Imaginary', title='Pole-Zero Plot')
ax.grid(True)
ax.legend()

st.pyplot(fig)
