---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-75
title: bt_iso_biginfo_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__biginfo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_bt\_iso\_biginfo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__biginfo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播等时组（Broadcast Isochronous Group，BIG）的信息。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

广播等时组（Broadcast Isochronous Group，BIG）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_aa7dbfd342eecf8ffc2fce9d3fa7209ea"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#aa7dbfd342eecf8ffc2fce9d3fa7209ea)。

广播者（Advertiser）的地址。

<a id="r_a78e0a53f920980081d7b0702b02cf386"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a78e0a53f920980081d7b0702b02cf386)。

广播者 SID。

<a id="r_a10eb24596a4353da3feb0d30fed35ae7"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a10eb24596a4353da3feb0d30fed35ae7)。

广播等时组（BIG）中的广播等时流数量（BISes）。

<a id="r_a24eb83f7b54e9f949cc07e9955b4a8b8"></a>

```c
uint8_t sub_evt_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub_evt_count](#a24eb83f7b54e9f949cc07e9955b4a8b8)。

每个等时事件（Isochronous event）的最大子事件数。

<a id="r_afe96caf570314731f6c543b40d7def9a"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#afe96caf570314731f6c543b40d7def9a)。

两个广播等时组锚点（BIG anchor points）之间的间隔，为 N × 1.25 毫秒。

<a id="r_ad114dd97500d12242da77e8522133953"></a>

```c
uint8_t burst_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[burst_number](#ad114dd97500d12242da77e8522133953)。

每个广播等时流事件（BIS event）中的新载荷数量。

<a id="r_a4efb91dc2f249e41c65cd0dcbfe45bad"></a>

```c
uint8_t offset
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[offset](#a4efb91dc2f249e41c65cd0dcbfe45bad)。

预传输使用的偏移量（Offset）。

<a id="r_a8458f6d6ebe936212d928caca61b13bd"></a>

```c
uint8_t rep_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rep_count](#a8458f6d6ebe936212d928caca61b13bd)。

一个载荷在广播等时流事件（BIS event）中的发送次数。

<a id="r_af356aa29aa82c8deb63a9f47e54070a1"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#af356aa29aa82c8deb63a9f47e54070a1)。

载荷最大大小（Maximum payload size），以八位组（Octets）为单位。

<a id="r_a4a6d6cdea56a69a0b3b3fd021489750d"></a>

```c
uint32_t sdu_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sdu_interval](#a4a6d6cdea56a69a0b3b3fd021489750d)。

周期性服务数据单元（SDUs）的间隔，单位为微秒。

<a id="r_a9fddcb74f3de7eb857583a0179427f84"></a>

```c
uint16_t max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_sdu](#a9fddcb74f3de7eb857583a0179427f84)。

服务数据单元最大大小（Maximum SDU size），以八位组（Octets）为单位。

<a id="r_a2cbaf6a89e8aaf62c7048e04523e57d4"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a2cbaf6a89e8aaf62c7048e04523e57d4)。

通道物理层（Channel PHY）。

<a id="r_a1084c209d122d2d13244b77659ce28dd"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#a1084c209d122d2d13244b77659ce28dd)。

通道成帧模式（Channel framing mode）。

<a id="r_a7d54ecb896c0d6bc590311d5d5a3ac7b"></a>

```c
bool encryption
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[encryption](#a7d54ecb896c0d6bc590311d5d5a3ac7b)。

广播等时组（BIG）是否加密（Encrypted）。

## 75.2\_详细说明（Detailed Documentation）

<a id="aa7dbfd342eecf8ffc2fce9d3fa7209ea"></a>

### `addr`

```c
const bt_addr_le_t* bt_iso_biginfo::addr
```

广播者（Advertiser）的地址。

<a id="ad114dd97500d12242da77e8522133953"></a>

### `burst_number`

```c
uint8_t bt_iso_biginfo::burst_number
```

每个广播等时流事件（BIS event）中的新载荷数量。

<a id="a7d54ecb896c0d6bc590311d5d5a3ac7b"></a>

### `encryption`

```c
bool bt_iso_biginfo::encryption
```

广播等时组（BIG）是否加密（Encrypted）。

<a id="a1084c209d122d2d13244b77659ce28dd"></a>

### `framing`

```c
uint8_t bt_iso_biginfo::framing
```

通道成帧模式（Channel framing mode）。

<a id="afe96caf570314731f6c543b40d7def9a"></a>

### `iso_interval`

```c
uint16_t bt_iso_biginfo::iso_interval
```

两个广播等时组锚点（BIG anchor points）之间的间隔，为 N × 1.25 毫秒。

<a id="af356aa29aa82c8deb63a9f47e54070a1"></a>

### `max_pdu`

```c
uint16_t bt_iso_biginfo::max_pdu
```

载荷最大大小（Maximum payload size），以八位组（Octets）为单位。

<a id="a9fddcb74f3de7eb857583a0179427f84"></a>

### `max_sdu`

```c
uint16_t bt_iso_biginfo::max_sdu
```

服务数据单元最大大小（Maximum SDU size），以八位组（Octets）为单位。

<a id="a10eb24596a4353da3feb0d30fed35ae7"></a>

### `num_bis`

```c
uint8_t bt_iso_biginfo::num_bis
```

广播等时组（BIG）中的广播等时流数量（BISes）。

<a id="a4efb91dc2f249e41c65cd0dcbfe45bad"></a>

### `offset`

```c
uint8_t bt_iso_biginfo::offset
```

预传输使用的偏移量（Offset）。

<a id="a2cbaf6a89e8aaf62c7048e04523e57d4"></a>

### `phy`

```c
uint8_t bt_iso_biginfo::phy
```

通道物理层（Channel PHY）。

<a id="a8458f6d6ebe936212d928caca61b13bd"></a>

### `rep_count`

```c
uint8_t bt_iso_biginfo::rep_count
```

一个载荷在广播等时流事件（BIS event）中的发送次数。

<a id="a4a6d6cdea56a69a0b3b3fd021489750d"></a>

### `sdu_interval`

```c
uint32_t bt_iso_biginfo::sdu_interval
```

周期性服务数据单元（SDUs）的间隔，单位为微秒。

<a id="a78e0a53f920980081d7b0702b02cf386"></a>

### `sid`

```c
uint8_t bt_iso_biginfo::sid
```

广播者 SID。

<a id="a24eb83f7b54e9f949cc07e9955b4a8b8"></a>

### `sub_evt_count`

```c
uint8_t bt_iso_biginfo::sub_evt_count
```

每个等时事件（Isochronous event）的最大子事件数。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_bt_iso_big_sync_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_bt_iso_broadcaster_info_结构体.md)
