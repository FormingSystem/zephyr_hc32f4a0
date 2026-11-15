/* SPDX-License-Identifier: Apache-2.0 */
#include <stddef.h>
#include <stdint.h>

struct panel_record {
    uint8_t state;
    uint32_t count;
};

_Static_assert(offsetof(struct panel_record, state) == 0u, "state offset");
_Static_assert(offsetof(struct panel_record, count) == 4u, "count alignment");
_Static_assert(sizeof(struct panel_record) == 8u, "record stride");

/** @brief 保留一个对象，使目标文件中可观察到普通布局大小。 */
struct panel_record panel_record_example;
