close, clear, clc


x =-pi:0.01:pi;
re = 2;
rp = 2;

plot(re*cos(x),rp*sin(x))
hold on
plot(1+(re*cos(x)/6),(0.5+rp*sin(x)/6));
plot(-1+(re*cos(x)/6),(0.5+rp*sin(x)/6));

b = -1:0.01:1;
bc = b.^2 - 1.5;
plot(b,bc);

corpo = [0 -2; 0 -5]
plot(corpo(:,1),corpo(:,2))

brac = [-3 -2.5;3 -2.5]
plot(brac(:,1),brac(:,2))

perna = [-2 -6.5; 0 -5; 2 -6.5]
plot(perna(:,1),perna(:,2))

plot (-4,4)
plot (4.5,-7)
axis equal