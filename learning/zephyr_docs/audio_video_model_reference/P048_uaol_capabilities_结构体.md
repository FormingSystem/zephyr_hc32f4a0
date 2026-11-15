---
id: learning.zephyr-docs.audio-video-model-reference.page-48
title: uaol_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuaol__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_uaol\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuaol__capabilities.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB音频卸载链路（UAOL）的硬件能力。

```c
#include <zephyr/drivers/uaol.h>
```

<a id="details"></a>

USB音频卸载链路（UAOL）的硬件能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a8ee3dd123ad8c5b5569d71a9051bb7ba"></a>

```c
uint32_t input_streams
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[input_streams](#a8ee3dd123ad8c5b5569d71a9051bb7ba)。

支持的输入流数量。

<a id="r_ad6bf2b46af3b8820a7ecc35e8085e6dd"></a>

```c
uint32_t output_streams
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[output_streams](#ad6bf2b46af3b8820a7ecc35e8085e6dd)。

支持的输出流数量。

<a id="r_a905a3ce47be7b6209734fb9db81a323c"></a>

```c
uint32_t bidirectional_streams
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bidirectional_streams](#a905a3ce47be7b6209734fb9db81a323c)。

支持的双向流（bidirectional streams）数量。

<a id="r_ab3206e9baa93edd745b041a2e8ae540b"></a>

```c
uint32_t max_tx_fifo_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_tx_fifo_size](#ab3206e9baa93edd745b041a2e8ae540b)。

最大发送（TX）FIFO 大小。

<a id="r_a62591bcea71bcdd7f38df544fdc5d86b"></a>

```c
uint32_t max_rx_fifo_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_rx_fifo_size](#a62591bcea71bcdd7f38df544fdc5d86b)。

最大接收（RX）FIFO 大小。

## 48.2\_详细说明（Detailed Documentation）

<a id="a905a3ce47be7b6209734fb9db81a323c"></a>

### `bidirectional_streams`

```c
uint32_t uaol_capabilities::bidirectional_streams
```

支持的双向流（bidirectional streams）数量。

<a id="a8ee3dd123ad8c5b5569d71a9051bb7ba"></a>

### `input_streams`

```c
uint32_t uaol_capabilities::input_streams
```

支持的输入流数量。

<a id="a62591bcea71bcdd7f38df544fdc5d86b"></a>

### `max_rx_fifo_size`

```c
uint32_t uaol_capabilities::max_rx_fifo_size
```

最大接收（RX）FIFO 大小。

<a id="ab3206e9baa93edd745b041a2e8ae540b"></a>

### `max_tx_fifo_size`

```c
uint32_t uaol_capabilities::max_tx_fifo_size
```

最大发送（TX）FIFO 大小。

<a id="ad6bf2b46af3b8820a7ecc35e8085e6dd"></a>

### `output_streams`

```c
uint32_t uaol_capabilities::output_streams
```

支持的输出流数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/uaol.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/uaol.h](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_sbc_encoder_init_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_uaol_config_结构体.md)
