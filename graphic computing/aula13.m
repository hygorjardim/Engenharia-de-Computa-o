close all
clc 
clear all
%elipse
re=0.5
rp=2
x0=0
y0=0
x=-pi:0.01:pi;




xe=x0+rp*cos(x);
ye=y0+re*sin(x);
me=[xe' ye'];






%circulo
c=-pi:0.01:pi;


%transformar elipse

for i= 1:0.01:4
 hold off
 
r=[cos(pi/i) -sin(pi/i);sin(pi/i) cos(pi/i)]
j=me*r;
plot(j(:,1),j(:,2),'--');
hold on
r2=[cos(pi/i) sin(pi/i);-sin(pi/i) cos(pi/i)]
j2=me*r2;
plot(j2(:,1),j2(:,2),'--');
hold on

r3=[cos(pi*i) sin(pi*i);-sin(pi*i) cos(pi*i)]

j3=me*r3;


r4=[cos(pi*i) -sin(pi*i);sin(pi*i) cos(pi*i)]

j4=me*r4;
plot(j4(:,1),j4(:,2),'--');
plot(j3(:,1),j3(:,2),'--');
plot(cos(c)*2,sin(c)*2,'black');
%plot(x0+rp*cos(x),y0+re*sin(x),'+');
pause (0.001)


axis equal
end




