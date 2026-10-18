---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-13
title: zephyr__dt-bindings__reset__focaltech_ft9001_reset.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_reset\_\_focaltech\_ft9001\_reset.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FocalTech FT9001的外设复位标识符（Peripheral Reset Identifiers）。

查看此文件的源码。

<a id="details"></a>

FocalTech FT9001的外设复位标识符（Peripheral Reset Identifiers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_ga14b208f0a5eb8e54f8cccb622896f367"></a>

```c
#define FOCALTECH_EPORTRSTCR_OFFSET 0x88U
```

相关声明：[FOCALTECH_EPORTRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga14b208f0a5eb8e54f8cccb622896f367)。

EPORT 复位控制寄存器（Reset Control Register）。

<a id="r_gabfd52f09e8021a6a4a88ea9545edd4ac"></a>

```c
#define FOCALTECH_MULTIRSTCR_OFFSET 0xACU
```

相关声明：[FOCALTECH_MULTIRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gabfd52f09e8021a6a4a88ea9545edd4ac)。

多模块复位控制寄存器（Multi Reset Control Register）。

<a id="r_ga943200e23ff31dce4a36b68b0664def7"></a>

```c
#define FOCALTECH_SYSRSTCR_OFFSET 0xB0U
```

相关声明：[FOCALTECH_SYSRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga943200e23ff31dce4a36b68b0664def7)。

系统复位控制寄存器（System Reset Control Register）。

<a id="r_gaa62d0bb8b7627d258095ef599ea803d0"></a>

```c
#define FOCALTECH_AHB3RSTCR_OFFSET 0xB4U
```

相关声明：[FOCALTECH_AHB3RSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gaa62d0bb8b7627d258095ef599ea803d0)。

AHB3 复位控制寄存器（Reset Control Register）。

<a id="r_ga386d01a7838235774815997a33f77577"></a>

```c
#define FOCALTECH_ARITHRSTCR_OFFSET 0xB8U
```

相关声明：[FOCALTECH_ARITHRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga386d01a7838235774815997a33f77577)。

算法复位控制寄存器（Algorithm Reset Control Register）。

<a id="r_gaa9c609bd1da838111513b2c5e78588ca"></a>

```c
#define FOCALTECH_IPSRSTCR_OFFSET 0xBCU
```

相关声明：[FOCALTECH_IPSRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gaa9c609bd1da838111513b2c5e78588ca)。

IPS 复位控制寄存器（Reset Control Register）。

<a id="r_gac1532022c40bd7d071e3597d70e7d0f4"></a>

```c
#define FOCALTECH_RESET_EPORT0 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_EPORT0](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gac1532022c40bd7d071e3597d70e7d0f4)。

EPORT0 复位（reset）。

<a id="r_ga9bdbff48cb55369a4b194785a9dd14a1"></a>

```c
#define FOCALTECH_RESET_EPORT1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_EPORT1](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga9bdbff48cb55369a4b194785a9dd14a1)。

EPORT1 复位。

<a id="r_ga1c731760579999f96687b8a81c61dc3e"></a>

```c
#define FOCALTECH_RESET_EPORT2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_EPORT2](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga1c731760579999f96687b8a81c61dc3e)。

EPORT2 复位。

<a id="r_gac2c04d30326e36e4e7b284e9852803a3"></a>

```c
#define FOCALTECH_RESET_EPORT3 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_EPORT3](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gac2c04d30326e36e4e7b284e9852803a3)。

EPORT3 复位。

<a id="r_ga15510335513f34201b7acb6239063d93"></a>

```c
#define FOCALTECH_RESET_EPORT4 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_EPORT4](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga15510335513f34201b7acb6239063d93)。

EPORT4 复位。

<a id="r_gaa72200eab0c7dc5daf7750c425a5c5a2"></a>

```c
#define FOCALTECH_RESET_EPORT5 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_EPORT5](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gaa72200eab0c7dc5daf7750c425a5c5a2)。

EPORT5 复位。

<a id="r_ga661d0cbcdff6e303f0c155c7fe7fe232"></a>

```c
#define FOCALTECH_RESET_EPORT6 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_EPORT6](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga661d0cbcdff6e303f0c155c7fe7fe232)。

EPORT6 复位。

<a id="r_gab608960b531c74daff4e6816ce8e4abf"></a>

```c
#define FOCALTECH_RESET_EPORT7 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_EPORT7](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gab608960b531c74daff4e6816ce8e4abf)。

EPORT7 复位。

<a id="r_ga66e82f86157f87b7c1e6a417bc5ac73d"></a>

```c
#define FOCALTECH_RESET_ACMP1 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_ACMP1](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga66e82f86157f87b7c1e6a417bc5ac73d)。

ACMP1 复位。

<a id="r_gafa0d499c4c67e8a7028383d3d67a8c75"></a>

```c
#define FOCALTECH_RESET_ACMP2 FOCALTECH_RESET_CONFIG(EPORTRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_ACMP2](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gafa0d499c4c67e8a7028383d3d67a8c75)。

ACMP2 复位。

<a id="r_ga46bbd9e1b3d0b62f61fabbaa8c334adc"></a>

