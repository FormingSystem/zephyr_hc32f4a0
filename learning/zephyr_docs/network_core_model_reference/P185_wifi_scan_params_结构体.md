---
id: learning.zephyr-docs.network-core-model-reference.page-185
title: wifi_scan_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__scan__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第185章\_wifi\_scan\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__scan__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi扫描参数（Scan Parameters）的结构。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi‑Fi 扫描参数结构（Wi-Fi scan parameters structure）。用于指定控制 Wi‑Fi 扫描执行方式的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 185.1\_数据成员（Data Fields）

<a id="r_a645acc54603cd4692527c1a028933078"></a>

```c
enum wifi_scan_type scan_type
```

相关声明：[wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)、[scan_type](#a645acc54603cd4692527c1a028933078)。

扫描类型（Scan type），参见枚举 `wifi_scan_type`。

<a id="r_a6b571d960ed9d7419e31530e5fb6f97a"></a>

```c
uint8_t bands
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bands](#a6b571d960ed9d7419e31530e5fb6f97a)。

待扫描频段的位图（Bitmap of bands）。

<a id="r_a2453a75c23e04e3572559c0e7199c1b4"></a>

```c
uint16_t dwell_time_active
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dwell_time_active](#a2453a75c23e04e3572559c0e7199c1b4)。

在一个信道上的主动扫描驻留时间（Active scan dwell time），单位为毫秒。

<a id="r_a8e7a37ccda8de635e7b7066d7943e814"></a>

```c
uint16_t dwell_time_passive
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dwell_time_passive](#a8e7a37ccda8de635e7b7066d7943e814)。

在一个信道上的被动扫描驻留时间（Passive scan dwell time），单位为毫秒。

<a id="r_aac11ee8e0ec8a4fa24668f4820bd1a12"></a>

```c
const char * ssids [WIFI_MGMT_SCAN_SSID_FILT_MAX]
```

相关声明：[ssids](#aac11ee8e0ec8a4fa24668f4820bd1a12)。

待扫描的服务集标识符字符串数组（SSID string array）。

<a id="r_a12d5dea7d8fa8ad03ac2366720c46243"></a>

```c
uint16_t max_bss_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_bss_cnt](#a12d5dea7d8fa8ad03ac2366720c46243)。

指定最多返回的扫描结果数量（Maximum number of scan results）。

<a id="r_aa5ddbd6bc97b7598288d4b0d38521681"></a>

```c
struct wifi_band_channel band_chan [WIFI_MGMT_SCAN_CHAN_MAX_MANUAL]
```

相关声明：[wifi_band_channel](P161_wifi_band_channel_结构体.md)、[band_chan](#aa5ddbd6bc97b7598288d4b0d38521681)。

信道信息数组（Channel information array），按 Wi‑Fi 频段及该频段内的信道索引。

## 185.2\_详细说明（Detailed Documentation）

<a id="aa5ddbd6bc97b7598288d4b0d38521681"></a>

### `band_chan`

```c
struct wifi_band_channel wifi_scan_params::band_chan[WIFI_MGMT_SCAN_CHAN_MAX_MANUAL]
```

信道信息数组（Channel information array），按 Wi‑Fi 频段及该频段内的信道索引。

例如，扫描 2.4 GHz 频段的信道 6 和 11，以及 5 GHz 频段的信道 36：

原始示例（Example）：

```c
chan[0] = {WIFI_FREQ_BAND_2_4_GHZ, 6};
chan[1] = {WIFI_FREQ_BAND_2_4_GHZ, 11};
chan[2] = {WIFI_FREQ_BAND_5_GHZ, 36};
```

此列表指定扫描时要考虑的信道（Channels）。底层 Wi‑Fi 芯片可能出于多种原因而静默略过某些信道，例如信道不符合监管限制（Regulatory restrictions）。API 调用者应确保指定的信道符合监管规则。

<a id="a6b571d960ed9d7419e31530e5fb6f97a"></a>

### `bands`

```c
uint8_t wifi_scan_params::bands
```

待扫描频段的位图（Bitmap of bands）。

各频段的位位置（Bit position）参见 `wifi_frequency_bands`。

<a id="a2453a75c23e04e3572559c0e7199c1b4"></a>

### `dwell_time_active`

```c
uint16_t wifi_scan_params::dwell_time_active
```

在一个信道上的主动扫描驻留时间（Active scan dwell time），单位为毫秒。

<a id="a8e7a37ccda8de635e7b7066d7943e814"></a>

### `dwell_time_passive`

```c
uint16_t wifi_scan_params::dwell_time_passive
```

在一个信道上的被动扫描驻留时间（Passive scan dwell time），单位为毫秒。

<a id="a12d5dea7d8fa8ad03ac2366720c46243"></a>

### `max_bss_cnt`

```c
uint16_t wifi_scan_params::max_bss_cnt
```

指定最多返回的扫描结果数量（Maximum number of scan results）。

这些结果是在所有已扫描信道中，接收信号强度指示（RSSI）值最好的基本服务集标识符（BSSIDs）。此参数只应用于限制返回的扫描结果数量，不能依靠它限制扫描时间；因为底层 Wi‑Fi 芯片可能需要扫描所有信道，才能找出信号强度最好的 `max_bss_cnt` 个接入点（APs）。值为 `0` 表示不限制返回的扫描结果数量。

<a id="a645acc54603cd4692527c1a028933078"></a>

### `scan_type`

```c
enum wifi_scan_type wifi_scan_params::scan_type
```

扫描类型（Scan type），参见枚举 `wifi_scan_type`。

`scan_type` 只是向底层 Wi‑Fi 芯片提示首选扫描模式（Preferred mode of scan）。实际扫描模式可能取决于芯片实现支持情况、监管域限制（Regulatory domain restrictions）等因素。

<a id="aac11ee8e0ec8a4fa24668f4820bd1a12"></a>

### `ssids`

```c
const char* wifi_scan_params::ssids[WIFI_MGMT_SCAN_SSID_FILT_MAX]
```

待扫描的服务集标识符字符串数组（SSID string array）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 185.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_band_channel](P161_wifi_band_channel_结构体.md)
- [WIFI_FREQ_BAND_2_4_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)
- [WIFI_FREQ_BAND_5_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895"></a>

---

[上一章](P184_wifi_reg_domain_结构体.md) · [返回大纲](大纲.md) · [下一章](P186_wifi_scan_result_结构体.md)
