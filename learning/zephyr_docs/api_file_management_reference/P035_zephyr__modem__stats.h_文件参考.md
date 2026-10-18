---
id: learning.zephyr-docs.api-file-management-reference.page-35
title: zephyr__modem__stats.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_modem\_\_stats.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.1\_函数（Functions）

<a id="r_ac97a44071b31768bd2d39bef27bfd746"></a>

```c
void modem_stats_buffer_init (struct modem_stats_buffer *buffer, const char *name, uint32_t size)
```

相关声明：[modem_stats_buffer_init](#ac97a44071b31768bd2d39bef27bfd746)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化调制解调器统计缓冲区（modem statistics buffer）。

<a id="r_af4ccdf8a97586021431d858565a8f28f"></a>

```c
void modem_stats_buffer_advertise_length (struct modem_stats_buffer *buffer, uint32_t length)
```

相关声明：[modem_stats_buffer_advertise_length](#af4ccdf8a97586021431d858565a8f28f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通告调制解调器统计缓冲区大小。

## 35.2\_详细说明（Detailed Documentation）

<a id="af4ccdf8a97586021431d858565a8f28f"></a>

### `modem_stats_buffer_advertise_length()`

```c
void modem_stats_buffer_advertise_length ( struct modem_stats_buffer * buffer, uint32_t length )
```

通告调制解调器统计缓冲区大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buffer` | 调制解调器统计缓冲区实例。 |
| `length` | 缓冲区长度。 |

**说明（Note）**：注意：缓冲区大小变化时调用；可安全地从中断服务程序（ISR）调用。

<a id="ac97a44071b31768bd2d39bef27bfd746"></a>

### `modem_stats_buffer_init()`

```c
void modem_stats_buffer_init ( struct modem_stats_buffer * buffer, const char * name, uint32_t size )
```

初始化调制解调器统计缓冲区（modem statistics buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buffer` | 调制解调器统计缓冲区实例。 |
| `name` | 缓冲区实例名称。 |
| `size` | 缓冲区大小。 |


## 35.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P539_stats.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P034_zephyr__drivers__mm__mm_drv_bank.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__modem__ubx__keys.h_文件参考.md)