```c
#define FOCALTECH_RESET_OTP_AHB FOCALTECH_RESET_CONFIG(MULTIRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_OTP_AHB](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga46bbd9e1b3d0b62f61fabbaa8c334adc)。

OTP AHB 复位（Reset）。

<a id="r_gaeee18837dae2087428921fcfcb556675"></a>

```c
#define FOCALTECH_RESET_MCC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_MCC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gaeee18837dae2087428921fcfcb556675)。

MCC 复位（Reset）。

<a id="r_ga0983a1b5886dfb370dbf9e2f705e441f"></a>

```c
#define FOCALTECH_RESET_MCCADR FOCALTECH_RESET_CONFIG(MULTIRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_MCCADR](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga0983a1b5886dfb370dbf9e2f705e441f)。

MCC 地址（Address） 复位（Reset）。

<a id="r_ga912e26cdf2b90bd075e1a69b425c97b2"></a>

```c
#define FOCALTECH_RESET_ADC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_ADC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga912e26cdf2b90bd075e1a69b425c97b2)。

ADC 复位（Reset）。

<a id="r_ga7ed484674341a911a948cff1d4594c9a"></a>

```c
#define FOCALTECH_RESET_MESH FOCALTECH_RESET_CONFIG(MULTIRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_MESH](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga7ed484674341a911a948cff1d4594c9a)。

MESH 复位（Reset）。

<a id="r_gab46b7e24dfde17907d3ebeb640afcdb9"></a>

```c
#define FOCALTECH_RESET_TC FOCALTECH_RESET_CONFIG(MULTIRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_TC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gab46b7e24dfde17907d3ebeb640afcdb9)。

TC 复位（Reset）。

<a id="r_gad58737d782cc2495d5bc173b6f02a0ff"></a>

```c
#define FOCALTECH_RESET_CLKOUT FOCALTECH_RESET_CONFIG(MULTIRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_CLKOUT](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gad58737d782cc2495d5bc173b6f02a0ff)。

时钟输出（Clock Output） 复位（Reset）。

<a id="r_ga5536cbd12d63c541b93b3afc8b7279ad"></a>

```c
#define FOCALTECH_RESET_KEY_CTRL FOCALTECH_RESET_CONFIG(MULTIRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_KEY_CTRL](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga5536cbd12d63c541b93b3afc8b7279ad)。

Key 控制器（Key Controller） 复位（Reset）。

<a id="r_gac2740388f9e13c9a41dbf519f4d81b1e"></a>

```c
#define FOCALTECH_RESET_CCM_RESET FOCALTECH_RESET_CONFIG(MULTIRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_CCM_RESET](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gac2740388f9e13c9a41dbf519f4d81b1e)。

CCM 复位（Reset）。

<a id="r_ga19ea0b41ff1d420fdd621231bc7f5620"></a>

```c
#define FOCALTECH_RESET_OTP_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_OTP_IPS](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga19ea0b41ff1d420fdd621231bc7f5620)。

OTP IPS 复位（Reset）。

<a id="r_ga82036818a156d4e471c4292382ebf4b4"></a>

```c
#define FOCALTECH_RESET_CPM_IPS FOCALTECH_RESET_CONFIG(MULTIRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_CPM_IPS](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga82036818a156d4e471c4292382ebf4b4)。

CPM IPS 复位（Reset）。

<a id="r_ga2089134755b7e42d06d75959cb630520"></a>

```c
#define FOCALTECH_RESET_TRACE FOCALTECH_RESET_CONFIG(MULTIRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_TRACE](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga2089134755b7e42d06d75959cb630520)。

跟踪（Trace） 复位（Reset）。

<a id="r_gad5f1147d63f910091e73a2963dc34849"></a>

```c
#define FOCALTECH_RESET_I2S_M FOCALTECH_RESET_CONFIG(MULTIRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_I2S_M](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gad5f1147d63f910091e73a2963dc34849)。

I2S 主设备（Master） 复位（Reset）。

<a id="r_ga3f74b242e0fa83ed8e80e38dc11847ff"></a>

```c
#define FOCALTECH_RESET_I2S_S FOCALTECH_RESET_CONFIG(MULTIRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_I2S_S](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga3f74b242e0fa83ed8e80e38dc11847ff)。

I2S 从设备（Slave） 复位（Reset）。

<a id="r_gab704c34447390a3a45a959175026f201"></a>

```c
#define FOCALTECH_RESET_CRC0 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_CRC0](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gab704c34447390a3a45a959175026f201)。

CRC0 复位（Reset）。

<a id="r_gaa05b6ae8e4720ff54d0a6586534496c9"></a>

```c
#define FOCALTECH_RESET_CRC1 FOCALTECH_RESET_CONFIG(MULTIRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_CRC1](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gaa05b6ae8e4720ff54d0a6586534496c9)。

CRC1 复位（Reset）。

<a id="r_ga59d4227c9bf1489f8677cc93acb9c51c"></a>

```c
#define FOCALTECH_RESET_SSISLV1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_SSISLV1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga59d4227c9bf1489f8677cc93acb9c51c)。

SSI 从机 1（Slave 1）复位。

<a id="r_gadf58c3c5d2308e7c65f6b76985344f1a"></a>

```c
#define FOCALTECH_RESET_DMAC1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_DMAC1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gadf58c3c5d2308e7c65f6b76985344f1a)。

DMAC1 复位（Reset）。

<a id="r_gaf267ed4b27b192b8f33070b946814643"></a>

