---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-2
title: zephyr__dt-bindings__clock__alif-balletto-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_alif-balletto-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Alif Balletto片上系统（SoC）系列的时钟ID。

<a id="details"></a>

```c
#include "alif-clocks-common.h"
```

查看此文件的源码。

Alif Balletto 片上系统（SoC）系列的时钟 ID（Clock IDs）。定义 Alif Balletto 系列的外设时钟标识符（Peripheral Clock Identifiers）。每个时钟 ID 都使用 `alif-clocks-common.h` 中的 `ALIF_CLK_CFG()` 宏编码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_a813a9b861434db79ed34077572d8a049"></a>

```c
#define ALIF_UART_CTRL_REG 0x08U
```

相关声明：[ALIF_UART_CTRL_REG](#a813a9b861434db79ed34077572d8a049)。

UART 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。

<a id="r_addde37c3ac85e05efadb7ce3bd593584"></a>

```c
#define ALIF_I2C0_CTRL_REG 0x50U
```

相关声明：[ALIF_I2C0_CTRL_REG](#addde37c3ac85e05efadb7ce3bd593584)。

I2C0 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。

<a id="r_acb2b4aa52d1ae84efea5ca1e970d2d89"></a>

```c
#define ALIF_I2C1_CTRL_REG 0x54U
```

相关声明：[ALIF_I2C1_CTRL_REG](#acb2b4aa52d1ae84efea5ca1e970d2d89)。

I2C1 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。

<a id="r_a7a39c396badaedaff3324b075890257c"></a>

```c
#define ALIF_TIMER_CLKSEL_REG 0x04U
```

相关声明：[ALIF_TIMER_CLKSEL_REG](#a7a39c396badaedaff3324b075890257c)。

LPTIMER 时钟选择寄存器在 `VBAT` 中的偏移量（Register Offset）。

<a id="define-members-1"></a>

### UART 外设时钟（Peripheral Clocks）

<a id="r_a43a7e3df28e51b5fafc9e0d3f0f51e1f"></a>

```c
#define ALIF_UART0_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 0U, 1U, 1U, 1U, 8U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART0_SYST_PCLK](#a43a7e3df28e51b5fafc9e0d3f0f51e1f)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART0 时钟来自系统外设时钟（PCLK）。

<a id="r_a93ab9f25dfbdcae0317933e78ae9626e"></a>

```c
#define ALIF_UART1_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 1U, 1U, 1U, 1U, 9U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART1_SYST_PCLK](#a93ab9f25dfbdcae0317933e78ae9626e)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART1 时钟来自系统外设时钟（PCLK）。

<a id="r_aec8f74217296de4e571560648bd9d79d"></a>

```c
#define ALIF_UART2_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 2U, 1U, 1U, 1U, 10U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART2_SYST_PCLK](#aec8f74217296de4e571560648bd9d79d)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART2 时钟来自系统外设时钟（PCLK）。

<a id="r_a18f62b7dafbee61e4ec18b3300b93073"></a>

```c
#define ALIF_UART3_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 3U, 1U, 1U, 1U, 11U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART3_SYST_PCLK](#a18f62b7dafbee61e4ec18b3300b93073)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART3 时钟来自系统外设时钟（PCLK）。

<a id="r_aebc7d4185a497b05abe49b2d75e022e7"></a>

```c
#define ALIF_UART4_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 4U, 1U, 1U, 1U, 12U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART4_SYST_PCLK](#aebc7d4185a497b05abe49b2d75e022e7)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART4 时钟来自系统外设时钟（PCLK）。

<a id="r_a666c22be8edf947889d81e2d69a02de9"></a>

```c
#define ALIF_UART5_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 5U, 1U, 1U, 1U, 13U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_UART5_SYST_PCLK](#a666c22be8edf947889d81e2d69a02de9)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

UART5 时钟来自系统外设时钟（PCLK）。

<a id="define-members-2"></a>

### I2C 外设时钟（Peripheral Clocks）

<a id="r_ab012193d089875a2a763ceb56347c7b4"></a>

```c
#define ALIF_I2C0_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C0_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_I2C0_SYST_PCLK](#ab012193d089875a2a763ceb56347c7b4)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

I2C0 时钟来自系统外设时钟（PCLK）。

<a id="r_a1b9a61d24a5fe4f25e56b997ffbd2f87"></a>

```c
#define ALIF_I2C1_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C1_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)
```

相关声明：[ALIF_I2C1_SYST_PCLK](#a1b9a61d24a5fe4f25e56b997ffbd2f87)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)。

I2C1 时钟来自系统外设时钟（PCLK）。

<a id="define-members-3"></a>

### LPTIMER 外设时钟（Peripheral Clocks）

这些通道没有时钟使能位（Clock Enable Bit）；只配置时钟源选择。

<a id="r_a7152242ea28bee4111a3e006d50c02e5"></a>

```c
#define ALIF_LPTIMER0_S32K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 0U, ALIF_PARENT_CLK_S32K)
```

相关声明：[ALIF_LPTIMER0_S32K_CLK](#a7152242ea28bee4111a3e006d50c02e5)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_S32K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a635a3c5ac05e64e3ad7e995512d723ec)。

LPTIMER0 时钟源（Clock Source）为 `S32K_CLK`。

<a id="r_aaa4613a850f2f81bd4dfee087467463f"></a>

```c
#define ALIF_LPTIMER0_128K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 0U, ALIF_PARENT_CLK_128K)
```

相关声明：[ALIF_LPTIMER0_128K_CLK](#aaa4613a850f2f81bd4dfee087467463f)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_128K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a2d26177aaee75a0afe00f9bd8a4e1a49)。

LPTIMER0 时钟源（Clock Source）为 `128K_CLK`。

<a id="r_ad2a4774bba40eefc4bc84cc6aece0126"></a>

```c
#define ALIF_LPTIMER1_S32K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 4U, ALIF_PARENT_CLK_S32K)
```

相关声明：[ALIF_LPTIMER1_S32K_CLK](#ad2a4774bba40eefc4bc84cc6aece0126)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_S32K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a635a3c5ac05e64e3ad7e995512d723ec)。

LPTIMER1 时钟源（Clock Source）为 `S32K_CLK`。

<a id="r_a1dd5fb759f8b31945758eea34030240a"></a>

```c
#define ALIF_LPTIMER1_128K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 4U, ALIF_PARENT_CLK_128K)
```

相关声明：[ALIF_LPTIMER1_128K_CLK](#a1dd5fb759f8b31945758eea34030240a)、[ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)、[ALIF_PARENT_CLK_128K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a2d26177aaee75a0afe00f9bd8a4e1a49)。

LPTIMER1 时钟源（Clock Source）为 `128K_CLK`。

## 2.2\_详细说明（Detailed Documentation）

<a id="addde37c3ac85e05efadb7ce3bd593584"></a>

### `ALIF_I2C0_CTRL_REG`

```c
#define ALIF_I2C0_CTRL_REG 0x50U
```

I2C0 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。

<a id="ab012193d089875a2a763ceb56347c7b4"></a>

### `ALIF_I2C0_SYST_PCLK`

```c
#define ALIF_I2C0_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C0_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)
```

I2C0 时钟来自系统外设时钟（PCLK）。

<a id="acb2b4aa52d1ae84efea5ca1e970d2d89"></a>

### `ALIF_I2C1_CTRL_REG`

```c
#define ALIF_I2C1_CTRL_REG 0x54U
```

I2C1 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。

<a id="a1b9a61d24a5fe4f25e56b997ffbd2f87"></a>

### `ALIF_I2C1_SYST_PCLK`

```c
#define ALIF_I2C1_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, I2C1_CTRL, 0U, 1U, 0U, 0U, 0U, ALIF_PARENT_CLK_SYST_PCLK)
```

I2C1 时钟来自系统外设时钟（PCLK）。

<a id="aaa4613a850f2f81bd4dfee087467463f"></a>

### `ALIF_LPTIMER0_128K_CLK`

```c
#define ALIF_LPTIMER0_128K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 0U, ALIF_PARENT_CLK_128K)
```

LPTIMER0 时钟源（Clock Source）为 `128K_CLK`。

<a id="a7152242ea28bee4111a3e006d50c02e5"></a>

### `ALIF_LPTIMER0_S32K_CLK`

```c
#define ALIF_LPTIMER0_S32K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 0U, ALIF_PARENT_CLK_S32K)
```

LPTIMER0 时钟源（Clock Source）为 `S32K_CLK`。

<a id="a1dd5fb759f8b31945758eea34030240a"></a>

### `ALIF_LPTIMER1_128K_CLK`

```c
#define ALIF_LPTIMER1_128K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 1U, 2U, 4U, ALIF_PARENT_CLK_128K)
```

LPTIMER1 时钟源（Clock Source）为 `128K_CLK`。

<a id="ad2a4774bba40eefc4bc84cc6aece0126"></a>

### `ALIF_LPTIMER1_S32K_CLK`

```c
#define ALIF_LPTIMER1_S32K_CLK ALIF_CLK_CFG(VBAT, TIMER_CLKSEL, 0U, 0U, 0U, 2U, 4U, ALIF_PARENT_CLK_S32K)
```

LPTIMER1 时钟源（Clock Source）为 `S32K_CLK`。

<a id="a7a39c396badaedaff3324b075890257c"></a>

### `ALIF_TIMER_CLKSEL_REG`

```c
#define ALIF_TIMER_CLKSEL_REG 0x04U
```

LPTIMER 时钟选择寄存器在 `VBAT` 中的偏移量（Register Offset）。

<a id="a43a7e3df28e51b5fafc9e0d3f0f51e1f"></a>

### `ALIF_UART0_SYST_PCLK`

```c
#define ALIF_UART0_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 0U, 1U, 1U, 1U, 8U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART0 时钟来自系统外设时钟（PCLK）。

<a id="a93ab9f25dfbdcae0317933e78ae9626e"></a>

### `ALIF_UART1_SYST_PCLK`

```c
#define ALIF_UART1_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 1U, 1U, 1U, 1U, 9U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART1 时钟来自系统外设时钟（PCLK）。

<a id="aec8f74217296de4e571560648bd9d79d"></a>

### `ALIF_UART2_SYST_PCLK`

```c
#define ALIF_UART2_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 2U, 1U, 1U, 1U, 10U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART2 时钟来自系统外设时钟（PCLK）。

<a id="a18f62b7dafbee61e4ec18b3300b93073"></a>

### `ALIF_UART3_SYST_PCLK`

```c
#define ALIF_UART3_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 3U, 1U, 1U, 1U, 11U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART3 时钟来自系统外设时钟（PCLK）。

<a id="aebc7d4185a497b05abe49b2d75e022e7"></a>

### `ALIF_UART4_SYST_PCLK`

```c
#define ALIF_UART4_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 4U, 1U, 1U, 1U, 12U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART4 时钟来自系统外设时钟（PCLK）。

<a id="a666c22be8edf947889d81e2d69a02de9"></a>

### `ALIF_UART5_SYST_PCLK`

```c
#define ALIF_UART5_SYST_PCLK ALIF_CLK_CFG(CLKCTL_PER_SLV, UART_CTRL, 5U, 1U, 1U, 1U, 13U, ALIF_PARENT_CLK_SYST_PCLK)
```

UART5 时钟来自系统外设时钟（PCLK）。

<a id="a813a9b861434db79ed34077572d8a049"></a>

### `ALIF_UART_CTRL_REG`

```c
#define ALIF_UART_CTRL_REG 0x08U
```

UART 控制寄存器在 `CLKCTL_PER_SLV` 中的偏移量（Register Offset）。


## 2.3\_原页交叉引用（Cross References）

- [alif-clocks-common.h](../api_source_reference/P021_alif-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P020_alif-balletto-clocks.h_源码浏览.md)
- [ALIF_CLK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#ad16c3d170e343c040ee7db3de70c1cd3)
- [ALIF_PARENT_CLK_SYST_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#acc723a914c55fe078a797fd3b27c8e31)
- [ALIF_PARENT_CLK_S32K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a635a3c5ac05e64e3ad7e995512d723ec)
- [ALIF_PARENT_CLK_128K](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html#a2d26177aaee75a0afe00f9bd8a4e1a49)
- [alif-clocks-common.h](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__net__conn_mgr_connectivity.h_文件参考.md)
