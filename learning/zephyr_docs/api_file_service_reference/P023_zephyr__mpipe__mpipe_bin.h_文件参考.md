---
id: learning.zephyr-docs.api-file-service-reference.page-23
title: zephyr__mpipe__mpipe_bin.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_mpipe\_\_mpipe\_bin.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

容器（Bin）：包含其他元素的元素。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/zbus/zbus.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_message.h>
```

查看此文件的源码。

容器（Bin）：包含其他元素的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fbin"></a>

```c
struct mpipe_bin
```

相关声明：[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)。

容器（Bin）结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.2\_函数（Functions）

<a id="r_gab9a27c7642bd57189aa1f62da3c080e3"></a>

```c
int mpipe_bin_init (struct mpipe_bin *bin, uint8_t id)
```

相关声明：[mpipe_bin_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#gab9a27c7642bd57189aa1f62da3c080e3)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化元素容器（Bin）。

<a id="r_ga57d13bc1cb4c8f3095e3acbe08f7b6d4"></a>

```c
int mpipe_bin_set_bus_validator (struct mpipe_bin *bin, zbus_validator bus_validator, void *user_data)
```

相关声明：[mpipe_bin_set_bus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga57d13bc1cb4c8f3095e3acbe08f7b6d4)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[zbus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga44ca2e52a4f1bcf298888a7ebf9b5cf7)。

在元素容器（Bin）的总线（Bus）上安装验证器（Validator）和用户数据（User Data）。

<a id="r_ga0029c3da6a9bfca02c22673e4622a957"></a>

```c
int mpipe_bin_add (struct mpipe_bin *bin, struct mpipe_element *element,...)
```

相关声明：[mpipe_bin_add](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga0029c3da6a9bfca02c22673e4622a957)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

向元素容器（Bin）添加元素（Elements）。

<a id="r_ga564685f39d56de259d9df1257a57b1b7"></a>

```c
int mpipe_bin_change_state_func (struct mpipe_element *element, enum mpipe_state_change transition)
```

相关声明：[mpipe_bin_change_state_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga564685f39d56de259d9df1257a57b1b7)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

元素容器（Bin）的状态切换函数（State Change Function）。


## 23.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/zbus/zbus.h](../intercore_reference/P212_zbus核心完整头文件.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_message.h](../api_source_reference/P552_mpipe_message.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P058_mpipe_bin.h_源码浏览.md)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [mpipe_bin_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#gab9a27c7642bd57189aa1f62da3c080e3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_bin_set_bus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga57d13bc1cb4c8f3095e3acbe08f7b6d4)
- [zbus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga44ca2e52a4f1bcf298888a7ebf9b5cf7)
- [mpipe_bin_add](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga0029c3da6a9bfca02c22673e4622a957)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_bin_change_state_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga564685f39d56de259d9df1257a57b1b7)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)

<a id="header-details"></a>

---

[上一章](P022_zephyr__mgmt__mcumgr__mgmt__mgmt_defines.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__mpipe__utils__mpipe_dump.h_文件参考.md)