```c
#define FOCALTECH_RESET_DMAC2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_DMAC2](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gaf267ed4b27b192b8f33070b946814643)。

DMAC2 复位（Reset）。

<a id="r_ga7efb131ead62ca3029a5bd160b38e781"></a>

```c
#define FOCALTECH_RESET_AHB2_MUX FOCALTECH_RESET_CONFIG(SYSRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_AHB2_MUX](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga7efb131ead62ca3029a5bd160b38e781)。

AHB2 多路复用器（MUX）复位。

<a id="r_ga5c79ce9cd726c2350ed604294657c825"></a>

```c
#define FOCALTECH_RESET_PXLP1_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_PXLP1_AHB](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga5c79ce9cd726c2350ed604294657c825)。

PXLP1 AHB 复位（Reset）。

<a id="r_ga41b21e2f451c2e8defd1ebb7badca937"></a>

```c
#define FOCALTECH_RESET_PXLP2_AHB FOCALTECH_RESET_CONFIG(SYSRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_PXLP2_AHB](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga41b21e2f451c2e8defd1ebb7badca937)。

PXLP2 AHB 复位（Reset）。

<a id="r_ga783ae3aa688eb9abe2d457051f35bb83"></a>

```c
#define FOCALTECH_RESET_SRAMD FOCALTECH_RESET_CONFIG(SYSRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_SRAMD](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga783ae3aa688eb9abe2d457051f35bb83)。

SRAM 数据复位（Data Reset）。

<a id="r_ga5101183f616716b3266d03b6d03c0d7c"></a>

```c
#define FOCALTECH_RESET_SRAM0 FOCALTECH_RESET_CONFIG(SYSRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_SRAM0](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga5101183f616716b3266d03b6d03c0d7c)。

SRAM0 复位（Reset）。

<a id="r_ga4cae816aba6332bf0cbf0adb38d618f1"></a>

```c
#define FOCALTECH_RESET_SRAM1 FOCALTECH_RESET_CONFIG(SYSRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_SRAM1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga4cae816aba6332bf0cbf0adb38d618f1)。

SRAM1 复位（Reset）。

<a id="r_ga70ac8466cce6411a8e159d6dded280e5"></a>

```c
#define FOCALTECH_RESET_SRAM2 FOCALTECH_RESET_CONFIG(SYSRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_SRAM2](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga70ac8466cce6411a8e159d6dded280e5)。

SRAM2 复位（Reset）。

<a id="r_gaa8b5763ee7e1ac184a28ec21d63e0d09"></a>

```c
#define FOCALTECH_RESET_SRAM3_4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 16U)
```

相关声明：[FOCALTECH_RESET_SRAM3_4](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gaa8b5763ee7e1ac184a28ec21d63e0d09)。

SRAM3/4 复位（Reset）。

<a id="r_ga484a4ec976b714c56db3bd6fa2fce500"></a>

```c
#define FOCALTECH_RESET_SSI4 FOCALTECH_RESET_CONFIG(SYSRSTCR, 17U)
```

相关声明：[FOCALTECH_RESET_SSI4](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga484a4ec976b714c56db3bd6fa2fce500)。

SSI4 复位（Reset）。

<a id="r_ga4a40dfcde87bf329e95d75960f40cb17"></a>

```c
#define FOCALTECH_RESET_SSI5 FOCALTECH_RESET_CONFIG(SYSRSTCR, 18U)
```

相关声明：[FOCALTECH_RESET_SSI5](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga4a40dfcde87bf329e95d75960f40cb17)。

SSI5 复位（Reset）。

<a id="r_ga61a5a9485deb12d5b4df72bd7e9ed4fd"></a>

```c
#define FOCALTECH_RESET_SSI6 FOCALTECH_RESET_CONFIG(SYSRSTCR, 19U)
```

相关声明：[FOCALTECH_RESET_SSI6](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga61a5a9485deb12d5b4df72bd7e9ed4fd)。

SSI6 复位（Reset）。

<a id="r_ga447851fbf278af65b38904e30045fc19"></a>

```c
#define FOCALTECH_RESET_ROM FOCALTECH_RESET_CONFIG(AHB3RSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_ROM](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga447851fbf278af65b38904e30045fc19)。

ROM 复位（reset）。

<a id="r_gab429b3964b5c228cce44c270c964e0ee"></a>

```c
#define FOCALTECH_RESET_ROM_OTP_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_ROM_OTP_MUX](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gab429b3964b5c228cce44c270c964e0ee)。

ROM OTP 多路复用器（MUX）复位。

<a id="r_gaf33f88c4f792b7529f075fbd83b01e71"></a>

```c
#define FOCALTECH_RESET_AHB3_MUX FOCALTECH_RESET_CONFIG(AHB3RSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_AHB3_MUX](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gaf33f88c4f792b7529f075fbd83b01e71)。

AHB3 多路复用器（MUX）复位。

<a id="r_ga743a6041380923309cc652cddab980a8"></a>

```c
#define FOCALTECH_RESET_USBC FOCALTECH_RESET_CONFIG(AHB3RSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_USBC](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga743a6041380923309cc652cddab980a8)。

USB 控制器复位。

<a id="r_gad76e8b42e772894a25fff56c91e46b08"></a>

