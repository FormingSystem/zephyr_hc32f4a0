/* SPDX-License-Identifier: Apache-2.0 */
#include <stdint.h>

uint32_t sample_unsigned(const uint8_t *samples)
{
    return samples[1];
}

int32_t sample_signed(const int8_t *samples)
{
    return samples[1];
}

uint32_t extract_mode(uint32_t frame)
{
    return (frame >> 4) & 7u;
}

uint32_t update_mode(uint32_t frame, uint32_t mode)
{
    return (frame & ~(7u << 4)) | ((mode & 7u) << 4);
}

uint32_t sum_samples(const uint8_t *samples, uint32_t count)
{
    uint32_t sum = 0;

    for (uint32_t index = 0; index < count; ++index) {
        sum += samples[index];
    }
    return sum;
}
