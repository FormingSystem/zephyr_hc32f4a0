---
id: learning.zephyr-docs.api-file-management-reference.page-26
title: zephyr__bluetooth__audio__lc3.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_bluetooth\_\_audio\_\_lc3.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙LC3编解码器（Codec）的处理。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
#include <zephyr/bluetooth/byteorder.h>
#include <zephyr/bluetooth/hci_types.h>
```

查看此文件的源码。

蓝牙LC3编解码器（Codec）的处理。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.1\_宏定义（Macros）

<a id="r_ga8d679b241585ff5ebff0d97bb22dfda9"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3_DATA(_freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga8d679b241585ff5ebff0d97bb22dfda9)。

用于声明低复杂度通信编解码器（LC3）能力（capability）的辅助宏。

<a id="r_ga9b5d5e300a7b41060329dbdd2cd073f6"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3_META(_prefer_context)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3_META](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga9b5d5e300a7b41060329dbdd2cd073f6)。

用于声明 LC3 编解码器元数据（metadata）的辅助宏。

<a id="r_gac474746e7314ebf7ed77b8937191cdc1"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3(_freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu, _prefer_context)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#gac474746e7314ebf7ed77b8937191cdc1)。

用于声明 LC3 编解码器（codec）的辅助宏。

<a id="r_ga497ff0aa1d7dcfeea6ec549e5fb155d6"></a>

```c
#define BT_AUDIO_CODEC_CFG_LC3_DATA(_freq, _duration, _loc, _len, _frames_per_sdu)
```

相关声明：[BT_AUDIO_CODEC_CFG_LC3_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga497ff0aa1d7dcfeea6ec549e5fb155d6)。

用于声明 LC3 编解码器数据配置（data configuration）的辅助宏。

<a id="r_ga2c00f8bd526305d878624c6f1b8030f8"></a>

```c
#define BT_AUDIO_CODEC_CFG_LC3_META(_stream_context)
```

相关声明：[BT_AUDIO_CODEC_CFG_LC3_META](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga2c00f8bd526305d878624c6f1b8030f8)。

用于声明 LC3 编解码器元数据配置（metadata configuration）的辅助宏。

<a id="r_ga2c5f1f9e6d80a2eef93f7b08a19ea245"></a>

```c
#define BT_AUDIO_CODEC_LC3_CONFIG(_freq, _duration, _loc, _len, _frames_per_sdu, _stream_context)
```

相关声明：[BT_AUDIO_CODEC_LC3_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga2c5f1f9e6d80a2eef93f7b08a19ea245)。

用于声明 LC3 编解码器配置的辅助宏。


## 26.2\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P005_蓝牙字节序头文件源码.md)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P437_lc3.h_源码浏览.md)
- [BT_AUDIO_CODEC_CAP_LC3_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga8d679b241585ff5ebff0d97bb22dfda9)
- [BT_AUDIO_CODEC_CAP_LC3_META](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga9b5d5e300a7b41060329dbdd2cd073f6)
- [BT_AUDIO_CODEC_CAP_LC3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#gac474746e7314ebf7ed77b8937191cdc1)
- [BT_AUDIO_CODEC_CFG_LC3_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga497ff0aa1d7dcfeea6ec549e5fb155d6)
- [BT_AUDIO_CODEC_CFG_LC3_META](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga2c00f8bd526305d878624c6f1b8030f8)
- [BT_AUDIO_CODEC_LC3_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html#ga2c5f1f9e6d80a2eef93f7b08a19ea245)

<a id="header-details"></a>

---

[上一章](P025_zephyr__net__ssh__keygen.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__dt-bindings__pinctrl__lpc11u6x-pinctrl.h_文件参考.md)
