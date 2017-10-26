clc
close all

a=[0 0;2 0;2 2;0 2;0 0]
plot(a(:,1),a(:,2));
hold on
q=a*2

plot(q(:,1),q(:,2));

q=a*0.5

plot(q(:,1),q(:,2));

axis equal