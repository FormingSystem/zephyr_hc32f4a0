---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-83
title: sdhc_host_props_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__props.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_sdhc\_host\_props\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__props.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD主控制器（Host Controller）的属性。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

SD 主机控制器属性（Host controller properties）。由主机控制器通过 `sdhc_get_host_props` API 填充。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 83.1\_数据成员（Data Fields）

<a id="r_aef7123dfa5690bc0525aa40dc623307c"></a>

```c
unsigned int f_max
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[f_max](#aef7123dfa5690bc0525aa40dc623307c)。

最高总线频率。

<a id="r_a28c69ba3fdae1393daa551f3f9b91057"></a>

```c
unsigned int f_min
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[f_min](#a28c69ba3fdae1393daa551f3f9b91057)。

最低总线频率。

<a id="r_a7f7b22b7b8fb46df0ec19e2bef2a4702"></a>

```c
unsigned int power_delay
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[power_delay](#a7f7b22b7b8fb46df0ec19e2bef2a4702)。

供 SD 上电或掉电所需的延迟，单位为毫秒。

<a id="r_ad60bf89e594a031f6be015888466a113"></a>

```c
struct sdhc_host_caps host_caps
```

相关声明：[sdhc_host_caps](P082_sdhc_host_caps_结构体.md)、[host_caps](#ad60bf89e594a031f6be015888466a113)。

主机能力位域（Host capability bitfield）。

<a id="r_afebe4aad820c1672635fd30aacec20e4"></a>

```c
uint32_t max_current_330
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current_330](#afebe4aad820c1672635fd30aacec20e4)。

3.3 V 时的最大电流，单位为 mA。

<a id="r_ac247312c9b10768fe878afc5c85d9eba"></a>

```c
uint32_t max_current_300
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current_300](#ac247312c9b10768fe878afc5c85d9eba)。

3.0 V 时的最大电流，单位为 mA。

<a id="r_a43d2b80ec0a5682783e4297c734a3c88"></a>

```c
uint32_t max_current_180
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_current_180](#a43d2b80ec0a5682783e4297c734a3c88)。

1.8 V 时的最大电流，单位为 mA。

<a id="r_a4a6ebccaddfc4bb99b0bbb628ffabb21"></a>

```c
bool bus_4_bit_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bus_4_bit_support](#a4a6ebccaddfc4bb99b0bbb628ffabb21)。

是否支持 4 位总线。

<a id="r_a6401a11a8ac85cf3951ec138173f87b7"></a>

```c
bool hs200_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[hs200_support](#a6401a11a8ac85cf3951ec138173f87b7)。

是否支持 HS200。

<a id="r_aec7874d1012fe5fb881c3ca5e913391e"></a>

```c
bool hs400_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[hs400_support](#aec7874d1012fe5fb881c3ca5e913391e)。

是否支持 HS400。

<a id="r_a7af8f0a9564db9ef0630a8bc85ac34a9"></a>

```c
bool hs400_enhanced_strobe_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[hs400_enhanced_strobe_support](#a7af8f0a9564db9ef0630a8bc85ac34a9)。

是否支持 HS400 增强选通（Enhanced strobe）。

<a id="r_abb18e33d99ed1e4a4400dccd2149816f"></a>

```c
bool is_spi
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_spi](#abb18e33d99ed1e4a4400dccd2149816f)。

主机是否使用 SPI 模式。

## 83.2\_详细说明（Detailed Documentation）

<a id="a4a6ebccaddfc4bb99b0bbb628ffabb21"></a>

### `bus_4_bit_support`

```c
bool sdhc_host_props::bus_4_bit_support
```

是否支持 4 位总线。

<a id="aef7123dfa5690bc0525aa40dc623307c"></a>

### `f_max`

```c
unsigned int sdhc_host_props::f_max
```

最高总线频率。

<a id="a28c69ba3fdae1393daa551f3f9b91057"></a>

### `f_min`

```c
unsigned int sdhc_host_props::f_min
```

最低总线频率。

<a id="ad60bf89e594a031f6be015888466a113"></a>

### `host_caps`

```c
struct sdhc_host_caps sdhc_host_props::host_caps
```

主机能力位域（Host capability bitfield）。

<a id="a6401a11a8ac85cf3951ec138173f87b7"></a>

### `hs200_support`

```c
bool sdhc_host_props::hs200_support
```

是否支持 HS200。

<a id="a7af8f0a9564db9ef0630a8bc85ac34a9"></a>

### `hs400_enhanced_strobe_support`

```c
bool sdhc_host_props::hs400_enhanced_strobe_support
```

是否支持 HS400 增强选通（Enhanced strobe）。

<a id="aec7874d1012fe5fb881c3ca5e913391e"></a>

### `hs400_support`

```c
bool sdhc_host_props::hs400_support
```

是否支持 HS400。

<a id="abb18e33d99ed1e4a4400dccd2149816f"></a>

### `is_spi`

```c
bool sdhc_host_props::is_spi
```

主机是否使用 SPI 模式。

<a id="a43d2b80ec0a5682783e4297c734a3c88"></a>

### `max_current_180`

```c
uint32_t sdhc_host_props::max_current_180
```

1.8 V 时的最大电流，单位为 mA。

<a id="ac247312c9b10768fe878afc5c85d9eba"></a>

### `max_current_300`

```c
uint32_t sdhc_host_props::max_current_300
```

3.0 V 时的最大电流，单位为 mA。

<a id="afebe4aad820c1672635fd30aacec20e4"></a>

### `max_current_330`

```c
uint32_t sdhc_host_props::max_current_330
```

3.3 V 时的最大电流，单位为 mA。

<a id="a7f7b22b7b8fb46df0ec19e2bef2a4702"></a>

### `power_delay`

```c
unsigned int sdhc_host_props::power_delay
```

供 SD 上电或掉电所需的延迟，单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 83.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [sdhc_host_caps](P082_sdhc_host_caps_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [sdhc_get_host_props](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab55cf88ae79e5aa9e2110b298048df8e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P082_sdhc_host_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_sdhc_io_结构体.md)
