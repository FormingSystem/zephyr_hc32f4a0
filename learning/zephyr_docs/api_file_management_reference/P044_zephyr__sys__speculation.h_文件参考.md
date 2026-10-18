---
id: learning.zephyr-docs.api-file-management-reference.page-44
title: zephyr__sys__speculation.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/speculation_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_sys\_\_speculation.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/speculation_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 44.1\_函数（Functions）

<a id="r_aa677f654a5febe3a9b7525e4306ede09"></a>

```c
static uint32_t k_array_index_sanitize (uint32_t index, uint32_t array_size)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_array_index_sanitize](#aa677f654a5febe3a9b7525e4306ede09)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

净化数组索引（sanitize array index），防范边界检查绕过攻击（bounds check bypass attacks），即 Spectre V1 漏洞。

## 44.2\_详细说明（Detailed Documentation）

<a id="aa677f654a5febe3a9b7525e4306ede09"></a>

### `k_array_index_sanitize()`

```c
uint32_t k_array_index_sanitize ( uint32_t index, uint32_t array_size )
```

声明属性：`inline`、`static`。

净化数组索引（sanitize array index），防范边界检查绕过攻击（bounds check bypass attacks），即 Spectre V1 漏洞。

具有推测执行（speculative execution）能力的 CPU 可能推测性地越过任意大小检查，并因微架构特性（micro-architectural properties）分析而泄露机密数据。此函数使用位运算而非分支指令，在推测执行路径上无条件地将所有越界索引截断为零。

使用示例：

使用示例：`if (index < size) { index = k_array_index_sanitize(index, size); data = array[index]; }`

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 已经验证但尚未使用的不可信数组索引（untrusted array index）。 |
| `array_size` | 数组大小（size）。 |

**返回（Returns）**：返回值：索引小于 `size` 时返回原索引值，否则返回 0。


## 44.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P185_speculation.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P043_zephyr__shared_irq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__drivers__i3c__target_device.h_文件参考.md)
