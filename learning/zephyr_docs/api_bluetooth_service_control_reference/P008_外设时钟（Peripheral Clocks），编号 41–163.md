---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-8
title: 外设时钟（Peripheral Clocks），编号 41–163
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_外设时钟（Peripheral Clocks），编号 41–163

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__peripheral__clocks.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于 MIMX9529 `fsl_clock.h` 的外设时钟定义。

<a id="details"></a>

基于 MIMX9529 `fsl_clock.h` 的外设时钟定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_gadd6d1896e8c854ea655c6149753054b2"></a>

```c
#define IMX952_CLK_ADC (IMX952_CCM_NUM_CLK_SRC + 0)
```

相关声明：[IMX952_CLK_ADC](#gadd6d1896e8c854ea655c6149753054b2)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

ADC 时钟（Clock）。

<a id="r_gabfebcfad721ae0c19c0fdab927890cc9"></a>

```c
#define IMX952_CLK_RESERVED1 (IMX952_CCM_NUM_CLK_SRC + 1)
```

相关声明：[IMX952_CLK_RESERVED1](#gabfebcfad721ae0c19c0fdab927890cc9)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 1（Reserved peripheral clock 1）。

<a id="r_ga3c9d2874480a9a3742b81aa64657d5a0"></a>

```c
#define IMX952_CLK_BUSAON (IMX952_CCM_NUM_CLK_SRC + 2)
```

相关声明：[IMX952_CLK_BUSAON](#ga3c9d2874480a9a3742b81aa64657d5a0)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

AON 总线 时钟（AON bus clock）。

<a id="r_gafe7b5204c752fa2dfc45abbe9ef56b1b"></a>

```c
#define IMX952_CLK_CAN1 (IMX952_CCM_NUM_CLK_SRC + 3)
```

相关声明：[IMX952_CLK_CAN1](#gafe7b5204c752fa2dfc45abbe9ef56b1b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN1 时钟（CAN1 clock）。

<a id="r_gaa2bec9707b9dca1d91c5473ef1640ca2"></a>

```c
#define IMX952_CLK_RESERVED4 (IMX952_CCM_NUM_CLK_SRC + 4)
```

相关声明：[IMX952_CLK_RESERVED4](#gaa2bec9707b9dca1d91c5473ef1640ca2)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 4（Reserved peripheral clock 4）。

<a id="r_gad356191a96c27cb2c84bb54fded38075"></a>

```c
#define IMX952_CLK_I3C1SLOW (IMX952_CCM_NUM_CLK_SRC + 5)
```

相关声明：[IMX952_CLK_I3C1SLOW](#gad356191a96c27cb2c84bb54fded38075)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

I3C1 慢速 时钟（I3C1 slow clock）。

<a id="r_gad2e8978ebfc8b671c2b0ad9d404be7d4"></a>

```c
#define IMX952_CLK_LPI2C1 (IMX952_CCM_NUM_CLK_SRC + 6)
```

相关声明：[IMX952_CLK_LPI2C1](#gad2e8978ebfc8b671c2b0ad9d404be7d4)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C1 时钟（LPI2C1 clock）。

<a id="r_ga41460f3425b5258f3936a4c05f9774ed"></a>

```c
#define IMX952_CLK_LPI2C2 (IMX952_CCM_NUM_CLK_SRC + 7)
```

相关声明：[IMX952_CLK_LPI2C2](#ga41460f3425b5258f3936a4c05f9774ed)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C2 时钟（LPI2C2 clock）。

<a id="r_ga03ef430f1aa454c4a765f540064045d4"></a>

```c
#define IMX952_CLK_LPSPI1 (IMX952_CCM_NUM_CLK_SRC + 8)
```

相关声明：[IMX952_CLK_LPSPI1](#ga03ef430f1aa454c4a765f540064045d4)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI1 时钟（LPSPI1 clock）。

<a id="r_ga72914bea56dffea39955b80a363aea68"></a>

```c
#define IMX952_CLK_LPSPI2 (IMX952_CCM_NUM_CLK_SRC + 9)
```

相关声明：[IMX952_CLK_LPSPI2](#ga72914bea56dffea39955b80a363aea68)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI2 时钟（LPSPI2 clock）。

<a id="r_gacb1ebcf043e321e0db27c5f191799529"></a>

```c
#define IMX952_CLK_LPTMR1 (IMX952_CCM_NUM_CLK_SRC + 10)
```

相关声明：[IMX952_CLK_LPTMR1](#gacb1ebcf043e321e0db27c5f191799529)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPTMR1 时钟（LPTMR1 clock）。

<a id="r_ga8436c0cf30cd588c6455d0321baec0dc"></a>

```c
#define IMX952_CLK_LPUART1 (IMX952_CCM_NUM_CLK_SRC + 11)
```

相关声明：[IMX952_CLK_LPUART1](#ga8436c0cf30cd588c6455d0321baec0dc)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART1 时钟（LPUART1 clock）。

<a id="r_ga79f9479bcd1aa7e6fcc69063391f4b14"></a>

```c
#define IMX952_CLK_LPUART2 (IMX952_CCM_NUM_CLK_SRC + 12)
```

相关声明：[IMX952_CLK_LPUART2](#ga79f9479bcd1aa7e6fcc69063391f4b14)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART2 时钟（LPUART2 clock）。

<a id="r_ga5659948ecd9b48807e051734ea707738"></a>

```c
#define IMX952_CLK_M33 (IMX952_CCM_NUM_CLK_SRC + 13)
```

相关声明：[IMX952_CLK_M33](#ga5659948ecd9b48807e051734ea707738)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M33 核心 时钟（Cortex-M33 core clock）。

<a id="r_ga2d428ca57850519a072c844cd6af195c"></a>

```c
#define IMX952_CLK_M33SYSTICK (IMX952_CCM_NUM_CLK_SRC + 14)
```

相关声明：[IMX952_CLK_M33SYSTICK](#ga2d428ca57850519a072c844cd6af195c)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M33 SysTick 时钟（Cortex-M33 SysTick clock）。

<a id="r_ga63ee8489512d404515a7c0a93f709461"></a>

```c
#define IMX952_CLK_RESERVED15 (IMX952_CCM_NUM_CLK_SRC + 15)
```

相关声明：[IMX952_CLK_RESERVED15](#ga63ee8489512d404515a7c0a93f709461)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 15（Reserved peripheral clock 15）。

<a id="r_ga67b66c12811be5bed864d37a25653e2d"></a>

```c
#define IMX952_CLK_PDM (IMX952_CCM_NUM_CLK_SRC + 16)
```

相关声明：[IMX952_CLK_PDM](#ga67b66c12811be5bed864d37a25653e2d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

PDM 时钟（PDM clock）。

<a id="r_gad6bb83d2d46f67c39716ec744909e1f6"></a>

```c
#define IMX952_CLK_SAI1 (IMX952_CCM_NUM_CLK_SRC + 17)
```

相关声明：[IMX952_CLK_SAI1](#gad6bb83d2d46f67c39716ec744909e1f6)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI1 时钟（SAI1 clock）。

<a id="r_ga651989292cdcf481380a884d4c0e5aef"></a>

```c
#define IMX952_CLK_RESERVED18 (IMX952_CCM_NUM_CLK_SRC + 18)
```

相关声明：[IMX952_CLK_RESERVED18](#ga651989292cdcf481380a884d4c0e5aef)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 18（Reserved peripheral clock 18）。

<a id="r_ga54de19acf040cef42d3e40ffce9412eb"></a>

```c
#define IMX952_CLK_TPM2 (IMX952_CCM_NUM_CLK_SRC + 19)
```

相关声明：[IMX952_CLK_TPM2](#ga54de19acf040cef42d3e40ffce9412eb)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM2 时钟（TPM2 clock）。

<a id="r_gae8433b2b0ba8c3daf76216a994a2d353"></a>

```c
#define IMX952_CLK_RESERVED20 (IMX952_CCM_NUM_CLK_SRC + 20)
```

相关声明：[IMX952_CLK_RESERVED20](#gae8433b2b0ba8c3daf76216a994a2d353)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 20（Reserved peripheral clock 20）。

<a id="r_ga04d79491636ed5a37b9b4ae801066574"></a>

```c
#define IMX952_CLK_CAMAPB (IMX952_CCM_NUM_CLK_SRC + 21)
```

相关声明：[IMX952_CLK_CAMAPB](#ga04d79491636ed5a37b9b4ae801066574)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 APB 时钟（Camera APB clock）。

<a id="r_ga09fffe1b5527547c20667290b422e7de"></a>

```c
#define IMX952_CLK_CAMAXI (IMX952_CCM_NUM_CLK_SRC + 22)
```

相关声明：[IMX952_CLK_CAMAXI](#ga09fffe1b5527547c20667290b422e7de)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 AXI 时钟（Camera AXI clock）。

<a id="r_ga3dbac1b1a9e7e6c644ee140c96bbf81f"></a>

```c
#define IMX952_CLK_CAMCM0 (IMX952_CCM_NUM_CLK_SRC + 23)
```

相关声明：[IMX952_CLK_CAMCM0](#ga3dbac1b1a9e7e6c644ee140c96bbf81f)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 CM0 时钟（Camera CM0 clock）。

<a id="r_ga19837041e27ed67e9e6df73716fc9d54"></a>

```c
#define IMX952_CLK_CAMISI (IMX952_CCM_NUM_CLK_SRC + 24)
```

相关声明：[IMX952_CLK_CAMISI](#ga19837041e27ed67e9e6df73716fc9d54)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 ISI 时钟（Camera ISI clock）。

<a id="r_ga586eb4045847dbe332d8575acf99f3be"></a>

```c
#define IMX952_CLK_CAMPHYCFG (IMX952_CCM_NUM_CLK_SRC + 25)
```

相关声明：[IMX952_CLK_CAMPHYCFG](#ga586eb4045847dbe332d8575acf99f3be)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

摄像头 PHY 配置 时钟（Camera PHY configuration clock）。

<a id="r_ga831a26f60a7116f4131bf77a8e5f66c9"></a>

```c
#define IMX952_CLK_MIPIPHYPLLBYPASS (IMX952_CCM_NUM_CLK_SRC + 26)
```

相关声明：[IMX952_CLK_MIPIPHYPLLBYPASS](#ga831a26f60a7116f4131bf77a8e5f66c9)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

MIPI PHY PLL 旁路 时钟（MIPI PHY PLL bypass clock）。

<a id="r_ga3db8105a07f2ce87e006a2b9f758bd8f"></a>

```c
#define IMX952_CLK_RESERVED27 (IMX952_CCM_NUM_CLK_SRC + 27)
```

相关声明：[IMX952_CLK_RESERVED27](#ga3db8105a07f2ce87e006a2b9f758bd8f)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 27（Reserved peripheral clock 27）。

<a id="r_ga59bed80ccf3b29c8a1f92f2a265e02b1"></a>

```c
#define IMX952_CLK_MIPITESTBYTE (IMX952_CCM_NUM_CLK_SRC + 28)
```

相关声明：[IMX952_CLK_MIPITESTBYTE](#ga59bed80ccf3b29c8a1f92f2a265e02b1)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

MIPI 测试 字节 时钟（MIPI test byte clock）。

<a id="r_gae927a53c34c5d1fcb6c4e7d6f5a2dbf2"></a>

```c
#define IMX952_CLK_A55 (IMX952_CCM_NUM_CLK_SRC + 29)
```

相关声明：[IMX952_CLK_A55](#gae927a53c34c5d1fcb6c4e7d6f5a2dbf2)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 核心 时钟（Cortex-A55 core clock）。

<a id="r_gaf97b4deb07b00e3d70b1ac3cf6604486"></a>

```c
#define IMX952_CLK_A55MTRBUS (IMX952_CCM_NUM_CLK_SRC + 30)
```

相关声明：[IMX952_CLK_A55MTRBUS](#gaf97b4deb07b00e3d70b1ac3cf6604486)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 MTR 总线 时钟（Cortex-A55 MTR bus clock）。

<a id="r_gad07cd50a19b3edea126a948af250e0e0"></a>

```c
#define IMX952_CLK_A55PERIPH (IMX952_CCM_NUM_CLK_SRC + 31)
```

相关声明：[IMX952_CLK_A55PERIPH](#gad07cd50a19b3edea126a948af250e0e0)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-A55 外设 时钟（Cortex-A55 peripheral clock）。

<a id="r_ga1de7bf9d1d6864c6d7f5b09de6d742c5"></a>

```c
#define IMX952_CLK_DRAMALT (IMX952_CCM_NUM_CLK_SRC + 32)
```

相关声明：[IMX952_CLK_DRAMALT](#ga1de7bf9d1d6864c6d7f5b09de6d742c5)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

DRAM 备用 时钟（DRAM alternate clock）。

<a id="r_ga4fc0088507462042656a34a6bf430dfb"></a>

```c
#define IMX952_CLK_DRAMAPB (IMX952_CCM_NUM_CLK_SRC + 33)
```

相关声明：[IMX952_CLK_DRAMAPB](#ga4fc0088507462042656a34a6bf430dfb)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

DRAM APB 时钟（DRAM APB clock）。

<a id="r_ga0439a95f09f1f498b45f4cf51ceb8983"></a>

```c
#define IMX952_CLK_DISPAPB (IMX952_CCM_NUM_CLK_SRC + 34)
```

相关声明：[IMX952_CLK_DISPAPB](#ga0439a95f09f1f498b45f4cf51ceb8983)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 APB 时钟（Display APB clock）。

<a id="r_gae7bdf479b9aea05d0c99afa3e08c56ee"></a>

```c
#define IMX952_CLK_DISPAXI (IMX952_CCM_NUM_CLK_SRC + 35)
```

相关声明：[IMX952_CLK_DISPAXI](#gae7bdf479b9aea05d0c99afa3e08c56ee)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 AXI 时钟（Display AXI clock）。

<a id="r_ga5a19ad3418eea5aedbbf72aa1b073a4b"></a>

```c
#define IMX952_CLK_DISPLPSPI (IMX952_CCM_NUM_CLK_SRC + 36)
```

相关声明：[IMX952_CLK_DISPLPSPI](#ga5a19ad3418eea5aedbbf72aa1b073a4b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 LPSPI 时钟（Display LPSPI clock）。

<a id="r_ga5cce1fd12ca390ad1b345813797d51bb"></a>

```c
#define IMX952_CLK_DISPOCRAM (IMX952_CCM_NUM_CLK_SRC + 37)
```

相关声明：[IMX952_CLK_DISPOCRAM](#ga5cce1fd12ca390ad1b345813797d51bb)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 OCRAM 时钟（Display OCRAM clock）。

<a id="r_gad866759ea1a19d4b38335a722dc36bb1"></a>

```c
#define IMX952_CLK_DISPHYCFG (IMX952_CCM_NUM_CLK_SRC + 38)
```

相关声明：[IMX952_CLK_DISPHYCFG](#gad866759ea1a19d4b38335a722dc36bb1)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 PHY 配置 时钟（Display PHY configuration clock）。

<a id="r_gabde7224b0230770740576871301f72a4"></a>

```c
#define IMX952_CLK_DISP1PIX (IMX952_CCM_NUM_CLK_SRC + 39)
```

相关声明：[IMX952_CLK_DISP1PIX](#gabde7224b0230770740576871301f72a4)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 1 像素 时钟（Display 1 pixel clock）。

<a id="r_ga4885eba2f05bd15129c8d732d06195b6"></a>

```c
#define IMX952_CLK_DISPCDPHYAPB (IMX952_CCM_NUM_CLK_SRC + 40)
```

相关声明：[IMX952_CLK_DISPCDPHYAPB](#ga4885eba2f05bd15129c8d732d06195b6)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

显示 CD PHY APB 时钟（Display CD PHY APB clock）。

<a id="r_ga17655f965e3128b63c8a3abf3c34768a"></a>

```c
#define IMX952_CLK_RESERVED41 (IMX952_CCM_NUM_CLK_SRC + 41)
```

相关声明：[IMX952_CLK_RESERVED41](#ga17655f965e3128b63c8a3abf3c34768a)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 41（Reserved peripheral clock 41）。

<a id="r_ga8b41919d03a6d77af5f4997b63899159"></a>

```c
#define IMX952_CLK_GPUAPB (IMX952_CCM_NUM_CLK_SRC + 42)
```

相关声明：[IMX952_CLK_GPUAPB](#ga8b41919d03a6d77af5f4997b63899159)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

GPU APB 时钟（GPU APB clock）。

<a id="r_ga24c41790fa58c6bf9b2170e23e0c56f0"></a>

```c
#define IMX952_CLK_GPU (IMX952_CCM_NUM_CLK_SRC + 43)
```

相关声明：[IMX952_CLK_GPU](#ga24c41790fa58c6bf9b2170e23e0c56f0)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

GPU 核心 时钟（GPU core clock）。

<a id="r_ga20f1a2162bf9ce0b5e0b2fe2db0075c5"></a>

```c
#define IMX952_CLK_HSIOACSCAN480M (IMX952_CCM_NUM_CLK_SRC + 44)
```

相关声明：[IMX952_CLK_HSIOACSCAN480M](#ga20f1a2162bf9ce0b5e0b2fe2db0075c5)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO AC 扫描 480MHz 时钟（HSIO AC scan 480MHz clock）。

<a id="r_ga1b77d6c93474b9bee9cf2691c2e38d91"></a>

```c
#define IMX952_CLK_HSIOACSCAN80M (IMX952_CCM_NUM_CLK_SRC + 45)
```

相关声明：[IMX952_CLK_HSIOACSCAN80M](#ga1b77d6c93474b9bee9cf2691c2e38d91)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO AC 扫描 80MHz 时钟（HSIO AC scan 80MHz clock）。

<a id="r_gaa79e6a0b67c4c3d2059821cf6304f94b"></a>

```c
#define IMX952_CLK_HSIO (IMX952_CCM_NUM_CLK_SRC + 46)
```

相关声明：[IMX952_CLK_HSIO](#gaa79e6a0b67c4c3d2059821cf6304f94b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO 总线 时钟（HSIO bus clock）。

<a id="r_gae3c37de19e68fc80164646d9f18aca67"></a>

```c
#define IMX952_CLK_HSIOPCIEAUX (IMX952_CCM_NUM_CLK_SRC + 47)
```

相关声明：[IMX952_CLK_HSIOPCIEAUX](#gae3c37de19e68fc80164646d9f18aca67)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 辅助 时钟（HSIO PCIe auxiliary clock）。

<a id="r_gaf9f80c9df9203ac548d36c2eef2e074b"></a>

```c
#define IMX952_CLK_HSIOPCIETEST160M (IMX952_CCM_NUM_CLK_SRC + 48)
```

相关声明：[IMX952_CLK_HSIOPCIETEST160M](#gaf9f80c9df9203ac548d36c2eef2e074b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 160MHz 时钟（HSIO PCIe test 160MHz clock）。

<a id="r_ga656c3a598cc01dd56074ba178f4dd564"></a>

```c
#define IMX952_CLK_HSIOPCIETEST400M (IMX952_CCM_NUM_CLK_SRC + 49)
```

相关声明：[IMX952_CLK_HSIOPCIETEST400M](#ga656c3a598cc01dd56074ba178f4dd564)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 400MHz 时钟（HSIO PCIe test 400MHz clock）。

<a id="r_gaf090ef87122451cc2c235950be7e7b86"></a>

```c
#define IMX952_CLK_HSIOPCIETEST500M (IMX952_CCM_NUM_CLK_SRC + 50)
```

相关声明：[IMX952_CLK_HSIOPCIETEST500M](#gaf090ef87122451cc2c235950be7e7b86)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO PCIe 测试 500MHz 时钟（HSIO PCIe test 500MHz clock）。

<a id="r_gafecfa87e99167f088cc489dae90a4173"></a>

```c
#define IMX952_CLK_HSIOUSBTEST50M (IMX952_CCM_NUM_CLK_SRC + 51)
```

相关声明：[IMX952_CLK_HSIOUSBTEST50M](#gafecfa87e99167f088cc489dae90a4173)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO USB 测试 50MHz 时钟（HSIO USB test 50MHz clock）。

<a id="r_gafadaf0326bf74a16cb1f58060fe3ce03"></a>

```c
#define IMX952_CLK_HSIOUSBTEST60M (IMX952_CCM_NUM_CLK_SRC + 52)
```

相关声明：[IMX952_CLK_HSIOUSBTEST60M](#gafadaf0326bf74a16cb1f58060fe3ce03)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

HSIO USB 测试 60MHz 时钟（HSIO USB test 60MHz clock）。

<a id="r_ga400485d6af68996afc3a86eabb9074f8"></a>

```c
#define IMX952_CLK_BUSM7 (IMX952_CCM_NUM_CLK_SRC + 53)
```

相关声明：[IMX952_CLK_BUSM7](#ga400485d6af68996afc3a86eabb9074f8)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

M7 总线 时钟（M7 bus clock）。

<a id="r_ga71d063d87af2e021db96f44c72d9e611"></a>

```c
#define IMX952_CLK_M7 (IMX952_CCM_NUM_CLK_SRC + 54)
```

相关声明：[IMX952_CLK_M7](#ga71d063d87af2e021db96f44c72d9e611)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M7 核心 时钟（Cortex-M7 core clock）。

<a id="r_ga4d4326b4f31df95619493a267b0faf4c"></a>

```c
#define IMX952_CLK_M7SYSTICK (IMX952_CCM_NUM_CLK_SRC + 55)
```

相关声明：[IMX952_CLK_M7SYSTICK](#ga4d4326b4f31df95619493a267b0faf4c)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Cortex-M7 SysTick 时钟（Cortex-M7 SysTick clock）。

<a id="r_gae52a0cc48000d0865742b08f072c7370"></a>

```c
#define IMX952_CLK_BUSNETCMIX (IMX952_CCM_NUM_CLK_SRC + 56)
```

相关声明：[IMX952_CLK_BUSNETCMIX](#gae52a0cc48000d0865742b08f072c7370)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

网络混合域 总线 时钟（Network mix bus clock）。

<a id="r_gab1af306d9110ef72fa5fdf25883da79b"></a>

```c
#define IMX952_CLK_ENET (IMX952_CCM_NUM_CLK_SRC + 57)
```

相关声明：[IMX952_CLK_ENET](#gab1af306d9110ef72fa5fdf25883da79b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 时钟（Ethernet clock）。

<a id="r_gacc5632392213d34c342965af3f709463"></a>

```c
#define IMX952_CLK_ENETPHYTEST200M (IMX952_CCM_NUM_CLK_SRC + 58)
```

相关声明：[IMX952_CLK_ENETPHYTEST200M](#gacc5632392213d34c342965af3f709463)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 200MHz 时钟（Ethernet PHY test 200MHz clock）。

<a id="r_ga5e18a17bbd01819729fbbd9f980b9c4a"></a>

```c
#define IMX952_CLK_ENETPHYTEST500M (IMX952_CCM_NUM_CLK_SRC + 59)
```

相关声明：[IMX952_CLK_ENETPHYTEST500M](#ga5e18a17bbd01819729fbbd9f980b9c4a)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 500MHz 时钟（Ethernet PHY test 500MHz clock）。

<a id="r_gadcf309e71ba8699ab9473fc0f6472afb"></a>

```c
#define IMX952_CLK_ENETPHYTEST667M (IMX952_CCM_NUM_CLK_SRC + 60)
```

相关声明：[IMX952_CLK_ENETPHYTEST667M](#gadcf309e71ba8699ab9473fc0f6472afb)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 PHY 测试 667MHz 时钟（Ethernet PHY test 667MHz clock）。

<a id="r_ga9fe95e36aa8fb3bac76a22bed8d6e968"></a>

```c
#define IMX952_CLK_ENETREF (IMX952_CCM_NUM_CLK_SRC + 61)
```

相关声明：[IMX952_CLK_ENETREF](#ga9fe95e36aa8fb3bac76a22bed8d6e968)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 参考 时钟（Ethernet reference clock）。

<a id="r_ga93e85bbc5951f6908f956f5c8d95e4d7"></a>

```c
#define IMX952_CLK_ENETTIMER1 (IMX952_CCM_NUM_CLK_SRC + 62)
```

相关声明：[IMX952_CLK_ENETTIMER1](#ga93e85bbc5951f6908f956f5c8d95e4d7)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

以太网 定时器 1 时钟（Ethernet timer 1 clock）。

<a id="r_ga58a267768b3191c2e01e7a18042950d8"></a>

```c
#define IMX952_CLK_RESERVED63 (IMX952_CCM_NUM_CLK_SRC + 63)
```

相关声明：[IMX952_CLK_RESERVED63](#ga58a267768b3191c2e01e7a18042950d8)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 63（Reserved peripheral clock 63）。

<a id="r_ga8f13732951eed83cecdac72b7180c4fa"></a>

```c
#define IMX952_CLK_SAI2 (IMX952_CCM_NUM_CLK_SRC + 64)
```

相关声明：[IMX952_CLK_SAI2](#ga8f13732951eed83cecdac72b7180c4fa)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI2 时钟（SAI2 clock）。

<a id="r_gadf0655cea3322c98c299982bb3a72b10"></a>

```c
#define IMX952_CLK_NOCAPB (IMX952_CCM_NUM_CLK_SRC + 65)
```

相关声明：[IMX952_CLK_NOCAPB](#gadf0655cea3322c98c299982bb3a72b10)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

NOC APB 时钟（NOC APB clock）。

<a id="r_gaf0b14b642cc622e4118566f980b2711b"></a>

```c
#define IMX952_CLK_NOC (IMX952_CCM_NUM_CLK_SRC + 66)
```

相关声明：[IMX952_CLK_NOC](#gaf0b14b642cc622e4118566f980b2711b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

片上网络 时钟（Network-on-chip clock）。

<a id="r_ga7679466832c15b9007ccbfd89f29399b"></a>

```c
#define IMX952_CLK_NPUAPB (IMX952_CCM_NUM_CLK_SRC + 67)
```

相关声明：[IMX952_CLK_NPUAPB](#ga7679466832c15b9007ccbfd89f29399b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

NPU APB 时钟（NPU APB clock）。

<a id="r_ga6c0826297d389a194d9c347e1dec2f3c"></a>

```c
#define IMX952_CLK_NPU (IMX952_CCM_NUM_CLK_SRC + 68)
```

相关声明：[IMX952_CLK_NPU](#ga6c0826297d389a194d9c347e1dec2f3c)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

神经网络处理单元 时钟（Neural processing unit clock）。

<a id="r_ga9e7e982eafba4ef8f087e86f09388dd1"></a>

```c
#define IMX952_CLK_CCMCKO1 (IMX952_CCM_NUM_CLK_SRC + 69)
```

相关声明：[IMX952_CLK_CCMCKO1](#ga9e7e982eafba4ef8f087e86f09388dd1)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 1（CCM clock output 1）。

<a id="r_ga0796739931db4bf6ca285dc9cef6442e"></a>

```c
#define IMX952_CLK_CCMCKO2 (IMX952_CCM_NUM_CLK_SRC + 70)
```

相关声明：[IMX952_CLK_CCMCKO2](#ga0796739931db4bf6ca285dc9cef6442e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 2（CCM clock output 2）。

<a id="r_ga7e163c133a4c737f00350698e800ced9"></a>

```c
#define IMX952_CLK_CCMCKO3 (IMX952_CCM_NUM_CLK_SRC + 71)
```

相关声明：[IMX952_CLK_CCMCKO3](#ga7e163c133a4c737f00350698e800ced9)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 3（CCM clock output 3）。

<a id="r_ga690093bbcb23e642d84b02b2a584db96"></a>

```c
#define IMX952_CLK_CCMCKO4 (IMX952_CCM_NUM_CLK_SRC + 72)
```

相关声明：[IMX952_CLK_CCMCKO4](#ga690093bbcb23e642d84b02b2a584db96)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CCM 时钟 输出 4（CCM clock output 4）。

<a id="r_ga06e617b155e10bead692b6681e06ce77"></a>

```c
#define IMX952_CLK_VPUAPB (IMX952_CCM_NUM_CLK_SRC + 73)
```

相关声明：[IMX952_CLK_VPUAPB](#ga06e617b155e10bead692b6681e06ce77)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

VPU APB 时钟（VPU APB clock）。

<a id="r_ga96a440ad719c4016207d3fefbeabbf6e"></a>

```c
#define IMX952_CLK_VPU (IMX952_CCM_NUM_CLK_SRC + 74)
```

相关声明：[IMX952_CLK_VPU](#ga96a440ad719c4016207d3fefbeabbf6e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

视频处理单元 时钟（Video processing unit clock）。

<a id="r_gae2d0ef4dcebbb0438c4a53856becc422"></a>

```c
#define IMX952_CLK_RESERVED75 (IMX952_CCM_NUM_CLK_SRC + 75)
```

相关声明：[IMX952_CLK_RESERVED75](#gae2d0ef4dcebbb0438c4a53856becc422)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 75（Reserved peripheral clock 75）。

<a id="r_gab9ce1f7a67d35b9aa91e4ccc0b221753"></a>

```c
#define IMX952_CLK_RESERVED76 (IMX952_CCM_NUM_CLK_SRC + 76)
```

相关声明：[IMX952_CLK_RESERVED76](#gab9ce1f7a67d35b9aa91e4ccc0b221753)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 76（Reserved peripheral clock 76）。

<a id="r_ga06b9b945d709ee18aaac219bc00c00b5"></a>

```c
#define IMX952_CLK_AUDIOXCVR (IMX952_CCM_NUM_CLK_SRC + 77)
```

相关声明：[IMX952_CLK_AUDIOXCVR](#ga06b9b945d709ee18aaac219bc00c00b5)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

音频收发器 时钟（Audio transceiver clock）。

<a id="r_gae001be70f9ee9e5dd3034168ac997357"></a>

```c
#define IMX952_CLK_BUSWAKEUP (IMX952_CCM_NUM_CLK_SRC + 78)
```

相关声明：[IMX952_CLK_BUSWAKEUP](#gae001be70f9ee9e5dd3034168ac997357)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

唤醒 总线 时钟（Wakeup bus clock）。

<a id="r_gad3cd5b7a2b34c6888809a8bf5588a9fe"></a>

```c
#define IMX952_CLK_CAN2 (IMX952_CCM_NUM_CLK_SRC + 79)
```

相关声明：[IMX952_CLK_CAN2](#gad3cd5b7a2b34c6888809a8bf5588a9fe)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN2 时钟（CAN2 clock）。

<a id="r_ga3965f0ca49447cef4bd6266baa4f203b"></a>

```c
#define IMX952_CLK_CAN3 (IMX952_CCM_NUM_CLK_SRC + 80)
```

相关声明：[IMX952_CLK_CAN3](#ga3965f0ca49447cef4bd6266baa4f203b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN3 时钟（CAN3 clock）。

<a id="r_ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d"></a>

```c
#define IMX952_CLK_CAN4 (IMX952_CCM_NUM_CLK_SRC + 81)
```

相关声明：[IMX952_CLK_CAN4](#ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN4 时钟（CAN4 clock）。

<a id="r_ga69c2d985644db8881a344d4d131ea4c8"></a>

```c
#define IMX952_CLK_CAN5 (IMX952_CCM_NUM_CLK_SRC + 82)
```

相关声明：[IMX952_CLK_CAN5](#ga69c2d985644db8881a344d4d131ea4c8)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

CAN5 时钟（CAN5 clock）。

<a id="r_ga1fcb9ea2063f15bf883bdec8c02e16b8"></a>

```c
#define IMX952_CLK_FLEXIO1 (IMX952_CCM_NUM_CLK_SRC + 83)
```

相关声明：[IMX952_CLK_FLEXIO1](#ga1fcb9ea2063f15bf883bdec8c02e16b8)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

FlexIO1 时钟（FlexIO1 clock）。

<a id="r_ga5dbb816f835529ef98f6a686294de54c"></a>

```c
#define IMX952_CLK_FLEXIO2 (IMX952_CCM_NUM_CLK_SRC + 84)
```

相关声明：[IMX952_CLK_FLEXIO2](#ga5dbb816f835529ef98f6a686294de54c)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

FlexIO2 时钟（FlexIO2 clock）。

<a id="r_gad9334abd1606ef0aaaf99220e69162e5"></a>

```c
#define IMX952_CLK_XSPI1 (IMX952_CCM_NUM_CLK_SRC + 85)
```

相关声明：[IMX952_CLK_XSPI1](#gad9334abd1606ef0aaaf99220e69162e5)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

就地执行 SPI 1 时钟（eXecute-in-place SPI 1 clock）。

<a id="r_ga48a75f83239ad51a9e9900d28a74f32d"></a>

```c
#define IMX952_CLK_RESERVED86 (IMX952_CCM_NUM_CLK_SRC + 86)
```

相关声明：[IMX952_CLK_RESERVED86](#ga48a75f83239ad51a9e9900d28a74f32d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

保留外设 时钟 86（Reserved peripheral clock 86）。

<a id="r_ga40f266412cf80cb111bd5b62089c74ac"></a>

```c
#define IMX952_CLK_I3C2SLOW (IMX952_CCM_NUM_CLK_SRC + 87)
```

相关声明：[IMX952_CLK_I3C2SLOW](#ga40f266412cf80cb111bd5b62089c74ac)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

I3C2 慢速 时钟（I3C2 slow clock）。

<a id="r_ga9927f113303645c1413f35382147b5a6"></a>

```c
#define IMX952_CLK_LPI2C3 (IMX952_CCM_NUM_CLK_SRC + 88)
```

相关声明：[IMX952_CLK_LPI2C3](#ga9927f113303645c1413f35382147b5a6)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C3 时钟（LPI2C3 clock）。

<a id="r_ga4b145aea4cf3032a42831d1c2a2a016b"></a>

```c
#define IMX952_CLK_LPI2C4 (IMX952_CCM_NUM_CLK_SRC + 89)
```

相关声明：[IMX952_CLK_LPI2C4](#ga4b145aea4cf3032a42831d1c2a2a016b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C4 时钟（LPI2C4 clock）。

<a id="r_ga340244c90568c62fa824ca8db2702b2e"></a>

```c
#define IMX952_CLK_LPI2C5 (IMX952_CCM_NUM_CLK_SRC + 90)
```

相关声明：[IMX952_CLK_LPI2C5](#ga340244c90568c62fa824ca8db2702b2e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C5 时钟（LPI2C5 clock）。

<a id="r_gae066026bf708d6ac46263a0a7ca23d24"></a>

```c
#define IMX952_CLK_LPI2C6 (IMX952_CCM_NUM_CLK_SRC + 91)
```

相关声明：[IMX952_CLK_LPI2C6](#gae066026bf708d6ac46263a0a7ca23d24)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C6 时钟（LPI2C6 clock）。

<a id="r_gae00eff47c6398a00f256caa56efa55f3"></a>

```c
#define IMX952_CLK_LPI2C7 (IMX952_CCM_NUM_CLK_SRC + 92)
```

相关声明：[IMX952_CLK_LPI2C7](#gae00eff47c6398a00f256caa56efa55f3)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C7 时钟（LPI2C7 clock）。

<a id="r_ga7a200fa7987ac930c8a5f3dbd1e74c81"></a>

```c
#define IMX952_CLK_LPI2C8 (IMX952_CCM_NUM_CLK_SRC + 93)
```

相关声明：[IMX952_CLK_LPI2C8](#ga7a200fa7987ac930c8a5f3dbd1e74c81)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPI2C8 时钟（LPI2C8 clock）。

<a id="r_ga3ab3fe70ad0fdd8c80069fc17867972b"></a>

```c
#define IMX952_CLK_LPSPI3 (IMX952_CCM_NUM_CLK_SRC + 94)
```

相关声明：[IMX952_CLK_LPSPI3](#ga3ab3fe70ad0fdd8c80069fc17867972b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI3 时钟（LPSPI3 clock）。

<a id="r_ga76b045cd9c12e41886306964791f46ec"></a>

```c
#define IMX952_CLK_LPSPI4 (IMX952_CCM_NUM_CLK_SRC + 95)
```

相关声明：[IMX952_CLK_LPSPI4](#ga76b045cd9c12e41886306964791f46ec)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI4 时钟（LPSPI4 clock）。

<a id="r_ga13516d021d6a4062fb31f124e3ee72a4"></a>

```c
#define IMX952_CLK_LPSPI5 (IMX952_CCM_NUM_CLK_SRC + 96)
```

相关声明：[IMX952_CLK_LPSPI5](#ga13516d021d6a4062fb31f124e3ee72a4)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI5 时钟（LPSPI5 clock）。

<a id="r_ga30dac0d2cb4c13dc914d950678ae7ff4"></a>

```c
#define IMX952_CLK_LPSPI6 (IMX952_CCM_NUM_CLK_SRC + 97)
```

相关声明：[IMX952_CLK_LPSPI6](#ga30dac0d2cb4c13dc914d950678ae7ff4)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI6 时钟（LPSPI6 clock）。

<a id="r_gac4f02540f9cf0a12dfe94ddfbdb2bfc3"></a>

```c
#define IMX952_CLK_LPSPI7 (IMX952_CCM_NUM_CLK_SRC + 98)
```

相关声明：[IMX952_CLK_LPSPI7](#gac4f02540f9cf0a12dfe94ddfbdb2bfc3)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI7 时钟（LPSPI7 clock）。

<a id="r_ga7e0f66376ddfa8d14689be5b1cc2f58d"></a>

```c
#define IMX952_CLK_LPSPI8 (IMX952_CCM_NUM_CLK_SRC + 99)
```

相关声明：[IMX952_CLK_LPSPI8](#ga7e0f66376ddfa8d14689be5b1cc2f58d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPSPI8 时钟（LPSPI8 clock）。

<a id="r_ga5a20f1157eb6e8204a4d0ada3aa82c89"></a>

```c
#define IMX952_CLK_LPTMR2 (IMX952_CCM_NUM_CLK_SRC + 100)
```

相关声明：[IMX952_CLK_LPTMR2](#ga5a20f1157eb6e8204a4d0ada3aa82c89)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPTMR2 时钟（LPTMR2 clock）。

<a id="r_gae58fc80ca785f07f5495230941815f7a"></a>

```c
#define IMX952_CLK_LPUART3 (IMX952_CCM_NUM_CLK_SRC + 101)
```

相关声明：[IMX952_CLK_LPUART3](#gae58fc80ca785f07f5495230941815f7a)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART3 时钟（LPUART3 clock）。

<a id="r_ga5653005f43f816acfa66ded30325a562"></a>

```c
#define IMX952_CLK_LPUART4 (IMX952_CCM_NUM_CLK_SRC + 102)
```

相关声明：[IMX952_CLK_LPUART4](#ga5653005f43f816acfa66ded30325a562)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART4 时钟（LPUART4 clock）。

<a id="r_gaeb992d7eaf2505cede034795536bdf37"></a>

```c
#define IMX952_CLK_LPUART5 (IMX952_CCM_NUM_CLK_SRC + 103)
```

相关声明：[IMX952_CLK_LPUART5](#gaeb992d7eaf2505cede034795536bdf37)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART5 时钟（LPUART5 clock）。

<a id="r_gae23f66d12251642ef39b1641b261f3af"></a>

```c
#define IMX952_CLK_LPUART6 (IMX952_CCM_NUM_CLK_SRC + 104)
```

相关声明：[IMX952_CLK_LPUART6](#gae23f66d12251642ef39b1641b261f3af)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART6 时钟（LPUART6 clock）。

<a id="r_ga270a616ad346393cc4c45a0645f2219d"></a>

```c
#define IMX952_CLK_LPUART7 (IMX952_CCM_NUM_CLK_SRC + 105)
```

相关声明：[IMX952_CLK_LPUART7](#ga270a616ad346393cc4c45a0645f2219d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART7 时钟（LPUART7 clock）。

<a id="r_gaff08699e35d25bd1dc758fcae970fc3e"></a>

```c
#define IMX952_CLK_LPUART8 (IMX952_CCM_NUM_CLK_SRC + 106)
```

相关声明：[IMX952_CLK_LPUART8](#gaff08699e35d25bd1dc758fcae970fc3e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

LPUART8 时钟（LPUART8 clock）。

<a id="r_gab86838fbcfa36a15bfb30241e811d4df"></a>

```c
#define IMX952_CLK_SAI3 (IMX952_CCM_NUM_CLK_SRC + 107)
```

相关声明：[IMX952_CLK_SAI3](#gab86838fbcfa36a15bfb30241e811d4df)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI3 时钟（SAI3 clock）。

<a id="r_ga4ec095c742bfdcc954b83d8c13aa1f95"></a>

```c
#define IMX952_CLK_SAI4 (IMX952_CCM_NUM_CLK_SRC + 108)
```

相关声明：[IMX952_CLK_SAI4](#ga4ec095c742bfdcc954b83d8c13aa1f95)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI4 时钟（SAI4 clock）。

<a id="r_gada66056d7a864b3a7fb73758d1f401e2"></a>

```c
#define IMX952_CLK_SAI5 (IMX952_CCM_NUM_CLK_SRC + 109)
```

相关声明：[IMX952_CLK_SAI5](#gada66056d7a864b3a7fb73758d1f401e2)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SAI5 时钟（SAI5 clock）。

<a id="r_ga879119b0739e90c08dfb21d89c58be8e"></a>

```c
#define IMX952_CLK_SPDIF (IMX952_CCM_NUM_CLK_SRC + 110)
```

相关声明：[IMX952_CLK_SPDIF](#ga879119b0739e90c08dfb21d89c58be8e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

S/PDIF 时钟（S/PDIF clock）。

<a id="r_ga743096ff4fa6975b7dac8f10584643ad"></a>

```c
#define IMX952_CLK_SWOTRACE (IMX952_CCM_NUM_CLK_SRC + 111)
```

相关声明：[IMX952_CLK_SWOTRACE](#ga743096ff4fa6975b7dac8f10584643ad)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

SWO 跟踪 时钟（SWO trace clock）。

<a id="r_gaef0ff808e6b781fa505dab10bc4fa51b"></a>

```c
#define IMX952_CLK_TPM4 (IMX952_CCM_NUM_CLK_SRC + 112)
```

相关声明：[IMX952_CLK_TPM4](#gaef0ff808e6b781fa505dab10bc4fa51b)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM4 时钟（TPM4 clock）。

<a id="r_gadd0bb62c169c44e38fffed5c08e66914"></a>

```c
#define IMX952_CLK_TPM5 (IMX952_CCM_NUM_CLK_SRC + 113)
```

相关声明：[IMX952_CLK_TPM5](#gadd0bb62c169c44e38fffed5c08e66914)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM5 时钟（TPM5 clock）。

<a id="r_ga263cf3ea860bfb247fdb40d8db63fcc3"></a>

```c
#define IMX952_CLK_TPM6 (IMX952_CCM_NUM_CLK_SRC + 114)
```

相关声明：[IMX952_CLK_TPM6](#ga263cf3ea860bfb247fdb40d8db63fcc3)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

TPM6 时钟（TPM6 clock）。

<a id="r_ga682869be4456f0e4502e2035e8dc9903"></a>

```c
#define IMX952_CLK_TSTMR2 (IMX952_CCM_NUM_CLK_SRC + 115)
```

相关声明：[IMX952_CLK_TSTMR2](#ga682869be4456f0e4502e2035e8dc9903)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Timestamp 定时器 2 时钟（Timestamp timer 2 clock）。

<a id="r_gaa073d854720457424d9c59efa414c998"></a>

```c
#define IMX952_CLK_USBPHYBURUNIN (IMX952_CCM_NUM_CLK_SRC + 116)
```

相关声明：[IMX952_CLK_USBPHYBURUNIN](#gaa073d854720457424d9c59efa414c998)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

USB PHY 老化测试 时钟（USB PHY burn-in clock）。

<a id="r_ga708f630fb04d80884836308c55e7478f"></a>

```c
#define IMX952_CLK_USDHC1 (IMX952_CCM_NUM_CLK_SRC + 117)
```

相关声明：[IMX952_CLK_USDHC1](#ga708f630fb04d80884836308c55e7478f)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC1 时钟（uSDHC1 clock）。

<a id="r_ga55b06e78fcbeda0b95541b9c75e43fac"></a>

```c
#define IMX952_CLK_USDHC2 (IMX952_CCM_NUM_CLK_SRC + 118)
```

相关声明：[IMX952_CLK_USDHC2](#ga55b06e78fcbeda0b95541b9c75e43fac)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC2 时钟（uSDHC2 clock）。

<a id="r_ga2c9789e768474a24203d85e0dfc4a43a"></a>

```c
#define IMX952_CLK_USDHC3 (IMX952_CCM_NUM_CLK_SRC + 119)
```

相关声明：[IMX952_CLK_USDHC3](#ga2c9789e768474a24203d85e0dfc4a43a)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

uSDHC3 时钟（uSDHC3 clock）。

<a id="r_ga79ee5f43bbd83b132a8d5a072a92aa14"></a>

```c
#define IMX952_CLK_V2XPK (IMX952_CCM_NUM_CLK_SRC + 120)
```

相关声明：[IMX952_CLK_V2XPK](#ga79ee5f43bbd83b132a8d5a072a92aa14)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

V2X 数据包引擎 时钟（V2X packet engine clock）。

<a id="r_ga34a721794435930c4491b4dea37fd8a3"></a>

```c
#define IMX952_CLK_WAKEUPAXI (IMX952_CCM_NUM_CLK_SRC + 121)
```

相关声明：[IMX952_CLK_WAKEUPAXI](#ga34a721794435930c4491b4dea37fd8a3)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

唤醒 AXI 时钟（Wakeup AXI clock）。

<a id="r_gacfb4422e38d4b3b1a28d06d7779264db"></a>

```c
#define IMX952_CLK_XSPISLVROOT (IMX952_CCM_NUM_CLK_SRC + 122)
```

相关声明：[IMX952_CLK_XSPISLVROOT](#gacfb4422e38d4b3b1a28d06d7779264db)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

XPI slave root 时钟（XPI slave root clock）。

<a id="r_gafb3ba58ee46ab0e69b617626f083c332"></a>

```c
#define IMX952_CLK_AUDMIX1 (IMX952_CCM_NUM_CLK_SRC + 123)
```

相关声明：[IMX952_CLK_AUDMIX1](#gafb3ba58ee46ab0e69b617626f083c332)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Audio Mixer 1 时钟（Audio Mixer 1 clock）。

<a id="r_ga4accc64cecdd4ea562951b65e0fbc813"></a>

```c
#define IMX952_CLK_ASRC1 (IMX952_CCM_NUM_CLK_SRC + 124)
```

相关声明：[IMX952_CLK_ASRC1](#ga4accc64cecdd4ea562951b65e0fbc813)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Asynchronous Sample Rate Converter 1 时钟（Asynchronous Sample Rate Converter 1 clock）。

<a id="r_gaeaa32e8ac4c23850897e39599db1efe9"></a>

```c
#define IMX952_CLK_ASRC2 (IMX952_CCM_NUM_CLK_SRC + 125)
```

相关声明：[IMX952_CLK_ASRC2](#gaeaa32e8ac4c23850897e39599db1efe9)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

Asynchronous Sample Rate Converter 2 时钟（Asynchronous Sample Rate Converter 2 clock）。

<a id="r_ga982ed68fc9c8f3fbe1615d6005870c55"></a>

```c
#define IMX952_CLK_GPT2 (IMX952_CCM_NUM_CLK_SRC + 126)
```

相关声明：[IMX952_CLK_GPT2](#ga982ed68fc9c8f3fbe1615d6005870c55)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 2 时钟（General Purpose Timer 2 clock）。

<a id="r_ga01dea83a9c18afc152aae5701c07d20d"></a>

```c
#define IMX952_CLK_GPT3 (IMX952_CCM_NUM_CLK_SRC + 127)
```

相关声明：[IMX952_CLK_GPT3](#ga01dea83a9c18afc152aae5701c07d20d)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 3 时钟（General Purpose Timer 3 clock）。

<a id="r_ga303d0f829e212027c9875fa3e7803a6e"></a>

```c
#define IMX952_CLK_GPT4 (IMX952_CCM_NUM_CLK_SRC + 128)
```

相关声明：[IMX952_CLK_GPT4](#ga303d0f829e212027c9875fa3e7803a6e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 4 时钟（General Purpose Timer 4 clock）。

<a id="r_gad5de7aa86c7849e87978870e642e765e"></a>

```c
#define IMX952_CLK_GPT5 (IMX952_CCM_NUM_CLK_SRC + 129)
```

相关声明：[IMX952_CLK_GPT5](#gad5de7aa86c7849e87978870e642e765e)、[IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)。

General Purpose Timer 5 时钟（General Purpose Timer 5 clock）。

## 8.2\_详细说明（Detailed Documentation）

<a id="gae927a53c34c5d1fcb6c4e7d6f5a2dbf2"></a>

### `IMX952_CLK_A55`

```c
#define IMX952_CLK_A55 (IMX952_CCM_NUM_CLK_SRC + 29)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-A55 核心 时钟（Cortex-A55 core clock）。

<a id="gaf97b4deb07b00e3d70b1ac3cf6604486"></a>

### `IMX952_CLK_A55MTRBUS`

```c
#define IMX952_CLK_A55MTRBUS (IMX952_CCM_NUM_CLK_SRC + 30)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-A55 MTR 总线 时钟（Cortex-A55 MTR bus clock）。

<a id="gad07cd50a19b3edea126a948af250e0e0"></a>

### `IMX952_CLK_A55PERIPH`

```c
#define IMX952_CLK_A55PERIPH (IMX952_CCM_NUM_CLK_SRC + 31)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-A55 外设 时钟（Cortex-A55 peripheral clock）。

<a id="gadd6d1896e8c854ea655c6149753054b2"></a>

### `IMX952_CLK_ADC`

```c
#define IMX952_CLK_ADC (IMX952_CCM_NUM_CLK_SRC + 0)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

ADC 时钟（Clock）。

<a id="ga4accc64cecdd4ea562951b65e0fbc813"></a>

### `IMX952_CLK_ASRC1`

```c
#define IMX952_CLK_ASRC1 (IMX952_CCM_NUM_CLK_SRC + 124)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Asynchronous Sample Rate Converter 1 时钟（Asynchronous Sample Rate Converter 1 clock）。

<a id="gaeaa32e8ac4c23850897e39599db1efe9"></a>

### `IMX952_CLK_ASRC2`

```c
#define IMX952_CLK_ASRC2 (IMX952_CCM_NUM_CLK_SRC + 125)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Asynchronous Sample Rate Converter 2 时钟（Asynchronous Sample Rate Converter 2 clock）。

<a id="ga06b9b945d709ee18aaac219bc00c00b5"></a>

### `IMX952_CLK_AUDIOXCVR`

```c
#define IMX952_CLK_AUDIOXCVR (IMX952_CCM_NUM_CLK_SRC + 77)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

音频收发器 时钟（Audio transceiver clock）。

<a id="gafb3ba58ee46ab0e69b617626f083c332"></a>

### `IMX952_CLK_AUDMIX1`

```c
#define IMX952_CLK_AUDMIX1 (IMX952_CCM_NUM_CLK_SRC + 123)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Audio Mixer 1 时钟（Audio Mixer 1 clock）。

<a id="ga3c9d2874480a9a3742b81aa64657d5a0"></a>

### `IMX952_CLK_BUSAON`

```c
#define IMX952_CLK_BUSAON (IMX952_CCM_NUM_CLK_SRC + 2)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

AON 总线 时钟（AON bus clock）。

<a id="ga400485d6af68996afc3a86eabb9074f8"></a>

### `IMX952_CLK_BUSM7`

```c
#define IMX952_CLK_BUSM7 (IMX952_CCM_NUM_CLK_SRC + 53)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

M7 总线 时钟（M7 bus clock）。

<a id="gae52a0cc48000d0865742b08f072c7370"></a>

### `IMX952_CLK_BUSNETCMIX`

```c
#define IMX952_CLK_BUSNETCMIX (IMX952_CCM_NUM_CLK_SRC + 56)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

网络混合域 总线 时钟（Network mix bus clock）。

<a id="gae001be70f9ee9e5dd3034168ac997357"></a>

### `IMX952_CLK_BUSWAKEUP`

```c
#define IMX952_CLK_BUSWAKEUP (IMX952_CCM_NUM_CLK_SRC + 78)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

唤醒 总线 时钟（Wakeup bus clock）。

<a id="ga04d79491636ed5a37b9b4ae801066574"></a>

### `IMX952_CLK_CAMAPB`

```c
#define IMX952_CLK_CAMAPB (IMX952_CCM_NUM_CLK_SRC + 21)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

摄像头 APB 时钟（Camera APB clock）。

<a id="ga09fffe1b5527547c20667290b422e7de"></a>

### `IMX952_CLK_CAMAXI`

```c
#define IMX952_CLK_CAMAXI (IMX952_CCM_NUM_CLK_SRC + 22)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

摄像头 AXI 时钟（Camera AXI clock）。

<a id="ga3dbac1b1a9e7e6c644ee140c96bbf81f"></a>

### `IMX952_CLK_CAMCM0`

```c
#define IMX952_CLK_CAMCM0 (IMX952_CCM_NUM_CLK_SRC + 23)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

摄像头 CM0 时钟（Camera CM0 clock）。

<a id="ga19837041e27ed67e9e6df73716fc9d54"></a>

### `IMX952_CLK_CAMISI`

```c
#define IMX952_CLK_CAMISI (IMX952_CCM_NUM_CLK_SRC + 24)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

摄像头 ISI 时钟（Camera ISI clock）。

<a id="ga586eb4045847dbe332d8575acf99f3be"></a>

### `IMX952_CLK_CAMPHYCFG`

```c
#define IMX952_CLK_CAMPHYCFG (IMX952_CCM_NUM_CLK_SRC + 25)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

摄像头 PHY 配置 时钟（Camera PHY configuration clock）。

<a id="gafe7b5204c752fa2dfc45abbe9ef56b1b"></a>

### `IMX952_CLK_CAN1`

```c
#define IMX952_CLK_CAN1 (IMX952_CCM_NUM_CLK_SRC + 3)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CAN1 时钟（CAN1 clock）。

<a id="gad3cd5b7a2b34c6888809a8bf5588a9fe"></a>

### `IMX952_CLK_CAN2`

```c
#define IMX952_CLK_CAN2 (IMX952_CCM_NUM_CLK_SRC + 79)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CAN2 时钟（CAN2 clock）。

<a id="ga3965f0ca49447cef4bd6266baa4f203b"></a>

### `IMX952_CLK_CAN3`

```c
#define IMX952_CLK_CAN3 (IMX952_CCM_NUM_CLK_SRC + 80)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CAN3 时钟（CAN3 clock）。

<a id="ga56ae00ef8a1ba6dab63a9f7cdd5a3d6d"></a>

### `IMX952_CLK_CAN4`

```c
#define IMX952_CLK_CAN4 (IMX952_CCM_NUM_CLK_SRC + 81)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CAN4 时钟（CAN4 clock）。

<a id="ga69c2d985644db8881a344d4d131ea4c8"></a>

### `IMX952_CLK_CAN5`

```c
#define IMX952_CLK_CAN5 (IMX952_CCM_NUM_CLK_SRC + 82)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CAN5 时钟（CAN5 clock）。

<a id="ga9e7e982eafba4ef8f087e86f09388dd1"></a>

### `IMX952_CLK_CCMCKO1`

```c
#define IMX952_CLK_CCMCKO1 (IMX952_CCM_NUM_CLK_SRC + 69)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CCM 时钟 输出 1（CCM clock output 1）。

<a id="ga0796739931db4bf6ca285dc9cef6442e"></a>

### `IMX952_CLK_CCMCKO2`

```c
#define IMX952_CLK_CCMCKO2 (IMX952_CCM_NUM_CLK_SRC + 70)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CCM 时钟 输出 2（CCM clock output 2）。

<a id="ga7e163c133a4c737f00350698e800ced9"></a>

### `IMX952_CLK_CCMCKO3`

```c
#define IMX952_CLK_CCMCKO3 (IMX952_CCM_NUM_CLK_SRC + 71)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CCM 时钟 输出 3（CCM clock output 3）。

<a id="ga690093bbcb23e642d84b02b2a584db96"></a>

### `IMX952_CLK_CCMCKO4`

```c
#define IMX952_CLK_CCMCKO4 (IMX952_CCM_NUM_CLK_SRC + 72)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

CCM 时钟 输出 4（CCM clock output 4）。

<a id="gabde7224b0230770740576871301f72a4"></a>

### `IMX952_CLK_DISP1PIX`

```c
#define IMX952_CLK_DISP1PIX (IMX952_CCM_NUM_CLK_SRC + 39)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 1 像素 时钟（Display 1 pixel clock）。

<a id="ga0439a95f09f1f498b45f4cf51ceb8983"></a>

### `IMX952_CLK_DISPAPB`

```c
#define IMX952_CLK_DISPAPB (IMX952_CCM_NUM_CLK_SRC + 34)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 APB 时钟（Display APB clock）。

<a id="gae7bdf479b9aea05d0c99afa3e08c56ee"></a>

### `IMX952_CLK_DISPAXI`

```c
#define IMX952_CLK_DISPAXI (IMX952_CCM_NUM_CLK_SRC + 35)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 AXI 时钟（Display AXI clock）。

<a id="ga4885eba2f05bd15129c8d732d06195b6"></a>

### `IMX952_CLK_DISPCDPHYAPB`

```c
#define IMX952_CLK_DISPCDPHYAPB (IMX952_CCM_NUM_CLK_SRC + 40)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 CD PHY APB 时钟（Display CD PHY APB clock）。

<a id="gad866759ea1a19d4b38335a722dc36bb1"></a>

### `IMX952_CLK_DISPHYCFG`

```c
#define IMX952_CLK_DISPHYCFG (IMX952_CCM_NUM_CLK_SRC + 38)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 PHY 配置 时钟（Display PHY configuration clock）。

<a id="ga5a19ad3418eea5aedbbf72aa1b073a4b"></a>

### `IMX952_CLK_DISPLPSPI`

```c
#define IMX952_CLK_DISPLPSPI (IMX952_CCM_NUM_CLK_SRC + 36)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 LPSPI 时钟（Display LPSPI clock）。

<a id="ga5cce1fd12ca390ad1b345813797d51bb"></a>

### `IMX952_CLK_DISPOCRAM`

```c
#define IMX952_CLK_DISPOCRAM (IMX952_CCM_NUM_CLK_SRC + 37)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

显示 OCRAM 时钟（Display OCRAM clock）。

<a id="ga1de7bf9d1d6864c6d7f5b09de6d742c5"></a>

### `IMX952_CLK_DRAMALT`

```c
#define IMX952_CLK_DRAMALT (IMX952_CCM_NUM_CLK_SRC + 32)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

DRAM 备用 时钟（DRAM alternate clock）。

<a id="ga4fc0088507462042656a34a6bf430dfb"></a>

### `IMX952_CLK_DRAMAPB`

```c
#define IMX952_CLK_DRAMAPB (IMX952_CCM_NUM_CLK_SRC + 33)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

DRAM APB 时钟（DRAM APB clock）。

<a id="gab1af306d9110ef72fa5fdf25883da79b"></a>

### `IMX952_CLK_ENET`

```c
#define IMX952_CLK_ENET (IMX952_CCM_NUM_CLK_SRC + 57)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 时钟（Ethernet clock）。

<a id="gacc5632392213d34c342965af3f709463"></a>

### `IMX952_CLK_ENETPHYTEST200M`

```c
#define IMX952_CLK_ENETPHYTEST200M (IMX952_CCM_NUM_CLK_SRC + 58)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 PHY 测试 200MHz 时钟（Ethernet PHY test 200MHz clock）。

<a id="ga5e18a17bbd01819729fbbd9f980b9c4a"></a>

### `IMX952_CLK_ENETPHYTEST500M`

```c
#define IMX952_CLK_ENETPHYTEST500M (IMX952_CCM_NUM_CLK_SRC + 59)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 PHY 测试 500MHz 时钟（Ethernet PHY test 500MHz clock）。

<a id="gadcf309e71ba8699ab9473fc0f6472afb"></a>

### `IMX952_CLK_ENETPHYTEST667M`

```c
#define IMX952_CLK_ENETPHYTEST667M (IMX952_CCM_NUM_CLK_SRC + 60)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 PHY 测试 667MHz 时钟（Ethernet PHY test 667MHz clock）。

<a id="ga9fe95e36aa8fb3bac76a22bed8d6e968"></a>

### `IMX952_CLK_ENETREF`

```c
#define IMX952_CLK_ENETREF (IMX952_CCM_NUM_CLK_SRC + 61)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 参考 时钟（Ethernet reference clock）。

<a id="ga93e85bbc5951f6908f956f5c8d95e4d7"></a>

### `IMX952_CLK_ENETTIMER1`

```c
#define IMX952_CLK_ENETTIMER1 (IMX952_CCM_NUM_CLK_SRC + 62)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

以太网 定时器 1 时钟（Ethernet timer 1 clock）。

<a id="ga1fcb9ea2063f15bf883bdec8c02e16b8"></a>

### `IMX952_CLK_FLEXIO1`

```c
#define IMX952_CLK_FLEXIO1 (IMX952_CCM_NUM_CLK_SRC + 83)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

FlexIO1 时钟（FlexIO1 clock）。

<a id="ga5dbb816f835529ef98f6a686294de54c"></a>

### `IMX952_CLK_FLEXIO2`

```c
#define IMX952_CLK_FLEXIO2 (IMX952_CCM_NUM_CLK_SRC + 84)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

FlexIO2 时钟（FlexIO2 clock）。

<a id="ga982ed68fc9c8f3fbe1615d6005870c55"></a>

### `IMX952_CLK_GPT2`

```c
#define IMX952_CLK_GPT2 (IMX952_CCM_NUM_CLK_SRC + 126)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

General Purpose Timer 2 时钟（General Purpose Timer 2 clock）。

<a id="ga01dea83a9c18afc152aae5701c07d20d"></a>

### `IMX952_CLK_GPT3`

```c
#define IMX952_CLK_GPT3 (IMX952_CCM_NUM_CLK_SRC + 127)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

General Purpose Timer 3 时钟（General Purpose Timer 3 clock）。

<a id="ga303d0f829e212027c9875fa3e7803a6e"></a>

### `IMX952_CLK_GPT4`

```c
#define IMX952_CLK_GPT4 (IMX952_CCM_NUM_CLK_SRC + 128)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

General Purpose Timer 4 时钟（General Purpose Timer 4 clock）。

<a id="gad5de7aa86c7849e87978870e642e765e"></a>

### `IMX952_CLK_GPT5`

```c
#define IMX952_CLK_GPT5 (IMX952_CCM_NUM_CLK_SRC + 129)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

General Purpose Timer 5 时钟（General Purpose Timer 5 clock）。

<a id="ga24c41790fa58c6bf9b2170e23e0c56f0"></a>

### `IMX952_CLK_GPU`

```c
#define IMX952_CLK_GPU (IMX952_CCM_NUM_CLK_SRC + 43)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

GPU 核心 时钟（GPU core clock）。

<a id="ga8b41919d03a6d77af5f4997b63899159"></a>

### `IMX952_CLK_GPUAPB`

```c
#define IMX952_CLK_GPUAPB (IMX952_CCM_NUM_CLK_SRC + 42)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

GPU APB 时钟（GPU APB clock）。

<a id="gaa79e6a0b67c4c3d2059821cf6304f94b"></a>

### `IMX952_CLK_HSIO`

```c
#define IMX952_CLK_HSIO (IMX952_CCM_NUM_CLK_SRC + 46)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO 总线 时钟（HSIO bus clock）。

<a id="ga20f1a2162bf9ce0b5e0b2fe2db0075c5"></a>

### `IMX952_CLK_HSIOACSCAN480M`

```c
#define IMX952_CLK_HSIOACSCAN480M (IMX952_CCM_NUM_CLK_SRC + 44)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO AC 扫描 480MHz 时钟（HSIO AC scan 480MHz clock）。

<a id="ga1b77d6c93474b9bee9cf2691c2e38d91"></a>

### `IMX952_CLK_HSIOACSCAN80M`

```c
#define IMX952_CLK_HSIOACSCAN80M (IMX952_CCM_NUM_CLK_SRC + 45)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO AC 扫描 80MHz 时钟（HSIO AC scan 80MHz clock）。

<a id="gae3c37de19e68fc80164646d9f18aca67"></a>

### `IMX952_CLK_HSIOPCIEAUX`

```c
#define IMX952_CLK_HSIOPCIEAUX (IMX952_CCM_NUM_CLK_SRC + 47)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PCIe 辅助 时钟（HSIO PCIe auxiliary clock）。

<a id="gaf9f80c9df9203ac548d36c2eef2e074b"></a>

### `IMX952_CLK_HSIOPCIETEST160M`

```c
#define IMX952_CLK_HSIOPCIETEST160M (IMX952_CCM_NUM_CLK_SRC + 48)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PCIe 测试 160MHz 时钟（HSIO PCIe test 160MHz clock）。

<a id="ga656c3a598cc01dd56074ba178f4dd564"></a>

### `IMX952_CLK_HSIOPCIETEST400M`

```c
#define IMX952_CLK_HSIOPCIETEST400M (IMX952_CCM_NUM_CLK_SRC + 49)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PCIe 测试 400MHz 时钟（HSIO PCIe test 400MHz clock）。

<a id="gaf090ef87122451cc2c235950be7e7b86"></a>

### `IMX952_CLK_HSIOPCIETEST500M`

```c
#define IMX952_CLK_HSIOPCIETEST500M (IMX952_CCM_NUM_CLK_SRC + 50)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO PCIe 测试 500MHz 时钟（HSIO PCIe test 500MHz clock）。

<a id="gafecfa87e99167f088cc489dae90a4173"></a>

### `IMX952_CLK_HSIOUSBTEST50M`

```c
#define IMX952_CLK_HSIOUSBTEST50M (IMX952_CCM_NUM_CLK_SRC + 51)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO USB 测试 50MHz 时钟（HSIO USB test 50MHz clock）。

<a id="gafadaf0326bf74a16cb1f58060fe3ce03"></a>

### `IMX952_CLK_HSIOUSBTEST60M`

```c
#define IMX952_CLK_HSIOUSBTEST60M (IMX952_CCM_NUM_CLK_SRC + 52)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

HSIO USB 测试 60MHz 时钟（HSIO USB test 60MHz clock）。

<a id="gad356191a96c27cb2c84bb54fded38075"></a>

### `IMX952_CLK_I3C1SLOW`

```c
#define IMX952_CLK_I3C1SLOW (IMX952_CCM_NUM_CLK_SRC + 5)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

I3C1 慢速 时钟（I3C1 slow clock）。

<a id="ga40f266412cf80cb111bd5b62089c74ac"></a>

### `IMX952_CLK_I3C2SLOW`

```c
#define IMX952_CLK_I3C2SLOW (IMX952_CCM_NUM_CLK_SRC + 87)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

I3C2 慢速 时钟（I3C2 slow clock）。

<a id="gad2e8978ebfc8b671c2b0ad9d404be7d4"></a>

### `IMX952_CLK_LPI2C1`

```c
#define IMX952_CLK_LPI2C1 (IMX952_CCM_NUM_CLK_SRC + 6)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C1 时钟（LPI2C1 clock）。

<a id="ga41460f3425b5258f3936a4c05f9774ed"></a>

### `IMX952_CLK_LPI2C2`

```c
#define IMX952_CLK_LPI2C2 (IMX952_CCM_NUM_CLK_SRC + 7)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C2 时钟（LPI2C2 clock）。

<a id="ga9927f113303645c1413f35382147b5a6"></a>

### `IMX952_CLK_LPI2C3`

```c
#define IMX952_CLK_LPI2C3 (IMX952_CCM_NUM_CLK_SRC + 88)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C3 时钟（LPI2C3 clock）。

<a id="ga4b145aea4cf3032a42831d1c2a2a016b"></a>

### `IMX952_CLK_LPI2C4`

```c
#define IMX952_CLK_LPI2C4 (IMX952_CCM_NUM_CLK_SRC + 89)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C4 时钟（LPI2C4 clock）。

<a id="ga340244c90568c62fa824ca8db2702b2e"></a>

### `IMX952_CLK_LPI2C5`

```c
#define IMX952_CLK_LPI2C5 (IMX952_CCM_NUM_CLK_SRC + 90)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C5 时钟（LPI2C5 clock）。

<a id="gae066026bf708d6ac46263a0a7ca23d24"></a>

### `IMX952_CLK_LPI2C6`

```c
#define IMX952_CLK_LPI2C6 (IMX952_CCM_NUM_CLK_SRC + 91)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C6 时钟（LPI2C6 clock）。

<a id="gae00eff47c6398a00f256caa56efa55f3"></a>

### `IMX952_CLK_LPI2C7`

```c
#define IMX952_CLK_LPI2C7 (IMX952_CCM_NUM_CLK_SRC + 92)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C7 时钟（LPI2C7 clock）。

<a id="ga7a200fa7987ac930c8a5f3dbd1e74c81"></a>

### `IMX952_CLK_LPI2C8`

```c
#define IMX952_CLK_LPI2C8 (IMX952_CCM_NUM_CLK_SRC + 93)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPI2C8 时钟（LPI2C8 clock）。

<a id="ga03ef430f1aa454c4a765f540064045d4"></a>

### `IMX952_CLK_LPSPI1`

```c
#define IMX952_CLK_LPSPI1 (IMX952_CCM_NUM_CLK_SRC + 8)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI1 时钟（LPSPI1 clock）。

<a id="ga72914bea56dffea39955b80a363aea68"></a>

### `IMX952_CLK_LPSPI2`

```c
#define IMX952_CLK_LPSPI2 (IMX952_CCM_NUM_CLK_SRC + 9)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI2 时钟（LPSPI2 clock）。

<a id="ga3ab3fe70ad0fdd8c80069fc17867972b"></a>

### `IMX952_CLK_LPSPI3`

```c
#define IMX952_CLK_LPSPI3 (IMX952_CCM_NUM_CLK_SRC + 94)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI3 时钟（LPSPI3 clock）。

<a id="ga76b045cd9c12e41886306964791f46ec"></a>

### `IMX952_CLK_LPSPI4`

```c
#define IMX952_CLK_LPSPI4 (IMX952_CCM_NUM_CLK_SRC + 95)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI4 时钟（LPSPI4 clock）。

<a id="ga13516d021d6a4062fb31f124e3ee72a4"></a>

### `IMX952_CLK_LPSPI5`

```c
#define IMX952_CLK_LPSPI5 (IMX952_CCM_NUM_CLK_SRC + 96)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI5 时钟（LPSPI5 clock）。

<a id="ga30dac0d2cb4c13dc914d950678ae7ff4"></a>

### `IMX952_CLK_LPSPI6`

```c
#define IMX952_CLK_LPSPI6 (IMX952_CCM_NUM_CLK_SRC + 97)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI6 时钟（LPSPI6 clock）。

<a id="gac4f02540f9cf0a12dfe94ddfbdb2bfc3"></a>

### `IMX952_CLK_LPSPI7`

```c
#define IMX952_CLK_LPSPI7 (IMX952_CCM_NUM_CLK_SRC + 98)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI7 时钟（LPSPI7 clock）。

<a id="ga7e0f66376ddfa8d14689be5b1cc2f58d"></a>

### `IMX952_CLK_LPSPI8`

```c
#define IMX952_CLK_LPSPI8 (IMX952_CCM_NUM_CLK_SRC + 99)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPSPI8 时钟（LPSPI8 clock）。

<a id="gacb1ebcf043e321e0db27c5f191799529"></a>

### `IMX952_CLK_LPTMR1`

```c
#define IMX952_CLK_LPTMR1 (IMX952_CCM_NUM_CLK_SRC + 10)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPTMR1 时钟（LPTMR1 clock）。

<a id="ga5a20f1157eb6e8204a4d0ada3aa82c89"></a>

### `IMX952_CLK_LPTMR2`

```c
#define IMX952_CLK_LPTMR2 (IMX952_CCM_NUM_CLK_SRC + 100)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPTMR2 时钟（LPTMR2 clock）。

<a id="ga8436c0cf30cd588c6455d0321baec0dc"></a>

### `IMX952_CLK_LPUART1`

```c
#define IMX952_CLK_LPUART1 (IMX952_CCM_NUM_CLK_SRC + 11)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART1 时钟（LPUART1 clock）。

<a id="ga79f9479bcd1aa7e6fcc69063391f4b14"></a>

### `IMX952_CLK_LPUART2`

```c
#define IMX952_CLK_LPUART2 (IMX952_CCM_NUM_CLK_SRC + 12)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART2 时钟（LPUART2 clock）。

<a id="gae58fc80ca785f07f5495230941815f7a"></a>

### `IMX952_CLK_LPUART3`

```c
#define IMX952_CLK_LPUART3 (IMX952_CCM_NUM_CLK_SRC + 101)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART3 时钟（LPUART3 clock）。

<a id="ga5653005f43f816acfa66ded30325a562"></a>

### `IMX952_CLK_LPUART4`

```c
#define IMX952_CLK_LPUART4 (IMX952_CCM_NUM_CLK_SRC + 102)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART4 时钟（LPUART4 clock）。

<a id="gaeb992d7eaf2505cede034795536bdf37"></a>

### `IMX952_CLK_LPUART5`

```c
#define IMX952_CLK_LPUART5 (IMX952_CCM_NUM_CLK_SRC + 103)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART5 时钟（LPUART5 clock）。

<a id="gae23f66d12251642ef39b1641b261f3af"></a>

### `IMX952_CLK_LPUART6`

```c
#define IMX952_CLK_LPUART6 (IMX952_CCM_NUM_CLK_SRC + 104)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART6 时钟（LPUART6 clock）。

<a id="ga270a616ad346393cc4c45a0645f2219d"></a>

### `IMX952_CLK_LPUART7`

```c
#define IMX952_CLK_LPUART7 (IMX952_CCM_NUM_CLK_SRC + 105)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART7 时钟（LPUART7 clock）。

<a id="gaff08699e35d25bd1dc758fcae970fc3e"></a>

### `IMX952_CLK_LPUART8`

```c
#define IMX952_CLK_LPUART8 (IMX952_CCM_NUM_CLK_SRC + 106)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

LPUART8 时钟（LPUART8 clock）。

<a id="ga5659948ecd9b48807e051734ea707738"></a>

### `IMX952_CLK_M33`

```c
#define IMX952_CLK_M33 (IMX952_CCM_NUM_CLK_SRC + 13)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-M33 核心 时钟（Cortex-M33 core clock）。

<a id="ga2d428ca57850519a072c844cd6af195c"></a>

### `IMX952_CLK_M33SYSTICK`

```c
#define IMX952_CLK_M33SYSTICK (IMX952_CCM_NUM_CLK_SRC + 14)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-M33 SysTick 时钟（Cortex-M33 SysTick clock）。

<a id="ga71d063d87af2e021db96f44c72d9e611"></a>

### `IMX952_CLK_M7`

```c
#define IMX952_CLK_M7 (IMX952_CCM_NUM_CLK_SRC + 54)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-M7 核心 时钟（Cortex-M7 core clock）。

<a id="ga4d4326b4f31df95619493a267b0faf4c"></a>

### `IMX952_CLK_M7SYSTICK`

```c
#define IMX952_CLK_M7SYSTICK (IMX952_CCM_NUM_CLK_SRC + 55)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Cortex-M7 SysTick 时钟（Cortex-M7 SysTick clock）。

<a id="ga831a26f60a7116f4131bf77a8e5f66c9"></a>

### `IMX952_CLK_MIPIPHYPLLBYPASS`

```c
#define IMX952_CLK_MIPIPHYPLLBYPASS (IMX952_CCM_NUM_CLK_SRC + 26)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

MIPI PHY PLL 旁路 时钟（MIPI PHY PLL bypass clock）。

<a id="ga59bed80ccf3b29c8a1f92f2a265e02b1"></a>

### `IMX952_CLK_MIPITESTBYTE`

```c
#define IMX952_CLK_MIPITESTBYTE (IMX952_CCM_NUM_CLK_SRC + 28)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

MIPI 测试 字节 时钟（MIPI test byte clock）。

<a id="gaf0b14b642cc622e4118566f980b2711b"></a>

### `IMX952_CLK_NOC`

```c
#define IMX952_CLK_NOC (IMX952_CCM_NUM_CLK_SRC + 66)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

片上网络 时钟（Network-on-chip clock）。

<a id="gadf0655cea3322c98c299982bb3a72b10"></a>

### `IMX952_CLK_NOCAPB`

```c
#define IMX952_CLK_NOCAPB (IMX952_CCM_NUM_CLK_SRC + 65)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

NOC APB 时钟（NOC APB clock）。

<a id="ga6c0826297d389a194d9c347e1dec2f3c"></a>

### `IMX952_CLK_NPU`

```c
#define IMX952_CLK_NPU (IMX952_CCM_NUM_CLK_SRC + 68)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

神经网络处理单元 时钟（Neural processing unit clock）。

<a id="ga7679466832c15b9007ccbfd89f29399b"></a>

### `IMX952_CLK_NPUAPB`

```c
#define IMX952_CLK_NPUAPB (IMX952_CCM_NUM_CLK_SRC + 67)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

NPU APB 时钟（NPU APB clock）。

<a id="ga67b66c12811be5bed864d37a25653e2d"></a>

### `IMX952_CLK_PDM`

```c
#define IMX952_CLK_PDM (IMX952_CCM_NUM_CLK_SRC + 16)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

PDM 时钟（PDM clock）。

<a id="gabfebcfad721ae0c19c0fdab927890cc9"></a>

### `IMX952_CLK_RESERVED1`

```c
#define IMX952_CLK_RESERVED1 (IMX952_CCM_NUM_CLK_SRC + 1)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 1（Reserved peripheral clock 1）。

<a id="ga63ee8489512d404515a7c0a93f709461"></a>

### `IMX952_CLK_RESERVED15`

```c
#define IMX952_CLK_RESERVED15 (IMX952_CCM_NUM_CLK_SRC + 15)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 15（Reserved peripheral clock 15）。

<a id="ga651989292cdcf481380a884d4c0e5aef"></a>

### `IMX952_CLK_RESERVED18`

```c
#define IMX952_CLK_RESERVED18 (IMX952_CCM_NUM_CLK_SRC + 18)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 18（Reserved peripheral clock 18）。

<a id="gae8433b2b0ba8c3daf76216a994a2d353"></a>

### `IMX952_CLK_RESERVED20`

```c
#define IMX952_CLK_RESERVED20 (IMX952_CCM_NUM_CLK_SRC + 20)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 20（Reserved peripheral clock 20）。

<a id="ga3db8105a07f2ce87e006a2b9f758bd8f"></a>

### `IMX952_CLK_RESERVED27`

```c
#define IMX952_CLK_RESERVED27 (IMX952_CCM_NUM_CLK_SRC + 27)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 27（Reserved peripheral clock 27）。

<a id="gaa2bec9707b9dca1d91c5473ef1640ca2"></a>

### `IMX952_CLK_RESERVED4`

```c
#define IMX952_CLK_RESERVED4 (IMX952_CCM_NUM_CLK_SRC + 4)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 4（Reserved peripheral clock 4）。

<a id="ga17655f965e3128b63c8a3abf3c34768a"></a>

### `IMX952_CLK_RESERVED41`

```c
#define IMX952_CLK_RESERVED41 (IMX952_CCM_NUM_CLK_SRC + 41)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 41（Reserved peripheral clock 41）。

<a id="ga58a267768b3191c2e01e7a18042950d8"></a>

### `IMX952_CLK_RESERVED63`

```c
#define IMX952_CLK_RESERVED63 (IMX952_CCM_NUM_CLK_SRC + 63)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 63（Reserved peripheral clock 63）。

<a id="gae2d0ef4dcebbb0438c4a53856becc422"></a>

### `IMX952_CLK_RESERVED75`

```c
#define IMX952_CLK_RESERVED75 (IMX952_CCM_NUM_CLK_SRC + 75)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 75（Reserved peripheral clock 75）。

<a id="gab9ce1f7a67d35b9aa91e4ccc0b221753"></a>

### `IMX952_CLK_RESERVED76`

```c
#define IMX952_CLK_RESERVED76 (IMX952_CCM_NUM_CLK_SRC + 76)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 76（Reserved peripheral clock 76）。

<a id="ga48a75f83239ad51a9e9900d28a74f32d"></a>

### `IMX952_CLK_RESERVED86`

```c
#define IMX952_CLK_RESERVED86 (IMX952_CCM_NUM_CLK_SRC + 86)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

保留外设 时钟 86（Reserved peripheral clock 86）。

<a id="gad6bb83d2d46f67c39716ec744909e1f6"></a>

### `IMX952_CLK_SAI1`

```c
#define IMX952_CLK_SAI1 (IMX952_CCM_NUM_CLK_SRC + 17)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SAI1 时钟（SAI1 clock）。

<a id="ga8f13732951eed83cecdac72b7180c4fa"></a>

### `IMX952_CLK_SAI2`

```c
#define IMX952_CLK_SAI2 (IMX952_CCM_NUM_CLK_SRC + 64)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SAI2 时钟（SAI2 clock）。

<a id="gab86838fbcfa36a15bfb30241e811d4df"></a>

### `IMX952_CLK_SAI3`

```c
#define IMX952_CLK_SAI3 (IMX952_CCM_NUM_CLK_SRC + 107)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SAI3 时钟（SAI3 clock）。

<a id="ga4ec095c742bfdcc954b83d8c13aa1f95"></a>

### `IMX952_CLK_SAI4`

```c
#define IMX952_CLK_SAI4 (IMX952_CCM_NUM_CLK_SRC + 108)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SAI4 时钟（SAI4 clock）。

<a id="gada66056d7a864b3a7fb73758d1f401e2"></a>

### `IMX952_CLK_SAI5`

```c
#define IMX952_CLK_SAI5 (IMX952_CCM_NUM_CLK_SRC + 109)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SAI5 时钟（SAI5 clock）。

<a id="ga879119b0739e90c08dfb21d89c58be8e"></a>

### `IMX952_CLK_SPDIF`

```c
#define IMX952_CLK_SPDIF (IMX952_CCM_NUM_CLK_SRC + 110)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

S/PDIF 时钟（S/PDIF clock）。

<a id="ga743096ff4fa6975b7dac8f10584643ad"></a>

### `IMX952_CLK_SWOTRACE`

```c
#define IMX952_CLK_SWOTRACE (IMX952_CCM_NUM_CLK_SRC + 111)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

SWO 跟踪 时钟（SWO trace clock）。

<a id="ga54de19acf040cef42d3e40ffce9412eb"></a>

### `IMX952_CLK_TPM2`

```c
#define IMX952_CLK_TPM2 (IMX952_CCM_NUM_CLK_SRC + 19)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

TPM2 时钟（TPM2 clock）。

<a id="gaef0ff808e6b781fa505dab10bc4fa51b"></a>

### `IMX952_CLK_TPM4`

```c
#define IMX952_CLK_TPM4 (IMX952_CCM_NUM_CLK_SRC + 112)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

TPM4 时钟（TPM4 clock）。

<a id="gadd0bb62c169c44e38fffed5c08e66914"></a>

### `IMX952_CLK_TPM5`

```c
#define IMX952_CLK_TPM5 (IMX952_CCM_NUM_CLK_SRC + 113)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

TPM5 时钟（TPM5 clock）。

<a id="ga263cf3ea860bfb247fdb40d8db63fcc3"></a>

### `IMX952_CLK_TPM6`

```c
#define IMX952_CLK_TPM6 (IMX952_CCM_NUM_CLK_SRC + 114)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

TPM6 时钟（TPM6 clock）。

<a id="ga682869be4456f0e4502e2035e8dc9903"></a>

### `IMX952_CLK_TSTMR2`

```c
#define IMX952_CLK_TSTMR2 (IMX952_CCM_NUM_CLK_SRC + 115)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

Timestamp 定时器 2 时钟（Timestamp timer 2 clock）。

<a id="gaa073d854720457424d9c59efa414c998"></a>

### `IMX952_CLK_USBPHYBURUNIN`

```c
#define IMX952_CLK_USBPHYBURUNIN (IMX952_CCM_NUM_CLK_SRC + 116)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

USB PHY 老化测试 时钟（USB PHY burn-in clock）。

<a id="ga708f630fb04d80884836308c55e7478f"></a>

### `IMX952_CLK_USDHC1`

```c
#define IMX952_CLK_USDHC1 (IMX952_CCM_NUM_CLK_SRC + 117)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

uSDHC1 时钟（uSDHC1 clock）。

<a id="ga55b06e78fcbeda0b95541b9c75e43fac"></a>

### `IMX952_CLK_USDHC2`

```c
#define IMX952_CLK_USDHC2 (IMX952_CCM_NUM_CLK_SRC + 118)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

uSDHC2 时钟（uSDHC2 clock）。

<a id="ga2c9789e768474a24203d85e0dfc4a43a"></a>

### `IMX952_CLK_USDHC3`

```c
#define IMX952_CLK_USDHC3 (IMX952_CCM_NUM_CLK_SRC + 119)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

uSDHC3 时钟（uSDHC3 clock）。

<a id="ga79ee5f43bbd83b132a8d5a072a92aa14"></a>

### `IMX952_CLK_V2XPK`

```c
#define IMX952_CLK_V2XPK (IMX952_CCM_NUM_CLK_SRC + 120)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

V2X 数据包引擎 时钟（V2X packet engine clock）。

<a id="ga96a440ad719c4016207d3fefbeabbf6e"></a>

### `IMX952_CLK_VPU`

```c
#define IMX952_CLK_VPU (IMX952_CCM_NUM_CLK_SRC + 74)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

视频处理单元 时钟（Video processing unit clock）。

<a id="ga06e617b155e10bead692b6681e06ce77"></a>

### `IMX952_CLK_VPUAPB`

```c
#define IMX952_CLK_VPUAPB (IMX952_CCM_NUM_CLK_SRC + 73)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

VPU APB 时钟（VPU APB clock）。

<a id="ga34a721794435930c4491b4dea37fd8a3"></a>

### `IMX952_CLK_WAKEUPAXI`

```c
#define IMX952_CLK_WAKEUPAXI (IMX952_CCM_NUM_CLK_SRC + 121)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

唤醒 AXI 时钟（Wakeup AXI clock）。

<a id="gad9334abd1606ef0aaaf99220e69162e5"></a>

### `IMX952_CLK_XSPI1`

```c
#define IMX952_CLK_XSPI1 (IMX952_CCM_NUM_CLK_SRC + 85)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

就地执行 SPI 1 时钟（eXecute-in-place SPI 1 clock）。

<a id="gacfb4422e38d4b3b1a28d06d7779264db"></a>

### `IMX952_CLK_XSPISLVROOT`

```c
#define IMX952_CLK_XSPISLVROOT (IMX952_CCM_NUM_CLK_SRC + 122)
```

```c
#include <zephyr/dt-bindings/clock/imx952_clock.h>
```

XPI slave root 时钟（XPI slave root clock）。


## 8.3\_原页交叉引用（Cross References）

- [IMX952_CCM_NUM_CLK_SRC](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md#a03330ea5d5d6cb6c5d0cbde5cc2bb8e6)
- [zephyr/dt-bindings/clock/imx952_clock.h](../api_file_pic_clock_reference/P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P007_增强串行外设接口（ESPI）.md) · [返回大纲](大纲.md)