```c
#define FOCALTECH_RESET_PXLP1_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_PXLP1_APB](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gad76e8b42e772894a25fff56c91e46b08)。

PXLP1 APB 复位。

<a id="r_gaa3710eb031f196eb13d98b9a34c6813c"></a>

```c
#define FOCALTECH_RESET_PXLP2_APB FOCALTECH_RESET_CONFIG(AHB3RSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_PXLP2_APB](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gaa3710eb031f196eb13d98b9a34c6813c)。

PXLP2 APB 复位。

<a id="r_ga03a88cdec31ee479b648d16609f3f1de"></a>

```c
#define FOCALTECH_RESET_I2S1 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_I2S1](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga03a88cdec31ee479b648d16609f3f1de)。

I2S1 复位。

<a id="r_ga9472bf1174ae07a3b1bb0fbda422742e"></a>

```c
#define FOCALTECH_RESET_I2S2 FOCALTECH_RESET_CONFIG(AHB3RSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_I2S2](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga9472bf1174ae07a3b1bb0fbda422742e)。

I2S2 复位。

<a id="r_ga429695ee2f576fc6a3357241aa38c215"></a>

```c
#define FOCALTECH_RESET_AES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_AES](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga429695ee2f576fc6a3357241aa38c215)。

AES 复位（Reset）。

<a id="r_ga7524cad266f64ab27830a8deb266bedd"></a>

```c
#define FOCALTECH_RESET_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_SM4](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga7524cad266f64ab27830a8deb266bedd)。

SM4 复位（Reset）。

<a id="r_ga1034fb963eb617815f8028bff5e5bcc7"></a>

```c
#define FOCALTECH_RESET_RF_AES_SM4 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_RF_AES_SM4](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga1034fb963eb617815f8028bff5e5bcc7)。

RF AES SM4 复位（Reset）。

<a id="r_ga1e3477301447a988b3f2ce831172b4a8"></a>

```c
#define FOCALTECH_RESET_CRYPTO FOCALTECH_RESET_CONFIG(ARITHRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_CRYPTO](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga1e3477301447a988b3f2ce831172b4a8)。

加密模块（Crypto）复位。

<a id="r_gaf3941bb54a85acdd59b995844b21bd42"></a>

```c
#define FOCALTECH_RESET_SHA FOCALTECH_RESET_CONFIG(ARITHRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_SHA](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gaf3941bb54a85acdd59b995844b21bd42)。

SHA 复位（Reset）。

<a id="r_ga8766e97447e1418adc43ad93cef51ba6"></a>

```c
#define FOCALTECH_RESET_EDMAC0 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_EDMAC0](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga8766e97447e1418adc43ad93cef51ba6)。

EDMAC0 复位（Reset）。

<a id="r_gadf9a12c842552043611970bf7f657df3"></a>

```c
#define FOCALTECH_RESET_DES FOCALTECH_RESET_CONFIG(ARITHRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_DES](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gadf9a12c842552043611970bf7f657df3)。

DES 复位（Reset）。

<a id="r_ga23e239f9738c819a2fe24016768c6995"></a>

```c
#define FOCALTECH_RESET_ZUC FOCALTECH_RESET_CONFIG(ARITHRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_ZUC](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga23e239f9738c819a2fe24016768c6995)。

ZUC 复位（Reset）。

<a id="r_gad5e83816e598adb358d726c941892fa7"></a>

```c
#define FOCALTECH_RESET_AHB2MLB FOCALTECH_RESET_CONFIG(ARITHRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_AHB2MLB](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gad5e83816e598adb358d726c941892fa7)。

AHB2MLB 复位（Reset）。

<a id="r_gad54c36e48530d8cf63b8d83a5e536ae5"></a>

```c
#define FOCALTECH_RESET_AHB2IPS2 FOCALTECH_RESET_CONFIG(ARITHRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_AHB2IPS2](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gad54c36e48530d8cf63b8d83a5e536ae5)。

AHB2IPS2 复位（Reset）。

<a id="r_gaa9011c2f1c02ea6b256155ef5fde3e05"></a>

