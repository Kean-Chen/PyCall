# PyCall
c/c++ code call python some function of matplotlib.pyplot 


# 1. 直接编译  

## compile
g++ -std=c++11 -I /usr/include/python3.8 main.cc -o main  -lpython3.8


## run
./main

# 2. CMake 编译  
参考 cmake文件夹内工程  
运行时需要将cpy.py放在可执行程序同一路径下
