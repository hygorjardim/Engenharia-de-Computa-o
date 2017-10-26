clc
close all

a=[0 0;2 0;2 2;0 2;0 0]

plot(a(:,1),a(:,2));

for i= 1:0.1:100
b=[i 0; i 0;i 0;i 0;i 0]

r=[cos(pi*i) sin(pi*i);-sin(pi*i) cos(pi*i)]
j=a*r
plot(j(:,1),j(:,2));
axis equal
pause (0.001)
end