```c
#define FOCALTECH_RESET_TRNG FOCALTECH_RESET_CONFIG(ARITHRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_TRNG](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gaa9011c2f1c02ea6b256155ef5fde3e05)。

真随机数发生器（True Random Number Generator，TRNG）复位。

<a id="r_ga60a6a9f5ef12bdb1ad5909c992234faa"></a>

```c
#define FOCALTECH_RESET_IO_CTRL FOCALTECH_RESET_CONFIG(IPSRSTCR, 0U)
```

相关声明：[FOCALTECH_RESET_IO_CTRL](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga60a6a9f5ef12bdb1ad5909c992234faa)。

I/O 控制器复位（IO Controller Reset）。

<a id="r_ga23196071f4d02b825b2e40fbc648b97a"></a>

```c
#define FOCALTECH_RESET_WDT FOCALTECH_RESET_CONFIG(IPSRSTCR, 1U)
```

相关声明：[FOCALTECH_RESET_WDT](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga23196071f4d02b825b2e40fbc648b97a)。

看门狗定时器复位（Watchdog Timer Reset）。

<a id="r_ga4875113ccb459b1e6e264de54c2ffc0a"></a>

```c
#define FOCALTECH_RESET_RTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 2U)
```

相关声明：[FOCALTECH_RESET_RTC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga4875113ccb459b1e6e264de54c2ffc0a)。

RTC 复位（Reset）。

<a id="r_gad973fbc73a970d07d6ad470f1b309ca4"></a>

```c
#define FOCALTECH_RESET_PIT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 3U)
```

相关声明：[FOCALTECH_RESET_PIT1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gad973fbc73a970d07d6ad470f1b309ca4)。

PIT1 复位（Reset）。

<a id="r_ga38943fdef6b7ee8417576078f85cf382"></a>

```c
#define FOCALTECH_RESET_PIT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 4U)
```

相关声明：[FOCALTECH_RESET_PIT2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga38943fdef6b7ee8417576078f85cf382)。

PIT2 复位（Reset）。

<a id="r_ga3ba939af141dff4f65cda43668ae8888"></a>

```c
#define FOCALTECH_RESET_USI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 5U)
```

相关声明：[FOCALTECH_RESET_USI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga3ba939af141dff4f65cda43668ae8888)。

USI1 复位（Reset）。

<a id="r_gacf9093e53fb0385eb90e66ef0f65f8de"></a>

```c
#define FOCALTECH_RESET_EDMAC1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 6U)
```

相关声明：[FOCALTECH_RESET_EDMAC1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gacf9093e53fb0385eb90e66ef0f65f8de)。

EDMAC1 复位（Reset）。

<a id="r_gadbced14265c08f7f8e234531d6e0abf7"></a>

```c
#define FOCALTECH_RESET_SPI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 7U)
```

相关声明：[FOCALTECH_RESET_SPI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gadbced14265c08f7f8e234531d6e0abf7)。

SPI1 复位（Reset）。

<a id="r_gabbe5f32ac775072810f02e779499462b"></a>

```c
#define FOCALTECH_RESET_SPI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 8U)
```

相关声明：[FOCALTECH_RESET_SPI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gabbe5f32ac775072810f02e779499462b)。

SPI2 复位（Reset）。

<a id="r_ga7281304a265cfd95b48fd7420f9f2027"></a>

```c
#define FOCALTECH_RESET_SPI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 9U)
```

相关声明：[FOCALTECH_RESET_SPI3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga7281304a265cfd95b48fd7420f9f2027)。

SPI3 复位（Reset）。

<a id="r_ga64d3fe882d3dbeb6ccd8218538a99fbf"></a>

```c
#define FOCALTECH_RESET_SCI1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 10U)
```

相关声明：[FOCALTECH_RESET_SCI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga64d3fe882d3dbeb6ccd8218538a99fbf)。

SCI1 复位（Reset）。

<a id="r_ga31b2bc4472d7455de72217216b9c068f"></a>

```c
#define FOCALTECH_RESET_SCI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 11U)
```

相关声明：[FOCALTECH_RESET_SCI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga31b2bc4472d7455de72217216b9c068f)。

SCI2 复位（Reset）。

<a id="r_ga75c151a5750135c086893af842fe167d"></a>

```c
#define FOCALTECH_RESET_USI2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 12U)
```

相关声明：[FOCALTECH_RESET_USI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga75c151a5750135c086893af842fe167d)。

USI2 复位（Reset）。

<a id="r_ga27413ec5515407960d47d4942e21e3e7"></a>

```c
#define FOCALTECH_RESET_CAN1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 13U)
```

相关声明：[FOCALTECH_RESET_CAN1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga27413ec5515407960d47d4942e21e3e7)。

CAN1 复位（Reset）。

<a id="r_ga721c4e8eaad920f3990547280a51de46"></a>

```c
#define FOCALTECH_RESET_I2C1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 14U)
```

相关声明：[FOCALTECH_RESET_I2C1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga721c4e8eaad920f3990547280a51de46)。

I2C1 复位（Reset）。

<a id="r_ga60d731d5f1b8f2219c842a94002fa14c"></a>

```c
#define FOCALTECH_RESET_PWM0 FOCALTECH_RESET_CONFIG(IPSRSTCR, 15U)
```

相关声明：[FOCALTECH_RESET_PWM0](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga60d731d5f1b8f2219c842a94002fa14c)。

PWM0 复位（Reset）。

<a id="r_gad3af6cad5d8ae27b40d0bb8a319e3d31"></a>

```c
#define FOCALTECH_RESET_I2C2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 16U)
```

相关声明：[FOCALTECH_RESET_I2C2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gad3af6cad5d8ae27b40d0bb8a319e3d31)。

I2C2 复位（Reset）。

<a id="r_ga1a390c4c955ad9a7889b4106e31c7c03"></a>

```c
#define FOCALTECH_RESET_CAN2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 17U)
```

相关声明：[FOCALTECH_RESET_CAN2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga1a390c4c955ad9a7889b4106e31c7c03)。

CAN2 复位（Reset）。

<a id="r_ga3b1fdc9f2d6f32ca105ccfd78d193cad"></a>

```c
#define FOCALTECH_RESET_SCI3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 18U)
```

相关声明：[FOCALTECH_RESET_SCI3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga3b1fdc9f2d6f32ca105ccfd78d193cad)。

SCI3 复位（Reset）。

<a id="r_ga5fc20fe7b8c04946b5e98da6e10c3225"></a>

```c
#define FOCALTECH_RESET_QADC FOCALTECH_RESET_CONFIG(IPSRSTCR, 20U)
```

相关声明：[FOCALTECH_RESET_QADC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga5fc20fe7b8c04946b5e98da6e10c3225)。

QADC 复位（Reset）。

<a id="r_gae919d9192d4e02630de012bfb2bac18c"></a>

```c
#define FOCALTECH_RESET_DAC FOCALTECH_RESET_CONFIG(IPSRSTCR, 21U)
```

相关声明：[FOCALTECH_RESET_DAC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gae919d9192d4e02630de012bfb2bac18c)。

DAC 复位（Reset）。

<a id="r_gac467218bae41cd35bb93335deb6197f8"></a>

```c
#define FOCALTECH_RESET_MCC_IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 22U)
```

相关声明：[FOCALTECH_RESET_MCC_IPS](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gac467218bae41cd35bb93335deb6197f8)。

MCC IPS 复位（Reset）。

<a id="r_ga49d792f2fff8f95d671689279b9e8b11"></a>

```c
#define FOCALTECH_RESET_PWMT1 FOCALTECH_RESET_CONFIG(IPSRSTCR, 23U)
```

相关声明：[FOCALTECH_RESET_PWMT1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga49d792f2fff8f95d671689279b9e8b11)。

PWMT1 复位（Reset）。

<a id="r_ga48331ab9690d7499fd8cfbcffb9705a9"></a>

```c
#define FOCALTECH_RESET_LD FOCALTECH_RESET_CONFIG(IPSRSTCR, 24U)
```

相关声明：[FOCALTECH_RESET_LD](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga48331ab9690d7499fd8cfbcffb9705a9)。

LD 复位（Reset）。

<a id="r_gac45d20a806ae571f15c120ddf30cb91c"></a>

```c
#define FOCALTECH_RESET_PWMT2 FOCALTECH_RESET_CONFIG(IPSRSTCR, 25U)
```

相关声明：[FOCALTECH_RESET_PWMT2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gac45d20a806ae571f15c120ddf30cb91c)。

PWMT2 复位（Reset）。

<a id="r_gaa4d9885a8d24489bd4dfab44ee62eeed"></a>

```c
#define FOCALTECH_RESET_PGD FOCALTECH_RESET_CONFIG(IPSRSTCR, 26U)
```

相关声明：[FOCALTECH_RESET_PGD](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gaa4d9885a8d24489bd4dfab44ee62eeed)。

PGD 复位（Reset）。

<a id="r_ga8dd114e35b6b12f157d5338b608a885f"></a>

```c
#define FOCALTECH_RESET_SEC_DET FOCALTECH_RESET_CONFIG(IPSRSTCR, 27U)
```

相关声明：[FOCALTECH_RESET_SEC_DET](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga8dd114e35b6b12f157d5338b608a885f)。

安全检测器复位（Security Detector Reset）。

<a id="r_gabf7202867a4dc81cb164e3e11a9497d3"></a>

```c
#define FOCALTECH_RESET_PCI FOCALTECH_RESET_CONFIG(IPSRSTCR, 28U)
```

相关声明：[FOCALTECH_RESET_PCI](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gabf7202867a4dc81cb164e3e11a9497d3)。

PCI 复位（Reset）。

<a id="r_ga6e2d8cd9384878ec751c01ca376c1396"></a>

```c
#define FOCALTECH_RESET_PMURTC FOCALTECH_RESET_CONFIG(IPSRSTCR, 29U)
```

相关声明：[FOCALTECH_RESET_PMURTC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga6e2d8cd9384878ec751c01ca376c1396)。

PMU RTC 复位（Reset）。

<a id="r_gab80962f564341a6bee51a9ef9f324602"></a>

```c
#define FOCALTECH_RESET_AHB2IPS FOCALTECH_RESET_CONFIG(IPSRSTCR, 30U)
```

相关声明：[FOCALTECH_RESET_AHB2IPS](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gab80962f564341a6bee51a9ef9f324602)。

AHB2IPS 复位（Reset）。

<a id="r_gacf8695dc4f1041d436a6d79ea3115eb5"></a>

```c
#define FOCALTECH_RESET_PWMT3 FOCALTECH_RESET_CONFIG(IPSRSTCR, 31U)
```

相关声明：[FOCALTECH_RESET_PWMT3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gacf8695dc4f1041d436a6d79ea3115eb5)。

PWMT3 复位（Reset）。


## 13.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P267_focaltech_ft9001_reset.h_源码浏览.md)
- [FOCALTECH_EPORTRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga14b208f0a5eb8e54f8cccb622896f367)
- [FOCALTECH_MULTIRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gabfd52f09e8021a6a4a88ea9545edd4ac)
- [FOCALTECH_SYSRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga943200e23ff31dce4a36b68b0664def7)
- [FOCALTECH_AHB3RSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gaa62d0bb8b7627d258095ef599ea803d0)
- [FOCALTECH_ARITHRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#ga386d01a7838235774815997a33f77577)
- [FOCALTECH_IPSRSTCR_OFFSET](../api_protocol_topic_reference/P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md#gaa9c609bd1da838111513b2c5e78588ca)
- [FOCALTECH_RESET_EPORT0](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gac1532022c40bd7d071e3597d70e7d0f4)
- [FOCALTECH_RESET_EPORT1](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga9bdbff48cb55369a4b194785a9dd14a1)
- [FOCALTECH_RESET_EPORT2](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga1c731760579999f96687b8a81c61dc3e)
- [FOCALTECH_RESET_EPORT3](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gac2c04d30326e36e4e7b284e9852803a3)
- [FOCALTECH_RESET_EPORT4](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga15510335513f34201b7acb6239063d93)
- [FOCALTECH_RESET_EPORT5](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gaa72200eab0c7dc5daf7750c425a5c5a2)
- [FOCALTECH_RESET_EPORT6](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga661d0cbcdff6e303f0c155c7fe7fe232)
- [FOCALTECH_RESET_EPORT7](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gab608960b531c74daff4e6816ce8e4abf)
- [FOCALTECH_RESET_ACMP1](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#ga66e82f86157f87b7c1e6a417bc5ac73d)
- [FOCALTECH_RESET_ACMP2](../api_network_time_topic_reference/P012_EPORTRSTR 复位控制（Reset Control）.md#gafa0d499c4c67e8a7028383d3d67a8c75)
- [FOCALTECH_RESET_OTP_AHB](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga46bbd9e1b3d0b62f61fabbaa8c334adc)
- [FOCALTECH_RESET_MCC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gaeee18837dae2087428921fcfcb556675)
- [FOCALTECH_RESET_MCCADR](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga0983a1b5886dfb370dbf9e2f705e441f)
- [FOCALTECH_RESET_ADC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga912e26cdf2b90bd075e1a69b425c97b2)
- [FOCALTECH_RESET_MESH](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga7ed484674341a911a948cff1d4594c9a)
- [FOCALTECH_RESET_TC](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gab46b7e24dfde17907d3ebeb640afcdb9)
- [FOCALTECH_RESET_CLKOUT](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gad58737d782cc2495d5bc173b6f02a0ff)
- [FOCALTECH_RESET_KEY_CTRL](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga5536cbd12d63c541b93b3afc8b7279ad)
- [FOCALTECH_RESET_CCM_RESET](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gac2740388f9e13c9a41dbf519f4d81b1e)
- [FOCALTECH_RESET_OTP_IPS](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga19ea0b41ff1d420fdd621231bc7f5620)
- [FOCALTECH_RESET_CPM_IPS](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga82036818a156d4e471c4292382ebf4b4)
- [FOCALTECH_RESET_TRACE](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga2089134755b7e42d06d75959cb630520)
- [FOCALTECH_RESET_I2S_M](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gad5f1147d63f910091e73a2963dc34849)
- [FOCALTECH_RESET_I2S_S](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#ga3f74b242e0fa83ed8e80e38dc11847ff)
- [FOCALTECH_RESET_CRC0](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gab704c34447390a3a45a959175026f201)
- [FOCALTECH_RESET_CRC1](../api_transport_control_topic_reference/P007_MULTIRSTCR 复位控制（Reset Control）.md#gaa05b6ae8e4720ff54d0a6586534496c9)
- [FOCALTECH_RESET_SSISLV1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga59d4227c9bf1489f8677cc93acb9c51c)
- [FOCALTECH_RESET_DMAC1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gadf58c3c5d2308e7c65f6b76985344f1a)
- [FOCALTECH_RESET_DMAC2](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gaf267ed4b27b192b8f33070b946814643)
- [FOCALTECH_RESET_AHB2_MUX](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga7efb131ead62ca3029a5bd160b38e781)
- [FOCALTECH_RESET_PXLP1_AHB](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga5c79ce9cd726c2350ed604294657c825)
- [FOCALTECH_RESET_PXLP2_AHB](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga41b21e2f451c2e8defd1ebb7badca937)
- [FOCALTECH_RESET_SRAMD](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga783ae3aa688eb9abe2d457051f35bb83)
- [FOCALTECH_RESET_SRAM0](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga5101183f616716b3266d03b6d03c0d7c)
- [FOCALTECH_RESET_SRAM1](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga4cae816aba6332bf0cbf0adb38d618f1)
- [FOCALTECH_RESET_SRAM2](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga70ac8466cce6411a8e159d6dded280e5)
- [FOCALTECH_RESET_SRAM3_4](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#gaa8b5763ee7e1ac184a28ec21d63e0d09)
- [FOCALTECH_RESET_SSI4](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga484a4ec976b714c56db3bd6fa2fce500)
- [FOCALTECH_RESET_SSI5](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga4a40dfcde87bf329e95d75960f40cb17)
- [FOCALTECH_RESET_SSI6](../api_interaction_transport_topic_reference/P003_SYSRSTCR 复位控制（Reset Control）.md#ga61a5a9485deb12d5b4df72bd7e9ed4fd)
- [FOCALTECH_RESET_ROM](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga447851fbf278af65b38904e30045fc19)
- [FOCALTECH_RESET_ROM_OTP_MUX](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gab429b3964b5c228cce44c270c964e0ee)
- [FOCALTECH_RESET_AHB3_MUX](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gaf33f88c4f792b7529f075fbd83b01e71)
- [FOCALTECH_RESET_USBC](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga743a6041380923309cc652cddab980a8)
- [FOCALTECH_RESET_PXLP1_APB](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gad76e8b42e772894a25fff56c91e46b08)
- [FOCALTECH_RESET_PXLP2_APB](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#gaa3710eb031f196eb13d98b9a34c6813c)
- [FOCALTECH_RESET_I2S1](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga03a88cdec31ee479b648d16609f3f1de)
- [FOCALTECH_RESET_I2S2](../api_auxiliary_topic_reference/P008_AHB3RSTCR 复位控制（Reset Control）.md#ga9472bf1174ae07a3b1bb0fbda422742e)
- [FOCALTECH_RESET_AES](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga429695ee2f576fc6a3357241aa38c215)
- [FOCALTECH_RESET_SM4](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga7524cad266f64ab27830a8deb266bedd)
- [FOCALTECH_RESET_RF_AES_SM4](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga1034fb963eb617815f8028bff5e5bcc7)
- [FOCALTECH_RESET_CRYPTO](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga1e3477301447a988b3f2ce831172b4a8)
- [FOCALTECH_RESET_SHA](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gaf3941bb54a85acdd59b995844b21bd42)
- [FOCALTECH_RESET_EDMAC0](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga8766e97447e1418adc43ad93cef51ba6)
- [FOCALTECH_RESET_DES](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gadf9a12c842552043611970bf7f657df3)
- [FOCALTECH_RESET_ZUC](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#ga23e239f9738c819a2fe24016768c6995)
- [FOCALTECH_RESET_AHB2MLB](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gad5e83816e598adb358d726c941892fa7)
- [FOCALTECH_RESET_AHB2IPS2](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gad54c36e48530d8cf63b8d83a5e536ae5)
- [FOCALTECH_RESET_TRNG](../api_vector_pipeline_topic_reference/P008_ARITHRSTCR 复位控制（Reset Control）.md#gaa9011c2f1c02ea6b256155ef5fde3e05)
- [FOCALTECH_RESET_IO_CTRL](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga60a6a9f5ef12bdb1ad5909c992234faa)
- [FOCALTECH_RESET_WDT](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga23196071f4d02b825b2e40fbc648b97a)
- [FOCALTECH_RESET_RTC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga4875113ccb459b1e6e264de54c2ffc0a)
- [FOCALTECH_RESET_PIT1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gad973fbc73a970d07d6ad470f1b309ca4)
- [FOCALTECH_RESET_PIT2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga38943fdef6b7ee8417576078f85cf382)
- [FOCALTECH_RESET_USI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga3ba939af141dff4f65cda43668ae8888)
- [FOCALTECH_RESET_EDMAC1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gacf9093e53fb0385eb90e66ef0f65f8de)
- [FOCALTECH_RESET_SPI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gadbced14265c08f7f8e234531d6e0abf7)
- [FOCALTECH_RESET_SPI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gabbe5f32ac775072810f02e779499462b)
- [FOCALTECH_RESET_SPI3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga7281304a265cfd95b48fd7420f9f2027)
- [FOCALTECH_RESET_SCI1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga64d3fe882d3dbeb6ccd8218538a99fbf)
- [FOCALTECH_RESET_SCI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga31b2bc4472d7455de72217216b9c068f)
- [FOCALTECH_RESET_USI2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga75c151a5750135c086893af842fe167d)
- [FOCALTECH_RESET_CAN1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga27413ec5515407960d47d4942e21e3e7)
- [FOCALTECH_RESET_I2C1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga721c4e8eaad920f3990547280a51de46)
- [FOCALTECH_RESET_PWM0](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga60d731d5f1b8f2219c842a94002fa14c)
- [FOCALTECH_RESET_I2C2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gad3af6cad5d8ae27b40d0bb8a319e3d31)
- [FOCALTECH_RESET_CAN2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga1a390c4c955ad9a7889b4106e31c7c03)
- [FOCALTECH_RESET_SCI3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga3b1fdc9f2d6f32ca105ccfd78d193cad)
- [FOCALTECH_RESET_QADC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga5fc20fe7b8c04946b5e98da6e10c3225)
- [FOCALTECH_RESET_DAC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gae919d9192d4e02630de012bfb2bac18c)
- [FOCALTECH_RESET_MCC_IPS](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gac467218bae41cd35bb93335deb6197f8)
- [FOCALTECH_RESET_PWMT1](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga49d792f2fff8f95d671689279b9e8b11)
- [FOCALTECH_RESET_LD](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga48331ab9690d7499fd8cfbcffb9705a9)
- [FOCALTECH_RESET_PWMT2](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gac45d20a806ae571f15c120ddf30cb91c)
- [FOCALTECH_RESET_PGD](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gaa4d9885a8d24489bd4dfab44ee62eeed)
- [FOCALTECH_RESET_SEC_DET](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga8dd114e35b6b12f157d5338b608a885f)
- [FOCALTECH_RESET_PCI](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gabf7202867a4dc81cb164e3e11a9497d3)
- [FOCALTECH_RESET_PMURTC](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#ga6e2d8cd9384878ec751c01ca376c1396)
- [FOCALTECH_RESET_AHB2IPS](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gab80962f564341a6bee51a9ef9f324602)
- [FOCALTECH_RESET_PWMT3](../api_buffer_paging_topic_reference/P007_IPSRSTCR 复位控制（Reset Control）.md#gacf8695dc4f1041d436a6d79ea3115eb5)

<a id="header-details"></a>

---

[上一章](P012_zephyr__dt-bindings__clock__esp32s3_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__misc__ft8xx__ft8xx_copro.h_文件参考.md)
