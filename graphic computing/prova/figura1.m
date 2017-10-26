close, clear, clc

a=1:0.001:100;
plot(cos(a),sin(a));hold on;

b=[-2.2 -0.6;-2.2 -0.5;-2 -0.5;-1.5 -1.5;-1.5 1.5;1.5 1.5];
plot(b(:,1),b(:,2));
plot(3,3);
plot(-3,-3);