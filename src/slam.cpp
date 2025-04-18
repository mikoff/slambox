#include "slam.h"

#include <sym/pose3.h>

#include <Eigen/Core>
#include <iostream>

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
