/* SPDX-License-Identifier: Apache-2.0 */
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

static uint32_t sum_bytes(const uint8_t *data, size_t length)
{
    uint32_t sum = 0u;
    for (size_t i = 0; i < length; ++i) {
        sum += data[i];
    }
    return sum;
}

int temporary_buffer_example(uint32_t *result)
{
    if (result == NULL) {
        return -1;
    }
    uint8_t *pixels = malloc(16u);
    if (pixels == NULL) {
        return -2;
    }
    for (size_t i = 0; i < 16u; ++i) {
        pixels[i] = (uint8_t)i;
    }
    *result = sum_bytes(pixels, 16u);
    free(pixels);
    return 0;
}
