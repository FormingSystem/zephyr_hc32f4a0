---
id: learning.zephyr-docs.api-file-configuration-reference.page-1
title: zephyr__dt-bindings__gpio__adi-sdp-120.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi-sdp-120_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_gpio\_\_adi-sdp-120.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adi-sdp-120_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Copyright (c) 2024 Analog Devices Inc.

查看此文件的源码。

<a id="details"></a>

版权所有（Copyright）2024 Analog Devices Inc.；版权所有（Copyright）2024 Baylibre, SAS。SPDX-License-Identifier: Apache-2.0。

SDP-120 GPIO 索引定义（GPIO Index Definitions）。这些定义应与 `adi,sdp-120` ADI SDP-120 映射（Mapping）配合使用。用法示例（Example Usage）：

```c
&spi1 {
        cs-gpios = <&sdp_120 SDP_120_SPI_SS_N GPIO_ACTIVE_LOW>;

        example_device: example-dev@0 {
                compatible = "vnd,spi-device";
                reg = <0>;
        };
};
```

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_a92ae0ab5dc11a6de9fe4436c497b6174"></a>

```c
#define SDP_120_IO(n)
```

相关声明：[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

SDP-120 GPIO 连接节点（Nexus Node）上的 `IO[n]` 信号。

<a id="r_aee741ae2a6bc2581ac2c4bb32a56aef7"></a>

```c
#define SDP_120_SPI_D2 SDP_120_IO(33) /* SPI_D2 */
```

相关声明：[SDP_120_SPI_D2](#aee741ae2a6bc2581ac2c4bb32a56aef7)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a9ed3217c827aa9f2262fa5bd77fbf11b"></a>

```c
#define SDP_120_SPI_D3 SDP_120_IO(34) /* SPI_D3 */
```

相关声明：[SDP_120_SPI_D3](#a9ed3217c827aa9f2262fa5bd77fbf11b)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a8e2bc0d10b7bff636da4f83b78f5aabc"></a>

```c
#define SDP_120_SERIAL_INT SDP_120_IO(35) /* SERIAL_INT */
```

相关声明：[SDP_120_SERIAL_INT](#a8e2bc0d10b7bff636da4f83b78f5aabc)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ad0630139116e6af22329af773a5dfc58"></a>

```c
#define SDP_120_SPI_SEL_B_N SDP_120_IO(37) /* SPI_SEL_B_N */
```

相关声明：[SDP_120_SPI_SEL_B_N](#ad0630139116e6af22329af773a5dfc58)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_acc00b195bf35cdea02ae02824c46a8bc"></a>

```c
#define SDP_120_SPI_SEL_C_N SDP_120_IO(38) /* SPI_SEL_C_N */
```

相关声明：[SDP_120_SPI_SEL_C_N](#acc00b195bf35cdea02ae02824c46a8bc)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a7bd3994cd8d15c7abc8f4c8c2cd0c935"></a>

```c
#define SDP_120_SPI_SS_N SDP_120_IO(39) /* SPI_SS_N */
```

相关声明：[SDP_120_SPI_SS_N](#a7bd3994cd8d15c7abc8f4c8c2cd0c935)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_add120c01738682c1bafb3e0709af107b"></a>

```c
#define SDP_120_GPIO0 SDP_120_IO(43) /* GPIO0 */
```

相关声明：[SDP_120_GPIO0](#add120c01738682c1bafb3e0709af107b)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a0ac1ea00a661fd760dbbe6d3d95e5cdb"></a>

```c
#define SDP_120_GPIO2 SDP_120_IO(44) /* GPIO2 */
```

相关声明：[SDP_120_GPIO2](#a0ac1ea00a661fd760dbbe6d3d95e5cdb)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ac6d9aadae724e4423475da16b04e2531"></a>

```c
#define SDP_120_GPIO4 SDP_120_IO(45) /* GPIO4 */
```

相关声明：[SDP_120_GPIO4](#ac6d9aadae724e4423475da16b04e2531)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a1a1f15052ff7cf0a1b39f9aee922dc83"></a>

```c
#define SDP_120_GPIO6 SDP_120_IO(47) /* GPIO6 */
```

相关声明：[SDP_120_GPIO6](#a1a1f15052ff7cf0a1b39f9aee922dc83)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a17e46db1c2848751cbff6cdc4f013bf5"></a>

```c
#define SDP_120_TMR_A SDP_120_IO(48) /* TMR_A */
```

相关声明：[SDP_120_TMR_A](#a17e46db1c2848751cbff6cdc4f013bf5)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a7ef869f19822b0866dd5cc8cf15d77b6"></a>

```c
#define SDP_120_UART_RX SDP_120_IO(59) /* UART2_RX */
```

相关声明：[SDP_120_UART_RX](#a7ef869f19822b0866dd5cc8cf15d77b6)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a816693d1532b48588f91fee54e78fd43"></a>

```c
#define SDP_120_UART_TX SDP_120_IO(62) /* UART2_TX */
```

相关声明：[SDP_120_UART_TX](#a816693d1532b48588f91fee54e78fd43)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_afe0bd2dd3b90e13d8973f087a2ccba6d"></a>

```c
#define SDP_120_TMR_D SDP_120_IO(72) /* TMR_D */
```

相关声明：[SDP_120_TMR_D](#afe0bd2dd3b90e13d8973f087a2ccba6d)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ae6861bfd6c1903f6cef4e20dde2c8307"></a>

```c
#define SDP_120_TMR_B SDP_120_IO(73) /* TMR_B */
```

相关声明：[SDP_120_TMR_B](#ae6861bfd6c1903f6cef4e20dde2c8307)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_aff11d960caef06059ad60cd0bc9d9649"></a>

```c
#define SDP_120_GPIO7 SDP_120_IO(74) /* GPIO7 */
```

相关声明：[SDP_120_GPIO7](#aff11d960caef06059ad60cd0bc9d9649)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a9b25021cd21089ffe45f447b3327f7e5"></a>

```c
#define SDP_120_GPIO5 SDP_120_IO(76) /* GPIO5 */
```

相关声明：[SDP_120_GPIO5](#a9b25021cd21089ffe45f447b3327f7e5)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a64dfbef1a64613dc18241199c3cfd1c2"></a>

```c
#define SDP_120_GPIO3 SDP_120_IO(77) /* GPIO3 */
```

相关声明：[SDP_120_GPIO3](#a64dfbef1a64613dc18241199c3cfd1c2)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a70d8426587c4497729eea1c9e201a53e"></a>

```c
#define SDP_120_GPIO1 SDP_120_IO(78) /* GPIO1 */
```

相关声明：[SDP_120_GPIO1](#a70d8426587c4497729eea1c9e201a53e)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ac43d3d5c6b9d35677821ef0184027577"></a>

```c
#define SDP_120_SCL_0 SDP_120_IO(79) /* SCL_0 */
```

相关声明：[SDP_120_SCL_0](#ac43d3d5c6b9d35677821ef0184027577)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a34cdc1330a64c8980a40052f380b3a25"></a>

```c
#define SDP_120_SDA_0 SDP_120_IO(80) /* SDA_0 */
```

相关声明：[SDP_120_SDA_0](#a34cdc1330a64c8980a40052f380b3a25)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ad13ae79930628584fb9eef6ee00f7103"></a>

```c
#define SDP_120_SPI_CLK SDP_120_IO(82) /* SPI_CLK */
```

相关声明：[SDP_120_SPI_CLK](#ad13ae79930628584fb9eef6ee00f7103)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a5c9a67e842262480a257f1e771f3bac4"></a>

```c
#define SDP_120_SPI_MISO SDP_120_IO(83) /* SPI_MISO */
```

相关声明：[SDP_120_SPI_MISO](#a5c9a67e842262480a257f1e771f3bac4)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ac45042556abbcb2b70738bb06a2f6f17"></a>

```c
#define SDP_120_SPI_MOSI SDP_120_IO(84) /* SPI_MOSI */
```

相关声明：[SDP_120_SPI_MOSI](#ac45042556abbcb2b70738bb06a2f6f17)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ae25f3acec680970f67ae1cdf57df9adb"></a>

```c
#define SDP_120_SPI_SEL_A_N SDP_120_IO(85) /* SPI_SEL_A_N */
```

相关声明：[SDP_120_SPI_SEL_A_N](#ae25f3acec680970f67ae1cdf57df9adb)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_aa7d9c2aacf247c057d9dd36a7fd37610"></a>

```c
#define SDP_120_SPI_SPORT_TSCLK SDP_120_IO(87) /* SPORT_TSCLK */
```

相关声明：[SDP_120_SPI_SPORT_TSCLK](#aa7d9c2aacf247c057d9dd36a7fd37610)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_ae07a46b852400aca6408948f54ccd6d3"></a>

```c
#define SDP_120_SPI_SPORT_DT0 SDP_120_IO(88) /* SPORT_DT0 */
```

相关声明：[SDP_120_SPI_SPORT_DT0](#ae07a46b852400aca6408948f54ccd6d3)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_aabc39d3cacfb51a0b5f6db48947750e2"></a>

```c
#define SDP_120_SPI_SPORT_TFS SDP_120_IO(89) /* SPORT_TFS */
```

相关声明：[SDP_120_SPI_SPORT_TFS](#aabc39d3cacfb51a0b5f6db48947750e2)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a19b87a9e7e924aad756e70df72b0a2f9"></a>

```c
#define SDP_120_SPI_SPORT_RFS SDP_120_IO(90) /* SPORT_RFS */
```

相关声明：[SDP_120_SPI_SPORT_RFS](#a19b87a9e7e924aad756e70df72b0a2f9)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a6346b80db55747c4ad2e10051616b168"></a>

```c
#define SDP_120_SPI_SPORT_DR0 SDP_120_IO(91) /* SPORT_DR0 */
```

相关声明：[SDP_120_SPI_SPORT_DR0](#a6346b80db55747c4ad2e10051616b168)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

<a id="r_a5f06bebd3dcaf01c3eefc6ffc9a2c3cf"></a>

```c
#define SDP_120_SPI_SPORT_RSCLK SDP_120_IO(92) /* SPORT_RSCLK */
```

相关声明：[SDP_120_SPI_SPORT_RSCLK](#a5f06bebd3dcaf01c3eefc6ffc9a2c3cf)、[SDP_120_IO](#a92ae0ab5dc11a6de9fe4436c497b6174)。

## 1.2\_详细说明（Detailed Documentation）

<a id="add120c01738682c1bafb3e0709af107b"></a>

### `SDP_120_GPIO0`

```c
#define SDP_120_GPIO0 SDP_120_IO(43) /* GPIO0 */
```

<a id="a70d8426587c4497729eea1c9e201a53e"></a>

### `SDP_120_GPIO1`

```c
#define SDP_120_GPIO1 SDP_120_IO(78) /* GPIO1 */
```

<a id="a0ac1ea00a661fd760dbbe6d3d95e5cdb"></a>

### `SDP_120_GPIO2`

```c
#define SDP_120_GPIO2 SDP_120_IO(44) /* GPIO2 */
```

<a id="a64dfbef1a64613dc18241199c3cfd1c2"></a>

### `SDP_120_GPIO3`

```c
#define SDP_120_GPIO3 SDP_120_IO(77) /* GPIO3 */
```

<a id="ac6d9aadae724e4423475da16b04e2531"></a>

### `SDP_120_GPIO4`

```c
#define SDP_120_GPIO4 SDP_120_IO(45) /* GPIO4 */
```

<a id="a9b25021cd21089ffe45f447b3327f7e5"></a>

### `SDP_120_GPIO5`

```c
#define SDP_120_GPIO5 SDP_120_IO(76) /* GPIO5 */
```

<a id="a1a1f15052ff7cf0a1b39f9aee922dc83"></a>

### `SDP_120_GPIO6`

```c
#define SDP_120_GPIO6 SDP_120_IO(47) /* GPIO6 */
```

<a id="aff11d960caef06059ad60cd0bc9d9649"></a>

### `SDP_120_GPIO7`

```c
#define SDP_120_GPIO7 SDP_120_IO(74) /* GPIO7 */
```

<a id="a92ae0ab5dc11a6de9fe4436c497b6174"></a>

### `SDP_120_IO`

```c
#define SDP_120_IO ( n)
```

展开值（Value）：

```c
(n-1)
```

SDP-120 GPIO 连接节点（Nexus Node）上的 `IO[n]` 信号。

<a id="ac43d3d5c6b9d35677821ef0184027577"></a>

### `SDP_120_SCL_0`

```c
#define SDP_120_SCL_0 SDP_120_IO(79) /* SCL_0 */
```

<a id="a34cdc1330a64c8980a40052f380b3a25"></a>

### `SDP_120_SDA_0`

```c
#define SDP_120_SDA_0 SDP_120_IO(80) /* SDA_0 */
```

<a id="a8e2bc0d10b7bff636da4f83b78f5aabc"></a>

### `SDP_120_SERIAL_INT`

```c
#define SDP_120_SERIAL_INT SDP_120_IO(35) /* SERIAL_INT */
```

<a id="ad13ae79930628584fb9eef6ee00f7103"></a>

### `SDP_120_SPI_CLK`

```c
#define SDP_120_SPI_CLK SDP_120_IO(82) /* SPI_CLK */
```

<a id="aee741ae2a6bc2581ac2c4bb32a56aef7"></a>

### `SDP_120_SPI_D2`

```c
#define SDP_120_SPI_D2 SDP_120_IO(33) /* SPI_D2 */
```

<a id="a9ed3217c827aa9f2262fa5bd77fbf11b"></a>

### `SDP_120_SPI_D3`

```c
#define SDP_120_SPI_D3 SDP_120_IO(34) /* SPI_D3 */
```

<a id="a5c9a67e842262480a257f1e771f3bac4"></a>

### `SDP_120_SPI_MISO`

```c
#define SDP_120_SPI_MISO SDP_120_IO(83) /* SPI_MISO */
```

<a id="ac45042556abbcb2b70738bb06a2f6f17"></a>

### `SDP_120_SPI_MOSI`

```c
#define SDP_120_SPI_MOSI SDP_120_IO(84) /* SPI_MOSI */
```

<a id="ae25f3acec680970f67ae1cdf57df9adb"></a>

### `SDP_120_SPI_SEL_A_N`

```c
#define SDP_120_SPI_SEL_A_N SDP_120_IO(85) /* SPI_SEL_A_N */
```

<a id="ad0630139116e6af22329af773a5dfc58"></a>

### `SDP_120_SPI_SEL_B_N`

```c
#define SDP_120_SPI_SEL_B_N SDP_120_IO(37) /* SPI_SEL_B_N */
```

<a id="acc00b195bf35cdea02ae02824c46a8bc"></a>

### `SDP_120_SPI_SEL_C_N`

```c
#define SDP_120_SPI_SEL_C_N SDP_120_IO(38) /* SPI_SEL_C_N */
```

<a id="a6346b80db55747c4ad2e10051616b168"></a>

### `SDP_120_SPI_SPORT_DR0`

```c
#define SDP_120_SPI_SPORT_DR0 SDP_120_IO(91) /* SPORT_DR0 */
```

<a id="ae07a46b852400aca6408948f54ccd6d3"></a>

### `SDP_120_SPI_SPORT_DT0`

```c
#define SDP_120_SPI_SPORT_DT0 SDP_120_IO(88) /* SPORT_DT0 */
```

<a id="a19b87a9e7e924aad756e70df72b0a2f9"></a>

### `SDP_120_SPI_SPORT_RFS`

```c
#define SDP_120_SPI_SPORT_RFS SDP_120_IO(90) /* SPORT_RFS */
```

<a id="a5f06bebd3dcaf01c3eefc6ffc9a2c3cf"></a>

### `SDP_120_SPI_SPORT_RSCLK`

```c
#define SDP_120_SPI_SPORT_RSCLK SDP_120_IO(92) /* SPORT_RSCLK */
```

<a id="aabc39d3cacfb51a0b5f6db48947750e2"></a>

### `SDP_120_SPI_SPORT_TFS`

```c
#define SDP_120_SPI_SPORT_TFS SDP_120_IO(89) /* SPORT_TFS */
```

<a id="aa7d9c2aacf247c057d9dd36a7fd37610"></a>

### `SDP_120_SPI_SPORT_TSCLK`

```c
#define SDP_120_SPI_SPORT_TSCLK SDP_120_IO(87) /* SPORT_TSCLK */
```

<a id="a7bd3994cd8d15c7abc8f4c8c2cd0c935"></a>

### `SDP_120_SPI_SS_N`

```c
#define SDP_120_SPI_SS_N SDP_120_IO(39) /* SPI_SS_N */
```

<a id="a17e46db1c2848751cbff6cdc4f013bf5"></a>

### `SDP_120_TMR_A`

```c
#define SDP_120_TMR_A SDP_120_IO(48) /* TMR_A */
```

<a id="ae6861bfd6c1903f6cef4e20dde2c8307"></a>

### `SDP_120_TMR_B`

```c
#define SDP_120_TMR_B SDP_120_IO(73) /* TMR_B */
```

<a id="afe0bd2dd3b90e13d8973f087a2ccba6d"></a>

### `SDP_120_TMR_D`

```c
#define SDP_120_TMR_D SDP_120_IO(72) /* TMR_D */
```

<a id="a7ef869f19822b0866dd5cc8cf15d77b6"></a>

### `SDP_120_UART_RX`

```c
#define SDP_120_UART_RX SDP_120_IO(59) /* UART2_RX */
```

<a id="a816693d1532b48588f91fee54e78fd43"></a>

### `SDP_120_UART_TX`

```c
#define SDP_120_UART_TX SDP_120_IO(62) /* UART2_TX */
```


## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/adi-sdp-120_8h_source.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__adi_max32_clock.h_文件参考.md)
