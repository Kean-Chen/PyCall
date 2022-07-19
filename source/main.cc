#include <stdio.h>
#include "PyCall.h"



int main()
{
    std::vector<double> x = {1.0,2.0,3.0};
    std::vector<double> xx = {11.0,22.0,33.0};

    PyCall* plt = PyCall::getInstance();

    plt->figure(1, 6, 6);
    // plt->subplot(211);
    // plt->plot(x,"g");
    // plt->grid();
    // plt->subplot(212);
    plt->plot(x, xx,"ro");
    plt->grid();
    plt->show();
}





