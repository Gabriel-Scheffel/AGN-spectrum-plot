import matplotlib.pyplot as plt
from astropy.io import fits
from lines import lines
'''
rascunhos e lembretes:
matriz[linha][coluna]
plt.plo(x, y)

NGC5548: z = 0.01627
SDSSJ1430+2303: z = 0.08105
NGC6264: z = 0.03384
NGC3259: z = 0.00560
NGC3982: z = 0.00371
arquivo fit NGC5548 --> 'spec-2127-53859-0085.fits'
arquivo fit SDSSJ1430+2303 --> 'spec-2132-53493-0002.fits'
arquivo fit NGC6264 --> 'spec-1691-53260-0620.fits'
arquivo fit NGC3259 --> 'spec-0489-51930-0193.fits'
arquivo fit NGC3982 --> 'spec-1018-52672-0359.fits'
'''
z = 0.00371  # redshift da galáxia usada
with fits.open('spec-1018-52672-0359.fits') as hdul:
    # hdul.info() # informações sobre o documento.fit
    # specobj = hdul[2].data
    coadd = hdul[1].data

fluxa = []
fluxb = []
wlena = []
wlenb = []
em_lines = []
for i in range(len(coadd)):
    if i <= int(len(coadd)/2):
        fluxa.append(coadd[i][0]*1e-17)
        wlena.append((10**coadd[i][1])/(z+1))
    else:
        fluxb.append(coadd[i][0] * 1e-17)
        wlenb.append((10 ** coadd[i][1]) / (z + 1))


fig = plt.figure(figsize=(12,4))
f, (axs1, axs2) = plt.subplots(1, 2, sharey=True)
#plt.figure(figsize=(12,4))
lines.plotlines(wlena[0], wlena[-1], 2.5e-14)
axs1.plot(wlena, fluxa, 'black')
axs2.plot(wlenb, fluxb, 'black')
#plt.xlim(6.5e3)
'''
A função plotlines recebe três valores:
- um limite mínimo e um máximo para o x;
    linhas fora desses valores não são plotadas no gráfico.
- e outro valor máximo para o y;
    define a altura máxima das legendas.
'''
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux Density [erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$]')
plt.title('Galaxy NGC3982 - Seyfert 2 - starburst')
plt.show()
