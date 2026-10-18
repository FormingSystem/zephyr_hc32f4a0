---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-90
title: bt_iso_unicast_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__unicast__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_bt\_iso\_unicast\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__unicast__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时单播（ISO Unicast）的信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时单播（ISO Unicast）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_a196ff16e4e959fa656d4af265e686f09"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a196ff16e4e959fa656d4af265e686f09)。

连接等时组标识符（Connected Isochronous Group ID）。

<a id="r_abc61e1d8edcb099a02054db8ec94ba22"></a>

```c
uint8_t cis_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_id](#abc61e1d8edcb099a02054db8ec94ba22)。

连接等时流标识符（Connected Isochronous Stream ID）。

<a id="r_a029c450e2324bbc6ee8fda6d1d10deef"></a>

```c
uint32_t cig_sync_delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cig_sync_delay](#a029c450e2324bbc6ee8fda6d1d10deef)。

一个连接等时组事件（CIG event）中，所有连接等时流（CIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

<a id="r_acbc8c068907eba204d369cf76f4f112d"></a>

```c
uint32_t cis_sync_delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cis_sync_delay](#acbc8c068907eba204d369cf76f4f112d)。

一个连接等时组事件（CIG event）中，本连接等时流（CIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

<a id="r_a4d53dc6adc8d5519cf74982aa5031e74"></a>

```c
uint32_t subinterval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subinterval](#a4d53dc6adc8d5519cf74982aa5031e74)。

子间隔（Subinterval），单位为微秒。

<a id="r_a4fc402b934ae8aa65493df01c88cae34"></a>

```c
struct bt_iso_unicast_tx_info central
```

相关声明：[bt_iso_unicast_tx_info](P091_bt_iso_unicast_tx_info_结构体.md)、[central](#a4fc402b934ae8aa65493df01c88cae34)。

中心设备到外设数据路径（Central to peripheral data path）的发送信息（TX information）。

<a id="r_a03b084fefcab049efbe1a609a59d9c54"></a>

```c
struct bt_iso_unicast_tx_info peripheral
```

相关声明：[bt_iso_unicast_tx_info](P091_bt_iso_unicast_tx_info_结构体.md)、[peripheral](#a03b084fefcab049efbe1a609a59d9c54)。

外设到中心设备数据（Peripheral to central data）的发送信息（TX information）。

## 90.2\_详细说明（Detailed Documentation）

<a id="a4fc402b934ae8aa65493df01c88cae34"></a>

### `central`

```c
struct bt_iso_unicast_tx_info bt_iso_unicast_info::central
```

中心设备到外设数据路径（Central to peripheral data path）的发送信息（TX information）。

<a id="a196ff16e4e959fa656d4af265e686f09"></a>

### `cig_id`

```c
uint8_t bt_iso_unicast_info::cig_id
```

连接等时组标识符（Connected Isochronous Group ID）。

<a id="a029c450e2324bbc6ee8fda6d1d10deef"></a>

### `cig_sync_delay`

```c
uint32_t bt_iso_unicast_info::cig_sync_delay
```

一个连接等时组事件（CIG event）中，所有连接等时流（CIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

<a id="abc61e1d8edcb099a02054db8ec94ba22"></a>

### `cis_id`

```c
uint8_t bt_iso_unicast_info::cis_id
```

连接等时流标识符（Connected Isochronous Stream ID）。

<a id="acbc8c068907eba204d369cf76f4f112d"></a>

### `cis_sync_delay`

```c
uint32_t bt_iso_unicast_info::cis_sync_delay
```

一个连接等时组事件（CIG event）中，本连接等时流（CIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

<a id="a03b084fefcab049efbe1a609a59d9c54"></a>

### `peripheral`

```c
struct bt_iso_unicast_tx_info bt_iso_unicast_info::peripheral
```

外设到中心设备数据（Peripheral to central data）的发送信息（TX information）。

<a id="a4d53dc6adc8d5519cf74982aa5031e74"></a>

### `subinterval`

```c
uint32_t bt_iso_unicast_info::subinterval
```

子间隔（Subinterval），单位为微秒。

没有子间隔（Subinterval），即 `NSE = 1` 时，值为 `BT_ISO_SUBINTERVAL_NONE`；未知时为 `BT_ISO_SUBINTERVAL_UNKNOWN`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_iso_unicast_tx_info](P091_bt_iso_unicast_tx_info_结构体.md)
- [BT_ISO_SUBINTERVAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4fb7985aa35292671abe881c1570c445)
- [BT_ISO_SUBINTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8085b01de2d1facb666215282690d674)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_bt_iso_tx_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_bt_iso_unicast_tx_info_结构体.md)
