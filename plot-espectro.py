import matplotlib.pyplot as plt
from astropy.io import fits
from lines import lines
'''
rascunhos e lembretes:
matriz[linha][coluna]
plt.plo(x, y)

NGC 5548: z = 0.01627
'''
z = 0.01627  # redshift
with fits.open('spec-2127-53859-0085.fits') as hdul:
    # hdul.info() # informações sobre o documento.fit
    coadd = hdul[1].data

flux = []
wlen = []
em_lines = []
for i in range(len(coadd)):
    flux.append(coadd[i][0]*1e-17)
    wlen.append((10**coadd[i][1])/(z+1))

plt.figure(figsize=(12,4))
lines.plotlines(3.5e3, 9.5e3, 5e-14)
plt.plot(wlen, flux, 'black')
'''
A função plotlines recebe três valores:
- um limite mínimo e um máximo para o x;
    linhas fora desses valores não são plotadas no gráfico.
- e outro valor máximo para o y;
    define a altura máxima das legendas.
'''
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux Density [erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$]')
plt.title('Galaxy NGC5548 - Seyfert 1')
plt.show()
