---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-3
title: crsf_link_stats_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__link__stats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_crsf\_link\_stats\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__link__stats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

链路统计信息（Link Statistics）载荷，类型为0x14。

```c
#include <zephyr/input/input_crsf.h>
```

<a id="details"></a>

链路统计信息（Link Statistics）载荷，类型为0x14。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a03786e5e70c07ea29e45d781374c783e"></a>

```c
uint8_t uplink_rssi_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uplink_rssi_1](#a03786e5e70c07ea29e45d781374c783e)。

上行链路天线 1 的接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="r_a9afe00cdbc866e8ad01583fb3a8c01f5"></a>

```c
uint8_t uplink_rssi_2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uplink_rssi_2](#a9afe00cdbc866e8ad01583fb3a8c01f5)。

上行链路天线 2 的接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="r_ab00ec240186f2e3967f27a878f3189cc"></a>

```c
uint8_t uplink_link_quality
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uplink_link_quality](#ab00ec240186f2e3967f27a878f3189cc)。

上行链路质量（link quality），范围为 0% 至 100%。

<a id="r_a985cc7785aea619a5c6fc0a01f4a51e9"></a>

```c
int8_t uplink_snr
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uplink_snr](#a985cc7785aea619a5c6fc0a01f4a51e9)。

上行链路信噪比（signal-to-noise ratio），单位为 dB。

<a id="r_ac32c03eff5b5722dae1fab83bba82cae"></a>

```c
uint8_t active_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[active_antenna](#ac32c03eff5b5722dae1fab83bba82cae)。

当前使用的天线索引。

<a id="r_a17f459d371712bdc98ff1cb4097078ac"></a>

```c
uint8_t rf_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rf_mode](#a17f459d371712bdc98ff1cb4097078ac)。

射频模式（RF mode），例如下列频率。

<a id="r_a94001c4fa56a67453dffaa6b2332714a"></a>

```c
uint8_t tx_power
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_power](#a94001c4fa56a67453dffaa6b2332714a)。

发射功率级别，由协议定义的枚举值表示。

<a id="r_a511eab5e2715a7801737a872070dc464"></a>

```c
uint8_t downlink_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[downlink_rssi](#a511eab5e2715a7801737a872070dc464)。

下行链路接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="r_a7b64694ea1180b538de7b20c349053bf"></a>

```c
uint8_t downlink_link_quality
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[downlink_link_quality](#a7b64694ea1180b538de7b20c349053bf)。

下行链路质量，范围为 0% 至 100%。

<a id="r_af30d3bf98388e9b59692e190b32ec34f"></a>

```c
int8_t downlink_snr
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[downlink_snr](#af30d3bf98388e9b59692e190b32ec34f)。

下行链路信噪比，单位为 dB。

## 3.2\_详细说明（Detailed Documentation）

<a id="ac32c03eff5b5722dae1fab83bba82cae"></a>

### `active_antenna`

```c
uint8_t crsf_link_stats::active_antenna
```

当前使用的天线索引。

<a id="a7b64694ea1180b538de7b20c349053bf"></a>

### `downlink_link_quality`

```c
uint8_t crsf_link_stats::downlink_link_quality
```

下行链路质量，范围为 0% 至 100%。

<a id="a511eab5e2715a7801737a872070dc464"></a>

### `downlink_rssi`

```c
uint8_t crsf_link_stats::downlink_rssi
```

下行链路接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="af30d3bf98388e9b59692e190b32ec34f"></a>

### `downlink_snr`

```c
int8_t crsf_link_stats::downlink_snr
```

下行链路信噪比，单位为 dB。

<a id="a17f459d371712bdc98ff1cb4097078ac"></a>

### `rf_mode`

```c
uint8_t crsf_link_stats::rf_mode
```

射频模式（RF mode），例如下列频率。

4 Hz、50 Hz、150 Hz。

<a id="a94001c4fa56a67453dffaa6b2332714a"></a>

### `tx_power`

```c
uint8_t crsf_link_stats::tx_power
```

发射功率级别，由协议定义的枚举值表示。

<a id="ab00ec240186f2e3967f27a878f3189cc"></a>

### `uplink_link_quality`

```c
uint8_t crsf_link_stats::uplink_link_quality
```

上行链路质量（link quality），范围为 0% 至 100%。

<a id="a03786e5e70c07ea29e45d781374c783e"></a>

### `uplink_rssi_1`

```c
uint8_t crsf_link_stats::uplink_rssi_1
```

上行链路天线 1 的接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="a9afe00cdbc866e8ad01583fb3a8c01f5"></a>

### `uplink_rssi_2`

```c
uint8_t crsf_link_stats::uplink_rssi_2
```

上行链路天线 2 的接收信号强度指示（RSSI），编码值为 dBm 数值乘以 -1。

<a id="a985cc7785aea619a5c6fc0a01f4a51e9"></a>

### `uplink_snr`

```c
int8_t crsf_link_stats::uplink_snr
```

上行链路信噪比（signal-to-noise ratio），单位为 dB。

本数据类型文档由以下文件生成：

- `zephyr/input/input_crsf.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/input/input_crsf.h](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_ccs811_result_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_crsf_payload_attitude_结构体.md)
