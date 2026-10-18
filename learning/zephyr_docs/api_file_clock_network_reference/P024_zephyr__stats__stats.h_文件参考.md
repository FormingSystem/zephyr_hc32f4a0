---
id: learning.zephyr-docs.api-file-clock-network-reference.page-24
title: zephyr__stats__stats.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_stats\_\_stats.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

统计信息（Statistics）。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/types.h>
```

查看此文件的源码。

统计信息（Statistics）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 统计组声明（Statistics Group Declarations）

<a id="r_ga21af7c98ccb9abb9464b9ef9358be880"></a>

```c
#define STATS_SECT_DECL(group__)
```

相关声明：[STATS_SECT_DECL](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga21af7c98ccb9abb9464b9ef9358be880)。

声明统计组结构体（Stat Group Struct）。

<a id="r_ga4124f8c0a9ffb78d8be608a780676785"></a>

```c
#define STATS_SECT_END }
```

相关声明：[STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)。

结束统计组结构体定义（Stats Group Struct Definition）。

<a id="r_gae8e85c3ce2d901f4668d7237b19999fe"></a>

```c
#define STATS_SECT_START(group__)
```

相关声明：[STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)。

开始统计组结构体定义（Stats Group Struct Definition）。

<a id="r_gafe8558503af10039b08a11f89c722783"></a>

```c
#define STATS_SECT_ENTRY(var__)
```

相关声明：[STATS_SECT_ENTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gafe8558503af10039b08a11f89c722783)。

在组结构体内声明 32 位统计条目（Stat Entry）。

<a id="r_ga681ab1b4b39cb753e362eedbd78943a9"></a>

```c
#define STATS_SECT_ENTRY16(var__)
```

相关声明：[STATS_SECT_ENTRY16](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga681ab1b4b39cb753e362eedbd78943a9)。

在组结构体内声明 16 位统计条目（Stat Entry）。

<a id="r_ga592329613cc77cfa5dee3e1d3b16dd93"></a>

```c
#define STATS_SECT_ENTRY32(var__)
```

相关声明：[STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)。

在组结构体内声明 32 位统计条目（Stat Entry）。

<a id="r_ga589764c7a1e7d60fe0285b839c6c36b4"></a>

```c
#define STATS_SECT_ENTRY64(var__)
```

相关声明：[STATS_SECT_ENTRY64](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga589764c7a1e7d60fe0285b839c6c36b4)。

在组结构体内声明 64 位统计条目（Stat Entry）。

<a id="r_ga6b5129b5d9a2ade6ecfd011ad2c4377f"></a>

```c
#define STATS_SIZE_16 (sizeof(uint16_t))
```

相关声明：[STATS_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga6b5129b5d9a2ade6ecfd011ad2c4377f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

16 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="r_ga68323f9fddd985e9042bdca5b7f830b5"></a>

```c
#define STATS_SIZE_32 (sizeof(uint32_t))
```

相关声明：[STATS_SIZE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga68323f9fddd985e9042bdca5b7f830b5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

32 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="r_gafc9977fb100d17785440abf9cb93e63d"></a>

```c
#define STATS_SIZE_64 (sizeof(uint64_t))
```

相关声明：[STATS_SIZE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gafc9977fb100d17785440abf9cb93e63d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

64 位统计条目大小（Statistics Entry Size），单位为字节。

<a id="define-members-1"></a>

### 计数器更新辅助接口（Counter Update Helpers）

<a id="r_gac5d5050e8684027a3efb5a8e7a830be6"></a>

```c
#define STATS_INCN(group__, var__, n__)
```

相关声明：[STATS_INCN](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gac5d5050e8684027a3efb5a8e7a830be6)。

将统计条目（Statistic Entry）增加指定数量。

<a id="r_ga725e1bf6b2c486de9603954974d6315a"></a>

```c
#define STATS_INC(group__, var__)
```

相关声明：[STATS_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga725e1bf6b2c486de9603954974d6315a)。

将统计条目（Statistic Entry）递增。

<a id="r_ga147f7c33929d040495d7bd526f5fca85"></a>

```c
#define STATS_SET(group__, var__, n__)
```

相关声明：[STATS_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga147f7c33929d040495d7bd526f5fca85)。

将统计条目（Statistic Entry）设为指定数量。

<a id="r_ga1cce9ba94338a7fb027c78b32e638da5"></a>

```c
#define STATS_CLEAR(group__, var__)
```

相关声明：[STATS_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga1cce9ba94338a7fb027c78b32e638da5)。

将统计条目（Statistic Entry）设为零。

<a id="define-members-2"></a>

### 可选统计名称（Optional Statistic Names）

这些宏定义启用 CONFIG_STATS_NAMES 时使用的可选条目名称映射（Entry-name Map）。

禁用此选项时，名称宏不会编译到程序中，统计条目使用 s0、s1 等自动生成的名称报告。

<a id="r_ga5fba46e743c05b4f36df91a86c37e30d"></a>

```c
#define STATS_NAME_START(sectname__)
```

相关声明：[STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)。

开始统计条目名称映射（Statistics Entry Name Map）。

<a id="r_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>

```c
#define STATS_NAME(sectname__, entry__)
```

相关声明：[STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)。

向统计条目名称映射（Statistics Entry Name Map）添加条目名称。

<a id="r_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>

```c
#define STATS_NAME_END(sectname__)
```

相关声明：[STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)。

结束统计条目名称映射（Statistics Entry Name Map）。

<a id="r_gad1a94bded5ab34ac48c0dfd4cbdc168f"></a>

```c
#define STATS_NAME_INIT_PARMS(name__)
```

相关声明：[STATS_NAME_INIT_PARMS](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gad1a94bded5ab34ac48c0dfd4cbdc168f)。

为 stats_init() 展开名称映射参数（Name-map Arguments）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 24.3\_初始化与注册（Initialization and Registration）

<a id="r_ga7a3f6d5dc044e6948998b8bc19efa493"></a>

```c
#define STATS_INIT_AND_REG(group__, size__, name__)
```

相关声明：[STATS_INIT_AND_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga7a3f6d5dc044e6948998b8bc19efa493)。

初始化并注册统计组（Statistics Group）。

<a id="r_ga5e2c74f2c77a8cf1d2a43eb7190a9b93"></a>

```c
void stats_init (struct stats_hdr *shdr, uint8_t size, uint16_t cnt, const struct stats_name_map *map, uint16_t map_cnt)
```

相关声明：[stats_init](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5e2c74f2c77a8cf1d2a43eb7190a9b93)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

初始化统计组（Statistics Group）。

<a id="r_ga0a26d63646d1157509afcc370738b9d8"></a>

```c
int stats_register (const char *name, struct stats_hdr *shdr)
```

相关声明：[stats_register](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga0a26d63646d1157509afcc370738b9d8)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

注册要管理的统计组（Statistics Group）。

<a id="r_ga687b3da8d0e3e0f55e8ea8d5e47eaf2a"></a>

```c
int stats_init_and_reg (struct stats_hdr *hdr, uint8_t size, uint16_t cnt, const struct stats_name_map *map, uint16_t map_cnt, const char *name)
```

相关声明：[stats_init_and_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga687b3da8d0e3e0f55e8ea8d5e47eaf2a)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

初始化并注册统计组（Statistics Group）。

<a id="r_gaca8e338b464a6c317232d7029c80f206"></a>

```c
void stats_reset (struct stats_hdr *shdr)
```

相关声明：[stats_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaca8e338b464a6c317232d7029c80f206)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

将指定统计组（Statistics Group）清零。

## 24.4\_遍历与查找（Walking and Lookup）

<a id="r_gaa4f75157451e12d76e5cc0fbc65063da"></a>

```c
typedef int stats_walk_fn(struct stats_hdr *hdr, void *arg, const char *name, uint16_t off)
```

相关声明：[stats_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaa4f75157451e12d76e5cc0fbc65063da)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

遍历（Walk）时对每个统计条目应用的函数。

<a id="r_ga454c4c833e25fcb8808c4b85db4f0291"></a>

```c
typedef int stats_group_walk_fn(struct stats_hdr *hdr, void *arg)
```

相关声明：[stats_group_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga454c4c833e25fcb8808c4b85db4f0291)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

对每个已注册统计组应用的函数。

<a id="r_gae6aeebd4e8f57b0b82c6dcf69bddcc64"></a>

```c
int stats_walk (struct stats_hdr *hdr, stats_walk_fn *walk_cb, void *arg)
```

相关声明：[stats_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae6aeebd4e8f57b0b82c6dcf69bddcc64)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaa4f75157451e12d76e5cc0fbc65063da)。

对组中的每个统计条目应用函数。

<a id="r_ga3b431d3e69b3978bfd81268b70eda6e0"></a>

```c
int stats_group_walk (stats_group_walk_fn *walk_cb, void *arg)
```

相关声明：[stats_group_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga3b431d3e69b3978bfd81268b70eda6e0)、[stats_group_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga454c4c833e25fcb8808c4b85db4f0291)。

对每个已注册统计组应用函数。

<a id="r_ga11402b3eb75529d1ebf7b7b87c9e20f8"></a>

```c
struct stats_hdr * stats_group_get_next (const struct stats_hdr *cur)
```

相关声明：[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_group_get_next](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga11402b3eb75529d1ebf7b7b87c9e20f8)、[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)。

获取下一个已注册统计组（Statistics Group）。

<a id="r_ga8cb611a313ede400835eb56a4d209c7a"></a>

```c
struct stats_hdr * stats_group_find (const char *name)
```

相关声明：[stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)、[stats_group_find](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga8cb611a313ede400835eb56a4d209c7a)。

获取具有指定名称的统计组（Statistics Group）。


## 24.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P106_stats.h_源码浏览.md)
- [stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)
- [stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)
- [STATS_SECT_DECL](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga21af7c98ccb9abb9464b9ef9358be880)
- [STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)
- [STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)
- [STATS_SECT_ENTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gafe8558503af10039b08a11f89c722783)
- [STATS_SECT_ENTRY16](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga681ab1b4b39cb753e362eedbd78943a9)
- [STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)
- [STATS_SECT_ENTRY64](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga589764c7a1e7d60fe0285b839c6c36b4)
- [STATS_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga6b5129b5d9a2ade6ecfd011ad2c4377f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [STATS_SIZE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga68323f9fddd985e9042bdca5b7f830b5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [STATS_SIZE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gafc9977fb100d17785440abf9cb93e63d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [STATS_INCN](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gac5d5050e8684027a3efb5a8e7a830be6)
- [STATS_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga725e1bf6b2c486de9603954974d6315a)
- [STATS_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga147f7c33929d040495d7bd526f5fca85)
- [STATS_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga1cce9ba94338a7fb027c78b32e638da5)
- [CONFIG_STATS_NAMES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS_NAMES)
- [STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)
- [STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)
- [STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)
- [STATS_NAME_INIT_PARMS](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gad1a94bded5ab34ac48c0dfd4cbdc168f)
- [stats_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5e2c74f2c77a8cf1d2a43eb7190a9b93)
- [STATS_INIT_AND_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga7a3f6d5dc044e6948998b8bc19efa493)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stats_register](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga0a26d63646d1157509afcc370738b9d8)
- [stats_init_and_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga687b3da8d0e3e0f55e8ea8d5e47eaf2a)
- [stats_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaca8e338b464a6c317232d7029c80f206)
- [stats_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaa4f75157451e12d76e5cc0fbc65063da)
- [stats_group_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga454c4c833e25fcb8808c4b85db4f0291)
- [stats_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae6aeebd4e8f57b0b82c6dcf69bddcc64)
- [stats_group_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga3b431d3e69b3978bfd81268b70eda6e0)
- [stats_group_get_next](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga11402b3eb75529d1ebf7b7b87c9e20f8)
- [stats_group_find](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga8cb611a313ede400835eb56a4d209c7a)

<a id="header-details"></a>

---

[上一章](P023_zephyr__dt-bindings__clock__rtl87x2g-clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__toolchain.h_文件参考.md)
