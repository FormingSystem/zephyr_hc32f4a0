/* SPDX-License-Identifier: Apache-2.0 */
#include <stdio.h>
#include "scale.h"
#include "calibrate.h"

int main(void)
{
    int raw = 21; /* 固定输入，让每次构建后的结果可以比较。 */
    int scaled = scale_sample(raw); /* 库函数：21 变为 42。 */
    int result = calibrate(scaled); /* 应用函数：42 校准为 43。 */

    printf("value=%d\n", result);
    return result == 43 ? 0 : 1; /* 将业务结果转成进程退出码。 */
}
