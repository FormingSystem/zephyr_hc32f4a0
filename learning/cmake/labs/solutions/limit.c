/* SPDX-License-Identifier: Apache-2.0 */
#include "limit.h"

int limit_value(int value, int maximum)
{
    return value > maximum ? maximum : value; /* 超过上限才截断，否则保留原值。 */
}
