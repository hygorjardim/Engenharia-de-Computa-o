clear all
clc
close all
x=-10:10;
y=(x.^2)+10*x;
plot(x,y)
hold on 
y=(x.^2)-10*x+5;
plot(x,y)