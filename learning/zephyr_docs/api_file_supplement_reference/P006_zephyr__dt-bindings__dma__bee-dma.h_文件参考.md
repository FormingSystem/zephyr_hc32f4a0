---
id: learning.zephyr-docs.api-file-supplement-reference.page-6
title: zephyr__dt-bindings__dma__bee-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_dma\_\_bee-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Bee DMA的设备树绑定（Devicetree Bindings）。

查看此文件的源码。

<a id="details"></a>

Realtek Bee DMA 设备树绑定（Devicetree Bindings）。这里定义所有 Bee 系列片上系统（SoCs）共用的 `config` 单元字段（Cell Fields）。各 SoC 的握手槽位标识（Handshake / Slot IDs）位于对应芯片的头文件中，例如 `<dt-bindings/dma/rtl87x2g-dma.h>` 或 `<dt-bindings/dma/rtl8752h-dma.h>`；这些头文件均包含本文件。`config` 是 `dmas` 条目的第三个单元，内容为 32 位掩码（Mask）。请使用下面的具名宏（Named Macros）组合它，不要直接填写数值：

```c
#include <dt-bindings/dma/rtl87x2g-dma.h>

&uart2 {
        status = "okay";
        dmas = <&dma0 2 BEE_DMA_HANDSHAKE_UART2_RX
                (BEE_DMA_P2M | BEE_DMA_SRC_FIXED | BEE_DMA_DST_INC |
                 BEE_DMA_SRC_WIDTH_8BIT | BEE_DMA_DST_WIDTH_8BIT |
                 BEE_DMA_SRC_MSIZE(BEE_DMA_MSIZE_1) |
                 BEE_DMA_DST_MSIZE(BEE_DMA_MSIZE_1) | BEE_DMA_PRIORITY(0))>,
               <&dma0 3 BEE_DMA_HANDSHAKE_UART2_TX
                (BEE_DMA_M2P | BEE_DMA_SRC_INC | BEE_DMA_DST_FIXED |
                 BEE_DMA_SRC_WIDTH_8BIT | BEE_DMA_DST_WIDTH_8BIT |
                 BEE_DMA_SRC_MSIZE(BEE_DMA_MSIZE_1) |
                 BEE_DMA_DST_MSIZE(BEE_DMA_MSIZE_1) | BEE_DMA_PRIORITY(1))>;
        dma-names = "rx", "tx";
};
```

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_a5df5e7035e59837c1ec40ed90bb58e4d"></a>

```c
#define BEE_DMA_M2M 0
```

