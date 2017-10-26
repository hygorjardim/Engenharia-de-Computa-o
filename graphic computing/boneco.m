close, clear, clc

a=1:0.001:100;
plot(cos(a),sin(a),'k');hold on;

w=-0.8:0.1:0.8;
z=w.^2-0.8;
plot(w,z,'k')

plot(-0.4,0.4,'ko')
plot(0.4,0.4,'ko')

b=[0 -1;0 -5];
plot(b(:,1),b(:,2),'k');

c=[0 -2;-1 -3];
plot(c(:,1),c(:,2),'k');

d=[0 -2;1 -3];
plot(d(:,1),d(:,2),'k');

e=[0 -5;-1 -6];
plot(e(:,1),e(:,2),'k');

f=[0 -5;1 -6];
plot(f(:,1),f(:,2),'k');

plot(4,4); plot(-4,-10);