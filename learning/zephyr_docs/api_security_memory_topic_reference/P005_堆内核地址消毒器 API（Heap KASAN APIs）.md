---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-5
title: 堆内核地址消毒器 API（Heap KASAN APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_堆内核地址消毒器 API（Heap KASAN APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga9bd0af55bae901bbea20e064d6171ee2"></a>

```c
#define SYS_HEAP_KASAN_SHADOW_BITS(_sz)
```

相关声明：[SYS_HEAP_KASAN_SHADOW_BITS](#ga9bd0af55bae901bbea20e064d6171ee2)。

大小为 `_sz` 字节的堆所需的影子位（shadow bits），每个粒度单元（granule）对应一位。

<a id="r_ga2714e1169d119a8e50265d2bced8d005"></a>

```c
#define SYS_HEAP_KASAN_SHADOW_BUNDLES(_sz)
```

相关声明：[SYS_HEAP_KASAN_SHADOW_BUNDLES](#ga2714e1169d119a8e50265d2bced8d005)。

大小为 `_sz` 字节的堆，其影子存储所需的 `uint32_t` 组数（bundle count）。

<a id="r_ga413c090cc09658ebc9b16406cd25558a"></a>

```c
#define SYS_HEAP_KASAN_ENABLE(_heap_name, _heap_sz)
```

相关声明：[SYS_HEAP_KASAN_ENABLE](#ga413c090cc09658ebc9b16406cd25558a)。

对 `struct sys_heap` 启用内核地址消毒器（KASAN）的影子跟踪（shadow tracking）。

<a id="r_ga0dc8b79da83fe6799e3c2c3b08b8c15b"></a>

```c
#define K_HEAP_KASAN_ENABLE(_heap_name, _heap_sz)
```

相关声明：[K_HEAP_KASAN_ENABLE](#ga0dc8b79da83fe6799e3c2c3b08b8c15b)。

对 `struct k_heap`（`K_HEAP_DEFINE`）启用 KASAN 影子跟踪。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga34f66dfa0f04034e756a4c2474a03f1b"></a>

```c
void heap_kasan_report (uintptr_t addr, size_t size)
```

相关声明：[heap_kasan_report](#ga34f66dfa0f04034e756a4c2474a03f1b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

报告堆的 KASAN 违规（violation）。

<a id="r_gad2cbd504b82b27ecf48eba519fc8c9ab"></a>

```c
void heap_kasan_register (struct sys_heap *heap, sys_bitarray_t *ba)
```

相关声明：[heap_kasan_register](#gad2cbd504b82b27ecf48eba519fc8c9ab)、[sys_heap](../lowheap_reference/P004_底层堆对象.md)、[sys_bitarray_t](../bitarray_reference/P001_位数组公共接口.md#ga168a1da9ac2bee523bdc9778e94fd841)。

将影子位数组（shadow bitarray）与堆关联，以进行 KASAN 跟踪。

## 5.3\_详细说明（Detailed Documentation）

<a id="ga0dc8b79da83fe6799e3c2c3b08b8c15b"></a>

### `K_HEAP_KASAN_ENABLE`

```c
#define K_HEAP_KASAN_ENABLE ( _heap_name, _heap_sz )
```

```c
#include <zephyr/sys/heap_kasan.h>
```

展开值（Value）：

```c
static uint32_t _heap_name##_kasan_bundles[SYS_HEAP_KASAN_SHADOW_BUNDLES( \
        MAX(_heap_sz, Z_HEAP_MIN_SIZE))] __noinit __aligned(4); \
static sys_bitarray_t _heap_name##_kasan_ba = { \
        .num_bits = SYS_HEAP_KASAN_SHADOW_BITS(MAX(_heap_sz, Z_HEAP_MIN_SIZE)), \
        .num_bundles = SYS_HEAP_KASAN_SHADOW_BUNDLES(MAX(_heap_sz, Z_HEAP_MIN_SIZE)), \
        .bundles = _heap_name##_kasan_bundles, \
}; \
static int _heap_name##_kasan_init_fn(void) \
{ \
        heap_kasan_register(&(_heap_name).heap, &_heap_name##_kasan_ba); \
        return 0; \
} \
SYS_INIT(_heap_name##_kasan_init_fn, PRE_KERNEL_1, 0)
```

对 `struct k_heap`（`K_HEAP_DEFINE`）启用 KASAN 影子跟踪。

应放在文件作用域中，位于 `K_HEAP_DEFINE` 之后。分配静态影子缓冲区（Static Shadow Buffer），并在 `PRE_KERNEL_1`、优先级 0 时将其注册到堆；早于位于 `(PRE_KERNEL_1, CONFIG_KERNEL_INIT_PRIORITY_OBJECTS)` 的静态堆初始化。

使用示例：

原始示例（Example）：

```c
K_HEAP_DEFINE(my_heap, 4096);
K_HEAP_KASAN_ENABLE(my_heap, 4096);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_heap_name` | `k_heap` 变量名称。 |
| `_heap_sz` | 与传给 `K_HEAP_DEFINE` 相同的大小，必须是编译时常量（Compile-time Constant）。 |

<a id="ga413c090cc09658ebc9b16406cd25558a"></a>

### `SYS_HEAP_KASAN_ENABLE`

```c
#define SYS_HEAP_KASAN_ENABLE ( _heap_name, _heap_sz )
```

```c
#include <zephyr/sys/heap_kasan.h>
```

展开值（Value）：

```c
static uint32_t \
        _heap_name##_kasan_bundles[SYS_HEAP_KASAN_SHADOW_BUNDLES(_heap_sz)] __noinit \
        __aligned(4); \
static sys_bitarray_t _heap_name##_kasan_ba = { \
        .num_bits = SYS_HEAP_KASAN_SHADOW_BITS(_heap_sz), \
        .num_bundles = SYS_HEAP_KASAN_SHADOW_BUNDLES(_heap_sz), \
        .bundles = _heap_name##_kasan_bundles, \
}; \
static int _heap_name##_kasan_init_fn(void) \
{ \
        heap_kasan_register(&(_heap_name), &_heap_name##_kasan_ba); \
        return 0; \
} \
SYS_INIT(_heap_name##_kasan_init_fn, PRE_KERNEL_1, 0)
```

对 `struct sys_heap` 启用内核地址消毒器（KASAN）的影子跟踪（shadow tracking）。

应放在文件作用域中，位于 `sys_heap` 声明之后。分配静态影子缓冲区（Static Shadow Buffer），并在 `PRE_KERNEL_1`、优先级 0 时将其注册到堆。必须在此后调用 `sys_heap_init()`。

使用示例：

原始示例（Example）：

```c
static char heap_buf[4096];
static struct sys_heap my_heap;

SYS_HEAP_KASAN_ENABLE(my_heap, sizeof(heap_buf));

// call sys_heap_init(&my_heap, heap_buf, sizeof(heap_buf)) at runtime
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_heap_name` | `sys_heap` 变量名称。 |
| `_heap_sz` | 堆缓冲区大小，单位为字节，必须是编译时常量（Compile-time Constant）。 |

<a id="ga9bd0af55bae901bbea20e064d6171ee2"></a>

### `SYS_HEAP_KASAN_SHADOW_BITS`

```c
#define SYS_HEAP_KASAN_SHADOW_BITS ( _sz)
```

```c
#include <zephyr/sys/heap_kasan.h>
```

展开值（Value）：

```c
((_sz) / SYS_HEAP_KASAN_GRANULE)
```

大小为 `_sz` 字节的堆所需的影子位（shadow bits），每个粒度单元（granule）对应一位。

<a id="ga2714e1169d119a8e50265d2bced8d005"></a>

### `SYS_HEAP_KASAN_SHADOW_BUNDLES`

```c
#define SYS_HEAP_KASAN_SHADOW_BUNDLES ( _sz)
```

```c
#include <zephyr/sys/heap_kasan.h>
```

展开值（Value）：

```c
DIV_ROUND_UP(SYS_HEAP_KASAN_SHADOW_BITS(_sz), 32)
```

大小为 `_sz` 字节的堆，其影子存储所需的 `uint32_t` 组数（bundle count）。

<a id="gad2cbd504b82b27ecf48eba519fc8c9ab"></a>

### `heap_kasan_register()`

```c
void heap_kasan_register ( struct sys_heap * heap, sys_bitarray_t * ba )
```

```c
#include <zephyr/sys/heap_kasan.h>
```

将影子位数组（shadow bitarray）与堆关联，以进行 KASAN 跟踪。

为构建时未通过 `SYS_HEAP_KASAN_ENABLE()` 或 `K_HEAP_KASAN_ENABLE()` 注册的堆启用内核地址消毒器（KASAN）影子跟踪（Shadow Tracking），适用于动态创建的堆。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `heap` | 要跟踪的 `sys_heap`。 |
| `ba` | 影子位数组（Shadow Bitarray），至少包含 `SYS_HEAP_KASAN_SHADOW_BITS(heap_size)` 位，由 `SYS_HEAP_KASAN_SHADOW_BUNDLES(heap_size)` 个 `uint32_t` 单元（Bundles）提供存储。 |

**警告（Warning）**：**警告（Warning）：**必须在 `sys_heap_init()` 之前调用。之后调用无效，该堆不会受到跟踪。

<a id="ga34f66dfa0f04034e756a4c2474a03f1b"></a>

### `heap_kasan_report()`

```c
void heap_kasan_report ( uintptr_t addr, size_t size )
```

```c
#include <zephyr/sys/heap_kasan.h>
```

报告堆的 KASAN 违规（violation）。

弱符号默认实现（Weak Default）调用 `k_panic()`。测试代码可覆盖它，以便在不触发内核崩溃（Panic）的情况下截获违规。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 发生违规的地址（Violating Address）。 |
| `size` | 写入大小，单位为字节。 |


## 5.4\_原页交叉引用（Cross References）

- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sys_heap](../lowheap_reference/P004_底层堆对象.md)
- [k_heap](../heap_reference/P002_内核堆结构.md)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [sys_bitarray_t](../bitarray_reference/P001_位数组公共接口.md#ga168a1da9ac2bee523bdc9778e94fd841)
- [zephyr/sys/heap_kasan.h](../api_file_management_reference/P020_zephyr__sys__heap_kasan.h_文件参考.md)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [K_HEAP_DEFINE](../heap_reference/P001_内核堆公共接口.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)
- [sys_heap_init()](../lowheap_reference/P001_底层堆分配接口.md#ga520768606a3c28b084cf11f8ec82fae6)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [k_panic()](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html#aedd541f707b1463aaac15c7798340329)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bitarray__apis_html_ga168a1da9ac2bee523bdc9778e94fd841"></a>
<a id="agroup__heap__kasan__apis_html_ga2714e1169d119a8e50265d2bced8d005"></a>
<a id="agroup__heap__kasan__apis_html_ga9bd0af55bae901bbea20e064d6171ee2"></a>
<a id="agroup__sys-util_html_gafa99ec4acc4ecb2dc3c2d05da15d0e3f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__heap__apis_html_ga795d7f1e6d5b7b19a7a50198d7829a0f"></a>
<a id="agroup__heap__kasan__apis_html_ga0dc8b79da83fe6799e3c2c3b08b8c15b"></a>
<a id="agroup__heap__kasan__apis_html_ga413c090cc09658ebc9b16406cd25558a"></a>
<a id="astructsys__heap_html"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_Intel I_O APIC中断控制器（Interrupt Controller）.md) · [返回大纲](大纲.md) · [下一章](P006_管理数据输入_输出（MDIO）.md)
