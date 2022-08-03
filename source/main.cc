/*
 * @Author: ChenGen chengen1993@126.com
 * @Date: 2022-07-19 17:27:22
 * @LastEditors: ChenGen chengen1993@126.com
 * @LastEditTime: 2022-08-03 18:55:07
 * @FilePath: /PyCall/source/main.cc
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <stdio.h>
#include "PyCall.h"
#include <thread>
#include <random>



int main()
{
    std::vector<double> x = {1.0,2.0,3.0};
    std::vector<double> y = {11.0,22.0,33.0};


    PyCall* plt = PyCall::getInstance();
    plt->ion();


    while (1)
    {
        plt->clf();
        plt->plot(x, y, "r-");
        std::this_thread::sleep_for(std::chrono::milliseconds(100));

        y[0] = random();
        y[1] = random();
        y[2] = random();
    }
    plt->ioff();
    plt->show();

}





