% Código Cálculo de Cargas Q1 Q2
% Universidade Federal do Pará - Engenharia de Computação
% Hygor Jardim

function calculo(q1,q2)
fprintf('MODULO: ');

%VALOR DO EPISOLON;
epsi=(10^-9)/(36*pi);

%DEFININDO PONTOS DAS CARGAS, Q2 É ORIGEM Q1 É DESTINO;
xo=2; yo=0; zo=0;
xd=0; yd=1; zd=2;

%DEFININDO AS COMPONENTES COM BASE NA POSICAO DAS CARGAS;
ax= xd-xo
ay= yd-yo
az= zd-zo

%ACHANDO O VALOR DO MODULO
R=sqrt(ax^2+ay^2+az^2)

%DEFININDO VETORES UNITARIOS
xu=ax/R
yu=ay/R
zu=az/R

%CALCULO DA FORÇA APLICADA;
fprintf('FORCA: ');
f=(q1*q2)/(4*pi*epsi*(R^2))

%CALCULO DO VETOR DA FORÇA
xf=xu*f
yf=yu*f
zf=zu*f

%quiver3(xo,yo,zo,ax,ay,az,0); hold on;
quiver3(xd,yd,zd,xf,yf,zf,0,'linewidth',3);
hold off;
end
