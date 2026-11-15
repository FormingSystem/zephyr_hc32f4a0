---
id: learning.zephyr-docs.api-file-reference.page-209
title: zephyr__dt-bindings__dma__max78000_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max78000__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第209章\_zephyr\_\_dt-bindings\_\_dma\_\_max78000\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max78000__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 209.1\_宏定义（Macros）

<a id="r_a804f371fcbd8b1340116f8438b7b188d"></a>

```c
#define MAX78_DMA_SLOT_MEMTOMEM 0x00U
```

相关声明：[MAX78_DMA_SLOT_MEMTOMEM](#a804f371fcbd8b1340116f8438b7b188d)。

<a id="r_ac4eb0187fa7ab1c0484c89ec1f607570"></a>

```c
#define MAX78_DMA_SLOT_SPI1_RX 0x01U
```

相关声明：[MAX78_DMA_SLOT_SPI1_RX](#ac4eb0187fa7ab1c0484c89ec1f607570)。

<a id="r_af20a164976c6fa2881df1cd32e85bb3a"></a>

```c
#define MAX78_DMA_SLOT_UART0_RX 0x04U
```

相关声明：[MAX78_DMA_SLOT_UART0_RX](#af20a164976c6fa2881df1cd32e85bb3a)。

<a id="r_a83b8c4ad1bf081f36da5f623ef110f26"></a>

```c
#define MAX78_DMA_SLOT_UART1_RX 0x05U
```

相关声明：[MAX78_DMA_SLOT_UART1_RX](#a83b8c4ad1bf081f36da5f623ef110f26)。

<a id="r_a828e58a06fddcb562fa9bf1bd457a62f"></a>

```c
#define MAX78_DMA_SLOT_I2C0_RX 0x07U
```

相关声明：[MAX78_DMA_SLOT_I2C0_RX](#a828e58a06fddcb562fa9bf1bd457a62f)。

<a id="r_a1788afc1b9bd9b8eb10e7e460008ef4b"></a>

```c
#define MAX78_DMA_SLOT_I2C1_RX 0x08U
```

相关声明：[MAX78_DMA_SLOT_I2C1_RX](#a1788afc1b9bd9b8eb10e7e460008ef4b)。

<a id="r_a21946e016bc350337ee481fdecd5dc31"></a>

```c
#define MAX78_DMA_SLOT_ADC 0x09U
```

相关声明：[MAX78_DMA_SLOT_ADC](#a21946e016bc350337ee481fdecd5dc31)。

<a id="r_ae0d35bd8d5afe9d72cd350433051e852"></a>

```c
#define MAX78_DMA_SLOT_I2C2_RX 0x0AU
```

相关声明：[MAX78_DMA_SLOT_I2C2_RX](#ae0d35bd8d5afe9d72cd350433051e852)。

<a id="r_a93bb2f789bbd725749a078d746489055"></a>

```c
#define MAX78_DMA_SLOT_PCIF_RX 0x0DU
```

相关声明：[MAX78_DMA_SLOT_PCIF_RX](#a93bb2f789bbd725749a078d746489055)。

<a id="r_a818af9d05cb91cdaf900eedd129c7f35"></a>

```c
#define MAX78_DMA_SLOT_UART2_RX 0x0EU
```

相关声明：[MAX78_DMA_SLOT_UART2_RX](#a818af9d05cb91cdaf900eedd129c7f35)。

<a id="r_a07dc60872bc29b57a05fcccfbcb7a39d"></a>

```c
#define MAX78_DMA_SLOT_SPI0_RX 0x0FU
```

相关声明：[MAX78_DMA_SLOT_SPI0_RX](#a07dc60872bc29b57a05fcccfbcb7a39d)。

<a id="r_aae23d3a3d83e43bcd389ad000c83ba1b"></a>

```c
#define MAX78_DMA_SLOT_UART3_RX 0x1CU
```

相关声明：[MAX78_DMA_SLOT_UART3_RX](#aae23d3a3d83e43bcd389ad000c83ba1b)。

<a id="r_a9128b048ce1b384a5154b30e1f9bad8c"></a>

```c
#define MAX78_DMA_SLOT_I2S_RX 0x1EU
```

相关声明：[MAX78_DMA_SLOT_I2S_RX](#a9128b048ce1b384a5154b30e1f9bad8c)。

<a id="r_a6f38b67fc333fc709fde5ccc7e399976"></a>

```c
#define MAX78_DMA_SLOT_SPI1_TX 0x21U
```

相关声明：[MAX78_DMA_SLOT_SPI1_TX](#a6f38b67fc333fc709fde5ccc7e399976)。

<a id="r_a7300e2d579c2884d7a3b237af452cdd4"></a>

```c
#define MAX78_DMA_SLOT_UART0_TX 0x24U
```

相关声明：[MAX78_DMA_SLOT_UART0_TX](#a7300e2d579c2884d7a3b237af452cdd4)。

<a id="r_a0bf86797983fa9d92b9872a89b5ab4c3"></a>

```c
#define MAX78_DMA_SLOT_UART1_TX 0x25U
```

相关声明：[MAX78_DMA_SLOT_UART1_TX](#a0bf86797983fa9d92b9872a89b5ab4c3)。

<a id="r_a023d8aac409ea08bee138ea6fed41bc9"></a>

```c
#define MAX78_DMA_SLOT_I2C0_TX 0x27U
```

相关声明：[MAX78_DMA_SLOT_I2C0_TX](#a023d8aac409ea08bee138ea6fed41bc9)。

<a id="r_a29c3b163b9dda961f998ace5405009bb"></a>

```c
#define MAX78_DMA_SLOT_I2C1_TX 0x28U
```

相关声明：[MAX78_DMA_SLOT_I2C1_TX](#a29c3b163b9dda961f998ace5405009bb)。

<a id="r_ab8a342926682de42ba082b13d278950f"></a>

```c
#define MAX78_DMA_SLOT_I2C2_TX 0x2AU
```

相关声明：[MAX78_DMA_SLOT_I2C2_TX](#ab8a342926682de42ba082b13d278950f)。

<a id="r_a57a7ef9f4ae8c6db6f78b789fac33f21"></a>

```c
#define MAX78_DMA_SLOT_CRC 0x2CU
```

相关声明：[MAX78_DMA_SLOT_CRC](#a57a7ef9f4ae8c6db6f78b789fac33f21)。

<a id="r_aaec39304514018ece49564641d060f9e"></a>

```c
#define MAX78_DMA_SLOT_PCIF_TX 0x2DU
```

相关声明：[MAX78_DMA_SLOT_PCIF_TX](#aaec39304514018ece49564641d060f9e)。

<a id="r_a3990ce90b6db0e6372c6af56d4e294ac"></a>

```c
#define MAX78_DMA_SLOT_UART2_TX 0x2EU
```

相关声明：[MAX78_DMA_SLOT_UART2_TX](#a3990ce90b6db0e6372c6af56d4e294ac)。

<a id="r_adb6a50ef9089ebe08d5b95521b037346"></a>

```c
#define MAX78_DMA_SLOT_SPI0_TX 0x2FU
```

相关声明：[MAX78_DMA_SLOT_SPI0_TX](#adb6a50ef9089ebe08d5b95521b037346)。

<a id="r_a6a7a6d09592f9fe03b88698d448e3b02"></a>

```c
#define MAX78_DMA_SLOT_UART3_TX 0x3CU
```

相关声明：[MAX78_DMA_SLOT_UART3_TX](#a6a7a6d09592f9fe03b88698d448e3b02)。

<a id="r_ae695fde1c5fd0714212be56b84b363a5"></a>

```c
#define MAX78_DMA_SLOT_I2S_TX 0x3EU
```

相关声明：[MAX78_DMA_SLOT_I2S_TX](#ae695fde1c5fd0714212be56b84b363a5)。

## 209.2\_详细说明（Detailed Documentation）

<a id="a21946e016bc350337ee481fdecd5dc31"></a>

### `MAX78_DMA_SLOT_ADC`

```c
#define MAX78_DMA_SLOT_ADC 0x09U
```

<a id="a57a7ef9f4ae8c6db6f78b789fac33f21"></a>

### `MAX78_DMA_SLOT_CRC`

```c
#define MAX78_DMA_SLOT_CRC 0x2CU
```

<a id="a828e58a06fddcb562fa9bf1bd457a62f"></a>

### `MAX78_DMA_SLOT_I2C0_RX`

```c
#define MAX78_DMA_SLOT_I2C0_RX 0x07U
```

<a id="a023d8aac409ea08bee138ea6fed41bc9"></a>

### `MAX78_DMA_SLOT_I2C0_TX`

```c
#define MAX78_DMA_SLOT_I2C0_TX 0x27U
```

<a id="a1788afc1b9bd9b8eb10e7e460008ef4b"></a>

### `MAX78_DMA_SLOT_I2C1_RX`

```c
#define MAX78_DMA_SLOT_I2C1_RX 0x08U
```

<a id="a29c3b163b9dda961f998ace5405009bb"></a>

### `MAX78_DMA_SLOT_I2C1_TX`

```c
#define MAX78_DMA_SLOT_I2C1_TX 0x28U
```

<a id="ae0d35bd8d5afe9d72cd350433051e852"></a>

### `MAX78_DMA_SLOT_I2C2_RX`

```c
#define MAX78_DMA_SLOT_I2C2_RX 0x0AU
```

<a id="ab8a342926682de42ba082b13d278950f"></a>

### `MAX78_DMA_SLOT_I2C2_TX`

```c
#define MAX78_DMA_SLOT_I2C2_TX 0x2AU
```

<a id="a9128b048ce1b384a5154b30e1f9bad8c"></a>

### `MAX78_DMA_SLOT_I2S_RX`

```c
#define MAX78_DMA_SLOT_I2S_RX 0x1EU
```

<a id="ae695fde1c5fd0714212be56b84b363a5"></a>

### `MAX78_DMA_SLOT_I2S_TX`

```c
#define MAX78_DMA_SLOT_I2S_TX 0x3EU
```

<a id="a804f371fcbd8b1340116f8438b7b188d"></a>

### `MAX78_DMA_SLOT_MEMTOMEM`

```c
#define MAX78_DMA_SLOT_MEMTOMEM 0x00U
```

<a id="a93bb2f789bbd725749a078d746489055"></a>

### `MAX78_DMA_SLOT_PCIF_RX`

```c
#define MAX78_DMA_SLOT_PCIF_RX 0x0DU
```

<a id="aaec39304514018ece49564641d060f9e"></a>

### `MAX78_DMA_SLOT_PCIF_TX`

```c
#define MAX78_DMA_SLOT_PCIF_TX 0x2DU
```

<a id="a07dc60872bc29b57a05fcccfbcb7a39d"></a>

### `MAX78_DMA_SLOT_SPI0_RX`

```c
#define MAX78_DMA_SLOT_SPI0_RX 0x0FU
```

<a id="adb6a50ef9089ebe08d5b95521b037346"></a>

### `MAX78_DMA_SLOT_SPI0_TX`

```c
#define MAX78_DMA_SLOT_SPI0_TX 0x2FU
```

<a id="ac4eb0187fa7ab1c0484c89ec1f607570"></a>

### `MAX78_DMA_SLOT_SPI1_RX`

```c
#define MAX78_DMA_SLOT_SPI1_RX 0x01U
```

<a id="a6f38b67fc333fc709fde5ccc7e399976"></a>

### `MAX78_DMA_SLOT_SPI1_TX`

```c
#define MAX78_DMA_SLOT_SPI1_TX 0x21U
```

<a id="af20a164976c6fa2881df1cd32e85bb3a"></a>

### `MAX78_DMA_SLOT_UART0_RX`

```c
#define MAX78_DMA_SLOT_UART0_RX 0x04U
```

<a id="a7300e2d579c2884d7a3b237af452cdd4"></a>

### `MAX78_DMA_SLOT_UART0_TX`

```c
#define MAX78_DMA_SLOT_UART0_TX 0x24U
```

<a id="a83b8c4ad1bf081f36da5f623ef110f26"></a>

### `MAX78_DMA_SLOT_UART1_RX`

```c
#define MAX78_DMA_SLOT_UART1_RX 0x05U
```

<a id="a0bf86797983fa9d92b9872a89b5ab4c3"></a>

### `MAX78_DMA_SLOT_UART1_TX`

```c
#define MAX78_DMA_SLOT_UART1_TX 0x25U
```

<a id="a818af9d05cb91cdaf900eedd129c7f35"></a>

### `MAX78_DMA_SLOT_UART2_RX`

```c
#define MAX78_DMA_SLOT_UART2_RX 0x0EU
```

<a id="a3990ce90b6db0e6372c6af56d4e294ac"></a>

### `MAX78_DMA_SLOT_UART2_TX`

```c
#define MAX78_DMA_SLOT_UART2_TX 0x2EU
```

<a id="aae23d3a3d83e43bcd389ad000c83ba1b"></a>

### `MAX78_DMA_SLOT_UART3_RX`

```c
#define MAX78_DMA_SLOT_UART3_RX 0x1CU
```

<a id="a6a7a6d09592f9fe03b88698d448e3b02"></a>

### `MAX78_DMA_SLOT_UART3_TX`

```c
#define MAX78_DMA_SLOT_UART3_TX 0x3CU
```


## 209.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P486_max78000_dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P208_zephyr__dt-bindings__dma__max32690_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P210_zephyr__dt-bindings__dma__max78002_dma.h_文件参考.md)
