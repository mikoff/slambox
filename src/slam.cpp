#include "slam.h"

#include <iostream>

int slam() {
#ifdef NDEBUG
    std::cout << "slambox/1.0: Hello World Release!\n";
#else
    std::cout << "slambox/1.0: Hello World Debug!\n";
#endif
    return 0;
}
