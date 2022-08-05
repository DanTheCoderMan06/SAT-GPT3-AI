# SAT-GPT3-AI
This Project was developed and created by Daniil Novak. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Background Information
GPT-3 is the most recent and advanced AI algorithm publically available for use. It was developed by Open-AI, and is the 3rd Version of their GPT AI. The SAT on the other hand is decades old, and a traditional way of grading students based on intelligence and ability to solve tasks.
#What does my program do
Automatically creates problems with one or two steps, division addition subtraction or multiplication, and feeds it to GPT-3. I then record values such as the type of the question, the steps in the question, etc.
#How does it work?
You have to download the ZIP Version and extract it to your desktop. Afterwords you have to insert a list of OpenAI keys into the open AI to avoid sending too many API Requests. Finally, you just wait until the data-set is done, and the last part of the code runs statistical tests which for Example find the correlation between steps and how well GPT-3 did.
#Example Data
![Alt text](https://i.imgur.com/NKbjQFK.png)
![Alt text](https://i.imgur.com/TUqonvv.png)
No. Observations:                1724   AIC:                            -2047.
Df Residuals:                    1704   BIC:                            -1938.
Df Model:                          19                                         
Covariance Type:            nonrobust                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                  3.519e+11   1.89e+11      1.864      0.062   -1.83e+10    7.22e+11
type[T.additionaddition]                   7.085e+10    3.8e+10      1.864      0.062   -3.69e+09    1.45e+11
type[T.additiondivison]                    6.491e+10   3.48e+10      1.864      0.062   -3.38e+09    1.33e+11
type[T.additionmultiplication]             7.264e+10    3.9e+10      1.864      0.062   -3.78e+09    1.49e+11
type[T.additionsubtraction]                6.353e+10   3.41e+10      1.864      0.062   -3.31e+09     1.3e+11
type[T.divison]                            1.981e+09   1.06e+09      1.864      0.062   -1.03e+08    4.06e+09
type[T.divisonaddition]                    7.059e+10   3.79e+10      1.864      0.062   -3.68e+09    1.45e+11
type[T.divisondivison]                      6.63e+10   3.56e+10      1.864      0.062   -3.45e+09    1.36e+11
type[T.divisonmultiplication]              6.708e+10    3.6e+10      1.864      0.062   -3.49e+09    1.38e+11
type[T.divisonsubtraction]                  6.96e+10   3.73e+10      1.864      0.062   -3.63e+09    1.43e+11
type[T.multiplication]                    -3.974e+08   2.13e+08     -1.864      0.062   -8.15e+08    2.07e+07
type[T.multiplicationaddition]             6.953e+10   3.73e+10      1.864      0.062   -3.62e+09    1.43e+11
type[T.multiplicationdivison]              7.033e+10   3.77e+10      1.864      0.062   -3.66e+09    1.44e+11
type[T.multiplicationmultiplication]       7.038e+10   3.78e+10      1.864      0.062   -3.67e+09    1.44e+11
type[T.multiplicationsubtraction]          6.985e+10   3.75e+10      1.864      0.062   -3.64e+09    1.43e+11
type[T.subtraction]                        1.325e+08   7.11e+07      1.864      0.062    -6.9e+06    2.72e+08
type[T.subtractionaddition]                 7.07e+10   3.79e+10      1.864      0.062   -3.68e+09    1.45e+11
type[T.subtractiondivison]                 6.862e+10   3.68e+10      1.864      0.062   -3.57e+09    1.41e+11
type[T.subtractionmultiplication]          6.799e+10   3.65e+10      1.864      0.062   -3.54e+09     1.4e+11
type[T.subtractionsubtraction]             6.874e+10   3.69e+10      1.864      0.062   -3.58e+09    1.41e+11
step                                      -3.519e+11   1.89e+11     -1.864      0.062   -7.22e+11    1.83e+10
step:type[T.additionaddition]              1.405e+11   7.54e+10      1.864      0.062   -7.32e+09    2.88e+11
step:type[T.additiondivison]               1.435e+11    7.7e+10      1.864      0.062   -7.47e+09    2.94e+11
step:type[T.additionmultiplication]        1.396e+11   7.49e+10      1.864      0.062   -7.27e+09    2.87e+11
step:type[T.additionsubtraction]           1.442e+11   7.73e+10      1.864      0.062   -7.51e+09    2.96e+11
step:type[T.divison]                      -1.981e+09   1.06e+09     -1.864      0.062   -4.06e+09    1.03e+08
step:type[T.divisonaddition]               1.407e+11   7.54e+10      1.864      0.062   -7.33e+09    2.89e+11
step:type[T.divisondivison]                1.428e+11   7.66e+10      1.864      0.062   -7.44e+09    2.93e+11
step:type[T.divisonmultiplication]         1.424e+11   7.64e+10      1.864      0.062   -7.42e+09    2.92e+11
step:type[T.divisonsubtraction]            1.411e+11   7.57e+10      1.864      0.062   -7.35e+09     2.9e+11
step:type[T.multiplication]                3.974e+08   2.13e+08      1.864      0.062   -2.07e+07    8.15e+08
step:type[T.multiplicationaddition]        1.412e+11   7.57e+10      1.864      0.062   -7.35e+09     2.9e+11
step:type[T.multiplicationdivison]         1.408e+11   7.55e+10      1.864      0.062   -7.33e+09    2.89e+11
step:type[T.multiplicationmultiplication]  1.408e+11   7.55e+10      1.864      0.062   -7.33e+09    2.89e+11
step:type[T.multiplicationsubtraction]      1.41e+11   7.56e+10      1.864      0.062   -7.34e+09    2.89e+11
step:type[T.subtraction]                  -1.325e+08   7.11e+07     -1.864      0.062   -2.72e+08     6.9e+06
step:type[T.subtractionaddition]           1.406e+11   7.54e+10      1.864      0.062   -7.32e+09    2.89e+11
step:type[T.subtractiondivison]            1.416e+11    7.6e+10      1.864      0.062   -7.38e+09    2.91e+11
step:type[T.subtractionmultiplication]      1.42e+11   7.61e+10      1.864      0.062   -7.39e+09    2.91e+11
step:type[T.subtractionsubtraction]        1.416e+11   7.59e+10      1.864      0.062   -7.37e+09    2.91e+11
==============================================================================
Omnibus:                      183.219   Durbin-Watson:                   2.055
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              273.792
Skew:                           0.780   Prob(JB):                     3.52e-60
Kurtosis:                       4.173   Cond. No.                     7.18e+16
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 1.5e-30. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
