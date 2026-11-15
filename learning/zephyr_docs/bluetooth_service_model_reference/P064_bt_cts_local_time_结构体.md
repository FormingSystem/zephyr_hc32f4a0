---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-64
title: bt_cts_local_time_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__local__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_bt\_cts\_local\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__local__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CTS 本地时间信息（Local Time Information）。

```c
#include <zephyr/bluetooth/services/cts.h>
```

<a id="details"></a>

CTS 本地时间信息（Local Time Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_abea48dd1a2e6426e19508ec124009c05"></a>

```c
int8_t timezone_offset
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[timezone_offset](#abea48dd1a2e6426e19508ec124009c05)。

相对于协调世界时（UTC）的偏移量，以 15 分钟为增量。

<a id="r_ac567357a4f8e2eebd1a03c2c182281c5"></a>

```c
enum bt_cts_dst_offset dst_offset
```

相关声明：[bt_cts_dst_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#gaea1ec94140fa450b8493540c1ec2511a)、[dst_offset](#ac567357a4f8e2eebd1a03c2c182281c5)。

夏令时偏移量（Daylight saving time offset），以 15 分钟为增量。

## 64.2\_详细说明（Detailed Documentation）

<a id="ac567357a4f8e2eebd1a03c2c182281c5"></a>

### `dst_offset`

```c
enum bt_cts_dst_offset bt_cts_local_time::dst_offset
```

夏令时偏移量（Daylight saving time offset），以 15 分钟为增量。

<a id="abea48dd1a2e6426e19508ec124009c05"></a>

### `timezone_offset`

```c
int8_t bt_cts_local_time::timezone_offset
```

相对于协调世界时（UTC）的偏移量，以 15 分钟为增量。

有效范围为 -48（`BT_CTS_TIMEZONE_MIN`）至 +56（`BT_CTS_TIMEZONE_MAX`）。值 -128（`BT_CTS_TIMEZONE_DEFAULT_VALUE`）表示时区偏移（Timezone offset）未知。其余值保留供将来使用。此特征定义的偏移量为常量，不随夏令时（Daylight savings）是否生效而改变。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/cts.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/cts.h](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_cts_dst_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#gaea1ec94140fa450b8493540c1ec2511a)
- [BT_CTS_TIMEZONE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga07b7421ed77c307503e154c5823ab32d)
- [BT_CTS_TIMEZONE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga204f8d7595bd169f4e547e66b8ca36b4)
- [BT_CTS_TIMEZONE_DEFAULT_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga38e3b4fec488ba4bcfcff097c752c32f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_bt_cts_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_bt_cts_time_format_结构体.md)
