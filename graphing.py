# def T(u):
#     return 1 - abs(2*u-1)

# def Tn(n, U):
#     for i in range(n):
#         U = T(U)
#     return U

# import numpy as np
# X1 = np.linspace(0,1,1200)
# Y= T(T(X1))

# import matplotlib.pyplot as plt

# # plt.plot(X1, Y, '-g')
# # plt.title(r'Plot of the map $T^2$, $T=1-|2u-1|$')
# # plt.xlabel(r'$x_n$')
# # plt.ylabel(r'$x_{n+2}$')
# # plt.savefig("T2.png")
# # plt.show()

# plt.plot(X1, Tn(2, X1), 'forestgreen')  #52=close, 53=line
# plt.savefig('tentmap_2.svg', format='svg', dpi=1000)
# plt.show()

# # plt.plot(X3, T(X3), '-k')
# # plt.show()

##################################### LOGISTIC MAP ############################

# def logistic(r, xn):
#     return r*xn*(1-xn)

# x0=0.2
# x0_p=0.20001
# r0=4 #3.7
# N=50

# Y1 = [x0]
# Y2= [x0_p]
# X = [i for i in range(N)]
# for i in range(1, N):
#     Y1.append(logistic(r0,Y1[i-1]))
#     Y2.append(logistic(r0,Y2[i-1]))

# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = [10, 4]
# fig, ax = plt.figure(), plt.axes()
# plt.plot(X, Y1, 'darkblue', lw=0.75)
# plt.plot(X, Y2, 'orangered', lw=0.75)

# ax.axhspan(0.4-0.05, 0.4+0.05, alpha=0.6, color='lightgreen')
# ax.set_xlabel(r"n", fontsize=12)
# ax.set_ylabel(r"$x_n$", fontsize=12)

# # plt.savefig('_logistic_sdic.eps', format='eps', dpi=1000)
# plt.show()


######################## NOISE ADDED #######################################
import numpy as np
def calcDB(noise, actual):
    import math
    print("Noise in dB")
    P_noise = np.std(noise, axis=0)**2
    P_signal = np.std(actual, axis=0)**2
    dB = [10*math.log10(P_signal[i]/P_noise[i]) for i in range(actual.shape[1]) ]
    print("Var of actual: {a}\nVar of noise: {n}\ndB: {d}".format(a=P_noise, n=P_signal, d=dB))
    print("Average dB's added: {avdb}".format(avdb=np.round(np.mean(dB), 3)))

print("Thomas")
_data = np.loadtxt('/home/jo-anne/Documents/Honours/Other/Supplementary_Article/Supplementary-Code/Data/Thomas_0.1056.txt') 
noise = np.random.normal(0,0.05,(_data.shape))
raw_mean = np.mean(_data, axis=0)
pulled_data = _data - raw_mean
calcDB(noise, pulled_data)

print("DP")
_data = np.loadtxt('/home/jo-anne/Documents/Honours/pendulum/Data/rK.txt')
noise = np.random.normal(0,0.01,(_data.shape))
raw_mean = np.mean(_data, axis=0)
pulled_data = _data - raw_mean
calcDB(noise, pulled_data)           