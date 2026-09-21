/* SPDX-License-Identifier: Apache-2.0 */
#include "limit.h"

int limit_value(int value, int maximum)
{
    return value > maximum ? maximum : value;
}
