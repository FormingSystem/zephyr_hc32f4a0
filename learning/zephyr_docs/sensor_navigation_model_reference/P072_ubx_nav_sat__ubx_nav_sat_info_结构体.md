---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-72
title: ubx_nav_sat__ubx_nav_sat_info_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__sat_1_1ubx__nav__sat__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_ubx\_nav\_sat\_\_ubx\_nav\_sat\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__sat_1_1ubx__nav__sat__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a04fc29e6cf9f1ff6f1f638ae633d5a11"></a>

```c
uint8_t gnss_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[gnss_id](#a04fc29e6cf9f1ff6f1f638ae633d5a11)。

<a id="r_ab7ba4e9d36ab136c0bb8fde9b4f9b3e5"></a>

```c
uint8_t sv_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sv_id](#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5)。

<a id="r_a83e6ba9e50cc24fc0d80de3947daf571"></a>

```c
uint8_t cno
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cno](#a83e6ba9e50cc24fc0d80de3947daf571)。

<a id="r_a9133131e06119371d14be09f99b24a8e"></a>

```c
int8_t elevation
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[elevation](#a9133131e06119371d14be09f99b24a8e)。

<a id="r_a3a50255230b6ed80bfa4eb8ff83acf89"></a>

```c
int16_t azimuth
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[azimuth](#a3a50255230b6ed80bfa4eb8ff83acf89)。

<a id="r_a442709d1e9b43ae8c27606a5fb878c89"></a>

```c
int16_t pseu_res
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[pseu_res](#a442709d1e9b43ae8c27606a5fb878c89)。

<a id="r_ac6872360564b383ce2cd5a061717c8fe"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#ac6872360564b383ce2cd5a061717c8fe)。

## 72.2\_详细说明（Detailed Documentation）

<a id="a3a50255230b6ed80bfa4eb8ff83acf89"></a>

### `azimuth`

```c
int16_t ubx_nav_sat::ubx_nav_sat_info::azimuth
```

<a id="a83e6ba9e50cc24fc0d80de3947daf571"></a>

### `cno`

```c
uint8_t ubx_nav_sat::ubx_nav_sat_info::cno
```

<a id="a9133131e06119371d14be09f99b24a8e"></a>

### `elevation`

```c
int8_t ubx_nav_sat::ubx_nav_sat_info::elevation
```

<a id="ac6872360564b383ce2cd5a061717c8fe"></a>

### `flags`

```c
uint32_t ubx_nav_sat::ubx_nav_sat_info::flags
```

<a id="a04fc29e6cf9f1ff6f1f638ae633d5a11"></a>

### `gnss_id`

```c
uint8_t ubx_nav_sat::ubx_nav_sat_info::gnss_id
```

<a id="a442709d1e9b43ae8c27606a5fb878c89"></a>

### `pseu_res`

```c
int16_t ubx_nav_sat::ubx_nav_sat_info::pseu_res
```

<a id="ab7ba4e9d36ab136c0bb8fde9b4f9b3e5"></a>

### `sv_id`

```c
uint8_t ubx_nav_sat::ubx_nav_sat_info::sv_id
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_ubx_nav_sat_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_veml60xx_it_data_结构体.md)
