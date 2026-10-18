---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-27
title: bt_bap_qos_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__qos__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_bap\_qos\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__qos__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

服务质量（QoS）配置结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

服务质量（QoS）配置结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_addf190fac00b2fb99c0d1abf13eb20b3"></a>

```c
uint32_t pd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pd](#addf190fac00b2fb99c0d1abf13eb20b3)。

呈现延迟（Presentation Delay），单位为微秒。

```c
struct {
```

<a id="r_aacc5e6617c98bd8fbc14baa989c24a8e"></a>

```c
enum bt_bap_qos_cfg_framing framing
```

相关声明：[bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)、[framing](#a60057a7812cdc5b26f839e68dc4603c4)。

QoS 成帧方式（Framing）。

<a id="r_a232c87f6da80b16c647b13b03b51da0d"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ac50ea51e1645546d8f8faa58c64672ce)。

物理层（PHY）。

<a id="r_a320c8f48a455dbcfce9f54551306c87f"></a>

```c
uint8_t rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtn](#aaaa4a88499cfd1f90e409fa98891bf2c)。

重传次数（Retransmission Number）。

<a id="r_a6c63523a92b3c9e26eb1b56f99d15008"></a>

```c
uint16_t sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sdu](#a294709496f7779ee4cb7aa542da8832b)。

服务数据单元（SDU）的最大大小。

<a id="r_a2022b655de7ccb2111fe3b032583e234"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a912ee316aa2ddb00ebab7bb78af0f34a)。

最大传输延迟（Maximum Transport Latency）。

<a id="r_a36c24985751825218dc2979eea5c3284"></a>

```c
uint32_t interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval](#abf8a1b76cc0735b9aec1962d2ce574ec)。

SDU 间隔（SDU Interval）。

<a id="r_aa9cb64c3020c6d03e629e5292a42b6c9"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#acb84f2da73e865e38dcefa92007f01e1)。

协议数据单元（PDU）的最大大小。

<a id="r_aa00f4636c3499cfd3124597d1ce2ba34"></a>

```c
uint8_t burst_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[burst_number](#a597b81261511ec820caa66bd091ab896)。

突发数量（Burst Number）。

<a id="r_a3aeb30be66c4ef3eb871893ef70a0a07"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a97094ac8254ff3e97790943a5c71cdf3)。

子事件数量（Number of Subevents）。

<a id="r_a9a3980ad5dcdb2e8fd5646d09364c555"></a>

```c
};
```

连接等时组（Connected Isochronous Group，CIG）参数。

## 27.2\_详细说明（Detailed Documentation）

<a id="a9a3980ad5dcdb2e8fd5646d09364c555"></a>

### `[struct]`

```c
struct { ... } bt_bap_qos_cfg
```

连接等时组（Connected Isochronous Group，CIG）参数。

此结构体中的字段影响创建 CIG 时通过 HCI 发送给控制器的值。使用 `bt_bap_unicast_group_create()` 创建组后，再修改这些字段不会影响该组。

<a id="a597b81261511ec820caa66bd091ab896"></a>

### `burst_number`

```c
uint8_t bt_bap_qos_cfg::burst_number
```

突发数量（Burst Number）。

取值范围为 `BT_ISO_BN_MIN` 到 `BT_ISO_BN_MAX`。

<a id="a60057a7812cdc5b26f839e68dc4603c4"></a>

### `framing`

```c
enum bt_bap_qos_cfg_framing bt_bap_qos_cfg::framing
```

QoS 成帧方式（Framing）。

<a id="abf8a1b76cc0735b9aec1962d2ce574ec"></a>

### `interval`

```c
uint32_t bt_bap_qos_cfg::interval
```

SDU 间隔（SDU Interval）。

取值范围为 `BT_ISO_SDU_INTERVAL_MIN` 到 `BT_ISO_SDU_INTERVAL_MAX`。

<a id="a912ee316aa2ddb00ebab7bb78af0f34a"></a>

### `latency`

```c
uint16_t bt_bap_qos_cfg::latency
```

最大传输延迟（Maximum Transport Latency）。

`CONFIG_BT_BAP_BROADCAST_SINK` 角色不使用此项。

<a id="acb84f2da73e865e38dcefa92007f01e1"></a>

### `max_pdu`

```c
uint16_t bt_bap_qos_cfg::max_pdu
```

协议数据单元（PDU）的最大大小。

链路层之间传递的载荷的最大大小，单位为八位字节。

连接等时（Connected ISO）的取值范围为 `BT_ISO_CONNECTED_PDU_MIN` 到 `BT_ISO_PDU_MAX`。

广播等时（Broadcast ISO）的取值范围为 `BT_ISO_BROADCAST_PDU_MIN` 到 `BT_ISO_PDU_MAX`。

<a id="a97094ac8254ff3e97790943a5c71cdf3"></a>

### `num_subevents`

```c
uint8_t bt_bap_qos_cfg::num_subevents
```

子事件数量（Number of Subevents）。

每个 CIS 或 BIS 事件中的最大子事件数量。

取值范围为 `BT_ISO_NSE_MIN` 到 `BT_ISO_NSE_MAX`。

<a id="addf190fac00b2fb99c0d1abf13eb20b3"></a>

### `pd`

```c
uint32_t bt_bap_qos_cfg::pd
```

呈现延迟（Presentation Delay），单位为微秒。

在调用 `bt_bap_stream_qos()` 之前，可以修改此值。流完成 QoS 配置后，仅修改该字段不会改变实际值。不过，如果流处于适当状态，可以修改此字段并再次调用 `bt_bap_stream_qos()` 来更新实际值。

取值范围为 0 到 `BT_AUDIO_PD_MAX`。

<a id="ac50ea51e1645546d8f8faa58c64672ce"></a>

### `phy`

```c
uint8_t bt_bap_qos_cfg::phy
```

物理层（PHY）。

允许的值为 `BT_BAP_QOS_CFG_1M`、`BT_BAP_QOS_CFG_2M` 和 `BT_BAP_QOS_CFG_CODED`。

<a id="aaaa4a88499cfd1f90e409fa98891bf2c"></a>

### `rtn`

```c
uint8_t bt_bap_qos_cfg::rtn
```

重传次数（Retransmission Number）。

这是向控制器提出的建议，实际重传次数可能与此值不同。

<a id="a294709496f7779ee4cb7aa542da8832b"></a>

### `sdu`

```c
uint16_t bt_bap_qos_cfg::sdu
```

服务数据单元（SDU）的最大大小。

取值范围为 `BT_ISO_MIN_SDU` 到 `BT_ISO_MAX_SDU`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)
- [bt_bap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaafd53b5f45d998b44e94a1b58e93ba21)
- [BT_ISO_BN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2905cddfa456fc846f0c8025487b404d)
- [BT_ISO_BN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac05f4f51ea04962679f616bb167b724d)
- [BT_ISO_SDU_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8122de88b6e5423dca653b1f0a484316)
- [BT_ISO_SDU_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga077eb6d219bba947d363e2cce8e0080c)
- [CONFIG_BT_BAP_BROADCAST_SINK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SINK)
- [BT_ISO_CONNECTED_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4e29d5966f959114754d62a8763c8c1e)
- [BT_ISO_PDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga88fb5690cd1cab4e5e8d5c025cc1af00)
- [BT_ISO_BROADCAST_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaee766ff789f1bf01f75c88112ddd2afa)
- [BT_ISO_NSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3eba4c20b4203b0323b14178522e6159)
- [BT_ISO_NSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab7637d96bde7a41123b34f487eec3436)
- [bt_bap_stream_qos()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)
- [BT_AUDIO_PD_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaaa0414a4baef5a867fd1c6b1865d2dbc)
- [BT_BAP_QOS_CFG_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)
- [BT_BAP_QOS_CFG_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)
- [BT_BAP_QOS_CFG_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)
- [BT_ISO_MIN_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4cc5565eeda9a3661d49d485637d1db2)
- [BT_ISO_MAX_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa5d5588e7229db16219b0c44921bbcf7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_bap_lc3_preset_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_bap_qos_cfg_pref_结构体.md)
