---
id: learning.zephyr-docs.api-platform-topic-reference.page-52
title: 敦泰（FocalTech）FT9001 时钟标识符（Clock identifiers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_敦泰（FocalTech）FT9001 时钟标识符（Clock identifiers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__ft9001__clocks.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FocalTech FT9001的时钟标识符（Clock Identifiers）。

<a id="details"></a>

FocalTech FT9001 时钟标识（Clock Identifiers）。时钟标识遵循命名约定 `FOCALTECH_CLOCK_<PERIPHERAL>`。例如，`FOCALTECH_CLOCK_SPI1` 标识 SPI1 的时钟门控（Clock Gate）。有效外设按时钟门控控制寄存器（Clock Gate Control Register）分组如下：

| 寄存器（Register） | 外设（Peripherals） |
| --- | --- |
| `MULTICGCR` | `OTP_AHB`, `MCC`, `MCCADR`, `ADC`, `MESH`, `TC`, `CLKOUT`, `KEY_CTRL`, `CCM_RESET`, `OTP_IPS`, `CPM_IPS`, `TRACE`, `I2S_M`, `I2S_S`, `CRC0`, `CRC1` |
| `SYSCGCR` | `SSISLV1`, `DMAC1`, `DMAC2`, `AHB2_MUX`, `PXLP1_AHB`, `PXLP2_AHB`, `SRAMD`, `SRAM0`, `SRAM1`, `SRAM2`, `SRAM3_4`, `SSI4`, `SSI5`, `SSI6` |
| `AHB3CGCR` | `ROM`, `ROM_OTP_MUX`, `AHB3_MUX`, `USBC`, `PXLP1_APB`, `PXLP2_APB`, `I2S1`, `I2S2` |
| `ARITHCGCR` | `AES`, `SM4`, `RF_AES_SM4`, `CRYPTO`, `SHA`, `EDMAC0`, `DES`, `ZUC`, `AHB2MLB`, `AHB2IPS2`, `TRNG` |
| `IPSCGCR` | `IO_CTRL`, `WDT`, `RTC`, `PIT1`, `PIT2`, `USI1`, `EDMAC1`, `SPI1`, `SPI2`, `SPI3`, `SCI1`, `SCI2`, `USI2`, `CAN1`, `I2C1`, `PWM0`, `I2C2`, `CAN2`, `SCI3`, `QADC`, `DAC`, `MCC_IPS`, `PWMT1`, `LD`, `PWMT2`, `PGD`, `SEC_DET`, `PCI`, `PMURTC`, `AHB2IPS`, `PWMT3` |
| `EPORTCGCR` | `EPORT0`, `EPORT1`, `EPORT2`, `EPORT3`, `EPORT4`, `EPORT5`, `EPORT6`, `EPORT7`, `ACMP1`, `ACMP2` |

<a id="header-files"></a>
<a id="files"></a>

## 52.1\_文件（Files）

<a id="r_focaltech_5Fft9001_5Fclocks_2Eh"></a>

```c
file focaltech_ft9001_clocks.h
```

相关声明：[focaltech_ft9001_clocks.h](../api_file_reference/P114_zephyr__dt-bindings__clock__focaltech_ft9001_clocks.h_文件参考.md)。

FocalTech FT9001的时钟标识符（Clock Identifiers）。


## 52.2\_原页交叉引用（Cross References）

- [focaltech_ft9001_clocks.h](../api_file_reference/P114_zephyr__dt-bindings__clock__focaltech_ft9001_clocks.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P051_以太网 PHY 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P053_HTTP头部压缩（HPACK）。.md)
