import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages

style.use("default")


##############################################################################

pp = PdfPages('18che160_Rajas_Mehendale_HW_2.pdf')
##############################################################################

tau = 160/100;
omega = np.linspace(0.001,1000,100000)
omega_tau = tau*omega
phi = (-1)*np.arctan(omega_tau)
AR_by_Kp = 1/np.sqrt(1+np.power(omega_tau,2))
##############################################################################
x1 = np.log10(omega)
y1 = np.log10(AR_by_Kp)
plt.plot(x1, y1, 'b')
plt.xlabel(r"${log}_{10}(\ \omega (\frac{rad}{s})\ )$", fontsize=14)
plt.ylabel(r"${log}_{10} \ \ (\frac{A*R}{K_P})$", fontsize=14)
plt.xlim([-3,3])
plt.ylim([-3.5,0.5])
plt.grid()
t1 = r"${log}_{10}(\frac{AR}{K_P})$"
t2 = " vs " + r"${log}_{10}(\omega )$"
t3 = " for " + r"$\tau =$" + " %.2f seconds" %(tau)
plt.title(t1+t2+t3,fontsize=14)
#plt.savefig("hw2_1.pdf")
pp.savefig(bbox_inches = 'tight')

##############################################################################
x2 = np.log10(omega)
y2 = phi
plt.figure()
plt.plot(x2, y2, 'b')
plt.xlabel(r"${log}_{10}(\ \omega (\frac{rad}{s})\ )$", fontsize=14)
plt.ylabel(r"$\phi =  \ \ {tan}^{-1} (-\omega \tau )$", fontsize=14)
plt.xlim([-3,3])
plt.ylim([-1.6,0.2])
plt.grid()
t1 = r"$\phi $"
t2 = " vs " + r"${log}_{10}(\omega )$"
t3 = " for " + r"$\tau =$" + " %.2f seconds" %(tau)
plt.title(t1+t2+t3,fontsize=14)
#plt.savefig("hw2_1.pdf")
pp.savefig(bbox_inches = 'tight')
##############################################################################
pp.close()