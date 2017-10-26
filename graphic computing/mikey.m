close all
clear all
clc

x = -pi:0.01:pi
re = 2;
rp = 2;

plot(re*cos(x),rp*sin(x)); % cabeça

hold on


plot(2+(re*cos(x)/2),(1.8+rp*sin(x)/2)); % orelha direita

plot(-2+(re*cos(x)/2),(1.8+rp*sin(x)/2)); % orelha esquerda

plot((cos(x)/4),(sin(x)/4)); % nariz

plot(-1+(1*cos(x)/4),(0.5+2*sin(x)/4)); % olho direito
plot(1+(1*cos(x)/4),(0.5+2*sin(x)/4)); % olho esquerdo

b = -1:0.01:1;
bc = b.^2 - 1.5;
plot(b,bc);

c = [-1 -0.5; 1 -0.5];
plot(c(:,1),c(:,2));


axis equal