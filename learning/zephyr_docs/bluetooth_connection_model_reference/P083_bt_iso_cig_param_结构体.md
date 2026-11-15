---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-83
title: bt_iso_cig_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__cig__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_bt\_iso\_cig\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__cig__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接等时组（Connected Isochronous Group，CIG）参数。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

连接等时组（Connected Isochronous Group，CIG）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 83.1\_数据成员（Data Fields）

<a id="r_a841dee850f3161bd8e904376792c8ad7"></a>

```c
struct bt_iso_chan ** cis_channels
```

相关声明：[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[cis_channels](#a841dee850f3161bd8e904376792c8ad7)。

连接等时流通道指针数组（CIS channel pointers）。

<a id="r_a69c12b704b9897d88b71bc96bd2d3024"></a>

```c
uint8_t num_cis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_cis](#a69c12b704b9897d88b71bc96bd2d3024)。

`cis_channels` 中的通道数量（Number of channels）。

<a id="r_ad7349213bab902a68c726da51fac2306"></a>

```c
uint32_t c_to_p_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[c_to_p_interval](#ad7349213bab902a68c726da51fac2306)。

从中心设备（Central）发往外设（Peripheral）的服务数据单元（SDUs）的通道间隔，单位为微秒。

<a id="r_a36d2eaa4fd3e08988d4c49ca0902a882"></a>

```c
uint32_t p_to_c_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[p_to_c_interval](#a36d2eaa4fd3e08988d4c49ca0902a882)。

从外设（Peripheral）发往中心设备（Central）的服务数据单元（SDUs）的通道间隔，单位为微秒。

<a id="r_aeffe10e87d81285196e931dcad2882ba"></a>

```c
uint16_t c_to_p_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_to_p_latency](#aeffe10e87d81285196e931dcad2882ba)。

从中心设备（Central）发往外设（Peripheral）的服务数据单元（SDUs）的通道延迟，单位为毫秒。

<a id="r_ad1725e09a397e83d1cc88ebd3a60ed93"></a>

```c
uint16_t p_to_c_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_to_c_latency](#ad1725e09a397e83d1cc88ebd3a60ed93)。

从外设（Peripheral）发往中心设备（Central）的服务数据单元（SDUs）的通道延迟，单位为毫秒。

<a id="r_a83fdc5374f341a421e1394b08297cdff"></a>

```c
uint8_t sca
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sca](#a83fdc5374f341a421e1394b08297cdff)。

通道外设的睡眠时钟精度（Sleep clock accuracy），仅用于连接等时流（CIS）。

<a id="r_a3908eadf3080731cb891e803162d321c"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a3908eadf3080731cb891e803162d321c)。

通道打包模式（Channel packing mode）。

<a id="r_a4a09f9f6e7a8db17c3037c9f1761b18a"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#a4a09f9f6e7a8db17c3037c9f1761b18a)。

通道成帧模式（Channel framing mode）。

<a id="r_aadc3762f3fec3127014378fe58c5b684"></a>

```c
uint8_t c_to_p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_to_p_ft](#aadc3762f3fec3127014378fe58c5b684)。

中心设备到外围设备的清除超时（Flush Timeout）。

<a id="r_ab222cdb0af475180dd715b4f5658dc65"></a>

```c
uint8_t p_to_c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_to_c_ft](#ab222cdb0af475180dd715b4f5658dc65)。

外围设备到中心设备的清除超时。

<a id="r_a85641a8f01d63b4221c013815c055526"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a85641a8f01d63b4221c013815c055526)。

等时间隔（ISO Interval）。

## 83.2\_详细说明（Detailed Documentation）

<a id="aadc3762f3fec3127014378fe58c5b684"></a>

### `c_to_p_ft`

```c
uint8_t bt_iso_cig_param::c_to_p_ft
```

中心设备到外围设备的清除超时（Flush Timeout）。

从中心设备发送到外围设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="ad7349213bab902a68c726da51fac2306"></a>

### `c_to_p_interval`

```c
uint32_t bt_iso_cig_param::c_to_p_interval
```

从中心设备（Central）发往外设（Peripheral）的服务数据单元（SDUs）的通道间隔，单位为微秒。

取值范围为 `BT_ISO_SDU_INTERVAL_MIN` 到 `BT_ISO_SDU_INTERVAL_MAX`。

<a id="aeffe10e87d81285196e931dcad2882ba"></a>

### `c_to_p_latency`

```c
uint16_t bt_iso_cig_param::c_to_p_latency
```

从中心设备（Central）发往外设（Peripheral）的服务数据单元（SDUs）的通道延迟，单位为毫秒。

取值范围为 `BT_ISO_LATENCY_MIN` 到 `BT_ISO_LATENCY_MAX`。

设置任何高级等时参数（Advanced ISO parameters）后，此值均被忽略。

<a id="a841dee850f3161bd8e904376792c8ad7"></a>

### `cis_channels`

```c
struct bt_iso_chan** bt_iso_cig_param::cis_channels
```

连接等时流通道指针数组（CIS channel pointers）。

<a id="a4a09f9f6e7a8db17c3037c9f1761b18a"></a>

### `framing`

```c
uint8_t bt_iso_cig_param::framing
```

通道成帧模式（Channel framing mode）。

无帧模式（Unframed）使用 `BT_ISO_FRAMING_UNFRAMED`，成帧模式（Framed）使用 `BT_ISO_FRAMING_FRAMED`。

<a id="a85641a8f01d63b4221c013815c055526"></a>

### `iso_interval`

```c
uint16_t bt_iso_cig_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 CIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="a69c12b704b9897d88b71bc96bd2d3024"></a>

### `num_cis`

```c
uint8_t bt_iso_cig_param::num_cis
```

`cis_channels` 中的通道数量（Number of channels）。

单组最大通道数量（Maximum channels per group）为 `BT_ISO_MAX_GROUP_ISO_COUNT`。

<a id="ab222cdb0af475180dd715b4f5658dc65"></a>

### `p_to_c_ft`

```c
uint8_t bt_iso_cig_param::p_to_c_ft
```

外围设备到中心设备的清除超时。

从外围设备发送到中心设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="a36d2eaa4fd3e08988d4c49ca0902a882"></a>

### `p_to_c_interval`

```c
uint32_t bt_iso_cig_param::p_to_c_interval
```

从外设（Peripheral）发往中心设备（Central）的服务数据单元（SDUs）的通道间隔，单位为微秒。

取值范围为 `BT_ISO_SDU_INTERVAL_MIN` 到 `BT_ISO_SDU_INTERVAL_MAX`。

<a id="ad1725e09a397e83d1cc88ebd3a60ed93"></a>

### `p_to_c_latency`

```c
uint16_t bt_iso_cig_param::p_to_c_latency
```

从外设（Peripheral）发往中心设备（Central）的服务数据单元（SDUs）的通道延迟，单位为毫秒。

取值范围为 `BT_ISO_LATENCY_MIN` 到 `BT_ISO_LATENCY_MAX`。

设置任何高级等时参数（Advanced ISO parameters）后，此值均被忽略。

<a id="a3908eadf3080731cb891e803162d321c"></a>

### `packing`

```c
uint8_t bt_iso_cig_param::packing
```

通道打包模式（Channel packing mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

<a id="a83fdc5374f341a421e1394b08297cdff"></a>

### `sca`

```c
uint8_t bt_iso_cig_param::sca
```

通道外设的睡眠时钟精度（Sleep clock accuracy），仅用于连接等时流（CIS）。

应为所有外设中最差情况下的睡眠时钟精度（Sleep clock accuracy）。可能值参见 `bt_gap_sca`；若不知道外设的该值，应设为 `BT_GAP_SCA_UNKNOWN`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 83.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_ISO_FT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2d3bde6b34f6b15474926ed97ad11d98)
- [BT_ISO_FT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga011c9d5840658fd0ef244f47893ec70e)
- [BT_ISO_SDU_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8122de88b6e5423dca653b1f0a484316)
- [BT_ISO_SDU_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga077eb6d219bba947d363e2cce8e0080c)
- [BT_ISO_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga77ae350543eb05617c590c0ad9cb0048)
- [BT_ISO_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad5e89d05d8706509d8d9d8dac40e3347)
- [BT_ISO_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga696a81180ae25aa686a53b73e352c9d2)
- [BT_ISO_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8f9aba389529ad2a3667ca378e99de2b)
- [BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)
- [BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)
- [BT_ISO_MAX_GROUP_ISO_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae9dc30b300e2c309d646e3227e8cc00e)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)
- [bt_gap_sca](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga3cd6d431193b05414020ca5686f4c0e4)
- [BT_GAP_SCA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P082_bt_iso_cig_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_bt_iso_connect_param_结构体.md)
