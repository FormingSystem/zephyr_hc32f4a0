---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-38
title: bt_bap_unicast_group_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_bap\_unicast\_group\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

使用 `bt_bap_unicast_group_create()` 创建单播组的参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

使用 `bt_bap_unicast_group_create()` 创建单播组的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a9cd09b720fa9a31364878ba205b3b58c"></a>

```c
size_t params_count
```

相关声明：[params_count](#a9cd09b720fa9a31364878ba205b3b58c)。

`params` 中的参数数量。

<a id="r_aefae7dfccdaed2bc3f59ca63689d4f2e"></a>

```c
struct bt_bap_unicast_group_stream_pair_param * params
```

相关声明：[bt_bap_unicast_group_stream_pair_param](P039_bt_bap_unicast_group_stream_pair_param_结构体.md)、[params](#aefae7dfccdaed2bc3f59ca63689d4f2e)。

流参数数组（Stream Parameters Array）。

<a id="r_a6829c82346ca70772a4ab0dc93fbb88f"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a6829c82346ca70772a4ab0dc93fbb88f)。

单播组打包模式（Unicast Group Packing Mode）。

<a id="r_a7980c8e5c66a11507701ce2679b461ed"></a>

```c
uint8_t c_to_p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_to_p_ft](#a7980c8e5c66a11507701ce2679b461ed)。

中心设备到外围设备的清除超时（Flush Timeout）。

<a id="r_a72e2c6dbeb7b7778f92af5cab2474a7e"></a>

```c
uint8_t p_to_c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_to_c_ft](#a72e2c6dbeb7b7778f92af5cab2474a7e)。

外围设备到中心设备的清除超时。

<a id="r_a278797713b97a6520247b01caa2938b9"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a278797713b97a6520247b01caa2938b9)。

等时间隔（ISO Interval）。

## 38.2\_详细说明（Detailed Documentation）

<a id="a7980c8e5c66a11507701ce2679b461ed"></a>

### `c_to_p_ft`

```c
uint8_t bt_bap_unicast_group_param::c_to_p_ft
```

中心设备到外围设备的清除超时（Flush Timeout）。

从中心设备发送到外围设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="a278797713b97a6520247b01caa2938b9"></a>

### `iso_interval`

```c
uint16_t bt_bap_unicast_group_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 CIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="a72e2c6dbeb7b7778f92af5cab2474a7e"></a>

### `p_to_c_ft`

```c
uint8_t bt_bap_unicast_group_param::p_to_c_ft
```

外围设备到中心设备的清除超时。

从外围设备发送到中心设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="a6829c82346ca70772a4ab0dc93fbb88f"></a>

### `packing`

```c
uint8_t bt_bap_unicast_group_param::packing
```

单播组打包模式（Unicast Group Packing Mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

说明（Note）：这是向控制器提出的建议，控制器可以忽略它。

<a id="aefae7dfccdaed2bc3f59ca63689d4f2e"></a>

### `params`

```c
struct bt_bap_unicast_group_stream_pair_param* bt_bap_unicast_group_param::params
```

流参数数组（Stream Parameters Array）。

<a id="a9cd09b720fa9a31364878ba205b3b58c"></a>

### `params_count`

```c
size_t bt_bap_unicast_group_param::params_count
```

`params` 中的参数数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 38.3\_原页交叉引用（Cross References）

- [bt_bap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaafd53b5f45d998b44e94a1b58e93ba21)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_unicast_group_stream_pair_param](P039_bt_bap_unicast_group_stream_pair_param_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_ISO_FT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2d3bde6b34f6b15474926ed97ad11d98)
- [BT_ISO_FT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga011c9d5840658fd0ef244f47893ec70e)
- [BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)
- [BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_bap_unicast_group_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_bap_unicast_group_stream_pair_param_结构体.md)
