---
id: learning.zephyr-docs.audio-video-model-reference.page-47
title: sbc_encoder_init_param_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsbc__encoder__init__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_sbc\_encoder\_init\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsbc__encoder__init__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

编码器初始化参数（Encoder Initialization Parameters）。

```c
#include <zephyr/bluetooth/sbc.h>
```

<a id="details"></a>

编码器初始化参数（Encoder Initialization Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a9a89d1044e10290e40265b64cd26067b"></a>

```c
uint32_t bit_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bit_rate](#a9a89d1044e10290e40265b64cd26067b)。

编码后的比特率（bit rate）。

<a id="r_a81742a0770d1f6e3723015baa2152edd"></a>

```c
uint32_t samp_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[samp_freq](#a81742a0770d1f6e3723015baa2152edd)。

采样频率（sample frequency）。

<a id="r_a9f2e03203a3ef41303c8de9c93198db1"></a>

```c
uint8_t blk_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[blk_len](#a9f2e03203a3ef41303c8de9c93198db1)。

块长度（block length）。

<a id="r_ad1f099d0d03f0c0d10febf2f7b3502d7"></a>

```c
uint8_t subband
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subband](#ad1f099d0d03f0c0d10febf2f7b3502d7)。

子带（subband）数量。

<a id="r_a3b8a6758fc1ef3c1c5ef1348e4d12ca9"></a>

```c
enum sbc_alloc_mthd alloc_mthd
```

相关声明：[sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)、[alloc_mthd](#a3b8a6758fc1ef3c1c5ef1348e4d12ca9)。

分配方法（allocation method）。

<a id="r_afb951bb13f5ad27ea9bba9ebc82e9776"></a>

```c
enum sbc_ch_mode ch_mode
```

相关声明：[sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)、[ch_mode](#afb951bb13f5ad27ea9bba9ebc82e9776)。

通道模式（channel mode）。

<a id="r_a668a198600211325788a168efe15d016"></a>

```c
uint8_t ch_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_num](#a668a198600211325788a168efe15d016)。

通道数量。

<a id="r_a5b537961f58be5b9b6df11f0afe4f990"></a>

```c
uint8_t min_bitpool
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_bitpool](#a5b537961f58be5b9b6df11f0afe4f990)。

最小比特池（bitpool）值。

<a id="r_a96a0c9a9657a6dce6e08e0648d844379"></a>

```c
uint8_t max_bitpool
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_bitpool](#a96a0c9a9657a6dce6e08e0648d844379)。

最大比特池（bitpool）值。

## 47.2\_详细说明（Detailed Documentation）

<a id="a3b8a6758fc1ef3c1c5ef1348e4d12ca9"></a>

### `alloc_mthd`

```c
enum sbc_alloc_mthd sbc_encoder_init_param::alloc_mthd
```

分配方法（allocation method）。

<a id="a9a89d1044e10290e40265b64cd26067b"></a>

### `bit_rate`

```c
uint32_t sbc_encoder_init_param::bit_rate
```

编码后的比特率（bit rate）。

<a id="a9f2e03203a3ef41303c8de9c93198db1"></a>

### `blk_len`

```c
uint8_t sbc_encoder_init_param::blk_len
```

块长度（block length）。

<a id="afb951bb13f5ad27ea9bba9ebc82e9776"></a>

### `ch_mode`

```c
enum sbc_ch_mode sbc_encoder_init_param::ch_mode
```

通道模式（channel mode）。

<a id="a668a198600211325788a168efe15d016"></a>

### `ch_num`

```c
uint8_t sbc_encoder_init_param::ch_num
```

通道数量。

<a id="a96a0c9a9657a6dce6e08e0648d844379"></a>

### `max_bitpool`

```c
uint8_t sbc_encoder_init_param::max_bitpool
```

最大比特池（bitpool）值。

<a id="a5b537961f58be5b9b6df11f0afe4f990"></a>

### `min_bitpool`

```c
uint8_t sbc_encoder_init_param::min_bitpool
```

最小比特池（bitpool）值。

<a id="a81742a0770d1f6e3723015baa2152edd"></a>

### `samp_freq`

```c
uint32_t sbc_encoder_init_param::samp_freq
```

采样频率（sample frequency）。

<a id="ad1f099d0d03f0c0d10febf2f7b3502d7"></a>

### `subband`

```c
uint8_t sbc_encoder_init_param::subband
```

子带（subband）数量。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/sbc.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/sbc.h](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)
- [sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_sbc_encoder_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_uaol_capabilities_结构体.md)
