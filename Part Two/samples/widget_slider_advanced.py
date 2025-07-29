import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Create initial plot and values
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5; f0 = 3; delta_f = 0.1; delta_a = 0.1
s = np.zeros_like(t)
l, = plt.plot(t, s, lw=2)
l1, = plt.plot(t, s, lw=1, linestyle='--')
l2, = plt.plot(t, s, lw=1, linestyle='--')
ax.margins(x=0)

ax.set_xlim(0, 1)
ax.set_ylim(-20, 20)

# Global mode
mode = 'De'

# Create three sliders
axcolor = 'lightgoldenrodyellow'
axfreq1 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axfreq2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axamp2 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
sfreq1 = Slider(axfreq1, 'Freq1', 0.1, 30.0, valinit=f0, valstep=delta_f)
sfreq2 = Slider(axfreq2, 'Freq2', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp1 = Slider(axamp1, 'Amp1', 0.1, 10.0, valinit=a0, valstep=delta_a)
samp2 = Slider(axamp2, 'Amp2', 0.1, 10.0, valinit=a0, valstep=delta_a)

# slider update actions
def update(val):
    amp1 = samp1.val
    amp2 = samp2.val
    freq1 = sfreq1.val
    freq2 = sfreq2.val
    l1.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t))
    if mode == 'Con':
        l.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * freq2 * t))
        l2.set_ydata(amp2 * np.sin(2 * np.pi * freq2 * t))
    elif mode == 'De':
        l.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t) - amp2 * np.sin(2 * np.pi * freq2 * t))
        l2.set_ydata(amp2 * -np.sin(2 * np.pi * freq2 * t))
    elif mode == 'Cos':
        l.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.cos(2 * np.pi * freq2 * t))
        l2.set_ydata(amp2 * np.cos(2 * np.pi * freq2 * t))
    elif mode == '120':
        l.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * ((freq2) * t + 1/3)))
        l2.set_ydata(amp2 * np.sin(2 * np.pi * ((freq2) * t + 1/3)))
    elif mode == '60':
        l.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * ((freq2) * t + 1/6)))
        l2.set_ydata(amp2 * np.sin(2 * np.pi * ((freq2) * t + 1/6)))
    fig.canvas.draw_idle()

sfreq1.on_changed(update)
sfreq2.on_changed(update)
samp1.on_changed(update)
samp2.on_changed(update)

# Create a radio button
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
l.set_color(radio.value_selected)
l1.set_color(radio.value_selected)
l2.set_color(radio.value_selected)
# Create a mode button
rax_mode = plt.axes([0.025, 0.7, 0.15, 0.15], facecolor=axcolor)
radio_mode = RadioButtons(rax_mode, ('Con', 'De', 'Cos', '60', '120'), active=1)

# radio button update actions
def colorfunc(label):
    l.set_color(label)
    l1.set_color(label)
    l2.set_color(label)
    fig.canvas.draw_idle()

# mode button update actions
def modefunc(label):
    if label == 'Con' or label == 'De' or label == 'Cos' or label == '60' or label == '120':
        global mode
        mode = label
        update(0)

radio_mode.on_clicked(modefunc)
radio.on_clicked(colorfunc)

plt.show()