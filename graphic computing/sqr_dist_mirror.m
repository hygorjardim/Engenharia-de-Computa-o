clc
close all

a=[0 0;3 0;3 3;0 3;0 0];
plot(a(:,1),a(:,2));
hold on

b=[0 0;0 0;1 1;-1 1;0 0];
d=a+b;
plot(d(:,1),d(:,2));


axis equal

ix=[1 0;0 -1];

m=d*ix;

plot(m(:,1),m(:,2));

iy=[-1 0;0 1];

my=d*iy;

plot(my(:,1),my(:,2));