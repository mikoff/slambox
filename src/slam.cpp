#include "slam.h"

#include <iostream>

#include <Eigen/Core>
#include <sym/pose3.h>

int slam() {
#ifdef NDEBUG
    std::cout << "slambox/1.0: Hello World Release!!\n";
    std::cout << sym::Pose3<double>::Identity() << std::endl;
#else
    std::cout << "slambox/1.0: Hello World Debug!!\n";
    std::cout << sym::Pose3<double, 0>::Identity() << std::endl;
#endif
    return 0;
}
