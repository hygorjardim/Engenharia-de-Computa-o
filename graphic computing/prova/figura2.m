close, clear, clc

a=[0 0;-1 3;1 3;0 0];
plot(a(:,1),a(:,2));hold on;

x=pi;
b=[cos(x) sin(x);-sin(x) cos(x)];
c=a*b;
plot(c(:,1),c(:,2),'r');

d=[cos(x/2) sin(x/2);-sin(x/2) cos(x/2)];
e=a*d;
plot(e(:,1),e(:,2),'y');

f=[cos(3*x/2) sin(3*x/2);-sin(3*x/2) cos(3*x/2)];
g=a*f;
plot(g(:,1),g(:,2),'g');

plot(6,6);
plot(-6,-6);