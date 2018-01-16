% [I1, J1, K1] = textread('Aliens\QValues_Aliens_0.1_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I2, J2, K2] = textread('Aliens\QValues_Aliens_0.2_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I3, J3, K3] = textread('Aliens\QValues_Aliens_0.3_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I4, J4, K4] = textread('Aliens\QValues_Aliens_0.4_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I5, J5, K5] = textread('Aliens\QValues_Aliens_0.5_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I6, J6, K6] = textread('Aliens\QValues_Aliens_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I1, J1, K1] = textread('Racing\QValues_Racing_0.1_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I2, J2, K2] = textread('Racing\QValues_Racing_0.2_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I3, J3, K3] = textread('Racing\QValues_Racing_0.3_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I4, J4, K4] = textread('Racing\QValues_Racing_0.4_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I5, J5, K5] = textread('Racing\QValues_Racing_0.5_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I6, J6, K6] = textread('Racing\QValues_Racing_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I1, J1, K1] = textread('ZenPuzzle\QValues_ZenPuzzle_1-101.1_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I2, J2, K2] = textread('ZenPuzzle\QValues_ZenPuzzle_1-101.2_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I3, J3, K3] = textread('ZenPuzzle\QValues_ZenPuzzle_1-101.3_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I4, J4, K4] = textread('ZenPuzzle\QValues_ZenPuzzle_1-101.4_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I5, J5, K5] = textread('ZenPuzzle\QValues_ZenPuzzle_1-101.5_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I6, J6, K6] = textread('ZenPuzzle\QValues_ZenPuzzle_1_48s_43s_38s_33s_28s_23s_18s_13s_8s_3s_8s_13s_18s_23s_28s_33s_38s_43s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I1, J1, K1] = textread('Aliens\QValues_Aliens_0.1_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I2, J2, K2] = textread('Aliens\QValues_Aliens_0.2_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I3, J3, K3] = textread('Aliens\QValues_Aliens_0.3_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I4, J4, K4] = textread('Aliens\QValues_Aliens_0.4_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I5, J5, K5] = textread('Aliens\QValues_Aliens_0.5_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
[I6, J6, K6] = textread('Aliens\QValues_Aliens_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I1, J1, K1] = textread('Racing\QValues_Racing_111.1_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I2, J2, K2] = textread('Racing\QValues_Racing_111.2_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I3, J3, K3] = textread('Racing\QValues_Racing_111.3_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I4, J4, K4] = textread('Racing\QValues_Racing_111.4_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I5, J5, K5] = textread('Racing\QValues_Racing_111.5_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I6, J6, K6] = textread('Racing\QValues_Racing_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I1, J1, K1] = textread('ZenPuzzle\QValues_ZenPuzzle_101.1_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I2, J2, K2] = textread('ZenPuzzle\QValues_ZenPuzzle_101.2_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I3, J3, K3] = textread('ZenPuzzle\QValues_ZenPuzzle_101.3_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I4, J4, K4] = textread('ZenPuzzle\QValues_ZenPuzzle_101.4_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I5, J5, K5] = textread('ZenPuzzle\QValues_ZenPuzzle_101.5_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');
% [I6, J6, K6] = textread('ZenPuzzle\QValues_ZenPuzzle_48s_38s_28s_18s_8s_3s_8s_18s_28s_38s_47_mean_squared_error_adam.txt', '[%f, %f, %f]');

%[I, J, K] = textread('indices.txt', '[%f, %f, %f]');

circleSize = 40;


figure

subplot(2, 3, 1)
c = linspace(0,1,length(I1));
scatter3(I1, J1, K1, circleSize, c, 'filled')
title('level 1')
subplot(2, 3, 2)
c = linspace(0,1,length(I2));
scatter3(I2, J2, K2, circleSize, c, 'filled')
title('level 2')
subplot(2, 3, 3)
c = linspace(0,1,length(I3));
scatter3(I3, J3, K3, circleSize, c, 'filled')
title('level 3')
subplot(2, 3, 4)
c = linspace(0,1,length(I4));
scatter3(I4, J4, K4, circleSize, c, 'filled')
title('level 4')
subplot(2, 3, 5)
c = linspace(0,1,length(I5));
scatter3(I5, J5, K5, circleSize, c, 'filled')
title('level 5')
subplot(2, 3, 6)
c = linspace(0,1,length(I6));
scatter3(I6, J6, K6, circleSize, c, 'filled')
title('levels combined')

%subplot(2, 3, [3, 6])
%scatter3(I, J, K, 'filled')
%title('combined')