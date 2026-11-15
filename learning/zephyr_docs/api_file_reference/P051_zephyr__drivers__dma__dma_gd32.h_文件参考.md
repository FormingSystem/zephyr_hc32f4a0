---
id: learning.zephyr-docs.api-file-reference.page-51
title: zephyr__drivers__dma__dma_gd32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__gd32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_drivers\_\_dma\_\_dma\_gd32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__gd32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.1\_宏定义（Macros）

<a id="r_a0bfc50da9b666c382ca00e53612c08e8"></a>

```c
#define GD32_DMA_CONFIG_DIRECTION(config)
```

相关声明：[GD32_DMA_CONFIG_DIRECTION](#a0bfc50da9b666c382ca00e53612c08e8)。

<a id="r_a12c9387cd798e45a97a025d892fee048"></a>

```c
#define GD32_DMA_CONFIG_PERIPH_ADDR_INC(config)
```

相关声明：[GD32_DMA_CONFIG_PERIPH_ADDR_INC](#a12c9387cd798e45a97a025d892fee048)。

<a id="r_a6048bfaf2929f8ace82bfdf910a85224"></a>

```c
#define GD32_DMA_CONFIG_MEMORY_ADDR_INC(config)
```

相关声明：[GD32_DMA_CONFIG_MEMORY_ADDR_INC](#a6048bfaf2929f8ace82bfdf910a85224)。

<a id="r_ae09b2bd2a0abf46f92afbc93c8f0b1f2"></a>

```c
#define GD32_DMA_CONFIG_PERIPH_WIDTH(config)
```

相关声明：[GD32_DMA_CONFIG_PERIPH_WIDTH](#ae09b2bd2a0abf46f92afbc93c8f0b1f2)。

<a id="r_af6d346ff11af7445ef216ff86943de58"></a>

```c
#define GD32_DMA_CONFIG_MEMORY_WIDTH(config)
```

相关声明：[GD32_DMA_CONFIG_MEMORY_WIDTH](#af6d346ff11af7445ef216ff86943de58)。

<a id="r_a3c35875713e5534e753068e77c4a8796"></a>

```c
#define GD32_DMA_CONFIG_PERIPHERAL_INC_FIXED(config)
```

相关声明：[GD32_DMA_CONFIG_PERIPHERAL_INC_FIXED](#a3c35875713e5534e753068e77c4a8796)。

<a id="r_acfb3e4c8ef6bed1484348f72be5a2fb9"></a>

```c
#define GD32_DMA_CONFIG_PRIORITY(config)
```

相关声明：[GD32_DMA_CONFIG_PRIORITY](#acfb3e4c8ef6bed1484348f72be5a2fb9)。

<a id="r_af41c61ae669ce510d514ccb9ff6204f9"></a>

```c
#define GD32_DMA_FEATURES_FIFO_THRESHOLD(threshold)
```

相关声明：[GD32_DMA_FEATURES_FIFO_THRESHOLD](#af41c61ae669ce510d514ccb9ff6204f9)。

## 51.2\_详细说明（Detailed Documentation）

<a id="a0bfc50da9b666c382ca00e53612c08e8"></a>

### `GD32_DMA_CONFIG_DIRECTION`

```c
#define GD32_DMA_CONFIG_DIRECTION ( config)
```

展开值（Value）：

```c
((config >> 6) & 0x3)
```

<a id="a6048bfaf2929f8ace82bfdf910a85224"></a>

### `GD32_DMA_CONFIG_MEMORY_ADDR_INC`

```c
#define GD32_DMA_CONFIG_MEMORY_ADDR_INC ( config)
```

展开值（Value）：

```c
((config >> 10) & 0x1)
```

<a id="af6d346ff11af7445ef216ff86943de58"></a>

### `GD32_DMA_CONFIG_MEMORY_WIDTH`

```c
#define GD32_DMA_CONFIG_MEMORY_WIDTH ( config)
```

展开值（Value）：

```c
((config >> 13) & 0x3)
```

<a id="a12c9387cd798e45a97a025d892fee048"></a>

### `GD32_DMA_CONFIG_PERIPH_ADDR_INC`

```c
#define GD32_DMA_CONFIG_PERIPH_ADDR_INC ( config)
```

展开值（Value）：

```c
((config >> 9) & 0x1)
```

<a id="ae09b2bd2a0abf46f92afbc93c8f0b1f2"></a>

### `GD32_DMA_CONFIG_PERIPH_WIDTH`

```c
#define GD32_DMA_CONFIG_PERIPH_WIDTH ( config)
```

展开值（Value）：

```c
((config >> 11) & 0x3)
```

<a id="a3c35875713e5534e753068e77c4a8796"></a>

### `GD32_DMA_CONFIG_PERIPHERAL_INC_FIXED`

```c
#define GD32_DMA_CONFIG_PERIPHERAL_INC_FIXED ( config)
```

展开值（Value）：

```c
((config >> 15) & 0x1)
```

<a id="acfb3e4c8ef6bed1484348f72be5a2fb9"></a>

### `GD32_DMA_CONFIG_PRIORITY`

```c
#define GD32_DMA_CONFIG_PRIORITY ( config)
```

展开值（Value）：

```c
((config >> 16) & 0x3)
```

<a id="af41c61ae669ce510d514ccb9ff6204f9"></a>

### `GD32_DMA_FEATURES_FIFO_THRESHOLD`

```c
#define GD32_DMA_FEATURES_FIFO_THRESHOLD ( threshold)
```

展开值（Value）：

```c
(threshold & 0x3)
```


## 51.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P138_dma_gd32.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P050_zephyr__bluetooth__services__dis.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__drivers__dma__dma_intel_lpss.h_文件参考.md)
