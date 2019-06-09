# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:52:32 2019

@author: aimth
"""

# -*- coding: utf-8 -*-

"""

Created on Sat Jun  8 17:14:39 2019

  

@author: Imthiaz.Ahmed

"""


#Initialization

from pylab import *
clf()
cla()
Eq1=190.5
V=127
Xd=14
Xq=7
p=2
rpm=1800
m=3
w=rpm*0.1047
I=[50,45,40,35,30,25,20]
torque_angle=arange(-90,91,1)
torque_angle_rad=torque_angle*pi/180
#Torque vs Torque Angle
Te=[]
for i in range(len(I)):
    Te=0.5*((m*p)/w)*((Eq1*I[i]*cos(torque_angle_rad))-(0.5*I[i]*I[i]*(Xd-Xq)*sin(2*torque_angle_rad)))  #Need to check why 0.5 needs to be added, not there in book
    plot(torque_angle,Te,label=str(I[i])+" A")
legend(loc="upper left")
title("Torque vs Torque Angle")   
xlabel("Torque Angle")
ylabel("Torque")
grid()
#Voltage Locus
I=50;
R=0.057;
fig2,ax2 = subplots()
axes().set_aspect('equal', 'datalim')
Vd=((-R*sin(torque_angle_rad))-(Xq*cos(torque_angle_rad)))*I
Vq=(((R*cos(torque_angle_rad))-(Xd*sin(torque_angle_rad)))*I)+Eq1
plot(Vd,Vq,label="voltage locus wrt to change in torque angle")
Vdm=max(abs(Vd))
Vqm=max(Vq)
Vm=sqrt((Vdm*Vdm)+(Vqm*Vqm))
plot((Vm*cos(arange(pi*0.5,pi,0.1))),(Vm*sin(arange(pi*0.5,pi,0.1))),"b--",label="Volage limit locus")
legend(loc="best")
title("Voltage Lous")   
xlabel("d-axis")
ylabel("q-axis")
grid()
#voltage current lmit circles
fig3,ax3 = subplots()
axes().set_aspect('equal', 'datalim')
circle_rad=arange(0,2*pi,0.01)
I=50
plot((I*cos(circle_rad)),(I*sin(circle_rad)),"r--",label="Current Limit Circle")    
center_shift=Eq1/Xd
Ld=Xd/w
rpm=arange(2500,10000,2000)
w=rpm*pi/30
Xd=Ld*w
for i in range(len(Xd)):
    Voltage_Radius=Vm/Xd[i]
    plot((Voltage_Radius*cos(circle_rad))-center_shift,(Voltage_Radius*sin(circle_rad)), label=str(rpm[i])+" RPM")
w=1800;
psimd=Eq1/w;
legend(loc="best")
title("Voltage-Current Circle Diagram")
scatter(0,0)
scatter(-center_shift,0)
grid()
corner_speed=V/sqrt((psimd*psimd)+(Ld*I)*(Ld*I))
corner_speed_rpm=corner_speed*30/pi;
print(corner_speed_rpm)
#Max Speed Calculation 
u=arange(0.8,0.99,0.05)  #back emf / applied voltage
corner_max_speed_ratio= 1/(u-sqrt(1-(u*u)))
corner_speed=4000;
max_speed=corner_speed*corner_max_speed_ratio
