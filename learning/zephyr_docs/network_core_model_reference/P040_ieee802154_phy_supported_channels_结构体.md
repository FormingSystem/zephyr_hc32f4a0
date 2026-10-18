---
id: learning.zephyr-docs.network-core-model-reference.page-40
title: ieee802154_phy_supported_channels_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__phy__supported__channels.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_ieee802154\_phy\_supported\_channels\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__phy__supported__channels.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示驱动对给定接口支持的信道列表，见IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

表示驱动对给定接口支持的信道列表，见IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a73ccabf887b567a0ce3ddc5f8a3eeed1"></a>

```c
const struct ieee802154_phy_channel_range *const ranges
```

相关声明：[ieee802154_phy_channel_range](P039_ieee802154_phy_channel_range_结构体.md)、[ranges](#a73ccabf887b567a0ce3ddc5f8a3eeed1)。

指向信道范围结构（Channel Range Structures）数组的指针。

<a id="r_a8fb56a7fc6be96035cf4b51891582da9"></a>

```c
const uint8_t num_ranges
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ranges](#a8fb56a7fc6be96035cf4b51891582da9)。

当前可用信道范围（Channel Ranges）的数量。

## 40.2\_详细说明（Detailed Documentation）

<a id="a8fb56a7fc6be96035cf4b51891582da9"></a>

### `num_ranges`

```c
const uint8_t ieee802154_phy_supported_channels::num_ranges
```

当前可用信道范围（Channel Ranges）的数量。

<a id="a73ccabf887b567a0ce3ddc5f8a3eeed1"></a>

### `ranges`

```c
const struct ieee802154_phy_channel_range* const ieee802154_phy_supported_channels::ranges
```

指向信道范围结构（Channel Range Structures）数组的指针。

**警告（Warning）**：警告（Warning）：此指针必须在接口的整个生命周期内有效且保持不变。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 40.3\_原页交叉引用（Cross References）

- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d)
- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [ieee802154_phy_channel_range](P039_ieee802154_phy_channel_range_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_ieee802154_phy_channel_range_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_ieee802154_radio_api_结构体.md)
