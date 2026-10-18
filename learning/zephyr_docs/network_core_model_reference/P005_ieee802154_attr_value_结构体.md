---
id: learning.zephyr-docs.network-core-model-reference.page-5
title: ieee802154_attr_value_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__attr__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_ieee802154\_attr\_value\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__attr__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4驱动的属性值（Attribute Values）。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

IEEE 802.15.4驱动属性值（Driver Attribute Values）。此结构仅用于来自驱动实现的标量属性和结构化属性，这些属性既不能实现为布尔形式的ieee802154_hw_caps，也不能由MAC第二层（L2）直接或间接推导。尤其不得（MUST NOT）使用此结构返回来自L2的配置数据。说明（Note）：为使此联合体保持适度大小，任何需要较大内存区域的属性，都应当（SHALL）通过指针提供；指针应指向驱动分配的静态内存，且在驱动实例的整个生命周期内有效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_ac35bed29b96b083573ce2bf911955442"></a>

```c
uint32_t phy_supported_channel_pages
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[phy_supported_channel_pages](#a75913597f93de1a80f96bb9dc32d38df)。

表示受支持信道页（Channel Pages）的位域，见ieee802154_phy_channel_page。

<a id="r_a2d84582b75e41e2cfa9b5d337850bdba"></a>

```c
const struct ieee802154_phy_supported_channels * phy_supported_channels
```

相关声明：[ieee802154_phy_supported_channels](P040_ieee802154_phy_supported_channels_结构体.md)、[phy_supported_channels](#a840d2f3a2502f87806ef79c6926f73f0)。

指向描述当前所选信道页可用信道范围（Channel Ranges）的结构的指针。

<a id="r_a0024c9a5fcc6167693f5d41c78b9697f"></a>

```c
uint32_t phy_hrp_uwb_supported_nominal_prfs
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[phy_hrp_uwb_supported_nominal_prfs](#af157805fb8acffb634cba4b37472bdb3)。

表示受支持HRP超宽带（HRP UWB）脉冲重复频率（PRF）的位域，见enum ieee802154_phy_hrp_uwb_nominal_prf。

<a id="r_a21799efa85150124b6333ac5c91d5f80"></a>

```c
};
```

## 5.2\_详细说明（Detailed Documentation）

<a id="a21799efa85150124b6333ac5c91d5f80"></a>

### `[union]`

```c
union { ... } ieee802154_attr_value
```

<a id="af157805fb8acffb634cba4b37472bdb3"></a>

### `phy_hrp_uwb_supported_nominal_prfs`

```c
uint32_t ieee802154_attr_value::phy_hrp_uwb_supported_nominal_prfs
```

表示受支持HRP超宽带（HRP UWB）脉冲重复频率（PRF）的位域，见enum ieee802154_phy_hrp_uwb_nominal_prf。

说明（Note）：当前Zephyr HRP UWB驱动均未在运行时实现多个标称脉冲重复频率（Nominal PRF），因此只会设置一个位。当前PRF（UwbPrf、MCPS-DATA.request，见第8.3.2节表8-88）被视为只读、固定，并可通过受支持PRF属性获知。

<a id="a75913597f93de1a80f96bb9dc32d38df"></a>

### `phy_supported_channel_pages`

```c
uint32_t ieee802154_attr_value::phy_supported_channel_pages
```

表示受支持信道页（Channel Pages）的位域，见ieee802154_phy_channel_page。

说明（Note）：为了按标准要求保持API可扩展性，受支持的信道页（Channel Pages）建模为位图，以支持在多个信道页之间运行时切换的驱动。目前Zephyr驱动均未在运行时实现多个信道页，因此只会设置一个位。当前信道页（PHY PIB属性phyCurrentPage，见第11.3节表11-2）被视为只读、固定，并可通过受支持信道页属性获知。

<a id="a840d2f3a2502f87806ef79c6926f73f0"></a>

### `phy_supported_channels`

```c
const struct ieee802154_phy_supported_channels* ieee802154_attr_value::phy_supported_channels
```

指向描述当前所选信道页可用信道范围（Channel Ranges）的结构的指针。

所选信道页（Channel Page）对应PHY PIB属性phyCurrentPage，见上面对phy_supported_channel_pages的说明。目前可通过IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES属性获取。

多数驱动会提供单个信道页（Channel Page），其中包含一个固定信道范围，通常从0开始。

一些值得注意的例外：

- 传统信道页（Legacy channel page，即第 0 页）公开了跨不同频段、甚至跨不同物理层（PHY）的信道范围，通常单个驱动不会实现所有这些范围。
- 智能公用事业网络（SUN）和低能耗关键基础设施监测（LECIM）物理层（PHY）在单个信道页中指定大量频段和工作模式，各自的信道范围相互重叠。有些范围并非从零开始，或者包含空洞（Holes）。因此，可能需要多个范围才能表示所有可用信道。
- 超宽带物理层（UWB PHY）通常依据支持的频段，仅支持同一信道页（Channel page）中的部分信道范围。

在这些情况下，驱动可能提供自定义配置属性（Kconfig、设备树、运行时配置等），以便在同一信道页（Channel Page）的不同子范围之间切换，例如在信道页0的SubG与2.4G频段之间切换，或在SUN、LECIM物理层（PHY）的多个工作模式之间切换。

**警告（Warning）**：警告（Warning）：此指针必须在接口的整个生命周期内有效且保持不变。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ieee802154_phy_channel_page](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacabc7386bea701373dfb36ab65bd36a9)
- [ieee802154_phy_supported_channels](P040_ieee802154_phy_supported_channels_结构体.md)
- [ieee802154_phy_hrp_uwb_nominal_prf](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga13610aeef06372bc47d84464537fdded)
- [ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)
- [ieee802154_attr_value](P005_ieee802154_attr_value_结构体.md)
- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_ieee802154_address_field_plain_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_ieee802154_aux_security_hdr_结构体.md)
