---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-9
title: 统计信息（Statistics）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_统计信息（Statistics）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

跟踪并报告子系统事件计数器。

<a id="details"></a>

跟踪并报告子系统事件计数器（Subsystem Event Counters）。统计（Statistics）是按模块组织的事件计数器，用于故障排查、维护和使用情况监测。统计组织为具名组（Groups），每组包含一组条目（Entries），每个条目对应一个计数器。启用 CONFIG_STATS_NAMES 时，各条目还可以具有名称。可通过统计管理子系统（Statistics Management Subsystem）获取统计数据。统计适合记录传输尝试、已处理字节、可恢复错误、阈值命中等运行时事件，或其他有助于诊断行为的数值，无需新增自定义管理命令。

这里有两个内容大体重复的统计部分，用于可选地为统计命名。STATS_SECT_START 与 STATS_SECT_END 声明统计结构体定义；STATS_SECT_DECL 创建结构体声明，使这些统计能够声明为全局结构体；STATS_NAME_START 与 STATS_NAME_END 则用于为统计条目命名。

统计条目（Statistics Entries）可声明为多种整数类型，但同一结构体中的所有统计必须大小一致，且均为无符号类型（Unsigned）：STATS_SECT_ENTRY() 为默认的 32 位条目；STATS_SECT_ENTRY16() 为 16 位，在需要满足特定 RAM 或代码大小限制时使用较小的统计；STATS_SECT_ENTRY32() 为 32 位；STATS_SECT_ENTRY64() 为 64 位，适合存储较大的数据块。

静态条目声明之后是统计名称声明。未定义 CONFIG_STATS_NAMES 时，这部分会被编译移除；定义时，统计名称会被存储并返回给管理 API。未定义时，按需生成以下格式的临时名称：

```text
s<stat-idx>
```

例如 "s0"、"s1" 等。示例（Example）：

```c
STATS_SECT_START(my_driver_stats)
STATS_SECT_ENTRY(rx_packets)
STATS_SECT_ENTRY(rx_bytes)
STATS_SECT_ENTRY(errors)
STATS_SECT_END;

STATS_NAME_START(my_driver_stats)
STATS_NAME(my_driver_stats, rx_packets)
STATS_NAME(my_driver_stats, rx_bytes)
STATS_NAME(my_driver_stats, errors)
STATS_NAME_END(my_driver_stats);

static STATS_SECT_DECL(my_driver_stats) stats;

static int my_driver_init(void)
{
    int rc;

    rc = STATS_INIT_AND_REG(stats, STATS_SIZE_32, "my_driver");
    if (rc != 0) {
        return rc;
    }

    return 0;
}

static void my_driver_rx_complete(size_t len)
{
    STATS_INC(stats, rx_packets);
    STATS_INCN(stats, rx_bytes, len);
}

static void my_driver_error(void)
{
    STATS_INC(stats, errors);
}
```

原页面示例符号说明（Symbol Definitions）：

- `#define STATS_SECT_DECL(group__)`：声明统计组结构体。定义于 stats.h:163。
- `#define STATS_SECT_END`：结束统计组结构体定义。定义于 stats.h:169。
- `#define STATS_NAME(sectname__, entry__)`：向统计条目名称映射添加条目名称。定义于 stats.h:519。
- `#define STATS_NAME_START(sectname__)`：开始统计条目名称映射。定义于 stats.h:510。
- `#define STATS_NAME_END(sectname__)`：结束统计条目名称映射。定义于 stats.h:527。
- `#define STATS_SIZE_32`：32 位统计条目的大小，以字节表示。定义于 stats.h:220。
- `#define STATS_INC(group__, var__)`：递增统计条目。定义于 stats.h:255。
- `#define STATS_INIT_AND_REG(group__, size__, name__)`：初始化并注册统计组。定义于 stats.h:311。
- `#define STATS_INCN(group__, var__, n__)`：将统计条目增加指定量。定义于 stats.h:243。
- `#define STATS_SECT_START(group__)`：开始统计组结构体定义。定义于 stats.h:181。
- `#define STATS_SECT_ENTRY(var__)`：在组结构体中声明一个 32 位统计条目。定义于 stats.h:190。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_stats_2Eh"></a>

