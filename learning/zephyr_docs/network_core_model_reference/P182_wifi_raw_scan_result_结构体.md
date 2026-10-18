---
id: learning.zephyr-docs.network-core-model-reference.page-182
title: wifi_raw_scan_result_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__raw__scan__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第182章\_wifi\_raw\_scan\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__raw__scan__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi原始扫描结果（Raw Scan Result）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi原始扫描结果（Raw Scan Result）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 182.1\_数据成员（Data Fields）

<a id="r_a3f08580c6448a5fa28dd8a594fa7dad6"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a3f08580c6448a5fa28dd8a594fa7dad6)。

接收信号强度指示（RSSI）。

<a id="r_a876966f469714eb481b42ccc8a63945c"></a>

```c
int frame_length
```

相关声明：[frame_length](#a876966f469714eb481b42ccc8a63945c)。

帧长度（Frame length）。

<a id="r_aa2c7781882c6775616cbc8016b0842f6"></a>

```c
unsigned short frequency
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[frequency](#aa2c7781882c6775616cbc8016b0842f6)。

频率（Frequency）。

<a id="r_a5710e89199c147ce898602795f00aba3"></a>

```c
uint8_t data [CONFIG_WIFI_MGMT_RAW_SCAN_RESULT_LENGTH]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a5710e89199c147ce898602795f00aba3)。

原始扫描数据（Raw scan data）。

## 182.2\_详细说明（Detailed Documentation）

<a id="a5710e89199c147ce898602795f00aba3"></a>

### `data`

```c
uint8_t wifi_raw_scan_result::data[CONFIG_WIFI_MGMT_RAW_SCAN_RESULT_LENGTH]
```

原始扫描数据（Raw scan data）。

<a id="a876966f469714eb481b42ccc8a63945c"></a>

### `frame_length`

```c
int wifi_raw_scan_result::frame_length
```

帧长度（Frame length）。

<a id="aa2c7781882c6775616cbc8016b0842f6"></a>

### `frequency`

```c
unsigned short wifi_raw_scan_result::frequency
```

频率（Frequency）。

<a id="a3f08580c6448a5fa28dd8a594fa7dad6"></a>

### `rssi`

```c
int8_t wifi_raw_scan_result::rssi
```

接收信号强度指示（RSSI）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 182.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P181_wifi_ps_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P183_wifi_reg_chan_info_结构体.md)
