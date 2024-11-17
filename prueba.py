import matplotlib.pyplot as plt

# Datos de la gráfica
epocas = range(1, 8)
train_loss = [1.5, 1.48, 1.46, 1.44, 1.42, 1.4, 1.38]

val_loss = [0.5, 0.48, 0.46, 0.44, 0.42, 0.4,0.38]

train_acc = [1.5, 1.48, 1.46, 1.44, 1.42, 1.4, 1.38]

val_acc = [1.5, 1.48, 1.46, 1.44, 1.42, 1.4, 1.38]


# Crear figura y ejes
fig, ax1 = plt.subplots()

# Gráfica de pérdida (loss)
ax1.plot(epocas, train_loss, 'b-', label='train_loss')
ax1.plot(epocas, val_loss, 'r-', label='val_loss')
ax1.set_xlabel('Epocas')
ax1.set_ylabel('Pérdida (Loss)', color='b')
ax1.tick_params('y', colors='b')

# Gráfica de precisión (accuracy)
ax2 = ax1.twinx()
ax2.plot(epocas, train_acc, 'g-', label='train_acc')
ax2.plot(epocas, val_acc, 'y-', label='val_acc')
ax2.set_ylabel('Precisión (Accuracy)', color='g')
ax2.tick_params('y', colors='g')

# Legend
fig.tight_layout()
plt.legend(loc='upper right')

# Mostrar gráfica
plt.show()