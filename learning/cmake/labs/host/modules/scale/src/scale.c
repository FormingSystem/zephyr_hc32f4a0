/* SPDX-License-Identifier: Apache-2.0 */
#include "scale.h"

int scale_sample(int value)
{
    return value * 2; /* 接收调用者的值，不自行获取传感器数据。 */
}
