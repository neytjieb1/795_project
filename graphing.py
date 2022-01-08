def T(u):
    return 1 - abs(2*u-1)

def Tn(n, U):
    for i in range(n):
        U = T(U)
    return U

import numpy as np
X1 = np.linspace(0,1,1200)
Y= T(T(X1))

import matplotlib.pyplot as plt

# plt.plot(X1, Y, '-g')
# plt.title(r'Plot of the map $T^2$, $T=1-|2u-1|$')
# plt.xlabel(r'$x_n$')
# plt.ylabel(r'$x_{n+2}$')
# plt.savefig("T2.png")
# plt.show()

plt.plot(X1, Tn(2, X1), 'forestgreen')  #52=close, 53=line
plt.savefig('tentmap_2.svg', format='svg', dpi=1000)
plt.show()


# plt.plot(X3, T(X3), '-k')
# plt.show()
