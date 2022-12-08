import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,8,10)
print(x)
y=np.cos(x)+2
plt.plot(x,y,'y:',label='y=2,27e^x*cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
plt.savefig("D:\Git\Repos\VKN\cosinus.png" ,dpi=400)



     
     

