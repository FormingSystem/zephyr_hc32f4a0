---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-56
title: osdp_cmd_buzzer_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__buzzer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_osdp\_cmd\_buzzer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__buzzer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由控制面板（CP）发送，用于控制外设（PD）中蜂鸣器的行为。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

由控制面板（CP）发送，用于控制外设（PD）中蜂鸣器的行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_a0e97e1e33eac4f25e5a05586f8135ab3"></a>

```c
uint8_t reader
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reader](#a0e97e1e33eac4f25e5a05586f8135ab3)。

读卡器编号（Reader number）。

<a id="r_a16d0f385264e247d942367a6a13a77af"></a>

```c
uint8_t control_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[control_code](#a16d0f385264e247d942367a6a13a77af)。

控制码（Control code）。

<a id="r_a9082cf0dd2e3e9d31d95051f2952d611"></a>

```c
uint8_t on_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[on_count](#a9082cf0dd2e3e9d31d95051f2952d611)。

声音开启（ON）的持续时间，以 100 ms 为单位。

<a id="r_ac83cdb57418fc28f11c686e79e811492"></a>

```c
uint8_t off_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_count](#ac83cdb57418fc28f11c686e79e811492)。

声音关闭（OFF）的持续时间，以 100 ms 为单位。

<a id="r_a0ea92ffb8ed7527e0373c0530edfb61d"></a>

```c
uint8_t rep_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rep_count](#a0ea92ffb8ed7527e0373c0530edfb61d)。

开启/关闭周期的重复次数；`0` 表示无限重复。

## 56.2\_详细说明（Detailed Documentation）

<a id="a16d0f385264e247d942367a6a13a77af"></a>

### `control_code`

```c
uint8_t osdp_cmd_buzzer::control_code
```

控制码（Control code）。

- `0`：无音调（No tone）。
- `1`：关闭（Off）。
- `2`：默认音调（Default tone）。
- `3` 及以上：待定义（TBD）。

<a id="ac83cdb57418fc28f11c686e79e811492"></a>

### `off_count`

```c
uint8_t osdp_cmd_buzzer::off_count
```

声音关闭（OFF）的持续时间，以 100 ms 为单位。

<a id="a9082cf0dd2e3e9d31d95051f2952d611"></a>

### `on_count`

```c
uint8_t osdp_cmd_buzzer::on_count
```

声音开启（ON）的持续时间，以 100 ms 为单位。

<a id="a0e97e1e33eac4f25e5a05586f8135ab3"></a>

### `reader`

```c
uint8_t osdp_cmd_buzzer::reader
```

读卡器编号（Reader number）。

`0` 表示第一个读卡器，`1` 表示第二个读卡器，依此类推。

<a id="a0ea92ffb8ed7527e0373c0530edfb61d"></a>

### `rep_count`

```c
uint8_t osdp_cmd_buzzer::rep_count
```

开启/关闭周期的重复次数；`0` 表示无限重复。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_osdp_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_osdp_cmd_comset_结构体.md)
