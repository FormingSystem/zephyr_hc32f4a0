---
id: learning.zephyr-docs.api-file-interface-reference.page-12
title: zephyr__drivers__dma__dma_silabs_ldma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_dma\_\_dma\_silabs\_ldma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__silabs__ldma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/dma.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_a0d4985670c10482d3999d08e4ba1fdc9"></a>

```c
#define SILABS_LDMA_SOURCE_MASK GENMASK(21, 16)
```

相关声明：[SILABS_LDMA_SOURCE_MASK](#a0d4985670c10482d3999d08e4ba1fdc9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a9559b6338f281c62c4cc28a37c6eaa1b"></a>

```c
#define SILABS_LDMA_SIG_MASK GENMASK(3, 0)
```

相关声明：[SILABS_LDMA_SIG_MASK](#a9559b6338f281c62c4cc28a37c6eaa1b)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a8b234dbc8be91a1c9ae4b6478a3ba0e9"></a>

```c
#define SILABS_DMA_SLOT_SOURCE_MASK GENMASK(7, 3)
```

相关声明：[SILABS_DMA_SLOT_SOURCE_MASK](#a8b234dbc8be91a1c9ae4b6478a3ba0e9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a9ccf7fd9a6101b88a45feaf1170de7d5"></a>

```c
#define SILABS_DMA_SLOT_SIG_MASK GENMASK(2, 0)
```

相关声明：[SILABS_DMA_SLOT_SIG_MASK](#a9ccf7fd9a6101b88a45feaf1170de7d5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a46d84aa830d58ab1e63133e3424361fb"></a>

```c
#define SILABS_LDMA_REQSEL_TO_SLOT(signal)
```

相关声明：[SILABS_LDMA_REQSEL_TO_SLOT](#a46d84aa830d58ab1e63133e3424361fb)、[signal](../api_file_reference/P391_____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考.md#a5d326f119f87d0facaa662520f8c322a)。

<a id="r_a8728e84cf05e093c864fe9dc8e9854c4"></a>

```c
#define SILABS_LDMA_SLOT_TO_REQSEL(slot)
```

相关声明：[SILABS_LDMA_SLOT_TO_REQSEL](#a8728e84cf05e093c864fe9dc8e9854c4)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.2\_函数（Functions）

<a id="r_a5f6501ec9e73cb8a3be76c418ebf1456"></a>

```c
int silabs_ldma_append_block (const struct device *dev, uint32_t channel, struct dma_config *config)
```

相关声明：[silabs_ldma_append_block](#a5f6501ec9e73cb8a3be76c418ebf1456)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[dma_config](../dma_reference/P004_DMA通道配置.md)。

向当前通道（channel）追加一个新块（block）。

## 12.3\_详细说明（Detailed Documentation）

<a id="a9ccf7fd9a6101b88a45feaf1170de7d5"></a>

### `SILABS_DMA_SLOT_SIG_MASK`

```c
#define SILABS_DMA_SLOT_SIG_MASK GENMASK(2, 0)
```

<a id="a8b234dbc8be91a1c9ae4b6478a3ba0e9"></a>

### `SILABS_DMA_SLOT_SOURCE_MASK`

```c
#define SILABS_DMA_SLOT_SOURCE_MASK GENMASK(7, 3)
```

<a id="a46d84aa830d58ab1e63133e3424361fb"></a>

### `SILABS_LDMA_REQSEL_TO_SLOT`

```c
#define SILABS_LDMA_REQSEL_TO_SLOT ( signal)
```

展开值（Value）：

```c
FIELD_PREP(SILABS_DMA_SLOT_SOURCE_MASK, FIELD_GET(SILABS_LDMA_SOURCE_MASK, signal)) | \
FIELD_PREP(SILABS_DMA_SLOT_SIG_MASK, FIELD_GET(SILABS_LDMA_SIG_MASK, signal))
```

<a id="a9559b6338f281c62c4cc28a37c6eaa1b"></a>

### `SILABS_LDMA_SIG_MASK`

```c
#define SILABS_LDMA_SIG_MASK GENMASK(3, 0)
```

<a id="a8728e84cf05e093c864fe9dc8e9854c4"></a>

### `SILABS_LDMA_SLOT_TO_REQSEL`

```c
#define SILABS_LDMA_SLOT_TO_REQSEL ( slot)
```

展开值（Value）：

```c
FIELD_PREP(SILABS_LDMA_SOURCE_MASK, FIELD_GET(SILABS_DMA_SLOT_SOURCE_MASK, slot)) | \
FIELD_PREP(SILABS_LDMA_SIG_MASK, FIELD_GET(SILABS_DMA_SLOT_SIG_MASK, slot))
```

<a id="a0d4985670c10482d3999d08e4ba1fdc9"></a>

### `SILABS_LDMA_SOURCE_MASK`

```c
#define SILABS_LDMA_SOURCE_MASK GENMASK(21, 16)
```

<a id="a5f6501ec9e73cb8a3be76c418ebf1456"></a>

### `silabs_ldma_append_block()`

```c
int silabs_ldma_append_block ( const struct device * dev, uint32_t channel, struct dma_config * config )
```

向当前通道（channel）追加一个新块（block）。

此函数允许向当前 DMA 传输追加一个块。用户或驱动程序可在传输进行期间注册下一次 DMA 传输，无须停止或重新启动 DMA 引擎。这非常适合 Zephyr UART API，因为用户会在 DMA 引擎运行期间提供缓冲区。此函数会动态改变指向 DMA 引擎下一次传输所加载块的链接，因此仅适用于尚未使用链接块列表（linked block list）的通道。

如果 DMA 引擎因上一次传输完成而自然停止，此函数会直接使用给定块重新启动 DMA 引擎。如果 DMA 引擎在重新配置下一次传输的过程中停止，也会重新启动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DMA 设备（device）。 |
| `channel` | 信道（Channel）。 |
| `config` | 通道配置，其中待追加的块作为 `head_block`。 |


## 12.4\_原页交叉引用（Cross References）

- [zephyr/drivers/dma.h](../dma_reference/P010_DMA驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P141_dma_silabs_ldma.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [signal](../api_file_reference/P391_____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考.md#a5d326f119f87d0facaa662520f8c322a)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [dma_config](../dma_reference/P004_DMA通道配置.md)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adma__silabs__ldma_8h_html_a0d4985670c10482d3999d08e4ba1fdc9"></a>
<a id="adma__silabs__ldma_8h_html_a8b234dbc8be91a1c9ae4b6478a3ba0e9"></a>
<a id="adma__silabs__ldma_8h_html_a9559b6338f281c62c4cc28a37c6eaa1b"></a>
<a id="adma__silabs__ldma_8h_html_a9ccf7fd9a6101b88a45feaf1170de7d5"></a>
<a id="asignal_8h_html_a5d326f119f87d0facaa662520f8c322a"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_zephyr__drivers__dma__dma_mcux_smartdma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__charger__npm10xx.h_文件参考.md)
