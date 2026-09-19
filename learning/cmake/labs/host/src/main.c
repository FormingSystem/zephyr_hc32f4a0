/* SPDX-License-Identifier: Apache-2.0 */
#include <stdio.h>
#include "scale.h"
#include "calibrate.h"

int main(void)
{
    int raw = 21;
    int scaled = scale_sample(raw);
    int result = calibrate(scaled);

    printf("value=%d\n", result);
    return result == 43 ? 0 : 1;
}
