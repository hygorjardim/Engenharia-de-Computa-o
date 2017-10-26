close all
clear all
clc

c=[0 0;1 0;1 1;0 1;0 0]

plot (c(:,1),c(:,2),'black') %cabeça
hold on

plot(0.2,0.7,'o') %olho esquerdo

plot(0.8,0.7,'o') %olho direito

k=-0.3:0.01:0.3
w=(-k.^2)+0.2;
plot(k+0.5,w+0.1, 'black') %boca

o=[0 0;0.2 0.5;0.4 0;0 0]

plot (o(:,1),o(:,2)+1,'black') %orelha esquerda

o2=[0 0;0.2 0.5;0.4 0;0 0]

plot (o2(:,1)+0.6,o2(:,2)+1,'black') %orelha direita

n=[0 0;0.1 0.2;0.2 0;0 0]

plot (n(:,1)+0.4,n(:,2)+0.4,'black') %nariz


p=[0 0;1 0;1 2;0 2;0 0]

p2=p*0.2

plot (p2(:,1)+0.4,p2(:,2)-0.4,'black') %pescoço

axis ([-1 2 -1 2])
axis equal