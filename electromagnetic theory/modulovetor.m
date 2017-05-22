% Código Cálculo do Modulo do Vetor
% Universidade Federal do Pará - Engenharia de Computação
% Hygor Jardim

q1 = [ 0 1 2 ];
q2 = [ 2 0 0 ];
rst = q1-q2;
rst2 = rst.^2;
rst2(1,3)

H = 0;
n = 3;
for i=1:n; 
H = H + rst2(1,i);
end

modulo = sqrt(H);
