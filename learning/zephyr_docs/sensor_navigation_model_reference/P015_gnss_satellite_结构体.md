---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-15
title: gnss_satellite_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__satellite.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_gnss\_satellite\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__satellite.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）的卫星结构。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

全球导航卫星系统（GNSS）的卫星结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a03543a7425f27c78e743b0ec180ccea7"></a>

```c
uint8_t prn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prn](#a03543a7425f27c78e743b0ec180ccea7)。

伪随机噪声序列（Pseudo-random noise sequence，PRN）。

<a id="r_a6818083aad878aa8b06d2cbeca53b1da"></a>

```c
uint8_t snr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snr](#a6818083aad878aa8b06d2cbeca53b1da)。

信噪比（Signal-to-noise ratio），单位为 dB。

<a id="r_a3d99c5ad18242a42f95b5de496ca501d"></a>

```c
uint8_t elevation
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elevation](#a3d99c5ad18242a42f95b5de496ca501d)。

仰角（Elevation），单位为度，范围为 `[0, 90]`。

<a id="r_a27a864422f5207b5d38efbd8b50893a3"></a>

```c
uint16_t azimuth
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[azimuth](#a27a864422f5207b5d38efbd8b50893a3)。

相对于真北（True North）的方位角（Azimuth），单位为度，范围为 `[0, 359]`。

<a id="r_ad9b31c85dd0e162979d384b049142549"></a>

```c
enum gnss_system system
```

相关声明：[gnss_system](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga928a05b4e820a9fcc8bc2db81f5f8c79)、[system](#ad9b31c85dd0e162979d384b049142549)。

卫星所属系统。

<a id="r_ae4c596c298ed158a188ea4a5fbd6181c"></a>

```c
uint8_t is_tracked: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_tracked](#ae4c596c298ed158a188ea4a5fbd6181c)。

正在跟踪该卫星时为 `true`。

<a id="r_a4296fad8444a7ebcd938f7550332ec52"></a>

```c
uint8_t is_corrected: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_corrected](#a4296fad8444a7ebcd938f7550332ec52)。

该卫星的跟踪使用了实时动态定位（RTK）改正时为 `true`。

## 15.2\_详细说明（Detailed Documentation）

<a id="a27a864422f5207b5d38efbd8b50893a3"></a>

### `azimuth`

```c
uint16_t gnss_satellite::azimuth
```

相对于真北（True North）的方位角（Azimuth），单位为度，范围为 `[0, 359]`。

<a id="a3d99c5ad18242a42f95b5de496ca501d"></a>

### `elevation`

```c
uint8_t gnss_satellite::elevation
```

仰角（Elevation），单位为度，范围为 `[0, 90]`。

<a id="a4296fad8444a7ebcd938f7550332ec52"></a>

### `is_corrected`

```c
uint8_t gnss_satellite::is_corrected
```

该卫星的跟踪使用了实时动态定位（RTK）改正时为 `true`。

<a id="ae4c596c298ed158a188ea4a5fbd6181c"></a>

### `is_tracked`

```c
uint8_t gnss_satellite::is_tracked
```

正在跟踪该卫星时为 `true`。

<a id="a03543a7425f27c78e743b0ec180ccea7"></a>

### `prn`

```c
uint8_t gnss_satellite::prn
```

伪随机噪声序列（Pseudo-random noise sequence，PRN）。

<a id="a6818083aad878aa8b06d2cbeca53b1da"></a>

### `snr`

```c
uint8_t gnss_satellite::snr
```

信噪比（Signal-to-noise ratio），单位为 dB。

<a id="ad9b31c85dd0e162979d384b049142549"></a>

### `system`

```c
enum gnss_system gnss_satellite::system
```

卫星所属系统。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gnss_system](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga928a05b4e820a9fcc8bc2db81f5f8c79)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_gnss_rtk_data_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_gnss_satellites_callback_结构体.md)
