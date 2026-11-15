---
id: learning.zephyr-docs.api-file-reference.page-117
title: zephyr__dt-bindings__dma__gd32_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_zephyr\_\_dt-bindings\_\_dma\_\_gd32\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 117.1\_宏定义（Macros）

<a id="r_ae2a0d7ee983ce7229d00424fc9bd561a"></a>

```c
#define GD32_DMA_CH_CFG_DIRECTION(val)
```

相关声明：[GD32_DMA_CH_CFG_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)。

<a id="r_ac66caaa6fd58e811ca1173afffb6eee0"></a>

```c
#define GD32_DMA_MEMORY_TO_MEMORY GD32_DMA_CH_CFG_DIRECTION(0)
```

相关声明：[GD32_DMA_MEMORY_TO_MEMORY](#ac66caaa6fd58e811ca1173afffb6eee0)、[GD32_DMA_CH_CFG_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)。

<a id="r_a133ee2eba1696a8a88e553899b42215d"></a>

```c
#define GD32_DMA_MEMORY_TO_PERIPH GD32_DMA_CH_CFG_DIRECTION(1)
```

相关声明：[GD32_DMA_MEMORY_TO_PERIPH](#a133ee2eba1696a8a88e553899b42215d)、[GD32_DMA_CH_CFG_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)。

<a id="r_a6db732bda87b175e5594e47120b50fc4"></a>

```c
#define GD32_DMA_PERIPH_TO_MEMORY GD32_DMA_CH_CFG_DIRECTION(2)
```

相关声明：[GD32_DMA_PERIPH_TO_MEMORY](#a6db732bda87b175e5594e47120b50fc4)、[GD32_DMA_CH_CFG_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)。

<a id="r_ad0abcd3eb77751438884eb14376a4249"></a>

```c
#define GD32_DMA_CH_CFG_PERIPH_ADDR_INC(val)
```

相关声明：[GD32_DMA_CH_CFG_PERIPH_ADDR_INC](#ad0abcd3eb77751438884eb14376a4249)。

<a id="r_a3190a823bcefea6dea75b22751437469"></a>

```c
#define GD32_DMA_NO_PERIPH_ADDR_INC GD32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
```

相关声明：[GD32_DMA_NO_PERIPH_ADDR_INC](#a3190a823bcefea6dea75b22751437469)、[GD32_DMA_CH_CFG_PERIPH_ADDR_INC](#ad0abcd3eb77751438884eb14376a4249)。

<a id="r_a886f483d28ecb076d76cab9807dbd9ae"></a>

```c
#define GD32_DMA_PERIPH_ADDR_INC GD32_DMA_CH_CFG_PERIPH_ADDR_INC(1)
```

相关声明：[GD32_DMA_PERIPH_ADDR_INC](#a886f483d28ecb076d76cab9807dbd9ae)、[GD32_DMA_CH_CFG_PERIPH_ADDR_INC](#ad0abcd3eb77751438884eb14376a4249)。

<a id="r_ae55d797279e2483a9de15ddb250d9c01"></a>

```c
#define GD32_DMA_CH_CFG_MEMORY_ADDR_INC(val)
```

相关声明：[GD32_DMA_CH_CFG_MEMORY_ADDR_INC](#ae55d797279e2483a9de15ddb250d9c01)。

<a id="r_a45eb42e1d19daa3d40831c93ad0ba0a0"></a>

```c
#define GD32_DMA_NO_MEMORY_ADDR_INC GD32_DMA_CH_CFG_MEMORY_ADDR_INC(0)
```

相关声明：[GD32_DMA_NO_MEMORY_ADDR_INC](#a45eb42e1d19daa3d40831c93ad0ba0a0)、[GD32_DMA_CH_CFG_MEMORY_ADDR_INC](#ae55d797279e2483a9de15ddb250d9c01)。

<a id="r_a1dfa4abe03789cb06229e071479a68d3"></a>

```c
#define GD32_DMA_MEMORY_ADDR_INC GD32_DMA_CH_CFG_MEMORY_ADDR_INC(1)
```

相关声明：[GD32_DMA_MEMORY_ADDR_INC](#a1dfa4abe03789cb06229e071479a68d3)、[GD32_DMA_CH_CFG_MEMORY_ADDR_INC](#ae55d797279e2483a9de15ddb250d9c01)。

<a id="r_a7ee975a1a1338f3fcbf9779a4f66ec7c"></a>

```c
#define GD32_DMA_CH_CFG_PERIPH_WIDTH(val)
```

相关声明：[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_a43f8444f017382621385497e88bc28eb"></a>

```c
#define GD32_DMA_PERIPH_WIDTH_8BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

相关声明：[GD32_DMA_PERIPH_WIDTH_8BIT](#a43f8444f017382621385497e88bc28eb)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_acd17760bf971b4efae57cbb7413c7993"></a>

```c
#define GD32_DMA_PERIPH_WIDTH_16BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

相关声明：[GD32_DMA_PERIPH_WIDTH_16BIT](#acd17760bf971b4efae57cbb7413c7993)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_ac8071edf3e9c36beb96f8a2f41f9b297"></a>

```c
#define GD32_DMA_PERIPH_WIDTH_32BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

相关声明：[GD32_DMA_PERIPH_WIDTH_32BIT](#ac8071edf3e9c36beb96f8a2f41f9b297)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_a7e46c2dd560ad05b3ef2d49e8e934634"></a>

```c
#define GD32_DMA_CH_CFG_MEMORY_WIDTH(val)
```

相关声明：[GD32_DMA_CH_CFG_MEMORY_WIDTH](#a7e46c2dd560ad05b3ef2d49e8e934634)。

<a id="r_aa02a7efc2fca50aa800f39e94b3759b4"></a>

```c
#define GD32_DMA_MEMORY_WIDTH_8BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

相关声明：[GD32_DMA_MEMORY_WIDTH_8BIT](#aa02a7efc2fca50aa800f39e94b3759b4)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_a0787852dc6f450f4eff8eea7be3a6b89"></a>

```c
#define GD32_DMA_MEMORY_WIDTH_16BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

相关声明：[GD32_DMA_MEMORY_WIDTH_16BIT](#a0787852dc6f450f4eff8eea7be3a6b89)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_a2d77c7ecc44a7c91dfecbf94044ec5a0"></a>

```c
#define GD32_DMA_MEMORY_WIDTH_32BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

相关声明：[GD32_DMA_MEMORY_WIDTH_32BIT](#a2d77c7ecc44a7c91dfecbf94044ec5a0)、[GD32_DMA_CH_CFG_PERIPH_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)。

<a id="r_a0eecb55bada0630383167b56d82c4892"></a>

```c
#define GD32_DMA_CH_CFG_PERIPH_INC_FIXED(val)
```

相关声明：[GD32_DMA_CH_CFG_PERIPH_INC_FIXED](#a0eecb55bada0630383167b56d82c4892)。

<a id="r_a7a95cc521b5445314d9d64528d885724"></a>

```c
#define GD32_DMA_CH_CFG_PRIORITY(val)
```

相关声明：[GD32_DMA_CH_CFG_PRIORITY](#a7a95cc521b5445314d9d64528d885724)。

<a id="r_ae68917539c8744ddcfbad918e69db56e"></a>

```c
#define GD32_DMA_PRIORITY_LOW GD32_DMA_CH_CFG_PRIORITY(0)
```

相关声明：[GD32_DMA_PRIORITY_LOW](#ae68917539c8744ddcfbad918e69db56e)、[GD32_DMA_CH_CFG_PRIORITY](#a7a95cc521b5445314d9d64528d885724)。

<a id="r_a548fac07f1b1c5cdd61670178c7ecc8b"></a>

```c
#define GD32_DMA_PRIORITY_MEDIUM GD32_DMA_CH_CFG_PRIORITY(1)
```

相关声明：[GD32_DMA_PRIORITY_MEDIUM](#a548fac07f1b1c5cdd61670178c7ecc8b)、[GD32_DMA_CH_CFG_PRIORITY](#a7a95cc521b5445314d9d64528d885724)。

<a id="r_a17a02cccc8980fd5a273f251b4e02ea6"></a>

```c
#define GD32_DMA_PRIORITY_HIGH GD32_DMA_CH_CFG_PRIORITY(2)
```

相关声明：[GD32_DMA_PRIORITY_HIGH](#a17a02cccc8980fd5a273f251b4e02ea6)、[GD32_DMA_CH_CFG_PRIORITY](#a7a95cc521b5445314d9d64528d885724)。

<a id="r_ad6e846a9a5b52f0838c1b214ba39b6b3"></a>

```c
#define GD32_DMA_PRIORITY_VERY_HIGH GD32_DMA_CH_CFG_PRIORITY(3)
```

相关声明：[GD32_DMA_PRIORITY_VERY_HIGH](#ad6e846a9a5b52f0838c1b214ba39b6b3)、[GD32_DMA_CH_CFG_PRIORITY](#a7a95cc521b5445314d9d64528d885724)。

## 117.2\_详细说明（Detailed Documentation）

<a id="ae2a0d7ee983ce7229d00424fc9bd561a"></a>

### `GD32_DMA_CH_CFG_DIRECTION`

```c
#define GD32_DMA_CH_CFG_DIRECTION ( val)
```

展开值（Value）：

```c
((val & 0x3) << 6)
```

<a id="ae55d797279e2483a9de15ddb250d9c01"></a>

### `GD32_DMA_CH_CFG_MEMORY_ADDR_INC`

```c
#define GD32_DMA_CH_CFG_MEMORY_ADDR_INC ( val)
```

展开值（Value）：

```c
((val & 0x1) << 10)
```

<a id="a7e46c2dd560ad05b3ef2d49e8e934634"></a>

### `GD32_DMA_CH_CFG_MEMORY_WIDTH`

```c
#define GD32_DMA_CH_CFG_MEMORY_WIDTH ( val)
```

展开值（Value）：

```c
((val & 0x3) << 13)
```

<a id="ad0abcd3eb77751438884eb14376a4249"></a>

### `GD32_DMA_CH_CFG_PERIPH_ADDR_INC`

```c
#define GD32_DMA_CH_CFG_PERIPH_ADDR_INC ( val)
```

展开值（Value）：

```c
((val & 0x1) << 9)
```

<a id="a0eecb55bada0630383167b56d82c4892"></a>

### `GD32_DMA_CH_CFG_PERIPH_INC_FIXED`

```c
#define GD32_DMA_CH_CFG_PERIPH_INC_FIXED ( val)
```

展开值（Value）：

```c
((val & 0x1) << 15)
```

<a id="a7ee975a1a1338f3fcbf9779a4f66ec7c"></a>

### `GD32_DMA_CH_CFG_PERIPH_WIDTH`

```c
#define GD32_DMA_CH_CFG_PERIPH_WIDTH ( val)
```

展开值（Value）：

```c
((val & 0x3) << 11)
```

<a id="a7a95cc521b5445314d9d64528d885724"></a>

### `GD32_DMA_CH_CFG_PRIORITY`

```c
#define GD32_DMA_CH_CFG_PRIORITY ( val)
```

展开值（Value）：

```c
((val & 0x3) << 16)
```

<a id="a1dfa4abe03789cb06229e071479a68d3"></a>

### `GD32_DMA_MEMORY_ADDR_INC`

```c
#define GD32_DMA_MEMORY_ADDR_INC GD32_DMA_CH_CFG_MEMORY_ADDR_INC(1)
```

<a id="ac66caaa6fd58e811ca1173afffb6eee0"></a>

### `GD32_DMA_MEMORY_TO_MEMORY`

```c
#define GD32_DMA_MEMORY_TO_MEMORY GD32_DMA_CH_CFG_DIRECTION(0)
```

<a id="a133ee2eba1696a8a88e553899b42215d"></a>

### `GD32_DMA_MEMORY_TO_PERIPH`

```c
#define GD32_DMA_MEMORY_TO_PERIPH GD32_DMA_CH_CFG_DIRECTION(1)
```

<a id="a0787852dc6f450f4eff8eea7be3a6b89"></a>

### `GD32_DMA_MEMORY_WIDTH_16BIT`

```c
#define GD32_DMA_MEMORY_WIDTH_16BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

<a id="a2d77c7ecc44a7c91dfecbf94044ec5a0"></a>

### `GD32_DMA_MEMORY_WIDTH_32BIT`

```c
#define GD32_DMA_MEMORY_WIDTH_32BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

<a id="aa02a7efc2fca50aa800f39e94b3759b4"></a>

### `GD32_DMA_MEMORY_WIDTH_8BIT`

```c
#define GD32_DMA_MEMORY_WIDTH_8BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

<a id="a45eb42e1d19daa3d40831c93ad0ba0a0"></a>

### `GD32_DMA_NO_MEMORY_ADDR_INC`

```c
#define GD32_DMA_NO_MEMORY_ADDR_INC GD32_DMA_CH_CFG_MEMORY_ADDR_INC(0)
```

<a id="a3190a823bcefea6dea75b22751437469"></a>

### `GD32_DMA_NO_PERIPH_ADDR_INC`

```c
#define GD32_DMA_NO_PERIPH_ADDR_INC GD32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
```

<a id="a886f483d28ecb076d76cab9807dbd9ae"></a>

### `GD32_DMA_PERIPH_ADDR_INC`

```c
#define GD32_DMA_PERIPH_ADDR_INC GD32_DMA_CH_CFG_PERIPH_ADDR_INC(1)
```

<a id="a6db732bda87b175e5594e47120b50fc4"></a>

### `GD32_DMA_PERIPH_TO_MEMORY`

```c
#define GD32_DMA_PERIPH_TO_MEMORY GD32_DMA_CH_CFG_DIRECTION(2)
```

<a id="acd17760bf971b4efae57cbb7413c7993"></a>

### `GD32_DMA_PERIPH_WIDTH_16BIT`

```c
#define GD32_DMA_PERIPH_WIDTH_16BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

<a id="ac8071edf3e9c36beb96f8a2f41f9b297"></a>

### `GD32_DMA_PERIPH_WIDTH_32BIT`

```c
#define GD32_DMA_PERIPH_WIDTH_32BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

<a id="a43f8444f017382621385497e88bc28eb"></a>

### `GD32_DMA_PERIPH_WIDTH_8BIT`

```c
#define GD32_DMA_PERIPH_WIDTH_8BIT GD32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

<a id="a17a02cccc8980fd5a273f251b4e02ea6"></a>

### `GD32_DMA_PRIORITY_HIGH`

```c
#define GD32_DMA_PRIORITY_HIGH GD32_DMA_CH_CFG_PRIORITY(2)
```

<a id="ae68917539c8744ddcfbad918e69db56e"></a>

### `GD32_DMA_PRIORITY_LOW`

```c
#define GD32_DMA_PRIORITY_LOW GD32_DMA_CH_CFG_PRIORITY(0)
```

<a id="a548fac07f1b1c5cdd61670178c7ecc8b"></a>

### `GD32_DMA_PRIORITY_MEDIUM`

```c
#define GD32_DMA_PRIORITY_MEDIUM GD32_DMA_CH_CFG_PRIORITY(1)
```

<a id="ad6e846a9a5b52f0838c1b214ba39b6b3"></a>

### `GD32_DMA_PRIORITY_VERY_HIGH`

```c
#define GD32_DMA_PRIORITY_VERY_HIGH GD32_DMA_CH_CFG_PRIORITY(3)
```


## 117.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/gd32__dma_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P116_zephyr__dt-bindings__reset__gd32-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P118_zephyr__dt-bindings__clock__gd32a50x-clocks.h_文件参考.md)
