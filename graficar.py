import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,8), )
_[['N', 'E']].plot(x='E', y='N', kind='scatter', ax=ax)
_[['N', 'E']].plot(x='E', y='N', ax=ax)
ax.grid()
plt.show()