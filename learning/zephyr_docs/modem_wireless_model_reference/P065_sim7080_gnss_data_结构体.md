---
id: learning.zephyr-docs.modem-wireless-model-reference.page-65
title: sim7080_gnss_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__gnss__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_sim7080\_gnss\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__gnss__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sim7080全球导航卫星系统（GNSS）的数据结构。

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

<a id="details"></a>

Sim7080全球导航卫星系统（GNSS）的数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_ab917d70a3c5adffb8aecc9e521c36599"></a>

```c
bool run_status
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_status](#ab917d70a3c5adffb8aecc9e521c36599)。

GNSS 是否已上电。

<a id="r_a881db8b7b52d481416bc5f373446bfc2"></a>

```c
bool fix_status
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[fix_status](#a881db8b7b52d481416bc5f373446bfc2)。

是否已取得定位结果（fix）。

<a id="r_a8a42fbb4a716a0eefe317996f8fe7a8a"></a>

```c
char utc [20]
```

相关声明：[utc](#a8a42fbb4a716a0eefe317996f8fe7a8a)。

UTC 时间，格式为 `yyyyMMddhhmmss.sss`。

<a id="r_a545077bd8eb1d6827c50b59d469bdc4a"></a>

```c
int32_t lat
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[lat](#a545077bd8eb1d6827c50b59d469bdc4a)。

纬度，单位为 `10^-7` 度。

<a id="r_a23dc6e7aa0cc507cf5141aa5329e17ef"></a>

```c
int32_t lon
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[lon](#a23dc6e7aa0cc507cf5141aa5329e17ef)。

经度，单位为 `10^-7` 度。

<a id="r_aa481937aedd2817e3a301663648d9f7d"></a>

```c
int32_t alt
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[alt](#aa481937aedd2817e3a301663648d9f7d)。

高度，单位为毫米。

<a id="r_aca6603b72f8ac67a0a0084a3fc8a60a1"></a>

```c
uint16_t hdop
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hdop](#aca6603b72f8ac67a0a0084a3fc8a60a1)。

水平精度因子（HDOP），单位为 `10^-2`。

<a id="r_a7dee72b39dc718ade2cc27bedc691d6e"></a>

```c
uint16_t cog
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cog](#a7dee72b39dc718ade2cc27bedc691d6e)。

对地航向（Course over ground），单位为 `10^-2` 度。

<a id="r_a62b8a5072942a325156a90607888612b"></a>

```c
uint16_t kmh
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[kmh](#a62b8a5072942a325156a90607888612b)。

速度，单位为 `10^-1 km/h`。

## 65.2\_详细说明（Detailed Documentation）

<a id="aa481937aedd2817e3a301663648d9f7d"></a>

### `alt`

```c
int32_t sim7080_gnss_data::alt
```

高度，单位为毫米。

<a id="a7dee72b39dc718ade2cc27bedc691d6e"></a>

### `cog`

```c
uint16_t sim7080_gnss_data::cog
```

对地航向（Course over ground），单位为 `10^-2` 度。

<a id="a881db8b7b52d481416bc5f373446bfc2"></a>

### `fix_status`

```c
bool sim7080_gnss_data::fix_status
```

是否已取得定位结果（fix）。

<a id="aca6603b72f8ac67a0a0084a3fc8a60a1"></a>

### `hdop`

```c
uint16_t sim7080_gnss_data::hdop
```

水平精度因子（HDOP），单位为 `10^-2`。

<a id="a62b8a5072942a325156a90607888612b"></a>

### `kmh`

```c
uint16_t sim7080_gnss_data::kmh
```

速度，单位为 `10^-1 km/h`。

<a id="a545077bd8eb1d6827c50b59d469bdc4a"></a>

### `lat`

```c
int32_t sim7080_gnss_data::lat
```

纬度，单位为 `10^-7` 度。

<a id="a23dc6e7aa0cc507cf5141aa5329e17ef"></a>

### `lon`

```c
int32_t sim7080_gnss_data::lon
```

经度，单位为 `10^-7` 度。

<a id="ab917d70a3c5adffb8aecc9e521c36599"></a>

### `run_status`

```c
bool sim7080_gnss_data::run_status
```

GNSS 是否已上电。

<a id="a8a42fbb4a716a0eefe317996f8fe7a8a"></a>

### `utc`

```c
char sim7080_gnss_data::utc[20]
```

UTC 时间，格式为 `yyyyMMddhhmmss.sss`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/simcom-sim7080.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/simcom-sim7080.h](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_modem_ubx_script_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_sim7080_sms_结构体.md)
