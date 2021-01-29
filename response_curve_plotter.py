import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from IPython.display import display

%config InlineBackend.figure_format = 'retina'

tau = 160.0/100.0
def response(w,z):

    Kp = 1.0
    a = 1- (tau**2)*(w**2)
    b = 2*tau*z*w
    sol = Kp/np.sqrt(a**2+b**2)
    sol1 = np.arctan(b/a)
    return sol
w = np.linspace(0.01,100,100000)

zeta = [0.2,1,2]
plt.figure();
plt.plot(np.log10(w), np.log10(response(w,zeta[0])), 'r', label = r"$\zeta$ = %.1f" %(zeta[0]))
plt.plot(np.log10(w), np.log10(response(w,zeta[1])), 'b', label = r"$\zeta$ = %.1f" %(zeta[1]))
plt.plot(np.log10(w), np.log10(response(w,zeta[2])), 'g', label = r"$\zeta$ = %.1f" %(zeta[2]))
plt.xlabel("Time (hours)", fontsize=12)
#plt.xlabel(r"{log}_{10}(\omega )")
#plt.ylabel(r"{log}_{10}(\frac{AR}{K_P} )")
plt.title(r"$\frac{AR}{K_P}$"+ "for 2nd Order System (" + r"$\tau =$ %.2f)"% (tau))
plt.legend();