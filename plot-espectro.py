import matplotlib.pyplot as plt
from astropy.io import fits
from lines import lines
'''
matriz[linha][coluna]
plt.plo(x, y)

NGC 5548: z = 0.01627
'''
z = 0.01627  # redshift
with fits.open('spec-2127-53859-0085.fits') as hdul:
    # hdul.info()
    coadd = hdul[1].data

flux = []
wlen = []
em_lines = []
for i in range(len(coadd)):
    flux.append(coadd[i][0])
    wlen.append((10**coadd[i][1])/(z+1))

fig = plt.xlim(3.5e3, 9.5e3)
plt.plot(wlen, flux, 'black')
lines.plotlines(3.5e3, 9.5e3, 5e3)
plt.show()
