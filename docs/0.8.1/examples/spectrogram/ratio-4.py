plot = normalised.plot(norm='log', vmin=.1, vmax=10, cmap='Spectral_r')
ax = plot.gca()
ax.set_yscale('log')
ax.set_ylim(10, 2000)
plot.add_colorbar(label='Relative amplitude')
plot.show()