import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
import pandas as pd
x =np.array([0,1,2,3,4,5,6,7,8,9,10])
y = np.array([42,41.6,40.6,40,39.6,39.2,39.2,38.9,38.6,38.4,38.3])
p= y-27;


def test(x, A, tau): 
    return A * np.exp(- x/tau) 
param, param_cov = curve_fit(test, x, p) 

z = np.linspace(0,10,100);
yy = param[0]*np.exp(-z/param[1])
plt.scatter(x,y)
plt.title(
        "Temperature Difference vs Time Data Plot")
#        r"Temperature T = A*exp(-t/$\tau$)"+ ";  "
#        r"A = %.2f, $\tau =$ %.1f " %(param[0], param[1])
#        )
plt.xlabel("Time (minutes)")
plt.ylabel(r'Temperature  $( ^{o}$C)')
plt.savefig("temperature.pdf")

df = pd.DataFrame(data=y)
display(df)