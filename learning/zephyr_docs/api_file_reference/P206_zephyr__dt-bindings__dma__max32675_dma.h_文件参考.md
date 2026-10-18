---
id: learning.zephyr-docs.api-file-reference.page-206
title: zephyr__dt-bindings__dma__max32675_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max32675__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第206章\_zephyr\_\_dt-bindings\_\_dma\_\_max32675\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max32675__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 206.1\_宏定义（Macros）

<a id="r_a6e1ea6d5650545947928c83c71776c04"></a>

```c
#define MAX32_DMA_SLOT_MEMTOMEM 0x00U
```

相关声明：[MAX32_DMA_SLOT_MEMTOMEM](#a6e1ea6d5650545947928c83c71776c04)。

<a id="r_ac505ee888a8cb52b03ac733a9b650097"></a>

```c
#define MAX32_DMA_SLOT_SPI0_RX 0x01U
```

相关声明：[MAX32_DMA_SLOT_SPI0_RX](#ac505ee888a8cb52b03ac733a9b650097)。

<a id="r_a0df8d71978ba7b5c5b6766c1cf28d00c"></a>

```c
#define MAX32_DMA_SLOT_SPI1_RX 0x02U
```

相关声明：[MAX32_DMA_SLOT_SPI1_RX](#a0df8d71978ba7b5c5b6766c1cf28d00c)。

<a id="r_ac823471b99eda7df54c2fce6eb923e96"></a>

```c
#define MAX32_DMA_SLOT_UART0_RX 0x04U
```

相关声明：[MAX32_DMA_SLOT_UART0_RX](#ac823471b99eda7df54c2fce6eb923e96)。

<a id="r_a207563fbc9fb4110d78f92b1d2d4c423"></a>

```c
#define MAX32_DMA_SLOT_I2C0_RX 0x07U
```

相关声明：[MAX32_DMA_SLOT_I2C0_RX](#a207563fbc9fb4110d78f92b1d2d4c423)。

<a id="r_a640bd0651d35157bdd822b11e8b23274"></a>

```c
#define MAX32_DMA_SLOT_I2C2_RX 0x0AU
```

相关声明：[MAX32_DMA_SLOT_I2C2_RX](#a640bd0651d35157bdd822b11e8b23274)。

<a id="r_ac82aa4f9ad49e656963580bf297dcd26"></a>

```c
#define MAX32_DMA_SLOT_UART2_RX 0x0EU
```

相关声明：[MAX32_DMA_SLOT_UART2_RX](#ac82aa4f9ad49e656963580bf297dcd26)。

<a id="r_a8244219f3dae7ceb188a3112ca041455"></a>

```c
#define MAX32_DMA_SLOT_AES_RX 0x10U
```

相关声明：[MAX32_DMA_SLOT_AES_RX](#a8244219f3dae7ceb188a3112ca041455)。

<a id="r_a56646e3053fc8a76ef214adbd0ba5921"></a>

```c
#define MAX32_DMA_SLOT_I2S_RX 0x1EU
```

相关声明：[MAX32_DMA_SLOT_I2S_RX](#a56646e3053fc8a76ef214adbd0ba5921)。

<a id="r_a26f06363fd4639eaee5668450adaa1c3"></a>

```c
#define MAX32_DMA_SLOT_SPI0_TX 0x21U
```

相关声明：[MAX32_DMA_SLOT_SPI0_TX](#a26f06363fd4639eaee5668450adaa1c3)。

<a id="r_aa85105348eeb191fd2799d645aacc575"></a>

```c
#define MAX32_DMA_SLOT_SPI1_TX 0x22U
```

相关声明：[MAX32_DMA_SLOT_SPI1_TX](#aa85105348eeb191fd2799d645aacc575)。

<a id="r_a009a7e71c5fed2afa3d8907411c454e3"></a>

```c
#define MAX32_DMA_SLOT_UART0_TX 0x24U
```

相关声明：[MAX32_DMA_SLOT_UART0_TX](#a009a7e71c5fed2afa3d8907411c454e3)。

<a id="r_aee43cae318d6b70f9f2a7e6bd77e02dd"></a>

```c
#define MAX32_DMA_SLOT_I2C0_TX 0x27U
```

相关声明：[MAX32_DMA_SLOT_I2C0_TX](#aee43cae318d6b70f9f2a7e6bd77e02dd)。

<a id="r_a8ae2d2fe05f0b1caea4b5c127fac3e11"></a>

```c
#define MAX32_DMA_SLOT_I2C2_TX 0x2AU
```

相关声明：[MAX32_DMA_SLOT_I2C2_TX](#a8ae2d2fe05f0b1caea4b5c127fac3e11)。

<a id="r_ac9b9591d0686de18fbbb1c3095754994"></a>

```c
#define MAX32_DMA_SLOT_CRC 0x2CU
```

相关声明：[MAX32_DMA_SLOT_CRC](#ac9b9591d0686de18fbbb1c3095754994)。

<a id="r_af2c822f39971c7bc6b8d58df6d139433"></a>

```c
#define MAX32_DMA_SLOT_UART2_TX 0x2EU
```

相关声明：[MAX32_DMA_SLOT_UART2_TX](#af2c822f39971c7bc6b8d58df6d139433)。

<a id="r_a60ee7da12fd5d1be90b7cd84f71e3400"></a>

```c
#define MAX32_DMA_SLOT_AES_TX 0x30U
```

相关声明：[MAX32_DMA_SLOT_AES_TX](#a60ee7da12fd5d1be90b7cd84f71e3400)。

<a id="r_a6ac25728509e7319f256fd02bb53f208"></a>

```c
#define MAX32_DMA_SLOT_I2S_TX 0x3EU
```

相关声明：[MAX32_DMA_SLOT_I2S_TX](#a6ac25728509e7319f256fd02bb53f208)。

## 206.2\_详细说明（Detailed Documentation）

<a id="a8244219f3dae7ceb188a3112ca041455"></a>

### `MAX32_DMA_SLOT_AES_RX`

```c
#define MAX32_DMA_SLOT_AES_RX 0x10U
```

<a id="a60ee7da12fd5d1be90b7cd84f71e3400"></a>

### `MAX32_DMA_SLOT_AES_TX`

```c
#define MAX32_DMA_SLOT_AES_TX 0x30U
```

<a id="ac9b9591d0686de18fbbb1c3095754994"></a>

### `MAX32_DMA_SLOT_CRC`

```c
#define MAX32_DMA_SLOT_CRC 0x2CU
```

<a id="a207563fbc9fb4110d78f92b1d2d4c423"></a>

### `MAX32_DMA_SLOT_I2C0_RX`

```c
#define MAX32_DMA_SLOT_I2C0_RX 0x07U
```

<a id="aee43cae318d6b70f9f2a7e6bd77e02dd"></a>

### `MAX32_DMA_SLOT_I2C0_TX`

```c
#define MAX32_DMA_SLOT_I2C0_TX 0x27U
```

<a id="a640bd0651d35157bdd822b11e8b23274"></a>

### `MAX32_DMA_SLOT_I2C2_RX`

```c
#define MAX32_DMA_SLOT_I2C2_RX 0x0AU
```

<a id="a8ae2d2fe05f0b1caea4b5c127fac3e11"></a>

### `MAX32_DMA_SLOT_I2C2_TX`

```c
#define MAX32_DMA_SLOT_I2C2_TX 0x2AU
```

<a id="a56646e3053fc8a76ef214adbd0ba5921"></a>

### `MAX32_DMA_SLOT_I2S_RX`

```c
#define MAX32_DMA_SLOT_I2S_RX 0x1EU
```

<a id="a6ac25728509e7319f256fd02bb53f208"></a>

### `MAX32_DMA_SLOT_I2S_TX`

```c
#define MAX32_DMA_SLOT_I2S_TX 0x3EU
```

<a id="a6e1ea6d5650545947928c83c71776c04"></a>

### `MAX32_DMA_SLOT_MEMTOMEM`

```c
#define MAX32_DMA_SLOT_MEMTOMEM 0x00U
```

<a id="ac505ee888a8cb52b03ac733a9b650097"></a>

### `MAX32_DMA_SLOT_SPI0_RX`

```c
#define MAX32_DMA_SLOT_SPI0_RX 0x01U
```

<a id="a26f06363fd4639eaee5668450adaa1c3"></a>

### `MAX32_DMA_SLOT_SPI0_TX`

```c
#define MAX32_DMA_SLOT_SPI0_TX 0x21U
```

<a id="a0df8d71978ba7b5c5b6766c1cf28d00c"></a>

### `MAX32_DMA_SLOT_SPI1_RX`

```c
#define MAX32_DMA_SLOT_SPI1_RX 0x02U
```

<a id="aa85105348eeb191fd2799d645aacc575"></a>

### `MAX32_DMA_SLOT_SPI1_TX`

```c
#define MAX32_DMA_SLOT_SPI1_TX 0x22U
```

<a id="ac823471b99eda7df54c2fce6eb923e96"></a>

### `MAX32_DMA_SLOT_UART0_RX`

```c
#define MAX32_DMA_SLOT_UART0_RX 0x04U
```

<a id="a009a7e71c5fed2afa3d8907411c454e3"></a>

### `MAX32_DMA_SLOT_UART0_TX`

```c
#define MAX32_DMA_SLOT_UART0_TX 0x24U
```

<a id="ac82aa4f9ad49e656963580bf297dcd26"></a>

### `MAX32_DMA_SLOT_UART2_RX`

```c
#define MAX32_DMA_SLOT_UART2_RX 0x0EU
```

<a id="af2c822f39971c7bc6b8d58df6d139433"></a>

### `MAX32_DMA_SLOT_UART2_TX`

```c
#define MAX32_DMA_SLOT_UART2_TX 0x2EU
```


## 206.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P483_max32675_dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P205_zephyr__dt-bindings__dma__max32672_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P207_zephyr__dt-bindings__dma__max32680_dma.h_文件参考.md)
