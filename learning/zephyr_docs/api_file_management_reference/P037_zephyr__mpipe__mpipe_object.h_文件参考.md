---
id: learning.zephyr-docs.api-file-management-reference.page-37
title: zephyr__mpipe__mpipe_object.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_mpipe\_\_mpipe\_object.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象（Object）：每个mpipe类型都嵌入的基类。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

对象（Object）：每个mpipe类型都嵌入的基类。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 37.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fobject"></a>

```c
struct mpipe_object
```

相关声明：[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

基础对象结构（Base Object Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.2\_宏定义（Macros）

<a id="r_ga40d41093fdd92de417133e57476d6e24"></a>

```c
#define MPIPE_OBJECT_FLAG_BASE BIT(0)
```

相关声明：[MPIPE_OBJECT_FLAG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga40d41093fdd92de417133e57476d6e24)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象的基础标志（base flag）。

<a id="r_ga1b65711b9e9f2e53f4a85d9db490cc91"></a>

```c
#define MPIPE_OBJECT_FLAG_BIN BIT(1)
```

相关声明：[MPIPE_OBJECT_FLAG_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga1b65711b9e9f2e53f4a85d9db490cc91)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该对象为容器（Bins），拥有自己的子对象。

<a id="r_gaecb3a88ad49c27402eebe277c73bc825"></a>

```c
#define MPIPE_PROP_LIST_END UINT32_MAX
```

相关声明：[MPIPE_PROP_LIST_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gaecb3a88ad49c27402eebe277c73bc825)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

标记属性列表结束的哨兵值（sentinel value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.3\_函数（Functions）

<a id="r_gaa248dc28bf93b5426a9614e8611f60fe"></a>

```c
void mpipe_object_init (struct mpipe_object *obj)
```

相关声明：[mpipe_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gaa248dc28bf93b5426a9614e8611f60fe)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

将 `mpipe_object` 的所有字段初始化为零。

<a id="r_gae63735281ccac01779ba1e037e438641"></a>

```c
int mpipe_object_set_properties (struct mpipe_object *obj,...)
```

相关声明：[mpipe_object_set_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gae63735281ccac01779ba1e037e438641)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

设置 `mpipe_object` 的多个属性（properties）。

<a id="r_ga7ae53fbbd40a3886b0baf767d1e5c4c5"></a>

```c
int mpipe_object_get_properties (struct mpipe_object *obj,...)
```

相关声明：[mpipe_object_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga7ae53fbbd40a3886b0baf767d1e5c4c5)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

获取 `mpipe_object` 的多个属性值。


## 37.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P553_mpipe_object.h_源码浏览.md)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [MPIPE_OBJECT_FLAG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga40d41093fdd92de417133e57476d6e24)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MPIPE_OBJECT_FLAG_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga1b65711b9e9f2e53f4a85d9db490cc91)
- [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)
- [MPIPE_PROP_LIST_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gaecb3a88ad49c27402eebe277c73bc825)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [mpipe_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gaa248dc28bf93b5426a9614e8611f60fe)
- [mpipe_object_set_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gae63735281ccac01779ba1e037e438641)
- [mpipe_object_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga7ae53fbbd40a3886b0baf767d1e5c4c5)

<a id="header-details"></a>

---

[上一章](P036_zephyr__modem__ubx__keys.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__net__net_time.h_文件参考.md)
