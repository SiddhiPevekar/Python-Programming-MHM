#program for integration with a=0 and b=1
import scipy
from scipy import integrate
f=lambda x:x**2#take f(x) as f
integration= integrate.quad(f,0,1)# limits a=0 and b=1
print(integration)
