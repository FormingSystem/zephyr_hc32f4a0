---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-35
title: mmc_ext_csd_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmmc__ext__csd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_mmc\_ext\_csd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmmc__ext__csd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多媒体卡（MMC）的扩展卡专用数据寄存器（Extended CSD）。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

MMC 扩展卡专用数据寄存器（Extended Card Specific Data register，EXT_CSD）。此寄存器包含 MMC 卡的附加数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a44aa7d6d1282a00a1875e92fb5b3c4b8"></a>

```c
uint32_t sec_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sec_count](#a44aa7d6d1282a00a1875e92fb5b3c4b8)。

扇区计数（Sector Count）`[215:212]`。

<a id="r_a63545477058cce0c5727637bcbb06a47"></a>

```c
uint8_t bus_width
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bus_width](#a63545477058cce0c5727637bcbb06a47)。

总线宽度模式（Bus Width Mode）`[183]`。

<a id="r_aa5089c06fcc9b6b60749388b594a12f5"></a>

```c
bool enhanced_strobe_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enhanced_strobe_support](#aa5089c06fcc9b6b60749388b594a12f5)。

增强选通支持（Enhanced strobe support）`[184]`。

<a id="r_a25fe8f962635be3d40b449203e7d34a2"></a>

```c
enum mmc_timing_mode hs_timing
```

相关声明：[mmc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#ae1956c4b374e2c8b6a585596e93ac345)、[hs_timing](#a25fe8f962635be3d40b449203e7d34a2)。

高速时序模式（High Speed Timing Mode）`[185]`。

<a id="r_a4c26010052a69e060742e0a05b6ad98b"></a>

```c
struct mmc_device_type device_type
```

相关声明：[mmc_device_type](P034_mmc_device_type_结构体.md)、[device_type](#a4c26010052a69e060742e0a05b6ad98b)。

设备类型（Device Type）`[196]`。

<a id="r_a3ee512cb3c0e3698d940c04eed3aa665"></a>

```c
enum mmc_ext_csd_rev rev
```

相关声明：[mmc_ext_csd_rev](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#ac86d8a44f37c771cb666f69a516dff81)、[rev](#a3ee512cb3c0e3698d940c04eed3aa665)。

扩展 CSD 修订版本（Revision）`[192]`。

<a id="r_a286b2783ac15dbec6fa3953f0cd69af4"></a>

```c
uint8_t power_class
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[power_class](#a286b2783ac15dbec6fa3953f0cd69af4)。

选定的功率等级（Power class）`[187]`。

<a id="r_a29a7f7502e6e6d93e76392b8ac45356f"></a>

```c
uint8_t mmc_driver_strengths
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mmc_driver_strengths](#a29a7f7502e6e6d93e76392b8ac45356f)。

驱动强度（Driver strengths）`[197]`。

<a id="r_acab002b3a28a3dc9bf58187e9e19a9fe"></a>

```c
uint8_t pwr_class_200MHZ_VCCQ195
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pwr_class_200MHZ_VCCQ195](#acab002b3a28a3dc9bf58187e9e19a9fe)。

`VCC != 1.95V` 时 HS200 的功率等级信息 `[237]`。

<a id="r_a3a38f805cac18f3429f57edc7cbf2134"></a>

```c
uint8_t pwr_class_HS400
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pwr_class_HS400](#a3a38f805cac18f3429f57edc7cbf2134)。

HS400 的功率等级信息 `[253]`。

<a id="r_a3aafc3e2b5b59cb79535411178a35efe"></a>

```c
uint32_t cache_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cache_size](#a3aafc3e2b5b59cb79535411178a35efe)。

eMMC 缓存大小（Cache size）`[252:249]`。

## 35.2\_详细说明（Detailed Documentation）

<a id="a63545477058cce0c5727637bcbb06a47"></a>

### `bus_width`

```c
uint8_t mmc_ext_csd::bus_width
```

总线宽度模式（Bus Width Mode）`[183]`。

<a id="a3aafc3e2b5b59cb79535411178a35efe"></a>

### `cache_size`

```c
uint32_t mmc_ext_csd::cache_size
```

eMMC 缓存大小（Cache size）`[252:249]`。

<a id="a4c26010052a69e060742e0a05b6ad98b"></a>

### `device_type`

```c
struct mmc_device_type mmc_ext_csd::device_type
```

设备类型（Device Type）`[196]`。

<a id="aa5089c06fcc9b6b60749388b594a12f5"></a>

### `enhanced_strobe_support`

```c
bool mmc_ext_csd::enhanced_strobe_support
```

增强选通支持（Enhanced strobe support）`[184]`。

<a id="a25fe8f962635be3d40b449203e7d34a2"></a>

### `hs_timing`

```c
enum mmc_timing_mode mmc_ext_csd::hs_timing
```

高速时序模式（High Speed Timing Mode）`[185]`。

<a id="a29a7f7502e6e6d93e76392b8ac45356f"></a>

### `mmc_driver_strengths`

```c
uint8_t mmc_ext_csd::mmc_driver_strengths
```

驱动强度（Driver strengths）`[197]`。

<a id="a286b2783ac15dbec6fa3953f0cd69af4"></a>

### `power_class`

```c
uint8_t mmc_ext_csd::power_class
```

选定的功率等级（Power class）`[187]`。

<a id="acab002b3a28a3dc9bf58187e9e19a9fe"></a>

### `pwr_class_200MHZ_VCCQ195`

```c
uint8_t mmc_ext_csd::pwr_class_200MHZ_VCCQ195
```

`VCC != 1.95V` 时 HS200 的功率等级信息 `[237]`。

<a id="a3a38f805cac18f3429f57edc7cbf2134"></a>

### `pwr_class_HS400`

```c
uint8_t mmc_ext_csd::pwr_class_HS400
```

HS400 的功率等级信息 `[253]`。

<a id="a3ee512cb3c0e3698d940c04eed3aa665"></a>

### `rev`

```c
enum mmc_ext_csd_rev mmc_ext_csd::rev
```

扩展 CSD 修订版本（Revision）`[192]`。

<a id="a44aa7d6d1282a00a1875e92fb5b3c4b8"></a>

### `sec_count`

```c
uint32_t mmc_ext_csd::sec_count
```

扇区计数（Sector Count）`[215:212]`。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mmc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#ae1956c4b374e2c8b6a585596e93ac345)
- [mmc_device_type](P034_mmc_device_type_结构体.md)
- [mmc_ext_csd_rev](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#ac86d8a44f37c771cb666f69a516dff81)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_mmc_device_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_mspi_cadence_timing_cfg_结构体.md)
