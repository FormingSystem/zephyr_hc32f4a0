/* SPDX-License-Identifier: Apache-2.0 */
#include <stdio.h>
#include "scale.h"
#include "calibrate.h"
#include "limit.h"

int main(void)
{
    int raw = 21;
    int scaled = scale_sample(raw);
    int result = limit_value(calibrate(scaled), 40);

    printf("value=%d\n", result);
    return result == 40 ? 0 : 1;
}
