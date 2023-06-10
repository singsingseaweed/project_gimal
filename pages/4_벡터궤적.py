import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sys = signal.lti([], [1, 5, 106])

freqs, H = signal.freqresp(sys)

fig, ax = plt.subplots()
ax.plot(H.real, H.imag, "b")
ax.plot(H.real, -H.imag, "r")
ax.set_xlim([-2.0, 2.0])
ax.set_ylim([-2.0, 2.0])
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title('Vector Diagram of G(s)')
ax.grid(True, which='both')

circle = plt.Circle((0, 0), 1, color='green', fill=False)
ax.add_artist(circle)

for i in range(0, len(H), len(H) // 10):
    ax.arrow(H.real[i], H.imag[i], H.real[i + 1] - H.real[i], H.imag[i + 1] - H.imag[i],
             shape='full', lw=0, length_includes_head=True, head_width=0.09)

# 그림을 Streamlit 애플리케이션에 표시
st.pyplot(fig)
