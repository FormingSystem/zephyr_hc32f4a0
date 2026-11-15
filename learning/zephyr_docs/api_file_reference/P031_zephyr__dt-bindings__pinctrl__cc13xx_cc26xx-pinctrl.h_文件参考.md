---
id: learning.zephyr-docs.api-file-reference.page-31
title: zephyr__dt-bindings__pinctrl__cc13xx_cc26xx-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cc13xx__cc26xx-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_cc13xx\_cc26xx-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cc13xx__cc26xx-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="r_a28f8e101ae30e86989a5c7b35be8f2d1"></a>

```c
#define IOC_PORT_GPIO 0x00000000 /* Default general purpose IO usage */
```

相关声明：[IOC_PORT_GPIO](#a28f8e101ae30e86989a5c7b35be8f2d1)。

<a id="r_a2dade73b9db2292ee357ec1ae92ed2d0"></a>

```c
#define IOC_PORT_AON_CLK32K 0x00000007 /* AON External 32kHz clock */
```

相关声明：[IOC_PORT_AON_CLK32K](#a2dade73b9db2292ee357ec1ae92ed2d0)。

<a id="r_a1b04b35124c351075fe3974adeb4d9aa"></a>

```c
#define IOC_PORT_AUX_IO 0x00000008 /* AUX IO Pin */
```

相关声明：[IOC_PORT_AUX_IO](#a1b04b35124c351075fe3974adeb4d9aa)。

<a id="r_a3ee91cd12de013161c91f231676b279c"></a>

```c
#define IOC_PORT_MCU_SSI0_RX 0x00000009 /* MCU SSI0 Receive Pin */
```

相关声明：[IOC_PORT_MCU_SSI0_RX](#a3ee91cd12de013161c91f231676b279c)。

<a id="r_a984735dec2b09061ab1be699a708367f"></a>

```c
#define IOC_PORT_MCU_SSI0_TX 0x0000000A /* MCU SSI0 Transmit Pin */
```

相关声明：[IOC_PORT_MCU_SSI0_TX](#a984735dec2b09061ab1be699a708367f)。

<a id="r_a5e72bbc3a52d1bd643059f9a2037db03"></a>

```c
#define IOC_PORT_MCU_SSI0_FSS 0x0000000B /* MCU SSI0 FSS Pin */
```

相关声明：[IOC_PORT_MCU_SSI0_FSS](#a5e72bbc3a52d1bd643059f9a2037db03)。

<a id="r_acfeabd6ba536f550b52c98eba600f99c"></a>

```c
#define IOC_PORT_MCU_SSI0_CLK 0x0000000C /* MCU SSI0 Clock Pin */
```

相关声明：[IOC_PORT_MCU_SSI0_CLK](#acfeabd6ba536f550b52c98eba600f99c)。

<a id="r_aa318c337f1371b5f81ebf427a43cf318"></a>

```c
#define IOC_PORT_MCU_I2C_MSSDA 0x0000000D /* MCU I2C Data Pin */
```

相关声明：[IOC_PORT_MCU_I2C_MSSDA](#aa318c337f1371b5f81ebf427a43cf318)。

<a id="r_a7d3e1312e3803326770e4d734e25b2eb"></a>

```c
#define IOC_PORT_MCU_I2C_MSSCL 0x0000000E /* MCU I2C Clock Pin */
```

相关声明：[IOC_PORT_MCU_I2C_MSSCL](#a7d3e1312e3803326770e4d734e25b2eb)。

<a id="r_aab1fbb3fbc8a90bd4d8fb1b55f69eb44"></a>

```c
#define IOC_PORT_MCU_UART0_RX 0x0000000F /* MCU UART0 Receive Pin */
```

相关声明：[IOC_PORT_MCU_UART0_RX](#aab1fbb3fbc8a90bd4d8fb1b55f69eb44)。

<a id="r_ac1adc319c3a412383fbd03d4dc9f08f5"></a>

```c
#define IOC_PORT_MCU_UART0_TX 0x00000010 /* MCU UART0 Transmit Pin */
```

相关声明：[IOC_PORT_MCU_UART0_TX](#ac1adc319c3a412383fbd03d4dc9f08f5)。

<a id="r_ad86b00b6011d22d55d31c8c2681edea8"></a>

```c
#define IOC_PORT_MCU_UART0_CTS 0x00000011 /* MCU UART0 Clear To Send Pin */
```

相关声明：[IOC_PORT_MCU_UART0_CTS](#ad86b00b6011d22d55d31c8c2681edea8)。

<a id="r_acdc4b3216e14a0525a9bff563c618505"></a>

```c
#define IOC_PORT_MCU_UART0_RTS 0x00000012 /* MCU UART0 Request To Send Pin */
```

相关声明：[IOC_PORT_MCU_UART0_RTS](#acdc4b3216e14a0525a9bff563c618505)。

<a id="r_a81eb684c41b27ab5c2e434f74cac653a"></a>

```c
#define IOC_PORT_MCU_UART1_RX 0x00000013 /* MCU UART1 Receive Pin */
```

相关声明：[IOC_PORT_MCU_UART1_RX](#a81eb684c41b27ab5c2e434f74cac653a)。

<a id="r_aabad6396786ac0fba4e030fa3bafaebe"></a>

```c
#define IOC_PORT_MCU_UART1_TX 0x00000014 /* MCU UART1 Transmit Pin */
```

相关声明：[IOC_PORT_MCU_UART1_TX](#aabad6396786ac0fba4e030fa3bafaebe)。

<a id="r_a3891eea57014086f4d9665c5659df9f9"></a>

```c
#define IOC_PORT_MCU_UART1_CTS 0x00000015 /* MCU UART1 Clear To Send Pin */
```

相关声明：[IOC_PORT_MCU_UART1_CTS](#a3891eea57014086f4d9665c5659df9f9)。

<a id="r_a07f27135f53b5f70c9cf611fee1da81c"></a>

```c
#define IOC_PORT_MCU_UART1_RTS 0x00000016 /* MCU UART1 Request To Send Pin */
```

相关声明：[IOC_PORT_MCU_UART1_RTS](#a07f27135f53b5f70c9cf611fee1da81c)。

<a id="r_abb2e44fdb358359785db59197e43bf77"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT0 0x00000017 /* MCU PORT EVENT 0 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT0](#abb2e44fdb358359785db59197e43bf77)。

<a id="r_a53158c583bdc22b05a3ab803976f86f3"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT1 0x00000018 /* MCU PORT EVENT 1 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT1](#a53158c583bdc22b05a3ab803976f86f3)。

<a id="r_a3c31d2aee7d57f0b939678d24489b288"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT2 0x00000019 /* MCU PORT EVENT 2 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT2](#a3c31d2aee7d57f0b939678d24489b288)。

<a id="r_af74865ea575600cdef510d96b765fcaa"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT3 0x0000001A /* MCU PORT EVENT 3 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT3](#af74865ea575600cdef510d96b765fcaa)。

<a id="r_a8c29bb202c04366637a067403cb04798"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT4 0x0000001B /* MCU PORT EVENT 4 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT4](#a8c29bb202c04366637a067403cb04798)。

<a id="r_a5018eb7bb384ce6240bc5ce37f684fd4"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT5 0x0000001C /* MCU PORT EVENT 5 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT5](#a5018eb7bb384ce6240bc5ce37f684fd4)。

<a id="r_a627f8281323ce4d84edc61c921e5fc35"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT6 0x0000001D /* MCU PORT EVENT 6 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT6](#a627f8281323ce4d84edc61c921e5fc35)。

<a id="r_ae058c9773b968e08c17f848e8a17e33e"></a>

```c
#define IOC_PORT_MCU_PORT_EVENT7 0x0000001E /* MCU PORT EVENT 7 */
```

相关声明：[IOC_PORT_MCU_PORT_EVENT7](#ae058c9773b968e08c17f848e8a17e33e)。

<a id="r_a5bf13b897900e2f62c82d84d23558c9b"></a>

```c
#define IOC_PORT_MCU_SWV 0x00000020 /* Serial Wire Viewer */
```

相关声明：[IOC_PORT_MCU_SWV](#a5bf13b897900e2f62c82d84d23558c9b)。

<a id="r_adc4c2aa534badaa6a40a994012968226"></a>

```c
#define IOC_PORT_MCU_SSI1_RX 0x00000021 /* MCU SSI1 Receive Pin */
```

相关声明：[IOC_PORT_MCU_SSI1_RX](#adc4c2aa534badaa6a40a994012968226)。

<a id="r_a9024a0c4d78a72ff56c12d9ef6bce984"></a>

```c
#define IOC_PORT_MCU_SSI1_TX 0x00000022 /* MCU SSI1 Transmit Pin */
```

相关声明：[IOC_PORT_MCU_SSI1_TX](#a9024a0c4d78a72ff56c12d9ef6bce984)。

<a id="r_a8517079f7b23895467d0c6c5cee74051"></a>

```c
#define IOC_PORT_MCU_SSI1_FSS 0x00000023 /* MCU SSI1 FSS Pin */
```

相关声明：[IOC_PORT_MCU_SSI1_FSS](#a8517079f7b23895467d0c6c5cee74051)。

<a id="r_aa657dc9b3b551a535207a5c70944c7ad"></a>

```c
#define IOC_PORT_MCU_SSI1_CLK 0x00000024 /* MCU SSI1 Clock Pin */
```

相关声明：[IOC_PORT_MCU_SSI1_CLK](#aa657dc9b3b551a535207a5c70944c7ad)。

<a id="r_ad8d7633125f181d03a832504ca0333af"></a>

```c
#define IOC_PORT_MCU_I2S_AD0 0x00000025 /* MCU I2S Data Pin 0 */
```

相关声明：[IOC_PORT_MCU_I2S_AD0](#ad8d7633125f181d03a832504ca0333af)。

<a id="r_a3e3c593f43d20f8b976104e4370e2bfe"></a>

```c
#define IOC_PORT_MCU_I2S_AD1 0x00000026 /* MCU I2S Data Pin 1 */
```

相关声明：[IOC_PORT_MCU_I2S_AD1](#a3e3c593f43d20f8b976104e4370e2bfe)。

<a id="r_a87f51f7808c53fb7a1d0ab0cfc7c3bfb"></a>

```c
#define IOC_PORT_MCU_I2S_WCLK 0x00000027 /* MCU I2S Frame/Word Clock */
```

相关声明：[IOC_PORT_MCU_I2S_WCLK](#a87f51f7808c53fb7a1d0ab0cfc7c3bfb)。

<a id="r_a27b5fe5cdbd768684939c52662ed919a"></a>

```c
#define IOC_PORT_MCU_I2S_BCLK 0x00000028 /* MCU I2S Bit Clock */
```

相关声明：[IOC_PORT_MCU_I2S_BCLK](#a27b5fe5cdbd768684939c52662ed919a)。

<a id="r_a72287ec0a2c5f0423e785d3e371a120e"></a>

```c
#define IOC_PORT_MCU_I2S_MCLK 0x00000029 /* MCU I2S Master clock 2 */
```

相关声明：[IOC_PORT_MCU_I2S_MCLK](#a72287ec0a2c5f0423e785d3e371a120e)。

<a id="r_ae6a1e66015d48324657ede92613381be"></a>

```c
#define IOC_PORT_RFC_TRC 0x0000002E /* RF Core Tracer */
```

相关声明：[IOC_PORT_RFC_TRC](#ae6a1e66015d48324657ede92613381be)。

<a id="r_a00a019e1ddf52b2913e8358c18095ed4"></a>

```c
#define IOC_PORT_RFC_GPO0 0x0000002F /* RC Core Data Out Pin 0 */
```

相关声明：[IOC_PORT_RFC_GPO0](#a00a019e1ddf52b2913e8358c18095ed4)。

<a id="r_a00ea75c9456ac6b11e666757750ae342"></a>

```c
#define IOC_PORT_RFC_GPO1 0x00000030 /* RC Core Data Out Pin 1 */
```

相关声明：[IOC_PORT_RFC_GPO1](#a00ea75c9456ac6b11e666757750ae342)。

<a id="r_a5f19fce0ef7c834714af2e7f1c2bd06d"></a>

```c
#define IOC_PORT_RFC_GPO2 0x00000031 /* RC Core Data Out Pin 2 */
```

相关声明：[IOC_PORT_RFC_GPO2](#a5f19fce0ef7c834714af2e7f1c2bd06d)。

<a id="r_ac940779073013ae6912da19fe598d999"></a>

```c
#define IOC_PORT_RFC_GPO3 0x00000032 /* RC Core Data Out Pin 3 */
```

相关声明：[IOC_PORT_RFC_GPO3](#ac940779073013ae6912da19fe598d999)。

<a id="r_af0c7ce805a62bed97029d997406e8ec7"></a>

```c
#define IOC_PORT_RFC_GPI0 0x00000033 /* RC Core Data In Pin 0 */
```

相关声明：[IOC_PORT_RFC_GPI0](#af0c7ce805a62bed97029d997406e8ec7)。

<a id="r_a6f1fc00a44a3311866187ce0c7470b1f"></a>

```c
#define IOC_PORT_RFC_GPI1 0x00000034 /* RC Core Data In Pin 1 */
```

相关声明：[IOC_PORT_RFC_GPI1](#a6f1fc00a44a3311866187ce0c7470b1f)。

<a id="r_a34286b14818f96f8e3955eebc3f453eb"></a>

```c
#define IOC_PORT_RFC_SMI_DL_OUT 0x00000035 /* RF Core SMI Data Link Out */
```

相关声明：[IOC_PORT_RFC_SMI_DL_OUT](#a34286b14818f96f8e3955eebc3f453eb)。

<a id="r_a38268821c556568eb9b8d0bd1b6bf4a4"></a>

```c
#define IOC_PORT_RFC_SMI_DL_IN 0x00000036 /* RF Core SMI Data Link in */
```

相关声明：[IOC_PORT_RFC_SMI_DL_IN](#a38268821c556568eb9b8d0bd1b6bf4a4)。

<a id="r_a8fa600a45bb7210a0a869232883a36d7"></a>

```c
#define IOC_PORT_RFC_SMI_CL_OUT 0x00000037 /* RF Core SMI Command Link Out */
```

相关声明：[IOC_PORT_RFC_SMI_CL_OUT](#a8fa600a45bb7210a0a869232883a36d7)。

<a id="r_a8955bb4c29c837e71983307d2fc46155"></a>

```c
#define IOC_PORT_RFC_SMI_CL_IN 0x00000038 /* RF Core SMI Command Link In */
```

相关声明：[IOC_PORT_RFC_SMI_CL_IN](#a8955bb4c29c837e71983307d2fc46155)。

<a id="r_a86134934e741c66f26bd4490e1f48553"></a>

```c
#define IOC_NO_EDGE 0x00000000 /* No edge detection */
```

相关声明：[IOC_NO_EDGE](#a86134934e741c66f26bd4490e1f48553)。

<a id="r_a812505ce5828cd40a9030f37445b7860"></a>

```c
#define IOC_FALLING_EDGE 0x00010000 /* Edge detection on falling edge */
```

相关声明：[IOC_FALLING_EDGE](#a812505ce5828cd40a9030f37445b7860)。

<a id="r_ac7124cf50c094bfc24313d88aa8c06f4"></a>

```c
#define IOC_RISING_EDGE 0x00020000 /* Edge detection on rising edge */
```

相关声明：[IOC_RISING_EDGE](#ac7124cf50c094bfc24313d88aa8c06f4)。

<a id="r_aff5b936c3bbd5bd0e9429c8c7ac5f6a8"></a>

```c
#define IOC_BOTH_EDGES 0x00030000 /* Edge detection on both edges */
```

相关声明：[IOC_BOTH_EDGES](#aff5b936c3bbd5bd0e9429c8c7ac5f6a8)。

## 31.2\_详细说明（Detailed Documentation）

<a id="aff5b936c3bbd5bd0e9429c8c7ac5f6a8"></a>

### `IOC_BOTH_EDGES`

```c
#define IOC_BOTH_EDGES 0x00030000 /* Edge detection on both edges */
```

<a id="a812505ce5828cd40a9030f37445b7860"></a>

### `IOC_FALLING_EDGE`

```c
#define IOC_FALLING_EDGE 0x00010000 /* Edge detection on falling edge */
```

<a id="a86134934e741c66f26bd4490e1f48553"></a>

### `IOC_NO_EDGE`

```c
#define IOC_NO_EDGE 0x00000000 /* No edge detection */
```

<a id="a2dade73b9db2292ee357ec1ae92ed2d0"></a>

### `IOC_PORT_AON_CLK32K`

```c
#define IOC_PORT_AON_CLK32K 0x00000007 /* AON External 32kHz clock */
```

<a id="a1b04b35124c351075fe3974adeb4d9aa"></a>

### `IOC_PORT_AUX_IO`

```c
#define IOC_PORT_AUX_IO 0x00000008 /* AUX IO Pin */
```

<a id="a28f8e101ae30e86989a5c7b35be8f2d1"></a>

### `IOC_PORT_GPIO`

```c
#define IOC_PORT_GPIO 0x00000000 /* Default general purpose IO usage */
```

<a id="a7d3e1312e3803326770e4d734e25b2eb"></a>

### `IOC_PORT_MCU_I2C_MSSCL`

```c
#define IOC_PORT_MCU_I2C_MSSCL 0x0000000E /* MCU I2C Clock Pin */
```

<a id="aa318c337f1371b5f81ebf427a43cf318"></a>

### `IOC_PORT_MCU_I2C_MSSDA`

```c
#define IOC_PORT_MCU_I2C_MSSDA 0x0000000D /* MCU I2C Data Pin */
```

<a id="ad8d7633125f181d03a832504ca0333af"></a>

### `IOC_PORT_MCU_I2S_AD0`

```c
#define IOC_PORT_MCU_I2S_AD0 0x00000025 /* MCU I2S Data Pin 0 */
```

<a id="a3e3c593f43d20f8b976104e4370e2bfe"></a>

### `IOC_PORT_MCU_I2S_AD1`

```c
#define IOC_PORT_MCU_I2S_AD1 0x00000026 /* MCU I2S Data Pin 1 */
```

<a id="a27b5fe5cdbd768684939c52662ed919a"></a>

### `IOC_PORT_MCU_I2S_BCLK`

```c
#define IOC_PORT_MCU_I2S_BCLK 0x00000028 /* MCU I2S Bit Clock */
```

<a id="a72287ec0a2c5f0423e785d3e371a120e"></a>

### `IOC_PORT_MCU_I2S_MCLK`

```c
#define IOC_PORT_MCU_I2S_MCLK 0x00000029 /* MCU I2S Master clock 2 */
```

<a id="a87f51f7808c53fb7a1d0ab0cfc7c3bfb"></a>

### `IOC_PORT_MCU_I2S_WCLK`

```c
#define IOC_PORT_MCU_I2S_WCLK 0x00000027 /* MCU I2S Frame/Word Clock */
```

<a id="abb2e44fdb358359785db59197e43bf77"></a>

### `IOC_PORT_MCU_PORT_EVENT0`

```c
#define IOC_PORT_MCU_PORT_EVENT0 0x00000017 /* MCU PORT EVENT 0 */
```

<a id="a53158c583bdc22b05a3ab803976f86f3"></a>

### `IOC_PORT_MCU_PORT_EVENT1`

```c
#define IOC_PORT_MCU_PORT_EVENT1 0x00000018 /* MCU PORT EVENT 1 */
```

<a id="a3c31d2aee7d57f0b939678d24489b288"></a>

### `IOC_PORT_MCU_PORT_EVENT2`

```c
#define IOC_PORT_MCU_PORT_EVENT2 0x00000019 /* MCU PORT EVENT 2 */
```

<a id="af74865ea575600cdef510d96b765fcaa"></a>

### `IOC_PORT_MCU_PORT_EVENT3`

```c
#define IOC_PORT_MCU_PORT_EVENT3 0x0000001A /* MCU PORT EVENT 3 */
```

<a id="a8c29bb202c04366637a067403cb04798"></a>

### `IOC_PORT_MCU_PORT_EVENT4`

```c
#define IOC_PORT_MCU_PORT_EVENT4 0x0000001B /* MCU PORT EVENT 4 */
```

<a id="a5018eb7bb384ce6240bc5ce37f684fd4"></a>

### `IOC_PORT_MCU_PORT_EVENT5`

```c
#define IOC_PORT_MCU_PORT_EVENT5 0x0000001C /* MCU PORT EVENT 5 */
```

<a id="a627f8281323ce4d84edc61c921e5fc35"></a>

### `IOC_PORT_MCU_PORT_EVENT6`

```c
#define IOC_PORT_MCU_PORT_EVENT6 0x0000001D /* MCU PORT EVENT 6 */
```

<a id="ae058c9773b968e08c17f848e8a17e33e"></a>

### `IOC_PORT_MCU_PORT_EVENT7`

```c
#define IOC_PORT_MCU_PORT_EVENT7 0x0000001E /* MCU PORT EVENT 7 */
```

<a id="acfeabd6ba536f550b52c98eba600f99c"></a>

### `IOC_PORT_MCU_SSI0_CLK`

```c
#define IOC_PORT_MCU_SSI0_CLK 0x0000000C /* MCU SSI0 Clock Pin */
```

<a id="a5e72bbc3a52d1bd643059f9a2037db03"></a>

### `IOC_PORT_MCU_SSI0_FSS`

```c
#define IOC_PORT_MCU_SSI0_FSS 0x0000000B /* MCU SSI0 FSS Pin */
```

<a id="a3ee91cd12de013161c91f231676b279c"></a>

### `IOC_PORT_MCU_SSI0_RX`

```c
#define IOC_PORT_MCU_SSI0_RX 0x00000009 /* MCU SSI0 Receive Pin */
```

<a id="a984735dec2b09061ab1be699a708367f"></a>

### `IOC_PORT_MCU_SSI0_TX`

```c
#define IOC_PORT_MCU_SSI0_TX 0x0000000A /* MCU SSI0 Transmit Pin */
```

<a id="aa657dc9b3b551a535207a5c70944c7ad"></a>

### `IOC_PORT_MCU_SSI1_CLK`

```c
#define IOC_PORT_MCU_SSI1_CLK 0x00000024 /* MCU SSI1 Clock Pin */
```

<a id="a8517079f7b23895467d0c6c5cee74051"></a>

### `IOC_PORT_MCU_SSI1_FSS`

```c
#define IOC_PORT_MCU_SSI1_FSS 0x00000023 /* MCU SSI1 FSS Pin */
```

<a id="adc4c2aa534badaa6a40a994012968226"></a>

### `IOC_PORT_MCU_SSI1_RX`

```c
#define IOC_PORT_MCU_SSI1_RX 0x00000021 /* MCU SSI1 Receive Pin */
```

<a id="a9024a0c4d78a72ff56c12d9ef6bce984"></a>

### `IOC_PORT_MCU_SSI1_TX`

```c
#define IOC_PORT_MCU_SSI1_TX 0x00000022 /* MCU SSI1 Transmit Pin */
```

<a id="a5bf13b897900e2f62c82d84d23558c9b"></a>

### `IOC_PORT_MCU_SWV`

```c
#define IOC_PORT_MCU_SWV 0x00000020 /* Serial Wire Viewer */
```

<a id="ad86b00b6011d22d55d31c8c2681edea8"></a>

### `IOC_PORT_MCU_UART0_CTS`

```c
#define IOC_PORT_MCU_UART0_CTS 0x00000011 /* MCU UART0 Clear To Send Pin */
```

<a id="acdc4b3216e14a0525a9bff563c618505"></a>

### `IOC_PORT_MCU_UART0_RTS`

```c
#define IOC_PORT_MCU_UART0_RTS 0x00000012 /* MCU UART0 Request To Send Pin */
```

<a id="aab1fbb3fbc8a90bd4d8fb1b55f69eb44"></a>

### `IOC_PORT_MCU_UART0_RX`

```c
#define IOC_PORT_MCU_UART0_RX 0x0000000F /* MCU UART0 Receive Pin */
```

<a id="ac1adc319c3a412383fbd03d4dc9f08f5"></a>

### `IOC_PORT_MCU_UART0_TX`

```c
#define IOC_PORT_MCU_UART0_TX 0x00000010 /* MCU UART0 Transmit Pin */
```

<a id="a3891eea57014086f4d9665c5659df9f9"></a>

### `IOC_PORT_MCU_UART1_CTS`

```c
#define IOC_PORT_MCU_UART1_CTS 0x00000015 /* MCU UART1 Clear To Send Pin */
```

<a id="a07f27135f53b5f70c9cf611fee1da81c"></a>

### `IOC_PORT_MCU_UART1_RTS`

```c
#define IOC_PORT_MCU_UART1_RTS 0x00000016 /* MCU UART1 Request To Send Pin */
```

<a id="a81eb684c41b27ab5c2e434f74cac653a"></a>

### `IOC_PORT_MCU_UART1_RX`

```c
#define IOC_PORT_MCU_UART1_RX 0x00000013 /* MCU UART1 Receive Pin */
```

<a id="aabad6396786ac0fba4e030fa3bafaebe"></a>

### `IOC_PORT_MCU_UART1_TX`

```c
#define IOC_PORT_MCU_UART1_TX 0x00000014 /* MCU UART1 Transmit Pin */
```

<a id="af0c7ce805a62bed97029d997406e8ec7"></a>

### `IOC_PORT_RFC_GPI0`

```c
#define IOC_PORT_RFC_GPI0 0x00000033 /* RC Core Data In Pin 0 */
```

<a id="a6f1fc00a44a3311866187ce0c7470b1f"></a>

### `IOC_PORT_RFC_GPI1`

```c
#define IOC_PORT_RFC_GPI1 0x00000034 /* RC Core Data In Pin 1 */
```

<a id="a00a019e1ddf52b2913e8358c18095ed4"></a>

### `IOC_PORT_RFC_GPO0`

```c
#define IOC_PORT_RFC_GPO0 0x0000002F /* RC Core Data Out Pin 0 */
```

<a id="a00ea75c9456ac6b11e666757750ae342"></a>

### `IOC_PORT_RFC_GPO1`

```c
#define IOC_PORT_RFC_GPO1 0x00000030 /* RC Core Data Out Pin 1 */
```

<a id="a5f19fce0ef7c834714af2e7f1c2bd06d"></a>

### `IOC_PORT_RFC_GPO2`

```c
#define IOC_PORT_RFC_GPO2 0x00000031 /* RC Core Data Out Pin 2 */
```

<a id="ac940779073013ae6912da19fe598d999"></a>

### `IOC_PORT_RFC_GPO3`

```c
#define IOC_PORT_RFC_GPO3 0x00000032 /* RC Core Data Out Pin 3 */
```

<a id="a8955bb4c29c837e71983307d2fc46155"></a>

### `IOC_PORT_RFC_SMI_CL_IN`

```c
#define IOC_PORT_RFC_SMI_CL_IN 0x00000038 /* RF Core SMI Command Link In */
```

<a id="a8fa600a45bb7210a0a869232883a36d7"></a>

### `IOC_PORT_RFC_SMI_CL_OUT`

```c
#define IOC_PORT_RFC_SMI_CL_OUT 0x00000037 /* RF Core SMI Command Link Out */
```

<a id="a38268821c556568eb9b8d0bd1b6bf4a4"></a>

### `IOC_PORT_RFC_SMI_DL_IN`

```c
#define IOC_PORT_RFC_SMI_DL_IN 0x00000036 /* RF Core SMI Data Link in */
```

<a id="a34286b14818f96f8e3955eebc3f453eb"></a>

### `IOC_PORT_RFC_SMI_DL_OUT`

```c
#define IOC_PORT_RFC_SMI_DL_OUT 0x00000035 /* RF Core SMI Data Link Out */
```

<a id="ae6a1e66015d48324657ede92613381be"></a>

### `IOC_PORT_RFC_TRC`

```c
#define IOC_PORT_RFC_TRC 0x0000002E /* RF Core Tracer */
```

<a id="ac7124cf50c094bfc24313d88aa8c06f4"></a>

### `IOC_RISING_EDGE`

```c
#define IOC_RISING_EDGE 0x00020000 /* Edge detection on rising edge */
```


## 31.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/cc13xx__cc26xx-pinctrl_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P030_zephyr__drivers__ieee802154__cc1200.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__dt-bindings__pinctrl__cc23x0-pinctrl.h_文件参考.md)
