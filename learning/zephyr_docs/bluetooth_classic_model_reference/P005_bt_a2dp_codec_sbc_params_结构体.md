---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-5
title: bt_a2dp_codec_sbc_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__sbc__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_a2dp\_codec\_sbc\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__sbc__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子带编解码器（Subband Codec，SBC）。

```c
#include <zephyr/bluetooth/classic/a2dp_codec_sbc.h>
```

<a id="details"></a>

子带编解码器（Subband Codec，SBC）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a80b0705befa9c573e4653a5f88f81e8d"></a>

```c
uint8_t config [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config](#a80b0705befa9c573e4653a5f88f81e8d)。

配置的前两个八位字节（Octets）。

<a id="r_a026f28b42a3e8b41a2597cfa4ca01f95"></a>

```c
uint8_t min_bitpool
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_bitpool](#a026f28b42a3e8b41a2597cfa4ca01f95)。

最小比特池值（Minimum Bitpool Value）。

<a id="r_a34319bc3d168e5eb7d3ef2cae521ca96"></a>

```c
uint8_t max_bitpool
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_bitpool](#a34319bc3d168e5eb7d3ef2cae521ca96)。

最大比特池值（Maximum Bitpool Value）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a80b0705befa9c573e4653a5f88f81e8d"></a>

### `config`

```c
uint8_t bt_a2dp_codec_sbc_params::config[2]
```

配置的前两个八位字节（Octets）。

<a id="a34319bc3d168e5eb7d3ef2cae521ca96"></a>

### `max_bitpool`

```c
uint8_t bt_a2dp_codec_sbc_params::max_bitpool
```

最大比特池值（Maximum Bitpool Value）。

<a id="a026f28b42a3e8b41a2597cfa4ca01f95"></a>

### `min_bitpool`

```c
uint8_t bt_a2dp_codec_sbc_params::min_bitpool
```

最小比特池值（Minimum Bitpool Value）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp_codec_sbc.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp_codec_sbc.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_a2dp_codec_ie_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_a2dp_discover_param_结构体.md)
