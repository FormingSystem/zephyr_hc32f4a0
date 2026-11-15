---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-78
title: bt_iso_chan_io_qos_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__io__qos.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_bt\_iso\_chan\_io\_qos\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__io__qos.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）的输入输出服务质量（IO QoS）结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时信道（ISO Channel）的输入输出服务质量（IO QoS）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_ae52611dc326b6777620ff7aa43f566e9"></a>

```c
uint16_t sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sdu](#ae52611dc326b6777620ff7aa43f566e9)。

通道服务数据单元（Channel SDU）。

<a id="r_a2180a4f82e4cdf5288b7f67701a16ad6"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a2180a4f82e4cdf5288b7f67701a16ad6)。

通道物理层（Channel PHY），参见 `bt_gap_le_phy` 的取值。

<a id="r_a5106bfd09f6be52604e7c7f0e3390684"></a>

```c
uint8_t rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtn](#a5106bfd09f6be52604e7c7f0e3390684)。

通道重传次数（Channel Retransmission Number）。

<a id="r_ae9e7678a63030353eea65152d89464cd"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#ae9e7678a63030353eea65152d89464cd)。

协议数据单元（PDU）的最大大小。

<a id="r_ac64a3ce7282ac8bc5b5420a46417b22c"></a>

```c
uint8_t burst_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[burst_number](#ac64a3ce7282ac8bc5b5420a46417b22c)。

突发数量（Burst Number）。

## 78.2\_详细说明（Detailed Documentation）

<a id="ac64a3ce7282ac8bc5b5420a46417b22c"></a>

### `burst_number`

```c
uint8_t bt_iso_chan_io_qos::burst_number
```

突发数量（Burst Number）。

取值范围为 `BT_ISO_BN_MIN` 到 `BT_ISO_BN_MAX`。

<a id="ae9e7678a63030353eea65152d89464cd"></a>

### `max_pdu`

```c
uint16_t bt_iso_chan_io_qos::max_pdu
```

协议数据单元（PDU）的最大大小。

链路层之间传递的载荷的最大大小，单位为八位字节。

连接等时（Connected ISO）的取值范围为 `BT_ISO_CONNECTED_PDU_MIN` 到 `BT_ISO_PDU_MAX`。

广播等时（Broadcast ISO）的取值范围为 `BT_ISO_BROADCAST_PDU_MIN` 到 `BT_ISO_PDU_MAX`。

<a id="a2180a4f82e4cdf5288b7f67701a16ad6"></a>

### `phy`

```c
uint8_t bt_iso_chan_io_qos::phy
```

通道物理层（Channel PHY），参见 `bt_gap_le_phy` 的取值。

设置为 `BT_GAP_LE_PHY_NONE` 无效。

<a id="a5106bfd09f6be52604e7c7f0e3390684"></a>

### `rtn`

```c
uint8_t bt_iso_chan_io_qos::rtn
```

通道重传次数（Channel Retransmission Number）。

设置任何高级等时参数（Advanced ISO parameters）后，此值均被忽略。

<a id="ae52611dc326b6777620ff7aa43f566e9"></a>

### `sdu`

```c
uint16_t bt_iso_chan_io_qos::sdu
```

通道服务数据单元（Channel SDU）。

取值范围为 `BT_ISO_MIN_SDU` 至 `BT_ISO_MAX_SDU`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)
- [BT_ISO_BN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2905cddfa456fc846f0c8025487b404d)
- [BT_ISO_BN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac05f4f51ea04962679f616bb167b724d)
- [BT_ISO_CONNECTED_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4e29d5966f959114754d62a8763c8c1e)
- [BT_ISO_PDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga88fb5690cd1cab4e5e8d5c025cc1af00)
- [BT_ISO_BROADCAST_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaee766ff789f1bf01f75c88112ddd2afa)
- [BT_GAP_LE_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)
- [BT_ISO_MIN_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4cc5565eeda9a3661d49d485637d1db2)
- [BT_ISO_MAX_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa5d5588e7229db16219b0c44921bbcf7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_bt_iso_chan_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_bt_iso_chan_ops_结构体.md)
