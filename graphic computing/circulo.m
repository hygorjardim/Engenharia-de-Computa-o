clc
clear all
close all
x=1:000.1:10;
plot(cos(x),sin(x))
hold on 
k=-0.8:000.1:0.8
w=(-k.^2)+0.2;
plot(k,w)

plot(-0.4,0.4,'penta')

plot(0.4,0.4,'penta')