```c
file stats.h
```

相关声明：[stats.h](../api_file_clock_network_reference/P024_zephyr__stats__stats.h_文件参考.md)。

统计信息（Statistics）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_stats_5Fname_5Fmap"></a>

```c
struct stats_name_map
```

相关声明：[stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)。

描述一个生成的统计条目名称（Statistic Entry Name）。

<a id="r_stats_5Fhdr"></a>

```c
struct stats_hdr
```

相关声明：[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

存储单个统计组（Statistics Group）的元数据。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.3\_遍历与查找（Walking and Lookup）

<a id="r_gaa4f75157451e12d76e5cc0fbc65063da"></a>

```c
typedef int stats_walk_fn(struct stats_hdr *hdr, void *arg, const char *name, uint16_t off)
```

相关声明：[stats_walk_fn](#gaa4f75157451e12d76e5cc0fbc65063da)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

遍历（Walk）时对每个统计条目应用的函数。

<a id="r_ga454c4c833e25fcb8808c4b85db4f0291"></a>

```c
typedef int stats_group_walk_fn(struct stats_hdr *hdr, void *arg)
```

相关声明：[stats_group_walk_fn](#ga454c4c833e25fcb8808c4b85db4f0291)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

对每个已注册统计组应用的函数。

<a id="r_gae6aeebd4e8f57b0b82c6dcf69bddcc64"></a>

```c
int stats_walk (struct stats_hdr *hdr, stats_walk_fn *walk_cb, void *arg)
```

相关声明：[stats_walk](#gae6aeebd4e8f57b0b82c6dcf69bddcc64)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_walk_fn](#gaa4f75157451e12d76e5cc0fbc65063da)。

对组中的每个统计条目应用函数。

<a id="r_ga3b431d3e69b3978bfd81268b70eda6e0"></a>

```c
int stats_group_walk (stats_group_walk_fn *walk_cb, void *arg)
```

相关声明：[stats_group_walk](#ga3b431d3e69b3978bfd81268b70eda6e0)、[stats_group_walk_fn](#ga454c4c833e25fcb8808c4b85db4f0291)。

对每个已注册统计组应用函数。

<a id="r_ga11402b3eb75529d1ebf7b7b87c9e20f8"></a>

```c
struct stats_hdr * stats_group_get_next (const struct stats_hdr *cur)
```

相关声明：[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_group_get_next](#ga11402b3eb75529d1ebf7b7b87c9e20f8)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

获取下一个已注册统计组（Statistics Group）。

<a id="r_ga8cb611a313ede400835eb56a4d209c7a"></a>

```c
struct stats_hdr * stats_group_find (const char *name)
```

相关声明：[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_group_find](#ga8cb611a313ede400835eb56a4d209c7a)。

获取具有指定名称的统计组（Statistics Group）。

## 9.4\_初始化与注册（Initialization and Registration）

<a id="r_ga5e2c74f2c77a8cf1d2a43eb7190a9b93"></a>

```c
void stats_init (struct stats_hdr *shdr, uint8_t size, uint16_t cnt, const struct stats_name_map *map, uint16_t map_cnt)
```

相关声明：[stats_init](#ga5e2c74f2c77a8cf1d2a43eb7190a9b93)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

初始化统计组（Statistics Group）。

<a id="r_ga0a26d63646d1157509afcc370738b9d8"></a>

```c
int stats_register (const char *name, struct stats_hdr *shdr)
```

相关声明：[stats_register](#ga0a26d63646d1157509afcc370738b9d8)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

注册要管理的统计组（Statistics Group）。

<a id="r_ga687b3da8d0e3e0f55e8ea8d5e47eaf2a"></a>

```c
int stats_init_and_reg (struct stats_hdr *hdr, uint8_t size, uint16_t cnt, const struct stats_name_map *map, uint16_t map_cnt, const char *name)
```

相关声明：[stats_init_and_reg](#ga687b3da8d0e3e0f55e8ea8d5e47eaf2a)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

初始化并注册统计组（Statistics Group）。

<a id="r_gaca8e338b464a6c317232d7029c80f206"></a>

```c
void stats_reset (struct stats_hdr *shdr)
```

相关声明：[stats_reset](#gaca8e338b464a6c317232d7029c80f206)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

将指定统计组（Statistics Group）清零。

<a id="r_ga7a3f6d5dc044e6948998b8bc19efa493"></a>

```c
#define STATS_INIT_AND_REG(group__, size__, name__)
```

相关声明：[STATS_INIT_AND_REG](#ga7a3f6d5dc044e6948998b8bc19efa493)。

初始化并注册统计组（Statistics Group）。

## 9.5\_统计组声明（Statistics Group Declarations）

<a id="r_ga21af7c98ccb9abb9464b9ef9358be880"></a>

```c
#define STATS_SECT_DECL(group__)
```

相关声明：[STATS_SECT_DECL](#ga21af7c98ccb9abb9464b9ef9358be880)。

声明统计组结构体（Stat Group Struct）。

<a id="r_ga4124f8c0a9ffb78d8be608a780676785"></a>

```c
#define STATS_SECT_END }
```

相关声明：[STATS_SECT_END](#ga4124f8c0a9ffb78d8be608a780676785)。

结束统计组结构体定义（Stats Group Struct Definition）。

<a id="r_gae8e85c3ce2d901f4668d7237b19999fe"></a>

```c
#define STATS_SECT_START(group__)
```

相关声明：[STATS_SECT_START](#gae8e85c3ce2d901f4668d7237b19999fe)。

开始统计组结构体定义（Stats Group Struct Definition）。

<a id="r_gafe8558503af10039b08a11f89c722783"></a>

```c
#define STATS_SECT_ENTRY(var__)
```

相关声明：[STATS_SECT_ENTRY](#gafe8558503af10039b08a11f89c722783)。

在组结构体内声明 32 位统计条目（Stat Entry）。

<a id="r_ga681ab1b4b39cb753e362eedbd78943a9"></a>

```c
#define STATS_SECT_ENTRY16(var__)
```

相关声明：[STATS_SECT_ENTRY16](#ga681ab1b4b39cb753e362eedbd78943a9)。

在组结构体内声明 16 位统计条目（Stat Entry）。

<a id="r_ga592329613cc77cfa5dee3e1d3b16dd93"></a>

```c
#define STATS_SECT_ENTRY32(var__)
```

相关声明：[STATS_SECT_ENTRY32](#ga592329613cc77cfa5dee3e1d3b16dd93)。

在组结构体内声明 32 位统计条目（Stat Entry）。

<a id="r_ga589764c7a1e7d60fe0285b839c6c36b4"></a>

```c
#define STATS_SECT_ENTRY64(var__)
```

相关声明：[STATS_SECT_ENTRY64](#ga589764c7a1e7d60fe0285b839c6c36b4)。

在组结构体内声明 64 位统计条目（Stat Entry）。

<a id="r_ga6b5129b5d9a2ade6ecfd011ad2c4377f"></a>

```c
#define STATS_SIZE_16 (sizeof(uint16_t))
```

相关声明：[STATS_SIZE_16](#ga6b5129b5d9a2ade6ecfd011ad2c4377f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

16 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="r_ga68323f9fddd985e9042bdca5b7f830b5"></a>

```c
#define STATS_SIZE_32 (sizeof(uint32_t))
```

相关声明：[STATS_SIZE_32](#ga68323f9fddd985e9042bdca5b7f830b5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

32 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="r_gafc9977fb100d17785440abf9cb93e63d"></a>

```c
#define STATS_SIZE_64 (sizeof(uint64_t))
```

相关声明：[STATS_SIZE_64](#gafc9977fb100d17785440abf9cb93e63d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

64 位统计条目大小（Statistics Entry Size），单位为字节。

## 9.6\_计数器更新辅助接口（Counter Update Helpers）

<a id="r_gac5d5050e8684027a3efb5a8e7a830be6"></a>

```c
#define STATS_INCN(group__, var__, n__)
```

相关声明：[STATS_INCN](#gac5d5050e8684027a3efb5a8e7a830be6)。

将统计条目（Statistic Entry）增加指定数量。

<a id="r_ga725e1bf6b2c486de9603954974d6315a"></a>

```c
#define STATS_INC(group__, var__)
```

相关声明：[STATS_INC](#ga725e1bf6b2c486de9603954974d6315a)。

将统计条目（Statistic Entry）递增。

<a id="r_ga147f7c33929d040495d7bd526f5fca85"></a>

```c
#define STATS_SET(group__, var__, n__)
```

相关声明：[STATS_SET](#ga147f7c33929d040495d7bd526f5fca85)。

将统计条目（Statistic Entry）设为指定数量。

<a id="r_ga1cce9ba94338a7fb027c78b32e638da5"></a>

```c
#define STATS_CLEAR(group__, var__)
```

相关声明：[STATS_CLEAR](#ga1cce9ba94338a7fb027c78b32e638da5)。

将统计条目（Statistic Entry）设为零。

## 9.7\_可选统计名称（Optional Statistic Names）

这些宏定义启用 CONFIG_STATS_NAMES 时使用的可选条目名称映射（Entry-name Map）。

禁用此选项时，名称宏不会编译到程序中，统计条目使用 s0、s1 等自动生成的名称报告。

<a id="r_ga5fba46e743c05b4f36df91a86c37e30d"></a>

```c
#define STATS_NAME_START(sectname__)
```

相关声明：[STATS_NAME_START](#ga5fba46e743c05b4f36df91a86c37e30d)。

开始统计条目名称映射（Statistics Entry Name Map）。

<a id="r_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>

```c
#define STATS_NAME(sectname__, entry__)
```

相关声明：[STATS_NAME](#ga498c4ee3baf1a4e21a6a5b0766d9b74e)。

向统计条目名称映射（Statistics Entry Name Map）添加条目名称。

<a id="r_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>

```c
#define STATS_NAME_END(sectname__)
```

相关声明：[STATS_NAME_END](#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)。

结束统计条目名称映射（Statistics Entry Name Map）。

<a id="r_gad1a94bded5ab34ac48c0dfd4cbdc168f"></a>

```c
#define STATS_NAME_INIT_PARMS(name__)
```

相关声明：[STATS_NAME_INIT_PARMS](#gad1a94bded5ab34ac48c0dfd4cbdc168f)。

为 stats_init() 展开名称映射参数（Name-map Arguments）。

## 9.8\_详细说明（Detailed Documentation）

<a id="ga1cce9ba94338a7fb027c78b32e638da5"></a>

### `STATS_CLEAR`

```c
#define STATS_CLEAR ( group__, var__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
((group__).var__ = 0)
```

将统计条目（Statistic Entry）设为零。

将统计条目（Statistic Entry）置零。未定义 CONFIG_STATS 时，编译移除此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 包含待清零条目的组（Group）。 |
| `var__` | 要清零的统计条目（Statistic Entry）。 |

<a id="ga725e1bf6b2c486de9603954974d6315a"></a>

### `STATS_INC`

```c
#define STATS_INC ( group__, var__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
STATS_INCN(group__, var__, 1)
```

将统计条目（Statistic Entry）递增。

将统计条目（Statistic Entry）加 1。未定义 CONFIG_STATS 时，编译移除此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 包含待增加条目的组（Group）。 |
| `var__` | 要增加的统计条目（Statistic Entry）。 |

<a id="gac5d5050e8684027a3efb5a8e7a830be6"></a>

### `STATS_INCN`

```c
#define STATS_INCN ( group__, var__, n__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
((group__).var__ += (n__))
```

将统计条目（Statistic Entry）增加指定数量。

将统计条目（Statistic Entry）增加指定量。未定义 CONFIG_STATS 时，编译移除此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 包含待增加条目的组（Group）。 |
| `var__` | 要增加的统计条目（Statistic Entry）。 |
| `n__` | 统计条目要增加的量（Amount）。 |

<a id="ga7a3f6d5dc044e6948998b8bc19efa493"></a>

### `STATS_INIT_AND_REG`

```c
#define STATS_INIT_AND_REG ( group__, size__, name__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
stats_init_and_reg(                                              \
        &(group__).s_hdr,                                        \
        (size__),                                                \
        (sizeof(group__) - sizeof(struct stats_hdr)) / (size__), \
        STATS_NAME_INIT_PARMS(group__),                          \
        (name__))
```

初始化并注册统计组（Statistics Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 要初始化并注册的统计组（Statistics Group）。 |
| `size__` | 统计组中每个条目的大小（Entry Size），单位为字节，必须为 2（16 位）、4（32 位）或 8（64 位）。 |
| `name__` | 要注册的统计组名称（Statistics Group Name），必须在所有统计组中唯一。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EALREADY` | 同名统计组（Statistics Group）已经注册。 |

<a id="ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>

### `STATS_NAME`

```c
#define STATS_NAME ( sectname__, entry__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
{ offsetof(STATS_SECT_DECL(sectname__), entry__), #entry__ },
```

向统计条目名称映射（Statistics Entry Name Map）添加条目名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sectname__` | 传给 STATS_NAME_START 的统计组名称（Statistics Group Name）。 |
| `entry__` | 在统计组中声明的条目名称（Entry Name）。 |

<a id="ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>

### `STATS_NAME_END`

```c
#define STATS_NAME_END ( sectname__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
}
```

结束统计条目名称映射（Statistics Entry Name Map）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sectname__` | 传给 STATS_NAME_START 的统计组名称（Statistics Group Name）。 |

<a id="gad1a94bded5ab34ac48c0dfd4cbdc168f"></a>

### `STATS_NAME_INIT_PARMS`

```c
#define STATS_NAME_INIT_PARMS ( name__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
&(STATS_NAME_MAP_NAME(name__)[0]), \
(sizeof(STATS_NAME_MAP_NAME(name__)) / sizeof(struct stats_name_map))
```

为 stats_init() 展开名称映射参数（Name-map Arguments）。

此宏展开为 stats_init() 或 stats_init_and_reg() 所需的映射指针（Map Pointer）和映射条目数量（Map Entry Count）。禁用 CONFIG_STATS_NAMES 时，展开为 NULL, 0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name__` | 传给 STATS_NAME_START 的统计组名称（Statistics Group Name）。 |

<a id="ga5fba46e743c05b4f36df91a86c37e30d"></a>

### `STATS_NAME_START`

```c
#define STATS_NAME_START ( sectname__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
static const struct stats_name_map STATS_NAME_MAP_NAME(sectname__)[] = {
```

开始统计条目名称映射（Statistics Entry Name Map）。

将此宏与 STATS_NAME、STATS_NAME_END 配合使用，为统计组中声明的条目定义名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sectname__` | 传给 STATS_SECT_START 的统计组名称（Statistics Group Name）。 |

<a id="ga21af7c98ccb9abb9464b9ef9358be880"></a>

### `STATS_SECT_DECL`

```c
#define STATS_SECT_DECL ( group__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
struct stats_ ## group__
```

声明统计组结构体（Stat Group Struct）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 要赋给结构体标签（Structure Tag）的名称。 |

<a id="ga4124f8c0a9ffb78d8be608a780676785"></a>

### `STATS_SECT_END`

```c
#define STATS_SECT_END }
```

```c
#include <zephyr/stats/stats.h>
```

结束统计组结构体定义（Stats Group Struct Definition）。

<a id="gafe8558503af10039b08a11f89c722783"></a>

### `STATS_SECT_ENTRY`

```c
#define STATS_SECT_ENTRY ( var__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
uint32_t var__;
```

在组结构体内声明 32 位统计条目（Stat Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `var__` | 要赋给条目（Entry）的名称。 |

<a id="ga681ab1b4b39cb753e362eedbd78943a9"></a>

### `STATS_SECT_ENTRY16`

```c
#define STATS_SECT_ENTRY16 ( var__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
uint16_t var__;
```

在组结构体内声明 16 位统计条目（Stat Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `var__` | 要赋给条目（Entry）的名称。 |

<a id="ga592329613cc77cfa5dee3e1d3b16dd93"></a>

### `STATS_SECT_ENTRY32`

```c
#define STATS_SECT_ENTRY32 ( var__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
uint32_t var__;
```

在组结构体内声明 32 位统计条目（Stat Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `var__` | 要赋给条目（Entry）的名称。 |

<a id="ga589764c7a1e7d60fe0285b839c6c36b4"></a>

### `STATS_SECT_ENTRY64`

```c
#define STATS_SECT_ENTRY64 ( var__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
uint64_t var__;
```

在组结构体内声明 64 位统计条目（Stat Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `var__` | 要赋给条目（Entry）的名称。 |

<a id="gae8e85c3ce2d901f4668d7237b19999fe"></a>

### `STATS_SECT_START`

```c
#define STATS_SECT_START ( group__)
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
STATS_SECT_DECL(group__) { \
        struct stats_hdr s_hdr;
```

开始统计组结构体定义（Stats Group Struct Definition）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 统计组结构体名称（Stats Group Struct Name）。 |

<a id="ga147f7c33929d040495d7bd526f5fca85"></a>

### `STATS_SET`

```c
#define STATS_SET ( group__, var__, n__ )
```

```c
#include <zephyr/stats/stats.h>
```

展开值（Value）：

```c
((group__).var__ = (n__))
```

将统计条目（Statistic Entry）设为指定数量。

将统计条目（Statistic Entry）设置为指定量。未定义 CONFIG_STATS 时，编译移除此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group__` | 包含待增加条目的组（Group）。 |
| `var__` | 要增加的统计条目（Statistic Entry）。 |
| `n__` | 统计条目要设置为的值（Amount）。 |

<a id="ga6b5129b5d9a2ade6ecfd011ad2c4377f"></a>

### `STATS_SIZE_16`

```c
#define STATS_SIZE_16 (sizeof(uint16_t))
```

```c
#include <zephyr/stats/stats.h>
```

16 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="ga68323f9fddd985e9042bdca5b7f830b5"></a>

### `STATS_SIZE_32`

```c
#define STATS_SIZE_32 (sizeof(uint32_t))
```

```c
#include <zephyr/stats/stats.h>
```

32 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="gafc9977fb100d17785440abf9cb93e63d"></a>

### `STATS_SIZE_64`

```c
#define STATS_SIZE_64 (sizeof(uint64_t))
```

```c
#include <zephyr/stats/stats.h>
```

64 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="ga454c4c833e25fcb8808c4b85db4f0291"></a>

### `stats_group_walk_fn`

```c
typedef int stats_group_walk_fn(struct stats_hdr *hdr, void *arg)
```

```c
#include <zephyr/stats/stats.h>
```

对每个已注册统计组应用的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdr` | 正在遍历的统计组（Stats Group）。 |
| `arg` | 可选参数（Optional Argument）。 |

返回（Returns）：继续遍历（Walk）时为 0，中止遍历时为非零。

<a id="gaa4f75157451e12d76e5cc0fbc65063da"></a>

### `stats_walk_fn`

```c
typedef int stats_walk_fn(struct stats_hdr *hdr, void *arg, const char *name, uint16_t off)
```

```c
#include <zephyr/stats/stats.h>
```

遍历（Walk）时对每个统计条目应用的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdr` | 包含正在遍历的统计条目（Stat Entry）的组。 |
| `arg` | 可选参数（Optional Argument）。 |
| `name` | 要处理的统计条目名称（Statistic Entry Name）。 |
| `off` | 条目相对于 hdr 的偏移量（Offset）。 |

返回（Returns）：继续遍历（Walk）时为 0，中止遍历时为非零。

<a id="ga8cb611a313ede400835eb56a4d209c7a"></a>

### `stats_group_find()`

```c
struct stats_hdr * stats_group_find ( const char * name)
```

```c
#include <zephyr/stats/stats.h>
```

获取具有指定名称的统计组（Statistics Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要查找的统计组名称（Statistics Group Name）。 |

返回（Returns）：成功时为指向所获取组的指针；没有匹配的已注册组时为 NULL。

<a id="ga11402b3eb75529d1ebf7b7b87c9e20f8"></a>

### `stats_group_get_next()`

```c
struct stats_hdr * stats_group_get_next ( const struct stats_hdr * cur)
```

```c
#include <zephyr/stats/stats.h>
```

获取下一个已注册统计组（Statistics Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cur` | 要获取其后继（Successor）的组；传入 NULL 则获取第一个组。 |

返回（Returns）：成功时为指向所获取组的指针；没有更多组时为 NULL。

<a id="ga3b431d3e69b3978bfd81268b70eda6e0"></a>

### `stats_group_walk()`

```c
int stats_group_walk ( stats_group_walk_fn * walk_cb, void * arg )
```

```c
#include <zephyr/stats/stats.h>
```

对每个已注册统计组应用函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `walk_cb` | 要对每个统计组（Stat Group）执行的函数。 |
| `arg` | 传给回调的可选参数（Optional Argument）。 |

返回（Returns）：遍历完成时为 0，遍历中止时为非零。

<a id="ga5e2c74f2c77a8cf1d2a43eb7190a9b93"></a>

### `stats_init()`

```c
void stats_init ( struct stats_hdr * shdr, uint8_t size, uint16_t cnt, const struct stats_name_map * map, uint16_t map_cnt )
```

```c
#include <zephyr/stats/stats.h>
```

初始化统计组（Statistics Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shdr` | 统计结构体头部（Statistics Structure Header），包含统计节名称、条目大小、统计数量等信息。 |
| `size` | 每个统计元素大小（Statistics Element Size），单位为字节，必须为 2（16 位）、4（32 位）或 8（64 位）。 |
| `cnt` | 统计组中的元素数量（Number of Elements）。 |
| `map` | 统计偏移量到名称的映射（Offset-to-name Mapping）。 |
| `map_cnt` | 统计映射中的条目数量（Number of Map Items）。 |

<a id="ga687b3da8d0e3e0f55e8ea8d5e47eaf2a"></a>

### `stats_init_and_reg()`

```c
int stats_init_and_reg ( struct stats_hdr * hdr, uint8_t size, uint16_t cnt, const struct stats_name_map * map, uint16_t map_cnt, const char * name )
```

```c
#include <zephyr/stats/stats.h>
```

初始化并注册统计组（Statistics Group）。

初始化并注册统计组（Statistics Group）。注意：建议使用 STATS_INIT_AND_REG 宏代替此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdr` | 要初始化并注册的统计组头部（Statistics Group Header）。 |
| `size` | 每个统计元素大小（Statistics Element Size），单位为字节，必须为 2（16 位）、4（32 位）或 8（64 位）。 |
| `cnt` | 统计组中的元素数量（Number of Elements）。 |
| `map` | 统计偏移量到名称的映射（Offset-to-name Mapping）。 |
| `map_cnt` | 统计映射中的条目数量（Number of Map Items）。 |
| `name` | 要注册的统计组名称（Statistics Group Name），必须在所有统计组中唯一。名称重复时，此函数返回 -EALREADY。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EALREADY` | 同名统计组（Statistics Group）已经注册。 |

**参阅（See Also）**：另请参见（See Also）：STATS_INIT_AND_REG。

<a id="ga0a26d63646d1157509afcc370738b9d8"></a>

### `stats_register()`

```c
int stats_register ( const char * name, struct stats_hdr * shdr )
```

```c
#include <zephyr/stats/stats.h>
```

注册要管理的统计组（Statistics Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要注册的统计组名称（Statistics Group Name），必须在所有统计组中唯一。名称重复时，此函数返回 -EALREADY。 |
| `shdr` | 要注册的统计组（Statistics Group）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EALREADY` | 同名统计组（Statistics Group）已经注册。 |

<a id="gaca8e338b464a6c317232d7029c80f206"></a>

### `stats_reset()`

```c
void stats_reset ( struct stats_hdr * shdr)
```

```c
#include <zephyr/stats/stats.h>
```

将指定统计组（Statistics Group）清零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shdr` | 要清零的统计组（Statistics Group）。 |

<a id="gae6aeebd4e8f57b0b82c6dcf69bddcc64"></a>

### `stats_walk()`

```c
int stats_walk ( struct stats_hdr * hdr, stats_walk_fn * walk_cb, void * arg )
```

```c
#include <zephyr/stats/stats.h>
```

对组中的每个统计条目应用函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdr` | 要操作的统计组（Stats Group）。 |
| `walk_cb` | 要对每个统计条目（Stat Entry）执行的函数。 |
| `arg` | 传给回调的可选参数（Optional Argument）。 |

返回（Returns）：遍历完成时为 0，遍历中止时为非零。


## 9.9\_原页交叉引用（Cross References）

- [stats.h](../api_file_clock_network_reference/P024_zephyr__stats__stats.h_文件参考.md)
- [stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)
- [stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [CONFIG_STATS_NAMES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS_NAMES)
- [统计信息管理（Statistics Management）](../api_service_topic_reference/P014_统计信息管理（Statistics Management）.md)

<a id="header-details"></a>
<a id="agroup__stats__apis_html_ga21af7c98ccb9abb9464b9ef9358be880"></a>
<a id="agroup__stats__apis_html_ga4124f8c0a9ffb78d8be608a780676785"></a>
<a id="agroup__stats__apis_html_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>
<a id="agroup__stats__apis_html_ga5fba46e743c05b4f36df91a86c37e30d"></a>
<a id="agroup__stats__apis_html_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>
<a id="agroup__stats__apis_html_ga68323f9fddd985e9042bdca5b7f830b5"></a>
<a id="agroup__stats__apis_html_ga725e1bf6b2c486de9603954974d6315a"></a>
<a id="agroup__stats__apis_html_ga7a3f6d5dc044e6948998b8bc19efa493"></a>
<a id="agroup__stats__apis_html_gac5d5050e8684027a3efb5a8e7a830be6"></a>
<a id="agroup__stats__apis_html_gae8e85c3ce2d901f4668d7237b19999fe"></a>
<a id="agroup__stats__apis_html_gafe8558503af10039b08a11f89c722783"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__stats__apis_html_ga687b3da8d0e3e0f55e8ea8d5e47eaf2a"></a>
<a id="agroup__stats__apis_html_gad1a94bded5ab34ac48c0dfd4cbdc168f"></a>
<a id="astructstats__hdr_html"></a>
<a id="astructstats__name__map_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_PCIe 主机（PCIe Host）.md) · [返回大纲](大纲.md) · [下一章](P010_定时器 API（Timer APIs）.md)
