clc
close all

a=[0 0;3 0;3 3;0 3;0 0];
plot(a(:,1),a(:,2));
hold on

b=[0 0;0 0;1 1;-1 1;0 0];
d=a+b;
plot(d(:,1),d(:,2));

axis ([-5 5 -5 5])
axis equal