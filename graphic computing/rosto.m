close all
clc 
clear all

re = 10
rp = 10
x0 = 0
y0 = 0
x = -pi:0.01:pi;

plot (x0+(re*cos(x)),y0+(rp*sin(x)))
hold on


plot (3+(2*cos(x)),3+(2*sin(x)))
plot (-3+(2*cos(x)),3+(2*sin(x)))
hold on
plot (x0+(1*cos(x)),y0+(1*sin(x)))

axis equal