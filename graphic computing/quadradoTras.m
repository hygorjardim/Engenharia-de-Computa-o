clc
close all

a=[0 0;3 0;3 3;0 3;0 0]
plot(a(:,1),a(:,2));


for i= 1:100
b=[i 0; i 0;i 0;i 0;i 0]
q=a+b

plot(q(:,1),q(:,2));

axis ([-5 100 -1 3])
axis equal
pause (0.01)
end