相关声明：[BEE_DMA_M2M](#a5df5e7035e59837c1ec40ed90bb58e4d)。

<a id="r_add438bcd123b1f5a5abe2b50d098f187"></a>

```c
#define BEE_DMA_M2P 1
```

相关声明：[BEE_DMA_M2P](#add438bcd123b1f5a5abe2b50d098f187)。

<a id="r_a78f2b31a1e086c54cf29ace78bcf0923"></a>

```c
#define BEE_DMA_P2M 2
```

相关声明：[BEE_DMA_P2M](#a78f2b31a1e086c54cf29ace78bcf0923)。

<a id="r_a7e01a19cc3472b5997450d7718fa32b5"></a>

```c
#define BEE_DMA_SRC_INC (0 << 2)
```

相关声明：[BEE_DMA_SRC_INC](#a7e01a19cc3472b5997450d7718fa32b5)。

<a id="r_a3c882058dc27a656c6aa0c5e5cee36f9"></a>

```c
#define BEE_DMA_SRC_DEC (1 << 2)
```

相关声明：[BEE_DMA_SRC_DEC](#a3c882058dc27a656c6aa0c5e5cee36f9)。

<a id="r_adfd6fa001e26f9677a5dad353056f08e"></a>

```c
#define BEE_DMA_SRC_FIXED (2 << 2)
```

相关声明：[BEE_DMA_SRC_FIXED](#adfd6fa001e26f9677a5dad353056f08e)。

<a id="r_a64654038e30e09fdebc69a356275f2f9"></a>

```c
#define BEE_DMA_DST_INC (0 << 4)
```

相关声明：[BEE_DMA_DST_INC](#a64654038e30e09fdebc69a356275f2f9)。

<a id="r_a84181fc068c2a1cd158262d308b358db"></a>

```c
#define BEE_DMA_DST_DEC (1 << 4)
```

相关声明：[BEE_DMA_DST_DEC](#a84181fc068c2a1cd158262d308b358db)。

<a id="r_a473ce92eab1752fee11c2a8fae9d05ea"></a>

```c
#define BEE_DMA_DST_FIXED (2 << 4)
```

相关声明：[BEE_DMA_DST_FIXED](#a473ce92eab1752fee11c2a8fae9d05ea)。

<a id="r_a8e108ff59e3fcd06b17b216bee577f01"></a>

```c
#define BEE_DMA_SRC_WIDTH_8BIT (0 << 6)
```

相关声明：[BEE_DMA_SRC_WIDTH_8BIT](#a8e108ff59e3fcd06b17b216bee577f01)。

<a id="r_ad6f21d4321280b9a5ffa6e7c78b3d39b"></a>

```c
#define BEE_DMA_SRC_WIDTH_16BIT (1 << 6)
```

相关声明：[BEE_DMA_SRC_WIDTH_16BIT](#ad6f21d4321280b9a5ffa6e7c78b3d39b)。

<a id="r_ae9c26fc6f3d9cc1b3717d6ecaf87d2c3"></a>

```c
#define BEE_DMA_SRC_WIDTH_32BIT (2 << 6)
```

相关声明：[BEE_DMA_SRC_WIDTH_32BIT](#ae9c26fc6f3d9cc1b3717d6ecaf87d2c3)。

<a id="r_afdd6959b828c83f814460416df55a360"></a>

```c
#define BEE_DMA_DST_WIDTH_8BIT (0 << 8)
```

相关声明：[BEE_DMA_DST_WIDTH_8BIT](#afdd6959b828c83f814460416df55a360)。

<a id="r_afde9215078b6b44ee1ce4ee596836f9e"></a>

```c
#define BEE_DMA_DST_WIDTH_16BIT (1 << 8)
```

相关声明：[BEE_DMA_DST_WIDTH_16BIT](#afde9215078b6b44ee1ce4ee596836f9e)。

<a id="r_aeb53c6f5c592c4eb3bc1e56541cde109"></a>

```c
#define BEE_DMA_DST_WIDTH_32BIT (2 << 8)
```

相关声明：[BEE_DMA_DST_WIDTH_32BIT](#aeb53c6f5c592c4eb3bc1e56541cde109)。

<a id="r_a747c9c93a7f649eb42c96f2e553f4431"></a>

```c
#define BEE_DMA_SRC_MSIZE(n)
```

相关声明：[BEE_DMA_SRC_MSIZE](#a747c9c93a7f649eb42c96f2e553f4431)。

<a id="r_a1274895459b11d812d728884c3c9c2c4"></a>

```c
#define BEE_DMA_DST_MSIZE(n)
```

相关声明：[BEE_DMA_DST_MSIZE](#a1274895459b11d812d728884c3c9c2c4)。

<a id="r_a16e79a1c022ef96a72e5a45335841f77"></a>

```c
#define BEE_DMA_MSIZE_1 0
```

相关声明：[BEE_DMA_MSIZE_1](#a16e79a1c022ef96a72e5a45335841f77)。

<a id="r_a5ac8ac942324a306dafc8af81aeb9fa9"></a>

```c
#define BEE_DMA_MSIZE_4 1
```

相关声明：[BEE_DMA_MSIZE_4](#a5ac8ac942324a306dafc8af81aeb9fa9)。

<a id="r_a06cd7e8a02a926d48b8b7a32824d6a30"></a>

```c
#define BEE_DMA_MSIZE_8 2
```

相关声明：[BEE_DMA_MSIZE_8](#a06cd7e8a02a926d48b8b7a32824d6a30)。

<a id="r_a8917db65fa2c12f889becc84fa0a26c8"></a>

```c
#define BEE_DMA_MSIZE_16 3
```

相关声明：[BEE_DMA_MSIZE_16](#a8917db65fa2c12f889becc84fa0a26c8)。

<a id="r_aa7c0dec9c01e76ea2492c108a7cadd63"></a>

```c
#define BEE_DMA_MSIZE_32 4
```

相关声明：[BEE_DMA_MSIZE_32](#aa7c0dec9c01e76ea2492c108a7cadd63)。

<a id="r_a2ad8c6e770a349b6527ea7f27f647edf"></a>

```c
#define BEE_DMA_MSIZE_64 5
```

相关声明：[BEE_DMA_MSIZE_64](#a2ad8c6e770a349b6527ea7f27f647edf)。

<a id="r_af60fbdb7836b2ba5c12615abf74185b5"></a>

```c
#define BEE_DMA_MSIZE_128 6
```

相关声明：[BEE_DMA_MSIZE_128](#af60fbdb7836b2ba5c12615abf74185b5)。

<a id="r_ab7daa6fd2a8d64ff2b2387ec63324899"></a>

```c
#define BEE_DMA_MSIZE_256 7
```

相关声明：[BEE_DMA_MSIZE_256](#ab7daa6fd2a8d64ff2b2387ec63324899)。

<a id="r_ad3bb860dd66f7f2b036a39790c1d1c80"></a>

```c
#define BEE_DMA_PRIORITY(n)
```

相关声明：[BEE_DMA_PRIORITY](#ad3bb860dd66f7f2b036a39790c1d1c80)。

## 6.2\_详细说明（Detailed Documentation）

<a id="a84181fc068c2a1cd158262d308b358db"></a>

### `BEE_DMA_DST_DEC`

```c
#define BEE_DMA_DST_DEC (1 << 4)
```

<a id="a473ce92eab1752fee11c2a8fae9d05ea"></a>

### `BEE_DMA_DST_FIXED`

```c
#define BEE_DMA_DST_FIXED (2 << 4)
```

<a id="a64654038e30e09fdebc69a356275f2f9"></a>

### `BEE_DMA_DST_INC`

```c
#define BEE_DMA_DST_INC (0 << 4)
```

<a id="a1274895459b11d812d728884c3c9c2c4"></a>

### `BEE_DMA_DST_MSIZE`

```c
#define BEE_DMA_DST_MSIZE ( n)
```

展开值（Value）：

```c
((n) << 13)
```

<a id="afde9215078b6b44ee1ce4ee596836f9e"></a>

### `BEE_DMA_DST_WIDTH_16BIT`

```c
#define BEE_DMA_DST_WIDTH_16BIT (1 << 8)
```

<a id="aeb53c6f5c592c4eb3bc1e56541cde109"></a>

### `BEE_DMA_DST_WIDTH_32BIT`

```c
#define BEE_DMA_DST_WIDTH_32BIT (2 << 8)
```

<a id="afdd6959b828c83f814460416df55a360"></a>

### `BEE_DMA_DST_WIDTH_8BIT`

```c
#define BEE_DMA_DST_WIDTH_8BIT (0 << 8)
```

<a id="a5df5e7035e59837c1ec40ed90bb58e4d"></a>

### `BEE_DMA_M2M`

```c
#define BEE_DMA_M2M 0
```

<a id="add438bcd123b1f5a5abe2b50d098f187"></a>

### `BEE_DMA_M2P`

```c
#define BEE_DMA_M2P 1
```

<a id="a16e79a1c022ef96a72e5a45335841f77"></a>

### `BEE_DMA_MSIZE_1`

```c
#define BEE_DMA_MSIZE_1 0
```

<a id="af60fbdb7836b2ba5c12615abf74185b5"></a>

### `BEE_DMA_MSIZE_128`

```c
#define BEE_DMA_MSIZE_128 6
```

<a id="a8917db65fa2c12f889becc84fa0a26c8"></a>

### `BEE_DMA_MSIZE_16`

```c
#define BEE_DMA_MSIZE_16 3
```

<a id="ab7daa6fd2a8d64ff2b2387ec63324899"></a>

### `BEE_DMA_MSIZE_256`

```c
#define BEE_DMA_MSIZE_256 7
```

<a id="aa7c0dec9c01e76ea2492c108a7cadd63"></a>

### `BEE_DMA_MSIZE_32`

```c
#define BEE_DMA_MSIZE_32 4
```

<a id="a5ac8ac942324a306dafc8af81aeb9fa9"></a>

### `BEE_DMA_MSIZE_4`

```c
#define BEE_DMA_MSIZE_4 1
```

<a id="a2ad8c6e770a349b6527ea7f27f647edf"></a>

### `BEE_DMA_MSIZE_64`

```c
#define BEE_DMA_MSIZE_64 5
```

<a id="a06cd7e8a02a926d48b8b7a32824d6a30"></a>

### `BEE_DMA_MSIZE_8`

```c
#define BEE_DMA_MSIZE_8 2
```

<a id="a78f2b31a1e086c54cf29ace78bcf0923"></a>

### `BEE_DMA_P2M`

```c
#define BEE_DMA_P2M 2
```

<a id="ad3bb860dd66f7f2b036a39790c1d1c80"></a>

### `BEE_DMA_PRIORITY`

```c
#define BEE_DMA_PRIORITY ( n)
```

展开值（Value）：

```c
((n) << 16)
```

<a id="a3c882058dc27a656c6aa0c5e5cee36f9"></a>

### `BEE_DMA_SRC_DEC`

```c
#define BEE_DMA_SRC_DEC (1 << 2)
```

<a id="adfd6fa001e26f9677a5dad353056f08e"></a>

### `BEE_DMA_SRC_FIXED`

```c
#define BEE_DMA_SRC_FIXED (2 << 2)
```

<a id="a7e01a19cc3472b5997450d7718fa32b5"></a>

### `BEE_DMA_SRC_INC`

```c
#define BEE_DMA_SRC_INC (0 << 2)
```

<a id="a747c9c93a7f649eb42c96f2e553f4431"></a>

### `BEE_DMA_SRC_MSIZE`

```c
#define BEE_DMA_SRC_MSIZE ( n)
```

展开值（Value）：

```c
((n) << 10)
```

<a id="ad6f21d4321280b9a5ffa6e7c78b3d39b"></a>

### `BEE_DMA_SRC_WIDTH_16BIT`

```c
#define BEE_DMA_SRC_WIDTH_16BIT (1 << 6)
```

<a id="ae9c26fc6f3d9cc1b3717d6ecaf87d2c3"></a>

### `BEE_DMA_SRC_WIDTH_32BIT`

```c
#define BEE_DMA_SRC_WIDTH_32BIT (2 << 6)
```

<a id="a8e108ff59e3fcd06b17b216bee577f01"></a>

### `BEE_DMA_SRC_WIDTH_8BIT`

```c
#define BEE_DMA_SRC_WIDTH_8BIT (0 << 6)
```


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/bee-dma_8h_source.html)
- [dt-bindings/dma/rtl87x2g-dma.h](P102_zephyr__dt-bindings__dma__rtl87x2g-dma.h_文件参考.md)
- [dt-bindings/dma/rtl8752h-dma.h](P101_zephyr__dt-bindings__dma__rtl8752h-dma.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__dt-bindings__interrupt-controller__bcm2835-armctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__clock_control__bee_clock_control.h_文件参考.md)
