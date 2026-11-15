---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-58
title: ubx_cfg_nav5_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__nav5.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_ubx\_cfg\_nav5\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__nav5.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a564548f9609493061e995219f6397060"></a>

```c
uint16_t apply
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[apply](#a564548f9609493061e995219f6397060)。

<a id="r_a70f931b76bcd7a07a225648a15e73493"></a>

```c
uint8_t dyn_model
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dyn_model](#a70f931b76bcd7a07a225648a15e73493)。

<a id="r_aab1b8aec77c186c576be839f728bba70"></a>

```c
uint8_t fix_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fix_mode](#aab1b8aec77c186c576be839f728bba70)。

<a id="r_af915a692066df1855c270e106c1981ca"></a>

```c
int32_t fixed_alt
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[fixed_alt](#af915a692066df1855c270e106c1981ca)。

<a id="r_abb48bda50e725eb8c2973518b468916f"></a>

```c
uint32_t fixed_alt_var
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fixed_alt_var](#abb48bda50e725eb8c2973518b468916f)。

<a id="r_a2e7353d4ef2f0b3eef4ae3d1cc2be5ed"></a>

```c
int8_t min_elev
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[min_elev](#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed)。

<a id="r_ace7d12cf8f63904274e658a6afe149d5"></a>

```c
uint8_t dr_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dr_limit](#ace7d12cf8f63904274e658a6afe149d5)。

<a id="r_a7c7f4338463e4d0c8040971ec31dc92c"></a>

```c
uint16_t p_dop
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_dop](#a7c7f4338463e4d0c8040971ec31dc92c)。

<a id="r_a4d8537de40aa5c98ae2e2183da9d44c3"></a>

```c
uint16_t t_dop
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_dop](#a4d8537de40aa5c98ae2e2183da9d44c3)。

<a id="r_a19d69c52edac0f65e2892b4c476d5a76"></a>

```c
uint16_t p_acc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_acc](#a19d69c52edac0f65e2892b4c476d5a76)。

<a id="r_ad78a8828482ce26597f80f5e5a548afd"></a>

```c
uint16_t t_acc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_acc](#ad78a8828482ce26597f80f5e5a548afd)。

<a id="r_a5afd803452c65c4f03b122c9ff59cf2b"></a>

```c
uint8_t static_hold_thresh
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[static_hold_thresh](#a5afd803452c65c4f03b122c9ff59cf2b)。

<a id="r_a2ee4fc58054c5f049890914c73089c99"></a>

```c
uint8_t dgnss_timeout
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dgnss_timeout](#a2ee4fc58054c5f049890914c73089c99)。

<a id="r_a648e22442293b24b2aa8b264a78b9bd2"></a>

```c
uint8_t cno_thresh_num_svs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cno_thresh_num_svs](#a648e22442293b24b2aa8b264a78b9bd2)。

<a id="r_abf2a3de97f8d9cade6ec18408452938a"></a>

```c
uint8_t cno_thresh
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cno_thresh](#abf2a3de97f8d9cade6ec18408452938a)。

<a id="r_ab6b5cd2ef8db8c281f77c6684f6f8c0c"></a>

```c
uint8_t reserved1 [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved1](#ab6b5cd2ef8db8c281f77c6684f6f8c0c)。

<a id="r_a6108faff3832cab3d734020c030c5c6c"></a>

```c
uint16_t static_hold_max_dist
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[static_hold_max_dist](#a6108faff3832cab3d734020c030c5c6c)。

<a id="r_ae0ecd871977ad119009cf1a2ac617327"></a>

```c
uint8_t utc_standard
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[utc_standard](#ae0ecd871977ad119009cf1a2ac617327)。

<a id="r_ac3d21a048e77c404bcfa180af2e41992"></a>

```c
uint8_t reserved2 [5]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved2](#ac3d21a048e77c404bcfa180af2e41992)。

## 58.2\_详细说明（Detailed Documentation）

<a id="a564548f9609493061e995219f6397060"></a>

### `apply`

```c
uint16_t ubx_cfg_nav5::apply
```

<a id="abf2a3de97f8d9cade6ec18408452938a"></a>

### `cno_thresh`

```c
uint8_t ubx_cfg_nav5::cno_thresh
```

<a id="a648e22442293b24b2aa8b264a78b9bd2"></a>

### `cno_thresh_num_svs`

```c
uint8_t ubx_cfg_nav5::cno_thresh_num_svs
```

<a id="a2ee4fc58054c5f049890914c73089c99"></a>

### `dgnss_timeout`

```c
uint8_t ubx_cfg_nav5::dgnss_timeout
```

<a id="ace7d12cf8f63904274e658a6afe149d5"></a>

### `dr_limit`

```c
uint8_t ubx_cfg_nav5::dr_limit
```

<a id="a70f931b76bcd7a07a225648a15e73493"></a>

### `dyn_model`

```c
uint8_t ubx_cfg_nav5::dyn_model
```

<a id="aab1b8aec77c186c576be839f728bba70"></a>

### `fix_mode`

```c
uint8_t ubx_cfg_nav5::fix_mode
```

<a id="af915a692066df1855c270e106c1981ca"></a>

### `fixed_alt`

```c
int32_t ubx_cfg_nav5::fixed_alt
```

<a id="abb48bda50e725eb8c2973518b468916f"></a>

### `fixed_alt_var`

```c
uint32_t ubx_cfg_nav5::fixed_alt_var
```

<a id="a2e7353d4ef2f0b3eef4ae3d1cc2be5ed"></a>

### `min_elev`

```c
int8_t ubx_cfg_nav5::min_elev
```

<a id="a19d69c52edac0f65e2892b4c476d5a76"></a>

### `p_acc`

```c
uint16_t ubx_cfg_nav5::p_acc
```

<a id="a7c7f4338463e4d0c8040971ec31dc92c"></a>

### `p_dop`

```c
uint16_t ubx_cfg_nav5::p_dop
```

<a id="ab6b5cd2ef8db8c281f77c6684f6f8c0c"></a>

### `reserved1`

```c
uint8_t ubx_cfg_nav5::reserved1[2]
```

<a id="ac3d21a048e77c404bcfa180af2e41992"></a>

### `reserved2`

```c
uint8_t ubx_cfg_nav5::reserved2[5]
```

<a id="a6108faff3832cab3d734020c030c5c6c"></a>

### `static_hold_max_dist`

```c
uint16_t ubx_cfg_nav5::static_hold_max_dist
```

<a id="a5afd803452c65c4f03b122c9ff59cf2b"></a>

### `static_hold_thresh`

```c
uint8_t ubx_cfg_nav5::static_hold_thresh
```

<a id="ad78a8828482ce26597f80f5e5a548afd"></a>

### `t_acc`

```c
uint16_t ubx_cfg_nav5::t_acc
```

<a id="a4d8537de40aa5c98ae2e2183da9d44c3"></a>

### `t_dop`

```c
uint16_t ubx_cfg_nav5::t_dop
```

<a id="ae0ecd871977ad119009cf1a2ac617327"></a>

### `utc_standard`

```c
uint8_t ubx_cfg_nav5::utc_standard
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_ubx_cfg_msg_rate_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_ubx_cfg_prt_结构体.md)
