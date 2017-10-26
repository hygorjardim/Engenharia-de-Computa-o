close, clear, clc


x =-pi:0.01:pi;

plot(cos(x),sin(x))

hold on

c = [-2.2 0.3;-2.2 0.5;-2 0.5; -1.5 -1.5;-1.5 1.5; -1.5 -1.5;-1.5 1.5; 1.5 1.5]

plot(c(:,1),c(:,2))

plot(3,3);
plot(-3,-3);
axis equal