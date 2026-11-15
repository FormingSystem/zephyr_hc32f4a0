---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-47
title: bt_cap_unicast_group_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_bt\_cap\_unicast\_group\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

使用 `bt_cap_unicast_group_create()` 创建单播组的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

使用 `bt_cap_unicast_group_create()` 创建单播组的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ab9748e9e230048af64ce9c9ce1006952"></a>

```c
size_t params_count
```

相关声明：[params_count](#ab9748e9e230048af64ce9c9ce1006952)。

`params` 中的参数数量。

<a id="r_a64ca2c5cc4f34821e567841ec8efe67b"></a>

```c
struct bt_cap_unicast_group_stream_pair_param * params
```

相关声明：[bt_cap_unicast_group_stream_pair_param](P048_bt_cap_unicast_group_stream_pair_param_结构体.md)、[params](#a64ca2c5cc4f34821e567841ec8efe67b)。

流参数数组（Stream Parameters Array）。

<a id="r_a97e67b903e72dd1f0fef4961810288b1"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a97e67b903e72dd1f0fef4961810288b1)。

单播组打包模式（Unicast Group Packing Mode）。

<a id="r_adb6cb5686b3d827156aef325b3dcdc84"></a>

```c
uint8_t c_to_p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_to_p_ft](#adb6cb5686b3d827156aef325b3dcdc84)。

中心设备到外围设备的清除超时（Flush Timeout）。

<a id="r_ab424be389b026ac5857e3bec1c3d686f"></a>

```c
uint8_t p_to_c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_to_c_ft](#ab424be389b026ac5857e3bec1c3d686f)。

外围设备到中心设备的清除超时。

<a id="r_ac52a0e09e3978a084e4fe558e4a5a848"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#ac52a0e09e3978a084e4fe558e4a5a848)。

等时间隔（ISO Interval）。

## 47.2\_详细说明（Detailed Documentation）

<a id="adb6cb5686b3d827156aef325b3dcdc84"></a>

### `c_to_p_ft`

```c
uint8_t bt_cap_unicast_group_param::c_to_p_ft
```

中心设备到外围设备的清除超时（Flush Timeout）。

从中心设备发送到外围设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="ac52a0e09e3978a084e4fe558e4a5a848"></a>

### `iso_interval`

```c
uint16_t bt_cap_unicast_group_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 CIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="ab424be389b026ac5857e3bec1c3d686f"></a>

### `p_to_c_ft`

```c
uint8_t bt_cap_unicast_group_param::p_to_c_ft
```

外围设备到中心设备的清除超时。

从外围设备发送到中心设备的每个载荷的清除超时，以 `ISO_Interval` 的倍数表示。

取值范围为 `BT_ISO_FT_MIN` 到 `BT_ISO_FT_MAX`。

<a id="a97e67b903e72dd1f0fef4961810288b1"></a>

### `packing`

```c
uint8_t bt_cap_unicast_group_param::packing
```

单播组打包模式（Unicast Group Packing Mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

说明（Note）：这是向控制器提出的建议，控制器可以忽略它。

<a id="a64ca2c5cc4f34821e567841ec8efe67b"></a>

### `params`

```c
struct bt_cap_unicast_group_stream_pair_param* bt_cap_unicast_group_param::params
```

流参数数组（Stream Parameters Array）。

<a id="ab9748e9e230048af64ce9c9ce1006952"></a>

### `params_count`

```c
size_t bt_cap_unicast_group_param::params_count
```

`params` 中的参数数量。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 47.3\_原页交叉引用（Cross References）

- [bt_cap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_unicast_group_stream_pair_param](P048_bt_cap_unicast_group_stream_pair_param_结构体.md)
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

[上一章](P046_bt_cap_unicast_group_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_bt_cap_unicast_group_stream_pair_param_结构体.md)
