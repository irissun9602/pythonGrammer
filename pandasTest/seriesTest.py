'''
Error :
Intel MKL FATAL ERROR: Cannot load libmkl_intel_thread.dylib.

Solve :
conda install nomkl numpy scipy scikit-learn numexpr
conda remove mkl mkl-service
'''

from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)



