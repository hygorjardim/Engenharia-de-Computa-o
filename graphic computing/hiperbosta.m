close all
clc 
clear all

x=-2:0.001:2;

plot(cosh(x), sinh(x))


hold on

h2=[cosh(x) sinh(x)]

r3=[cos(pi/4) sin(pi/4);-sin(pi/4) cos(pi/4)]

h=r3*h2;


plot(h(:,1),h(:,2),'--');

axis equal