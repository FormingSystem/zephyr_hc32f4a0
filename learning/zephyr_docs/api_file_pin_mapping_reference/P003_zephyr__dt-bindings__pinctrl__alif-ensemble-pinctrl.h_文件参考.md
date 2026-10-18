---
id: learning.zephyr-docs.api-file-pin-mapping-reference.page-3
title: zephyr__dt-bindings__pinctrl__alif-ensemble-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_alif-ensemble-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Alif Ensemble片上系统（SoC）系列的引脚控制定义（Pinctrl Definitions）。

查看此文件的源码。

<a id="details"></a>

Alif Ensemble 片上系统（SoC）系列的引脚控制（Pinctrl）定义。本头文件提供 Alif Ensemble 系列的引脚复用（Pin Multiplexing）定义。每个引脚最多可以配置为 8 种不同功能，即 GPIO 加 7 种复用功能（Alternate Functions）。引脚复用编码（Pinmux Encoding）采用 11 位值：位 [0:2] 为复用功能，`0` 表示 GPIO，`1–7` 表示 AF1–AF7；位 [3:5] 为端口内的引脚编号，范围为 `0–7`；位 [6:10] 为端口编号，范围为 `0–17`。引脚命名约定为 `PIN_P{port}_{pin}__{function}`。例如，`PIN_P0_0__UART0_RX_A` 表示端口 0、引脚 0、UART0 RX 功能（A 组）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ab0a2e9966868f5dcb365d5d533318a21"></a>

```c
#define ALIF_PINMUX(port, pin, func)
```

相关声明：[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

编码引脚复用配置（Pinmux Configuration）。

<a id="define-members-0"></a>

### 引脚复用编码位域定义（Pinmux encoding bit field definitions）

<a id="r_ab8529e7ad1002e2e112bf1286d4d6c62"></a>

```c
#define ALIF_PINMUX_FUNC_POS 0U
```

相关声明：[ALIF_PINMUX_FUNC_POS](#ab8529e7ad1002e2e112bf1286d4d6c62)。

复用功能（Alternate Function）字段的位位置。

<a id="r_a195b3893d9913e77419e111178923a3d"></a>

```c
#define ALIF_PINMUX_FUNC_MASK 0x7U
```

相关声明：[ALIF_PINMUX_FUNC_MASK](#a195b3893d9913e77419e111178923a3d)。

复用功能（Alternate Function）字段的位掩码，共 3 位。

<a id="r_a8c94e09e787a9fb1079e5fbe0aa875d2"></a>

```c
#define ALIF_PINMUX_PIN_POS 3U
```

相关声明：[ALIF_PINMUX_PIN_POS](#a8c94e09e787a9fb1079e5fbe0aa875d2)。

引脚编号（Pin Number）字段的位位置。

<a id="r_a723a8df1e91c947c25af42db8b9f73dd"></a>

```c
#define ALIF_PINMUX_PIN_MASK 0x7U
```

相关声明：[ALIF_PINMUX_PIN_MASK](#a723a8df1e91c947c25af42db8b9f73dd)。

引脚编号（Pin Number）字段的位掩码，共 3 位。

<a id="r_a5d3f4f922452dc948bcc7727d9875107"></a>

```c
#define ALIF_PINMUX_PORT_POS 6U
```

相关声明：[ALIF_PINMUX_PORT_POS](#a5d3f4f922452dc948bcc7727d9875107)。

端口编号（Port Number）字段的位位置。

<a id="r_a280dd67858770ceb0a88153aa29e09da"></a>

```c
#define ALIF_PINMUX_PORT_MASK 0x1FU
```

相关声明：[ALIF_PINMUX_PORT_MASK](#a280dd67858770ceb0a88153aa29e09da)。

端口编号（Port Number）字段的位掩码，共 5 位。

<a id="define-members-1"></a>

### 端口 0 的引脚定义（Port 0 Pin Definitions）

GPIO 端口（Port）0 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a21c0982e31739a0e14d1d5bbe8d28e26"></a>

```c
#define PIN_P0_0__GPIO ALIF_PINMUX(0, 0, 0)
```

相关声明：[PIN_P0_0__GPIO](#a21c0982e31739a0e14d1d5bbe8d28e26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.0` 的复用功能（Alternate Functions）。

<a id="r_a4903b693f23df7008874d2c03bd411b3"></a>

```c
#define PIN_P0_0__OSPI0_D0_A ALIF_PINMUX(0, 0, 1)
```

相关声明：[PIN_P0_0__OSPI0_D0_A](#a4903b693f23df7008874d2c03bd411b3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="r_a90cebb445be4e8ec705a6fec4f446849"></a>

```c
#define PIN_P0_0__UART0_RX_A ALIF_PINMUX(0, 0, 2)
```

相关声明：[PIN_P0_0__UART0_RX_A](#a90cebb445be4e8ec705a6fec4f446849)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`UART0_RX_A`。

<a id="r_acfd60a41f314cb4771cfeacc0cf01933"></a>

```c
#define PIN_P0_0__I3C_SDA_A ALIF_PINMUX(0, 0, 3)
```

相关声明：[PIN_P0_0__I3C_SDA_A](#acfd60a41f314cb4771cfeacc0cf01933)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`I3C_SDA_A`。

<a id="r_a4dbe11402f4375a20d2999a50dd777b1"></a>

```c
#define PIN_P0_0__UT0_T0_A ALIF_PINMUX(0, 0, 4)
```

相关声明：[PIN_P0_0__UT0_T0_A](#a4dbe11402f4375a20d2999a50dd777b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`UT0_T0_A`。

<a id="r_a6d2a6e4d7178a94d59328d894e147133"></a>

```c
#define PIN_P0_0__LPCAM_HSYNC_B ALIF_PINMUX(0, 0, 5)
```

相关声明：[PIN_P0_0__LPCAM_HSYNC_B](#a6d2a6e4d7178a94d59328d894e147133)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`LPCAM_HSYNC_B`。

<a id="r_ab88bf5ae68f6b947fbfe57a7a7918a2d"></a>

```c
#define PIN_P0_0__CAM_HSYNC_A ALIF_PINMUX(0, 0, 6)
```

相关声明：[PIN_P0_0__CAM_HSYNC_A](#ab88bf5ae68f6b947fbfe57a7a7918a2d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`CAM_HSYNC_A`。

<a id="r_aa23df37079d3cb2dfc04e0712ea4b98d"></a>

```c
#define PIN_P0_0__ANA_S0 ALIF_PINMUX(0, 0, 7)
```

相关声明：[PIN_P0_0__ANA_S0](#aa23df37079d3cb2dfc04e0712ea4b98d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`ANA_S0`。

<a id="r_a32eb0096f118eeaafa9f397de1d80611"></a>

```c
#define PIN_P0_1__GPIO ALIF_PINMUX(0, 1, 0)
```

相关声明：[PIN_P0_1__GPIO](#a32eb0096f118eeaafa9f397de1d80611)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.1` 的复用功能（Alternate Functions）。

<a id="r_a32e491127585b229574cfeb1fa4cd623"></a>

```c
#define PIN_P0_1__OSPI0_D1_A ALIF_PINMUX(0, 1, 1)
```

相关声明：[PIN_P0_1__OSPI0_D1_A](#a32e491127585b229574cfeb1fa4cd623)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="r_ad3c6925fe9f38326a5750bfa5bfca6f1"></a>

```c
#define PIN_P0_1__UART0_TX_A ALIF_PINMUX(0, 1, 2)
```

相关声明：[PIN_P0_1__UART0_TX_A](#ad3c6925fe9f38326a5750bfa5bfca6f1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`UART0_TX_A`。

<a id="r_a0fc3ec407b82193623a96299f03c99ee"></a>

```c
#define PIN_P0_1__I3C_SCL_A ALIF_PINMUX(0, 1, 3)
```

相关声明：[PIN_P0_1__I3C_SCL_A](#a0fc3ec407b82193623a96299f03c99ee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`I3C_SCL_A`。

<a id="r_aa03c1f85a5f3e45b2f91fe3c75d7f679"></a>

```c
#define PIN_P0_1__UT0_T1_A ALIF_PINMUX(0, 1, 4)
```

相关声明：[PIN_P0_1__UT0_T1_A](#aa03c1f85a5f3e45b2f91fe3c75d7f679)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`UT0_T1_A`。

<a id="r_af5e1715d9cc788ce35500c8a3d95a4d5"></a>

```c
#define PIN_P0_1__LPCAM_VSYNC_B ALIF_PINMUX(0, 1, 5)
```

相关声明：[PIN_P0_1__LPCAM_VSYNC_B](#af5e1715d9cc788ce35500c8a3d95a4d5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`LPCAM_VSYNC_B`。

<a id="r_a8631817f0da565c3d84cffef0d672c3e"></a>

```c
#define PIN_P0_1__CAM_VSYNC_A ALIF_PINMUX(0, 1, 6)
```

相关声明：[PIN_P0_1__CAM_VSYNC_A](#a8631817f0da565c3d84cffef0d672c3e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`CAM_VSYNC_A`。

<a id="r_a9a7460d69ed218e8bfe8e5038ad27f92"></a>

```c
#define PIN_P0_1__ANA_S1 ALIF_PINMUX(0, 1, 7)
```

相关声明：[PIN_P0_1__ANA_S1](#a9a7460d69ed218e8bfe8e5038ad27f92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`ANA_S1`。

<a id="r_a4fb3d6992e5eedb80cd18620d13aa3f4"></a>

```c
#define PIN_P0_2__GPIO ALIF_PINMUX(0, 2, 0)
```

相关声明：[PIN_P0_2__GPIO](#a4fb3d6992e5eedb80cd18620d13aa3f4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.2` 的复用功能（Alternate Functions）。

<a id="r_ad6b5a361d0324dd50534f9c49fbf1849"></a>

```c
#define PIN_P0_2__OSPI0_D2_A ALIF_PINMUX(0, 2, 1)
```

相关声明：[PIN_P0_2__OSPI0_D2_A](#ad6b5a361d0324dd50534f9c49fbf1849)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="r_a81dafa48db9962a46d804fe26b4d9aef"></a>

```c
#define PIN_P0_2__UART0_CTS_A ALIF_PINMUX(0, 2, 2)
```

相关声明：[PIN_P0_2__UART0_CTS_A](#a81dafa48db9962a46d804fe26b4d9aef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`UART0_CTS_A`。

<a id="r_aa2297640ed760699881972950ecde05f"></a>

```c
#define PIN_P0_2__I2C0_SDA_A ALIF_PINMUX(0, 2, 3)
```

相关声明：[PIN_P0_2__I2C0_SDA_A](#aa2297640ed760699881972950ecde05f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`I2C0_SDA_A`。

<a id="r_a1cbbd5723ce8730a93bbfb242ff83ad6"></a>

```c
#define PIN_P0_2__UT1_T0_A ALIF_PINMUX(0, 2, 4)
```

相关声明：[PIN_P0_2__UT1_T0_A](#a1cbbd5723ce8730a93bbfb242ff83ad6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`UT1_T0_A`。

<a id="r_a50b34f4621fbb5e99c8e9d60396b6731"></a>

```c
#define PIN_P0_2__LPCAM_PCLK_B ALIF_PINMUX(0, 2, 5)
```

相关声明：[PIN_P0_2__LPCAM_PCLK_B](#a50b34f4621fbb5e99c8e9d60396b6731)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`LPCAM_PCLK_B`。

<a id="r_af4ca0560e8c5c817b8c21ee225f87b20"></a>

```c
#define PIN_P0_2__CAM_PCLK_A ALIF_PINMUX(0, 2, 6)
```

相关声明：[PIN_P0_2__CAM_PCLK_A](#af4ca0560e8c5c817b8c21ee225f87b20)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`CAM_PCLK_A`。

<a id="r_a49b9fef54a6baea750aadaa5d80f8b59"></a>

```c
#define PIN_P0_2__ANA_S2 ALIF_PINMUX(0, 2, 7)
```

相关声明：[PIN_P0_2__ANA_S2](#a49b9fef54a6baea750aadaa5d80f8b59)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`ANA_S2`。

<a id="r_af6db067634b65894a37a5edbe29654a5"></a>

```c
#define PIN_P0_3__GPIO ALIF_PINMUX(0, 3, 0)
```

相关声明：[PIN_P0_3__GPIO](#af6db067634b65894a37a5edbe29654a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.3` 的复用功能（Alternate Functions）。

<a id="r_a7dc662eaf7011fadcb4402da22e5af64"></a>

```c
#define PIN_P0_3__OSPI0_D3_A ALIF_PINMUX(0, 3, 1)
```

相关声明：[PIN_P0_3__OSPI0_D3_A](#a7dc662eaf7011fadcb4402da22e5af64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`OSPI0_D3_A`。

<a id="r_a37d3d9cde76c648ab549818678cdd02c"></a>

```c
#define PIN_P0_3__UART0_RTS_A ALIF_PINMUX(0, 3, 2)
```

相关声明：[PIN_P0_3__UART0_RTS_A](#a37d3d9cde76c648ab549818678cdd02c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`UART0_RTS_A`。

<a id="r_a5c1d69ea260d2b1e17fc42fd9985edf6"></a>

```c
#define PIN_P0_3__I2C0_SCL_A ALIF_PINMUX(0, 3, 3)
```

相关声明：[PIN_P0_3__I2C0_SCL_A](#a5c1d69ea260d2b1e17fc42fd9985edf6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`I2C0_SCL_A`。

<a id="r_a92a256fe56cf75cba3a7caf048bc2015"></a>

```c
#define PIN_P0_3__UT1_T1_A ALIF_PINMUX(0, 3, 4)
```

相关声明：[PIN_P0_3__UT1_T1_A](#a92a256fe56cf75cba3a7caf048bc2015)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`UT1_T1_A`。

<a id="r_a165315703135d7f256218ad852d4111b"></a>

```c
#define PIN_P0_3__LPCAM_XVCLK_B ALIF_PINMUX(0, 3, 5)
```

相关声明：[PIN_P0_3__LPCAM_XVCLK_B](#a165315703135d7f256218ad852d4111b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`LPCAM_XVCLK_B`。

<a id="r_a7a1274ec637e3efeacab1bc77bd9bf69"></a>

```c
#define PIN_P0_3__CAM_XVCLK_A ALIF_PINMUX(0, 3, 6)
```

相关声明：[PIN_P0_3__CAM_XVCLK_A](#a7a1274ec637e3efeacab1bc77bd9bf69)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`CAM_XVCLK_A`。

<a id="r_acde8c916348493ac12ab8d892f4c4f5d"></a>

```c
#define PIN_P0_3__ANA_S3 ALIF_PINMUX(0, 3, 7)
```

相关声明：[PIN_P0_3__ANA_S3](#acde8c916348493ac12ab8d892f4c4f5d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`ANA_S3`。

<a id="r_a068d5bd9723f62cb6aaa42fba90a9034"></a>

```c
#define PIN_P0_4__GPIO ALIF_PINMUX(0, 4, 0)
```

相关声明：[PIN_P0_4__GPIO](#a068d5bd9723f62cb6aaa42fba90a9034)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.4` 的复用功能（Alternate Functions）。

<a id="r_a19f3852ecf10227358ff4e55add2c5a4"></a>

```c
#define PIN_P0_4__OSPI0_D4_A ALIF_PINMUX(0, 4, 1)
```

相关声明：[PIN_P0_4__OSPI0_D4_A](#a19f3852ecf10227358ff4e55add2c5a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`OSPI0_D4_A`。

<a id="r_a86dde3f58b034c8276602748a76ca207"></a>

```c
#define PIN_P0_4__UART1_RX_A ALIF_PINMUX(0, 4, 2)
```

相关声明：[PIN_P0_4__UART1_RX_A](#a86dde3f58b034c8276602748a76ca207)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`UART1_RX_A`。

<a id="r_ab3670c7a57f35ae1a77e2b28d74cb787"></a>

```c
#define PIN_P0_4__PDM_D0_A ALIF_PINMUX(0, 4, 3)
```

相关声明：[PIN_P0_4__PDM_D0_A](#ab3670c7a57f35ae1a77e2b28d74cb787)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`PDM_D0_A`。

<a id="r_a97fb0f48651a63fc62a6450cfd366a26"></a>

```c
#define PIN_P0_4__I2C1_SDA_A ALIF_PINMUX(0, 4, 4)
```

相关声明：[PIN_P0_4__I2C1_SDA_A](#a97fb0f48651a63fc62a6450cfd366a26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`I2C1_SDA_A`。

<a id="r_a75f02a4170bb4cce26c68473a82ccb23"></a>

```c
#define PIN_P0_4__UT2_T0_A ALIF_PINMUX(0, 4, 5)
```

相关声明：[PIN_P0_4__UT2_T0_A](#a75f02a4170bb4cce26c68473a82ccb23)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`UT2_T0_A`。

<a id="r_a783d402e95eb758ec44d01ef022000b6"></a>

```c
#define PIN_P0_4__CAN_RXD_B ALIF_PINMUX(0, 4, 6)
```

相关声明：[PIN_P0_4__CAN_RXD_B](#a783d402e95eb758ec44d01ef022000b6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`CAN_RXD_B`。

<a id="r_aa132663d37ec856ce1cad081dbe0193e"></a>

```c
#define PIN_P0_4__ANA_S4 ALIF_PINMUX(0, 4, 7)
```

相关声明：[PIN_P0_4__ANA_S4](#aa132663d37ec856ce1cad081dbe0193e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`ANA_S4`。

<a id="r_abd7d8c1f0be68ab38e7e4c7d62e8c88d"></a>

```c
#define PIN_P0_5__GPIO ALIF_PINMUX(0, 5, 0)
```

相关声明：[PIN_P0_5__GPIO](#abd7d8c1f0be68ab38e7e4c7d62e8c88d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.5` 的复用功能（Alternate Functions）。

<a id="r_abd9928a8129e505c14e5386176ae6201"></a>

```c
#define PIN_P0_5__OSPI0_D5_A ALIF_PINMUX(0, 5, 1)
```

相关声明：[PIN_P0_5__OSPI0_D5_A](#abd9928a8129e505c14e5386176ae6201)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`OSPI0_D5_A`。

<a id="r_a4c0f43be2ca7617733c39d6956d0898c"></a>

```c
#define PIN_P0_5__UART1_TX_A ALIF_PINMUX(0, 5, 2)
```

相关声明：[PIN_P0_5__UART1_TX_A](#a4c0f43be2ca7617733c39d6956d0898c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`UART1_TX_A`。

<a id="r_a7157d108eeba57c6e780f9b622123a88"></a>

```c
#define PIN_P0_5__PDM_C0_A ALIF_PINMUX(0, 5, 3)
```

相关声明：[PIN_P0_5__PDM_C0_A](#a7157d108eeba57c6e780f9b622123a88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`PDM_C0_A`。

<a id="r_a7c3f7fae777efdcfeb26b785b2d29b0d"></a>

```c
#define PIN_P0_5__I2C1_SCL_A ALIF_PINMUX(0, 5, 4)
```

相关声明：[PIN_P0_5__I2C1_SCL_A](#a7c3f7fae777efdcfeb26b785b2d29b0d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`I2C1_SCL_A`。

<a id="r_a96935f674c5309d86939d41a2fb1f7fe"></a>

```c
#define PIN_P0_5__UT2_T1_A ALIF_PINMUX(0, 5, 5)
```

相关声明：[PIN_P0_5__UT2_T1_A](#a96935f674c5309d86939d41a2fb1f7fe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`UT2_T1_A`。

<a id="r_a6035a6be92eefbac36961efebbde9b86"></a>

```c
#define PIN_P0_5__CAN_TXD_B ALIF_PINMUX(0, 5, 6)
```

相关声明：[PIN_P0_5__CAN_TXD_B](#a6035a6be92eefbac36961efebbde9b86)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`CAN_TXD_B`。

<a id="r_adab066f4e9f8d2741b138fc08b513cf6"></a>

```c
#define PIN_P0_5__ANA_S5 ALIF_PINMUX(0, 5, 7)
```

相关声明：[PIN_P0_5__ANA_S5](#adab066f4e9f8d2741b138fc08b513cf6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`ANA_S5`。

<a id="r_ad494beaa1230d6528f706e36a8f007cd"></a>

```c
#define PIN_P0_6__GPIO ALIF_PINMUX(0, 6, 0)
```

相关声明：[PIN_P0_6__GPIO](#ad494beaa1230d6528f706e36a8f007cd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.6` 的复用功能（Alternate Functions）。

<a id="r_ac3fcdf80f9e0d4a961561c32ae9694f9"></a>

```c
#define PIN_P0_6__OSPI0_D6_A ALIF_PINMUX(0, 6, 1)
```

相关声明：[PIN_P0_6__OSPI0_D6_A](#ac3fcdf80f9e0d4a961561c32ae9694f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`OSPI0_D6_A`。

<a id="r_a8d2cc812b823a3e6dfc06cb34e57a0aa"></a>

```c
#define PIN_P0_6__UART1_CTS_A ALIF_PINMUX(0, 6, 2)
```

相关声明：[PIN_P0_6__UART1_CTS_A](#a8d2cc812b823a3e6dfc06cb34e57a0aa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`UART1_CTS_A`。

<a id="r_a48eef1d4e9206d1c2eba6cdb40c9ad24"></a>

```c
#define PIN_P0_6__PDM_D1_A ALIF_PINMUX(0, 6, 3)
```

相关声明：[PIN_P0_6__PDM_D1_A](#a48eef1d4e9206d1c2eba6cdb40c9ad24)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`PDM_D1_A`。

<a id="r_ad09e6e851c799927c52951de92b9c1c1"></a>

```c
#define PIN_P0_6__I2C2_SCL_A ALIF_PINMUX(0, 6, 4)
```

相关声明：[PIN_P0_6__I2C2_SCL_A](#ad09e6e851c799927c52951de92b9c1c1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`I2C2_SCL_A`。

<a id="r_a3d822add657e1d953b28c0735fd3a9c6"></a>

```c
#define PIN_P0_6__UT3_T0_A ALIF_PINMUX(0, 6, 5)
```

相关声明：[PIN_P0_6__UT3_T0_A](#a3d822add657e1d953b28c0735fd3a9c6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`UT3_T0_A`。

<a id="r_ab54a6c6132f34080fabde5b5fe055124"></a>

```c
#define PIN_P0_6__CAN_STBY_B ALIF_PINMUX(0, 6, 6)
```

相关声明：[PIN_P0_6__CAN_STBY_B](#ab54a6c6132f34080fabde5b5fe055124)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`CAN_STBY_B`。

<a id="r_aa5907af749639d7948c06be6af51c75e"></a>

```c
#define PIN_P0_6__ANA_S6 ALIF_PINMUX(0, 6, 7)
```

相关声明：[PIN_P0_6__ANA_S6](#aa5907af749639d7948c06be6af51c75e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`ANA_S6`。

<a id="r_a3461a7c5af5e46d8e668e1e633c5d721"></a>

```c
#define PIN_P0_7__GPIO ALIF_PINMUX(0, 7, 0)
```

相关声明：[PIN_P0_7__GPIO](#a3461a7c5af5e46d8e668e1e633c5d721)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.7` 的复用功能（Alternate Functions）。

<a id="r_add0bf72a6fdf8887b88ba696c5f00a40"></a>

```c
#define PIN_P0_7__OSPI0_D7_A ALIF_PINMUX(0, 7, 1)
```

相关声明：[PIN_P0_7__OSPI0_D7_A](#add0bf72a6fdf8887b88ba696c5f00a40)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`OSPI0_D7_A`。

<a id="r_a8c262122844a7c5ff415d909d982a9b3"></a>

```c
#define PIN_P0_7__UART1_RTS_A ALIF_PINMUX(0, 7, 2)
```

相关声明：[PIN_P0_7__UART1_RTS_A](#a8c262122844a7c5ff415d909d982a9b3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`UART1_RTS_A`。

<a id="r_a10ada1c7e06b0a06cd4fb4f5d384329b"></a>

```c
#define PIN_P0_7__PDM_C1_A ALIF_PINMUX(0, 7, 3)
```

相关声明：[PIN_P0_7__PDM_C1_A](#a10ada1c7e06b0a06cd4fb4f5d384329b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`PDM_C1_A`。

<a id="r_ad0645a98d86cbc0b4f539a3db1c2856d"></a>

```c
#define PIN_P0_7__I2C2_SDA_A ALIF_PINMUX(0, 7, 4)
```

相关声明：[PIN_P0_7__I2C2_SDA_A](#ad0645a98d86cbc0b4f539a3db1c2856d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`I2C2_SDA_A`。

<a id="r_a9affec2fc3a89563e4528dda6feefeb1"></a>

```c
#define PIN_P0_7__UT3_T1_A ALIF_PINMUX(0, 7, 5)
```

相关声明：[PIN_P0_7__UT3_T1_A](#a9affec2fc3a89563e4528dda6feefeb1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`UT3_T1_A`。

<a id="r_abd2bbc4e66a09b210a11c8180f72757b"></a>

```c
#define PIN_P0_7__CDC_DE_B ALIF_PINMUX(0, 7, 6)
```

相关声明：[PIN_P0_7__CDC_DE_B](#abd2bbc4e66a09b210a11c8180f72757b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`CDC_DE_B`。

<a id="r_a996b9421d83cdf9fc98ee86a07037882"></a>

```c
#define PIN_P0_7__ANA_S7 ALIF_PINMUX(0, 7, 7)
```

相关声明：[PIN_P0_7__ANA_S7](#a996b9421d83cdf9fc98ee86a07037882)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`ANA_S7`。

<a id="define-members-2"></a>

### 端口 1 的引脚定义（Port 1 Pin Definitions）

GPIO 端口（Port）1 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_af59cc6b851070a403399aa14ec9522d5"></a>

```c
#define PIN_P1_0__GPIO ALIF_PINMUX(1, 0, 0)
```

相关声明：[PIN_P1_0__GPIO](#af59cc6b851070a403399aa14ec9522d5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.0` 的复用功能（Alternate Functions）。

<a id="r_a86fd70e32e1fe8ef3ddb28394c1181b9"></a>

```c
#define PIN_P1_0__UART2_RX_A ALIF_PINMUX(1, 0, 1)
```

相关声明：[PIN_P1_0__UART2_RX_A](#a86fd70e32e1fe8ef3ddb28394c1181b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`UART2_RX_A`。

<a id="r_a1b162fa1d3aa4c3dd720b47331a07a43"></a>

```c
#define PIN_P1_0__SPI0_MISO_A ALIF_PINMUX(1, 0, 2)
```

相关声明：[PIN_P1_0__SPI0_MISO_A](#a1b162fa1d3aa4c3dd720b47331a07a43)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`SPI0_MISO_A`。

<a id="r_a5b2648f183931a24604241319842e227"></a>

```c
#define PIN_P1_0__I2C3_SDA_A ALIF_PINMUX(1, 0, 3)
```

相关声明：[PIN_P1_0__I2C3_SDA_A](#a5b2648f183931a24604241319842e227)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`I2C3_SDA_A`。

<a id="r_a3f3320201474237109dbd44284ccfedc"></a>

```c
#define PIN_P1_0__UT4_T0_A ALIF_PINMUX(1, 0, 4)
```

相关声明：[PIN_P1_0__UT4_T0_A](#a3f3320201474237109dbd44284ccfedc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`UT4_T0_A`。

<a id="r_ae6e14263f73fe7b05294646dbb49c0bb"></a>

```c
#define PIN_P1_0__LPCAM_HSYNC_C ALIF_PINMUX(1, 0, 5)
```

相关声明：[PIN_P1_0__LPCAM_HSYNC_C](#ae6e14263f73fe7b05294646dbb49c0bb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`LPCAM_HSYNC_C`。

<a id="r_a814937842bb7225f52db5bf2f9f8818b"></a>

```c
#define PIN_P1_0__ETH_RXD0_C ALIF_PINMUX(1, 0, 6)
```

相关声明：[PIN_P1_0__ETH_RXD0_C](#a814937842bb7225f52db5bf2f9f8818b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`ETH_RXD0_C`。

<a id="r_af46992d6adf393d9fffa0b3d6bdf4568"></a>

```c
#define PIN_P1_0__ANA_S8 ALIF_PINMUX(1, 0, 7)
```

相关声明：[PIN_P1_0__ANA_S8](#af46992d6adf393d9fffa0b3d6bdf4568)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`ANA_S8`。

<a id="r_a5bde8570f8ee36a7dfa0e5d486dcb4d1"></a>

```c
#define PIN_P1_1__GPIO ALIF_PINMUX(1, 1, 0)
```

相关声明：[PIN_P1_1__GPIO](#a5bde8570f8ee36a7dfa0e5d486dcb4d1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.1` 的复用功能（Alternate Functions）。

<a id="r_ae31470618a41e1fa01512589fd7d454d"></a>

```c
#define PIN_P1_1__UART2_TX_A ALIF_PINMUX(1, 1, 1)
```

相关声明：[PIN_P1_1__UART2_TX_A](#ae31470618a41e1fa01512589fd7d454d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`UART2_TX_A`。

<a id="r_a37f579415afac4b490325552b9a90197"></a>

```c
#define PIN_P1_1__SPI0_MOSI_A ALIF_PINMUX(1, 1, 2)
```

相关声明：[PIN_P1_1__SPI0_MOSI_A](#a37f579415afac4b490325552b9a90197)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`SPI0_MOSI_A`。

<a id="r_a2399f5c76054a2d2d0f516faffd33dd0"></a>

```c
#define PIN_P1_1__I2C3_SCL_A ALIF_PINMUX(1, 1, 3)
```

相关声明：[PIN_P1_1__I2C3_SCL_A](#a2399f5c76054a2d2d0f516faffd33dd0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`I2C3_SCL_A`。

<a id="r_a7f6c1d958eca3b932064e4fe6422536e"></a>

```c
#define PIN_P1_1__UT4_T1_A ALIF_PINMUX(1, 1, 4)
```

相关声明：[PIN_P1_1__UT4_T1_A](#a7f6c1d958eca3b932064e4fe6422536e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`UT4_T1_A`。

<a id="r_a0eee3d62f2ee65deb0cd9f2b69882199"></a>

```c
#define PIN_P1_1__LPCAM_VSYNC_C ALIF_PINMUX(1, 1, 5)
```

相关声明：[PIN_P1_1__LPCAM_VSYNC_C](#a0eee3d62f2ee65deb0cd9f2b69882199)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`LPCAM_VSYNC_C`。

<a id="r_a4ef1406076debf4c5218543e138228e3"></a>

```c
#define PIN_P1_1__ETH_RXD1_C ALIF_PINMUX(1, 1, 6)
```

相关声明：[PIN_P1_1__ETH_RXD1_C](#a4ef1406076debf4c5218543e138228e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`ETH_RXD1_C`。

<a id="r_a86211d8e48dc86b32b17f2f6d1756ba9"></a>

```c
#define PIN_P1_1__ANA_S9 ALIF_PINMUX(1, 1, 7)
```

相关声明：[PIN_P1_1__ANA_S9](#a86211d8e48dc86b32b17f2f6d1756ba9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`ANA_S9`。

<a id="r_a6b0ea73c6cb252fda5ad10a28ceae4cf"></a>

```c
#define PIN_P1_2__GPIO ALIF_PINMUX(1, 2, 0)
```

相关声明：[PIN_P1_2__GPIO](#a6b0ea73c6cb252fda5ad10a28ceae4cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.2` 的复用功能（Alternate Functions）。

<a id="r_a75bdf22221574ac8f8d52c0ca11b9d01"></a>

```c
#define PIN_P1_2__UART3_RX_A ALIF_PINMUX(1, 2, 1)
```

相关声明：[PIN_P1_2__UART3_RX_A](#a75bdf22221574ac8f8d52c0ca11b9d01)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`UART3_RX_A`。

<a id="r_a80e2fc726f8004102da0cc8cf2acbaa3"></a>

```c
#define PIN_P1_2__SPI0_SCLK_A ALIF_PINMUX(1, 2, 2)
```

相关声明：[PIN_P1_2__SPI0_SCLK_A](#a80e2fc726f8004102da0cc8cf2acbaa3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`SPI0_SCLK_A`。

<a id="r_af47e1bc6844cd83ac416a61f08a496d0"></a>

```c
#define PIN_P1_2__I3C_SDA_B ALIF_PINMUX(1, 2, 3)
```

相关声明：[PIN_P1_2__I3C_SDA_B](#af47e1bc6844cd83ac416a61f08a496d0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`I3C_SDA_B`。

<a id="r_ae2cf8fd83f09da752634bcd3be2c945e"></a>

```c
#define PIN_P1_2__UT5_T0_A ALIF_PINMUX(1, 2, 4)
```

相关声明：[PIN_P1_2__UT5_T0_A](#ae2cf8fd83f09da752634bcd3be2c945e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`UT5_T0_A`。

<a id="r_a9aeae29f48b994b81c2223e5eddd24c4"></a>

```c
#define PIN_P1_2__LPCAM_PCLK_C ALIF_PINMUX(1, 2, 5)
```

相关声明：[PIN_P1_2__LPCAM_PCLK_C](#a9aeae29f48b994b81c2223e5eddd24c4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`LPCAM_PCLK_C`。

<a id="r_ace30b43016cff2a82db9893dd1eebd97"></a>

```c
#define PIN_P1_2__ETH_RST_C ALIF_PINMUX(1, 2, 6)
```

相关声明：[PIN_P1_2__ETH_RST_C](#ace30b43016cff2a82db9893dd1eebd97)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`ETH_RST_C`。

<a id="r_aa592bdbfcd49525f21feb3f9b9f5c0f9"></a>

```c
#define PIN_P1_2__ANA_S10 ALIF_PINMUX(1, 2, 7)
```

相关声明：[PIN_P1_2__ANA_S10](#aa592bdbfcd49525f21feb3f9b9f5c0f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`ANA_S10`。

<a id="r_a7ff354be10a7bcfd9418e346c2f860e5"></a>

```c
#define PIN_P1_3__GPIO ALIF_PINMUX(1, 3, 0)
```

相关声明：[PIN_P1_3__GPIO](#a7ff354be10a7bcfd9418e346c2f860e5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.3` 的复用功能（Alternate Functions）。

<a id="r_a8b0a4679230f962bd0847217bd78758d"></a>

```c
#define PIN_P1_3__UART3_TX_A ALIF_PINMUX(1, 3, 1)
```

相关声明：[PIN_P1_3__UART3_TX_A](#a8b0a4679230f962bd0847217bd78758d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`UART3_TX_A`。

<a id="r_acf307eea767cfd0532384afee6889ded"></a>

```c
#define PIN_P1_3__SPI0_SS0_A ALIF_PINMUX(1, 3, 2)
```

相关声明：[PIN_P1_3__SPI0_SS0_A](#acf307eea767cfd0532384afee6889ded)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`SPI0_SS0_A`。

<a id="r_afed98f0a2042138d28a4bc1ddf9b1413"></a>

```c
#define PIN_P1_3__I3C_SCL_B ALIF_PINMUX(1, 3, 3)
```

相关声明：[PIN_P1_3__I3C_SCL_B](#afed98f0a2042138d28a4bc1ddf9b1413)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`I3C_SCL_B`。

<a id="r_ada6e4116bf669193c8cf1b1ed196fbf5"></a>

```c
#define PIN_P1_3__UT5_T1_A ALIF_PINMUX(1, 3, 4)
```

相关声明：[PIN_P1_3__UT5_T1_A](#ada6e4116bf669193c8cf1b1ed196fbf5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`UT5_T1_A`。

<a id="r_aefe456eb61a82a883729e9ffb3fc6094"></a>

```c
#define PIN_P1_3__LPCAM_XVCLK_C ALIF_PINMUX(1, 3, 5)
```

相关声明：[PIN_P1_3__LPCAM_XVCLK_C](#aefe456eb61a82a883729e9ffb3fc6094)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`LPCAM_XVCLK_C`。

<a id="r_a72dfb2f9baf5ced5aed74c89826aa0f5"></a>

```c
#define PIN_P1_3__ETH_TXD0_C ALIF_PINMUX(1, 3, 6)
```

相关声明：[PIN_P1_3__ETH_TXD0_C](#a72dfb2f9baf5ced5aed74c89826aa0f5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`ETH_TXD0_C`。

<a id="r_ae90b82e11aa2b5d577d576047e1e5293"></a>

```c
#define PIN_P1_3__ANA_S11 ALIF_PINMUX(1, 3, 7)
```

相关声明：[PIN_P1_3__ANA_S11](#ae90b82e11aa2b5d577d576047e1e5293)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`ANA_S11`。

<a id="r_ad1e50e7a0add033402abf705b503b80a"></a>

```c
#define PIN_P1_4__GPIO ALIF_PINMUX(1, 4, 0)
```

相关声明：[PIN_P1_4__GPIO](#ad1e50e7a0add033402abf705b503b80a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.4` 的复用功能（Alternate Functions）。

<a id="r_ac80717bc4532eef10d5d26e2a23abe12"></a>

```c
#define PIN_P1_4__OSPI0_SS0_A ALIF_PINMUX(1, 4, 1)
```

相关声明：[PIN_P1_4__OSPI0_SS0_A](#ac80717bc4532eef10d5d26e2a23abe12)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`OSPI0_SS0_A`。

<a id="r_ab3d6a529ce7c2b8b8efccfb6a05f4130"></a>

```c
#define PIN_P1_4__UART0_RX_B ALIF_PINMUX(1, 4, 2)
```

相关声明：[PIN_P1_4__UART0_RX_B](#ab3d6a529ce7c2b8b8efccfb6a05f4130)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`UART0_RX_B`。

<a id="r_a07943991a186c8d4bd34f439df430651"></a>

```c
#define PIN_P1_4__SPI0_SS1_A ALIF_PINMUX(1, 4, 3)
```

相关声明：[PIN_P1_4__SPI0_SS1_A](#a07943991a186c8d4bd34f439df430651)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`SPI0_SS1_A`。

<a id="r_a741fc08fdd89f80a78183ffebcc20a25"></a>

```c
#define PIN_P1_4__UT6_T0_A ALIF_PINMUX(1, 4, 4)
```

相关声明：[PIN_P1_4__UT6_T0_A](#a741fc08fdd89f80a78183ffebcc20a25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`UT6_T0_A`。

<a id="r_a1142b9fb3e15c186d7267b63597e3b6b"></a>

```c
#define PIN_P1_4__LPCAM_D0_C ALIF_PINMUX(1, 4, 5)
```

相关声明：[PIN_P1_4__LPCAM_D0_C](#a1142b9fb3e15c186d7267b63597e3b6b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`LPCAM_D0_C`。

<a id="r_a46f5e6410d3fe7119511e8385ec1ca9b"></a>

```c
#define PIN_P1_4__ETH_TXD1_C ALIF_PINMUX(1, 4, 6)
```

相关声明：[PIN_P1_4__ETH_TXD1_C](#a46f5e6410d3fe7119511e8385ec1ca9b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`ETH_TXD1_C`。

<a id="r_a93d7e266264960f84f8805cb86a31a88"></a>

```c
#define PIN_P1_4__ANA_S12 ALIF_PINMUX(1, 4, 7)
```

相关声明：[PIN_P1_4__ANA_S12](#a93d7e266264960f84f8805cb86a31a88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`ANA_S12`。

<a id="r_a0fb34153badcd47f16246988312d0275"></a>

```c
#define PIN_P1_5__GPIO ALIF_PINMUX(1, 5, 0)
```

相关声明：[PIN_P1_5__GPIO](#a0fb34153badcd47f16246988312d0275)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.5` 的复用功能（Alternate Functions）。

<a id="r_a3dd514f984c015bb539a06b6d5167e90"></a>

```c
#define PIN_P1_5__OSPI0_SS1_A ALIF_PINMUX(1, 5, 1)
```

相关声明：[PIN_P1_5__OSPI0_SS1_A](#a3dd514f984c015bb539a06b6d5167e90)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`OSPI0_SS1_A`。

<a id="r_a0d8f5efff85a27a618933da01782ceea"></a>

```c
#define PIN_P1_5__UART0_TX_B ALIF_PINMUX(1, 5, 2)
```

相关声明：[PIN_P1_5__UART0_TX_B](#a0d8f5efff85a27a618933da01782ceea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`UART0_TX_B`。

<a id="r_a33819bc403cac0989edef3e0002b5c26"></a>

```c
#define PIN_P1_5__SPI0_SS2_A ALIF_PINMUX(1, 5, 3)
```

相关声明：[PIN_P1_5__SPI0_SS2_A](#a33819bc403cac0989edef3e0002b5c26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`SPI0_SS2_A`。

<a id="r_a3522647cc4e6bb11fdc53c388d1da8a9"></a>

```c
#define PIN_P1_5__UT6_T1_A ALIF_PINMUX(1, 5, 4)
```

相关声明：[PIN_P1_5__UT6_T1_A](#a3522647cc4e6bb11fdc53c388d1da8a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`UT6_T1_A`。

<a id="r_ab082a597cf3f000433c4c5dbff856357"></a>

```c
#define PIN_P1_5__LPCAM_D1_C ALIF_PINMUX(1, 5, 5)
```

相关声明：[PIN_P1_5__LPCAM_D1_C](#ab082a597cf3f000433c4c5dbff856357)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`LPCAM_D1_C`。

<a id="r_a88a8bc7139c0e5e3b2aaf02d1f8bdde1"></a>

```c
#define PIN_P1_5__ETH_TXEN_C ALIF_PINMUX(1, 5, 6)
```

相关声明：[PIN_P1_5__ETH_TXEN_C](#a88a8bc7139c0e5e3b2aaf02d1f8bdde1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`ETH_TXEN_C`。

<a id="r_a4ddb6ff8be37b8c2ec9973fb5b316ce5"></a>

```c
#define PIN_P1_5__ANA_S13 ALIF_PINMUX(1, 5, 7)
```

相关声明：[PIN_P1_5__ANA_S13](#a4ddb6ff8be37b8c2ec9973fb5b316ce5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`ANA_S13`。

<a id="r_ab6f0917e71cae608320a3c16b8edf1bf"></a>

```c
#define PIN_P1_6__GPIO ALIF_PINMUX(1, 6, 0)
```

相关声明：[PIN_P1_6__GPIO](#ab6f0917e71cae608320a3c16b8edf1bf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.6` 的复用功能（Alternate Functions）。

<a id="r_a00ced09f5db7ad96ec72a1375ba91254"></a>

```c
#define PIN_P1_6__OSPI0_RXDS_B ALIF_PINMUX(1, 6, 1)
```

相关声明：[PIN_P1_6__OSPI0_RXDS_B](#a00ced09f5db7ad96ec72a1375ba91254)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`OSPI0_RXDS_B`。

<a id="r_a04e94f302847e57cdc54e8bfee7b0e46"></a>

```c
#define PIN_P1_6__UART1_RX_B ALIF_PINMUX(1, 6, 2)
```

相关声明：[PIN_P1_6__UART1_RX_B](#a04e94f302847e57cdc54e8bfee7b0e46)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`UART1_RX_B`。

<a id="r_ab5b6fa72a51d06f2c315cdfb4ba8c4ad"></a>

```c
#define PIN_P1_6__I2S0_SDI_A ALIF_PINMUX(1, 6, 3)
```

相关声明：[PIN_P1_6__I2S0_SDI_A](#ab5b6fa72a51d06f2c315cdfb4ba8c4ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`I2S0_SDI_A`。

<a id="r_a7220a9ebc489750752d69dad135e73e9"></a>

```c
#define PIN_P1_6__UT7_T0_A ALIF_PINMUX(1, 6, 4)
```

相关声明：[PIN_P1_6__UT7_T0_A](#a7220a9ebc489750752d69dad135e73e9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`UT7_T0_A`。

<a id="r_aa28b285837812ca3bbb00f20610aceab"></a>

```c
#define PIN_P1_6__LPCAM_D2_C ALIF_PINMUX(1, 6, 5)
```

相关声明：[PIN_P1_6__LPCAM_D2_C](#aa28b285837812ca3bbb00f20610aceab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`LPCAM_D2_C`。

<a id="r_a38276b33e082e4c6a044cd8baebf5107"></a>

```c
#define PIN_P1_6__ETH_IRQ_C ALIF_PINMUX(1, 6, 6)
```

相关声明：[PIN_P1_6__ETH_IRQ_C](#a38276b33e082e4c6a044cd8baebf5107)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`ETH_IRQ_C`。

<a id="r_aa1f2e27a7534f0db8518b4b8c68d5857"></a>

```c
#define PIN_P1_6__ANA_S14 ALIF_PINMUX(1, 6, 7)
```

相关声明：[PIN_P1_6__ANA_S14](#aa1f2e27a7534f0db8518b4b8c68d5857)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`ANA_S14`。

<a id="r_a259e17b2ef415b6aed714af92b5f2ac5"></a>

```c
#define PIN_P1_7__GPIO ALIF_PINMUX(1, 7, 0)
```

相关声明：[PIN_P1_7__GPIO](#a259e17b2ef415b6aed714af92b5f2ac5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.7` 的复用功能（Alternate Functions）。

<a id="r_a9e55d200e8e937a5b20a4924adaae8c3"></a>

```c
#define PIN_P1_7__OSPI0_SCLK_A ALIF_PINMUX(1, 7, 1)
```

相关声明：[PIN_P1_7__OSPI0_SCLK_A](#a9e55d200e8e937a5b20a4924adaae8c3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`OSPI0_SCLK_A`。

<a id="r_ae8cbc076f0a1d507587fa57614314cca"></a>

```c
#define PIN_P1_7__UART1_TX_B ALIF_PINMUX(1, 7, 2)
```

相关声明：[PIN_P1_7__UART1_TX_B](#ae8cbc076f0a1d507587fa57614314cca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`UART1_TX_B`。

<a id="r_aba970af9b7ed5c4a767c77dba5342f9b"></a>

```c
#define PIN_P1_7__I2S0_SDO_A ALIF_PINMUX(1, 7, 3)
```

相关声明：[PIN_P1_7__I2S0_SDO_A](#aba970af9b7ed5c4a767c77dba5342f9b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`I2S0_SDO_A`。

<a id="r_aaef22b9773f6bcb90a55f76c500e1b25"></a>

```c
#define PIN_P1_7__UT7_T1_A ALIF_PINMUX(1, 7, 4)
```

相关声明：[PIN_P1_7__UT7_T1_A](#aaef22b9773f6bcb90a55f76c500e1b25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`UT7_T1_A`。

<a id="r_acf6622697cdb02583d3fc6a300ae1af2"></a>

```c
#define PIN_P1_7__LPCAM_D3_C ALIF_PINMUX(1, 7, 5)
```

相关声明：[PIN_P1_7__LPCAM_D3_C](#acf6622697cdb02583d3fc6a300ae1af2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`LPCAM_D3_C`。

<a id="r_afd5a53c152a2c162e9e94c610d039f26"></a>

```c
#define PIN_P1_7__ETH_REFCLK_C ALIF_PINMUX(1, 7, 6)
```

相关声明：[PIN_P1_7__ETH_REFCLK_C](#afd5a53c152a2c162e9e94c610d039f26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`ETH_REFCLK_C`。

<a id="r_a92f2d3bd8b00e50624f60cc265b30551"></a>

```c
#define PIN_P1_7__ANA_S15 ALIF_PINMUX(1, 7, 7)
```

相关声明：[PIN_P1_7__ANA_S15](#a92f2d3bd8b00e50624f60cc265b30551)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`ANA_S15`。

<a id="define-members-3"></a>

### 端口 2 的引脚定义（Port 2 Pin Definitions）

GPIO 端口（Port）2 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a2ed50f7f44d929b517287eaae4560f33"></a>

```c
#define PIN_P2_0__GPIO ALIF_PINMUX(2, 0, 0)
```

相关声明：[PIN_P2_0__GPIO](#a2ed50f7f44d929b517287eaae4560f33)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.0` 的复用功能（Alternate Functions）。

<a id="r_aa82957297e0601b509bfd324ee68c619"></a>

```c
#define PIN_P2_0__OSPI0_D0_B ALIF_PINMUX(2, 0, 1)
```

相关声明：[PIN_P2_0__OSPI0_D0_B](#aa82957297e0601b509bfd324ee68c619)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`OSPI0_D0_B`。

<a id="r_aaf2248797fce75459afa8361685c4f99"></a>

```c
#define PIN_P2_0__UART2_RX_B ALIF_PINMUX(2, 0, 2)
```

相关声明：[PIN_P2_0__UART2_RX_B](#aaf2248797fce75459afa8361685c4f99)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`UART2_RX_B`。

<a id="r_a577845dca48bd5b863e581412aebc03d"></a>

```c
#define PIN_P2_0__LPPDM_DO_A ALIF_PINMUX(2, 0, 3)
```

相关声明：[PIN_P2_0__LPPDM_DO_A](#a577845dca48bd5b863e581412aebc03d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`LPPDM_DO_A`。

<a id="r_acc68e58a4a1b2d16f7cf1761763e69da"></a>

```c
#define PIN_P2_0__UT8_T0_A ALIF_PINMUX(2, 0, 4)
```

相关声明：[PIN_P2_0__UT8_T0_A](#acc68e58a4a1b2d16f7cf1761763e69da)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`UT8_T0_A`。

<a id="r_a3955ab4850804ac7b5b7f7301028f5bc"></a>

```c
#define PIN_P2_0__LPCAM_D4_C ALIF_PINMUX(2, 0, 5)
```

相关声明：[PIN_P2_0__LPCAM_D4_C](#a3955ab4850804ac7b5b7f7301028f5bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`LPCAM_D4_C`。

<a id="r_a9adb3410c6b24e5ca6ada558dfb3fbc4"></a>

```c
#define PIN_P2_0__ETH_MDIO_C ALIF_PINMUX(2, 0, 6)
```

相关声明：[PIN_P2_0__ETH_MDIO_C](#a9adb3410c6b24e5ca6ada558dfb3fbc4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`ETH_MDIO_C`。

<a id="r_a5fdc0b91384ca45874ca44628d9c8b22"></a>

```c
#define PIN_P2_0__ANA_S16 ALIF_PINMUX(2, 0, 7)
```

相关声明：[PIN_P2_0__ANA_S16](#a5fdc0b91384ca45874ca44628d9c8b22)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`ANA_S16`。

<a id="r_ac05af956aca2528e61e358c597c5b637"></a>

```c
#define PIN_P2_1__GPIO ALIF_PINMUX(2, 1, 0)
```

相关声明：[PIN_P2_1__GPIO](#ac05af956aca2528e61e358c597c5b637)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.1` 的复用功能（Alternate Functions）。

<a id="r_a842c077a7b7716b901c7c980f793e910"></a>

```c
#define PIN_P2_1__OSPI0_D1_B ALIF_PINMUX(2, 1, 1)
```

相关声明：[PIN_P2_1__OSPI0_D1_B](#a842c077a7b7716b901c7c980f793e910)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`OSPI0_D1_B`。

<a id="r_a001165a8acc638335d9794dda1595faa"></a>

```c
#define PIN_P2_1__UART2_TX_B ALIF_PINMUX(2, 1, 2)
```

相关声明：[PIN_P2_1__UART2_TX_B](#a001165a8acc638335d9794dda1595faa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`UART2_TX_B`。

<a id="r_adf29ae0357511182f97b1ff2753cc474"></a>

```c
#define PIN_P2_1__LPPDM_CO_A ALIF_PINMUX(2, 1, 3)
```

相关声明：[PIN_P2_1__LPPDM_CO_A](#adf29ae0357511182f97b1ff2753cc474)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`LPPDM_CO_A`。

<a id="r_a32110e2d98bfacf89cedebf7e4d737ce"></a>

```c
#define PIN_P2_1__UT8_T1_A ALIF_PINMUX(2, 1, 4)
```

相关声明：[PIN_P2_1__UT8_T1_A](#a32110e2d98bfacf89cedebf7e4d737ce)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`UT8_T1_A`。

<a id="r_aa30d906709b79bb5ac704517df51c6f8"></a>

```c
#define PIN_P2_1__LPCAM_D5_C ALIF_PINMUX(2, 1, 5)
```

相关声明：[PIN_P2_1__LPCAM_D5_C](#aa30d906709b79bb5ac704517df51c6f8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`LPCAM_D5_C`。

<a id="r_ad40a374561a166ed81116bbc7e2e8388"></a>

```c
#define PIN_P2_1__ETH_MDC_C ALIF_PINMUX(2, 1, 6)
```

相关声明：[PIN_P2_1__ETH_MDC_C](#ad40a374561a166ed81116bbc7e2e8388)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`ETH_MDC_C`。

<a id="r_aeed5bdbf4e2c204b433b82007e816119"></a>

```c
#define PIN_P2_1__ANA_S17 ALIF_PINMUX(2, 1, 7)
```

相关声明：[PIN_P2_1__ANA_S17](#aeed5bdbf4e2c204b433b82007e816119)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`ANA_S17`。

<a id="r_a3fc212b07d980d4ae21a1743da443ac8"></a>

```c
#define PIN_P2_2__GPIO ALIF_PINMUX(2, 2, 0)
```

相关声明：[PIN_P2_2__GPIO](#a3fc212b07d980d4ae21a1743da443ac8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.2` 的复用功能（Alternate Functions）。

<a id="r_a58cecc0983fa40257343759dd563238c"></a>

```c
#define PIN_P2_2__OSPI0_D2_B ALIF_PINMUX(2, 2, 1)
```

相关声明：[PIN_P2_2__OSPI0_D2_B](#a58cecc0983fa40257343759dd563238c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`OSPI0_D2_B`。

<a id="r_a0e7ae0e5d25d567d45b82c69bf6c3449"></a>

```c
#define PIN_P2_2__UART3_RX_B ALIF_PINMUX(2, 2, 2)
```

相关声明：[PIN_P2_2__UART3_RX_B](#a0e7ae0e5d25d567d45b82c69bf6c3449)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`UART3_RX_B`。

<a id="r_abc4c737fb7dfbda40f2451b15b3009e8"></a>

```c
#define PIN_P2_2__LPPDM_D1_A ALIF_PINMUX(2, 2, 3)
```

相关声明：[PIN_P2_2__LPPDM_D1_A](#abc4c737fb7dfbda40f2451b15b3009e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`LPPDM_D1_A`。

<a id="r_aed1b4637862440bcf15ecf9e4a522a70"></a>

```c
#define PIN_P2_2__UT9_T0_A ALIF_PINMUX(2, 2, 4)
```

相关声明：[PIN_P2_2__UT9_T0_A](#aed1b4637862440bcf15ecf9e4a522a70)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`UT9_T0_A`。

<a id="r_aa3ddf0b435364b8b12f44ec46e6818a7"></a>

```c
#define PIN_P2_2__LPCAM_D6_C ALIF_PINMUX(2, 2, 5)
```

相关声明：[PIN_P2_2__LPCAM_D6_C](#aa3ddf0b435364b8b12f44ec46e6818a7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`LPCAM_D6_C`。

<a id="r_a79595ae2bb209452669c2e9080467b0a"></a>

```c
#define PIN_P2_2__ETH_CRS_DV_C ALIF_PINMUX(2, 2, 6)
```

相关声明：[PIN_P2_2__ETH_CRS_DV_C](#a79595ae2bb209452669c2e9080467b0a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`ETH_CRS_DV_C`。

<a id="r_a1c5aed6c5f029bf93595865c45c40ab8"></a>

```c
#define PIN_P2_2__ANA_S18 ALIF_PINMUX(2, 2, 7)
```

相关声明：[PIN_P2_2__ANA_S18](#a1c5aed6c5f029bf93595865c45c40ab8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`ANA_S18`。

<a id="r_a8408f18132258a0ef9fb8c3fe4f33977"></a>

```c
#define PIN_P2_3__GPIO ALIF_PINMUX(2, 3, 0)
```

相关声明：[PIN_P2_3__GPIO](#a8408f18132258a0ef9fb8c3fe4f33977)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.3` 的复用功能（Alternate Functions）。

<a id="r_a54f3045b17356a82629a1556aa7ff73a"></a>

```c
#define PIN_P2_3__OSPI0_D3_B ALIF_PINMUX(2, 3, 1)
```

相关声明：[PIN_P2_3__OSPI0_D3_B](#a54f3045b17356a82629a1556aa7ff73a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`OSPI0_D3_B`。

<a id="r_a616776438eb862a4108a37992a632e67"></a>

```c
#define PIN_P2_3__UART3_TX_B ALIF_PINMUX(2, 3, 2)
```

相关声明：[PIN_P2_3__UART3_TX_B](#a616776438eb862a4108a37992a632e67)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`UART3_TX_B`。

<a id="r_ada2c11fb58922dd44e9d8eab855e814e"></a>

```c
#define PIN_P2_3__LPPDM_C1_A ALIF_PINMUX(2, 3, 3)
```

相关声明：[PIN_P2_3__LPPDM_C1_A](#ada2c11fb58922dd44e9d8eab855e814e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`LPPDM_C1_A`。

<a id="r_afdeb160972e810f240b4702c2b1eeec9"></a>

```c
#define PIN_P2_3__UT9_T1_A ALIF_PINMUX(2, 3, 4)
```

相关声明：[PIN_P2_3__UT9_T1_A](#afdeb160972e810f240b4702c2b1eeec9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`UT9_T1_A`。

<a id="r_a61e5f243810f4850f937ca8d1545e3fc"></a>

```c
#define PIN_P2_3__LPCAM_D7_C ALIF_PINMUX(2, 3, 5)
```

相关声明：[PIN_P2_3__LPCAM_D7_C](#a61e5f243810f4850f937ca8d1545e3fc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`LPCAM_D7_C`。

<a id="r_a6b3f74c3429e0b1bcc951344dd2769ea"></a>

```c
#define PIN_P2_3__CDC_PCLK_B ALIF_PINMUX(2, 3, 6)
```

相关声明：[PIN_P2_3__CDC_PCLK_B](#a6b3f74c3429e0b1bcc951344dd2769ea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`CDC_PCLK_B`。

<a id="r_a278c1c69c1630a34e9614df51b00b23e"></a>

```c
#define PIN_P2_3__ANA_S19 ALIF_PINMUX(2, 3, 7)
```

相关声明：[PIN_P2_3__ANA_S19](#a278c1c69c1630a34e9614df51b00b23e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`ANA_S19`。

<a id="r_a649d4dc937e3cb6269408b128ed3aae3"></a>

```c
#define PIN_P2_4__GPIO ALIF_PINMUX(2, 4, 0)
```

相关声明：[PIN_P2_4__GPIO](#a649d4dc937e3cb6269408b128ed3aae3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.4` 的复用功能（Alternate Functions）。

<a id="r_adf2f3b37102ca4d9b2f0911883bac38b"></a>

```c
#define PIN_P2_4__OSPI0_D4_B ALIF_PINMUX(2, 4, 1)
```

相关声明：[PIN_P2_4__OSPI0_D4_B](#adf2f3b37102ca4d9b2f0911883bac38b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`OSPI0_D4_B`。

<a id="r_a0a7d9b1a52f563523232be9bf721b93c"></a>

```c
#define PIN_P2_4__LPI2S_SDI_A ALIF_PINMUX(2, 4, 2)
```

相关声明：[PIN_P2_4__LPI2S_SDI_A](#a0a7d9b1a52f563523232be9bf721b93c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`LPI2S_SDI_A`。

<a id="r_a2aa83e7a998c6c5bb3f50752acf36596"></a>

```c
#define PIN_P2_4__SPI1_MISO_A ALIF_PINMUX(2, 4, 3)
```

相关声明：[PIN_P2_4__SPI1_MISO_A](#a2aa83e7a998c6c5bb3f50752acf36596)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`SPI1_MISO_A`。

<a id="r_ab3881a977b071eea87195c775af58362"></a>

```c
#define PIN_P2_4__UT10_T0_A ALIF_PINMUX(2, 4, 4)
```

相关声明：[PIN_P2_4__UT10_T0_A](#ab3881a977b071eea87195c775af58362)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`UT10_T0_A`。

<a id="r_a45c1199b3ae89c34db01df5b52ee4b44"></a>

```c
#define PIN_P2_4__LPCAM_D0_B ALIF_PINMUX(2, 4, 5)
```

相关声明：[PIN_P2_4__LPCAM_D0_B](#a45c1199b3ae89c34db01df5b52ee4b44)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`LPCAM_D0_B`。

<a id="r_a319dc0b42697fc3b306d26008b19a143"></a>

```c
#define PIN_P2_4__CAM_D0_A ALIF_PINMUX(2, 4, 6)
```

相关声明：[PIN_P2_4__CAM_D0_A](#a319dc0b42697fc3b306d26008b19a143)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`CAM_D0_A`。

<a id="r_a9a559ace0037b84ab5a1e40077ea8808"></a>

```c
#define PIN_P2_4__ANA_S20 ALIF_PINMUX(2, 4, 7)
```

相关声明：[PIN_P2_4__ANA_S20](#a9a559ace0037b84ab5a1e40077ea8808)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`ANA_S20`。

<a id="r_ac399d584c2f7dbdf0a2ceeb91a9a9ea0"></a>

```c
#define PIN_P2_5__GPIO ALIF_PINMUX(2, 5, 0)
```

相关声明：[PIN_P2_5__GPIO](#ac399d584c2f7dbdf0a2ceeb91a9a9ea0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.5` 的复用功能（Alternate Functions）。

<a id="r_a34d5cf58f78ffdc01a47a4caf42f6d49"></a>

```c
#define PIN_P2_5__OSPI0_D5_B ALIF_PINMUX(2, 5, 1)
```

相关声明：[PIN_P2_5__OSPI0_D5_B](#a34d5cf58f78ffdc01a47a4caf42f6d49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`OSPI0_D5_B`。

<a id="r_a3ce54d780b1c7f8edd0a417884172658"></a>

```c
#define PIN_P2_5__LPI2S_SDO_A ALIF_PINMUX(2, 5, 2)
```

相关声明：[PIN_P2_5__LPI2S_SDO_A](#a3ce54d780b1c7f8edd0a417884172658)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`LPI2S_SDO_A`。

<a id="r_a3e7ab219ef183221184241ddbd94e7ed"></a>

```c
#define PIN_P2_5__SPI1_MOSI_A ALIF_PINMUX(2, 5, 3)
```

相关声明：[PIN_P2_5__SPI1_MOSI_A](#a3e7ab219ef183221184241ddbd94e7ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`SPI1_MOSI_A`。

<a id="r_a6029e70b8f2cf154922af02809ee10f8"></a>

```c
#define PIN_P2_5__UT10_T1_A ALIF_PINMUX(2, 5, 4)
```

相关声明：[PIN_P2_5__UT10_T1_A](#a6029e70b8f2cf154922af02809ee10f8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`UT10_T1_A`。

<a id="r_a3c58d40ef3db239807b40c2c369f7340"></a>

```c
#define PIN_P2_5__LPCAM_D1_B ALIF_PINMUX(2, 5, 5)
```

相关声明：[PIN_P2_5__LPCAM_D1_B](#a3c58d40ef3db239807b40c2c369f7340)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`LPCAM_D1_B`。

<a id="r_ac0a6ef529c49b06354fefd6006df80a8"></a>

```c
#define PIN_P2_5__CAM_D1_A ALIF_PINMUX(2, 5, 6)
```

相关声明：[PIN_P2_5__CAM_D1_A](#ac0a6ef529c49b06354fefd6006df80a8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`CAM_D1_A`。

<a id="r_a3a52e20cf83881a4040b2923a908312d"></a>

```c
#define PIN_P2_5__ANA_S21 ALIF_PINMUX(2, 5, 7)
```

相关声明：[PIN_P2_5__ANA_S21](#a3a52e20cf83881a4040b2923a908312d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`ANA_S21`。

<a id="r_acf70da7d084f17a152af48ea6ef34527"></a>

```c
#define PIN_P2_6__GPIO ALIF_PINMUX(2, 6, 0)
```

相关声明：[PIN_P2_6__GPIO](#acf70da7d084f17a152af48ea6ef34527)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.6` 的复用功能（Alternate Functions）。

<a id="r_a0e37543540f7a5debb4880c428e5d386"></a>

```c
#define PIN_P2_6__OSPI0_D6_B ALIF_PINMUX(2, 6, 1)
```

相关声明：[PIN_P2_6__OSPI0_D6_B](#a0e37543540f7a5debb4880c428e5d386)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`OSPI0_D6_B`。

<a id="r_a4a56c254577a79842f8d72c49bd72a39"></a>

```c
#define PIN_P2_6__LPI2S_SCLK_A ALIF_PINMUX(2, 6, 2)
```

相关声明：[PIN_P2_6__LPI2S_SCLK_A](#a4a56c254577a79842f8d72c49bd72a39)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`LPI2S_SCLK_A`。

<a id="r_a13b12f2f3dd64b479f8823b630f7ca16"></a>

```c
#define PIN_P2_6__SPI1_SCLK_A ALIF_PINMUX(2, 6, 3)
```

相关声明：[PIN_P2_6__SPI1_SCLK_A](#a13b12f2f3dd64b479f8823b630f7ca16)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`SPI1_SCLK_A`。

<a id="r_ac79a307d2c8bd2e69bd0ca655e4d4fba"></a>

```c
#define PIN_P2_6__UT11_T0_A ALIF_PINMUX(2, 6, 4)
```

相关声明：[PIN_P2_6__UT11_T0_A](#ac79a307d2c8bd2e69bd0ca655e4d4fba)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`UT11_T0_A`。

<a id="r_a4c8b29f25f52029b6cb08a5ec5afa779"></a>

```c
#define PIN_P2_6__LPCAM_D2_B ALIF_PINMUX(2, 6, 5)
```

相关声明：[PIN_P2_6__LPCAM_D2_B](#a4c8b29f25f52029b6cb08a5ec5afa779)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`LPCAM_D2_B`。

<a id="r_a63c496343932fe27c57ee6b43811b196"></a>

```c
#define PIN_P2_6__CAM_D2_A ALIF_PINMUX(2, 6, 6)
```

相关声明：[PIN_P2_6__CAM_D2_A](#a63c496343932fe27c57ee6b43811b196)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`CAM_D2_A`。

<a id="r_a5f155f536d36ca472970a8a88cd88fbf"></a>

```c
#define PIN_P2_6__ANA_S22 ALIF_PINMUX(2, 6, 7)
```

相关声明：[PIN_P2_6__ANA_S22](#a5f155f536d36ca472970a8a88cd88fbf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`ANA_S22`。

<a id="r_ab3f711dc40129f35a38cec46e12f23dd"></a>

```c
#define PIN_P2_7__GPIO ALIF_PINMUX(2, 7, 0)
```

相关声明：[PIN_P2_7__GPIO](#ab3f711dc40129f35a38cec46e12f23dd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.7` 的复用功能（Alternate Functions）。

<a id="r_a5d48a8c10667866e552c55b82bfb8c72"></a>

```c
#define PIN_P2_7__OSPI0_D7_B ALIF_PINMUX(2, 7, 1)
```

相关声明：[PIN_P2_7__OSPI0_D7_B](#a5d48a8c10667866e552c55b82bfb8c72)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`OSPI0_D7_B`。

<a id="r_a7bb33b4187db11f73bb44771e06a1043"></a>

```c
#define PIN_P2_7__LPI2S_WS_A ALIF_PINMUX(2, 7, 2)
```

相关声明：[PIN_P2_7__LPI2S_WS_A](#a7bb33b4187db11f73bb44771e06a1043)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`LPI2S_WS_A`。

<a id="r_afc70e6300e5e0b337be0dfca7c65dd60"></a>

```c
#define PIN_P2_7__SPI1_SS0_A ALIF_PINMUX(2, 7, 3)
```

相关声明：[PIN_P2_7__SPI1_SS0_A](#afc70e6300e5e0b337be0dfca7c65dd60)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`SPI1_SS0_A`。

<a id="r_a18f66ed0932d572410bdc86defb04969"></a>

```c
#define PIN_P2_7__UT11_T1_A ALIF_PINMUX(2, 7, 4)
```

相关声明：[PIN_P2_7__UT11_T1_A](#a18f66ed0932d572410bdc86defb04969)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`UT11_T1_A`。

<a id="r_ae5fd2294c685aa90b41f782ae19cc853"></a>

```c
#define PIN_P2_7__LPCAM_D3_B ALIF_PINMUX(2, 7, 5)
```

相关声明：[PIN_P2_7__LPCAM_D3_B](#ae5fd2294c685aa90b41f782ae19cc853)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`LPCAM_D3_B`。

<a id="r_a532ec1795ccf99a05c09f4546ebc9b09"></a>

```c
#define PIN_P2_7__CAM_D3_A ALIF_PINMUX(2, 7, 6)
```

相关声明：[PIN_P2_7__CAM_D3_A](#a532ec1795ccf99a05c09f4546ebc9b09)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`CAM_D3_A`。

<a id="r_a2cf38a7fbf2e09a633cb3d5599739988"></a>

```c
#define PIN_P2_7__ANA_S23 ALIF_PINMUX(2, 7, 7)
```

相关声明：[PIN_P2_7__ANA_S23](#a2cf38a7fbf2e09a633cb3d5599739988)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`ANA_S23`。

<a id="define-members-4"></a>

### 端口 3 的引脚定义（Port 3 Pin Definitions）

GPIO 端口（Port）3 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_aeb39304438c089405b315935caa1d90b"></a>

```c
#define PIN_P3_0__GPIO ALIF_PINMUX(3, 0, 0)
```

相关声明：[PIN_P3_0__GPIO](#aeb39304438c089405b315935caa1d90b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.0` 的复用功能（Alternate Functions）。

<a id="r_a209d55bd85828cc2d2dd906ce00a54bc"></a>

```c
#define PIN_P3_0__OSPI0_SCLK_B ALIF_PINMUX(3, 0, 1)
```

相关声明：[PIN_P3_0__OSPI0_SCLK_B](#a209d55bd85828cc2d2dd906ce00a54bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`OSPI0_SCLK_B`。

<a id="r_aa62f64668d791bbee277fe5d60c3e30c"></a>

```c
#define PIN_P3_0__UART4_RX_A ALIF_PINMUX(3, 0, 2)
```

相关声明：[PIN_P3_0__UART4_RX_A](#aa62f64668d791bbee277fe5d60c3e30c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`UART4_RX_A`。

<a id="r_ac15579dca0f426d4c98762b1e3e48a0b"></a>

```c
#define PIN_P3_0__PDM_D0_B ALIF_PINMUX(3, 0, 3)
```

相关声明：[PIN_P3_0__PDM_D0_B](#ac15579dca0f426d4c98762b1e3e48a0b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`PDM_D0_B`。

<a id="r_ae61620d2e6ad149c619c9abd41c6f265"></a>

```c
#define PIN_P3_0__I2S0_SCLK_A ALIF_PINMUX(3, 0, 4)
```

相关声明：[PIN_P3_0__I2S0_SCLK_A](#ae61620d2e6ad149c619c9abd41c6f265)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`I2S0_SCLK_A`。

<a id="r_aa7685bafaaf059dba920a3ff14f0946f"></a>

```c
#define PIN_P3_0__QEC0_X_A ALIF_PINMUX(3, 0, 5)
```

相关声明：[PIN_P3_0__QEC0_X_A](#aa7685bafaaf059dba920a3ff14f0946f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`QEC0_X_A`。

<a id="r_a4836305188a3a85d3af2dc45f6139629"></a>

```c
#define PIN_P3_0__LPCAM_D4_B ALIF_PINMUX(3, 0, 6)
```

相关声明：[PIN_P3_0__LPCAM_D4_B](#a4836305188a3a85d3af2dc45f6139629)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`LPCAM_D4_B`。

<a id="r_a28c59ba78d7a8dec612833b49bf283f7"></a>

```c
#define PIN_P3_0__CAM_D4_A ALIF_PINMUX(3, 0, 7)
```

相关声明：[PIN_P3_0__CAM_D4_A](#a28c59ba78d7a8dec612833b49bf283f7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`CAM_D4_A`。

<a id="r_a6cd05b1a797d571a1d1d1981ba849f8f"></a>

```c
#define PIN_P3_1__GPIO ALIF_PINMUX(3, 1, 0)
```

相关声明：[PIN_P3_1__GPIO](#a6cd05b1a797d571a1d1d1981ba849f8f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.1` 的复用功能（Alternate Functions）。

<a id="r_aaba2b57d35fa7d428a318a0dc9855025"></a>

```c
#define PIN_P3_1__OSPI0_SCLKN_B ALIF_PINMUX(3, 1, 1)
```

相关声明：[PIN_P3_1__OSPI0_SCLKN_B](#aaba2b57d35fa7d428a318a0dc9855025)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`OSPI0_SCLKN_B`。

<a id="r_a0512fcc221b1f4be00f7c0c07f4c05ad"></a>

```c
#define PIN_P3_1__UART4_TX_A ALIF_PINMUX(3, 1, 2)
```

相关声明：[PIN_P3_1__UART4_TX_A](#a0512fcc221b1f4be00f7c0c07f4c05ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`UART4_TX_A`。

<a id="r_ac646919b01848e8b19e48b2bfd3c6d5e"></a>

```c
#define PIN_P3_1__PDM_C0_B ALIF_PINMUX(3, 1, 3)
```

相关声明：[PIN_P3_1__PDM_C0_B](#ac646919b01848e8b19e48b2bfd3c6d5e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`PDM_C0_B`。

<a id="r_a328c1fc58286091b09614c0d462f99ed"></a>

```c
#define PIN_P3_1__I2S0_WS_A ALIF_PINMUX(3, 1, 4)
```

相关声明：[PIN_P3_1__I2S0_WS_A](#a328c1fc58286091b09614c0d462f99ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`I2S0_WS_A`。

<a id="r_a8194b8be869e35552ea43b5e0a010f1c"></a>

```c
#define PIN_P3_1__QEC0_Y_A ALIF_PINMUX(3, 1, 5)
```

相关声明：[PIN_P3_1__QEC0_Y_A](#a8194b8be869e35552ea43b5e0a010f1c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`QEC0_Y_A`。

<a id="r_a1b63270ca2becba12cb7f760e083c15f"></a>

```c
#define PIN_P3_1__LPCAM_D5_B ALIF_PINMUX(3, 1, 6)
```

相关声明：[PIN_P3_1__LPCAM_D5_B](#a1b63270ca2becba12cb7f760e083c15f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`LPCAM_D5_B`。

<a id="r_a4234dfa64e59a21f8dceb1eb089e4c57"></a>

```c
#define PIN_P3_1__CAM_D5_A ALIF_PINMUX(3, 1, 7)
```

相关声明：[PIN_P3_1__CAM_D5_A](#a4234dfa64e59a21f8dceb1eb089e4c57)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`CAM_D5_A`。

<a id="r_a4bfd126d24cab1669b9880c163e9b73a"></a>

```c
#define PIN_P3_2__GPIO ALIF_PINMUX(3, 2, 0)
```

相关声明：[PIN_P3_2__GPIO](#a4bfd126d24cab1669b9880c163e9b73a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.2` 的复用功能（Alternate Functions）。

<a id="r_a4d5b9cece4a56b2a102b1925ff1f9a1b"></a>

```c
#define PIN_P3_2__OSPI0_SS0_B ALIF_PINMUX(3, 2, 1)
```

相关声明：[PIN_P3_2__OSPI0_SS0_B](#a4d5b9cece4a56b2a102b1925ff1f9a1b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`OSPI0_SS0_B`。

<a id="r_a219f780cdd43c9ac60fc5e05a073dc2e"></a>

```c
#define PIN_P3_2__PDM_D1_B ALIF_PINMUX(3, 2, 2)
```

相关声明：[PIN_P3_2__PDM_D1_B](#a219f780cdd43c9ac60fc5e05a073dc2e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`PDM_D1_B`。

<a id="r_a14c39a4fe27d9ec9f126ce635873324b"></a>

```c
#define PIN_P3_2__I2S1_SDI_A ALIF_PINMUX(3, 2, 3)
```

相关声明：[PIN_P3_2__I2S1_SDI_A](#a14c39a4fe27d9ec9f126ce635873324b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`I2S1_SDI_A`。

<a id="r_a7fe93f89c7972565ea925b65e8c33ac3"></a>

```c
#define PIN_P3_2__I3C_SDA_C ALIF_PINMUX(3, 2, 4)
```

相关声明：[PIN_P3_2__I3C_SDA_C](#a7fe93f89c7972565ea925b65e8c33ac3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`I3C_SDA_C`。

<a id="r_a4c9789730311f91c9f1535dde7b94e9d"></a>

```c
#define PIN_P3_2__QEC0_Z_A ALIF_PINMUX(3, 2, 5)
```

相关声明：[PIN_P3_2__QEC0_Z_A](#a4c9789730311f91c9f1535dde7b94e9d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`QEC0_Z_A`。

<a id="r_a6fbc5b2f77d7b2be8a6b89c2d4b0124b"></a>

```c
#define PIN_P3_2__LPCAM_D6_B ALIF_PINMUX(3, 2, 6)
```

相关声明：[PIN_P3_2__LPCAM_D6_B](#a6fbc5b2f77d7b2be8a6b89c2d4b0124b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`LPCAM_D6_B`。

<a id="r_a89dc9f0608bd14bc339aad2a6352b072"></a>

```c
#define PIN_P3_2__CAM_D6_A ALIF_PINMUX(3, 2, 7)
```

相关声明：[PIN_P3_2__CAM_D6_A](#a89dc9f0608bd14bc339aad2a6352b072)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`CAM_D6_A`。

<a id="r_ac22b3e259b7eac30c576114860368ae4"></a>

```c
#define PIN_P3_3__GPIO ALIF_PINMUX(3, 3, 0)
```

相关声明：[PIN_P3_3__GPIO](#ac22b3e259b7eac30c576114860368ae4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.3` 的复用功能（Alternate Functions）。

<a id="r_aa5bf95d622e1c2284151ac4ff625ed63"></a>

```c
#define PIN_P3_3__OSPI0_SS1_B ALIF_PINMUX(3, 3, 1)
```

相关声明：[PIN_P3_3__OSPI0_SS1_B](#aa5bf95d622e1c2284151ac4ff625ed63)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`OSPI0_SS1_B`。

<a id="r_a762ad931b8b9351a3bb168a9aaccf7d6"></a>

```c
#define PIN_P3_3__PDM_C1_B ALIF_PINMUX(3, 3, 2)
```

相关声明：[PIN_P3_3__PDM_C1_B](#a762ad931b8b9351a3bb168a9aaccf7d6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`PDM_C1_B`。

<a id="r_a3d84682d52ba3eb596c9c4eaa707ee17"></a>

```c
#define PIN_P3_3__I2S1_SDO_A ALIF_PINMUX(3, 3, 3)
```

相关声明：[PIN_P3_3__I2S1_SDO_A](#a3d84682d52ba3eb596c9c4eaa707ee17)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`I2S1_SDO_A`。

<a id="r_a8cd7ccbaba7a127e079eeae5f3fb6df6"></a>

```c
#define PIN_P3_3__I3C_SCL_C ALIF_PINMUX(3, 3, 4)
```

相关声明：[PIN_P3_3__I3C_SCL_C](#a8cd7ccbaba7a127e079eeae5f3fb6df6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`I3C_SCL_C`。

<a id="r_aa1a195a08756e8d8afbb0c488b92103c"></a>

```c
#define PIN_P3_3__QEC1_X_A ALIF_PINMUX(3, 3, 5)
```

相关声明：[PIN_P3_3__QEC1_X_A](#aa1a195a08756e8d8afbb0c488b92103c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`QEC1_X_A`。

<a id="r_ad2843f4084856d540a0936f609ea673f"></a>

```c
#define PIN_P3_3__LPCAM_D7_B ALIF_PINMUX(3, 3, 6)
```

相关声明：[PIN_P3_3__LPCAM_D7_B](#ad2843f4084856d540a0936f609ea673f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`LPCAM_D7_B`。

<a id="r_ae578ece739f190c58b879086a37f56f3"></a>

```c
#define PIN_P3_3__CAM_D7_A ALIF_PINMUX(3, 3, 7)
```

相关声明：[PIN_P3_3__CAM_D7_A](#ae578ece739f190c58b879086a37f56f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`CAM_D7_A`。

<a id="r_af826ee88e3ed085269f16bee4a1a5bd7"></a>

```c
#define PIN_P3_4__GPIO ALIF_PINMUX(3, 4, 0)
```

相关声明：[PIN_P3_4__GPIO](#af826ee88e3ed085269f16bee4a1a5bd7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.4` 的复用功能（Alternate Functions）。

<a id="r_aa814da0a75dab71857b6a875e2a60508"></a>

```c
#define PIN_P3_4__OSPI0_RXDS_B ALIF_PINMUX(3, 4, 1)
```

相关声明：[PIN_P3_4__OSPI0_RXDS_B](#aa814da0a75dab71857b6a875e2a60508)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`OSPI0_RXDS_B`。

<a id="r_a8e810a67528a4d5be263dd1f9ad5010e"></a>

```c
#define PIN_P3_4__UART5_RX_A ALIF_PINMUX(3, 4, 2)
```

相关声明：[PIN_P3_4__UART5_RX_A](#a8e810a67528a4d5be263dd1f9ad5010e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`UART5_RX_A`。

<a id="r_a9927106dac12e76682f04fb72f9696a4"></a>

```c
#define PIN_P3_4__LPPDM_CO_B ALIF_PINMUX(3, 4, 3)
```

相关声明：[PIN_P3_4__LPPDM_CO_B](#a9927106dac12e76682f04fb72f9696a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`LPPDM_CO_B`。

<a id="r_adb9a325b5eb089330ba3c4e33396f8fe"></a>

```c
#define PIN_P3_4__I2S1_SCLK_A ALIF_PINMUX(3, 4, 4)
```

相关声明：[PIN_P3_4__I2S1_SCLK_A](#adb9a325b5eb089330ba3c4e33396f8fe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`I2S1_SCLK_A`。

<a id="r_aecbc53340aefc0c7177839de1f8a3e4d"></a>

```c
#define PIN_P3_4__I2C0_SCL_B ALIF_PINMUX(3, 4, 5)
```

相关声明：[PIN_P3_4__I2C0_SCL_B](#aecbc53340aefc0c7177839de1f8a3e4d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`I2C0_SCL_B`。

<a id="r_ad6e6395511f3c3839a42f634893ee164"></a>

```c
#define PIN_P3_4__QEC1_Y_A ALIF_PINMUX(3, 4, 6)
```

相关声明：[PIN_P3_4__QEC1_Y_A](#ad6e6395511f3c3839a42f634893ee164)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`QEC1_Y_A`。

<a id="r_ae136906f8123c136a7e152663076a1fa"></a>

```c
#define PIN_P3_4__CAM_D8_A ALIF_PINMUX(3, 4, 7)
```

相关声明：[PIN_P3_4__CAM_D8_A](#ae136906f8123c136a7e152663076a1fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`CAM_D8_A`。

<a id="r_a3f53dddbffc228108e7c1eb17ee058a4"></a>

```c
#define PIN_P3_5__GPIO ALIF_PINMUX(3, 5, 0)
```

相关声明：[PIN_P3_5__GPIO](#a3f53dddbffc228108e7c1eb17ee058a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.5` 的复用功能（Alternate Functions）。

<a id="r_a7fc7acde9b754dffdaa864b5ee54fb44"></a>

```c
#define PIN_P3_5__OSPI0_SCLKN_A ALIF_PINMUX(3, 5, 1)
```

相关声明：[PIN_P3_5__OSPI0_SCLKN_A](#a7fc7acde9b754dffdaa864b5ee54fb44)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`OSPI0_SCLKN_A`。

<a id="r_a089bc9a32dfe0c666bf67b1da11c200a"></a>

```c
#define PIN_P3_5__UART5_TX_A ALIF_PINMUX(3, 5, 2)
```

相关声明：[PIN_P3_5__UART5_TX_A](#a089bc9a32dfe0c666bf67b1da11c200a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`UART5_TX_A`。

<a id="r_a7cf933b9c6211dd08668b2132b7fcb01"></a>

```c
#define PIN_P3_5__LPPDM_DO_B ALIF_PINMUX(3, 5, 3)
```

相关声明：[PIN_P3_5__LPPDM_DO_B](#a7cf933b9c6211dd08668b2132b7fcb01)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`LPPDM_DO_B`。

<a id="r_a305645868ca565ed269a48043a6fb2d9"></a>

```c
#define PIN_P3_5__SPI0_SS1_B ALIF_PINMUX(3, 5, 4)
```

相关声明：[PIN_P3_5__SPI0_SS1_B](#a305645868ca565ed269a48043a6fb2d9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`SPI0_SS1_B`。

<a id="r_a775a93715f9a556bbb359bc9d4483a0e"></a>

```c
#define PIN_P3_5__I2C0_SDA_B ALIF_PINMUX(3, 5, 5)
```

相关声明：[PIN_P3_5__I2C0_SDA_B](#a775a93715f9a556bbb359bc9d4483a0e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`I2C0_SDA_B`。

<a id="r_ac36f03cf5b7982ca0f93cc6f72166a8a"></a>

```c
#define PIN_P3_5__QEC1_Z_A ALIF_PINMUX(3, 5, 6)
```

相关声明：[PIN_P3_5__QEC1_Z_A](#ac36f03cf5b7982ca0f93cc6f72166a8a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`QEC1_Z_A`。

<a id="r_aeaa8655a99307bee669e168ef00aebf3"></a>

```c
#define PIN_P3_5__CAM_D9_A ALIF_PINMUX(3, 5, 7)
```

相关声明：[PIN_P3_5__CAM_D9_A](#aeaa8655a99307bee669e168ef00aebf3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`CAM_D9_A`。

<a id="r_a6de92753c75d2827828767a9ed529829"></a>

```c
#define PIN_P3_6__GPIO ALIF_PINMUX(3, 6, 0)
```

相关声明：[PIN_P3_6__GPIO](#a6de92753c75d2827828767a9ed529829)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.6` 的复用功能（Alternate Functions）。

<a id="r_a8dcc9473cc0421a6fc13f955d766706c"></a>

```c
#define PIN_P3_6__HFXO_OUT_A ALIF_PINMUX(3, 6, 1)
```

相关声明：[PIN_P3_6__HFXO_OUT_A](#a8dcc9473cc0421a6fc13f955d766706c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`HFXO_OUT_A`。

<a id="r_ae73382d7e3ca133ff282b1f281d19cf2"></a>

```c
#define PIN_P3_6__LPUART_CTS_B ALIF_PINMUX(3, 6, 2)
```

相关声明：[PIN_P3_6__LPUART_CTS_B](#ae73382d7e3ca133ff282b1f281d19cf2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`LPUART_CTS_B`。

<a id="r_aec50fbbc0ef5faf9e7f65e7a5975b273"></a>

```c
#define PIN_P3_6__LPPDM_C1_B ALIF_PINMUX(3, 6, 3)
```

相关声明：[PIN_P3_6__LPPDM_C1_B](#aec50fbbc0ef5faf9e7f65e7a5975b273)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`LPPDM_C1_B`。

<a id="r_a4474c1dae558d0a9ce5f113eab5c60ea"></a>

```c
#define PIN_P3_6__SPI0_SS2_B ALIF_PINMUX(3, 6, 4)
```

相关声明：[PIN_P3_6__SPI0_SS2_B](#a4474c1dae558d0a9ce5f113eab5c60ea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`SPI0_SS2_B`。

<a id="r_ab8537cba85090cfc2c9bbe72c6c7ccb7"></a>

```c
#define PIN_P3_6__I2C1_SDA_B ALIF_PINMUX(3, 6, 5)
```

相关声明：[PIN_P3_6__I2C1_SDA_B](#ab8537cba85090cfc2c9bbe72c6c7ccb7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`I2C1_SDA_B`。

<a id="r_af2adbee156a78c5c61512c7376bd39fb"></a>

```c
#define PIN_P3_6__QEC2_X_A ALIF_PINMUX(3, 6, 6)
```

相关声明：[PIN_P3_6__QEC2_X_A](#af2adbee156a78c5c61512c7376bd39fb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`QEC2_X_A`。

<a id="r_a3f1fdd1c8aaf26eb18c13ed71a5eb26a"></a>

```c
#define PIN_P3_6__CAM_D10_A ALIF_PINMUX(3, 6, 7)
```

相关声明：[PIN_P3_6__CAM_D10_A](#a3f1fdd1c8aaf26eb18c13ed71a5eb26a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`CAM_D10_A`。

<a id="r_a60d3cb4a00a06169c18eedd0593c0e3b"></a>

```c
#define PIN_P3_7__GPIO ALIF_PINMUX(3, 7, 0)
```

相关声明：[PIN_P3_7__GPIO](#a60d3cb4a00a06169c18eedd0593c0e3b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.7` 的复用功能（Alternate Functions）。

<a id="r_a92596105a0f8236c4ef8cfc58580ce2a"></a>

```c
#define PIN_P3_7__JTAG0_TRACECLK ALIF_PINMUX(3, 7, 1)
```

相关声明：[PIN_P3_7__JTAG0_TRACECLK](#a92596105a0f8236c4ef8cfc58580ce2a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`JTAG0_TRACECLK`。

<a id="r_aca12188c280e9b043eb8af55b2b4bbf0"></a>

```c
#define PIN_P3_7__LPUART_RTS_B ALIF_PINMUX(3, 7, 2)
```

相关声明：[PIN_P3_7__LPUART_RTS_B](#aca12188c280e9b043eb8af55b2b4bbf0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`LPUART_RTS_B`。

<a id="r_a5d9255b7352d89afc3c8c43139d0ca2d"></a>

```c
#define PIN_P3_7__LPPDM_D1_B ALIF_PINMUX(3, 7, 3)
```

相关声明：[PIN_P3_7__LPPDM_D1_B](#a5d9255b7352d89afc3c8c43139d0ca2d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`LPPDM_D1_B`。

<a id="r_affc5f0a75e96cc6327cec31adb4fb9d7"></a>

```c
#define PIN_P3_7__SPI1_SS1_A ALIF_PINMUX(3, 7, 4)
```

相关声明：[PIN_P3_7__SPI1_SS1_A](#affc5f0a75e96cc6327cec31adb4fb9d7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`SPI1_SS1_A`。

<a id="r_af3466c0dca56a62cb762174d47b85118"></a>

```c
#define PIN_P3_7__I2C1_SCL_B ALIF_PINMUX(3, 7, 5)
```

相关声明：[PIN_P3_7__I2C1_SCL_B](#af3466c0dca56a62cb762174d47b85118)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`I2C1_SCL_B`。

<a id="r_aa3c253cd1c5a3247ab412596d853c5f5"></a>

```c
#define PIN_P3_7__QEC2_Y_A ALIF_PINMUX(3, 7, 6)
```

相关声明：[PIN_P3_7__QEC2_Y_A](#aa3c253cd1c5a3247ab412596d853c5f5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`QEC2_Y_A`。

<a id="r_a48aaf47242ae02df16dd1689f6c5f155"></a>

```c
#define PIN_P3_7__CAM_D11_A ALIF_PINMUX(3, 7, 7)
```

相关声明：[PIN_P3_7__CAM_D11_A](#a48aaf47242ae02df16dd1689f6c5f155)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`CAM_D11_A`。

<a id="define-members-5"></a>

### 端口 4 的引脚定义（Port 4 Pin Definitions）

GPIO 端口（Port）4 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a1ab2ef5cf337828d3e4be24bba3391e6"></a>

```c
#define PIN_P4_0__GPIO ALIF_PINMUX(4, 0, 0)
```

相关声明：[PIN_P4_0__GPIO](#a1ab2ef5cf337828d3e4be24bba3391e6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.0` 的复用功能（Alternate Functions）。

<a id="r_a86076829771e261af384c66974a9f7ff"></a>

```c
#define PIN_P4_0__JTAG0_TDATA0 ALIF_PINMUX(4, 0, 1)
```

相关声明：[PIN_P4_0__JTAG0_TDATA0](#a86076829771e261af384c66974a9f7ff)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`JTAG0_TDATA0`。

<a id="r_a4d64ab7e7d18c8f20d0cf177adf1b89b"></a>

```c
#define PIN_P4_0__APLL_OUT_A ALIF_PINMUX(4, 0, 2)
```

相关声明：[PIN_P4_0__APLL_OUT_A](#a4d64ab7e7d18c8f20d0cf177adf1b89b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`APLL_OUT_A`。

<a id="r_ab74dba96fd07a01a87937196a9cf5e37"></a>

```c
#define PIN_P4_0__I2S1_WS_A ALIF_PINMUX(4, 0, 3)
```

相关声明：[PIN_P4_0__I2S1_WS_A](#ab74dba96fd07a01a87937196a9cf5e37)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`I2S1_WS_A`。

<a id="r_a1dc4196c647c8e6b06737779c81ccbca"></a>

```c
#define PIN_P4_0__SPI1_SS2_A ALIF_PINMUX(4, 0, 4)
```

相关声明：[PIN_P4_0__SPI1_SS2_A](#a1dc4196c647c8e6b06737779c81ccbca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`SPI1_SS2_A`。

<a id="r_a1de41f5582dd807e013ab8bfc440aba6"></a>

```c
#define PIN_P4_0__QEC2_Z_A ALIF_PINMUX(4, 0, 5)
```

相关声明：[PIN_P4_0__QEC2_Z_A](#a1de41f5582dd807e013ab8bfc440aba6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`QEC2_Z_A`。

<a id="r_a2e463cc07539e43e956355a907627b26"></a>

```c
#define PIN_P4_0__CDC_VSYNC_B ALIF_PINMUX(4, 0, 6)
```

相关声明：[PIN_P4_0__CDC_VSYNC_B](#a2e463cc07539e43e956355a907627b26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`CDC_VSYNC_B`。

<a id="r_a3bb26e78e1b13d1b8334f62837a6d634"></a>

```c
#define PIN_P4_0__CAM_D12_A ALIF_PINMUX(4, 0, 7)
```

相关声明：[PIN_P4_0__CAM_D12_A](#a3bb26e78e1b13d1b8334f62837a6d634)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`CAM_D12_A`。

<a id="r_a5fb4375020986c6656759f3223558f10"></a>

```c
#define PIN_P4_1__GPIO ALIF_PINMUX(4, 1, 0)
```

相关声明：[PIN_P4_1__GPIO](#a5fb4375020986c6656759f3223558f10)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.1` 的复用功能（Alternate Functions）。

<a id="r_ae3bdf81bc183b5b5f91d6e1cdff0ed9e"></a>

```c
#define PIN_P4_1__JTAG0_TDATA1 ALIF_PINMUX(4, 1, 1)
```

相关声明：[PIN_P4_1__JTAG0_TDATA1](#ae3bdf81bc183b5b5f91d6e1cdff0ed9e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`JTAG0_TDATA1`。

<a id="r_aecb4db0667f7c228780c1eb21e7ebc67"></a>

```c
#define PIN_P4_1__I2S0_SDI_B ALIF_PINMUX(4, 1, 2)
```

相关声明：[PIN_P4_1__I2S0_SDI_B](#aecb4db0667f7c228780c1eb21e7ebc67)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`I2S0_SDI_B`。

<a id="r_a724a7b36c0c03d06956eed86d907d195"></a>

```c
#define PIN_P4_1__SPI1_SS3_A ALIF_PINMUX(4, 1, 3)
```

相关声明：[PIN_P4_1__SPI1_SS3_A](#a724a7b36c0c03d06956eed86d907d195)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`SPI1_SS3_A`。

<a id="r_a33cf5fdcb6246f20e11294e3fe2ee5a8"></a>

```c
#define PIN_P4_1__QEC3_X_A ALIF_PINMUX(4, 1, 4)
```

相关声明：[PIN_P4_1__QEC3_X_A](#a33cf5fdcb6246f20e11294e3fe2ee5a8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`QEC3_X_A`。

<a id="r_a1cfa948cf149c9975a5a90f557f2ca5d"></a>

```c
#define PIN_P4_1__SD_CLK_D ALIF_PINMUX(4, 1, 5)
```

相关声明：[PIN_P4_1__SD_CLK_D](#a1cfa948cf149c9975a5a90f557f2ca5d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`SD_CLK_D`。

<a id="r_a81411c54132629886379f9795f0d3504"></a>

```c
#define PIN_P4_1__CDC_HSYNC_B ALIF_PINMUX(4, 1, 6)
```

相关声明：[PIN_P4_1__CDC_HSYNC_B](#a81411c54132629886379f9795f0d3504)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`CDC_HSYNC_B`。

<a id="r_a446e9e914f59c6daa81d90d4929f7a3e"></a>

```c
#define PIN_P4_1__CAM_D13_A ALIF_PINMUX(4, 1, 7)
```

相关声明：[PIN_P4_1__CAM_D13_A](#a446e9e914f59c6daa81d90d4929f7a3e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`CAM_D13_A`。

<a id="r_a2a9f0b7627d1f0149fa1cddc428e76f9"></a>

```c
#define PIN_P4_2__GPIO ALIF_PINMUX(4, 2, 0)
```

相关声明：[PIN_P4_2__GPIO](#a2a9f0b7627d1f0149fa1cddc428e76f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.2` 的复用功能（Alternate Functions）。

<a id="r_ad6ac79e681a0c110e38afde11bde0a91"></a>

```c
#define PIN_P4_2__JTAG0_TDATA2 ALIF_PINMUX(4, 2, 1)
```

相关声明：[PIN_P4_2__JTAG0_TDATA2](#ad6ac79e681a0c110e38afde11bde0a91)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`JTAG0_TDATA2`。

<a id="r_a4826bd5accf8c5c35b4c9375ef68001f"></a>

```c
#define PIN_P4_2__LPI2C1_SDA_A ALIF_PINMUX(4, 2, 2)
```

相关声明：[PIN_P4_2__LPI2C1_SDA_A](#a4826bd5accf8c5c35b4c9375ef68001f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`LPI2C1_SDA_A`。

<a id="r_a78f480ef1aa0d692eba930bceec76518"></a>

```c
#define PIN_P4_2__I2S0_SDO_B ALIF_PINMUX(4, 2, 3)
```

相关声明：[PIN_P4_2__I2S0_SDO_B](#a78f480ef1aa0d692eba930bceec76518)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`I2S0_SDO_B`。

<a id="r_a2540b24293afcf26019769d63cf1a3fe"></a>

```c
#define PIN_P4_2__SPI2_MISO_A ALIF_PINMUX(4, 2, 4)
```

相关声明：[PIN_P4_2__SPI2_MISO_A](#a2540b24293afcf26019769d63cf1a3fe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`SPI2_MISO_A`。

<a id="r_a5d88b8bf2baae0426adfc982f54d7bd4"></a>

```c
#define PIN_P4_2__QEC3_Y_A ALIF_PINMUX(4, 2, 5)
```

相关声明：[PIN_P4_2__QEC3_Y_A](#a5d88b8bf2baae0426adfc982f54d7bd4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`QEC3_Y_A`。

<a id="r_a2a14d7d416fad7d60af53778a4b08edd"></a>

```c
#define PIN_P4_2__SD_CMD_D ALIF_PINMUX(4, 2, 6)
```

相关声明：[PIN_P4_2__SD_CMD_D](#a2a14d7d416fad7d60af53778a4b08edd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`SD_CMD_D`。

<a id="r_a0354de3c1060268335afbded61177cc8"></a>

```c
#define PIN_P4_2__CAM_D14_A ALIF_PINMUX(4, 2, 7)
```

相关声明：[PIN_P4_2__CAM_D14_A](#a0354de3c1060268335afbded61177cc8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`CAM_D14_A`。

<a id="r_a97b4675f5259e06d48cdd30755a46f3e"></a>

```c
#define PIN_P4_3__GPIO ALIF_PINMUX(4, 3, 0)
```

相关声明：[PIN_P4_3__GPIO](#a97b4675f5259e06d48cdd30755a46f3e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.3` 的复用功能（Alternate Functions）。

<a id="r_a2fcaaedf7a85609b19db31228eaed463"></a>

```c
#define PIN_P4_3__JTAG0_TDATA3 ALIF_PINMUX(4, 3, 1)
```

相关声明：[PIN_P4_3__JTAG0_TDATA3](#a2fcaaedf7a85609b19db31228eaed463)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`JTAG0_TDATA3`。

<a id="r_a3f6bdede6384a4038847b2272472c6a1"></a>

```c
#define PIN_P4_3__LPI2C1_SCL_A ALIF_PINMUX(4, 3, 2)
```

相关声明：[PIN_P4_3__LPI2C1_SCL_A](#a3f6bdede6384a4038847b2272472c6a1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`LPI2C1_SCL_A`。

<a id="r_aa00669ae9c9416a1cc1c47311a5d8c93"></a>

```c
#define PIN_P4_3__I2S0_SCLK_B ALIF_PINMUX(4, 3, 3)
```

相关声明：[PIN_P4_3__I2S0_SCLK_B](#aa00669ae9c9416a1cc1c47311a5d8c93)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`I2S0_SCLK_B`。

<a id="r_af3e803ca5495352c98a07f1451b13f55"></a>

```c
#define PIN_P4_3__SPI2_MOSI_A ALIF_PINMUX(4, 3, 4)
```

相关声明：[PIN_P4_3__SPI2_MOSI_A](#af3e803ca5495352c98a07f1451b13f55)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`SPI2_MOSI_A`。

<a id="r_aedca512b9e51012bb05f50b67d045ee1"></a>

```c
#define PIN_P4_3__QEC3_Z_A ALIF_PINMUX(4, 3, 5)
```

相关声明：[PIN_P4_3__QEC3_Z_A](#aedca512b9e51012bb05f50b67d045ee1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`QEC3_Z_A`。

<a id="r_a9f5b8736ca866c11f10d09d22ccdc2fd"></a>

```c
#define PIN_P4_3__SD_RST_D ALIF_PINMUX(4, 3, 6)
```

相关声明：[PIN_P4_3__SD_RST_D](#a9f5b8736ca866c11f10d09d22ccdc2fd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`SD_RST_D`。

<a id="r_a6c31bd33f5f9199591339b4cbbf3a0f9"></a>

```c
#define PIN_P4_3__CAM_D15_A ALIF_PINMUX(4, 3, 7)
```

相关声明：[PIN_P4_3__CAM_D15_A](#a6c31bd33f5f9199591339b4cbbf3a0f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`CAM_D15_A`。

<a id="r_a71f56da2cfc34a4fa6dbbba7e9936d28"></a>

```c
#define PIN_P4_4__GPIO ALIF_PINMUX(4, 4, 0)
```

相关声明：[PIN_P4_4__GPIO](#a71f56da2cfc34a4fa6dbbba7e9936d28)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.4` 的复用功能（Alternate Functions）。

<a id="r_a026da00206cb806cf7e868c00dfa15de"></a>

```c
#define PIN_P4_4__JTAG0_TCK ALIF_PINMUX(4, 4, 1)
```

相关声明：[PIN_P4_4__JTAG0_TCK](#a026da00206cb806cf7e868c00dfa15de)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`JTAG0_TCK`。

<a id="r_a517a020d5c948995364f2312904b6018"></a>

```c
#define PIN_P4_4__I2S0_WS_B ALIF_PINMUX(4, 4, 2)
```

相关声明：[PIN_P4_4__I2S0_WS_B](#a517a020d5c948995364f2312904b6018)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`I2S0_WS_B`。

<a id="r_af5dff5e905e521347a9a9571c4fa6361"></a>

```c
#define PIN_P4_4__SPI2_SCLK_A ALIF_PINMUX(4, 4, 3)
```

相关声明：[PIN_P4_4__SPI2_SCLK_A](#af5dff5e905e521347a9a9571c4fa6361)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`SPI2_SCLK_A`。

<a id="r_ac444c571b0be2a2a8683c04da4db9a85"></a>

```c
#define PIN_P4_4__FAULT0_A ALIF_PINMUX(4, 4, 4)
```

相关声明：[PIN_P4_4__FAULT0_A](#ac444c571b0be2a2a8683c04da4db9a85)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`FAULT0_A`。

<a id="r_a44781940091d6eadb753aa098a1c8a3a"></a>

```c
#define PIN_P4_5__GPIO ALIF_PINMUX(4, 5, 0)
```

相关声明：[PIN_P4_5__GPIO](#a44781940091d6eadb753aa098a1c8a3a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.5` 的复用功能（Alternate Functions）。

<a id="r_ac8c66019ed9ef1f3e1761b9676666d7c"></a>

```c
#define PIN_P4_5__JTAG0_TMS ALIF_PINMUX(4, 5, 1)
```

相关声明：[PIN_P4_5__JTAG0_TMS](#ac8c66019ed9ef1f3e1761b9676666d7c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`JTAG0_TMS`。

<a id="r_a96b572900d599f788751338a196db2ee"></a>

```c
#define PIN_P4_5__SPI2_SS0_A ALIF_PINMUX(4, 5, 2)
```

相关声明：[PIN_P4_5__SPI2_SS0_A](#a96b572900d599f788751338a196db2ee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`SPI2_SS0_A`。

<a id="r_afeedeeea96759b383282b0304e66941c"></a>

```c
#define PIN_P4_5__FAULT1_A ALIF_PINMUX(4, 5, 3)
```

相关声明：[PIN_P4_5__FAULT1_A](#afeedeeea96759b383282b0304e66941c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`FAULT1_A`。

<a id="r_aae4c2f3f2743c6281127d761c2d3c952"></a>

```c
#define PIN_P4_6__GPIO ALIF_PINMUX(4, 6, 0)
```

相关声明：[PIN_P4_6__GPIO](#aae4c2f3f2743c6281127d761c2d3c952)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.6` 的复用功能（Alternate Functions）。

<a id="r_a64e905aad463ddb010ef5e31aa4bb355"></a>

```c
#define PIN_P4_6__JTAG0_TDI ALIF_PINMUX(4, 6, 1)
```

相关声明：[PIN_P4_6__JTAG0_TDI](#a64e905aad463ddb010ef5e31aa4bb355)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`JTAG0_TDI`。

<a id="r_ada6fe7a94f5948aa450c52df17a1f6d3"></a>

```c
#define PIN_P4_6__SPI2_SS1_A ALIF_PINMUX(4, 6, 2)
```

相关声明：[PIN_P4_6__SPI2_SS1_A](#ada6fe7a94f5948aa450c52df17a1f6d3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`SPI2_SS1_A`。

<a id="r_a4b838a52a7d7b92372f93c33d5ce32e8"></a>

```c
#define PIN_P4_6__FAULT2_A ALIF_PINMUX(4, 6, 3)
```

相关声明：[PIN_P4_6__FAULT2_A](#a4b838a52a7d7b92372f93c33d5ce32e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`FAULT2_A`。

<a id="r_a414ee602068915040eb8dab92a92bb61"></a>

```c
#define PIN_P4_7__GPIO ALIF_PINMUX(4, 7, 0)
```

相关声明：[PIN_P4_7__GPIO](#a414ee602068915040eb8dab92a92bb61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.7` 的复用功能（Alternate Functions）。

<a id="r_a1882c539a53276d676235207bd87494a"></a>

```c
#define PIN_P4_7__JTAG0_TDO ALIF_PINMUX(4, 7, 1)
```

相关声明：[PIN_P4_7__JTAG0_TDO](#a1882c539a53276d676235207bd87494a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`JTAG0_TDO`。

<a id="r_a7f053b743ad776d35543bbd4aeed4291"></a>

```c
#define PIN_P4_7__SPI2_SS2_A ALIF_PINMUX(4, 7, 2)
```

相关声明：[PIN_P4_7__SPI2_SS2_A](#a7f053b743ad776d35543bbd4aeed4291)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`SPI2_SS2_A`。

<a id="r_a3708d4f0c3187f5c3e82e7be8d5b7e88"></a>

```c
#define PIN_P4_7__FAULT3_A ALIF_PINMUX(4, 7, 3)
```

相关声明：[PIN_P4_7__FAULT3_A](#a3708d4f0c3187f5c3e82e7be8d5b7e88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`FAULT3_A`。

<a id="define-members-6"></a>

### 端口 5 的引脚定义（Port 5 Pin Definitions）

GPIO 端口（Port）5 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a456e61913b22b9d8a56be8b0377ac81e"></a>

```c
#define PIN_P5_0__GPIO ALIF_PINMUX(5, 0, 0)
```

相关声明：[PIN_P5_0__GPIO](#a456e61913b22b9d8a56be8b0377ac81e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.0` 的复用功能（Alternate Functions）。

<a id="r_a38d38f8ae3bae90deab3ce80caf0ee09"></a>

```c
#define PIN_P5_0__OSPI1_RXDS_A ALIF_PINMUX(5, 0, 1)
```

相关声明：[PIN_P5_0__OSPI1_RXDS_A](#a38d38f8ae3bae90deab3ce80caf0ee09)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`OSPI1_RXDS_A`。

<a id="r_ae55f7b3bba263faff5336e5e704e68a1"></a>

```c
#define PIN_P5_0__UART4_RX_C ALIF_PINMUX(5, 0, 2)
```

相关声明：[PIN_P5_0__UART4_RX_C](#ae55f7b3bba263faff5336e5e704e68a1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`UART4_RX_C`。

<a id="r_a8251fa8634b4fca0caee874df82c0fe3"></a>

```c
#define PIN_P5_0__PDM_D2_A ALIF_PINMUX(5, 0, 3)
```

相关声明：[PIN_P5_0__PDM_D2_A](#a8251fa8634b4fca0caee874df82c0fe3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`PDM_D2_A`。

<a id="r_a8d7a46642529764190d788a4e6fd45ad"></a>

```c
#define PIN_P5_0__SPI0_MISO_B ALIF_PINMUX(5, 0, 4)
```

相关声明：[PIN_P5_0__SPI0_MISO_B](#a8d7a46642529764190d788a4e6fd45ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`SPI0_MISO_B`。

<a id="r_a0a3d80a4b6d1716af1ad5ed469920c64"></a>

```c
#define PIN_P5_0__I2C2_SDA_B ALIF_PINMUX(5, 0, 5)
```

相关声明：[PIN_P5_0__I2C2_SDA_B](#a0a3d80a4b6d1716af1ad5ed469920c64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`I2C2_SDA_B`。

<a id="r_a5d9ca9901b30db06b82c4b24f4b9a080"></a>

```c
#define PIN_P5_0__UT0_T0_B ALIF_PINMUX(5, 0, 6)
```

相关声明：[PIN_P5_0__UT0_T0_B](#a5d9ca9901b30db06b82c4b24f4b9a080)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`UT0_T0_B`。

<a id="r_a2e92a4a046037ece8270c1279d22c177"></a>

```c
#define PIN_P5_0__SD_D0_A ALIF_PINMUX(5, 0, 7)
```

相关声明：[PIN_P5_0__SD_D0_A](#a2e92a4a046037ece8270c1279d22c177)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`SD_D0_A`。

<a id="r_a98fa74bbdae6f1f210c490cdc73d7cb8"></a>

```c
#define PIN_P5_1__GPIO ALIF_PINMUX(5, 1, 0)
```

相关声明：[PIN_P5_1__GPIO](#a98fa74bbdae6f1f210c490cdc73d7cb8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.1` 的复用功能（Alternate Functions）。

<a id="r_abe8b3c1281f707f6d860126f3ce452f5"></a>

```c
#define PIN_P5_1__OSPI1_SS0_A ALIF_PINMUX(5, 1, 1)
```

相关声明：[PIN_P5_1__OSPI1_SS0_A](#abe8b3c1281f707f6d860126f3ce452f5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`OSPI1_SS0_A`。

<a id="r_aaaf94476a9b2113d129e1357b61cab88"></a>

```c
#define PIN_P5_1__UART4_TX_C ALIF_PINMUX(5, 1, 2)
```

相关声明：[PIN_P5_1__UART4_TX_C](#aaaf94476a9b2113d129e1357b61cab88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`UART4_TX_C`。

<a id="r_a6d88b7b2fe07955ec419faef9b0fc542"></a>

```c
#define PIN_P5_1__PDM_D3_A ALIF_PINMUX(5, 1, 3)
```

相关声明：[PIN_P5_1__PDM_D3_A](#a6d88b7b2fe07955ec419faef9b0fc542)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`PDM_D3_A`。

<a id="r_a02c0d84f1ce09a7db4f16344ce7d6e0f"></a>

```c
#define PIN_P5_1__SPI0_MOSI_B ALIF_PINMUX(5, 1, 4)
```

相关声明：[PIN_P5_1__SPI0_MOSI_B](#a02c0d84f1ce09a7db4f16344ce7d6e0f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`SPI0_MOSI_B`。

<a id="r_a337b1b86add6bae57f8f3cf3e6b0316e"></a>

```c
#define PIN_P5_1__I2C2_SCL_B ALIF_PINMUX(5, 1, 5)
```

相关声明：[PIN_P5_1__I2C2_SCL_B](#a337b1b86add6bae57f8f3cf3e6b0316e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`I2C2_SCL_B`。

<a id="r_a576645eb18a7f9b249aa745cdf2763bd"></a>

```c
#define PIN_P5_1__UT0_T1_B ALIF_PINMUX(5, 1, 6)
```

相关声明：[PIN_P5_1__UT0_T1_B](#a576645eb18a7f9b249aa745cdf2763bd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`UT0_T1_B`。

<a id="r_ad23c4691fc9bc556d010d12280678018"></a>

```c
#define PIN_P5_1__SD_D1_A ALIF_PINMUX(5, 1, 7)
```

相关声明：[PIN_P5_1__SD_D1_A](#ad23c4691fc9bc556d010d12280678018)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`SD_D1_A`。

<a id="r_a97a74c55bf53c437a39b3f10cfa778bc"></a>

```c
#define PIN_P5_2__GPIO ALIF_PINMUX(5, 2, 0)
```

相关声明：[PIN_P5_2__GPIO](#a97a74c55bf53c437a39b3f10cfa778bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.2` 的复用功能（Alternate Functions）。

<a id="r_aeb292ae2d7a8c7fe6fcc98e89383d5bd"></a>

```c
#define PIN_P5_2__OSPI1_SCLKN_A ALIF_PINMUX(5, 2, 1)
```

相关声明：[PIN_P5_2__OSPI1_SCLKN_A](#aeb292ae2d7a8c7fe6fcc98e89383d5bd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`OSPI1_SCLKN_A`。

<a id="r_ab92d5af8661fa39bb5c5344fe8b5c5d2"></a>

```c
#define PIN_P5_2__UART5_RX_C ALIF_PINMUX(5, 2, 2)
```

相关声明：[PIN_P5_2__UART5_RX_C](#ab92d5af8661fa39bb5c5344fe8b5c5d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`UART5_RX_C`。

<a id="r_a92b9e7a2225b7430c821afff772501b1"></a>

```c
#define PIN_P5_2__PDM_C3_A ALIF_PINMUX(5, 2, 3)
```

相关声明：[PIN_P5_2__PDM_C3_A](#a92b9e7a2225b7430c821afff772501b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`PDM_C3_A`。

<a id="r_ab94c708fa67f401c517167652262ee25"></a>

```c
#define PIN_P5_2__SPI0_SS0_B ALIF_PINMUX(5, 2, 4)
```

相关声明：[PIN_P5_2__SPI0_SS0_B](#ab94c708fa67f401c517167652262ee25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`SPI0_SS0_B`。

<a id="r_a892bb2cd62f830b62180a28935584442"></a>

```c
#define PIN_P5_2__LPI2C0_SCL_B ALIF_PINMUX(5, 2, 5)
```

相关声明：[PIN_P5_2__LPI2C0_SCL_B](#a892bb2cd62f830b62180a28935584442)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`LPI2C0_SCL_B`。

<a id="r_a65e944abdcb0b4d0eec9d47cdc5ea36f"></a>

```c
#define PIN_P5_2__UT1_T0_B ALIF_PINMUX(5, 2, 6)
```

相关声明：[PIN_P5_2__UT1_T0_B](#a65e944abdcb0b4d0eec9d47cdc5ea36f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`UT1_T0_B`。

<a id="r_a2c66e34e62616968081d9b785c298e89"></a>

```c
#define PIN_P5_2__SD_D2_A ALIF_PINMUX(5, 2, 7)
```

相关声明：[PIN_P5_2__SD_D2_A](#a2c66e34e62616968081d9b785c298e89)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`SD_D2_A`。

<a id="r_af2c171dfdada8390ed0c80e115f024eb"></a>

```c
#define PIN_P5_3__GPIO ALIF_PINMUX(5, 3, 0)
```

相关声明：[PIN_P5_3__GPIO](#af2c171dfdada8390ed0c80e115f024eb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.3` 的复用功能（Alternate Functions）。

<a id="r_ad770693b035fa8cdcf85199cdb6296f8"></a>

```c
#define PIN_P5_3__OSPI1_SCLK_A ALIF_PINMUX(5, 3, 1)
```

相关声明：[PIN_P5_3__OSPI1_SCLK_A](#ad770693b035fa8cdcf85199cdb6296f8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`OSPI1_SCLK_A`。

<a id="r_a984109f4b5194e919517f1a88ce2f173"></a>

```c
#define PIN_P5_3__UART5_TX_C ALIF_PINMUX(5, 3, 2)
```

相关声明：[PIN_P5_3__UART5_TX_C](#a984109f4b5194e919517f1a88ce2f173)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`UART5_TX_C`。

<a id="r_a1bbacbdb5ebd7073e5dc46bdafa49467"></a>

```c
#define PIN_P5_3__SPI0_SCLK_B ALIF_PINMUX(5, 3, 3)
```

相关声明：[PIN_P5_3__SPI0_SCLK_B](#a1bbacbdb5ebd7073e5dc46bdafa49467)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`SPI0_SCLK_B`。

<a id="r_a2c4599b05f666b7ea53515be543afc47"></a>

```c
#define PIN_P5_3__LPI2C0_SDA_B ALIF_PINMUX(5, 3, 4)
```

相关声明：[PIN_P5_3__LPI2C0_SDA_B](#a2c4599b05f666b7ea53515be543afc47)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`LPI2C0_SDA_B`。

<a id="r_a7cf30f670a605528e535e100cc7d6259"></a>

```c
#define PIN_P5_3__UT1_T1_B ALIF_PINMUX(5, 3, 5)
```

相关声明：[PIN_P5_3__UT1_T1_B](#a7cf30f670a605528e535e100cc7d6259)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`UT1_T1_B`。

<a id="r_aab6554ba3e217bd60c778793a0637938"></a>

```c
#define PIN_P5_3__SD_D3_A ALIF_PINMUX(5, 3, 6)
```

相关声明：[PIN_P5_3__SD_D3_A](#aab6554ba3e217bd60c778793a0637938)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`SD_D3_A`。

<a id="r_a238189907f455451e5d023d257b36ec0"></a>

```c
#define PIN_P5_3__CDC_PCLK_A ALIF_PINMUX(5, 3, 7)
```

相关声明：[PIN_P5_3__CDC_PCLK_A](#a238189907f455451e5d023d257b36ec0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`CDC_PCLK_A`。

<a id="r_a6846e3f2b170cb7a3216f81e5ec3b30e"></a>

```c
#define PIN_P5_4__GPIO ALIF_PINMUX(5, 4, 0)
```

相关声明：[PIN_P5_4__GPIO](#a6846e3f2b170cb7a3216f81e5ec3b30e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.4` 的复用功能（Alternate Functions）。

<a id="r_a24bae128d43897cb5ad1e4e1fbeb9999"></a>

```c
#define PIN_P5_4__OSPI1_SS1_A ALIF_PINMUX(5, 4, 1)
```

相关声明：[PIN_P5_4__OSPI1_SS1_A](#a24bae128d43897cb5ad1e4e1fbeb9999)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`OSPI1_SS1_A`。

<a id="r_ae8575f29fe033284403815de52e2b0b1"></a>

```c
#define PIN_P5_4__UART3_CTS_A ALIF_PINMUX(5, 4, 2)
```

相关声明：[PIN_P5_4__UART3_CTS_A](#ae8575f29fe033284403815de52e2b0b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`UART3_CTS_A`。

<a id="r_a7e382ce13d0f82f75edfb660eba65867"></a>

```c
#define PIN_P5_4__PDM_D2_B ALIF_PINMUX(5, 4, 3)
```

相关声明：[PIN_P5_4__PDM_D2_B](#a7e382ce13d0f82f75edfb660eba65867)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`PDM_D2_B`。

<a id="r_ae8083b7bfacd1411f63cda33c47fbd8a"></a>

```c
#define PIN_P5_4__SPI0_SS3_A ALIF_PINMUX(5, 4, 4)
```

相关声明：[PIN_P5_4__SPI0_SS3_A](#ae8083b7bfacd1411f63cda33c47fbd8a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`SPI0_SS3_A`。

<a id="r_a1ab3ffb8876342ce40588a35cded4e04"></a>

```c
#define PIN_P5_4__UT2_T0_B ALIF_PINMUX(5, 4, 5)
```

相关声明：[PIN_P5_4__UT2_T0_B](#a1ab3ffb8876342ce40588a35cded4e04)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`UT2_T0_B`。

<a id="r_a7293d170665dd2c6a04a211939a39134"></a>

```c
#define PIN_P5_4__SD_D4_A ALIF_PINMUX(5, 4, 6)
```

相关声明：[PIN_P5_4__SD_D4_A](#a7293d170665dd2c6a04a211939a39134)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`SD_D4_A`。

<a id="r_ab777f9158aae4ce2654f7b62430e50df"></a>

```c
#define PIN_P5_4__CDC_DE_A ALIF_PINMUX(5, 4, 7)
```

相关声明：[PIN_P5_4__CDC_DE_A](#ab777f9158aae4ce2654f7b62430e50df)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`CDC_DE_A`。

<a id="r_a466c951ce8310bac71e4a36b062e3b48"></a>

```c
#define PIN_P5_5__GPIO ALIF_PINMUX(5, 5, 0)
```

相关声明：[PIN_P5_5__GPIO](#a466c951ce8310bac71e4a36b062e3b48)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.5` 的复用功能（Alternate Functions）。

<a id="r_a8f88bd645e38b86560892fea67bd768e"></a>

```c
#define PIN_P5_5__OSPI1_SCLK_C ALIF_PINMUX(5, 5, 1)
```

相关声明：[PIN_P5_5__OSPI1_SCLK_C](#a8f88bd645e38b86560892fea67bd768e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`OSPI1_SCLK_C`。

<a id="r_aefd41d2a46a675a37216980f16e2fd58"></a>

```c
#define PIN_P5_5__UART3_RTS_A ALIF_PINMUX(5, 5, 2)
```

相关声明：[PIN_P5_5__UART3_RTS_A](#aefd41d2a46a675a37216980f16e2fd58)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`UART3_RTS_A`。

<a id="r_a0c81622ee140b8913502807a6c560792"></a>

```c
#define PIN_P5_5__PDM_D3_B ALIF_PINMUX(5, 5, 3)
```

相关声明：[PIN_P5_5__PDM_D3_B](#a0c81622ee140b8913502807a6c560792)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`PDM_D3_B`。

<a id="r_a05e05aac0465080bbbff700323a68631"></a>

```c
#define PIN_P5_5__UT2_T1_B ALIF_PINMUX(5, 5, 4)
```

相关声明：[PIN_P5_5__UT2_T1_B](#a05e05aac0465080bbbff700323a68631)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`UT2_T1_B`。

<a id="r_aeb2cd7eebb652c43aa0f1809e816ecf0"></a>

```c
#define PIN_P5_5__SD_D5_A ALIF_PINMUX(5, 5, 5)
```

相关声明：[PIN_P5_5__SD_D5_A](#aeb2cd7eebb652c43aa0f1809e816ecf0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`SD_D5_A`。

<a id="r_a5fe74885176a43241bd56514eb40a78d"></a>

```c
#define PIN_P5_5__ETH_RXD0_A ALIF_PINMUX(5, 5, 6)
```

相关声明：[PIN_P5_5__ETH_RXD0_A](#a5fe74885176a43241bd56514eb40a78d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`ETH_RXD0_A`。

<a id="r_ab8c45949da634838ed5ab9cd77d5e108"></a>

```c
#define PIN_P5_5__CDC_HSYNC_A ALIF_PINMUX(5, 5, 7)
```

相关声明：[PIN_P5_5__CDC_HSYNC_A](#ab8c45949da634838ed5ab9cd77d5e108)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`CDC_HSYNC_A`。

<a id="r_acd3416c5b74cd24d02c29e3144d63436"></a>

```c
#define PIN_P5_6__GPIO ALIF_PINMUX(5, 6, 0)
```

相关声明：[PIN_P5_6__GPIO](#acd3416c5b74cd24d02c29e3144d63436)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.6` 的复用功能（Alternate Functions）。

<a id="r_a3bd03266c3d91de23071a3d0241e97e3"></a>

```c
#define PIN_P5_6__UART1_CTS_B ALIF_PINMUX(5, 6, 1)
```

相关声明：[PIN_P5_6__UART1_CTS_B](#a3bd03266c3d91de23071a3d0241e97e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`UART1_CTS_B`。

<a id="r_a7bb8e7df55124de4d1d5d1e0136ec791"></a>

```c
#define PIN_P5_6__I2C2_SCL_C ALIF_PINMUX(5, 6, 2)
```

相关声明：[PIN_P5_6__I2C2_SCL_C](#a7bb8e7df55124de4d1d5d1e0136ec791)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`I2C2_SCL_C`。

<a id="r_a3b51e56aff1116a7f78c72b8d105a4f3"></a>

```c
#define PIN_P5_6__UT3_T0_B ALIF_PINMUX(5, 6, 3)
```

相关声明：[PIN_P5_6__UT3_T0_B](#a3b51e56aff1116a7f78c72b8d105a4f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`UT3_T0_B`。

<a id="r_a255d5c869e69a05f60dbd2545133d6db"></a>

```c
#define PIN_P5_6__SD_D6_A ALIF_PINMUX(5, 6, 4)
```

相关声明：[PIN_P5_6__SD_D6_A](#a255d5c869e69a05f60dbd2545133d6db)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`SD_D6_A`。

<a id="r_a122c965e0d825860f500690c068010ad"></a>

```c
#define PIN_P5_6__ETH_RXD1_A ALIF_PINMUX(5, 6, 5)
```

相关声明：[PIN_P5_6__ETH_RXD1_A](#a122c965e0d825860f500690c068010ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`ETH_RXD1_A`。

<a id="r_ad052d0128c64793bf06c8235680591bc"></a>

```c
#define PIN_P5_6__CDC_VSYNC_A ALIF_PINMUX(5, 6, 6)
```

相关声明：[PIN_P5_6__CDC_VSYNC_A](#ad052d0128c64793bf06c8235680591bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`CDC_VSYNC_A`。

<a id="r_abc168fa2810d9a33b66d8899581c97ed"></a>

```c
#define PIN_P5_7__GPIO ALIF_PINMUX(5, 7, 0)
```

相关声明：[PIN_P5_7__GPIO](#abc168fa2810d9a33b66d8899581c97ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.7` 的复用功能（Alternate Functions）。

<a id="r_a10109fc6ff0b3958f2bfbb530e9ec192"></a>

```c
#define PIN_P5_7__OSPI1_SS0_C ALIF_PINMUX(5, 7, 1)
```

相关声明：[PIN_P5_7__OSPI1_SS0_C](#a10109fc6ff0b3958f2bfbb530e9ec192)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`OSPI1_SS0_C`。

<a id="r_a16337846b4c79f3bf2b8601bd2b97f91"></a>

```c
#define PIN_P5_7__UART1_RTS_B ALIF_PINMUX(5, 7, 2)
```

相关声明：[PIN_P5_7__UART1_RTS_B](#a16337846b4c79f3bf2b8601bd2b97f91)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`UART1_RTS_B`。

<a id="r_a1eafcfc5a29262235cfca353e2cec793"></a>

```c
#define PIN_P5_7__I2C2_SDA_C ALIF_PINMUX(5, 7, 3)
```

相关声明：[PIN_P5_7__I2C2_SDA_C](#a1eafcfc5a29262235cfca353e2cec793)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`I2C2_SDA_C`。

<a id="r_ae4fc1d80ddbf968fee17d1487bc3a1e8"></a>

```c
#define PIN_P5_7__UT3_T1_B ALIF_PINMUX(5, 7, 4)
```

相关声明：[PIN_P5_7__UT3_T1_B](#ae4fc1d80ddbf968fee17d1487bc3a1e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`UT3_T1_B`。

<a id="r_afd5e370c63d9395a646422f878defdb8"></a>

```c
#define PIN_P5_7__SD_D7_A ALIF_PINMUX(5, 7, 5)
```

相关声明：[PIN_P5_7__SD_D7_A](#afd5e370c63d9395a646422f878defdb8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`SD_D7_A`。

<a id="r_af90659a4ef350cc3759d00d4cc2df529"></a>

```c
#define PIN_P5_7__ETH_RST_A ALIF_PINMUX(5, 7, 6)
```

相关声明：[PIN_P5_7__ETH_RST_A](#af90659a4ef350cc3759d00d4cc2df529)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`ETH_RST_A`。

<a id="define-members-7"></a>

### 端口 6 的引脚定义（Port 6 Pin Definitions）

GPIO 端口（Port）6 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_ae7ade9dfd32e609fb86f13f6525953fc"></a>

```c
#define PIN_P6_0__GPIO ALIF_PINMUX(6, 0, 0)
```

相关声明：[PIN_P6_0__GPIO](#ae7ade9dfd32e609fb86f13f6525953fc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.0` 的复用功能（Alternate Functions）。

<a id="r_af006833ac80c14da05e6a4599a24ac61"></a>

```c
#define PIN_P6_0__OSPI0_D0_C ALIF_PINMUX(6, 0, 1)
```

相关声明：[PIN_P6_0__OSPI0_D0_C](#af006833ac80c14da05e6a4599a24ac61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`OSPI0_D0_C`。

<a id="r_ada38a2f1ef366ed1e1bc1a7283a1181e"></a>

```c
#define PIN_P6_0__UART4_DE_A ALIF_PINMUX(6, 0, 2)
```

相关声明：[PIN_P6_0__UART4_DE_A](#ada38a2f1ef366ed1e1bc1a7283a1181e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`UART4_DE_A`。

<a id="r_a5b804aab91d3d453bfa99b86da3136be"></a>

```c
#define PIN_P6_0__PDM_D0_C ALIF_PINMUX(6, 0, 3)
```

相关声明：[PIN_P6_0__PDM_D0_C](#a5b804aab91d3d453bfa99b86da3136be)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`PDM_D0_C`。

<a id="r_a402739f36398287a0c22a91323b91e04"></a>

```c
#define PIN_P6_0__UT4_T0_B ALIF_PINMUX(6, 0, 4)
```

相关声明：[PIN_P6_0__UT4_T0_B](#a402739f36398287a0c22a91323b91e04)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`UT4_T0_B`。

<a id="r_a9cee6c3cc19b52912293b79a4a264d0e"></a>

```c
#define PIN_P6_0__SD_D0_D ALIF_PINMUX(6, 0, 5)
```

相关声明：[PIN_P6_0__SD_D0_D](#a9cee6c3cc19b52912293b79a4a264d0e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`SD_D0_D`。

<a id="r_aed149da5f699fd5c2a29cd5a12e08ab5"></a>

```c
#define PIN_P6_0__ETH_TXD0_A ALIF_PINMUX(6, 0, 6)
```

相关声明：[PIN_P6_0__ETH_TXD0_A](#aed149da5f699fd5c2a29cd5a12e08ab5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`ETH_TXD0_A`。

<a id="r_ae69d866c114aa4304b207ece8b102c8b"></a>

```c
#define PIN_P6_0__LPSPI_SS1_A ALIF_PINMUX(6, 0, 7)
```

相关声明：[PIN_P6_0__LPSPI_SS1_A](#ae69d866c114aa4304b207ece8b102c8b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`LPSPI_SS1_A`。

<a id="r_ad55f5467ffabdbffd5b51ddfeaed9c4f"></a>

```c
#define PIN_P6_1__GPIO ALIF_PINMUX(6, 1, 0)
```

相关声明：[PIN_P6_1__GPIO](#ad55f5467ffabdbffd5b51ddfeaed9c4f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.1` 的复用功能（Alternate Functions）。

<a id="r_aa0c327b4b44ee5068c84f65827555817"></a>

```c
#define PIN_P6_1__OSPI0_D1_C ALIF_PINMUX(6, 1, 1)
```

相关声明：[PIN_P6_1__OSPI0_D1_C](#aa0c327b4b44ee5068c84f65827555817)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`OSPI0_D1_C`。

<a id="r_aeb4ee42999e56e3a6c98cf66e476be59"></a>

```c
#define PIN_P6_1__UART5_DE_A ALIF_PINMUX(6, 1, 2)
```

相关声明：[PIN_P6_1__UART5_DE_A](#aeb4ee42999e56e3a6c98cf66e476be59)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`UART5_DE_A`。

<a id="r_af3dc31906265cf8bba81d8fc925b180d"></a>

```c
#define PIN_P6_1__PDM_C0_C ALIF_PINMUX(6, 1, 3)
```

相关声明：[PIN_P6_1__PDM_C0_C](#af3dc31906265cf8bba81d8fc925b180d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`PDM_C0_C`。

<a id="r_a1e1c46edc4c4a367c7c6d4e1f8fff335"></a>

```c
#define PIN_P6_1__UT4_T1_B ALIF_PINMUX(6, 1, 4)
```

相关声明：[PIN_P6_1__UT4_T1_B](#a1e1c46edc4c4a367c7c6d4e1f8fff335)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`UT4_T1_B`。

<a id="r_a1c445b43a94d1635e7174caf60e97515"></a>

```c
#define PIN_P6_1__SD_D1_D ALIF_PINMUX(6, 1, 5)
```

相关声明：[PIN_P6_1__SD_D1_D](#a1c445b43a94d1635e7174caf60e97515)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`SD_D1_D`。

<a id="r_a8dd66a2e9cdd82b4e68015167b7bdcbc"></a>

```c
#define PIN_P6_1__ETH_TXD1_A ALIF_PINMUX(6, 1, 6)
```

相关声明：[PIN_P6_1__ETH_TXD1_A](#a8dd66a2e9cdd82b4e68015167b7bdcbc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`ETH_TXD1_A`。

<a id="r_a76a7ed4d6d4b4f9c8c733e84ede8e3e7"></a>

```c
#define PIN_P6_1__LPSPI_SS2_A ALIF_PINMUX(6, 1, 7)
```

相关声明：[PIN_P6_1__LPSPI_SS2_A](#a76a7ed4d6d4b4f9c8c733e84ede8e3e7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`LPSPI_SS2_A`。

<a id="r_adae4d80fc2a0fb040a8eed5c89e72cdd"></a>

```c
#define PIN_P6_2__GPIO ALIF_PINMUX(6, 2, 0)
```

相关声明：[PIN_P6_2__GPIO](#adae4d80fc2a0fb040a8eed5c89e72cdd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.2` 的复用功能（Alternate Functions）。

<a id="r_a1a29ae10d58edee6e97fd88d3057f1d6"></a>

```c
#define PIN_P6_2__OSPI0_D2_C ALIF_PINMUX(6, 2, 1)
```

相关声明：[PIN_P6_2__OSPI0_D2_C](#a1a29ae10d58edee6e97fd88d3057f1d6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`OSPI0_D2_C`。

<a id="r_a9bae739436d46b7844632df7afa34d94"></a>

```c
#define PIN_P6_2__UART2_CTS_A ALIF_PINMUX(6, 2, 2)
```

相关声明：[PIN_P6_2__UART2_CTS_A](#a9bae739436d46b7844632df7afa34d94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`UART2_CTS_A`。

<a id="r_a4a9f88b662c4b84e2f3a5528909fccee"></a>

```c
#define PIN_P6_2__LPI3C_SDA_A ALIF_PINMUX(6, 2, 3)
```

相关声明：[PIN_P6_2__LPI3C_SDA_A](#a4a9f88b662c4b84e2f3a5528909fccee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`LPI3C_SDA_A`。

<a id="r_ac4c16861bda7b2dbefcf702539014843"></a>

```c
#define PIN_P6_2__PDM_D1_C ALIF_PINMUX(6, 2, 4)
```

相关声明：[PIN_P6_2__PDM_D1_C](#ac4c16861bda7b2dbefcf702539014843)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`PDM_D1_C`。

<a id="r_ad597d36c8c835cbf70d7f47e26b6d81a"></a>

```c
#define PIN_P6_2__UT5_T0_B ALIF_PINMUX(6, 2, 5)
```

相关声明：[PIN_P6_2__UT5_T0_B](#ad597d36c8c835cbf70d7f47e26b6d81a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`UT5_T0_B`。

<a id="r_a097abf1cabcdb008ce0f09bae51eb06c"></a>

```c
#define PIN_P6_2__SD_D2_D ALIF_PINMUX(6, 2, 6)
```

相关声明：[PIN_P6_2__SD_D2_D](#a097abf1cabcdb008ce0f09bae51eb06c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`SD_D2_D`。

<a id="r_abb3f78429006127f69d0bf3e5f2267b0"></a>

```c
#define PIN_P6_2__ETH_TXEN_A ALIF_PINMUX(6, 2, 7)
```

相关声明：[PIN_P6_2__ETH_TXEN_A](#abb3f78429006127f69d0bf3e5f2267b0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`ETH_TXEN_A`。

<a id="r_a9c055a8795fbd5a4145bf758a72d1d23"></a>

```c
#define PIN_P6_3__GPIO ALIF_PINMUX(6, 3, 0)
```

相关声明：[PIN_P6_3__GPIO](#a9c055a8795fbd5a4145bf758a72d1d23)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.3` 的复用功能（Alternate Functions）。

<a id="r_ab9ef591fd0935f7082f8a08d31f3393f"></a>

```c
#define PIN_P6_3__OSPI0_D3_C ALIF_PINMUX(6, 3, 1)
```

相关声明：[PIN_P6_3__OSPI0_D3_C](#ab9ef591fd0935f7082f8a08d31f3393f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`OSPI0_D3_C`。

<a id="r_a6407df773a1b7922599c36f9d5ba134f"></a>

```c
#define PIN_P6_3__UART2_RTS_A ALIF_PINMUX(6, 3, 2)
```

相关声明：[PIN_P6_3__UART2_RTS_A](#a6407df773a1b7922599c36f9d5ba134f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`UART2_RTS_A`。

<a id="r_a4c6ef322bf1641221a89d79f80d9e54b"></a>

```c
#define PIN_P6_3__LPI3C_SCL_A ALIF_PINMUX(6, 3, 3)
```

相关声明：[PIN_P6_3__LPI3C_SCL_A](#a4c6ef322bf1641221a89d79f80d9e54b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`LPI3C_SCL_A`。

<a id="r_a8445cb982e67a20abbd68ba9f0aa76bd"></a>

```c
#define PIN_P6_3__PDM_C1_C ALIF_PINMUX(6, 3, 4)
```

相关声明：[PIN_P6_3__PDM_C1_C](#a8445cb982e67a20abbd68ba9f0aa76bd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`PDM_C1_C`。

<a id="r_aaff27d0a5cff17c25bd2b1b46fcd4aec"></a>

```c
#define PIN_P6_3__UT5_T1_B ALIF_PINMUX(6, 3, 5)
```

相关声明：[PIN_P6_3__UT5_T1_B](#aaff27d0a5cff17c25bd2b1b46fcd4aec)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`UT5_T1_B`。

<a id="r_a3c17bec984f4e85d9f9f571a0b60e3fb"></a>

```c
#define PIN_P6_3__SD_D3_D ALIF_PINMUX(6, 3, 6)
```

相关声明：[PIN_P6_3__SD_D3_D](#a3c17bec984f4e85d9f9f571a0b60e3fb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`SD_D3_D`。

<a id="r_a3fdfbc0ae95496472b9a0b95efa67009"></a>

```c
#define PIN_P6_3__ETH_IRQ_A ALIF_PINMUX(6, 3, 7)
```

相关声明：[PIN_P6_3__ETH_IRQ_A](#a3fdfbc0ae95496472b9a0b95efa67009)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`ETH_IRQ_A`。

<a id="r_a80712cd6a9a977af7a2f879634daf24d"></a>

```c
#define PIN_P6_4__GPIO ALIF_PINMUX(6, 4, 0)
```

相关声明：[PIN_P6_4__GPIO](#a80712cd6a9a977af7a2f879634daf24d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.4` 的复用功能（Alternate Functions）。

<a id="r_a587f62993920d1f067ce5b5119b05aab"></a>

```c
#define PIN_P6_4__OSPI0_D4_C ALIF_PINMUX(6, 4, 1)
```

相关声明：[PIN_P6_4__OSPI0_D4_C](#a587f62993920d1f067ce5b5119b05aab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`OSPI0_D4_C`。

<a id="r_a3ce358cbdd477ef4755e0a59e5d62b22"></a>

```c
#define PIN_P6_4__UART2_CTS_B ALIF_PINMUX(6, 4, 2)
```

相关声明：[PIN_P6_4__UART2_CTS_B](#a3ce358cbdd477ef4755e0a59e5d62b22)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`UART2_CTS_B`。

<a id="r_a4710b74789b94bdfb32c93bdde987275"></a>

```c
#define PIN_P6_4__LRFC_OUT_A ALIF_PINMUX(6, 4, 3)
```

相关声明：[PIN_P6_4__LRFC_OUT_A](#a4710b74789b94bdfb32c93bdde987275)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`LRFC_OUT_A`。

<a id="r_a4097acd4e3c33280170dbea58ab20604"></a>

```c
#define PIN_P6_4__SPI1_SS0_B ALIF_PINMUX(6, 4, 4)
```

相关声明：[PIN_P6_4__SPI1_SS0_B](#a4097acd4e3c33280170dbea58ab20604)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`SPI1_SS0_B`。

<a id="r_a6b587d186ecf998fcd206b77404c1c8f"></a>

```c
#define PIN_P6_4__UT6_T0_B ALIF_PINMUX(6, 4, 5)
```

相关声明：[PIN_P6_4__UT6_T0_B](#a6b587d186ecf998fcd206b77404c1c8f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`UT6_T0_B`。

<a id="r_a5ca66e739931cdbbd828ac11f3625797"></a>

```c
#define PIN_P6_4__SD_D4_D ALIF_PINMUX(6, 4, 6)
```

相关声明：[PIN_P6_4__SD_D4_D](#a5ca66e739931cdbbd828ac11f3625797)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`SD_D4_D`。

<a id="r_a520b5fa720b201790a99eb45431a09f9"></a>

```c
#define PIN_P6_4__ETH_REFCLK_A ALIF_PINMUX(6, 4, 7)
```

相关声明：[PIN_P6_4__ETH_REFCLK_A](#a520b5fa720b201790a99eb45431a09f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`ETH_REFCLK_A`。

<a id="r_a4f8cb1991ad80690327a9272f790c7fa"></a>

```c
#define PIN_P6_5__GPIO ALIF_PINMUX(6, 5, 0)
```

相关声明：[PIN_P6_5__GPIO](#a4f8cb1991ad80690327a9272f790c7fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.5` 的复用功能（Alternate Functions）。

<a id="r_ae178273fd0d60e578038153dfa3d44d2"></a>

```c
#define PIN_P6_5__OSPI0_D5_C ALIF_PINMUX(6, 5, 1)
```

相关声明：[PIN_P6_5__OSPI0_D5_C](#ae178273fd0d60e578038153dfa3d44d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`OSPI0_D5_C`。

<a id="r_ac1b09ec40a2a0d186be393ce2a22bb6e"></a>

```c
#define PIN_P6_5__UART2_RTS_B ALIF_PINMUX(6, 5, 2)
```

相关声明：[PIN_P6_5__UART2_RTS_B](#ac1b09ec40a2a0d186be393ce2a22bb6e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`UART2_RTS_B`。

<a id="r_ab6c15149f8b91e22006b04b4ccc1ad20"></a>

```c
#define PIN_P6_5__LPI2C1_SDA_B ALIF_PINMUX(6, 5, 3)
```

相关声明：[PIN_P6_5__LPI2C1_SDA_B](#ab6c15149f8b91e22006b04b4ccc1ad20)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`LPI2C1_SDA_B`。

<a id="r_af896508d8b1829141300d9c174c6a4dc"></a>

```c
#define PIN_P6_5__SPI1_SS1_B ALIF_PINMUX(6, 5, 4)
```

相关声明：[PIN_P6_5__SPI1_SS1_B](#af896508d8b1829141300d9c174c6a4dc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`SPI1_SS1_B`。

<a id="r_a916adb647d27f3566a0b42449d85c4a9"></a>

```c
#define PIN_P6_5__UT6_T1_B ALIF_PINMUX(6, 5, 5)
```

相关声明：[PIN_P6_5__UT6_T1_B](#a916adb647d27f3566a0b42449d85c4a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`UT6_T1_B`。

<a id="r_a5e8205cbf5db34bf667639f7a32b212d"></a>

```c
#define PIN_P6_5__SD_D5_D ALIF_PINMUX(6, 5, 6)
```

相关声明：[PIN_P6_5__SD_D5_D](#a5e8205cbf5db34bf667639f7a32b212d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`SD_D5_D`。

<a id="r_a1acc616b5209cc593c2330115a14ac57"></a>

```c
#define PIN_P6_5__ETH_MDIO_A ALIF_PINMUX(6, 5, 7)
```

相关声明：[PIN_P6_5__ETH_MDIO_A](#a1acc616b5209cc593c2330115a14ac57)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`ETH_MDIO_A`。

<a id="r_ae379d12c8cb8b76c585b3745eef14bfc"></a>

```c
#define PIN_P6_6__GPIO ALIF_PINMUX(6, 6, 0)
```

相关声明：[PIN_P6_6__GPIO](#ae379d12c8cb8b76c585b3745eef14bfc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.6` 的复用功能（Alternate Functions）。

<a id="r_a8adab274d4857b76f38a42a19c7af021"></a>

```c
#define PIN_P6_6__OSPI0_D6_C ALIF_PINMUX(6, 6, 1)
```

相关声明：[PIN_P6_6__OSPI0_D6_C](#a8adab274d4857b76f38a42a19c7af021)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`OSPI0_D6_C`。

<a id="r_a149c5ebf20984a0032f56170946e1b76"></a>

```c
#define PIN_P6_6__UART0_CTS_B ALIF_PINMUX(6, 6, 2)
```

相关声明：[PIN_P6_6__UART0_CTS_B](#a149c5ebf20984a0032f56170946e1b76)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`UART0_CTS_B`。

<a id="r_aba610b37817ff9ca78102b5e39b8382c"></a>

```c
#define PIN_P6_6__LPI2C1_SCL_B ALIF_PINMUX(6, 6, 3)
```

相关声明：[PIN_P6_6__LPI2C1_SCL_B](#aba610b37817ff9ca78102b5e39b8382c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`LPI2C1_SCL_B`。

<a id="r_a88f58696cc0671871bbf7e67d96411ba"></a>

```c
#define PIN_P6_6__SPI1_SS2_B ALIF_PINMUX(6, 6, 4)
```

相关声明：[PIN_P6_6__SPI1_SS2_B](#a88f58696cc0671871bbf7e67d96411ba)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`SPI1_SS2_B`。

<a id="r_a7a6a79728de2d21d2e9d8e1c4ef8d81f"></a>

```c
#define PIN_P6_6__UT7_T0_B ALIF_PINMUX(6, 6, 5)
```

相关声明：[PIN_P6_6__UT7_T0_B](#a7a6a79728de2d21d2e9d8e1c4ef8d81f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`UT7_T0_B`。

<a id="r_a7d30cf3447edf43ec02ea570fbaca29a"></a>

```c
#define PIN_P6_6__SD_D6_D ALIF_PINMUX(6, 6, 6)
```

相关声明：[PIN_P6_6__SD_D6_D](#a7d30cf3447edf43ec02ea570fbaca29a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`SD_D6_D`。

<a id="r_affd24cc4890332ab2e6292bb5b34437d"></a>

```c
#define PIN_P6_6__ETH_MDC_A ALIF_PINMUX(6, 6, 7)
```

相关声明：[PIN_P6_6__ETH_MDC_A](#affd24cc4890332ab2e6292bb5b34437d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`ETH_MDC_A`。

<a id="r_a1e66098ffe67eddd23463192fcd1fbcd"></a>

```c
#define PIN_P6_7__GPIO ALIF_PINMUX(6, 7, 0)
```

相关声明：[PIN_P6_7__GPIO](#a1e66098ffe67eddd23463192fcd1fbcd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.7` 的复用功能（Alternate Functions）。

<a id="r_aef69daa6cb1613f9c4e417eaa709d9df"></a>

```c
#define PIN_P6_7__OSPI0_D7_C ALIF_PINMUX(6, 7, 1)
```

相关声明：[PIN_P6_7__OSPI0_D7_C](#aef69daa6cb1613f9c4e417eaa709d9df)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`OSPI0_D7_C`。

<a id="r_ae4dd7c19afbead2d7459b0e317238ae4"></a>

```c
#define PIN_P6_7__UART0_RTS_B ALIF_PINMUX(6, 7, 2)
```

相关声明：[PIN_P6_7__UART0_RTS_B](#ae4dd7c19afbead2d7459b0e317238ae4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`UART0_RTS_B`。

<a id="r_ae9d35ac26e71b26e7772f77cf7e90ddb"></a>

```c
#define PIN_P6_7__PDM_C2_A ALIF_PINMUX(6, 7, 3)
```

相关声明：[PIN_P6_7__PDM_C2_A](#ae9d35ac26e71b26e7772f77cf7e90ddb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`PDM_C2_A`。

<a id="r_aa7ffcbeb2e8ffd0f250fa1c144c90944"></a>

```c
#define PIN_P6_7__SPI1_SS3_B ALIF_PINMUX(6, 7, 4)
```

相关声明：[PIN_P6_7__SPI1_SS3_B](#aa7ffcbeb2e8ffd0f250fa1c144c90944)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`SPI1_SS3_B`。

<a id="r_a55c1a3571873fc72ef41cdf77589af42"></a>

```c
#define PIN_P6_7__UT7_T1_B ALIF_PINMUX(6, 7, 5)
```

相关声明：[PIN_P6_7__UT7_T1_B](#a55c1a3571873fc72ef41cdf77589af42)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`UT7_T1_B`。

<a id="r_a391061e40809b0bc10035a3850709364"></a>

```c
#define PIN_P6_7__SD_D7_D ALIF_PINMUX(6, 7, 6)
```

相关声明：[PIN_P6_7__SD_D7_D](#a391061e40809b0bc10035a3850709364)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`SD_D7_D`。

<a id="r_afa6eac87bb7aa7316085bb6ec187adb1"></a>

```c
#define PIN_P6_7__ETH_CRS_DV_A ALIF_PINMUX(6, 7, 7)
```

相关声明：[PIN_P6_7__ETH_CRS_DV_A](#afa6eac87bb7aa7316085bb6ec187adb1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`ETH_CRS_DV_A`。

<a id="define-members-8"></a>

### 端口 7 的引脚定义（Port 7 Pin Definitions）

GPIO 端口（Port）7 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_ac5e4bcb47b0ccd35d7458401dbe81233"></a>

```c
#define PIN_P7_0__GPIO ALIF_PINMUX(7, 0, 0)
```

相关声明：[PIN_P7_0__GPIO](#ac5e4bcb47b0ccd35d7458401dbe81233)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.0` 的复用功能（Alternate Functions）。

<a id="r_ae22354ee8a017c5e71ec62a007ca6b11"></a>

```c
#define PIN_P7_0__LPUT0_T0_A ALIF_PINMUX(7, 0, 1)
```

相关声明：[PIN_P7_0__LPUT0_T0_A](#ae22354ee8a017c5e71ec62a007ca6b11)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`LPUT0_T0_A`。

<a id="r_a573f0d4279a1715761d6676bcb2e6694"></a>

```c
#define PIN_P7_0__CMP3_OUT_A ALIF_PINMUX(7, 0, 2)
```

相关声明：[PIN_P7_0__CMP3_OUT_A](#a573f0d4279a1715761d6676bcb2e6694)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`CMP3_OUT_A`。

<a id="r_af0831316631026230f9038d7fadf92e7"></a>

```c
#define PIN_P7_0__SPI0_MISO_C ALIF_PINMUX(7, 0, 3)
```

相关声明：[PIN_P7_0__SPI0_MISO_C](#af0831316631026230f9038d7fadf92e7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`SPI0_MISO_C`。

<a id="r_a1fde60e018d010f91f259fe2684f2bef"></a>

```c
#define PIN_P7_0__I2C0_SDA_C ALIF_PINMUX(7, 0, 4)
```

相关声明：[PIN_P7_0__I2C0_SDA_C](#a1fde60e018d010f91f259fe2684f2bef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`I2C0_SDA_C`。

<a id="r_aa2090c10fe53165b850dd0cfbd00b28e"></a>

```c
#define PIN_P7_0__UT8_T0_B ALIF_PINMUX(7, 0, 5)
```

相关声明：[PIN_P7_0__UT8_T0_B](#aa2090c10fe53165b850dd0cfbd00b28e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`UT8_T0_B`。

<a id="r_af19527b153d09b5a76baaaf5ee394509"></a>

```c
#define PIN_P7_0__SD_CMD_A ALIF_PINMUX(7, 0, 6)
```

相关声明：[PIN_P7_0__SD_CMD_A](#af19527b153d09b5a76baaaf5ee394509)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`SD_CMD_A`。

<a id="r_a315b39b900cb690c70021e36cb57a52e"></a>

```c
#define PIN_P7_0__CAN_RXD_A ALIF_PINMUX(7, 0, 7)
```

相关声明：[PIN_P7_0__CAN_RXD_A](#a315b39b900cb690c70021e36cb57a52e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`CAN_RXD_A`。

<a id="r_afd333ffdddac335d52e506deb72eacaf"></a>

```c
#define PIN_P7_1__GPIO ALIF_PINMUX(7, 1, 0)
```

相关声明：[PIN_P7_1__GPIO](#afd333ffdddac335d52e506deb72eacaf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.1` 的复用功能（Alternate Functions）。

<a id="r_a5934e917d97771544a2de6f7df6b177c"></a>

```c
#define PIN_P7_1__LPUT0_T1_A ALIF_PINMUX(7, 1, 1)
```

相关声明：[PIN_P7_1__LPUT0_T1_A](#a5934e917d97771544a2de6f7df6b177c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`LPUT0_T1_A`。

<a id="r_a0f00923007990dc5d99c9e68cb9b8bea"></a>

```c
#define PIN_P7_1__CMP2_OUT_A ALIF_PINMUX(7, 1, 2)
```

相关声明：[PIN_P7_1__CMP2_OUT_A](#a0f00923007990dc5d99c9e68cb9b8bea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`CMP2_OUT_A`。

<a id="r_aeb314afb125e7530cd9002ff3dc3b107"></a>

```c
#define PIN_P7_1__SPI0_MOSI_C ALIF_PINMUX(7, 1, 3)
```

相关声明：[PIN_P7_1__SPI0_MOSI_C](#aeb314afb125e7530cd9002ff3dc3b107)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`SPI0_MOSI_C`。

<a id="r_af1c7a7f1fc1d87b7036a5ac346c435a7"></a>

```c
#define PIN_P7_1__I2C0_SCL_C ALIF_PINMUX(7, 1, 4)
```

相关声明：[PIN_P7_1__I2C0_SCL_C](#af1c7a7f1fc1d87b7036a5ac346c435a7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`I2C0_SCL_C`。

<a id="r_a2cf53f369584f6c900545f79981f24ca"></a>

```c
#define PIN_P7_1__UT8_T1_B ALIF_PINMUX(7, 1, 5)
```

相关声明：[PIN_P7_1__UT8_T1_B](#a2cf53f369584f6c900545f79981f24ca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`UT8_T1_B`。

<a id="r_a644faaea1fba0a87fabe761141752c1f"></a>

```c
#define PIN_P7_1__SD_CLK_A ALIF_PINMUX(7, 1, 6)
```

相关声明：[PIN_P7_1__SD_CLK_A](#a644faaea1fba0a87fabe761141752c1f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`SD_CLK_A`。

<a id="r_a0c095cb41bcce62e68f99852527fb472"></a>

```c
#define PIN_P7_1__CAN_TXD_A ALIF_PINMUX(7, 1, 7)
```

相关声明：[PIN_P7_1__CAN_TXD_A](#a0c095cb41bcce62e68f99852527fb472)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`CAN_TXD_A`。

<a id="r_adc16259fec5582a1e6ebc9cb8a825c03"></a>

```c
#define PIN_P7_2__GPIO ALIF_PINMUX(7, 2, 0)
```

相关声明：[PIN_P7_2__GPIO](#adc16259fec5582a1e6ebc9cb8a825c03)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.2` 的复用功能（Alternate Functions）。

<a id="r_ac414182ecfa6cdfc7249c7aa2d59681a"></a>

```c
#define PIN_P7_2__LPUT1_T0_A ALIF_PINMUX(7, 2, 1)
```

相关声明：[PIN_P7_2__LPUT1_T0_A](#ac414182ecfa6cdfc7249c7aa2d59681a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`LPUT1_T0_A`。

<a id="r_a0228bb15a003556d45cdba01039e5fb3"></a>

```c
#define PIN_P7_2__UART3_CTS_B ALIF_PINMUX(7, 2, 2)
```

相关声明：[PIN_P7_2__UART3_CTS_B](#a0228bb15a003556d45cdba01039e5fb3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`UART3_CTS_B`。

<a id="r_a9741c146d7f9b394e10e8ecbc2547bb5"></a>

```c
#define PIN_P7_2__CMP1_OUT_A ALIF_PINMUX(7, 2, 3)
```

相关声明：[PIN_P7_2__CMP1_OUT_A](#a9741c146d7f9b394e10e8ecbc2547bb5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`CMP1_OUT_A`。

<a id="r_ad36e1683e60fe5a8ac68fff42ea59029"></a>

```c
#define PIN_P7_2__SPI0_SCLK_C ALIF_PINMUX(7, 2, 4)
```

相关声明：[PIN_P7_2__SPI0_SCLK_C](#ad36e1683e60fe5a8ac68fff42ea59029)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`SPI0_SCLK_C`。

<a id="r_a803ef3f2d107d05670bba596998fca2a"></a>

```c
#define PIN_P7_2__I2C1_SDA_C ALIF_PINMUX(7, 2, 5)
```

相关声明：[PIN_P7_2__I2C1_SDA_C](#a803ef3f2d107d05670bba596998fca2a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`I2C1_SDA_C`。

<a id="r_a827131e3b96c2ff6166e10b6bf8a714a"></a>

```c
#define PIN_P7_2__UT9_T0_B ALIF_PINMUX(7, 2, 6)
```

相关声明：[PIN_P7_2__UT9_T0_B](#a827131e3b96c2ff6166e10b6bf8a714a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`UT9_T0_B`。

<a id="r_aa1020e341c285beed6019cf5c9e7cd0f"></a>

```c
#define PIN_P7_2__SD_RST_A ALIF_PINMUX(7, 2, 7)
```

相关声明：[PIN_P7_2__SD_RST_A](#aa1020e341c285beed6019cf5c9e7cd0f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`SD_RST_A`。

<a id="r_a75dbeec7072793acd5eaa20f0d0d1055"></a>

```c
#define PIN_P7_3__GPIO ALIF_PINMUX(7, 3, 0)
```

相关声明：[PIN_P7_3__GPIO](#a75dbeec7072793acd5eaa20f0d0d1055)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.3` 的复用功能（Alternate Functions）。

<a id="r_a286332f2ba4230cc9d065d89dd366ee8"></a>

```c
#define PIN_P7_3__LPUT1_T1_A ALIF_PINMUX(7, 3, 1)
```

相关声明：[PIN_P7_3__LPUT1_T1_A](#a286332f2ba4230cc9d065d89dd366ee8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`LPUT1_T1_A`。

<a id="r_a70267fe4f07b3962dc3f82831eaec387"></a>

```c
#define PIN_P7_3__UART3_RTS_B ALIF_PINMUX(7, 3, 2)
```

相关声明：[PIN_P7_3__UART3_RTS_B](#a70267fe4f07b3962dc3f82831eaec387)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`UART3_RTS_B`。

<a id="r_afad69246b1edd640cbc69277c6dea5f7"></a>

```c
#define PIN_P7_3__CMP0_OUT_A ALIF_PINMUX(7, 3, 3)
```

相关声明：[PIN_P7_3__CMP0_OUT_A](#afad69246b1edd640cbc69277c6dea5f7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`CMP0_OUT_A`。

<a id="r_a6d6173bcd02b0ae215e1c1dd4756ea49"></a>

```c
#define PIN_P7_3__SPI0_SS0_C ALIF_PINMUX(7, 3, 4)
```

相关声明：[PIN_P7_3__SPI0_SS0_C](#a6d6173bcd02b0ae215e1c1dd4756ea49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`SPI0_SS0_C`。

<a id="r_a62c7010c5c2ec0aa887cdc198dc4ab61"></a>

```c
#define PIN_P7_3__I2C1_SCL_C ALIF_PINMUX(7, 3, 5)
```

相关声明：[PIN_P7_3__I2C1_SCL_C](#a62c7010c5c2ec0aa887cdc198dc4ab61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`I2C1_SCL_C`。

<a id="r_a70d270eee3fd69cf7b2a0baf848829bd"></a>

```c
#define PIN_P7_3__UT9_T1_B ALIF_PINMUX(7, 3, 6)
```

相关声明：[PIN_P7_3__UT9_T1_B](#a70d270eee3fd69cf7b2a0baf848829bd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`UT9_T1_B`。

<a id="r_a4736c7a65fab9ad1788b1b333ecd9048"></a>

```c
#define PIN_P7_3__CAN_STBY_A ALIF_PINMUX(7, 3, 7)
```

相关声明：[PIN_P7_3__CAN_STBY_A](#a4736c7a65fab9ad1788b1b333ecd9048)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`CAN_STBY_A`。

<a id="r_ae4761d31982dad9a275346a237d734c7"></a>

```c
#define PIN_P7_4__GPIO ALIF_PINMUX(7, 4, 0)
```

相关声明：[PIN_P7_4__GPIO](#ae4761d31982dad9a275346a237d734c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.4` 的复用功能（Alternate Functions）。

<a id="r_a4a2ce8e3f9a8ee8c6cc63189fd4f1b2b"></a>

```c
#define PIN_P7_4__LPUT2_T0_A ALIF_PINMUX(7, 4, 1)
```

相关声明：[PIN_P7_4__LPUT2_T0_A](#a4a2ce8e3f9a8ee8c6cc63189fd4f1b2b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPUT2_T0_A`。

<a id="r_af9b0f86a16481eaa6ba6158c3c4a1f27"></a>

```c
#define PIN_P7_4__LPUART_CTS_A ALIF_PINMUX(7, 4, 2)
```

相关声明：[PIN_P7_4__LPUART_CTS_A](#af9b0f86a16481eaa6ba6158c3c4a1f27)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPUART_CTS_A`。

<a id="r_a59af3f76078b27d2140424517cc75344"></a>

```c
#define PIN_P7_4__LPPDM_C2_A ALIF_PINMUX(7, 4, 3)
```

相关声明：[PIN_P7_4__LPPDM_C2_A](#a59af3f76078b27d2140424517cc75344)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPPDM_C2_A`。

<a id="r_a78ee9a3bf488866f266cba2bfac445c3"></a>

```c
#define PIN_P7_4__LPSPI_MISO_A ALIF_PINMUX(7, 4, 4)
```

相关声明：[PIN_P7_4__LPSPI_MISO_A](#a78ee9a3bf488866f266cba2bfac445c3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPSPI_MISO_A`。

<a id="r_a60f056cd47fb1a96f4fafa3e2c069766"></a>

```c
#define PIN_P7_4__LPI2C0_SCL_A ALIF_PINMUX(7, 4, 5)
```

相关声明：[PIN_P7_4__LPI2C0_SCL_A](#a60f056cd47fb1a96f4fafa3e2c069766)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPI2C0_SCL_A`。

<a id="r_a29e164a0438f28339ce98a0fb9575e78"></a>

```c
#define PIN_P7_4__UT10_T0_B ALIF_PINMUX(7, 4, 6)
```

相关声明：[PIN_P7_4__UT10_T0_B](#a29e164a0438f28339ce98a0fb9575e78)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`UT10_T0_B`。

<a id="r_ac47d162d1d4eb774e733fe27673c7c6b"></a>

```c
#define PIN_P7_5__GPIO ALIF_PINMUX(7, 5, 0)
```

相关声明：[PIN_P7_5__GPIO](#ac47d162d1d4eb774e733fe27673c7c6b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.5` 的复用功能（Alternate Functions）。

<a id="r_a6d6127b10c8091e50322519c6dfd7717"></a>

```c
#define PIN_P7_5__LPUT2_T1_A ALIF_PINMUX(7, 5, 1)
```

相关声明：[PIN_P7_5__LPUT2_T1_A](#a6d6127b10c8091e50322519c6dfd7717)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPUT2_T1_A`。

<a id="r_a528ac9bd32e60609a78a980cdf5599c7"></a>

```c
#define PIN_P7_5__LPUART_RTS_A ALIF_PINMUX(7, 5, 2)
```

相关声明：[PIN_P7_5__LPUART_RTS_A](#a528ac9bd32e60609a78a980cdf5599c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPUART_RTS_A`。

<a id="r_aa749c8fc95bb1b08d0e30577bf16ea25"></a>

```c
#define PIN_P7_5__LFXO_OUT_A ALIF_PINMUX(7, 5, 3)
```

相关声明：[PIN_P7_5__LFXO_OUT_A](#aa749c8fc95bb1b08d0e30577bf16ea25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LFXO_OUT_A`。

<a id="r_a8c7a9903bb1ee74e9e3d008269a9208c"></a>

```c
#define PIN_P7_5__LPPDM_D2_A ALIF_PINMUX(7, 5, 4)
```

相关声明：[PIN_P7_5__LPPDM_D2_A](#a8c7a9903bb1ee74e9e3d008269a9208c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPPDM_D2_A`。

<a id="r_a6b1969e563d7224a9056d36904d6e3db"></a>

```c
#define PIN_P7_5__LPSPI_MOSI_A ALIF_PINMUX(7, 5, 5)
```

相关声明：[PIN_P7_5__LPSPI_MOSI_A](#a6b1969e563d7224a9056d36904d6e3db)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPSPI_MOSI_A`。

<a id="r_af08809b51ad5dfd7d5bdd46aa2bc5072"></a>

```c
#define PIN_P7_5__LPI2C0_SDA_A ALIF_PINMUX(7, 5, 6)
```

相关声明：[PIN_P7_5__LPI2C0_SDA_A](#af08809b51ad5dfd7d5bdd46aa2bc5072)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPI2C0_SDA_A`。

<a id="r_a8a91b43d2f6023ae6d6e60347456613c"></a>

```c
#define PIN_P7_5__UT10_T1_B ALIF_PINMUX(7, 5, 7)
```

相关声明：[PIN_P7_5__UT10_T1_B](#a8a91b43d2f6023ae6d6e60347456613c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`UT10_T1_B`。

<a id="r_ab95fc52f53c6a1703df290ac307871e4"></a>

```c
#define PIN_P7_6__GPIO ALIF_PINMUX(7, 6, 0)
```

相关声明：[PIN_P7_6__GPIO](#ab95fc52f53c6a1703df290ac307871e4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.6` 的复用功能（Alternate Functions）。

<a id="r_aec52e333e3549d491bf248f21537c997"></a>

```c
#define PIN_P7_6__LPI2C1_SDA_C ALIF_PINMUX(7, 6, 1)
```

相关声明：[PIN_P7_6__LPI2C1_SDA_C](#aec52e333e3549d491bf248f21537c997)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPI2C1_SDA_C`。

<a id="r_a8e8245f9ad371815fe2ecde177626055"></a>

```c
#define PIN_P7_6__LPUART_RX_A ALIF_PINMUX(7, 6, 2)
```

相关声明：[PIN_P7_6__LPUART_RX_A](#a8e8245f9ad371815fe2ecde177626055)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPUART_RX_A`。

<a id="r_af6c6d6ca80af88d9bda2d5c721942271"></a>

```c
#define PIN_P7_6__LPI3C_SDA_B ALIF_PINMUX(7, 6, 3)
```

相关声明：[PIN_P7_6__LPI3C_SDA_B](#af6c6d6ca80af88d9bda2d5c721942271)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPI3C_SDA_B`。

<a id="r_aa762aaa39051c078d337fd65c3af5594"></a>

```c
#define PIN_P7_6__LPPDM_C3_A ALIF_PINMUX(7, 6, 4)
```

相关声明：[PIN_P7_6__LPPDM_C3_A](#aa762aaa39051c078d337fd65c3af5594)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPPDM_C3_A`。

<a id="r_ae1366010110318f0f429f912b5372cbf"></a>

```c
#define PIN_P7_6__LPSPI_SCLK_A ALIF_PINMUX(7, 6, 5)
```

相关声明：[PIN_P7_6__LPSPI_SCLK_A](#ae1366010110318f0f429f912b5372cbf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPSPI_SCLK_A`。

<a id="r_aede5f0616ee5550e1865a79632851405"></a>

```c
#define PIN_P7_6__I3C_SDA_D ALIF_PINMUX(7, 6, 6)
```

相关声明：[PIN_P7_6__I3C_SDA_D](#aede5f0616ee5550e1865a79632851405)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`I3C_SDA_D`。

<a id="r_af25f44d0c6c3a9ffc6277d47de0faf20"></a>

```c
#define PIN_P7_6__UT11_T0_B ALIF_PINMUX(7, 6, 7)
```

相关声明：[PIN_P7_6__UT11_T0_B](#af25f44d0c6c3a9ffc6277d47de0faf20)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`UT11_T0_B`。

<a id="r_ae3abc19efe0b06fc7f3dc73c1eb040c7"></a>

```c
#define PIN_P7_7__GPIO ALIF_PINMUX(7, 7, 0)
```

相关声明：[PIN_P7_7__GPIO](#ae3abc19efe0b06fc7f3dc73c1eb040c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.7` 的复用功能（Alternate Functions）。

<a id="r_a2aced875528e0e6570a05f0b8aa9a8f4"></a>

```c
#define PIN_P7_7__LPI2C1_SCL_C ALIF_PINMUX(7, 7, 1)
```

相关声明：[PIN_P7_7__LPI2C1_SCL_C](#a2aced875528e0e6570a05f0b8aa9a8f4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPI2C1_SCL_C`。

<a id="r_a4a121c7800a2c7bf027101c8e6be0981"></a>

```c
#define PIN_P7_7__LPUART_TX_A ALIF_PINMUX(7, 7, 2)
```

相关声明：[PIN_P7_7__LPUART_TX_A](#a4a121c7800a2c7bf027101c8e6be0981)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPUART_TX_A`。

<a id="r_a51f939dd65c588c9fee6bb08ff1d014c"></a>

```c
#define PIN_P7_7__LPI3C_SCL_B ALIF_PINMUX(7, 7, 3)
```

相关声明：[PIN_P7_7__LPI3C_SCL_B](#a51f939dd65c588c9fee6bb08ff1d014c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPI3C_SCL_B`。

<a id="r_ac9968fc164932e8c44c9211dbfda8c23"></a>

```c
#define PIN_P7_7__LPPDM_D3_A ALIF_PINMUX(7, 7, 4)
```

相关声明：[PIN_P7_7__LPPDM_D3_A](#ac9968fc164932e8c44c9211dbfda8c23)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPPDM_D3_A`。

<a id="r_afb80459bd6c6c944fa257a46ca978070"></a>

```c
#define PIN_P7_7__LPSPI_SS0_A ALIF_PINMUX(7, 7, 5)
```

相关声明：[PIN_P7_7__LPSPI_SS0_A](#afb80459bd6c6c944fa257a46ca978070)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPSPI_SS0_A`。

<a id="r_a6757d24d4e447acbfcb834c22859ea2f"></a>

```c
#define PIN_P7_7__I3C_SCL_D ALIF_PINMUX(7, 7, 6)
```

相关声明：[PIN_P7_7__I3C_SCL_D](#a6757d24d4e447acbfcb834c22859ea2f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`I3C_SCL_D`。

<a id="r_a74bcedf4c0f0de4ef1fdd168e7f5ac07"></a>

```c
#define PIN_P7_7__UT11_T1_B ALIF_PINMUX(7, 7, 7)
```

相关声明：[PIN_P7_7__UT11_T1_B](#a74bcedf4c0f0de4ef1fdd168e7f5ac07)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`UT11_T1_B`。

<a id="define-members-9"></a>

### 端口 8 的引脚定义（Port 8 Pin Definitions）

GPIO 端口（Port）8 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_afae07d2c2c36cf28b58d3025bd312bcd"></a>

```c
#define PIN_P8_0__GPIO ALIF_PINMUX(8, 0, 0)
```

相关声明：[PIN_P8_0__GPIO](#afae07d2c2c36cf28b58d3025bd312bcd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.0` 的复用功能（Alternate Functions）。

<a id="r_ac170e16e07731581b3efa51fd5f5e87b"></a>

```c
#define PIN_P8_0__OSPI1_SCLKN_C ALIF_PINMUX(8, 0, 1)
```

相关声明：[PIN_P8_0__OSPI1_SCLKN_C](#ac170e16e07731581b3efa51fd5f5e87b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`OSPI1_SCLKN_C`。

<a id="r_afd9b154a630faffbb4ed569a1b1728e5"></a>

```c
#define PIN_P8_0__AUDIO_CLK_A ALIF_PINMUX(8, 0, 2)
```

相关声明：[PIN_P8_0__AUDIO_CLK_A](#afd9b154a630faffbb4ed569a1b1728e5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`AUDIO_CLK_A`。

<a id="r_ae7ea63c6f45c50ee3dbe6c4c5fb885b0"></a>

```c
#define PIN_P8_0__FAULT0_B ALIF_PINMUX(8, 0, 3)
```

相关声明：[PIN_P8_0__FAULT0_B](#ae7ea63c6f45c50ee3dbe6c4c5fb885b0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`FAULT0_B`。

<a id="r_a2cd736bf19d6192bf3e3c3f5d32af663"></a>

```c
#define PIN_P8_0__LPCAM_D0_A ALIF_PINMUX(8, 0, 4)
```

相关声明：[PIN_P8_0__LPCAM_D0_A](#a2cd736bf19d6192bf3e3c3f5d32af663)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="r_a985d8090a059e89d8f08cca3ced6b4ee"></a>

```c
#define PIN_P8_0__SD_D0_C ALIF_PINMUX(8, 0, 5)
```

相关声明：[PIN_P8_0__SD_D0_C](#a985d8090a059e89d8f08cca3ced6b4ee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`SD_D0_C`。

<a id="r_afe19a4d1634357b733f1256f1af834d8"></a>

```c
#define PIN_P8_0__CDC_D0_A ALIF_PINMUX(8, 0, 6)
```

相关声明：[PIN_P8_0__CDC_D0_A](#afe19a4d1634357b733f1256f1af834d8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`CDC_D0_A`。

<a id="r_a46242fe0b6bef22903ee8521cc2f7114"></a>

```c
#define PIN_P8_0__CAM_D0_B ALIF_PINMUX(8, 0, 7)
```

相关声明：[PIN_P8_0__CAM_D0_B](#a46242fe0b6bef22903ee8521cc2f7114)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`CAM_D0_B`。

<a id="r_ab7545d1438381ff91c47907abe36bde2"></a>

```c
#define PIN_P8_1__GPIO ALIF_PINMUX(8, 1, 0)
```

相关声明：[PIN_P8_1__GPIO](#ab7545d1438381ff91c47907abe36bde2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.1` 的复用功能（Alternate Functions）。

<a id="r_aed14311308ba4434e797d9755927571c"></a>

```c
#define PIN_P8_1__I2S2_SDI_A ALIF_PINMUX(8, 1, 1)
```

相关声明：[PIN_P8_1__I2S2_SDI_A](#aed14311308ba4434e797d9755927571c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`I2S2_SDI_A`。

<a id="r_ade34846e1cde4f9d437200205354fc49"></a>

```c
#define PIN_P8_1__FAULT1_B ALIF_PINMUX(8, 1, 2)
```

相关声明：[PIN_P8_1__FAULT1_B](#ade34846e1cde4f9d437200205354fc49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`FAULT1_B`。

<a id="r_a8619f56c0d93c514ae9e3087e3658d57"></a>

```c
#define PIN_P8_1__LPCAM_D1_A ALIF_PINMUX(8, 1, 3)
```

相关声明：[PIN_P8_1__LPCAM_D1_A](#a8619f56c0d93c514ae9e3087e3658d57)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="r_a270654843e3737dde6343aeb430381aa"></a>

```c
#define PIN_P8_1__SD_D1_C ALIF_PINMUX(8, 1, 4)
```

相关声明：[PIN_P8_1__SD_D1_C](#a270654843e3737dde6343aeb430381aa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`SD_D1_C`。

<a id="r_ad7959cb731c45e0fdbdaa316ce9b46b3"></a>

```c
#define PIN_P8_1__CDC_D1_A ALIF_PINMUX(8, 1, 5)
```

相关声明：[PIN_P8_1__CDC_D1_A](#ad7959cb731c45e0fdbdaa316ce9b46b3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`CDC_D1_A`。

<a id="r_a3b536ef4e1eb1a398f4b5fca65268578"></a>

```c
#define PIN_P8_1__CAM_D1_B ALIF_PINMUX(8, 1, 6)
```

相关声明：[PIN_P8_1__CAM_D1_B](#a3b536ef4e1eb1a398f4b5fca65268578)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`CAM_D1_B`。

<a id="r_ab945bad6f40aeb586d3bedd041cddc8e"></a>

```c
#define PIN_P8_1__OSPI1_SS1_C ALIF_PINMUX(8, 1, 7)
```

相关声明：[PIN_P8_1__OSPI1_SS1_C](#ab945bad6f40aeb586d3bedd041cddc8e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`OSPI1_SS1_C`。

<a id="r_a60cd1313b5dbd2f3e804024add367802"></a>

```c
#define PIN_P8_2__GPIO ALIF_PINMUX(8, 2, 0)
```

相关声明：[PIN_P8_2__GPIO](#a60cd1313b5dbd2f3e804024add367802)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.2` 的复用功能（Alternate Functions）。

<a id="r_a9ea5544fe5b2c4576dd82884e13395df"></a>

```c
#define PIN_P8_2__I2S2_SDO_A ALIF_PINMUX(8, 2, 1)
```

相关声明：[PIN_P8_2__I2S2_SDO_A](#a9ea5544fe5b2c4576dd82884e13395df)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`I2S2_SDO_A`。

<a id="r_a6d412afabb6859b510829773e835fc0d"></a>

```c
#define PIN_P8_2__SPI0_SS3_B ALIF_PINMUX(8, 2, 2)
```

相关声明：[PIN_P8_2__SPI0_SS3_B](#a6d412afabb6859b510829773e835fc0d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`SPI0_SS3_B`。

<a id="r_a150dc67f0f284e49967bd0d01f4ed834"></a>

```c
#define PIN_P8_2__FAULT2_B ALIF_PINMUX(8, 2, 3)
```

相关声明：[PIN_P8_2__FAULT2_B](#a150dc67f0f284e49967bd0d01f4ed834)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`FAULT2_B`。

<a id="r_a3b1ede5fe15c4d88a3bd13dc3ee334d4"></a>

```c
#define PIN_P8_2__LPCAM_D2_A ALIF_PINMUX(8, 2, 4)
```

相关声明：[PIN_P8_2__LPCAM_D2_A](#a3b1ede5fe15c4d88a3bd13dc3ee334d4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="r_aa5d039fdf4e676090df9ff678fd4e519"></a>

```c
#define PIN_P8_2__SD_D2_C ALIF_PINMUX(8, 2, 5)
```

相关声明：[PIN_P8_2__SD_D2_C](#aa5d039fdf4e676090df9ff678fd4e519)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`SD_D2_C`。

<a id="r_a14ec0433913ab0ca33bf7324459fd430"></a>

```c
#define PIN_P8_2__CDC_D2_A ALIF_PINMUX(8, 2, 6)
```

相关声明：[PIN_P8_2__CDC_D2_A](#a14ec0433913ab0ca33bf7324459fd430)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`CDC_D2_A`。

<a id="r_a782d57f5a111a3fc8b226aefc82ade9b"></a>

```c
#define PIN_P8_2__CAM_D2_B ALIF_PINMUX(8, 2, 7)
```

相关声明：[PIN_P8_2__CAM_D2_B](#a782d57f5a111a3fc8b226aefc82ade9b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`CAM_D2_B`。

<a id="r_ada60da6343aec9d7f341d29d6c0f7d6e"></a>

```c
#define PIN_P8_3__GPIO ALIF_PINMUX(8, 3, 0)
```

相关声明：[PIN_P8_3__GPIO](#ada60da6343aec9d7f341d29d6c0f7d6e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.3` 的复用功能（Alternate Functions）。

<a id="r_a7fe15caced34ecf53b4b0fce1872cd5a"></a>

```c
#define PIN_P8_3__I2S2_SCLK_A ALIF_PINMUX(8, 3, 1)
```

相关声明：[PIN_P8_3__I2S2_SCLK_A](#a7fe15caced34ecf53b4b0fce1872cd5a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`I2S2_SCLK_A`。

<a id="r_a1603e457c636619279c6ed35e69a3cf2"></a>

```c
#define PIN_P8_3__SPI1_MISO_B ALIF_PINMUX(8, 3, 2)
```

相关声明：[PIN_P8_3__SPI1_MISO_B](#a1603e457c636619279c6ed35e69a3cf2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`SPI1_MISO_B`。

<a id="r_ace81371f4c2d6ad8f4769ca638c92737"></a>

```c
#define PIN_P8_3__FAULT3_B ALIF_PINMUX(8, 3, 3)
```

相关声明：[PIN_P8_3__FAULT3_B](#ace81371f4c2d6ad8f4769ca638c92737)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`FAULT3_B`。

<a id="r_a2bdc2a068101da6a91f67764fa027a94"></a>

```c
#define PIN_P8_3__LPCAM_D3_A ALIF_PINMUX(8, 3, 4)
```

相关声明：[PIN_P8_3__LPCAM_D3_A](#a2bdc2a068101da6a91f67764fa027a94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`LPCAM_D3_A`。

<a id="r_a1d349e741c7483151b7bb795040ff91f"></a>

```c
#define PIN_P8_3__SD_D3_C ALIF_PINMUX(8, 3, 5)
```

相关声明：[PIN_P8_3__SD_D3_C](#a1d349e741c7483151b7bb795040ff91f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`SD_D3_C`。

<a id="r_a70b935056e53ed2c964488bc1848d876"></a>

```c
#define PIN_P8_3__CDC_D3_A ALIF_PINMUX(8, 3, 6)
```

相关声明：[PIN_P8_3__CDC_D3_A](#a70b935056e53ed2c964488bc1848d876)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`CDC_D3_A`。

<a id="r_af221fa9c7c280f0fc9ca550e58151be0"></a>

```c
#define PIN_P8_3__CAM_D3_B ALIF_PINMUX(8, 3, 7)
```

相关声明：[PIN_P8_3__CAM_D3_B](#af221fa9c7c280f0fc9ca550e58151be0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`CAM_D3_B`。

<a id="r_a077f91c6d32af478832d2f868a03ce92"></a>

```c
#define PIN_P8_4__GPIO ALIF_PINMUX(8, 4, 0)
```

相关声明：[PIN_P8_4__GPIO](#a077f91c6d32af478832d2f868a03ce92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.4` 的复用功能（Alternate Functions）。

<a id="r_ad6ec829cafb61c3ca9f5cde62add27cc"></a>

```c
#define PIN_P8_4__I2S2_WS_A ALIF_PINMUX(8, 4, 1)
```

相关声明：[PIN_P8_4__I2S2_WS_A](#ad6ec829cafb61c3ca9f5cde62add27cc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`I2S2_WS_A`。

<a id="r_a08a61462ce55c049a6e607ca104fad5c"></a>

```c
#define PIN_P8_4__SPI1_MOSI_B ALIF_PINMUX(8, 4, 2)
```

相关声明：[PIN_P8_4__SPI1_MOSI_B](#a08a61462ce55c049a6e607ca104fad5c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`SPI1_MOSI_B`。

<a id="r_a60238f03990fa811ca84e9bd6c607a86"></a>

```c
#define PIN_P8_4__QEC0_X_B ALIF_PINMUX(8, 4, 3)
```

相关声明：[PIN_P8_4__QEC0_X_B](#a60238f03990fa811ca84e9bd6c607a86)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`QEC0_X_B`。

<a id="r_a45eb5a3acd40b9e97f88a179b2e16284"></a>

```c
#define PIN_P8_4__LPCAM_D4_A ALIF_PINMUX(8, 4, 4)
```

相关声明：[PIN_P8_4__LPCAM_D4_A](#a45eb5a3acd40b9e97f88a179b2e16284)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`LPCAM_D4_A`。

<a id="r_a831ed2e8215f6ba12ac665ef3dcfbc4f"></a>

```c
#define PIN_P8_4__SD_D4_C ALIF_PINMUX(8, 4, 5)
```

相关声明：[PIN_P8_4__SD_D4_C](#a831ed2e8215f6ba12ac665ef3dcfbc4f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`SD_D4_C`。

<a id="r_ab79b6cd1f13c929a09782df627f4f41a"></a>

```c
#define PIN_P8_4__CDC_D4_A ALIF_PINMUX(8, 4, 6)
```

相关声明：[PIN_P8_4__CDC_D4_A](#ab79b6cd1f13c929a09782df627f4f41a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`CDC_D4_A`。

<a id="r_a7a3f80febc5c72fd959aea6d11fc6868"></a>

```c
#define PIN_P8_4__CAM_D4_B ALIF_PINMUX(8, 4, 7)
```

相关声明：[PIN_P8_4__CAM_D4_B](#a7a3f80febc5c72fd959aea6d11fc6868)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`CAM_D4_B`。

<a id="r_a3d1dbbf65ec7141c08cbdf70186faa0a"></a>

```c
#define PIN_P8_5__GPIO ALIF_PINMUX(8, 5, 0)
```

相关声明：[PIN_P8_5__GPIO](#a3d1dbbf65ec7141c08cbdf70186faa0a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.5` 的复用功能（Alternate Functions）。

<a id="r_a5aaf1e1d094132d176d5b5b706168240"></a>

```c
#define PIN_P8_5__OSPI0_RXDS1_A ALIF_PINMUX(8, 5, 1)
```

相关声明：[PIN_P8_5__OSPI0_RXDS1_A](#a5aaf1e1d094132d176d5b5b706168240)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`OSPI0_RXDS1_A`。

<a id="r_a01fa8957cb94ee6e829a876fb0af631f"></a>

```c
#define PIN_P8_5__SPI1_SCLK_B ALIF_PINMUX(8, 5, 2)
```

相关声明：[PIN_P8_5__SPI1_SCLK_B](#a01fa8957cb94ee6e829a876fb0af631f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`SPI1_SCLK_B`。

<a id="r_a5a1f1e7e28cfc2e35f2acd079226872c"></a>

```c
#define PIN_P8_5__QEC0_Y_B ALIF_PINMUX(8, 5, 3)
```

相关声明：[PIN_P8_5__QEC0_Y_B](#a5a1f1e7e28cfc2e35f2acd079226872c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`QEC0_Y_B`。

<a id="r_a7ee0f06bc2b5d3ef1f91815d61372987"></a>

```c
#define PIN_P8_5__LPCAM_D5_A ALIF_PINMUX(8, 5, 4)
```

相关声明：[PIN_P8_5__LPCAM_D5_A](#a7ee0f06bc2b5d3ef1f91815d61372987)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`LPCAM_D5_A`。

<a id="r_acc5f05b73b0370106e7ffc49e4bff2c2"></a>

```c
#define PIN_P8_5__SD_D5_C ALIF_PINMUX(8, 5, 5)
```

相关声明：[PIN_P8_5__SD_D5_C](#acc5f05b73b0370106e7ffc49e4bff2c2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`SD_D5_C`。

<a id="r_a9b890e71e9480f5d6f15abaf29b984a0"></a>

```c
#define PIN_P8_5__CDC_D5_A ALIF_PINMUX(8, 5, 6)
```

相关声明：[PIN_P8_5__CDC_D5_A](#a9b890e71e9480f5d6f15abaf29b984a0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`CDC_D5_A`。

<a id="r_a0eda6c75336d02a21d83e14ffa02275c"></a>

```c
#define PIN_P8_5__CAM_D5_B ALIF_PINMUX(8, 5, 7)
```

相关声明：[PIN_P8_5__CAM_D5_B](#a0eda6c75336d02a21d83e14ffa02275c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`CAM_D5_B`。

<a id="r_aac04079cc075adb9c60dc629fb9e544e"></a>

```c
#define PIN_P8_6__GPIO ALIF_PINMUX(8, 6, 0)
```

相关声明：[PIN_P8_6__GPIO](#aac04079cc075adb9c60dc629fb9e544e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.6` 的复用功能（Alternate Functions）。

<a id="r_af28764146f32632aa6c0a740defff893"></a>

```c
#define PIN_P8_6__OSPI1_RXDS1_B ALIF_PINMUX(8, 6, 1)
```

相关声明：[PIN_P8_6__OSPI1_RXDS1_B](#af28764146f32632aa6c0a740defff893)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`OSPI1_RXDS1_B`。

<a id="r_aa0dcf82c495888b3589f6233ee96a9ea"></a>

```c
#define PIN_P8_6__I2S3_SCLK_B ALIF_PINMUX(8, 6, 2)
```

相关声明：[PIN_P8_6__I2S3_SCLK_B](#aa0dcf82c495888b3589f6233ee96a9ea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`I2S3_SCLK_B`。

<a id="r_a942f076af1c013b2d500cdd85bbbd7a2"></a>

```c
#define PIN_P8_6__QEC0_Z_B ALIF_PINMUX(8, 6, 3)
```

相关声明：[PIN_P8_6__QEC0_Z_B](#a942f076af1c013b2d500cdd85bbbd7a2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`QEC0_Z_B`。

<a id="r_afe04f9d7665f3818e7f66b567a69f10e"></a>

```c
#define PIN_P8_6__LPCAM_D6_A ALIF_PINMUX(8, 6, 4)
```

相关声明：[PIN_P8_6__LPCAM_D6_A](#afe04f9d7665f3818e7f66b567a69f10e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`LPCAM_D6_A`。

<a id="r_aae6cb48371c69ec68657716554d99f5a"></a>

```c
#define PIN_P8_6__SD_D6_C ALIF_PINMUX(8, 6, 5)
```

相关声明：[PIN_P8_6__SD_D6_C](#aae6cb48371c69ec68657716554d99f5a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`SD_D6_C`。

<a id="r_a4601228b6c06379cf97f14a93ea46a7c"></a>

```c
#define PIN_P8_6__CDC_D6_A ALIF_PINMUX(8, 6, 6)
```

相关声明：[PIN_P8_6__CDC_D6_A](#a4601228b6c06379cf97f14a93ea46a7c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`CDC_D6_A`。

<a id="r_a505e16163e7d4506f77d5efef0bd4091"></a>

```c
#define PIN_P8_6__CAM_D6_B ALIF_PINMUX(8, 6, 7)
```

相关声明：[PIN_P8_6__CAM_D6_B](#a505e16163e7d4506f77d5efef0bd4091)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`CAM_D6_B`。

<a id="r_adeed03c5ceab2806bff7df654f45982d"></a>

```c
#define PIN_P8_7__GPIO ALIF_PINMUX(8, 7, 0)
```

相关声明：[PIN_P8_7__GPIO](#adeed03c5ceab2806bff7df654f45982d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.7` 的复用功能（Alternate Functions）。

<a id="r_a3a15a5d9c88f736f38a9054133847e18"></a>

```c
#define PIN_P8_7__OSPI0_RXDS1_C ALIF_PINMUX(8, 7, 1)
```

相关声明：[PIN_P8_7__OSPI0_RXDS1_C](#a3a15a5d9c88f736f38a9054133847e18)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`OSPI0_RXDS1_C`。

<a id="r_a4f4921bd231e42c104f884b50019a779"></a>

```c
#define PIN_P8_7__I2S3_WS_B ALIF_PINMUX(8, 7, 2)
```

相关声明：[PIN_P8_7__I2S3_WS_B](#a4f4921bd231e42c104f884b50019a779)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`I2S3_WS_B`。

<a id="r_a662c47d7f293a00715e2d94948bcba17"></a>

```c
#define PIN_P8_7__QEC1_X_B ALIF_PINMUX(8, 7, 3)
```

相关声明：[PIN_P8_7__QEC1_X_B](#a662c47d7f293a00715e2d94948bcba17)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`QEC1_X_B`。

<a id="r_ad78a16e7892b71380e4fef2afc9bcc78"></a>

```c
#define PIN_P8_7__LPCAM_D7_A ALIF_PINMUX(8, 7, 4)
```

相关声明：[PIN_P8_7__LPCAM_D7_A](#ad78a16e7892b71380e4fef2afc9bcc78)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`LPCAM_D7_A`。

<a id="r_ab02bc30a86ad95d16bf0c51e5d90f133"></a>

```c
#define PIN_P8_7__SD_D7_C ALIF_PINMUX(8, 7, 5)
```

相关声明：[PIN_P8_7__SD_D7_C](#ab02bc30a86ad95d16bf0c51e5d90f133)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`SD_D7_C`。

<a id="r_a1275cdc5c8fbd8d744c38e5ad16b3d83"></a>

```c
#define PIN_P8_7__CDC_D7_A ALIF_PINMUX(8, 7, 6)
```

相关声明：[PIN_P8_7__CDC_D7_A](#a1275cdc5c8fbd8d744c38e5ad16b3d83)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`CDC_D7_A`。

<a id="r_a5d417264ffe4cba745f1db5b9416bc26"></a>

```c
#define PIN_P8_7__CAM_D7_B ALIF_PINMUX(8, 7, 7)
```

相关声明：[PIN_P8_7__CAM_D7_B](#a5d417264ffe4cba745f1db5b9416bc26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`CAM_D7_B`。

<a id="define-members-10"></a>

### 端口 9 的引脚定义（Port 9 Pin Definitions）

GPIO 端口（Port）9 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a6c39dd61a6f51d3877bd1c31274d96d2"></a>

```c
#define PIN_P9_0__GPIO ALIF_PINMUX(9, 0, 0)
```

相关声明：[PIN_P9_0__GPIO](#a6c39dd61a6f51d3877bd1c31274d96d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.0` 的复用功能（Alternate Functions）。

<a id="r_a876adc4eec0f56c60d601b76e71e4e27"></a>

```c
#define PIN_P9_0__OSPI1_RXDS1_C ALIF_PINMUX(9, 0, 1)
```

相关声明：[PIN_P9_0__OSPI1_RXDS1_C](#a876adc4eec0f56c60d601b76e71e4e27)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`OSPI1_RXDS1_C`。

<a id="r_a595fa627a03ebc400663b5dbccba599b"></a>

```c
#define PIN_P9_0__I2S3_SDI_B ALIF_PINMUX(9, 0, 2)
```

相关声明：[PIN_P9_0__I2S3_SDI_B](#a595fa627a03ebc400663b5dbccba599b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`I2S3_SDI_B`。

<a id="r_ab5aefebdeac0bb35f8f5a98b5430b4a5"></a>

```c
#define PIN_P9_0__QEC1_Y_B ALIF_PINMUX(9, 0, 3)
```

相关声明：[PIN_P9_0__QEC1_Y_B](#ab5aefebdeac0bb35f8f5a98b5430b4a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`QEC1_Y_B`。

<a id="r_abce9d55757744ded12d9044b3bc62967"></a>

```c
#define PIN_P9_0__SD_CMD_C ALIF_PINMUX(9, 0, 4)
```

相关声明：[PIN_P9_0__SD_CMD_C](#abce9d55757744ded12d9044b3bc62967)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`SD_CMD_C`。

<a id="r_a509eb405b8f384e617d11de1852866f9"></a>

```c
#define PIN_P9_0__CDC_D8_A ALIF_PINMUX(9, 0, 5)
```

相关声明：[PIN_P9_0__CDC_D8_A](#a509eb405b8f384e617d11de1852866f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`CDC_D8_A`。

<a id="r_aea987334f62371b27ec6bb42168ff87f"></a>

```c
#define PIN_P9_0__CAM_D8_B ALIF_PINMUX(9, 0, 6)
```

相关声明：[PIN_P9_0__CAM_D8_B](#aea987334f62371b27ec6bb42168ff87f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`CAM_D8_B`。

<a id="r_aed687e7b6d3de8b66abb80a6f30dc7ee"></a>

```c
#define PIN_P9_0__LPSPI_SS3_A ALIF_PINMUX(9, 0, 7)
```

相关声明：[PIN_P9_0__LPSPI_SS3_A](#aed687e7b6d3de8b66abb80a6f30dc7ee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）0：`LPSPI_SS3_A`。

<a id="r_aab6b8b8f040a3f5afe7fbd03d3853b7a"></a>

```c
#define PIN_P9_1__GPIO ALIF_PINMUX(9, 1, 0)
```

相关声明：[PIN_P9_1__GPIO](#aab6b8b8f040a3f5afe7fbd03d3853b7a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.1` 的复用功能（Alternate Functions）。

<a id="r_a859e9d9dd96e1662c274caf7d12cfda6"></a>

```c
#define PIN_P9_1__LPUART_RX_B ALIF_PINMUX(9, 1, 1)
```

相关声明：[PIN_P9_1__LPUART_RX_B](#a859e9d9dd96e1662c274caf7d12cfda6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`LPUART_RX_B`。

<a id="r_a468c77663dba4ffebd41e72ec28ce6b6"></a>

```c
#define PIN_P9_1__I2S3_SDO_B ALIF_PINMUX(9, 1, 2)
```

相关声明：[PIN_P9_1__I2S3_SDO_B](#a468c77663dba4ffebd41e72ec28ce6b6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`I2S3_SDO_B`。

<a id="r_a36e98da75fa758bac27102d2f2d0ab05"></a>

```c
#define PIN_P9_1__QEC1_Z_B ALIF_PINMUX(9, 1, 3)
```

相关声明：[PIN_P9_1__QEC1_Z_B](#a36e98da75fa758bac27102d2f2d0ab05)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`QEC1_Z_B`。

<a id="r_a0c5ce6459107866e3498303ea38afe09"></a>

```c
#define PIN_P9_1__SD_CLK_C ALIF_PINMUX(9, 1, 4)
```

相关声明：[PIN_P9_1__SD_CLK_C](#a0c5ce6459107866e3498303ea38afe09)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`SD_CLK_C`。

<a id="r_aef6e841520a75a2a61a2783e5aaa1147"></a>

```c
#define PIN_P9_1__CDC_D9_A ALIF_PINMUX(9, 1, 5)
```

相关声明：[PIN_P9_1__CDC_D9_A](#aef6e841520a75a2a61a2783e5aaa1147)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`CDC_D9_A`。

<a id="r_ab99d67b8e8b6c7a3f279dc999eb1f045"></a>

```c
#define PIN_P9_1__CAM_D9_B ALIF_PINMUX(9, 1, 6)
```

相关声明：[PIN_P9_1__CAM_D9_B](#ab99d67b8e8b6c7a3f279dc999eb1f045)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`CAM_D9_B`。

<a id="r_acd54d522aeb121ff465149fa6c3a123c"></a>

```c
#define PIN_P9_1__LPSPI_SS4_A ALIF_PINMUX(9, 1, 7)
```

相关声明：[PIN_P9_1__LPSPI_SS4_A](#acd54d522aeb121ff465149fa6c3a123c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）1：`LPSPI_SS4_A`。

<a id="r_a0049a6c751eb2db4593b4d7e3e830932"></a>

```c
#define PIN_P9_2__GPIO ALIF_PINMUX(9, 2, 0)
```

相关声明：[PIN_P9_2__GPIO](#a0049a6c751eb2db4593b4d7e3e830932)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.2` 的复用功能（Alternate Functions）。

<a id="r_a2354961e2101a008a5a00ded07bae5f4"></a>

```c
#define PIN_P9_2__LPUART_TX_B ALIF_PINMUX(9, 2, 1)
```

相关声明：[PIN_P9_2__LPUART_TX_B](#a2354961e2101a008a5a00ded07bae5f4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`LPUART_TX_B`。

<a id="r_af249d8b7910f0eb2232b8b1f11ad81ab"></a>

```c
#define PIN_P9_2__I2S3_SDI_A ALIF_PINMUX(9, 2, 2)
```

相关声明：[PIN_P9_2__I2S3_SDI_A](#af249d8b7910f0eb2232b8b1f11ad81ab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`I2S3_SDI_A`。

<a id="r_ac59323909944702a56f068e8583781be"></a>

```c
#define PIN_P9_2__SPI2_MISO_B ALIF_PINMUX(9, 2, 3)
```

相关声明：[PIN_P9_2__SPI2_MISO_B](#ac59323909944702a56f068e8583781be)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`SPI2_MISO_B`。

<a id="r_a3c759baab9b5d753382b5630724786e8"></a>

```c
#define PIN_P9_2__QEC2_X_B ALIF_PINMUX(9, 2, 4)
```

相关声明：[PIN_P9_2__QEC2_X_B](#a3c759baab9b5d753382b5630724786e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`QEC2_X_B`。

<a id="r_acd7551ce812d7813b846ed6e2366157e"></a>

```c
#define PIN_P9_2__SD_RST_C ALIF_PINMUX(9, 2, 5)
```

相关声明：[PIN_P9_2__SD_RST_C](#acd7551ce812d7813b846ed6e2366157e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`SD_RST_C`。

<a id="r_a42a94c1c7e34d8f7e709c86d594b62b0"></a>

```c
#define PIN_P9_2__CDC_D10_A ALIF_PINMUX(9, 2, 6)
```

相关声明：[PIN_P9_2__CDC_D10_A](#a42a94c1c7e34d8f7e709c86d594b62b0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`CDC_D10_A`。

<a id="r_a8b454fcb18e8070c814632929bfb9234"></a>

```c
#define PIN_P9_2__CAM_D10_B ALIF_PINMUX(9, 2, 7)
```

相关声明：[PIN_P9_2__CAM_D10_B](#a8b454fcb18e8070c814632929bfb9234)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）2：`CAM_D10_B`。

<a id="r_a6343335b0acb9b74ddb08de62c328033"></a>

```c
#define PIN_P9_3__GPIO ALIF_PINMUX(9, 3, 0)
```

相关声明：[PIN_P9_3__GPIO](#a6343335b0acb9b74ddb08de62c328033)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.3` 的复用功能（Alternate Functions）。

<a id="r_a1374eb963d78b099332a18ebd9852d74"></a>

```c
#define PIN_P9_3__HFXO_OUT_B ALIF_PINMUX(9, 3, 1)
```

相关声明：[PIN_P9_3__HFXO_OUT_B](#a1374eb963d78b099332a18ebd9852d74)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`HFXO_OUT_B`。

<a id="r_a76dce03300f4eed2b0e94506295c3afe"></a>

```c
#define PIN_P9_3__UART7_RX_B ALIF_PINMUX(9, 3, 2)
```

相关声明：[PIN_P9_3__UART7_RX_B](#a76dce03300f4eed2b0e94506295c3afe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`UART7_RX_B`。

<a id="r_a20aa8587904237b969887d925da63126"></a>

```c
#define PIN_P9_3__I2S3_SDO_A ALIF_PINMUX(9, 3, 3)
```

相关声明：[PIN_P9_3__I2S3_SDO_A](#a20aa8587904237b969887d925da63126)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`I2S3_SDO_A`。

<a id="r_a33a6f2669041c50a2274db4bcf089664"></a>

```c
#define PIN_P9_3__SPI2_MOSI_B ALIF_PINMUX(9, 3, 4)
```

相关声明：[PIN_P9_3__SPI2_MOSI_B](#a33a6f2669041c50a2274db4bcf089664)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`SPI2_MOSI_B`。

<a id="r_a1739a3d7f0caa394957aa363664b747e"></a>

```c
#define PIN_P9_3__QEC2_Y_B ALIF_PINMUX(9, 3, 5)
```

相关声明：[PIN_P9_3__QEC2_Y_B](#a1739a3d7f0caa394957aa363664b747e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`QEC2_Y_B`。

<a id="r_ac10618ac25d3fa32572beca9747930ea"></a>

```c
#define PIN_P9_3__CDC_D11_A ALIF_PINMUX(9, 3, 6)
```

相关声明：[PIN_P9_3__CDC_D11_A](#ac10618ac25d3fa32572beca9747930ea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`CDC_D11_A`。

<a id="r_a820e7fd4aa0a9db16fb91ad00d8129e4"></a>

```c
#define PIN_P9_3__CAM_D11_B ALIF_PINMUX(9, 3, 7)
```

相关声明：[PIN_P9_3__CAM_D11_B](#a820e7fd4aa0a9db16fb91ad00d8129e4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）3：`CAM_D11_B`。

<a id="r_aceea4881f07d17df9389a9bb2b5687b1"></a>

```c
#define PIN_P9_4__GPIO ALIF_PINMUX(9, 4, 0)
```

相关声明：[PIN_P9_4__GPIO](#aceea4881f07d17df9389a9bb2b5687b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.4` 的复用功能（Alternate Functions）。

<a id="r_a310700b8fee4462929d48f363b88922a"></a>

```c
#define PIN_P9_4__UART7_TX_B ALIF_PINMUX(9, 4, 1)
```

相关声明：[PIN_P9_4__UART7_TX_B](#a310700b8fee4462929d48f363b88922a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`UART7_TX_B`。

<a id="r_aab63b1b5e74ed1b493d64ee065f67ff9"></a>

```c
#define PIN_P9_4__I2S3_SCLK_A ALIF_PINMUX(9, 4, 2)
```

相关声明：[PIN_P9_4__I2S3_SCLK_A](#aab63b1b5e74ed1b493d64ee065f67ff9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`I2S3_SCLK_A`。

<a id="r_acab28fd9dabc6f1ac721b078b6c7208a"></a>

```c
#define PIN_P9_4__SPI2_SCLK_B ALIF_PINMUX(9, 4, 3)
```

相关声明：[PIN_P9_4__SPI2_SCLK_B](#acab28fd9dabc6f1ac721b078b6c7208a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`SPI2_SCLK_B`。

<a id="r_a6013125ed1a4918027ffa0112b5e4dac"></a>

```c
#define PIN_P9_4__I2C3_SDA_C ALIF_PINMUX(9, 4, 4)
```

相关声明：[PIN_P9_4__I2C3_SDA_C](#a6013125ed1a4918027ffa0112b5e4dac)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`I2C3_SDA_C`。

<a id="r_a49adce0d28a3dcb38967895905666e50"></a>

```c
#define PIN_P9_4__QEC2_Z_B ALIF_PINMUX(9, 4, 5)
```

相关声明：[PIN_P9_4__QEC2_Z_B](#a49adce0d28a3dcb38967895905666e50)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`QEC2_Z_B`。

<a id="r_aeb8e8cc88d8e4918aa4e03eb62506002"></a>

```c
#define PIN_P9_4__CDC_D12_A ALIF_PINMUX(9, 4, 6)
```

相关声明：[PIN_P9_4__CDC_D12_A](#aeb8e8cc88d8e4918aa4e03eb62506002)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`CDC_D12_A`。

<a id="r_a30980382d11bab5cee6798d0aeedd6d1"></a>

```c
#define PIN_P9_4__CAM_D12_B ALIF_PINMUX(9, 4, 7)
```

相关声明：[PIN_P9_4__CAM_D12_B](#a30980382d11bab5cee6798d0aeedd6d1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）4：`CAM_D12_B`。

<a id="r_ad2941c38b5b4bd08db9cd7c9e5832ae3"></a>

```c
#define PIN_P9_5__GPIO ALIF_PINMUX(9, 5, 0)
```

相关声明：[PIN_P9_5__GPIO](#ad2941c38b5b4bd08db9cd7c9e5832ae3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.5` 的复用功能（Alternate Functions）。

<a id="r_a5603b3daa4c24a6676468412da316b29"></a>

```c
#define PIN_P9_5__OSPI1_D0_C ALIF_PINMUX(9, 5, 1)
```

相关声明：[PIN_P9_5__OSPI1_D0_C](#a5603b3daa4c24a6676468412da316b29)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`OSPI1_D0_C`。

<a id="r_ac7aca81f38fb5faf22864186816c7680"></a>

```c
#define PIN_P9_5__I2S3_WS_A ALIF_PINMUX(9, 5, 2)
```

相关声明：[PIN_P9_5__I2S3_WS_A](#ac7aca81f38fb5faf22864186816c7680)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`I2S3_WS_A`。

<a id="r_aad885f3710e8a8751f138066dcad8d2d"></a>

```c
#define PIN_P9_5__SPI2_SS0_B ALIF_PINMUX(9, 5, 3)
```

相关声明：[PIN_P9_5__SPI2_SS0_B](#aad885f3710e8a8751f138066dcad8d2d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`SPI2_SS0_B`。

<a id="r_a728309c21e6482c2c6e2b683ef9c15a8"></a>

```c
#define PIN_P9_5__I2C3_SCL_C ALIF_PINMUX(9, 5, 4)
```

相关声明：[PIN_P9_5__I2C3_SCL_C](#a728309c21e6482c2c6e2b683ef9c15a8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`I2C3_SCL_C`。

<a id="r_a15ab6ecc8d267121c684c4cf70255710"></a>

```c
#define PIN_P9_5__QEC3_X_B ALIF_PINMUX(9, 5, 5)
```

相关声明：[PIN_P9_5__QEC3_X_B](#a15ab6ecc8d267121c684c4cf70255710)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`QEC3_X_B`。

<a id="r_ac48cfbf8f1f08bd5a6fd3a8b155b19e8"></a>

```c
#define PIN_P9_5__CDC_D13_A ALIF_PINMUX(9, 5, 6)
```

相关声明：[PIN_P9_5__CDC_D13_A](#ac48cfbf8f1f08bd5a6fd3a8b155b19e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`CDC_D13_A`。

<a id="r_a1f23bf2d9d927de033d8a479449ba284"></a>

```c
#define PIN_P9_5__CAM_D13_B ALIF_PINMUX(9, 5, 7)
```

相关声明：[PIN_P9_5__CAM_D13_B](#a1f23bf2d9d927de033d8a479449ba284)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）5：`CAM_D13_B`。

<a id="r_adebbf408f66abe66612efca4e0d40308"></a>

```c
#define PIN_P9_6__GPIO ALIF_PINMUX(9, 6, 0)
```

相关声明：[PIN_P9_6__GPIO](#adebbf408f66abe66612efca4e0d40308)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.6` 的复用功能（Alternate Functions）。

<a id="r_aa519282029b6903e371928229f1e296d"></a>

```c
#define PIN_P9_6__OSPI1_D1_C ALIF_PINMUX(9, 6, 1)
```

相关声明：[PIN_P9_6__OSPI1_D1_C](#aa519282029b6903e371928229f1e296d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`OSPI1_D1_C`。

<a id="r_a96e81f854bec0687cfc9632a9bd4c9f9"></a>

```c
#define PIN_P9_6__AUDIO_CLK_B ALIF_PINMUX(9, 6, 2)
```

相关声明：[PIN_P9_6__AUDIO_CLK_B](#a96e81f854bec0687cfc9632a9bd4c9f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`AUDIO_CLK_B`。

<a id="r_a9247ba0566dd4266b13a372703b86cc1"></a>

```c
#define PIN_P9_6__SPI2_SS1_B ALIF_PINMUX(9, 6, 3)
```

相关声明：[PIN_P9_6__SPI2_SS1_B](#a9247ba0566dd4266b13a372703b86cc1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`SPI2_SS1_B`。

<a id="r_aba985f9582cb768cba020cb5a937e808"></a>

```c
#define PIN_P9_6__I2C3_SDA_B ALIF_PINMUX(9, 6, 4)
```

相关声明：[PIN_P9_6__I2C3_SDA_B](#aba985f9582cb768cba020cb5a937e808)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`I2C3_SDA_B`。

<a id="r_a2221154ae285caa9f2ffe8381bb8645f"></a>

```c
#define PIN_P9_6__QEC3_Y_B ALIF_PINMUX(9, 6, 5)
```

相关声明：[PIN_P9_6__QEC3_Y_B](#a2221154ae285caa9f2ffe8381bb8645f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`QEC3_Y_B`。

<a id="r_a077fa99bd66774a7dbde71b74867ff14"></a>

```c
#define PIN_P9_6__CDC_D14_A ALIF_PINMUX(9, 6, 6)
```

相关声明：[PIN_P9_6__CDC_D14_A](#a077fa99bd66774a7dbde71b74867ff14)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`CDC_D14_A`。

<a id="r_a77a3725429d3642ef80caf75d9338676"></a>

```c
#define PIN_P9_6__CAM_D14_B ALIF_PINMUX(9, 6, 7)
```

相关声明：[PIN_P9_6__CAM_D14_B](#a77a3725429d3642ef80caf75d9338676)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）6：`CAM_D14_B`。

<a id="r_a76cb3601b18a43915bbeb240086db0c9"></a>

```c
#define PIN_P9_7__GPIO ALIF_PINMUX(9, 7, 0)
```

相关声明：[PIN_P9_7__GPIO](#a76cb3601b18a43915bbeb240086db0c9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P9.7` 的复用功能（Alternate Functions）。

<a id="r_a4b8484edd05564fb0a4688bda8de446f"></a>

```c
#define PIN_P9_7__OSPI1_D2_C ALIF_PINMUX(9, 7, 1)
```

相关声明：[PIN_P9_7__OSPI1_D2_C](#a4b8484edd05564fb0a4688bda8de446f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`OSPI1_D2_C`。

<a id="r_ac7e2363181acbefadb542099a9fb5537"></a>

```c
#define PIN_P9_7__UART7_DE_B ALIF_PINMUX(9, 7, 2)
```

相关声明：[PIN_P9_7__UART7_DE_B](#ac7e2363181acbefadb542099a9fb5537)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`UART7_DE_B`。

<a id="r_a22df37e2123ac9b1a6fb570f84aef07f"></a>

```c
#define PIN_P9_7__SPI2_SS2_B ALIF_PINMUX(9, 7, 3)
```

相关声明：[PIN_P9_7__SPI2_SS2_B](#a22df37e2123ac9b1a6fb570f84aef07f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`SPI2_SS2_B`。

<a id="r_a9fc6d8aba93de436b35c7dcac4c9c09c"></a>

```c
#define PIN_P9_7__I2C3_SCL_B ALIF_PINMUX(9, 7, 4)
```

相关声明：[PIN_P9_7__I2C3_SCL_B](#a9fc6d8aba93de436b35c7dcac4c9c09c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`I2C3_SCL_B`。

<a id="r_ac4e8e4fca41208c4f4ca9f20d3fa40ed"></a>

```c
#define PIN_P9_7__QEC3_Z_B ALIF_PINMUX(9, 7, 5)
```

相关声明：[PIN_P9_7__QEC3_Z_B](#ac4e8e4fca41208c4f4ca9f20d3fa40ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`QEC3_Z_B`。

<a id="r_a246965bab24ee029b2f6306a2220dbb9"></a>

```c
#define PIN_P9_7__CDC_D15_A ALIF_PINMUX(9, 7, 6)
```

相关声明：[PIN_P9_7__CDC_D15_A](#a246965bab24ee029b2f6306a2220dbb9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`CDC_D15_A`。

<a id="r_aabf3438a1cd4b3663259241a7d5109a1"></a>

```c
#define PIN_P9_7__CAM_D15_B ALIF_PINMUX(9, 7, 7)
```

相关声明：[PIN_P9_7__CAM_D15_B](#aabf3438a1cd4b3663259241a7d5109a1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）9 的引脚（Pin）7：`CAM_D15_B`。

<a id="define-members-11"></a>

### 端口 10 的引脚定义（Port 10 Pin Definitions）

GPIO 端口（Port）10 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a0d09d7d90b901160d900bde4fe064fa8"></a>

```c
#define PIN_P10_0__GPIO ALIF_PINMUX(10, 0, 0)
```

相关声明：[PIN_P10_0__GPIO](#a0d09d7d90b901160d900bde4fe064fa8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.0` 的复用功能（Alternate Functions）。

<a id="r_a3734bb4f47ee59a20e21452ccfad232d"></a>

```c
#define PIN_P10_0__OSPI1_D3_C ALIF_PINMUX(10, 0, 1)
```

相关声明：[PIN_P10_0__OSPI1_D3_C](#a3734bb4f47ee59a20e21452ccfad232d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`OSPI1_D3_C`。

<a id="r_ad07d8eb42ddde1260281ea90875d02c7"></a>

```c
#define PIN_P10_0__UART6_DE_B ALIF_PINMUX(10, 0, 2)
```

相关声明：[PIN_P10_0__UART6_DE_B](#ad07d8eb42ddde1260281ea90875d02c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`UART6_DE_B`。

<a id="r_ad8c14f987d490c56a883235a78ae2c09"></a>

```c
#define PIN_P10_0__SPI2_SS3_B ALIF_PINMUX(10, 0, 3)
```

相关声明：[PIN_P10_0__SPI2_SS3_B](#ad8c14f987d490c56a883235a78ae2c09)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`SPI2_SS3_B`。

<a id="r_ac8fe2a408fb2fe327cfe9e47fdb2ca94"></a>

```c
#define PIN_P10_0__UT0_T0_C ALIF_PINMUX(10, 0, 4)
```

相关声明：[PIN_P10_0__UT0_T0_C](#ac8fe2a408fb2fe327cfe9e47fdb2ca94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`UT0_T0_C`。

<a id="r_a524f9ad04babc125a373f406d1a9657b"></a>

```c
#define PIN_P10_0__LPCAM_HSYNC_A ALIF_PINMUX(10, 0, 5)
```

相关声明：[PIN_P10_0__LPCAM_HSYNC_A](#a524f9ad04babc125a373f406d1a9657b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`LPCAM_HSYNC_A`。

<a id="r_a8a9136a6f45bc7048124d084209856a1"></a>

```c
#define PIN_P10_0__CDC_D16_A ALIF_PINMUX(10, 0, 6)
```

相关声明：[PIN_P10_0__CDC_D16_A](#a8a9136a6f45bc7048124d084209856a1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`CDC_D16_A`。

<a id="r_a83bf5da94e1c8c6aaae0a857ad5a01d9"></a>

```c
#define PIN_P10_0__CAM_HSYNC_B ALIF_PINMUX(10, 0, 7)
```

相关声明：[PIN_P10_0__CAM_HSYNC_B](#a83bf5da94e1c8c6aaae0a857ad5a01d9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）0：`CAM_HSYNC_B`。

<a id="r_a06764986a0d6fca85d68e1d50d4bbce7"></a>

```c
#define PIN_P10_1__GPIO ALIF_PINMUX(10, 1, 0)
```

相关声明：[PIN_P10_1__GPIO](#a06764986a0d6fca85d68e1d50d4bbce7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.1` 的复用功能（Alternate Functions）。

<a id="r_a435c2a45aacecce2cf55e883dcf989fd"></a>

```c
#define PIN_P10_1__OSPI1_D4_C ALIF_PINMUX(10, 1, 1)
```

相关声明：[PIN_P10_1__OSPI1_D4_C](#a435c2a45aacecce2cf55e883dcf989fd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`OSPI1_D4_C`。

<a id="r_a30b11b254684b83084315e4dd470d183"></a>

```c
#define PIN_P10_1__HSUART0_RX_A ALIF_PINMUX(10, 1, 2)
```

相关声明：[PIN_P10_1__HSUART0_RX_A](#a30b11b254684b83084315e4dd470d183)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`HSUART0_RX_A`。

<a id="r_add14028df60e7b6c4191fa400d7c46fb"></a>

```c
#define PIN_P10_1__LPI2S_SDI_B ALIF_PINMUX(10, 1, 3)
```

相关声明：[PIN_P10_1__LPI2S_SDI_B](#add14028df60e7b6c4191fa400d7c46fb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`LPI2S_SDI_B`。

<a id="r_abcd471e5e73d4dc91337ee5817fdaee0"></a>

```c
#define PIN_P10_1__UT0_T1_C ALIF_PINMUX(10, 1, 4)
```

相关声明：[PIN_P10_1__UT0_T1_C](#abcd471e5e73d4dc91337ee5817fdaee0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`UT0_T1_C`。

<a id="r_a8d7b7553fd5f6c73212a723b735368e3"></a>

```c
#define PIN_P10_1__LPCAM_VSYNC_A ALIF_PINMUX(10, 1, 5)
```

相关声明：[PIN_P10_1__LPCAM_VSYNC_A](#a8d7b7553fd5f6c73212a723b735368e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`LPCAM_VSYNC_A`。

<a id="r_a643d326ca3a6a5bb8c56c63f1a2f661c"></a>

```c
#define PIN_P10_1__CDC_D17_A ALIF_PINMUX(10, 1, 6)
```

相关声明：[PIN_P10_1__CDC_D17_A](#a643d326ca3a6a5bb8c56c63f1a2f661c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`CDC_D17_A`。

<a id="r_a3588aa90a7de8e8f8d8eb9c272dd72e8"></a>

```c
#define PIN_P10_1__CAM_VSYNC_B ALIF_PINMUX(10, 1, 7)
```

相关声明：[PIN_P10_1__CAM_VSYNC_B](#a3588aa90a7de8e8f8d8eb9c272dd72e8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）1：`CAM_VSYNC_B`。

<a id="r_af38abdfdcd535b66e3a06e67dbce6ad2"></a>

```c
#define PIN_P10_2__GPIO ALIF_PINMUX(10, 2, 0)
```

相关声明：[PIN_P10_2__GPIO](#af38abdfdcd535b66e3a06e67dbce6ad2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.2` 的复用功能（Alternate Functions）。

<a id="r_a570b682d1bb7049f018ade169cc8d283"></a>

```c
#define PIN_P10_2__OSPI1_D5_C ALIF_PINMUX(10, 2, 1)
```

相关声明：[PIN_P10_2__OSPI1_D5_C](#a570b682d1bb7049f018ade169cc8d283)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`OSPI1_D5_C`。

<a id="r_a2e0d49b16b1002113a57edae8c709276"></a>

```c
#define PIN_P10_2__HSUART0_TX_A ALIF_PINMUX(10, 2, 2)
```

相关声明：[PIN_P10_2__HSUART0_TX_A](#a2e0d49b16b1002113a57edae8c709276)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`HSUART0_TX_A`。

<a id="r_a3f39b7debe40524149de804280922136"></a>

```c
#define PIN_P10_2__LPI2S_SDO_B ALIF_PINMUX(10, 2, 3)
```

相关声明：[PIN_P10_2__LPI2S_SDO_B](#a3f39b7debe40524149de804280922136)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`LPI2S_SDO_B`。

<a id="r_a19f3416067803dd83dde7f8015bb6e63"></a>

```c
#define PIN_P10_2__UT1_T0_C ALIF_PINMUX(10, 2, 4)
```

相关声明：[PIN_P10_2__UT1_T0_C](#a19f3416067803dd83dde7f8015bb6e63)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`UT1_T0_C`。

<a id="r_a16f6f6b6c45d33ade034724cc73e512a"></a>

```c
#define PIN_P10_2__LPCAM_PCLK_A ALIF_PINMUX(10, 2, 5)
```

相关声明：[PIN_P10_2__LPCAM_PCLK_A](#a16f6f6b6c45d33ade034724cc73e512a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`LPCAM_PCLK_A`。

<a id="r_a2e8a45e9598437ab30a116f9211df08f"></a>

```c
#define PIN_P10_2__CDC_D18_A ALIF_PINMUX(10, 2, 6)
```

相关声明：[PIN_P10_2__CDC_D18_A](#a2e8a45e9598437ab30a116f9211df08f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`CDC_D18_A`。

<a id="r_a6a44353c221bce09c02874838836e462"></a>

```c
#define PIN_P10_2__CAM_PCLK_B ALIF_PINMUX(10, 2, 7)
```

相关声明：[PIN_P10_2__CAM_PCLK_B](#a6a44353c221bce09c02874838836e462)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）2：`CAM_PCLK_B`。

<a id="r_ae8178ae82b29bbb96a413070911232e4"></a>

```c
#define PIN_P10_3__GPIO ALIF_PINMUX(10, 3, 0)
```

相关声明：[PIN_P10_3__GPIO](#ae8178ae82b29bbb96a413070911232e4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.3` 的复用功能（Alternate Functions）。

<a id="r_a69eee953512b4a0f61e3beedfbcfd111"></a>

```c
#define PIN_P10_3__OSPI1_D6_C ALIF_PINMUX(10, 3, 1)
```

相关声明：[PIN_P10_3__OSPI1_D6_C](#a69eee953512b4a0f61e3beedfbcfd111)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`OSPI1_D6_C`。

<a id="r_a296690843c2f351d976c14ee140e85b4"></a>

```c
#define PIN_P10_3__HSUART1_RX_A ALIF_PINMUX(10, 3, 2)
```

相关声明：[PIN_P10_3__HSUART1_RX_A](#a296690843c2f351d976c14ee140e85b4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`HSUART1_RX_A`。

<a id="r_a44ec4fc6bde183ff499d4bb3dd92c01f"></a>

```c
#define PIN_P10_3__LPI2S_SCLK_B ALIF_PINMUX(10, 3, 3)
```

相关声明：[PIN_P10_3__LPI2S_SCLK_B](#a44ec4fc6bde183ff499d4bb3dd92c01f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`LPI2S_SCLK_B`。

<a id="r_ab2a777e85d7bb6c88e8a01147df3577d"></a>

```c
#define PIN_P10_3__UT1_T1_C ALIF_PINMUX(10, 3, 4)
```

相关声明：[PIN_P10_3__UT1_T1_C](#ab2a777e85d7bb6c88e8a01147df3577d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`UT1_T1_C`。

<a id="r_a03eb3e67619bca555f7fcb517aaff5b9"></a>

```c
#define PIN_P10_3__LPCAM_XVCLK_A ALIF_PINMUX(10, 3, 5)
```

相关声明：[PIN_P10_3__LPCAM_XVCLK_A](#a03eb3e67619bca555f7fcb517aaff5b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`LPCAM_XVCLK_A`。

<a id="r_a772d15bf38887b4c3203eba42cca7767"></a>

```c
#define PIN_P10_3__CDC_D19_A ALIF_PINMUX(10, 3, 6)
```

相关声明：[PIN_P10_3__CDC_D19_A](#a772d15bf38887b4c3203eba42cca7767)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`CDC_D19_A`。

<a id="r_a7cb3915243855dbbf28f7a99881b0376"></a>

```c
#define PIN_P10_3__CAM_XVCLK_B ALIF_PINMUX(10, 3, 7)
```

相关声明：[PIN_P10_3__CAM_XVCLK_B](#a7cb3915243855dbbf28f7a99881b0376)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）3：`CAM_XVCLK_B`。

<a id="r_a824864668a22a50a8bd0d30782d6fd35"></a>

```c
#define PIN_P10_4__GPIO ALIF_PINMUX(10, 4, 0)
```

相关声明：[PIN_P10_4__GPIO](#a824864668a22a50a8bd0d30782d6fd35)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.4` 的复用功能（Alternate Functions）。

<a id="r_a12bed392d874ede18dc9395ca8be773f"></a>

```c
#define PIN_P10_4__OSPI1_D7_C ALIF_PINMUX(10, 4, 1)
```

相关声明：[PIN_P10_4__OSPI1_D7_C](#a12bed392d874ede18dc9395ca8be773f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`OSPI1_D7_C`。

<a id="r_a159ade6a4cde73ad97a2d6abe2d667c4"></a>

```c
#define PIN_P10_4__HSUART1_TX_A ALIF_PINMUX(10, 4, 2)
```

相关声明：[PIN_P10_4__HSUART1_TX_A](#a159ade6a4cde73ad97a2d6abe2d667c4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`HSUART1_TX_A`。

<a id="r_a99776d853de115507e3601e94ee45c8c"></a>

```c
#define PIN_P10_4__LPI2S_WS_B ALIF_PINMUX(10, 4, 3)
```

相关声明：[PIN_P10_4__LPI2S_WS_B](#a99776d853de115507e3601e94ee45c8c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`LPI2S_WS_B`。

<a id="r_ad21a0874594d59bbb0b1c4112cb6b66f"></a>

```c
#define PIN_P10_4__I2C0_SDA_D ALIF_PINMUX(10, 4, 4)
```

相关声明：[PIN_P10_4__I2C0_SDA_D](#ad21a0874594d59bbb0b1c4112cb6b66f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`I2C0_SDA_D`。

<a id="r_aef90d2be77688791ce99e819c7760dd7"></a>

```c
#define PIN_P10_4__UT2_T0_C ALIF_PINMUX(10, 4, 5)
```

相关声明：[PIN_P10_4__UT2_T0_C](#aef90d2be77688791ce99e819c7760dd7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`UT2_T0_C`。

<a id="r_a237b7a24bc9b0d43420ddce0d571677d"></a>

```c
#define PIN_P10_4__ETH_TXD0_B ALIF_PINMUX(10, 4, 6)
```

相关声明：[PIN_P10_4__ETH_TXD0_B](#a237b7a24bc9b0d43420ddce0d571677d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`ETH_TXD0_B`。

<a id="r_aed0e35581bee766b0a41e646fdc95b9c"></a>

```c
#define PIN_P10_4__CDC_D20_A ALIF_PINMUX(10, 4, 7)
```

相关声明：[PIN_P10_4__CDC_D20_A](#aed0e35581bee766b0a41e646fdc95b9c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）4：`CDC_D20_A`。

<a id="r_a95c7cbebacff815700ac996fb8a9e032"></a>

```c
#define PIN_P10_5__GPIO ALIF_PINMUX(10, 5, 0)
```

相关声明：[PIN_P10_5__GPIO](#a95c7cbebacff815700ac996fb8a9e032)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.5` 的复用功能（Alternate Functions）。

<a id="r_a65a373a0f9dbf88278afbc75a8a6a3db"></a>

```c
#define PIN_P10_5__UART6_RX_A ALIF_PINMUX(10, 5, 1)
```

相关声明：[PIN_P10_5__UART6_RX_A](#a65a373a0f9dbf88278afbc75a8a6a3db)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`UART6_RX_A`。

<a id="r_a5ab587662a9897cf75069890773ce9c7"></a>

```c
#define PIN_P10_5__I2S2_SDI_B ALIF_PINMUX(10, 5, 2)
```

相关声明：[PIN_P10_5__I2S2_SDI_B](#a5ab587662a9897cf75069890773ce9c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`I2S2_SDI_B`。

<a id="r_a1c721f6365cb15250855a37579a4924f"></a>

```c
#define PIN_P10_5__SPI3_MISO_B ALIF_PINMUX(10, 5, 3)
```

相关声明：[PIN_P10_5__SPI3_MISO_B](#a1c721f6365cb15250855a37579a4924f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`SPI3_MISO_B`。

<a id="r_aebb5ee312fdff17857bce74fd872c7e3"></a>

```c
#define PIN_P10_5__I2C0_SCL_D ALIF_PINMUX(10, 5, 4)
```

相关声明：[PIN_P10_5__I2C0_SCL_D](#aebb5ee312fdff17857bce74fd872c7e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`I2C0_SCL_D`。

<a id="r_a428f14aa14e085e23508004490c8fa7f"></a>

```c
#define PIN_P10_5__UT2_T1_C ALIF_PINMUX(10, 5, 5)
```

相关声明：[PIN_P10_5__UT2_T1_C](#a428f14aa14e085e23508004490c8fa7f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`UT2_T1_C`。

<a id="r_acf344432c9e6b30a75f455334ded4ebc"></a>

```c
#define PIN_P10_5__ETH_TXD1_B ALIF_PINMUX(10, 5, 6)
```

相关声明：[PIN_P10_5__ETH_TXD1_B](#acf344432c9e6b30a75f455334ded4ebc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`ETH_TXD1_B`。

<a id="r_a87b3e92aeb9b612d7709a24007d4f05c"></a>

```c
#define PIN_P10_5__CDC_D21_A ALIF_PINMUX(10, 5, 7)
```

相关声明：[PIN_P10_5__CDC_D21_A](#a87b3e92aeb9b612d7709a24007d4f05c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）5：`CDC_D21_A`。

<a id="r_a9e78737dc9d1689eb2217db1a12bb927"></a>

```c
#define PIN_P10_6__GPIO ALIF_PINMUX(10, 6, 0)
```

相关声明：[PIN_P10_6__GPIO](#a9e78737dc9d1689eb2217db1a12bb927)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.6` 的复用功能（Alternate Functions）。

<a id="r_aebdac92a16ef4e6011fef1ada8e2648b"></a>

```c
#define PIN_P10_6__UART6_TX_A ALIF_PINMUX(10, 6, 1)
```

相关声明：[PIN_P10_6__UART6_TX_A](#aebdac92a16ef4e6011fef1ada8e2648b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`UART6_TX_A`。

<a id="r_aee6fed8b3cd016c8affc10ed5621c163"></a>

```c
#define PIN_P10_6__I2S2_SDO_B ALIF_PINMUX(10, 6, 2)
```

相关声明：[PIN_P10_6__I2S2_SDO_B](#aee6fed8b3cd016c8affc10ed5621c163)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`I2S2_SDO_B`。

<a id="r_a2d2306dee429751af687499f35eaed5e"></a>

```c
#define PIN_P10_6__SPI3_MOSI_B ALIF_PINMUX(10, 6, 3)
```

相关声明：[PIN_P10_6__SPI3_MOSI_B](#a2d2306dee429751af687499f35eaed5e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`SPI3_MOSI_B`。

<a id="r_a7e64c71976bda3c86a7509dfcb6c1a51"></a>

```c
#define PIN_P10_6__I2C1_SDA_D ALIF_PINMUX(10, 6, 4)
```

相关声明：[PIN_P10_6__I2C1_SDA_D](#a7e64c71976bda3c86a7509dfcb6c1a51)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`I2C1_SDA_D`。

<a id="r_a33e003aa8e4dd4154e09fee58daed7c2"></a>

```c
#define PIN_P10_6__UT3_T0_C ALIF_PINMUX(10, 6, 5)
```

相关声明：[PIN_P10_6__UT3_T0_C](#a33e003aa8e4dd4154e09fee58daed7c2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`UT3_T0_C`。

<a id="r_aaecd255f11e4e5bb4362f975f144c323"></a>

```c
#define PIN_P10_6__ETH_TXEN_B ALIF_PINMUX(10, 6, 6)
```

相关声明：[PIN_P10_6__ETH_TXEN_B](#aaecd255f11e4e5bb4362f975f144c323)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`ETH_TXEN_B`。

<a id="r_a86336c491101c39955e644402c77bb58"></a>

```c
#define PIN_P10_6__CDC_D22_A ALIF_PINMUX(10, 6, 7)
```

相关声明：[PIN_P10_6__CDC_D22_A](#a86336c491101c39955e644402c77bb58)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）6：`CDC_D22_A`。

<a id="r_a646299e814c054ff2cf11e254ddd78d0"></a>

```c
#define PIN_P10_7__GPIO ALIF_PINMUX(10, 7, 0)
```

相关声明：[PIN_P10_7__GPIO](#a646299e814c054ff2cf11e254ddd78d0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P10.7` 的复用功能（Alternate Functions）。

<a id="r_a8181dfa74455316c9fde735d0b3b09e6"></a>

```c
#define PIN_P10_7__UART7_RX_A ALIF_PINMUX(10, 7, 1)
```

相关声明：[PIN_P10_7__UART7_RX_A](#a8181dfa74455316c9fde735d0b3b09e6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`UART7_RX_A`。

<a id="r_a1a3e27ebae94f07b9a60c7c56e706454"></a>

```c
#define PIN_P10_7__I2S2_SCLK_B ALIF_PINMUX(10, 7, 2)
```

相关声明：[PIN_P10_7__I2S2_SCLK_B](#a1a3e27ebae94f07b9a60c7c56e706454)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`I2S2_SCLK_B`。

<a id="r_a2511a1e177bde1bf1d9a6a93d9129d66"></a>

```c
#define PIN_P10_7__SPI3_SCLK_B ALIF_PINMUX(10, 7, 3)
```

相关声明：[PIN_P10_7__SPI3_SCLK_B](#a2511a1e177bde1bf1d9a6a93d9129d66)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`SPI3_SCLK_B`。

<a id="r_a32a7e8261101544dd558ed5aa2ab694d"></a>

```c
#define PIN_P10_7__I2C1_SCL_D ALIF_PINMUX(10, 7, 4)
```

相关声明：[PIN_P10_7__I2C1_SCL_D](#a32a7e8261101544dd558ed5aa2ab694d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`I2C1_SCL_D`。

<a id="r_a941371373e96ad0197810ab5b3b4ccdc"></a>

```c
#define PIN_P10_7__UT3_T1_C ALIF_PINMUX(10, 7, 5)
```

相关声明：[PIN_P10_7__UT3_T1_C](#a941371373e96ad0197810ab5b3b4ccdc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`UT3_T1_C`。

<a id="r_a71b5b5dddd55df63873b364556c82e19"></a>

```c
#define PIN_P10_7__CDC_D23_A ALIF_PINMUX(10, 7, 6)
```

相关声明：[PIN_P10_7__CDC_D23_A](#a71b5b5dddd55df63873b364556c82e19)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`CDC_D23_A`。

<a id="r_a7b0d3a1498c04034496602535623a576"></a>

```c
#define PIN_P10_7__OSPI1_RXDS0_C ALIF_PINMUX(10, 7, 7)
```

相关声明：[PIN_P10_7__OSPI1_RXDS0_C](#a7b0d3a1498c04034496602535623a576)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）10 的引脚（Pin）7：`OSPI1_RXDS0_C`。

<a id="define-members-12"></a>

### 端口 11 的引脚定义（Port 11 Pin Definitions）

GPIO 端口（Port）11 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a6e3ae82413ed22d0b762a03a42b58f07"></a>

```c
#define PIN_P11_0__GPIO ALIF_PINMUX(11, 0, 0)
```

相关声明：[PIN_P11_0__GPIO](#a6e3ae82413ed22d0b762a03a42b58f07)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.0` 的复用功能（Alternate Functions）。

<a id="r_a3857a5aee76d8744f64fa86feaa89d74"></a>

```c
#define PIN_P11_0__OSPI1_D0_A ALIF_PINMUX(11, 0, 1)
```

相关声明：[PIN_P11_0__OSPI1_D0_A](#a3857a5aee76d8744f64fa86feaa89d74)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`OSPI1_D0_A`。

<a id="r_aba1d719c68dd035777d4f3c1c56127fa"></a>

```c
#define PIN_P11_0__UART7_TX_A ALIF_PINMUX(11, 0, 2)
```

相关声明：[PIN_P11_0__UART7_TX_A](#aba1d719c68dd035777d4f3c1c56127fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`UART7_TX_A`。

<a id="r_a02319eba4a567fe789fe6b2474431fa7"></a>

```c
#define PIN_P11_0__I2S2_WS_B ALIF_PINMUX(11, 0, 3)
```

相关声明：[PIN_P11_0__I2S2_WS_B](#a02319eba4a567fe789fe6b2474431fa7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`I2S2_WS_B`。

<a id="r_a527184616eb9dc3476848e6684261ddb"></a>

```c
#define PIN_P11_0__SPI3_SS0_B ALIF_PINMUX(11, 0, 4)
```

相关声明：[PIN_P11_0__SPI3_SS0_B](#a527184616eb9dc3476848e6684261ddb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`SPI3_SS0_B`。

<a id="r_a8b6b125474bfc5ead883dc6137d6721b"></a>

```c
#define PIN_P11_0__UT4_T0_C ALIF_PINMUX(11, 0, 5)
```

相关声明：[PIN_P11_0__UT4_T0_C](#a8b6b125474bfc5ead883dc6137d6721b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`UT4_T0_C`。

<a id="r_aa131fa2180357840aafa8fa03f3ffa76"></a>

```c
#define PIN_P11_0__ETH_REFCLK_B ALIF_PINMUX(11, 0, 6)
```

相关声明：[PIN_P11_0__ETH_REFCLK_B](#aa131fa2180357840aafa8fa03f3ffa76)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`ETH_REFCLK_B`。

<a id="r_adb815f1dd9c2beab4e9ab7f3a5550a34"></a>

```c
#define PIN_P11_0__CDC_D0_B ALIF_PINMUX(11, 0, 7)
```

相关声明：[PIN_P11_0__CDC_D0_B](#adb815f1dd9c2beab4e9ab7f3a5550a34)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）0：`CDC_D0_B`。

<a id="r_a28c06a03d694d015672f85490df35151"></a>

```c
#define PIN_P11_1__GPIO ALIF_PINMUX(11, 1, 0)
```

相关声明：[PIN_P11_1__GPIO](#a28c06a03d694d015672f85490df35151)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.1` 的复用功能（Alternate Functions）。

<a id="r_aac14a399f11b961ddc1efa6854416877"></a>

```c
#define PIN_P11_1__OSPI1_D1_A ALIF_PINMUX(11, 1, 1)
```

相关声明：[PIN_P11_1__OSPI1_D1_A](#aac14a399f11b961ddc1efa6854416877)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`OSPI1_D1_A`。

<a id="r_a21e4ae82b997254ce64ba763d5a0d0ae"></a>

```c
#define PIN_P11_1__UART7_DE_A ALIF_PINMUX(11, 1, 2)
```

相关声明：[PIN_P11_1__UART7_DE_A](#a21e4ae82b997254ce64ba763d5a0d0ae)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`UART7_DE_A`。

<a id="r_ac3b662da6abd1b9dd9603a97e5e0a215"></a>

```c
#define PIN_P11_1__SPI3_SS1_B ALIF_PINMUX(11, 1, 3)
```

相关声明：[PIN_P11_1__SPI3_SS1_B](#ac3b662da6abd1b9dd9603a97e5e0a215)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`SPI3_SS1_B`。

<a id="r_a755b9e846c57bd09ef90b9d4443b37d5"></a>

```c
#define PIN_P11_1__UT4_T1_C ALIF_PINMUX(11, 1, 4)
```

相关声明：[PIN_P11_1__UT4_T1_C](#a755b9e846c57bd09ef90b9d4443b37d5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`UT4_T1_C`。

<a id="r_aafc326843a27fc885ee7f976dc8efe0e"></a>

```c
#define PIN_P11_1__ETH_MDIO_B ALIF_PINMUX(11, 1, 5)
```

相关声明：[PIN_P11_1__ETH_MDIO_B](#aafc326843a27fc885ee7f976dc8efe0e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`ETH_MDIO_B`。

<a id="r_ac55f4a9e0beaf4c0d2b69a2b64261ffd"></a>

```c
#define PIN_P11_1__CDC_D1_B ALIF_PINMUX(11, 1, 6)
```

相关声明：[PIN_P11_1__CDC_D1_B](#ac55f4a9e0beaf4c0d2b69a2b64261ffd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`CDC_D1_B`。

<a id="r_a87648d17a7db98c8f1a8fb66b8012d05"></a>

```c
#define PIN_P11_1__LPSPI_SS5_A ALIF_PINMUX(11, 1, 7)
```

相关声明：[PIN_P11_1__LPSPI_SS5_A](#a87648d17a7db98c8f1a8fb66b8012d05)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）1：`LPSPI_SS5_A`。

<a id="r_a5cd1d6b953e6db042a10b3c9ddc79dfc"></a>

```c
#define PIN_P11_2__GPIO ALIF_PINMUX(11, 2, 0)
```

相关声明：[PIN_P11_2__GPIO](#a5cd1d6b953e6db042a10b3c9ddc79dfc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.2` 的复用功能（Alternate Functions）。

<a id="r_a979e7b6dce5f839f31e2f86be7a584cb"></a>

```c
#define PIN_P11_2__OSPI1_D2_A ALIF_PINMUX(11, 2, 1)
```

相关声明：[PIN_P11_2__OSPI1_D2_A](#a979e7b6dce5f839f31e2f86be7a584cb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`OSPI1_D2_A`。

<a id="r_a22ec216eb854b57591ba815ba2d7430f"></a>

```c
#define PIN_P11_2__UART6_DE_A ALIF_PINMUX(11, 2, 2)
```

相关声明：[PIN_P11_2__UART6_DE_A](#a22ec216eb854b57591ba815ba2d7430f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`UART6_DE_A`。

<a id="r_a34107c3b33af1290cca19c62cded8b20"></a>

```c
#define PIN_P11_2__LPPDM_C2_B ALIF_PINMUX(11, 2, 3)
```

相关声明：[PIN_P11_2__LPPDM_C2_B](#a34107c3b33af1290cca19c62cded8b20)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`LPPDM_C2_B`。

<a id="r_afcddc8c47c7ed27f1cb7806bb119749b"></a>

```c
#define PIN_P11_2__SPI3_SS2_B ALIF_PINMUX(11, 2, 4)
```

相关声明：[PIN_P11_2__SPI3_SS2_B](#afcddc8c47c7ed27f1cb7806bb119749b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`SPI3_SS2_B`。

<a id="r_acd886c4095963d69329fdfa4c05a2312"></a>

```c
#define PIN_P11_2__UT5_T0_C ALIF_PINMUX(11, 2, 5)
```

相关声明：[PIN_P11_2__UT5_T0_C](#acd886c4095963d69329fdfa4c05a2312)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`UT5_T0_C`。

<a id="r_a38f9beb907a0c3987b87ebb72afa8aed"></a>

```c
#define PIN_P11_2__ETH_MDC_B ALIF_PINMUX(11, 2, 6)
```

相关声明：[PIN_P11_2__ETH_MDC_B](#a38f9beb907a0c3987b87ebb72afa8aed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`ETH_MDC_B`。

<a id="r_a31170ed09fdbc65b8a596c2b89cd9484"></a>

```c
#define PIN_P11_2__CDC_D2_B ALIF_PINMUX(11, 2, 7)
```

相关声明：[PIN_P11_2__CDC_D2_B](#a31170ed09fdbc65b8a596c2b89cd9484)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）2：`CDC_D2_B`。

<a id="r_ab0eacf2ec80c89810e5aca5970bd41dd"></a>

```c
#define PIN_P11_3__GPIO ALIF_PINMUX(11, 3, 0)
```

相关声明：[PIN_P11_3__GPIO](#ab0eacf2ec80c89810e5aca5970bd41dd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.3` 的复用功能（Alternate Functions）。

<a id="r_a89fff5dce962cdd009c9d37d51bc7c16"></a>

```c
#define PIN_P11_3__OSPI1_D3_A ALIF_PINMUX(11, 3, 1)
```

相关声明：[PIN_P11_3__OSPI1_D3_A](#a89fff5dce962cdd009c9d37d51bc7c16)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`OSPI1_D3_A`。

<a id="r_ab77ab9d24b65d90edc9d37855f08c6b2"></a>

```c
#define PIN_P11_3__UART5_RX_B ALIF_PINMUX(11, 3, 2)
```

相关声明：[PIN_P11_3__UART5_RX_B](#ab77ab9d24b65d90edc9d37855f08c6b2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`UART5_RX_B`。

<a id="r_a49088562bf7428d75ff8129f274ffd3c"></a>

```c
#define PIN_P11_3__LPPDM_C3_B ALIF_PINMUX(11, 3, 3)
```

相关声明：[PIN_P11_3__LPPDM_C3_B](#a49088562bf7428d75ff8129f274ffd3c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`LPPDM_C3_B`。

<a id="r_a7aabbf5a6929de1e106d1cd2421975e0"></a>

```c
#define PIN_P11_3__SPI3_SS3_B ALIF_PINMUX(11, 3, 4)
```

相关声明：[PIN_P11_3__SPI3_SS3_B](#a7aabbf5a6929de1e106d1cd2421975e0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`SPI3_SS3_B`。

<a id="r_ad980a679ec7803b1c294340c3f0610cf"></a>

```c
#define PIN_P11_3__UT5_T1_C ALIF_PINMUX(11, 3, 5)
```

相关声明：[PIN_P11_3__UT5_T1_C](#ad980a679ec7803b1c294340c3f0610cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`UT5_T1_C`。

<a id="r_a68166c81dbe880d2806d5c2c06825c48"></a>

```c
#define PIN_P11_3__ETH_RXD0_B ALIF_PINMUX(11, 3, 6)
```

相关声明：[PIN_P11_3__ETH_RXD0_B](#a68166c81dbe880d2806d5c2c06825c48)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`ETH_RXD0_B`。

<a id="r_ab192580524bad00ab8d4bf5d10d0785c"></a>

```c
#define PIN_P11_3__CDC_D3_B ALIF_PINMUX(11, 3, 7)
```

相关声明：[PIN_P11_3__CDC_D3_B](#ab192580524bad00ab8d4bf5d10d0785c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）3：`CDC_D3_B`。

<a id="r_a967d01834b4cf01973898c49793d1733"></a>

```c
#define PIN_P11_4__GPIO ALIF_PINMUX(11, 4, 0)
```

相关声明：[PIN_P11_4__GPIO](#a967d01834b4cf01973898c49793d1733)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.4` 的复用功能（Alternate Functions）。

<a id="r_a61082916fa2ad0e66d622769051916f6"></a>

```c
#define PIN_P11_4__OSPI1_D4_A ALIF_PINMUX(11, 4, 1)
```

相关声明：[PIN_P11_4__OSPI1_D4_A](#a61082916fa2ad0e66d622769051916f6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`OSPI1_D4_A`。

<a id="r_adee30b4484c8f089fc9d1b7b47334c94"></a>

```c
#define PIN_P11_4__UART5_TX_B ALIF_PINMUX(11, 4, 2)
```

相关声明：[PIN_P11_4__UART5_TX_B](#adee30b4484c8f089fc9d1b7b47334c94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`UART5_TX_B`。

<a id="r_a0e6d741081c4a1baa037392b63e97d6d"></a>

```c
#define PIN_P11_4__PDM_C2_B ALIF_PINMUX(11, 4, 3)
```

相关声明：[PIN_P11_4__PDM_C2_B](#a0e6d741081c4a1baa037392b63e97d6d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`PDM_C2_B`。

<a id="r_afe9676848a3cd8317303074db663e470"></a>

```c
#define PIN_P11_4__LPSPI_MISO_B ALIF_PINMUX(11, 4, 4)
```

相关声明：[PIN_P11_4__LPSPI_MISO_B](#afe9676848a3cd8317303074db663e470)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`LPSPI_MISO_B`。

<a id="r_a8bb3c00b1e19d9cbde2f81ae5b8c37a5"></a>

```c
#define PIN_P11_4__UT6_T0_C ALIF_PINMUX(11, 4, 5)
```

相关声明：[PIN_P11_4__UT6_T0_C](#a8bb3c00b1e19d9cbde2f81ae5b8c37a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`UT6_T0_C`。

<a id="r_a7af33556f38553a9d080e4cc674dd9ef"></a>

```c
#define PIN_P11_4__ETH_RXD1_B ALIF_PINMUX(11, 4, 6)
```

相关声明：[PIN_P11_4__ETH_RXD1_B](#a7af33556f38553a9d080e4cc674dd9ef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`ETH_RXD1_B`。

<a id="r_a18e9c7e0a390f44e8a26d03cc82b60e0"></a>

```c
#define PIN_P11_4__CDC_D4_B ALIF_PINMUX(11, 4, 7)
```

相关声明：[PIN_P11_4__CDC_D4_B](#a18e9c7e0a390f44e8a26d03cc82b60e0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）4：`CDC_D4_B`。

<a id="r_acbb30ce67fe4cbccf8cd10925545b331"></a>

```c
#define PIN_P11_5__GPIO ALIF_PINMUX(11, 5, 0)
```

相关声明：[PIN_P11_5__GPIO](#acbb30ce67fe4cbccf8cd10925545b331)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.5` 的复用功能（Alternate Functions）。

<a id="r_a28db5ce1c956f30d370b9b49cf85daf2"></a>

```c
#define PIN_P11_5__OSPI1_D5_A ALIF_PINMUX(11, 5, 1)
```

相关声明：[PIN_P11_5__OSPI1_D5_A](#a28db5ce1c956f30d370b9b49cf85daf2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`OSPI1_D5_A`。

<a id="r_ab8c5add28319ad641d59f09b2b38c862"></a>

```c
#define PIN_P11_5__UART6_RX_B ALIF_PINMUX(11, 5, 2)
```

相关声明：[PIN_P11_5__UART6_RX_B](#ab8c5add28319ad641d59f09b2b38c862)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`UART6_RX_B`。

<a id="r_aee7f163a9651eb6623eb80185c2426ca"></a>

```c
#define PIN_P11_5__PDM_C3_B ALIF_PINMUX(11, 5, 3)
```

相关声明：[PIN_P11_5__PDM_C3_B](#aee7f163a9651eb6623eb80185c2426ca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`PDM_C3_B`。

<a id="r_a16f8c46779f6a257c34af69735254b6c"></a>

```c
#define PIN_P11_5__LPSPI_MOSI_B ALIF_PINMUX(11, 5, 4)
```

相关声明：[PIN_P11_5__LPSPI_MOSI_B](#a16f8c46779f6a257c34af69735254b6c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`LPSPI_MOSI_B`。

<a id="r_ae01c8f68dc1a4a9e0444eac296b91766"></a>

```c
#define PIN_P11_5__UT6_T1_C ALIF_PINMUX(11, 5, 5)
```

相关声明：[PIN_P11_5__UT6_T1_C](#ae01c8f68dc1a4a9e0444eac296b91766)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`UT6_T1_C`。

<a id="r_a4e133a5eab6a2d2dd76e444b1b6a64e5"></a>

```c
#define PIN_P11_5__ETH_CRS_DV_B ALIF_PINMUX(11, 5, 6)
```

相关声明：[PIN_P11_5__ETH_CRS_DV_B](#a4e133a5eab6a2d2dd76e444b1b6a64e5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`ETH_CRS_DV_B`。

<a id="r_a8c42f7452eb11f2b4c8bb538485ef5b1"></a>

```c
#define PIN_P11_5__CDC_D5_B ALIF_PINMUX(11, 5, 7)
```

相关声明：[PIN_P11_5__CDC_D5_B](#a8c42f7452eb11f2b4c8bb538485ef5b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）5：`CDC_D5_B`。

<a id="r_ab6efcf118d6d87b5bbe36989673b03cb"></a>

```c
#define PIN_P11_6__GPIO ALIF_PINMUX(11, 6, 0)
```

相关声明：[PIN_P11_6__GPIO](#ab6efcf118d6d87b5bbe36989673b03cb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.6` 的复用功能（Alternate Functions）。

<a id="r_adc272402fc3155d4ec2d1e90a001e2aa"></a>

```c
#define PIN_P11_6__OSPI1_D6_A ALIF_PINMUX(11, 6, 1)
```

相关声明：[PIN_P11_6__OSPI1_D6_A](#adc272402fc3155d4ec2d1e90a001e2aa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`OSPI1_D6_A`。

<a id="r_a51435c722389d9fe457a1bc456a2f464"></a>

```c
#define PIN_P11_6__UART6_TX_B ALIF_PINMUX(11, 6, 2)
```

相关声明：[PIN_P11_6__UART6_TX_B](#a51435c722389d9fe457a1bc456a2f464)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`UART6_TX_B`。

<a id="r_acfb92bfddbce7875829a9faecbb561e3"></a>

```c
#define PIN_P11_6__LPPDM_D2_B ALIF_PINMUX(11, 6, 3)
```

相关声明：[PIN_P11_6__LPPDM_D2_B](#acfb92bfddbce7875829a9faecbb561e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`LPPDM_D2_B`。

<a id="r_a65e21d4d8f03542db85c921ae7b3563d"></a>

```c
#define PIN_P11_6__LPSPI_SCLK_B ALIF_PINMUX(11, 6, 4)
```

相关声明：[PIN_P11_6__LPSPI_SCLK_B](#a65e21d4d8f03542db85c921ae7b3563d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`LPSPI_SCLK_B`。

<a id="r_a45bcd40c046279256ea6726b26b1f517"></a>

```c
#define PIN_P11_6__UT7_T0_C ALIF_PINMUX(11, 6, 5)
```

相关声明：[PIN_P11_6__UT7_T0_C](#a45bcd40c046279256ea6726b26b1f517)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`UT7_T0_C`。

<a id="r_a84c7faae457bbaf10d69c67c3ceae9ab"></a>

```c
#define PIN_P11_6__ETH_RST_B ALIF_PINMUX(11, 6, 6)
```

相关声明：[PIN_P11_6__ETH_RST_B](#a84c7faae457bbaf10d69c67c3ceae9ab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`ETH_RST_B`。

<a id="r_af7f16b9c0ea55fd1344c40bd660c08ff"></a>

```c
#define PIN_P11_6__CDC_D6_B ALIF_PINMUX(11, 6, 7)
```

相关声明：[PIN_P11_6__CDC_D6_B](#af7f16b9c0ea55fd1344c40bd660c08ff)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）6：`CDC_D6_B`。

<a id="r_ac6bdb71edb24a330dda2258195b07fb8"></a>

```c
#define PIN_P11_7__GPIO ALIF_PINMUX(11, 7, 0)
```

相关声明：[PIN_P11_7__GPIO](#ac6bdb71edb24a330dda2258195b07fb8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P11.7` 的复用功能（Alternate Functions）。

<a id="r_a3203e514c7579f68bd0e6bbb34b385f3"></a>

```c
#define PIN_P11_7__OSPI1_D7_A ALIF_PINMUX(11, 7, 1)
```

相关声明：[PIN_P11_7__OSPI1_D7_A](#a3203e514c7579f68bd0e6bbb34b385f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`OSPI1_D7_A`。

<a id="r_a92bd8c9cc4a26f5f3466eef2983335e2"></a>

```c
#define PIN_P11_7__UART5_DE_B ALIF_PINMUX(11, 7, 2)
```

相关声明：[PIN_P11_7__UART5_DE_B](#a92bd8c9cc4a26f5f3466eef2983335e2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`UART5_DE_B`。

<a id="r_a90bc9c9e0ced226e158826241a2efb1a"></a>

```c
#define PIN_P11_7__LPPDM_D3_B ALIF_PINMUX(11, 7, 3)
```

相关声明：[PIN_P11_7__LPPDM_D3_B](#a90bc9c9e0ced226e158826241a2efb1a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`LPPDM_D3_B`。

<a id="r_af59e97786bf73aded8d830a37b48230c"></a>

```c
#define PIN_P11_7__LPSPI_SS_B ALIF_PINMUX(11, 7, 4)
```

相关声明：[PIN_P11_7__LPSPI_SS_B](#af59e97786bf73aded8d830a37b48230c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`LPSPI_SS_B`。

<a id="r_aabdb02e3be3ad1699860ab1fe53793b9"></a>

```c
#define PIN_P11_7__UT7_T1_C ALIF_PINMUX(11, 7, 5)
```

相关声明：[PIN_P11_7__UT7_T1_C](#aabdb02e3be3ad1699860ab1fe53793b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`UT7_T1_C`。

<a id="r_a5f5319f8ed8cbab82055c3e8532781e1"></a>

```c
#define PIN_P11_7__ETH_IRQ_B ALIF_PINMUX(11, 7, 6)
```

相关声明：[PIN_P11_7__ETH_IRQ_B](#a5f5319f8ed8cbab82055c3e8532781e1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`ETH_IRQ_B`。

<a id="r_a05d9d53114570005812f0d834b1d03db"></a>

```c
#define PIN_P11_7__CDC_D7_B ALIF_PINMUX(11, 7, 7)
```

相关声明：[PIN_P11_7__CDC_D7_B](#a05d9d53114570005812f0d834b1d03db)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）11 的引脚（Pin）7：`CDC_D7_B`。

<a id="define-members-13"></a>

### 端口 12 的引脚定义（Port 12 Pin Definitions）

GPIO 端口（Port）12 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a65f9bbfcb57ddd6d11d0ec2d070c5883"></a>

```c
#define PIN_P12_0__GPIO ALIF_PINMUX(12, 0, 0)
```

相关声明：[PIN_P12_0__GPIO](#a65f9bbfcb57ddd6d11d0ec2d070c5883)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.0` 的复用功能（Alternate Functions）。

<a id="r_a28ee98d3dca437831995987eec236128"></a>

```c
#define PIN_P12_0__OSPI0_SCLK_C ALIF_PINMUX(12, 0, 1)
```

相关声明：[PIN_P12_0__OSPI0_SCLK_C](#a28ee98d3dca437831995987eec236128)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`OSPI0_SCLK_C`。

<a id="r_a26ccc2c035ac447ee3d8d524712a0a38"></a>

```c
#define PIN_P12_0__AUDIO_CLK_C ALIF_PINMUX(12, 0, 2)
```

相关声明：[PIN_P12_0__AUDIO_CLK_C](#a26ccc2c035ac447ee3d8d524712a0a38)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`AUDIO_CLK_C`。

<a id="r_ac6de26aa62db5a686e7b1ca231455ae2"></a>

```c
#define PIN_P12_0__I2S1_SDI_B ALIF_PINMUX(12, 0, 3)
```

相关声明：[PIN_P12_0__I2S1_SDI_B](#ac6de26aa62db5a686e7b1ca231455ae2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`I2S1_SDI_B`。

<a id="r_a2649935928ef15fe94aea023c53db7d0"></a>

```c
#define PIN_P12_0__UT8_T0_C ALIF_PINMUX(12, 0, 4)
```

相关声明：[PIN_P12_0__UT8_T0_C](#a2649935928ef15fe94aea023c53db7d0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`UT8_T0_C`。

<a id="r_a3737b779a1becc91e670e4c43ce98517"></a>

```c
#define PIN_P12_0__CDC_D8_B ALIF_PINMUX(12, 0, 5)
```

相关声明：[PIN_P12_0__CDC_D8_B](#a3737b779a1becc91e670e4c43ce98517)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`CDC_D8_B`。

<a id="r_a53cacd2a917dba9f73429243bd7aa4b6"></a>

```c
#define PIN_P12_0__OSPI1_D8_B ALIF_PINMUX(12, 0, 6)
```

相关声明：[PIN_P12_0__OSPI1_D8_B](#a53cacd2a917dba9f73429243bd7aa4b6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`OSPI1_D8_B`。

<a id="r_a7ee571ad8643801e9cb9daa958277eef"></a>

```c
#define PIN_P12_0__LPUT0_T0_B ALIF_PINMUX(12, 0, 7)
```

相关声明：[PIN_P12_0__LPUT0_T0_B](#a7ee571ad8643801e9cb9daa958277eef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）0：`LPUT0_T0_B`。

<a id="r_ace08c69e67060f4a71a24fb30dc509a8"></a>

```c
#define PIN_P12_1__GPIO ALIF_PINMUX(12, 1, 0)
```

相关声明：[PIN_P12_1__GPIO](#ace08c69e67060f4a71a24fb30dc509a8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.1` 的复用功能（Alternate Functions）。

<a id="r_a8221b41b8fb28555926d5b85d15d5e34"></a>

```c
#define PIN_P12_1__OSPI0_SCLKN_C ALIF_PINMUX(12, 1, 1)
```

相关声明：[PIN_P12_1__OSPI0_SCLKN_C](#a8221b41b8fb28555926d5b85d15d5e34)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`OSPI0_SCLKN_C`。

<a id="r_acd826cd6a2b2c9da4090a449c87b096f"></a>

```c
#define PIN_P12_1__UART4_RX_B ALIF_PINMUX(12, 1, 2)
```

相关声明：[PIN_P12_1__UART4_RX_B](#acd826cd6a2b2c9da4090a449c87b096f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`UART4_RX_B`。

<a id="r_a6350f1bf23731e2613c38513ade47d49"></a>

```c
#define PIN_P12_1__I2S1_SDO_B ALIF_PINMUX(12, 1, 3)
```

相关声明：[PIN_P12_1__I2S1_SDO_B](#a6350f1bf23731e2613c38513ade47d49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`I2S1_SDO_B`。

<a id="r_ac4acb53411c1a6e76660328524557cea"></a>

```c
#define PIN_P12_1__UT8_T1_C ALIF_PINMUX(12, 1, 4)
```

相关声明：[PIN_P12_1__UT8_T1_C](#ac4acb53411c1a6e76660328524557cea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`UT8_T1_C`。

<a id="r_a5ec1ec316fbad9d5102e079167cac94a"></a>

```c
#define PIN_P12_1__CDC_D9_B ALIF_PINMUX(12, 1, 5)
```

相关声明：[PIN_P12_1__CDC_D9_B](#a5ec1ec316fbad9d5102e079167cac94a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`CDC_D9_B`。

<a id="r_aa6c3f5c6a65b4a7a910ee860ce2769cd"></a>

```c
#define PIN_P12_1__OSPI1_D9_B ALIF_PINMUX(12, 1, 6)
```

相关声明：[PIN_P12_1__OSPI1_D9_B](#aa6c3f5c6a65b4a7a910ee860ce2769cd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`OSPI1_D9_B`。

<a id="r_a65a2680d02e24df11227fa9ba9abfeea"></a>

```c
#define PIN_P12_1__LPUT0_T1_B ALIF_PINMUX(12, 1, 7)
```

相关声明：[PIN_P12_1__LPUT0_T1_B](#a65a2680d02e24df11227fa9ba9abfeea)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）1：`LPUT0_T1_B`。

<a id="r_a27c28839016ec48c161a409262ee9fd3"></a>

```c
#define PIN_P12_2__GPIO ALIF_PINMUX(12, 2, 0)
```

相关声明：[PIN_P12_2__GPIO](#a27c28839016ec48c161a409262ee9fd3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.2` 的复用功能（Alternate Functions）。

<a id="r_a7dbe1289bb1eb6a5b2a9cfd35966346f"></a>

```c
#define PIN_P12_2__OSPI0_RXDS_C ALIF_PINMUX(12, 2, 1)
```

相关声明：[PIN_P12_2__OSPI0_RXDS_C](#a7dbe1289bb1eb6a5b2a9cfd35966346f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`OSPI0_RXDS_C`。

<a id="r_a09c39aeecba670bd260b1c6a9c2206bc"></a>

```c
#define PIN_P12_2__UART4_TX_B ALIF_PINMUX(12, 2, 2)
```

相关声明：[PIN_P12_2__UART4_TX_B](#a09c39aeecba670bd260b1c6a9c2206bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`UART4_TX_B`。

<a id="r_ad949740e8031844551438d452ea9fd98"></a>

```c
#define PIN_P12_2__I2S1_SCLK_B ALIF_PINMUX(12, 2, 3)
```

相关声明：[PIN_P12_2__I2S1_SCLK_B](#ad949740e8031844551438d452ea9fd98)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`I2S1_SCLK_B`。

<a id="r_a0d7147a61860a86ea3a8e14a6ec7fa1a"></a>

```c
#define PIN_P12_2__UT9_T0_C ALIF_PINMUX(12, 2, 4)
```

相关声明：[PIN_P12_2__UT9_T0_C](#a0d7147a61860a86ea3a8e14a6ec7fa1a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`UT9_T0_C`。

<a id="r_a11a8af8b4f8b44ec756ff5227326b660"></a>

```c
#define PIN_P12_2__CDC_D10_B ALIF_PINMUX(12, 2, 5)
```

相关声明：[PIN_P12_2__CDC_D10_B](#a11a8af8b4f8b44ec756ff5227326b660)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`CDC_D10_B`。

<a id="r_a31d26e22fa189f90cc1feaf47255ce58"></a>

```c
#define PIN_P12_2__OSPI1_D10_B ALIF_PINMUX(12, 2, 6)
```

相关声明：[PIN_P12_2__OSPI1_D10_B](#a31d26e22fa189f90cc1feaf47255ce58)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`OSPI1_D10_B`。

<a id="r_a494c0abfb0d593e0a7ce48942956c678"></a>

```c
#define PIN_P12_2__LPUT1_T0_B ALIF_PINMUX(12, 2, 7)
```

相关声明：[PIN_P12_2__LPUT1_T0_B](#a494c0abfb0d593e0a7ce48942956c678)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）2：`LPUT1_T0_B`。

<a id="r_af1e08dc87d97396b75f809ae0af2d992"></a>

```c
#define PIN_P12_3__GPIO ALIF_PINMUX(12, 3, 0)
```

相关声明：[PIN_P12_3__GPIO](#af1e08dc87d97396b75f809ae0af2d992)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.3` 的复用功能（Alternate Functions）。

<a id="r_ade9db8b6544f6e122d68929dbe159547"></a>

```c
#define PIN_P12_3__OSPI0_SS0_C ALIF_PINMUX(12, 3, 1)
```

相关声明：[PIN_P12_3__OSPI0_SS0_C](#ade9db8b6544f6e122d68929dbe159547)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`OSPI0_SS0_C`。

<a id="r_a6a3faabad47ea4952ff4ebdf2b590504"></a>

```c
#define PIN_P12_3__UART4_DE_B ALIF_PINMUX(12, 3, 2)
```

相关声明：[PIN_P12_3__UART4_DE_B](#a6a3faabad47ea4952ff4ebdf2b590504)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`UART4_DE_B`。

<a id="r_a6ce1e66ccde7c94d44cd3ea5d1fe36a5"></a>

```c
#define PIN_P12_3__I2S1_WS_B ALIF_PINMUX(12, 3, 3)
```

相关声明：[PIN_P12_3__I2S1_WS_B](#a6ce1e66ccde7c94d44cd3ea5d1fe36a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`I2S1_WS_B`。

<a id="r_a5a6847eb83cfba63b1a2f4d9ba263aaf"></a>

```c
#define PIN_P12_3__UT9_T1_C ALIF_PINMUX(12, 3, 4)
```

相关声明：[PIN_P12_3__UT9_T1_C](#a5a6847eb83cfba63b1a2f4d9ba263aaf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`UT9_T1_C`。

<a id="r_a4faa710258403e0879ba0b870caca58f"></a>

```c
#define PIN_P12_3__CDC_D11_B ALIF_PINMUX(12, 3, 5)
```

相关声明：[PIN_P12_3__CDC_D11_B](#a4faa710258403e0879ba0b870caca58f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`CDC_D11_B`。

<a id="r_a3f62884b90729ebee6430dc16eb6668d"></a>

```c
#define PIN_P12_3__OSPI1_D11_B ALIF_PINMUX(12, 3, 6)
```

相关声明：[PIN_P12_3__OSPI1_D11_B](#a3f62884b90729ebee6430dc16eb6668d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`OSPI1_D11_B`。

<a id="r_a2e108a8f92ba50eb7959b099e3e2c976"></a>

```c
#define PIN_P12_3__LPUT1_T1_B ALIF_PINMUX(12, 3, 7)
```

相关声明：[PIN_P12_3__LPUT1_T1_B](#a2e108a8f92ba50eb7959b099e3e2c976)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）3：`LPUT1_T1_B`。

<a id="r_adac47965f758c34ea5851e3c7994c684"></a>

```c
#define PIN_P12_4__GPIO ALIF_PINMUX(12, 4, 0)
```

相关声明：[PIN_P12_4__GPIO](#adac47965f758c34ea5851e3c7994c684)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.4` 的复用功能（Alternate Functions）。

<a id="r_a68cf8ccca7a0c7a6673f31617965cfc0"></a>

```c
#define PIN_P12_4__OSPI0_SS1_C ALIF_PINMUX(12, 4, 1)
```

相关声明：[PIN_P12_4__OSPI0_SS1_C](#a68cf8ccca7a0c7a6673f31617965cfc0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`OSPI0_SS1_C`。

<a id="r_a127ff0a7e34f5ad312615ef2c902cd19"></a>

```c
#define PIN_P12_4__SPI3_MISO_A ALIF_PINMUX(12, 4, 2)
```

相关声明：[PIN_P12_4__SPI3_MISO_A](#a127ff0a7e34f5ad312615ef2c902cd19)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`SPI3_MISO_A`。

<a id="r_a982db257c715bf8b82cdbb30126527c3"></a>

```c
#define PIN_P12_4__UT10_T0_C ALIF_PINMUX(12, 4, 3)
```

相关声明：[PIN_P12_4__UT10_T0_C](#a982db257c715bf8b82cdbb30126527c3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`UT10_T0_C`。

<a id="r_a4ff0a4748c5cda7cc3692d2e07f98df9"></a>

```c
#define PIN_P12_4__CAN_RXD_C ALIF_PINMUX(12, 4, 4)
```

相关声明：[PIN_P12_4__CAN_RXD_C](#a4ff0a4748c5cda7cc3692d2e07f98df9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`CAN_RXD_C`。

<a id="r_ae7b3d27ae4e38b66820c3f52ba36aad6"></a>

```c
#define PIN_P12_4__CDC_D12_B ALIF_PINMUX(12, 4, 5)
```

相关声明：[PIN_P12_4__CDC_D12_B](#ae7b3d27ae4e38b66820c3f52ba36aad6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`CDC_D12_B`。

<a id="r_adc73498c5243f494e5bb9e564ff7d765"></a>

```c
#define PIN_P12_4__OSPI1_D12_B ALIF_PINMUX(12, 4, 6)
```

相关声明：[PIN_P12_4__OSPI1_D12_B](#adc73498c5243f494e5bb9e564ff7d765)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`OSPI1_D12_B`。

<a id="r_ad8c7034e3f90fa1f4af3aa7f3f7df47f"></a>

```c
#define PIN_P12_4__LPUT2_T0_B ALIF_PINMUX(12, 4, 7)
```

相关声明：[PIN_P12_4__LPUT2_T0_B](#ad8c7034e3f90fa1f4af3aa7f3f7df47f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）4：`LPUT2_T0_B`。

<a id="r_a56334fbf74f9d40c512b30e00b5d59af"></a>

```c
#define PIN_P12_5__GPIO ALIF_PINMUX(12, 5, 0)
```

相关声明：[PIN_P12_5__GPIO](#a56334fbf74f9d40c512b30e00b5d59af)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.5` 的复用功能（Alternate Functions）。

<a id="r_a7b35f4e92b2fedbfd860f43f6b2692d8"></a>

```c
#define PIN_P12_5__HSUART0_RX_B ALIF_PINMUX(12, 5, 1)
```

相关声明：[PIN_P12_5__HSUART0_RX_B](#a7b35f4e92b2fedbfd860f43f6b2692d8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`HSUART0_RX_B`。

<a id="r_a2942041be841278356e235fafad62bb5"></a>

```c
#define PIN_P12_5__SPI3_MOSI_A ALIF_PINMUX(12, 5, 2)
```

相关声明：[PIN_P12_5__SPI3_MOSI_A](#a2942041be841278356e235fafad62bb5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`SPI3_MOSI_A`。

<a id="r_a841df0bcb5b3a75dbcb72ee691bfbb9d"></a>

```c
#define PIN_P12_5__UT10_T1_C ALIF_PINMUX(12, 5, 3)
```

相关声明：[PIN_P12_5__UT10_T1_C](#a841df0bcb5b3a75dbcb72ee691bfbb9d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`UT10_T1_C`。

<a id="r_ab78bc9a9078a306a8d10f6075ee31e6a"></a>

```c
#define PIN_P12_5__CAN_TXD_C ALIF_PINMUX(12, 5, 4)
```

相关声明：[PIN_P12_5__CAN_TXD_C](#ab78bc9a9078a306a8d10f6075ee31e6a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`CAN_TXD_C`。

<a id="r_a491b6de41ca668cb5d4b0b1d937949f3"></a>

```c
#define PIN_P12_5__CDC_D13_B ALIF_PINMUX(12, 5, 5)
```

相关声明：[PIN_P12_5__CDC_D13_B](#a491b6de41ca668cb5d4b0b1d937949f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`CDC_D13_B`。

<a id="r_a13897033e94c85375684df80e4b1dbbd"></a>

```c
#define PIN_P12_5__OSPI1_D13_B ALIF_PINMUX(12, 5, 6)
```

相关声明：[PIN_P12_5__OSPI1_D13_B](#a13897033e94c85375684df80e4b1dbbd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`OSPI1_D13_B`。

<a id="r_a4e74f662d9f36465ea5de6bd8aa0d7bd"></a>

```c
#define PIN_P12_5__LPUT2_T1_B ALIF_PINMUX(12, 5, 7)
```

相关声明：[PIN_P12_5__LPUT2_T1_B](#a4e74f662d9f36465ea5de6bd8aa0d7bd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）5：`LPUT2_T1_B`。

<a id="r_a39b3372e2a2ef9ebb8f4a621c856089e"></a>

```c
#define PIN_P12_6__GPIO ALIF_PINMUX(12, 6, 0)
```

相关声明：[PIN_P12_6__GPIO](#a39b3372e2a2ef9ebb8f4a621c856089e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.6` 的复用功能（Alternate Functions）。

<a id="r_a6c48c0632f27aec091208c2031a446a8"></a>

```c
#define PIN_P12_6__HSUART0_TX_B ALIF_PINMUX(12, 6, 1)
```

相关声明：[PIN_P12_6__HSUART0_TX_B](#a6c48c0632f27aec091208c2031a446a8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`HSUART0_TX_B`。

<a id="r_a50613420302d014ae2000b32497b0fa0"></a>

```c
#define PIN_P12_6__SPI3_SCLK_A ALIF_PINMUX(12, 6, 2)
```

相关声明：[PIN_P12_6__SPI3_SCLK_A](#a50613420302d014ae2000b32497b0fa0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`SPI3_SCLK_A`。

<a id="r_a67e9c045b7cd555d0060e3cc3964dd00"></a>

```c
#define PIN_P12_6__UT11_T0_C ALIF_PINMUX(12, 6, 3)
```

相关声明：[PIN_P12_6__UT11_T0_C](#a67e9c045b7cd555d0060e3cc3964dd00)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`UT11_T0_C`。

<a id="r_a098e6097b45f7451f6cee83577d0c2c0"></a>

```c
#define PIN_P12_6__CAN_STBY_C ALIF_PINMUX(12, 6, 4)
```

相关声明：[PIN_P12_6__CAN_STBY_C](#a098e6097b45f7451f6cee83577d0c2c0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`CAN_STBY_C`。

<a id="r_a24a0e40fe3472fcde95cf3551881764f"></a>

```c
#define PIN_P12_6__CDC_D14_B ALIF_PINMUX(12, 6, 5)
```

相关声明：[PIN_P12_6__CDC_D14_B](#a24a0e40fe3472fcde95cf3551881764f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`CDC_D14_B`。

<a id="r_af15787d2609e9f9aac820e0b5d7ab776"></a>

```c
#define PIN_P12_6__OSPI1_D14_B ALIF_PINMUX(12, 6, 6)
```

相关声明：[PIN_P12_6__OSPI1_D14_B](#af15787d2609e9f9aac820e0b5d7ab776)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）6：`OSPI1_D14_B`。

<a id="r_a7858fdaeed8a5e6f7fd673f67f8c7fdf"></a>

```c
#define PIN_P12_7__GPIO ALIF_PINMUX(12, 7, 0)
```

相关声明：[PIN_P12_7__GPIO](#a7858fdaeed8a5e6f7fd673f67f8c7fdf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P12.7` 的复用功能（Alternate Functions）。

<a id="r_a3bb480a483bbda13621751c2250647b8"></a>

```c
#define PIN_P12_7__OSPI1_RXDS0_B ALIF_PINMUX(12, 7, 1)
```

相关声明：[PIN_P12_7__OSPI1_RXDS0_B](#a3bb480a483bbda13621751c2250647b8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）7：`OSPI1_RXDS0_B`。

<a id="r_a322aa6e6071783ea7ec6c3583031ebf5"></a>

```c
#define PIN_P12_7__HSUART1_RX_B ALIF_PINMUX(12, 7, 2)
```

相关声明：[PIN_P12_7__HSUART1_RX_B](#a322aa6e6071783ea7ec6c3583031ebf5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）7：`HSUART1_RX_B`。

<a id="r_a2097584caa2b6da62fe7d6c78a5cd1c5"></a>

```c
#define PIN_P12_7__SPI3_SS0_A ALIF_PINMUX(12, 7, 3)
```

相关声明：[PIN_P12_7__SPI3_SS0_A](#a2097584caa2b6da62fe7d6c78a5cd1c5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）7：`SPI3_SS0_A`。

<a id="r_a4cfdb56dc6bec8fa75a054e75534c55b"></a>

```c
#define PIN_P12_7__UT11_T1_C ALIF_PINMUX(12, 7, 4)
```

相关声明：[PIN_P12_7__UT11_T1_C](#a4cfdb56dc6bec8fa75a054e75534c55b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）7：`UT11_T1_C`。

<a id="r_a6a19b3ceff99c8c3a88f010ca0e1c9e7"></a>

```c
#define PIN_P12_7__CDC_D15_B ALIF_PINMUX(12, 7, 5)
```

相关声明：[PIN_P12_7__CDC_D15_B](#a6a19b3ceff99c8c3a88f010ca0e1c9e7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）12 的引脚（Pin）7：`CDC_D15_B`。

<a id="define-members-14"></a>

### 端口 13 的引脚定义（Port 13 Pin Definitions）

GPIO 端口（Port）13 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a15b1cf15c599d1f8b2b01dd0e6f08d70"></a>

```c
#define PIN_P13_0__GPIO ALIF_PINMUX(13, 0, 0)
```

相关声明：[PIN_P13_0__GPIO](#a15b1cf15c599d1f8b2b01dd0e6f08d70)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.0` 的复用功能（Alternate Functions）。

<a id="r_a6f3684172961cbfa4e19238b8e07dbae"></a>

```c
#define PIN_P13_0__OSPI1_D0_B ALIF_PINMUX(13, 0, 1)
```

相关声明：[PIN_P13_0__OSPI1_D0_B](#a6f3684172961cbfa4e19238b8e07dbae)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`OSPI1_D0_B`。

<a id="r_a2935d09e541aa1b42e37115e7f6f1710"></a>

```c
#define PIN_P13_0__HSUART1_TX_B ALIF_PINMUX(13, 0, 2)
```

相关声明：[PIN_P13_0__HSUART1_TX_B](#a2935d09e541aa1b42e37115e7f6f1710)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`HSUART1_TX_B`。

<a id="r_aca67dc2ec0398fb093bdd6c27e7b1f90"></a>

```c
#define PIN_P13_0__SPI3_SS1_A ALIF_PINMUX(13, 0, 3)
```

相关声明：[PIN_P13_0__SPI3_SS1_A](#aca67dc2ec0398fb093bdd6c27e7b1f90)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`SPI3_SS1_A`。

<a id="r_ab3f16dacfc6ee3d596888fc83547b6d0"></a>

```c
#define PIN_P13_0__QEC0_X_C ALIF_PINMUX(13, 0, 4)
```

相关声明：[PIN_P13_0__QEC0_X_C](#ab3f16dacfc6ee3d596888fc83547b6d0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`QEC0_X_C`。

<a id="r_a6a38e02a116d40e4e50869ce0b7e134b"></a>

```c
#define PIN_P13_0__SD_D0_B ALIF_PINMUX(13, 0, 5)
```

相关声明：[PIN_P13_0__SD_D0_B](#a6a38e02a116d40e4e50869ce0b7e134b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`SD_D0_B`。

<a id="r_ade80479d70d2edcd9ee57fb11afe656a"></a>

```c
#define PIN_P13_0__CDC_D16_B ALIF_PINMUX(13, 0, 6)
```

相关声明：[PIN_P13_0__CDC_D16_B](#ade80479d70d2edcd9ee57fb11afe656a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`CDC_D16_B`。

<a id="r_a192323c04bd6e93e90c2fc5eacde9a4c"></a>

```c
#define PIN_P13_0__OSPI0_D8_A ALIF_PINMUX(13, 0, 7)
```

相关声明：[PIN_P13_0__OSPI0_D8_A](#a192323c04bd6e93e90c2fc5eacde9a4c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）0：`OSPI0_D8_A`。

<a id="r_ad680890bb2eb8d56701b7cab37482767"></a>

```c
#define PIN_P13_1__GPIO ALIF_PINMUX(13, 1, 0)
```

相关声明：[PIN_P13_1__GPIO](#ad680890bb2eb8d56701b7cab37482767)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.1` 的复用功能（Alternate Functions）。

<a id="r_ad532a64dc6a56d13a81016031e4e30ed"></a>

```c
#define PIN_P13_1__OSPI1_D1_B ALIF_PINMUX(13, 1, 1)
```

相关声明：[PIN_P13_1__OSPI1_D1_B](#ad532a64dc6a56d13a81016031e4e30ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`OSPI1_D1_B`。

<a id="r_a0d354def26be8822fdd3a5be9bcd81eb"></a>

```c
#define PIN_P13_1__SPI3_SS2_A ALIF_PINMUX(13, 1, 2)
```

相关声明：[PIN_P13_1__SPI3_SS2_A](#a0d354def26be8822fdd3a5be9bcd81eb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`SPI3_SS2_A`。

<a id="r_a931706ab2e90060aa32a96f6cfe20763"></a>

```c
#define PIN_P13_1__QEC0_Y_C ALIF_PINMUX(13, 1, 3)
```

相关声明：[PIN_P13_1__QEC0_Y_C](#a931706ab2e90060aa32a96f6cfe20763)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`QEC0_Y_C`。

<a id="r_ac764057ca19fb5947b08f4550e9ec218"></a>

```c
#define PIN_P13_1__SD_D1_B ALIF_PINMUX(13, 1, 4)
```

相关声明：[PIN_P13_1__SD_D1_B](#ac764057ca19fb5947b08f4550e9ec218)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`SD_D1_B`。

<a id="r_acccdd7840c08eec4de7bd8da9954a2b1"></a>

```c
#define PIN_P13_1__CDC_D17_B ALIF_PINMUX(13, 1, 5)
```

相关声明：[PIN_P13_1__CDC_D17_B](#acccdd7840c08eec4de7bd8da9954a2b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`CDC_D17_B`。

<a id="r_a9f2874e10fbd465f2e48b565be1e7334"></a>

```c
#define PIN_P13_1__OSPI0_D9_A ALIF_PINMUX(13, 1, 6)
```

相关声明：[PIN_P13_1__OSPI0_D9_A](#a9f2874e10fbd465f2e48b565be1e7334)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）1：`OSPI0_D9_A`。

<a id="r_aa087d0ade6968b63ff889cd05b975192"></a>

```c
#define PIN_P13_2__GPIO ALIF_PINMUX(13, 2, 0)
```

相关声明：[PIN_P13_2__GPIO](#aa087d0ade6968b63ff889cd05b975192)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.2` 的复用功能（Alternate Functions）。

<a id="r_a2c27142f1f5b8c87d9464692a792831a"></a>

```c
#define PIN_P13_2__OSPI1_D2_B ALIF_PINMUX(13, 2, 1)
```

相关声明：[PIN_P13_2__OSPI1_D2_B](#a2c27142f1f5b8c87d9464692a792831a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`OSPI1_D2_B`。

<a id="r_ab2a0c570e42d5602a13a74fa7667fffe"></a>

```c
#define PIN_P13_2__SPI3_SS3_A ALIF_PINMUX(13, 2, 2)
```

相关声明：[PIN_P13_2__SPI3_SS3_A](#ab2a0c570e42d5602a13a74fa7667fffe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`SPI3_SS3_A`。

<a id="r_a0f7d649cce0dda7a84c33277e2436d2d"></a>

```c
#define PIN_P13_2__QEC0_Z_C ALIF_PINMUX(13, 2, 3)
```

相关声明：[PIN_P13_2__QEC0_Z_C](#a0f7d649cce0dda7a84c33277e2436d2d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`QEC0_Z_C`。

<a id="r_aa8d14eb950ebc23d1c98a32bfbde5495"></a>

```c
#define PIN_P13_2__SD_D2_B ALIF_PINMUX(13, 2, 4)
```

相关声明：[PIN_P13_2__SD_D2_B](#aa8d14eb950ebc23d1c98a32bfbde5495)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`SD_D2_B`。

<a id="r_a935b8f0ed9215a2eaa878655a8063cdc"></a>

```c
#define PIN_P13_2__CDC_D18_B ALIF_PINMUX(13, 2, 5)
```

相关声明：[PIN_P13_2__CDC_D18_B](#a935b8f0ed9215a2eaa878655a8063cdc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`CDC_D18_B`。

<a id="r_ad511c284c7d0da7272fc448afd033f1a"></a>

```c
#define PIN_P13_2__OSPI0_D10_A ALIF_PINMUX(13, 2, 6)
```

相关声明：[PIN_P13_2__OSPI0_D10_A](#ad511c284c7d0da7272fc448afd033f1a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）2：`OSPI0_D10_A`。

<a id="r_aa75934dca9e234c0c0a7f284d4095d59"></a>

```c
#define PIN_P13_3__GPIO ALIF_PINMUX(13, 3, 0)
```

相关声明：[PIN_P13_3__GPIO](#aa75934dca9e234c0c0a7f284d4095d59)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.3` 的复用功能（Alternate Functions）。

<a id="r_adf31b9cc8510d1cff024c469a301a57c"></a>

```c
#define PIN_P13_3__OSPI1_D3_B ALIF_PINMUX(13, 3, 1)
```

相关声明：[PIN_P13_3__OSPI1_D3_B](#adf31b9cc8510d1cff024c469a301a57c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`OSPI1_D3_B`。

<a id="r_a3d41bd64e1a820e1cfbf40bb0bc43e21"></a>

```c
#define PIN_P13_3__SPI2_SS3_A ALIF_PINMUX(13, 3, 2)
```

相关声明：[PIN_P13_3__SPI2_SS3_A](#a3d41bd64e1a820e1cfbf40bb0bc43e21)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`SPI2_SS3_A`。

<a id="r_a0f12c337ed941d3f5e9d470ce92cad5b"></a>

```c
#define PIN_P13_3__QEC1_X_C ALIF_PINMUX(13, 3, 3)
```

相关声明：[PIN_P13_3__QEC1_X_C](#a0f12c337ed941d3f5e9d470ce92cad5b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`QEC1_X_C`。

<a id="r_aabf8b3713a85719ff1f18360bd59030a"></a>

```c
#define PIN_P13_3__SD_D3_B ALIF_PINMUX(13, 3, 4)
```

相关声明：[PIN_P13_3__SD_D3_B](#aabf8b3713a85719ff1f18360bd59030a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`SD_D3_B`。

<a id="r_a48ad50a933711f1f56cdb3438a0a8647"></a>

```c
#define PIN_P13_3__CDC_D19_B ALIF_PINMUX(13, 3, 5)
```

相关声明：[PIN_P13_3__CDC_D19_B](#a48ad50a933711f1f56cdb3438a0a8647)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`CDC_D19_B`。

<a id="r_add876fa4d66bc0f9b87b464175b36dfd"></a>

```c
#define PIN_P13_3__OSPI0_D11_A ALIF_PINMUX(13, 3, 6)
```

相关声明：[PIN_P13_3__OSPI0_D11_A](#add876fa4d66bc0f9b87b464175b36dfd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）3：`OSPI0_D11_A`。

<a id="r_ac67604479bd4bf8d4559a867553df01f"></a>

```c
#define PIN_P13_4__GPIO ALIF_PINMUX(13, 4, 0)
```

相关声明：[PIN_P13_4__GPIO](#ac67604479bd4bf8d4559a867553df01f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.4` 的复用功能（Alternate Functions）。

<a id="r_abacc197dea6924e35a8aa3e01b6ea71f"></a>

```c
#define PIN_P13_4__OSPI1_D4_B ALIF_PINMUX(13, 4, 1)
```

相关声明：[PIN_P13_4__OSPI1_D4_B](#abacc197dea6924e35a8aa3e01b6ea71f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`OSPI1_D4_B`。

<a id="r_ac316a1a39b1173a2121e2bb05c19d389"></a>

```c
#define PIN_P13_4__LPI2S_SDI_C ALIF_PINMUX(13, 4, 2)
```

相关声明：[PIN_P13_4__LPI2S_SDI_C](#ac316a1a39b1173a2121e2bb05c19d389)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`LPI2S_SDI_C`。

<a id="r_a6b47ac5773bf1c042efad0d88c963427"></a>

```c
#define PIN_P13_4__QEC1_Y_C ALIF_PINMUX(13, 4, 3)
```

相关声明：[PIN_P13_4__QEC1_Y_C](#a6b47ac5773bf1c042efad0d88c963427)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`QEC1_Y_C`。

<a id="r_a8b3d10ffbd5921896369eba148b7d919"></a>

```c
#define PIN_P13_4__SD_D4_B ALIF_PINMUX(13, 4, 4)
```

相关声明：[PIN_P13_4__SD_D4_B](#a8b3d10ffbd5921896369eba148b7d919)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`SD_D4_B`。

<a id="r_a9897921b8d6b3fafa479463b8420ffad"></a>

```c
#define PIN_P13_4__CDC_D20_B ALIF_PINMUX(13, 4, 5)
```

相关声明：[PIN_P13_4__CDC_D20_B](#a9897921b8d6b3fafa479463b8420ffad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`CDC_D20_B`。

<a id="r_a73a3e949def6b47cacfbab4c6a001f61"></a>

```c
#define PIN_P13_4__OSPI0_D12_A ALIF_PINMUX(13, 4, 6)
```

相关声明：[PIN_P13_4__OSPI0_D12_A](#a73a3e949def6b47cacfbab4c6a001f61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）4：`OSPI0_D12_A`。

<a id="r_a5a16054a66476a1e2cbb11e5d6fac9fe"></a>

```c
#define PIN_P13_5__GPIO ALIF_PINMUX(13, 5, 0)
```

相关声明：[PIN_P13_5__GPIO](#a5a16054a66476a1e2cbb11e5d6fac9fe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.5` 的复用功能（Alternate Functions）。

<a id="r_ac66b3b045737b1b495bd3d43eabd8ab8"></a>

```c
#define PIN_P13_5__OSPI1_D5_B ALIF_PINMUX(13, 5, 1)
```

相关声明：[PIN_P13_5__OSPI1_D5_B](#ac66b3b045737b1b495bd3d43eabd8ab8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`OSPI1_D5_B`。

<a id="r_af9307e64da01a7637f0d8df7883181a6"></a>

```c
#define PIN_P13_5__LPI2S_SDO_C ALIF_PINMUX(13, 5, 2)
```

相关声明：[PIN_P13_5__LPI2S_SDO_C](#af9307e64da01a7637f0d8df7883181a6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`LPI2S_SDO_C`。

<a id="r_a35346a9168c7589d1e70fc685d330a71"></a>

```c
#define PIN_P13_5__QEC1_Z_C ALIF_PINMUX(13, 5, 3)
```

相关声明：[PIN_P13_5__QEC1_Z_C](#a35346a9168c7589d1e70fc685d330a71)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`QEC1_Z_C`。

<a id="r_a49bba43520eeb4a0218b252dabe03613"></a>

```c
#define PIN_P13_5__SD_D5_B ALIF_PINMUX(13, 5, 4)
```

相关声明：[PIN_P13_5__SD_D5_B](#a49bba43520eeb4a0218b252dabe03613)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`SD_D5_B`。

<a id="r_a7b37cc3713b8987aee7bd378959ff597"></a>

```c
#define PIN_P13_5__CDC_D21_B ALIF_PINMUX(13, 5, 5)
```

相关声明：[PIN_P13_5__CDC_D21_B](#a7b37cc3713b8987aee7bd378959ff597)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`CDC_D21_B`。

<a id="r_ac5cbc603086cf6505246c22cbf5f14d9"></a>

```c
#define PIN_P13_5__OSPI0_D13_A ALIF_PINMUX(13, 5, 6)
```

相关声明：[PIN_P13_5__OSPI0_D13_A](#ac5cbc603086cf6505246c22cbf5f14d9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）5：`OSPI0_D13_A`。

<a id="r_a1f29f9ca971127618363127bf894a719"></a>

```c
#define PIN_P13_6__GPIO ALIF_PINMUX(13, 6, 0)
```

相关声明：[PIN_P13_6__GPIO](#a1f29f9ca971127618363127bf894a719)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.6` 的复用功能（Alternate Functions）。

<a id="r_af1c5fffce14d64485deb44043aa66295"></a>

```c
#define PIN_P13_6__OSPI1_D6_B ALIF_PINMUX(13, 6, 1)
```

相关声明：[PIN_P13_6__OSPI1_D6_B](#af1c5fffce14d64485deb44043aa66295)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`OSPI1_D6_B`。

<a id="r_a90861db1213e8bf6795fb97a18cccd90"></a>

```c
#define PIN_P13_6__LPI2S_SCLK_C ALIF_PINMUX(13, 6, 2)
```

相关声明：[PIN_P13_6__LPI2S_SCLK_C](#a90861db1213e8bf6795fb97a18cccd90)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`LPI2S_SCLK_C`。

<a id="r_ab8cba6146de31920e5ca261dd2b5b441"></a>

```c
#define PIN_P13_6__QEC2_X_C ALIF_PINMUX(13, 6, 3)
```

相关声明：[PIN_P13_6__QEC2_X_C](#ab8cba6146de31920e5ca261dd2b5b441)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`QEC2_X_C`。

<a id="r_a3143074cd350459fac284ef487c3c028"></a>

```c
#define PIN_P13_6__SD_D6_B ALIF_PINMUX(13, 6, 4)
```

相关声明：[PIN_P13_6__SD_D6_B](#a3143074cd350459fac284ef487c3c028)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`SD_D6_B`。

<a id="r_aa7eba7adaf6ccecf44391774c204928a"></a>

```c
#define PIN_P13_6__CDC_D22_B ALIF_PINMUX(13, 6, 5)
```

相关声明：[PIN_P13_6__CDC_D22_B](#aa7eba7adaf6ccecf44391774c204928a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`CDC_D22_B`。

<a id="r_ac9ccede3204288a2fbb4a0eb0100ce46"></a>

```c
#define PIN_P13_6__OSPI0_D14_A ALIF_PINMUX(13, 6, 6)
```

相关声明：[PIN_P13_6__OSPI0_D14_A](#ac9ccede3204288a2fbb4a0eb0100ce46)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）6：`OSPI0_D14_A`。

<a id="r_a42b654beaf5fb3f6722d69bafbd24beb"></a>

```c
#define PIN_P13_7__GPIO ALIF_PINMUX(13, 7, 0)
```

相关声明：[PIN_P13_7__GPIO](#a42b654beaf5fb3f6722d69bafbd24beb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P13.7` 的复用功能（Alternate Functions）。

<a id="r_a7f4ac9014f2a64e50e947e63a31fc6a3"></a>

```c
#define PIN_P13_7__OSPI1_D7_B ALIF_PINMUX(13, 7, 1)
```

相关声明：[PIN_P13_7__OSPI1_D7_B](#a7f4ac9014f2a64e50e947e63a31fc6a3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`OSPI1_D7_B`。

<a id="r_af1c94f8937b181d916b96fe0ccb385dd"></a>

```c
#define PIN_P13_7__LPI2S_WS_C ALIF_PINMUX(13, 7, 2)
```

相关声明：[PIN_P13_7__LPI2S_WS_C](#af1c94f8937b181d916b96fe0ccb385dd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`LPI2S_WS_C`。

<a id="r_a16b73c14e00b6780414435fc1f99a008"></a>

```c
#define PIN_P13_7__QEC2_Y_C ALIF_PINMUX(13, 7, 3)
```

相关声明：[PIN_P13_7__QEC2_Y_C](#a16b73c14e00b6780414435fc1f99a008)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`QEC2_Y_C`。

<a id="r_a8df4b1ab413c637d7aa5e8f6601ab5a4"></a>

```c
#define PIN_P13_7__SD_D7_B ALIF_PINMUX(13, 7, 4)
```

相关声明：[PIN_P13_7__SD_D7_B](#a8df4b1ab413c637d7aa5e8f6601ab5a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`SD_D7_B`。

<a id="r_a2a8d8fdf7c1da386aec7cf8dc992cfe8"></a>

```c
#define PIN_P13_7__CDC_D23_B ALIF_PINMUX(13, 7, 5)
```

相关声明：[PIN_P13_7__CDC_D23_B](#a2a8d8fdf7c1da386aec7cf8dc992cfe8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`CDC_D23_B`。

<a id="r_a9e813aca4f7934a6d468fc3a994fb043"></a>

```c
#define PIN_P13_7__OSPI0_D15_A ALIF_PINMUX(13, 7, 6)
```

相关声明：[PIN_P13_7__OSPI0_D15_A](#a9e813aca4f7934a6d468fc3a994fb043)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）13 的引脚（Pin）7：`OSPI0_D15_A`。

<a id="define-members-15"></a>

### 端口 14 的引脚定义（Port 14 Pin Definitions）

GPIO 端口（Port）14 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a1cbf1f2e853f2d489eeb2d2a1daa54b1"></a>

```c
#define PIN_P14_0__GPIO ALIF_PINMUX(14, 0, 0)
```

相关声明：[PIN_P14_0__GPIO](#a1cbf1f2e853f2d489eeb2d2a1daa54b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.0` 的复用功能（Alternate Functions）。

<a id="r_a5ca2782d59baafba4a2e0295e3333753"></a>

```c
#define PIN_P14_0__OSPI1_SCLK_B ALIF_PINMUX(14, 0, 1)
```

相关声明：[PIN_P14_0__OSPI1_SCLK_B](#a5ca2782d59baafba4a2e0295e3333753)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）0：`OSPI1_SCLK_B`。

<a id="r_a49b4d7291de66dc53a8b63746549b18d"></a>

```c
#define PIN_P14_0__UART6_RX_C ALIF_PINMUX(14, 0, 2)
```

相关声明：[PIN_P14_0__UART6_RX_C](#a49b4d7291de66dc53a8b63746549b18d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）0：`UART6_RX_C`。

<a id="r_a49aa7894468a1a50107ed45dba960049"></a>

```c
#define PIN_P14_0__QEC2_Z_C ALIF_PINMUX(14, 0, 3)
```

相关声明：[PIN_P14_0__QEC2_Z_C](#a49aa7894468a1a50107ed45dba960049)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）0：`QEC2_Z_C`。

<a id="r_a4b5bd52ebe29d09d5aa76da653578978"></a>

```c
#define PIN_P14_0__SD_CMD_B ALIF_PINMUX(14, 0, 4)
```

相关声明：[PIN_P14_0__SD_CMD_B](#a4b5bd52ebe29d09d5aa76da653578978)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）0：`SD_CMD_B`。

<a id="r_a3d35e77d076c4bc3f284a0270bddbbdf"></a>

```c
#define PIN_P14_0__LFRC_OUT_B ALIF_PINMUX(14, 0, 5)
```

相关声明：[PIN_P14_0__LFRC_OUT_B](#a3d35e77d076c4bc3f284a0270bddbbdf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）0：`LFRC_OUT_B`。

<a id="r_a04f061154e4fe1cbc3bca5d7f66c79be"></a>

```c
#define PIN_P14_1__GPIO ALIF_PINMUX(14, 1, 0)
```

相关声明：[PIN_P14_1__GPIO](#a04f061154e4fe1cbc3bca5d7f66c79be)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.1` 的复用功能（Alternate Functions）。

<a id="r_a20c4ce2960204844c6521a351c597ca5"></a>

```c
#define PIN_P14_1__OSPI1_SCLKN_B ALIF_PINMUX(14, 1, 1)
```

相关声明：[PIN_P14_1__OSPI1_SCLKN_B](#a20c4ce2960204844c6521a351c597ca5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`OSPI1_SCLKN_B`。

<a id="r_ad6eaa8dd8c5be5317ba78a60f4e52de8"></a>

```c
#define PIN_P14_1__UART6_TX_C ALIF_PINMUX(14, 1, 2)
```

相关声明：[PIN_P14_1__UART6_TX_C](#ad6eaa8dd8c5be5317ba78a60f4e52de8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`UART6_TX_C`。

<a id="r_a1ed2a56d90d62dc6537ca251a51d9f11"></a>

```c
#define PIN_P14_1__APLL_OUT_C ALIF_PINMUX(14, 1, 3)
```

相关声明：[PIN_P14_1__APLL_OUT_C](#a1ed2a56d90d62dc6537ca251a51d9f11)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`APLL_OUT_C`。

<a id="r_a1dd67381d31bf2a77432474b28c96171"></a>

```c
#define PIN_P14_1__QEC3_X_C ALIF_PINMUX(14, 1, 4)
```

相关声明：[PIN_P14_1__QEC3_X_C](#a1dd67381d31bf2a77432474b28c96171)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`QEC3_X_C`。

<a id="r_a696067713fdb1bcaae580f9243fc532f"></a>

```c
#define PIN_P14_1__SD_CLK_B ALIF_PINMUX(14, 1, 5)
```

相关声明：[PIN_P14_1__SD_CLK_B](#a696067713fdb1bcaae580f9243fc532f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`SD_CLK_B`。

<a id="r_a5309e7ad0e247402ec4f4668790c0f16"></a>

```c
#define PIN_P14_1__LFXO_OUT_B ALIF_PINMUX(14, 1, 6)
```

相关声明：[PIN_P14_1__LFXO_OUT_B](#a5309e7ad0e247402ec4f4668790c0f16)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）1：`LFXO_OUT_B`。

<a id="r_a540585afd2427a265053f4033f1d0e92"></a>

```c
#define PIN_P14_2__GPIO ALIF_PINMUX(14, 2, 0)
```

相关声明：[PIN_P14_2__GPIO](#a540585afd2427a265053f4033f1d0e92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.2` 的复用功能（Alternate Functions）。

<a id="r_a7e8dfedc5e752f15125b114555451178"></a>

```c
#define PIN_P14_2__OSPI1_SS0_B ALIF_PINMUX(14, 2, 1)
```

相关声明：[PIN_P14_2__OSPI1_SS0_B](#a7e8dfedc5e752f15125b114555451178)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`OSPI1_SS0_B`。

<a id="r_a94d4d9dd458f09d2f49db1bbe739fc89"></a>

```c
#define PIN_P14_2__UART7_RX_C ALIF_PINMUX(14, 2, 2)
```

相关声明：[PIN_P14_2__UART7_RX_C](#a94d4d9dd458f09d2f49db1bbe739fc89)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`UART7_RX_C`。

<a id="r_a33da038373513a8395f48823b06c3111"></a>

```c
#define PIN_P14_2__LPI3C_SDA_C ALIF_PINMUX(14, 2, 3)
```

相关声明：[PIN_P14_2__LPI3C_SDA_C](#a33da038373513a8395f48823b06c3111)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`LPI3C_SDA_C`。

<a id="r_ad04b7586c46f82324cd494ded92f1734"></a>

```c
#define PIN_P14_2__QEC3_Y_C ALIF_PINMUX(14, 2, 4)
```

相关声明：[PIN_P14_2__QEC3_Y_C](#ad04b7586c46f82324cd494ded92f1734)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`QEC3_Y_C`。

<a id="r_a2b2afb838b4fc24227e5dc587b692938"></a>

```c
#define PIN_P14_2__SD_RST_B ALIF_PINMUX(14, 2, 5)
```

相关声明：[PIN_P14_2__SD_RST_B](#a2b2afb838b4fc24227e5dc587b692938)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`SD_RST_B`。

<a id="r_aa17bd78fd8b8190e613d199761128602"></a>

```c
#define PIN_P14_2__LPSPI_SS5_B ALIF_PINMUX(14, 2, 6)
```

相关声明：[PIN_P14_2__LPSPI_SS5_B](#aa17bd78fd8b8190e613d199761128602)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）2：`LPSPI_SS5_B`。

<a id="r_a143e7d370589dab01e92dfbd48336c85"></a>

```c
#define PIN_P14_3__GPIO ALIF_PINMUX(14, 3, 0)
```

相关声明：[PIN_P14_3__GPIO](#a143e7d370589dab01e92dfbd48336c85)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.3` 的复用功能（Alternate Functions）。

<a id="r_abd81a8224aa0eaeae2471a989abe24a5"></a>

```c
#define PIN_P14_3__OSPI1_SS1_B ALIF_PINMUX(14, 3, 1)
```

相关声明：[PIN_P14_3__OSPI1_SS1_B](#abd81a8224aa0eaeae2471a989abe24a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）3：`OSPI1_SS1_B`。

<a id="r_a82039aa8a98ed309e89ca8996bd4d3fa"></a>

```c
#define PIN_P14_3__UART7_TX_C ALIF_PINMUX(14, 3, 2)
```

相关声明：[PIN_P14_3__UART7_TX_C](#a82039aa8a98ed309e89ca8996bd4d3fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）3：`UART7_TX_C`。

<a id="r_a2c5f5373c98d4d1efb13e4b6f4650f00"></a>

```c
#define PIN_P14_3__LPI3C_SCL_C ALIF_PINMUX(14, 3, 3)
```

相关声明：[PIN_P14_3__LPI3C_SCL_C](#a2c5f5373c98d4d1efb13e4b6f4650f00)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）3：`LPI3C_SCL_C`。

<a id="r_ae80e3c69274bbe71007d2ab84d822328"></a>

```c
#define PIN_P14_3__QEC3_Z_C ALIF_PINMUX(14, 3, 4)
```

相关声明：[PIN_P14_3__QEC3_Z_C](#ae80e3c69274bbe71007d2ab84d822328)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）3：`QEC3_Z_C`。

<a id="r_a394dc4720bf0af77b3a1bc0e1fd3bbd9"></a>

```c
#define PIN_P14_4__GPIO ALIF_PINMUX(14, 4, 0)
```

相关声明：[PIN_P14_4__GPIO](#a394dc4720bf0af77b3a1bc0e1fd3bbd9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.4` 的复用功能（Alternate Functions）。

<a id="r_acee71b28db5d2fa95abfe302d44f5b25"></a>

```c
#define PIN_P14_4__CMP3_OUT_B ALIF_PINMUX(14, 4, 1)
```

相关声明：[PIN_P14_4__CMP3_OUT_B](#acee71b28db5d2fa95abfe302d44f5b25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）4：`CMP3_OUT_B`。

<a id="r_a6c6af82925d4c50ce7c0c50ace329326"></a>

```c
#define PIN_P14_4__SPI1_MISO_C ALIF_PINMUX(14, 4, 2)
```

相关声明：[PIN_P14_4__SPI1_MISO_C](#a6c6af82925d4c50ce7c0c50ace329326)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）4：`SPI1_MISO_C`。

<a id="r_ad5113822126585fe88b5f8ecafc2143f"></a>

```c
#define PIN_P14_4__FAULT0_C ALIF_PINMUX(14, 4, 3)
```

相关声明：[PIN_P14_4__FAULT0_C](#ad5113822126585fe88b5f8ecafc2143f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）4：`FAULT0_C`。

<a id="r_a241b5f26d5b27d9713824727bbb56f67"></a>

```c
#define PIN_P14_4__OSPI1_RXDS1_A ALIF_PINMUX(14, 4, 4)
```

相关声明：[PIN_P14_4__OSPI1_RXDS1_A](#a241b5f26d5b27d9713824727bbb56f67)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）4：`OSPI1_RXDS1_A`。

<a id="r_afdd8de79f83cd6eeb27882eb915c1837"></a>

```c
#define PIN_P14_4__LPSPI_SS1_B ALIF_PINMUX(14, 4, 5)
```

相关声明：[PIN_P14_4__LPSPI_SS1_B](#afdd8de79f83cd6eeb27882eb915c1837)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）4：`LPSPI_SS1_B`。

<a id="r_a8a95826bd89110378f6bf0885216d120"></a>

```c
#define PIN_P14_5__GPIO ALIF_PINMUX(14, 5, 0)
```

相关声明：[PIN_P14_5__GPIO](#a8a95826bd89110378f6bf0885216d120)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.5` 的复用功能（Alternate Functions）。

<a id="r_aac41aa725e8c16a0b28a17fce43d6f11"></a>

```c
#define PIN_P14_5__CMP2_OUT_B ALIF_PINMUX(14, 5, 1)
```

相关声明：[PIN_P14_5__CMP2_OUT_B](#aac41aa725e8c16a0b28a17fce43d6f11)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）5：`CMP2_OUT_B`。

<a id="r_a2dc20aaefaebb6f454c03453904c1f42"></a>

```c
#define PIN_P14_5__SPI1_MOSI_C ALIF_PINMUX(14, 5, 2)
```

相关声明：[PIN_P14_5__SPI1_MOSI_C](#a2dc20aaefaebb6f454c03453904c1f42)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）5：`SPI1_MOSI_C`。

<a id="r_af36139ef2ab829cbcd2e0417bcd3246e"></a>

```c
#define PIN_P14_5__FAULT1_C ALIF_PINMUX(14, 5, 3)
```

相关声明：[PIN_P14_5__FAULT1_C](#af36139ef2ab829cbcd2e0417bcd3246e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）5：`FAULT1_C`。

<a id="r_a385b2d31c016c30bd67c4cdba1011ead"></a>

```c
#define PIN_P14_5__OSPI0_RXDS1_B ALIF_PINMUX(14, 5, 4)
```

相关声明：[PIN_P14_5__OSPI0_RXDS1_B](#a385b2d31c016c30bd67c4cdba1011ead)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）5：`OSPI0_RXDS1_B`。

<a id="r_a9cc5380a5984b10a1630f8755985fa71"></a>

```c
#define PIN_P14_5__LPSPI_SS2_B ALIF_PINMUX(14, 5, 5)
```

相关声明：[PIN_P14_5__LPSPI_SS2_B](#a9cc5380a5984b10a1630f8755985fa71)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）5：`LPSPI_SS2_B`。

<a id="r_a995ed7190261b83cede4eab37c6afdd8"></a>

```c
#define PIN_P14_6__GPIO ALIF_PINMUX(14, 6, 0)
```

相关声明：[PIN_P14_6__GPIO](#a995ed7190261b83cede4eab37c6afdd8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.6` 的复用功能（Alternate Functions）。

<a id="r_a0cb8498d547cb5b864d008a8744612c6"></a>

```c
#define PIN_P14_6__CMP1_OUT_B ALIF_PINMUX(14, 6, 1)
```

相关声明：[PIN_P14_6__CMP1_OUT_B](#a0cb8498d547cb5b864d008a8744612c6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）6：`CMP1_OUT_B`。

<a id="r_a117d335a297134a4af1f3e7a83bf15af"></a>

```c
#define PIN_P14_6__SPI1_SCLK_C ALIF_PINMUX(14, 6, 2)
```

相关声明：[PIN_P14_6__SPI1_SCLK_C](#a117d335a297134a4af1f3e7a83bf15af)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）6：`SPI1_SCLK_C`。

<a id="r_a7bc7b758724c5f381b917faa265a06cd"></a>

```c
#define PIN_P14_6__FAULT2_C ALIF_PINMUX(14, 6, 3)
```

相关声明：[PIN_P14_6__FAULT2_C](#a7bc7b758724c5f381b917faa265a06cd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）6：`FAULT2_C`。

<a id="r_a52a6a685be88180e360e1a3b29a327f6"></a>

```c
#define PIN_P14_6__OSPI1_D15_B ALIF_PINMUX(14, 6, 4)
```

相关声明：[PIN_P14_6__OSPI1_D15_B](#a52a6a685be88180e360e1a3b29a327f6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）6：`OSPI1_D15_B`。

<a id="r_a639129b2cbcb7a39509533c748b719d2"></a>

```c
#define PIN_P14_6__LPSPI_SS3_B ALIF_PINMUX(14, 6, 5)
```

相关声明：[PIN_P14_6__LPSPI_SS3_B](#a639129b2cbcb7a39509533c748b719d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）6：`LPSPI_SS3_B`。

<a id="r_abd4fb434a55d691d2fa3a5267187ae9c"></a>

```c
#define PIN_P14_7__GPIO ALIF_PINMUX(14, 7, 0)
```

相关声明：[PIN_P14_7__GPIO](#abd4fb434a55d691d2fa3a5267187ae9c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P14.7` 的复用功能（Alternate Functions）。

<a id="r_afa8df9c3a93767723e25958f5c37882c"></a>

```c
#define PIN_P14_7__CMP0_OUT_B ALIF_PINMUX(14, 7, 1)
```

相关声明：[PIN_P14_7__CMP0_OUT_B](#afa8df9c3a93767723e25958f5c37882c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）7：`CMP0_OUT_B`。

<a id="r_aebe3294759cc2654a4dca1a81002bb03"></a>

```c
#define PIN_P14_7__SPI1_SS0_C ALIF_PINMUX(14, 7, 2)
```

相关声明：[PIN_P14_7__SPI1_SS0_C](#aebe3294759cc2654a4dca1a81002bb03)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）7：`SPI1_SS0_C`。

<a id="r_a16d1531f14b3fd9138d362bef5e91339"></a>

```c
#define PIN_P14_7__FAULT3_C ALIF_PINMUX(14, 7, 3)
```

相关声明：[PIN_P14_7__FAULT3_C](#a16d1531f14b3fd9138d362bef5e91339)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）7：`FAULT3_C`。

<a id="r_a3c9b1256f40856381742ee1f656eb59f"></a>

```c
#define PIN_P14_7__APLL_OUT_B ALIF_PINMUX(14, 7, 4)
```

相关声明：[PIN_P14_7__APLL_OUT_B](#a3c9b1256f40856381742ee1f656eb59f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）7：`APLL_OUT_B`。

<a id="r_ad43c40c9a544ed09eb334d772f8ce862"></a>

```c
#define PIN_P14_7__LPSPI_SS4_B ALIF_PINMUX(14, 7, 5)
```

相关声明：[PIN_P14_7__LPSPI_SS4_B](#ad43c40c9a544ed09eb334d772f8ce862)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）14 的引脚（Pin）7：`LPSPI_SS4_B`。

<a id="define-members-16"></a>

### 端口 15 的引脚定义（Port 15 Pin Definitions）

GPIO 端口（Port）15 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a482ff296b3458b8da397d102f23bba34"></a>

```c
#define PIN_P15_0__LPGPIO ALIF_PINMUX(15, 0, 0)
```

相关声明：[PIN_P15_0__LPGPIO](#a482ff296b3458b8da397d102f23bba34)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.0` 的复用功能（Alternate Functions）。

<a id="r_a87b1f1b590da3e225affcf5e22e0fde0"></a>

```c
#define PIN_P15_1__LPGPIO ALIF_PINMUX(15, 1, 0)
```

相关声明：[PIN_P15_1__LPGPIO](#a87b1f1b590da3e225affcf5e22e0fde0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.1` 的复用功能（Alternate Functions）。

<a id="r_a751069828ce828f0fde9e133d1cff1d8"></a>

```c
#define PIN_P15_2__LPGPIO ALIF_PINMUX(15, 2, 0)
```

相关声明：[PIN_P15_2__LPGPIO](#a751069828ce828f0fde9e133d1cff1d8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.2` 的复用功能（Alternate Functions）。

<a id="r_a53daed0b63bb612e52340e3d0bff6469"></a>

```c
#define PIN_P15_3__LPGPIO ALIF_PINMUX(15, 3, 0)
```

相关声明：[PIN_P15_3__LPGPIO](#a53daed0b63bb612e52340e3d0bff6469)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.3` 的复用功能（Alternate Functions）。

<a id="r_a6d2b399ef4fc71146b02683ad8b922f4"></a>

```c
#define PIN_P15_4__LPGPIO ALIF_PINMUX(15, 4, 0)
```

相关声明：[PIN_P15_4__LPGPIO](#a6d2b399ef4fc71146b02683ad8b922f4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.4` 的复用功能（Alternate Functions）。

<a id="r_a59a4b7046f20d806ef14f465199ec07b"></a>

```c
#define PIN_P15_5__LPGPIO ALIF_PINMUX(15, 5, 0)
```

相关声明：[PIN_P15_5__LPGPIO](#a59a4b7046f20d806ef14f465199ec07b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.5` 的复用功能（Alternate Functions）。

<a id="r_adc15a08c93aafd26cea6eb6deced95a9"></a>

```c
#define PIN_P15_6__LPGPIO ALIF_PINMUX(15, 6, 0)
```

相关声明：[PIN_P15_6__LPGPIO](#adc15a08c93aafd26cea6eb6deced95a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.6` 的复用功能（Alternate Functions）。

<a id="r_a345e070b3f7cc4176a2d730829b248b9"></a>

```c
#define PIN_P15_7__LPGPIO ALIF_PINMUX(15, 7, 0)
```

相关声明：[PIN_P15_7__LPGPIO](#a345e070b3f7cc4176a2d730829b248b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P15.7` 的复用功能（Alternate Functions）。

<a id="define-members-17"></a>

### 端口 16 的引脚定义（Port 16 Pin Definitions）

GPIO 端口（Port）16 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_abfb6c484ca20ec0b083a4413b4dc3fc3"></a>

```c
#define PIN_P16_0__GPIO ALIF_PINMUX(16, 0, 0)
```

相关声明：[PIN_P16_0__GPIO](#abfb6c484ca20ec0b083a4413b4dc3fc3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.0` 的复用功能（Alternate Functions）。

<a id="r_a485d492961fdff6770233e4f41da383f"></a>

```c
#define PIN_P16_0__OSPI0_D8_B ALIF_PINMUX(16, 0, 1)
```

相关声明：[PIN_P16_0__OSPI0_D8_B](#a485d492961fdff6770233e4f41da383f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）0：`OSPI0_D8_B`。

<a id="r_a02cd3d03d139cbf6522ab0cef61f665e"></a>

```c
#define PIN_P16_1__GPIO ALIF_PINMUX(16, 1, 0)
```

相关声明：[PIN_P16_1__GPIO](#a02cd3d03d139cbf6522ab0cef61f665e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.1` 的复用功能（Alternate Functions）。

<a id="r_a6ae160d4439825219291f521bdd5e378"></a>

```c
#define PIN_P16_1__OSPI0_D9_B ALIF_PINMUX(16, 1, 1)
```

相关声明：[PIN_P16_1__OSPI0_D9_B](#a6ae160d4439825219291f521bdd5e378)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）1：`OSPI0_D9_B`。

<a id="r_aaf71f322736ae2427cd663318492a956"></a>

```c
#define PIN_P16_2__GPIO ALIF_PINMUX(16, 2, 0)
```

相关声明：[PIN_P16_2__GPIO](#aaf71f322736ae2427cd663318492a956)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.2` 的复用功能（Alternate Functions）。

<a id="r_ad1434cab1444cc0537314b8df3661b9b"></a>

```c
#define PIN_P16_2__OSPI0_D10_B ALIF_PINMUX(16, 2, 1)
```

相关声明：[PIN_P16_2__OSPI0_D10_B](#ad1434cab1444cc0537314b8df3661b9b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）2：`OSPI0_D10_B`。

<a id="r_a619c9544bbcf8b2e74be37cc140e097c"></a>

```c
#define PIN_P16_3__GPIO ALIF_PINMUX(16, 3, 0)
```

相关声明：[PIN_P16_3__GPIO](#a619c9544bbcf8b2e74be37cc140e097c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.3` 的复用功能（Alternate Functions）。

<a id="r_a532efee68413e7a1213ca76dbd759b48"></a>

```c
#define PIN_P16_3__OSPI0_D11_B ALIF_PINMUX(16, 3, 1)
```

相关声明：[PIN_P16_3__OSPI0_D11_B](#a532efee68413e7a1213ca76dbd759b48)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）3：`OSPI0_D11_B`。

<a id="r_af904fe04f416c076c1bae945cd29ea09"></a>

```c
#define PIN_P16_4__GPIO ALIF_PINMUX(16, 4, 0)
```

相关声明：[PIN_P16_4__GPIO](#af904fe04f416c076c1bae945cd29ea09)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.4` 的复用功能（Alternate Functions）。

<a id="r_a28722750644304419fc81705c277904e"></a>

```c
#define PIN_P16_4__OSPI0_D12_B ALIF_PINMUX(16, 4, 1)
```

相关声明：[PIN_P16_4__OSPI0_D12_B](#a28722750644304419fc81705c277904e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）4：`OSPI0_D12_B`。

<a id="r_a44a5ae5fa1c9d027d52bed5b6e7ef6db"></a>

```c
#define PIN_P16_5__GPIO ALIF_PINMUX(16, 5, 0)
```

相关声明：[PIN_P16_5__GPIO](#a44a5ae5fa1c9d027d52bed5b6e7ef6db)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.5` 的复用功能（Alternate Functions）。

<a id="r_adba8b9b4957cbfeb71144b05887ac040"></a>

```c
#define PIN_P16_5__OSPI0_D13_B ALIF_PINMUX(16, 5, 1)
```

相关声明：[PIN_P16_5__OSPI0_D13_B](#adba8b9b4957cbfeb71144b05887ac040)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）5：`OSPI0_D13_B`。

<a id="r_a123ae5eee36c06a449bccf886b48806b"></a>

```c
#define PIN_P16_6__GPIO ALIF_PINMUX(16, 6, 0)
```

相关声明：[PIN_P16_6__GPIO](#a123ae5eee36c06a449bccf886b48806b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.6` 的复用功能（Alternate Functions）。

<a id="r_a351e28f4ffc15bc8cbfc8febd24f6872"></a>

```c
#define PIN_P16_6__OSPI0_D14_B ALIF_PINMUX(16, 6, 1)
```

相关声明：[PIN_P16_6__OSPI0_D14_B](#a351e28f4ffc15bc8cbfc8febd24f6872)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）6：`OSPI0_D14_B`。

<a id="r_ab7acb4286b257f94f3a0051ae863dfa6"></a>

```c
#define PIN_P16_7__GPIO ALIF_PINMUX(16, 7, 0)
```

相关声明：[PIN_P16_7__GPIO](#ab7acb4286b257f94f3a0051ae863dfa6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P16.7` 的复用功能（Alternate Functions）。

<a id="r_aa87bbb168ea3a41c76cbd437d02bcfbe"></a>

```c
#define PIN_P16_7__OSPI0_D15_B ALIF_PINMUX(16, 7, 1)
```

相关声明：[PIN_P16_7__OSPI0_D15_B](#aa87bbb168ea3a41c76cbd437d02bcfbe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）16 的引脚（Pin）7：`OSPI0_D15_B`。

<a id="define-members-18"></a>

### 端口 17 的引脚定义（Port 17 Pin Definitions）

GPIO 端口（Port）17 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a5c98a4c40236de006b32484b485bea65"></a>

```c
#define PIN_P17_0__GPIO ALIF_PINMUX(17, 0, 0)
```

相关声明：[PIN_P17_0__GPIO](#a5c98a4c40236de006b32484b485bea65)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.0` 的复用功能（Alternate Functions）。

<a id="r_a63fc4d6d872ca13ab41154620c7cb6a3"></a>

```c
#define PIN_P17_0__OSPI1_D8_C ALIF_PINMUX(17, 0, 1)
```

相关声明：[PIN_P17_0__OSPI1_D8_C](#a63fc4d6d872ca13ab41154620c7cb6a3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）0：`OSPI1_D8_C`。

<a id="r_abbb6a915fdb7d1a1b5949c0ec17bbdba"></a>

```c
#define PIN_P17_1__GPIO ALIF_PINMUX(17, 1, 0)
```

相关声明：[PIN_P17_1__GPIO](#abbb6a915fdb7d1a1b5949c0ec17bbdba)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.1` 的复用功能（Alternate Functions）。

<a id="r_a47038228f774e7d02197614267a65be5"></a>

```c
#define PIN_P17_1__OSPI1_D9_C ALIF_PINMUX(17, 1, 1)
```

相关声明：[PIN_P17_1__OSPI1_D9_C](#a47038228f774e7d02197614267a65be5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）1：`OSPI1_D9_C`。

<a id="r_a574598de77ccdb330be4c9f480d0c0c6"></a>

```c
#define PIN_P17_2__GPIO ALIF_PINMUX(17, 2, 0)
```

相关声明：[PIN_P17_2__GPIO](#a574598de77ccdb330be4c9f480d0c0c6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.2` 的复用功能（Alternate Functions）。

<a id="r_a69a8a2c8793d9d827948a8c09786bd81"></a>

```c
#define PIN_P17_2__OSPI1_D10_C ALIF_PINMUX(17, 2, 1)
```

相关声明：[PIN_P17_2__OSPI1_D10_C](#a69a8a2c8793d9d827948a8c09786bd81)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）2：`OSPI1_D10_C`。

<a id="r_afd3b2e2d006b6b3f4c1323469d9366c0"></a>

```c
#define PIN_P17_3__GPIO ALIF_PINMUX(17, 3, 0)
```

相关声明：[PIN_P17_3__GPIO](#afd3b2e2d006b6b3f4c1323469d9366c0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.3` 的复用功能（Alternate Functions）。

<a id="r_aa05d36fb2a03632ebbf31ef3025fa9a4"></a>

```c
#define PIN_P17_3__OSPI1_D11_C ALIF_PINMUX(17, 3, 1)
```

相关声明：[PIN_P17_3__OSPI1_D11_C](#aa05d36fb2a03632ebbf31ef3025fa9a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）3：`OSPI1_D11_C`。

<a id="r_a3987a256ab19e5653c3cf2c39dd62722"></a>

```c
#define PIN_P17_4__GPIO ALIF_PINMUX(17, 4, 0)
```

相关声明：[PIN_P17_4__GPIO](#a3987a256ab19e5653c3cf2c39dd62722)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.4` 的复用功能（Alternate Functions）。

<a id="r_a224218094cfd29015cbb6702eb8c3ffb"></a>

```c
#define PIN_P17_4__OSPI1_D12_C ALIF_PINMUX(17, 4, 1)
```

相关声明：[PIN_P17_4__OSPI1_D12_C](#a224218094cfd29015cbb6702eb8c3ffb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）4：`OSPI1_D12_C`。

<a id="r_a2a6dd0f9c58af43a8c0dec530b4eac31"></a>

```c
#define PIN_P17_5__GPIO ALIF_PINMUX(17, 5, 0)
```

相关声明：[PIN_P17_5__GPIO](#a2a6dd0f9c58af43a8c0dec530b4eac31)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.5` 的复用功能（Alternate Functions）。

<a id="r_a8449a677fedbc254b014dc91de8eb7ec"></a>

```c
#define PIN_P17_5__OSPI1_D13_C ALIF_PINMUX(17, 5, 1)
```

相关声明：[PIN_P17_5__OSPI1_D13_C](#a8449a677fedbc254b014dc91de8eb7ec)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）5：`OSPI1_D13_C`。

<a id="r_ab7d0d3b92adf9ca32d37337c12df63d6"></a>

```c
#define PIN_P17_6__GPIO ALIF_PINMUX(17, 6, 0)
```

相关声明：[PIN_P17_6__GPIO](#ab7d0d3b92adf9ca32d37337c12df63d6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.6` 的复用功能（Alternate Functions）。

<a id="r_aea275755208a04e1cf624d773f611015"></a>

```c
#define PIN_P17_6__OSPI1_D14_C ALIF_PINMUX(17, 6, 1)
```

相关声明：[PIN_P17_6__OSPI1_D14_C](#aea275755208a04e1cf624d773f611015)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）6：`OSPI1_D14_C`。

<a id="r_a6bb6e4af895fa892866cb228c5b9413b"></a>

```c
#define PIN_P17_7__GPIO ALIF_PINMUX(17, 7, 0)
```

相关声明：[PIN_P17_7__GPIO](#a6bb6e4af895fa892866cb228c5b9413b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P17.7` 的复用功能（Alternate Functions）。

<a id="r_a5efdaed363308f46af5032c61f7656a3"></a>

```c
#define PIN_P17_7__OSPI1_D15_C ALIF_PINMUX(17, 7, 1)
```

相关声明：[PIN_P17_7__OSPI1_D15_C](#a5efdaed363308f46af5032c61f7656a3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）17 的引脚（Pin）7：`OSPI1_D15_C`。

## 3.2\_详细说明（Detailed Documentation）

<a id="ab0a2e9966868f5dcb365d5d533318a21"></a>

### `ALIF_PINMUX`

```c
#define ALIF_PINMUX ( port, pin, func )
```

展开值（Value）：

```c
((((port) & ALIF_PINMUX_PORT_MASK) << ALIF_PINMUX_PORT_POS) |   \
(((pin) & ALIF_PINMUX_PIN_MASK) << ALIF_PINMUX_PIN_POS) |       \
(((func) & ALIF_PINMUX_FUNC_MASK) << ALIF_PINMUX_FUNC_POS))
```

编码引脚复用配置（Pinmux Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口编号（Port Number），范围为 `0–17`。 |
| `pin` | 端口内的引脚编号（Pin Number Within Port），范围为 `0–7`。 |
| `func` | 复用功能（Alternate Function）：`0` 表示 GPIO，`1–7` 表示 AF1–AF7。 |

**返回（Returns）**：返回值（Returns）：用于设备树（Devicetree）的已编码引脚复用值（Pinmux Value）。

<a id="a195b3893d9913e77419e111178923a3d"></a>

### `ALIF_PINMUX_FUNC_MASK`

```c
#define ALIF_PINMUX_FUNC_MASK 0x7U
```

复用功能（Alternate Function）字段的位掩码，共 3 位。

<a id="ab8529e7ad1002e2e112bf1286d4d6c62"></a>

### `ALIF_PINMUX_FUNC_POS`

```c
#define ALIF_PINMUX_FUNC_POS 0U
```

复用功能（Alternate Function）字段的位位置。

<a id="a723a8df1e91c947c25af42db8b9f73dd"></a>

### `ALIF_PINMUX_PIN_MASK`

```c
#define ALIF_PINMUX_PIN_MASK 0x7U
```

引脚编号（Pin Number）字段的位掩码，共 3 位。

<a id="a8c94e09e787a9fb1079e5fbe0aa875d2"></a>

### `ALIF_PINMUX_PIN_POS`

```c
#define ALIF_PINMUX_PIN_POS 3U
```

引脚编号（Pin Number）字段的位位置。

<a id="a280dd67858770ceb0a88153aa29e09da"></a>

### `ALIF_PINMUX_PORT_MASK`

```c
#define ALIF_PINMUX_PORT_MASK 0x1FU
```

端口编号（Port Number）字段的位掩码，共 5 位。

<a id="a5d3f4f922452dc948bcc7727d9875107"></a>

### `ALIF_PINMUX_PORT_POS`

```c
#define ALIF_PINMUX_PORT_POS 6U
```

端口编号（Port Number）字段的位位置。

<a id="aa23df37079d3cb2dfc04e0712ea4b98d"></a>

### `PIN_P0_0__ANA_S0`

```c
#define PIN_P0_0__ANA_S0 ALIF_PINMUX(0, 0, 7)
```

端口（Port）0 的引脚（Pin）0：`ANA_S0`。

<a id="ab88bf5ae68f6b947fbfe57a7a7918a2d"></a>

### `PIN_P0_0__CAM_HSYNC_A`

```c
#define PIN_P0_0__CAM_HSYNC_A ALIF_PINMUX(0, 0, 6)
```

端口（Port）0 的引脚（Pin）0：`CAM_HSYNC_A`。

<a id="a21c0982e31739a0e14d1d5bbe8d28e26"></a>

### `PIN_P0_0__GPIO`

```c
#define PIN_P0_0__GPIO ALIF_PINMUX(0, 0, 0)
```

引脚 `P0.0` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）0：`GPIO`。

<a id="acfd60a41f314cb4771cfeacc0cf01933"></a>

### `PIN_P0_0__I3C_SDA_A`

```c
#define PIN_P0_0__I3C_SDA_A ALIF_PINMUX(0, 0, 3)
```

端口（Port）0 的引脚（Pin）0：`I3C_SDA_A`。

<a id="a6d2a6e4d7178a94d59328d894e147133"></a>

### `PIN_P0_0__LPCAM_HSYNC_B`

```c
#define PIN_P0_0__LPCAM_HSYNC_B ALIF_PINMUX(0, 0, 5)
```

端口（Port）0 的引脚（Pin）0：`LPCAM_HSYNC_B`。

<a id="a4903b693f23df7008874d2c03bd411b3"></a>

### `PIN_P0_0__OSPI0_D0_A`

```c
#define PIN_P0_0__OSPI0_D0_A ALIF_PINMUX(0, 0, 1)
```

端口（Port）0 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="a90cebb445be4e8ec705a6fec4f446849"></a>

### `PIN_P0_0__UART0_RX_A`

```c
#define PIN_P0_0__UART0_RX_A ALIF_PINMUX(0, 0, 2)
```

端口（Port）0 的引脚（Pin）0：`UART0_RX_A`。

<a id="a4dbe11402f4375a20d2999a50dd777b1"></a>

### `PIN_P0_0__UT0_T0_A`

```c
#define PIN_P0_0__UT0_T0_A ALIF_PINMUX(0, 0, 4)
```

端口（Port）0 的引脚（Pin）0：`UT0_T0_A`。

<a id="a9a7460d69ed218e8bfe8e5038ad27f92"></a>

### `PIN_P0_1__ANA_S1`

```c
#define PIN_P0_1__ANA_S1 ALIF_PINMUX(0, 1, 7)
```

端口（Port）0 的引脚（Pin）1：`ANA_S1`。

<a id="a8631817f0da565c3d84cffef0d672c3e"></a>

### `PIN_P0_1__CAM_VSYNC_A`

```c
#define PIN_P0_1__CAM_VSYNC_A ALIF_PINMUX(0, 1, 6)
```

端口（Port）0 的引脚（Pin）1：`CAM_VSYNC_A`。

<a id="a32eb0096f118eeaafa9f397de1d80611"></a>

### `PIN_P0_1__GPIO`

```c
#define PIN_P0_1__GPIO ALIF_PINMUX(0, 1, 0)
```

引脚 `P0.1` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）1：`GPIO`。

<a id="a0fc3ec407b82193623a96299f03c99ee"></a>

### `PIN_P0_1__I3C_SCL_A`

```c
#define PIN_P0_1__I3C_SCL_A ALIF_PINMUX(0, 1, 3)
```

端口（Port）0 的引脚（Pin）1：`I3C_SCL_A`。

<a id="af5e1715d9cc788ce35500c8a3d95a4d5"></a>

### `PIN_P0_1__LPCAM_VSYNC_B`

```c
#define PIN_P0_1__LPCAM_VSYNC_B ALIF_PINMUX(0, 1, 5)
```

端口（Port）0 的引脚（Pin）1：`LPCAM_VSYNC_B`。

<a id="a32e491127585b229574cfeb1fa4cd623"></a>

### `PIN_P0_1__OSPI0_D1_A`

```c
#define PIN_P0_1__OSPI0_D1_A ALIF_PINMUX(0, 1, 1)
```

端口（Port）0 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="ad3c6925fe9f38326a5750bfa5bfca6f1"></a>

### `PIN_P0_1__UART0_TX_A`

```c
#define PIN_P0_1__UART0_TX_A ALIF_PINMUX(0, 1, 2)
```

端口（Port）0 的引脚（Pin）1：`UART0_TX_A`。

<a id="aa03c1f85a5f3e45b2f91fe3c75d7f679"></a>

### `PIN_P0_1__UT0_T1_A`

```c
#define PIN_P0_1__UT0_T1_A ALIF_PINMUX(0, 1, 4)
```

端口（Port）0 的引脚（Pin）1：`UT0_T1_A`。

<a id="a49b9fef54a6baea750aadaa5d80f8b59"></a>

### `PIN_P0_2__ANA_S2`

```c
#define PIN_P0_2__ANA_S2 ALIF_PINMUX(0, 2, 7)
```

端口（Port）0 的引脚（Pin）2：`ANA_S2`。

<a id="af4ca0560e8c5c817b8c21ee225f87b20"></a>

### `PIN_P0_2__CAM_PCLK_A`

```c
#define PIN_P0_2__CAM_PCLK_A ALIF_PINMUX(0, 2, 6)
```

端口（Port）0 的引脚（Pin）2：`CAM_PCLK_A`。

<a id="a4fb3d6992e5eedb80cd18620d13aa3f4"></a>

### `PIN_P0_2__GPIO`

```c
#define PIN_P0_2__GPIO ALIF_PINMUX(0, 2, 0)
```

引脚 `P0.2` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）2：`GPIO`。

<a id="aa2297640ed760699881972950ecde05f"></a>

### `PIN_P0_2__I2C0_SDA_A`

```c
#define PIN_P0_2__I2C0_SDA_A ALIF_PINMUX(0, 2, 3)
```

端口（Port）0 的引脚（Pin）2：`I2C0_SDA_A`。

<a id="a50b34f4621fbb5e99c8e9d60396b6731"></a>

### `PIN_P0_2__LPCAM_PCLK_B`

```c
#define PIN_P0_2__LPCAM_PCLK_B ALIF_PINMUX(0, 2, 5)
```

端口（Port）0 的引脚（Pin）2：`LPCAM_PCLK_B`。

<a id="ad6b5a361d0324dd50534f9c49fbf1849"></a>

### `PIN_P0_2__OSPI0_D2_A`

```c
#define PIN_P0_2__OSPI0_D2_A ALIF_PINMUX(0, 2, 1)
```

端口（Port）0 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="a81dafa48db9962a46d804fe26b4d9aef"></a>

### `PIN_P0_2__UART0_CTS_A`

```c
#define PIN_P0_2__UART0_CTS_A ALIF_PINMUX(0, 2, 2)
```

端口（Port）0 的引脚（Pin）2：`UART0_CTS_A`。

<a id="a1cbbd5723ce8730a93bbfb242ff83ad6"></a>

### `PIN_P0_2__UT1_T0_A`

```c
#define PIN_P0_2__UT1_T0_A ALIF_PINMUX(0, 2, 4)
```

端口（Port）0 的引脚（Pin）2：`UT1_T0_A`。

<a id="acde8c916348493ac12ab8d892f4c4f5d"></a>

### `PIN_P0_3__ANA_S3`

```c
#define PIN_P0_3__ANA_S3 ALIF_PINMUX(0, 3, 7)
```

端口（Port）0 的引脚（Pin）3：`ANA_S3`。

<a id="a7a1274ec637e3efeacab1bc77bd9bf69"></a>

### `PIN_P0_3__CAM_XVCLK_A`

```c
#define PIN_P0_3__CAM_XVCLK_A ALIF_PINMUX(0, 3, 6)
```

端口（Port）0 的引脚（Pin）3：`CAM_XVCLK_A`。

<a id="af6db067634b65894a37a5edbe29654a5"></a>

### `PIN_P0_3__GPIO`

```c
#define PIN_P0_3__GPIO ALIF_PINMUX(0, 3, 0)
```

引脚 `P0.3` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）3：`GPIO`。

<a id="a5c1d69ea260d2b1e17fc42fd9985edf6"></a>

### `PIN_P0_3__I2C0_SCL_A`

```c
#define PIN_P0_3__I2C0_SCL_A ALIF_PINMUX(0, 3, 3)
```

端口（Port）0 的引脚（Pin）3：`I2C0_SCL_A`。

<a id="a165315703135d7f256218ad852d4111b"></a>

### `PIN_P0_3__LPCAM_XVCLK_B`

```c
#define PIN_P0_3__LPCAM_XVCLK_B ALIF_PINMUX(0, 3, 5)
```

端口（Port）0 的引脚（Pin）3：`LPCAM_XVCLK_B`。

<a id="a7dc662eaf7011fadcb4402da22e5af64"></a>

### `PIN_P0_3__OSPI0_D3_A`

```c
#define PIN_P0_3__OSPI0_D3_A ALIF_PINMUX(0, 3, 1)
```

端口（Port）0 的引脚（Pin）3：`OSPI0_D3_A`。

<a id="a37d3d9cde76c648ab549818678cdd02c"></a>

### `PIN_P0_3__UART0_RTS_A`

```c
#define PIN_P0_3__UART0_RTS_A ALIF_PINMUX(0, 3, 2)
```

端口（Port）0 的引脚（Pin）3：`UART0_RTS_A`。

<a id="a92a256fe56cf75cba3a7caf048bc2015"></a>

### `PIN_P0_3__UT1_T1_A`

```c
#define PIN_P0_3__UT1_T1_A ALIF_PINMUX(0, 3, 4)
```

端口（Port）0 的引脚（Pin）3：`UT1_T1_A`。

<a id="aa132663d37ec856ce1cad081dbe0193e"></a>

### `PIN_P0_4__ANA_S4`

```c
#define PIN_P0_4__ANA_S4 ALIF_PINMUX(0, 4, 7)
```

端口（Port）0 的引脚（Pin）4：`ANA_S4`。

<a id="a783d402e95eb758ec44d01ef022000b6"></a>

### `PIN_P0_4__CAN_RXD_B`

```c
#define PIN_P0_4__CAN_RXD_B ALIF_PINMUX(0, 4, 6)
```

端口（Port）0 的引脚（Pin）4：`CAN_RXD_B`。

<a id="a068d5bd9723f62cb6aaa42fba90a9034"></a>

### `PIN_P0_4__GPIO`

```c
#define PIN_P0_4__GPIO ALIF_PINMUX(0, 4, 0)
```

引脚 `P0.4` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）4：`GPIO`。

<a id="a97fb0f48651a63fc62a6450cfd366a26"></a>

### `PIN_P0_4__I2C1_SDA_A`

```c
#define PIN_P0_4__I2C1_SDA_A ALIF_PINMUX(0, 4, 4)
```

端口（Port）0 的引脚（Pin）4：`I2C1_SDA_A`。

<a id="a19f3852ecf10227358ff4e55add2c5a4"></a>

### `PIN_P0_4__OSPI0_D4_A`

```c
#define PIN_P0_4__OSPI0_D4_A ALIF_PINMUX(0, 4, 1)
```

端口（Port）0 的引脚（Pin）4：`OSPI0_D4_A`。

<a id="ab3670c7a57f35ae1a77e2b28d74cb787"></a>

### `PIN_P0_4__PDM_D0_A`

```c
#define PIN_P0_4__PDM_D0_A ALIF_PINMUX(0, 4, 3)
```

端口（Port）0 的引脚（Pin）4：`PDM_D0_A`。

<a id="a86dde3f58b034c8276602748a76ca207"></a>

### `PIN_P0_4__UART1_RX_A`

```c
#define PIN_P0_4__UART1_RX_A ALIF_PINMUX(0, 4, 2)
```

端口（Port）0 的引脚（Pin）4：`UART1_RX_A`。

<a id="a75f02a4170bb4cce26c68473a82ccb23"></a>

### `PIN_P0_4__UT2_T0_A`

```c
#define PIN_P0_4__UT2_T0_A ALIF_PINMUX(0, 4, 5)
```

端口（Port）0 的引脚（Pin）4：`UT2_T0_A`。

<a id="adab066f4e9f8d2741b138fc08b513cf6"></a>

### `PIN_P0_5__ANA_S5`

```c
#define PIN_P0_5__ANA_S5 ALIF_PINMUX(0, 5, 7)
```

端口（Port）0 的引脚（Pin）5：`ANA_S5`。

<a id="a6035a6be92eefbac36961efebbde9b86"></a>

### `PIN_P0_5__CAN_TXD_B`

```c
#define PIN_P0_5__CAN_TXD_B ALIF_PINMUX(0, 5, 6)
```

端口（Port）0 的引脚（Pin）5：`CAN_TXD_B`。

<a id="abd7d8c1f0be68ab38e7e4c7d62e8c88d"></a>

### `PIN_P0_5__GPIO`

```c
#define PIN_P0_5__GPIO ALIF_PINMUX(0, 5, 0)
```

引脚 `P0.5` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）5：`GPIO`。

<a id="a7c3f7fae777efdcfeb26b785b2d29b0d"></a>

### `PIN_P0_5__I2C1_SCL_A`

```c
#define PIN_P0_5__I2C1_SCL_A ALIF_PINMUX(0, 5, 4)
```

端口（Port）0 的引脚（Pin）5：`I2C1_SCL_A`。

<a id="abd9928a8129e505c14e5386176ae6201"></a>

### `PIN_P0_5__OSPI0_D5_A`

```c
#define PIN_P0_5__OSPI0_D5_A ALIF_PINMUX(0, 5, 1)
```

端口（Port）0 的引脚（Pin）5：`OSPI0_D5_A`。

<a id="a7157d108eeba57c6e780f9b622123a88"></a>

### `PIN_P0_5__PDM_C0_A`

```c
#define PIN_P0_5__PDM_C0_A ALIF_PINMUX(0, 5, 3)
```

端口（Port）0 的引脚（Pin）5：`PDM_C0_A`。

<a id="a4c0f43be2ca7617733c39d6956d0898c"></a>

### `PIN_P0_5__UART1_TX_A`

```c
#define PIN_P0_5__UART1_TX_A ALIF_PINMUX(0, 5, 2)
```

端口（Port）0 的引脚（Pin）5：`UART1_TX_A`。

<a id="a96935f674c5309d86939d41a2fb1f7fe"></a>

### `PIN_P0_5__UT2_T1_A`

```c
#define PIN_P0_5__UT2_T1_A ALIF_PINMUX(0, 5, 5)
```

端口（Port）0 的引脚（Pin）5：`UT2_T1_A`。

<a id="aa5907af749639d7948c06be6af51c75e"></a>

### `PIN_P0_6__ANA_S6`

```c
#define PIN_P0_6__ANA_S6 ALIF_PINMUX(0, 6, 7)
```

端口（Port）0 的引脚（Pin）6：`ANA_S6`。

<a id="ab54a6c6132f34080fabde5b5fe055124"></a>

### `PIN_P0_6__CAN_STBY_B`

```c
#define PIN_P0_6__CAN_STBY_B ALIF_PINMUX(0, 6, 6)
```

端口（Port）0 的引脚（Pin）6：`CAN_STBY_B`。

<a id="ad494beaa1230d6528f706e36a8f007cd"></a>

### `PIN_P0_6__GPIO`

```c
#define PIN_P0_6__GPIO ALIF_PINMUX(0, 6, 0)
```

引脚 `P0.6` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）6：`GPIO`。

<a id="ad09e6e851c799927c52951de92b9c1c1"></a>

### `PIN_P0_6__I2C2_SCL_A`

```c
#define PIN_P0_6__I2C2_SCL_A ALIF_PINMUX(0, 6, 4)
```

端口（Port）0 的引脚（Pin）6：`I2C2_SCL_A`。

<a id="ac3fcdf80f9e0d4a961561c32ae9694f9"></a>

### `PIN_P0_6__OSPI0_D6_A`

```c
#define PIN_P0_6__OSPI0_D6_A ALIF_PINMUX(0, 6, 1)
```

端口（Port）0 的引脚（Pin）6：`OSPI0_D6_A`。

<a id="a48eef1d4e9206d1c2eba6cdb40c9ad24"></a>

### `PIN_P0_6__PDM_D1_A`

```c
#define PIN_P0_6__PDM_D1_A ALIF_PINMUX(0, 6, 3)
```

端口（Port）0 的引脚（Pin）6：`PDM_D1_A`。

<a id="a8d2cc812b823a3e6dfc06cb34e57a0aa"></a>

### `PIN_P0_6__UART1_CTS_A`

```c
#define PIN_P0_6__UART1_CTS_A ALIF_PINMUX(0, 6, 2)
```

端口（Port）0 的引脚（Pin）6：`UART1_CTS_A`。

<a id="a3d822add657e1d953b28c0735fd3a9c6"></a>

### `PIN_P0_6__UT3_T0_A`

```c
#define PIN_P0_6__UT3_T0_A ALIF_PINMUX(0, 6, 5)
```

端口（Port）0 的引脚（Pin）6：`UT3_T0_A`。

<a id="a996b9421d83cdf9fc98ee86a07037882"></a>

### `PIN_P0_7__ANA_S7`

```c
#define PIN_P0_7__ANA_S7 ALIF_PINMUX(0, 7, 7)
```

端口（Port）0 的引脚（Pin）7：`ANA_S7`。

<a id="abd2bbc4e66a09b210a11c8180f72757b"></a>

### `PIN_P0_7__CDC_DE_B`

```c
#define PIN_P0_7__CDC_DE_B ALIF_PINMUX(0, 7, 6)
```

端口（Port）0 的引脚（Pin）7：`CDC_DE_B`。

<a id="a3461a7c5af5e46d8e668e1e633c5d721"></a>

### `PIN_P0_7__GPIO`

```c
#define PIN_P0_7__GPIO ALIF_PINMUX(0, 7, 0)
```

引脚 `P0.7` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）7：`GPIO`。

<a id="ad0645a98d86cbc0b4f539a3db1c2856d"></a>

### `PIN_P0_7__I2C2_SDA_A`

```c
#define PIN_P0_7__I2C2_SDA_A ALIF_PINMUX(0, 7, 4)
```

端口（Port）0 的引脚（Pin）7：`I2C2_SDA_A`。

<a id="add0bf72a6fdf8887b88ba696c5f00a40"></a>

### `PIN_P0_7__OSPI0_D7_A`

```c
#define PIN_P0_7__OSPI0_D7_A ALIF_PINMUX(0, 7, 1)
```

端口（Port）0 的引脚（Pin）7：`OSPI0_D7_A`。

<a id="a10ada1c7e06b0a06cd4fb4f5d384329b"></a>

### `PIN_P0_7__PDM_C1_A`

```c
#define PIN_P0_7__PDM_C1_A ALIF_PINMUX(0, 7, 3)
```

端口（Port）0 的引脚（Pin）7：`PDM_C1_A`。

<a id="a8c262122844a7c5ff415d909d982a9b3"></a>

### `PIN_P0_7__UART1_RTS_A`

```c
#define PIN_P0_7__UART1_RTS_A ALIF_PINMUX(0, 7, 2)
```

端口（Port）0 的引脚（Pin）7：`UART1_RTS_A`。

<a id="a9affec2fc3a89563e4528dda6feefeb1"></a>

### `PIN_P0_7__UT3_T1_A`

```c
#define PIN_P0_7__UT3_T1_A ALIF_PINMUX(0, 7, 5)
```

端口（Port）0 的引脚（Pin）7：`UT3_T1_A`。

<a id="a83bf5da94e1c8c6aaae0a857ad5a01d9"></a>

### `PIN_P10_0__CAM_HSYNC_B`

```c
#define PIN_P10_0__CAM_HSYNC_B ALIF_PINMUX(10, 0, 7)
```

端口（Port）10 的引脚（Pin）0：`CAM_HSYNC_B`。

<a id="a8a9136a6f45bc7048124d084209856a1"></a>

### `PIN_P10_0__CDC_D16_A`

```c
#define PIN_P10_0__CDC_D16_A ALIF_PINMUX(10, 0, 6)
```

端口（Port）10 的引脚（Pin）0：`CDC_D16_A`。

<a id="a0d09d7d90b901160d900bde4fe064fa8"></a>

### `PIN_P10_0__GPIO`

```c
#define PIN_P10_0__GPIO ALIF_PINMUX(10, 0, 0)
```

引脚 `P10.0` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）0：`GPIO`。

<a id="a524f9ad04babc125a373f406d1a9657b"></a>

### `PIN_P10_0__LPCAM_HSYNC_A`

```c
#define PIN_P10_0__LPCAM_HSYNC_A ALIF_PINMUX(10, 0, 5)
```

端口（Port）10 的引脚（Pin）0：`LPCAM_HSYNC_A`。

<a id="a3734bb4f47ee59a20e21452ccfad232d"></a>

### `PIN_P10_0__OSPI1_D3_C`

```c
#define PIN_P10_0__OSPI1_D3_C ALIF_PINMUX(10, 0, 1)
```

端口（Port）10 的引脚（Pin）0：`OSPI1_D3_C`。

<a id="ad8c14f987d490c56a883235a78ae2c09"></a>

### `PIN_P10_0__SPI2_SS3_B`

```c
#define PIN_P10_0__SPI2_SS3_B ALIF_PINMUX(10, 0, 3)
```

端口（Port）10 的引脚（Pin）0：`SPI2_SS3_B`。

<a id="ad07d8eb42ddde1260281ea90875d02c7"></a>

### `PIN_P10_0__UART6_DE_B`

```c
#define PIN_P10_0__UART6_DE_B ALIF_PINMUX(10, 0, 2)
```

端口（Port）10 的引脚（Pin）0：`UART6_DE_B`。

<a id="ac8fe2a408fb2fe327cfe9e47fdb2ca94"></a>

### `PIN_P10_0__UT0_T0_C`

```c
#define PIN_P10_0__UT0_T0_C ALIF_PINMUX(10, 0, 4)
```

端口（Port）10 的引脚（Pin）0：`UT0_T0_C`。

<a id="a3588aa90a7de8e8f8d8eb9c272dd72e8"></a>

### `PIN_P10_1__CAM_VSYNC_B`

```c
#define PIN_P10_1__CAM_VSYNC_B ALIF_PINMUX(10, 1, 7)
```

端口（Port）10 的引脚（Pin）1：`CAM_VSYNC_B`。

<a id="a643d326ca3a6a5bb8c56c63f1a2f661c"></a>

### `PIN_P10_1__CDC_D17_A`

```c
#define PIN_P10_1__CDC_D17_A ALIF_PINMUX(10, 1, 6)
```

端口（Port）10 的引脚（Pin）1：`CDC_D17_A`。

<a id="a06764986a0d6fca85d68e1d50d4bbce7"></a>

### `PIN_P10_1__GPIO`

```c
#define PIN_P10_1__GPIO ALIF_PINMUX(10, 1, 0)
```

引脚 `P10.1` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）1：`GPIO`。

<a id="a30b11b254684b83084315e4dd470d183"></a>

### `PIN_P10_1__HSUART0_RX_A`

```c
#define PIN_P10_1__HSUART0_RX_A ALIF_PINMUX(10, 1, 2)
```

端口（Port）10 的引脚（Pin）1：`HSUART0_RX_A`。

<a id="a8d7b7553fd5f6c73212a723b735368e3"></a>

### `PIN_P10_1__LPCAM_VSYNC_A`

```c
#define PIN_P10_1__LPCAM_VSYNC_A ALIF_PINMUX(10, 1, 5)
```

端口（Port）10 的引脚（Pin）1：`LPCAM_VSYNC_A`。

<a id="add14028df60e7b6c4191fa400d7c46fb"></a>

### `PIN_P10_1__LPI2S_SDI_B`

```c
#define PIN_P10_1__LPI2S_SDI_B ALIF_PINMUX(10, 1, 3)
```

端口（Port）10 的引脚（Pin）1：`LPI2S_SDI_B`。

<a id="a435c2a45aacecce2cf55e883dcf989fd"></a>

### `PIN_P10_1__OSPI1_D4_C`

```c
#define PIN_P10_1__OSPI1_D4_C ALIF_PINMUX(10, 1, 1)
```

端口（Port）10 的引脚（Pin）1：`OSPI1_D4_C`。

<a id="abcd471e5e73d4dc91337ee5817fdaee0"></a>

### `PIN_P10_1__UT0_T1_C`

```c
#define PIN_P10_1__UT0_T1_C ALIF_PINMUX(10, 1, 4)
```

端口（Port）10 的引脚（Pin）1：`UT0_T1_C`。

<a id="a6a44353c221bce09c02874838836e462"></a>

### `PIN_P10_2__CAM_PCLK_B`

```c
#define PIN_P10_2__CAM_PCLK_B ALIF_PINMUX(10, 2, 7)
```

端口（Port）10 的引脚（Pin）2：`CAM_PCLK_B`。

<a id="a2e8a45e9598437ab30a116f9211df08f"></a>

### `PIN_P10_2__CDC_D18_A`

```c
#define PIN_P10_2__CDC_D18_A ALIF_PINMUX(10, 2, 6)
```

端口（Port）10 的引脚（Pin）2：`CDC_D18_A`。

<a id="af38abdfdcd535b66e3a06e67dbce6ad2"></a>

### `PIN_P10_2__GPIO`

```c
#define PIN_P10_2__GPIO ALIF_PINMUX(10, 2, 0)
```

引脚 `P10.2` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）2：`GPIO`。

<a id="a2e0d49b16b1002113a57edae8c709276"></a>

### `PIN_P10_2__HSUART0_TX_A`

```c
#define PIN_P10_2__HSUART0_TX_A ALIF_PINMUX(10, 2, 2)
```

端口（Port）10 的引脚（Pin）2：`HSUART0_TX_A`。

<a id="a16f6f6b6c45d33ade034724cc73e512a"></a>

### `PIN_P10_2__LPCAM_PCLK_A`

```c
#define PIN_P10_2__LPCAM_PCLK_A ALIF_PINMUX(10, 2, 5)
```

端口（Port）10 的引脚（Pin）2：`LPCAM_PCLK_A`。

<a id="a3f39b7debe40524149de804280922136"></a>

### `PIN_P10_2__LPI2S_SDO_B`

```c
#define PIN_P10_2__LPI2S_SDO_B ALIF_PINMUX(10, 2, 3)
```

端口（Port）10 的引脚（Pin）2：`LPI2S_SDO_B`。

<a id="a570b682d1bb7049f018ade169cc8d283"></a>

### `PIN_P10_2__OSPI1_D5_C`

```c
#define PIN_P10_2__OSPI1_D5_C ALIF_PINMUX(10, 2, 1)
```

端口（Port）10 的引脚（Pin）2：`OSPI1_D5_C`。

<a id="a19f3416067803dd83dde7f8015bb6e63"></a>

### `PIN_P10_2__UT1_T0_C`

```c
#define PIN_P10_2__UT1_T0_C ALIF_PINMUX(10, 2, 4)
```

端口（Port）10 的引脚（Pin）2：`UT1_T0_C`。

<a id="a7cb3915243855dbbf28f7a99881b0376"></a>

### `PIN_P10_3__CAM_XVCLK_B`

```c
#define PIN_P10_3__CAM_XVCLK_B ALIF_PINMUX(10, 3, 7)
```

端口（Port）10 的引脚（Pin）3：`CAM_XVCLK_B`。

<a id="a772d15bf38887b4c3203eba42cca7767"></a>

### `PIN_P10_3__CDC_D19_A`

```c
#define PIN_P10_3__CDC_D19_A ALIF_PINMUX(10, 3, 6)
```

端口（Port）10 的引脚（Pin）3：`CDC_D19_A`。

<a id="ae8178ae82b29bbb96a413070911232e4"></a>

### `PIN_P10_3__GPIO`

```c
#define PIN_P10_3__GPIO ALIF_PINMUX(10, 3, 0)
```

引脚 `P10.3` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）3：`GPIO`。

<a id="a296690843c2f351d976c14ee140e85b4"></a>

### `PIN_P10_3__HSUART1_RX_A`

```c
#define PIN_P10_3__HSUART1_RX_A ALIF_PINMUX(10, 3, 2)
```

端口（Port）10 的引脚（Pin）3：`HSUART1_RX_A`。

<a id="a03eb3e67619bca555f7fcb517aaff5b9"></a>

### `PIN_P10_3__LPCAM_XVCLK_A`

```c
#define PIN_P10_3__LPCAM_XVCLK_A ALIF_PINMUX(10, 3, 5)
```

端口（Port）10 的引脚（Pin）3：`LPCAM_XVCLK_A`。

<a id="a44ec4fc6bde183ff499d4bb3dd92c01f"></a>

### `PIN_P10_3__LPI2S_SCLK_B`

```c
#define PIN_P10_3__LPI2S_SCLK_B ALIF_PINMUX(10, 3, 3)
```

端口（Port）10 的引脚（Pin）3：`LPI2S_SCLK_B`。

<a id="a69eee953512b4a0f61e3beedfbcfd111"></a>

### `PIN_P10_3__OSPI1_D6_C`

```c
#define PIN_P10_3__OSPI1_D6_C ALIF_PINMUX(10, 3, 1)
```

端口（Port）10 的引脚（Pin）3：`OSPI1_D6_C`。

<a id="ab2a777e85d7bb6c88e8a01147df3577d"></a>

### `PIN_P10_3__UT1_T1_C`

```c
#define PIN_P10_3__UT1_T1_C ALIF_PINMUX(10, 3, 4)
```

端口（Port）10 的引脚（Pin）3：`UT1_T1_C`。

<a id="aed0e35581bee766b0a41e646fdc95b9c"></a>

### `PIN_P10_4__CDC_D20_A`

```c
#define PIN_P10_4__CDC_D20_A ALIF_PINMUX(10, 4, 7)
```

端口（Port）10 的引脚（Pin）4：`CDC_D20_A`。

<a id="a237b7a24bc9b0d43420ddce0d571677d"></a>

### `PIN_P10_4__ETH_TXD0_B`

```c
#define PIN_P10_4__ETH_TXD0_B ALIF_PINMUX(10, 4, 6)
```

端口（Port）10 的引脚（Pin）4：`ETH_TXD0_B`。

<a id="a824864668a22a50a8bd0d30782d6fd35"></a>

### `PIN_P10_4__GPIO`

```c
#define PIN_P10_4__GPIO ALIF_PINMUX(10, 4, 0)
```

引脚 `P10.4` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）4：`GPIO`。

<a id="a159ade6a4cde73ad97a2d6abe2d667c4"></a>

### `PIN_P10_4__HSUART1_TX_A`

```c
#define PIN_P10_4__HSUART1_TX_A ALIF_PINMUX(10, 4, 2)
```

端口（Port）10 的引脚（Pin）4：`HSUART1_TX_A`。

<a id="ad21a0874594d59bbb0b1c4112cb6b66f"></a>

### `PIN_P10_4__I2C0_SDA_D`

```c
#define PIN_P10_4__I2C0_SDA_D ALIF_PINMUX(10, 4, 4)
```

端口（Port）10 的引脚（Pin）4：`I2C0_SDA_D`。

<a id="a99776d853de115507e3601e94ee45c8c"></a>

### `PIN_P10_4__LPI2S_WS_B`

```c
#define PIN_P10_4__LPI2S_WS_B ALIF_PINMUX(10, 4, 3)
```

端口（Port）10 的引脚（Pin）4：`LPI2S_WS_B`。

<a id="a12bed392d874ede18dc9395ca8be773f"></a>

### `PIN_P10_4__OSPI1_D7_C`

```c
#define PIN_P10_4__OSPI1_D7_C ALIF_PINMUX(10, 4, 1)
```

端口（Port）10 的引脚（Pin）4：`OSPI1_D7_C`。

<a id="aef90d2be77688791ce99e819c7760dd7"></a>

### `PIN_P10_4__UT2_T0_C`

```c
#define PIN_P10_4__UT2_T0_C ALIF_PINMUX(10, 4, 5)
```

端口（Port）10 的引脚（Pin）4：`UT2_T0_C`。

<a id="a87b3e92aeb9b612d7709a24007d4f05c"></a>

### `PIN_P10_5__CDC_D21_A`

```c
#define PIN_P10_5__CDC_D21_A ALIF_PINMUX(10, 5, 7)
```

端口（Port）10 的引脚（Pin）5：`CDC_D21_A`。

<a id="acf344432c9e6b30a75f455334ded4ebc"></a>

### `PIN_P10_5__ETH_TXD1_B`

```c
#define PIN_P10_5__ETH_TXD1_B ALIF_PINMUX(10, 5, 6)
```

端口（Port）10 的引脚（Pin）5：`ETH_TXD1_B`。

<a id="a95c7cbebacff815700ac996fb8a9e032"></a>

### `PIN_P10_5__GPIO`

```c
#define PIN_P10_5__GPIO ALIF_PINMUX(10, 5, 0)
```

引脚 `P10.5` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）5：`GPIO`。

<a id="aebb5ee312fdff17857bce74fd872c7e3"></a>

### `PIN_P10_5__I2C0_SCL_D`

```c
#define PIN_P10_5__I2C0_SCL_D ALIF_PINMUX(10, 5, 4)
```

端口（Port）10 的引脚（Pin）5：`I2C0_SCL_D`。

<a id="a5ab587662a9897cf75069890773ce9c7"></a>

### `PIN_P10_5__I2S2_SDI_B`

```c
#define PIN_P10_5__I2S2_SDI_B ALIF_PINMUX(10, 5, 2)
```

端口（Port）10 的引脚（Pin）5：`I2S2_SDI_B`。

<a id="a1c721f6365cb15250855a37579a4924f"></a>

### `PIN_P10_5__SPI3_MISO_B`

```c
#define PIN_P10_5__SPI3_MISO_B ALIF_PINMUX(10, 5, 3)
```

端口（Port）10 的引脚（Pin）5：`SPI3_MISO_B`。

<a id="a65a373a0f9dbf88278afbc75a8a6a3db"></a>

### `PIN_P10_5__UART6_RX_A`

```c
#define PIN_P10_5__UART6_RX_A ALIF_PINMUX(10, 5, 1)
```

端口（Port）10 的引脚（Pin）5：`UART6_RX_A`。

<a id="a428f14aa14e085e23508004490c8fa7f"></a>

### `PIN_P10_5__UT2_T1_C`

```c
#define PIN_P10_5__UT2_T1_C ALIF_PINMUX(10, 5, 5)
```

端口（Port）10 的引脚（Pin）5：`UT2_T1_C`。

<a id="a86336c491101c39955e644402c77bb58"></a>

### `PIN_P10_6__CDC_D22_A`

```c
#define PIN_P10_6__CDC_D22_A ALIF_PINMUX(10, 6, 7)
```

端口（Port）10 的引脚（Pin）6：`CDC_D22_A`。

<a id="aaecd255f11e4e5bb4362f975f144c323"></a>

### `PIN_P10_6__ETH_TXEN_B`

```c
#define PIN_P10_6__ETH_TXEN_B ALIF_PINMUX(10, 6, 6)
```

端口（Port）10 的引脚（Pin）6：`ETH_TXEN_B`。

<a id="a9e78737dc9d1689eb2217db1a12bb927"></a>

### `PIN_P10_6__GPIO`

```c
#define PIN_P10_6__GPIO ALIF_PINMUX(10, 6, 0)
```

引脚 `P10.6` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）6：`GPIO`。

<a id="a7e64c71976bda3c86a7509dfcb6c1a51"></a>

### `PIN_P10_6__I2C1_SDA_D`

```c
#define PIN_P10_6__I2C1_SDA_D ALIF_PINMUX(10, 6, 4)
```

端口（Port）10 的引脚（Pin）6：`I2C1_SDA_D`。

<a id="aee6fed8b3cd016c8affc10ed5621c163"></a>

### `PIN_P10_6__I2S2_SDO_B`

```c
#define PIN_P10_6__I2S2_SDO_B ALIF_PINMUX(10, 6, 2)
```

端口（Port）10 的引脚（Pin）6：`I2S2_SDO_B`。

<a id="a2d2306dee429751af687499f35eaed5e"></a>

### `PIN_P10_6__SPI3_MOSI_B`

```c
#define PIN_P10_6__SPI3_MOSI_B ALIF_PINMUX(10, 6, 3)
```

端口（Port）10 的引脚（Pin）6：`SPI3_MOSI_B`。

<a id="aebdac92a16ef4e6011fef1ada8e2648b"></a>

### `PIN_P10_6__UART6_TX_A`

```c
#define PIN_P10_6__UART6_TX_A ALIF_PINMUX(10, 6, 1)
```

端口（Port）10 的引脚（Pin）6：`UART6_TX_A`。

<a id="a33e003aa8e4dd4154e09fee58daed7c2"></a>

### `PIN_P10_6__UT3_T0_C`

```c
#define PIN_P10_6__UT3_T0_C ALIF_PINMUX(10, 6, 5)
```

端口（Port）10 的引脚（Pin）6：`UT3_T0_C`。

<a id="a71b5b5dddd55df63873b364556c82e19"></a>

### `PIN_P10_7__CDC_D23_A`

```c
#define PIN_P10_7__CDC_D23_A ALIF_PINMUX(10, 7, 6)
```

端口（Port）10 的引脚（Pin）7：`CDC_D23_A`。

<a id="a646299e814c054ff2cf11e254ddd78d0"></a>

### `PIN_P10_7__GPIO`

```c
#define PIN_P10_7__GPIO ALIF_PINMUX(10, 7, 0)
```

引脚 `P10.7` 的复用功能（Alternate Functions）。

端口（Port）10 的引脚（Pin）7：`GPIO`。

<a id="a32a7e8261101544dd558ed5aa2ab694d"></a>

### `PIN_P10_7__I2C1_SCL_D`

```c
#define PIN_P10_7__I2C1_SCL_D ALIF_PINMUX(10, 7, 4)
```

端口（Port）10 的引脚（Pin）7：`I2C1_SCL_D`。

<a id="a1a3e27ebae94f07b9a60c7c56e706454"></a>

### `PIN_P10_7__I2S2_SCLK_B`

```c
#define PIN_P10_7__I2S2_SCLK_B ALIF_PINMUX(10, 7, 2)
```

端口（Port）10 的引脚（Pin）7：`I2S2_SCLK_B`。

<a id="a7b0d3a1498c04034496602535623a576"></a>

### `PIN_P10_7__OSPI1_RXDS0_C`

```c
#define PIN_P10_7__OSPI1_RXDS0_C ALIF_PINMUX(10, 7, 7)
```

端口（Port）10 的引脚（Pin）7：`OSPI1_RXDS0_C`。

<a id="a2511a1e177bde1bf1d9a6a93d9129d66"></a>

### `PIN_P10_7__SPI3_SCLK_B`

```c
#define PIN_P10_7__SPI3_SCLK_B ALIF_PINMUX(10, 7, 3)
```

端口（Port）10 的引脚（Pin）7：`SPI3_SCLK_B`。

<a id="a8181dfa74455316c9fde735d0b3b09e6"></a>

### `PIN_P10_7__UART7_RX_A`

```c
#define PIN_P10_7__UART7_RX_A ALIF_PINMUX(10, 7, 1)
```

端口（Port）10 的引脚（Pin）7：`UART7_RX_A`。

<a id="a941371373e96ad0197810ab5b3b4ccdc"></a>

### `PIN_P10_7__UT3_T1_C`

```c
#define PIN_P10_7__UT3_T1_C ALIF_PINMUX(10, 7, 5)
```

端口（Port）10 的引脚（Pin）7：`UT3_T1_C`。

<a id="adb815f1dd9c2beab4e9ab7f3a5550a34"></a>

### `PIN_P11_0__CDC_D0_B`

```c
#define PIN_P11_0__CDC_D0_B ALIF_PINMUX(11, 0, 7)
```

端口（Port）11 的引脚（Pin）0：`CDC_D0_B`。

<a id="aa131fa2180357840aafa8fa03f3ffa76"></a>

### `PIN_P11_0__ETH_REFCLK_B`

```c
#define PIN_P11_0__ETH_REFCLK_B ALIF_PINMUX(11, 0, 6)
```

端口（Port）11 的引脚（Pin）0：`ETH_REFCLK_B`。

<a id="a6e3ae82413ed22d0b762a03a42b58f07"></a>

### `PIN_P11_0__GPIO`

```c
#define PIN_P11_0__GPIO ALIF_PINMUX(11, 0, 0)
```

引脚 `P11.0` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）0：`GPIO`。

<a id="a02319eba4a567fe789fe6b2474431fa7"></a>

### `PIN_P11_0__I2S2_WS_B`

```c
#define PIN_P11_0__I2S2_WS_B ALIF_PINMUX(11, 0, 3)
```

端口（Port）11 的引脚（Pin）0：`I2S2_WS_B`。

<a id="a3857a5aee76d8744f64fa86feaa89d74"></a>

### `PIN_P11_0__OSPI1_D0_A`

```c
#define PIN_P11_0__OSPI1_D0_A ALIF_PINMUX(11, 0, 1)
```

端口（Port）11 的引脚（Pin）0：`OSPI1_D0_A`。

<a id="a527184616eb9dc3476848e6684261ddb"></a>

### `PIN_P11_0__SPI3_SS0_B`

```c
#define PIN_P11_0__SPI3_SS0_B ALIF_PINMUX(11, 0, 4)
```

端口（Port）11 的引脚（Pin）0：`SPI3_SS0_B`。

<a id="aba1d719c68dd035777d4f3c1c56127fa"></a>

### `PIN_P11_0__UART7_TX_A`

```c
#define PIN_P11_0__UART7_TX_A ALIF_PINMUX(11, 0, 2)
```

端口（Port）11 的引脚（Pin）0：`UART7_TX_A`。

<a id="a8b6b125474bfc5ead883dc6137d6721b"></a>

### `PIN_P11_0__UT4_T0_C`

```c
#define PIN_P11_0__UT4_T0_C ALIF_PINMUX(11, 0, 5)
```

端口（Port）11 的引脚（Pin）0：`UT4_T0_C`。

<a id="ac55f4a9e0beaf4c0d2b69a2b64261ffd"></a>

### `PIN_P11_1__CDC_D1_B`

```c
#define PIN_P11_1__CDC_D1_B ALIF_PINMUX(11, 1, 6)
```

端口（Port）11 的引脚（Pin）1：`CDC_D1_B`。

<a id="aafc326843a27fc885ee7f976dc8efe0e"></a>

### `PIN_P11_1__ETH_MDIO_B`

```c
#define PIN_P11_1__ETH_MDIO_B ALIF_PINMUX(11, 1, 5)
```

端口（Port）11 的引脚（Pin）1：`ETH_MDIO_B`。

<a id="a28c06a03d694d015672f85490df35151"></a>

### `PIN_P11_1__GPIO`

```c
#define PIN_P11_1__GPIO ALIF_PINMUX(11, 1, 0)
```

引脚 `P11.1` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）1：`GPIO`。

<a id="a87648d17a7db98c8f1a8fb66b8012d05"></a>

### `PIN_P11_1__LPSPI_SS5_A`

```c
#define PIN_P11_1__LPSPI_SS5_A ALIF_PINMUX(11, 1, 7)
```

端口（Port）11 的引脚（Pin）1：`LPSPI_SS5_A`。

<a id="aac14a399f11b961ddc1efa6854416877"></a>

### `PIN_P11_1__OSPI1_D1_A`

```c
#define PIN_P11_1__OSPI1_D1_A ALIF_PINMUX(11, 1, 1)
```

端口（Port）11 的引脚（Pin）1：`OSPI1_D1_A`。

<a id="ac3b662da6abd1b9dd9603a97e5e0a215"></a>

### `PIN_P11_1__SPI3_SS1_B`

```c
#define PIN_P11_1__SPI3_SS1_B ALIF_PINMUX(11, 1, 3)
```

端口（Port）11 的引脚（Pin）1：`SPI3_SS1_B`。

<a id="a21e4ae82b997254ce64ba763d5a0d0ae"></a>

### `PIN_P11_1__UART7_DE_A`

```c
#define PIN_P11_1__UART7_DE_A ALIF_PINMUX(11, 1, 2)
```

端口（Port）11 的引脚（Pin）1：`UART7_DE_A`。

<a id="a755b9e846c57bd09ef90b9d4443b37d5"></a>

### `PIN_P11_1__UT4_T1_C`

```c
#define PIN_P11_1__UT4_T1_C ALIF_PINMUX(11, 1, 4)
```

端口（Port）11 的引脚（Pin）1：`UT4_T1_C`。

<a id="a31170ed09fdbc65b8a596c2b89cd9484"></a>

### `PIN_P11_2__CDC_D2_B`

```c
#define PIN_P11_2__CDC_D2_B ALIF_PINMUX(11, 2, 7)
```

端口（Port）11 的引脚（Pin）2：`CDC_D2_B`。

<a id="a38f9beb907a0c3987b87ebb72afa8aed"></a>

### `PIN_P11_2__ETH_MDC_B`

```c
#define PIN_P11_2__ETH_MDC_B ALIF_PINMUX(11, 2, 6)
```

端口（Port）11 的引脚（Pin）2：`ETH_MDC_B`。

<a id="a5cd1d6b953e6db042a10b3c9ddc79dfc"></a>

### `PIN_P11_2__GPIO`

```c
#define PIN_P11_2__GPIO ALIF_PINMUX(11, 2, 0)
```

引脚 `P11.2` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）2：`GPIO`。

<a id="a34107c3b33af1290cca19c62cded8b20"></a>

### `PIN_P11_2__LPPDM_C2_B`

```c
#define PIN_P11_2__LPPDM_C2_B ALIF_PINMUX(11, 2, 3)
```

端口（Port）11 的引脚（Pin）2：`LPPDM_C2_B`。

<a id="a979e7b6dce5f839f31e2f86be7a584cb"></a>

### `PIN_P11_2__OSPI1_D2_A`

```c
#define PIN_P11_2__OSPI1_D2_A ALIF_PINMUX(11, 2, 1)
```

端口（Port）11 的引脚（Pin）2：`OSPI1_D2_A`。

<a id="afcddc8c47c7ed27f1cb7806bb119749b"></a>

### `PIN_P11_2__SPI3_SS2_B`

```c
#define PIN_P11_2__SPI3_SS2_B ALIF_PINMUX(11, 2, 4)
```

端口（Port）11 的引脚（Pin）2：`SPI3_SS2_B`。

<a id="a22ec216eb854b57591ba815ba2d7430f"></a>

### `PIN_P11_2__UART6_DE_A`

```c
#define PIN_P11_2__UART6_DE_A ALIF_PINMUX(11, 2, 2)
```

端口（Port）11 的引脚（Pin）2：`UART6_DE_A`。

<a id="acd886c4095963d69329fdfa4c05a2312"></a>

### `PIN_P11_2__UT5_T0_C`

```c
#define PIN_P11_2__UT5_T0_C ALIF_PINMUX(11, 2, 5)
```

端口（Port）11 的引脚（Pin）2：`UT5_T0_C`。

<a id="ab192580524bad00ab8d4bf5d10d0785c"></a>

### `PIN_P11_3__CDC_D3_B`

```c
#define PIN_P11_3__CDC_D3_B ALIF_PINMUX(11, 3, 7)
```

端口（Port）11 的引脚（Pin）3：`CDC_D3_B`。

<a id="a68166c81dbe880d2806d5c2c06825c48"></a>

### `PIN_P11_3__ETH_RXD0_B`

```c
#define PIN_P11_3__ETH_RXD0_B ALIF_PINMUX(11, 3, 6)
```

端口（Port）11 的引脚（Pin）3：`ETH_RXD0_B`。

<a id="ab0eacf2ec80c89810e5aca5970bd41dd"></a>

### `PIN_P11_3__GPIO`

```c
#define PIN_P11_3__GPIO ALIF_PINMUX(11, 3, 0)
```

引脚 `P11.3` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）3：`GPIO`。

<a id="a49088562bf7428d75ff8129f274ffd3c"></a>

### `PIN_P11_3__LPPDM_C3_B`

```c
#define PIN_P11_3__LPPDM_C3_B ALIF_PINMUX(11, 3, 3)
```

端口（Port）11 的引脚（Pin）3：`LPPDM_C3_B`。

<a id="a89fff5dce962cdd009c9d37d51bc7c16"></a>

### `PIN_P11_3__OSPI1_D3_A`

```c
#define PIN_P11_3__OSPI1_D3_A ALIF_PINMUX(11, 3, 1)
```

端口（Port）11 的引脚（Pin）3：`OSPI1_D3_A`。

<a id="a7aabbf5a6929de1e106d1cd2421975e0"></a>

### `PIN_P11_3__SPI3_SS3_B`

```c
#define PIN_P11_3__SPI3_SS3_B ALIF_PINMUX(11, 3, 4)
```

端口（Port）11 的引脚（Pin）3：`SPI3_SS3_B`。

<a id="ab77ab9d24b65d90edc9d37855f08c6b2"></a>

### `PIN_P11_3__UART5_RX_B`

```c
#define PIN_P11_3__UART5_RX_B ALIF_PINMUX(11, 3, 2)
```

端口（Port）11 的引脚（Pin）3：`UART5_RX_B`。

<a id="ad980a679ec7803b1c294340c3f0610cf"></a>

### `PIN_P11_3__UT5_T1_C`

```c
#define PIN_P11_3__UT5_T1_C ALIF_PINMUX(11, 3, 5)
```

端口（Port）11 的引脚（Pin）3：`UT5_T1_C`。

<a id="a18e9c7e0a390f44e8a26d03cc82b60e0"></a>

### `PIN_P11_4__CDC_D4_B`

```c
#define PIN_P11_4__CDC_D4_B ALIF_PINMUX(11, 4, 7)
```

端口（Port）11 的引脚（Pin）4：`CDC_D4_B`。

<a id="a7af33556f38553a9d080e4cc674dd9ef"></a>

### `PIN_P11_4__ETH_RXD1_B`

```c
#define PIN_P11_4__ETH_RXD1_B ALIF_PINMUX(11, 4, 6)
```

端口（Port）11 的引脚（Pin）4：`ETH_RXD1_B`。

<a id="a967d01834b4cf01973898c49793d1733"></a>

### `PIN_P11_4__GPIO`

```c
#define PIN_P11_4__GPIO ALIF_PINMUX(11, 4, 0)
```

引脚 `P11.4` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）4：`GPIO`。

<a id="afe9676848a3cd8317303074db663e470"></a>

### `PIN_P11_4__LPSPI_MISO_B`

```c
#define PIN_P11_4__LPSPI_MISO_B ALIF_PINMUX(11, 4, 4)
```

端口（Port）11 的引脚（Pin）4：`LPSPI_MISO_B`。

<a id="a61082916fa2ad0e66d622769051916f6"></a>

### `PIN_P11_4__OSPI1_D4_A`

```c
#define PIN_P11_4__OSPI1_D4_A ALIF_PINMUX(11, 4, 1)
```

端口（Port）11 的引脚（Pin）4：`OSPI1_D4_A`。

<a id="a0e6d741081c4a1baa037392b63e97d6d"></a>

### `PIN_P11_4__PDM_C2_B`

```c
#define PIN_P11_4__PDM_C2_B ALIF_PINMUX(11, 4, 3)
```

端口（Port）11 的引脚（Pin）4：`PDM_C2_B`。

<a id="adee30b4484c8f089fc9d1b7b47334c94"></a>

### `PIN_P11_4__UART5_TX_B`

```c
#define PIN_P11_4__UART5_TX_B ALIF_PINMUX(11, 4, 2)
```

端口（Port）11 的引脚（Pin）4：`UART5_TX_B`。

<a id="a8bb3c00b1e19d9cbde2f81ae5b8c37a5"></a>

### `PIN_P11_4__UT6_T0_C`

```c
#define PIN_P11_4__UT6_T0_C ALIF_PINMUX(11, 4, 5)
```

端口（Port）11 的引脚（Pin）4：`UT6_T0_C`。

<a id="a8c42f7452eb11f2b4c8bb538485ef5b1"></a>

### `PIN_P11_5__CDC_D5_B`

```c
#define PIN_P11_5__CDC_D5_B ALIF_PINMUX(11, 5, 7)
```

端口（Port）11 的引脚（Pin）5：`CDC_D5_B`。

<a id="a4e133a5eab6a2d2dd76e444b1b6a64e5"></a>

### `PIN_P11_5__ETH_CRS_DV_B`

```c
#define PIN_P11_5__ETH_CRS_DV_B ALIF_PINMUX(11, 5, 6)
```

端口（Port）11 的引脚（Pin）5：`ETH_CRS_DV_B`。

<a id="acbb30ce67fe4cbccf8cd10925545b331"></a>

### `PIN_P11_5__GPIO`

```c
#define PIN_P11_5__GPIO ALIF_PINMUX(11, 5, 0)
```

引脚 `P11.5` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）5：`GPIO`。

<a id="a16f8c46779f6a257c34af69735254b6c"></a>

### `PIN_P11_5__LPSPI_MOSI_B`

```c
#define PIN_P11_5__LPSPI_MOSI_B ALIF_PINMUX(11, 5, 4)
```

端口（Port）11 的引脚（Pin）5：`LPSPI_MOSI_B`。

<a id="a28db5ce1c956f30d370b9b49cf85daf2"></a>

### `PIN_P11_5__OSPI1_D5_A`

```c
#define PIN_P11_5__OSPI1_D5_A ALIF_PINMUX(11, 5, 1)
```

端口（Port）11 的引脚（Pin）5：`OSPI1_D5_A`。

<a id="aee7f163a9651eb6623eb80185c2426ca"></a>

### `PIN_P11_5__PDM_C3_B`

```c
#define PIN_P11_5__PDM_C3_B ALIF_PINMUX(11, 5, 3)
```

端口（Port）11 的引脚（Pin）5：`PDM_C3_B`。

<a id="ab8c5add28319ad641d59f09b2b38c862"></a>

### `PIN_P11_5__UART6_RX_B`

```c
#define PIN_P11_5__UART6_RX_B ALIF_PINMUX(11, 5, 2)
```

端口（Port）11 的引脚（Pin）5：`UART6_RX_B`。

<a id="ae01c8f68dc1a4a9e0444eac296b91766"></a>

### `PIN_P11_5__UT6_T1_C`

```c
#define PIN_P11_5__UT6_T1_C ALIF_PINMUX(11, 5, 5)
```

端口（Port）11 的引脚（Pin）5：`UT6_T1_C`。

<a id="af7f16b9c0ea55fd1344c40bd660c08ff"></a>

### `PIN_P11_6__CDC_D6_B`

```c
#define PIN_P11_6__CDC_D6_B ALIF_PINMUX(11, 6, 7)
```

端口（Port）11 的引脚（Pin）6：`CDC_D6_B`。

<a id="a84c7faae457bbaf10d69c67c3ceae9ab"></a>

### `PIN_P11_6__ETH_RST_B`

```c
#define PIN_P11_6__ETH_RST_B ALIF_PINMUX(11, 6, 6)
```

端口（Port）11 的引脚（Pin）6：`ETH_RST_B`。

<a id="ab6efcf118d6d87b5bbe36989673b03cb"></a>

### `PIN_P11_6__GPIO`

```c
#define PIN_P11_6__GPIO ALIF_PINMUX(11, 6, 0)
```

引脚 `P11.6` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）6：`GPIO`。

<a id="acfb92bfddbce7875829a9faecbb561e3"></a>

### `PIN_P11_6__LPPDM_D2_B`

```c
#define PIN_P11_6__LPPDM_D2_B ALIF_PINMUX(11, 6, 3)
```

端口（Port）11 的引脚（Pin）6：`LPPDM_D2_B`。

<a id="a65e21d4d8f03542db85c921ae7b3563d"></a>

### `PIN_P11_6__LPSPI_SCLK_B`

```c
#define PIN_P11_6__LPSPI_SCLK_B ALIF_PINMUX(11, 6, 4)
```

端口（Port）11 的引脚（Pin）6：`LPSPI_SCLK_B`。

<a id="adc272402fc3155d4ec2d1e90a001e2aa"></a>

### `PIN_P11_6__OSPI1_D6_A`

```c
#define PIN_P11_6__OSPI1_D6_A ALIF_PINMUX(11, 6, 1)
```

端口（Port）11 的引脚（Pin）6：`OSPI1_D6_A`。

<a id="a51435c722389d9fe457a1bc456a2f464"></a>

### `PIN_P11_6__UART6_TX_B`

```c
#define PIN_P11_6__UART6_TX_B ALIF_PINMUX(11, 6, 2)
```

端口（Port）11 的引脚（Pin）6：`UART6_TX_B`。

<a id="a45bcd40c046279256ea6726b26b1f517"></a>

### `PIN_P11_6__UT7_T0_C`

```c
#define PIN_P11_6__UT7_T0_C ALIF_PINMUX(11, 6, 5)
```

端口（Port）11 的引脚（Pin）6：`UT7_T0_C`。

<a id="a05d9d53114570005812f0d834b1d03db"></a>

### `PIN_P11_7__CDC_D7_B`

```c
#define PIN_P11_7__CDC_D7_B ALIF_PINMUX(11, 7, 7)
```

端口（Port）11 的引脚（Pin）7：`CDC_D7_B`。

<a id="a5f5319f8ed8cbab82055c3e8532781e1"></a>

### `PIN_P11_7__ETH_IRQ_B`

```c
#define PIN_P11_7__ETH_IRQ_B ALIF_PINMUX(11, 7, 6)
```

端口（Port）11 的引脚（Pin）7：`ETH_IRQ_B`。

<a id="ac6bdb71edb24a330dda2258195b07fb8"></a>

### `PIN_P11_7__GPIO`

```c
#define PIN_P11_7__GPIO ALIF_PINMUX(11, 7, 0)
```

引脚 `P11.7` 的复用功能（Alternate Functions）。

端口（Port）11 的引脚（Pin）7：`GPIO`。

<a id="a90bc9c9e0ced226e158826241a2efb1a"></a>

### `PIN_P11_7__LPPDM_D3_B`

```c
#define PIN_P11_7__LPPDM_D3_B ALIF_PINMUX(11, 7, 3)
```

端口（Port）11 的引脚（Pin）7：`LPPDM_D3_B`。

<a id="af59e97786bf73aded8d830a37b48230c"></a>

### `PIN_P11_7__LPSPI_SS_B`

```c
#define PIN_P11_7__LPSPI_SS_B ALIF_PINMUX(11, 7, 4)
```

端口（Port）11 的引脚（Pin）7：`LPSPI_SS_B`。

<a id="a3203e514c7579f68bd0e6bbb34b385f3"></a>

### `PIN_P11_7__OSPI1_D7_A`

```c
#define PIN_P11_7__OSPI1_D7_A ALIF_PINMUX(11, 7, 1)
```

端口（Port）11 的引脚（Pin）7：`OSPI1_D7_A`。

<a id="a92bd8c9cc4a26f5f3466eef2983335e2"></a>

### `PIN_P11_7__UART5_DE_B`

```c
#define PIN_P11_7__UART5_DE_B ALIF_PINMUX(11, 7, 2)
```

端口（Port）11 的引脚（Pin）7：`UART5_DE_B`。

<a id="aabdb02e3be3ad1699860ab1fe53793b9"></a>

### `PIN_P11_7__UT7_T1_C`

```c
#define PIN_P11_7__UT7_T1_C ALIF_PINMUX(11, 7, 5)
```

端口（Port）11 的引脚（Pin）7：`UT7_T1_C`。

<a id="a26ccc2c035ac447ee3d8d524712a0a38"></a>

### `PIN_P12_0__AUDIO_CLK_C`

```c
#define PIN_P12_0__AUDIO_CLK_C ALIF_PINMUX(12, 0, 2)
```

端口（Port）12 的引脚（Pin）0：`AUDIO_CLK_C`。

<a id="a3737b779a1becc91e670e4c43ce98517"></a>

### `PIN_P12_0__CDC_D8_B`

```c
#define PIN_P12_0__CDC_D8_B ALIF_PINMUX(12, 0, 5)
```

端口（Port）12 的引脚（Pin）0：`CDC_D8_B`。

<a id="a65f9bbfcb57ddd6d11d0ec2d070c5883"></a>

### `PIN_P12_0__GPIO`

```c
#define PIN_P12_0__GPIO ALIF_PINMUX(12, 0, 0)
```

引脚 `P12.0` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）0：`GPIO`。

<a id="ac6de26aa62db5a686e7b1ca231455ae2"></a>

### `PIN_P12_0__I2S1_SDI_B`

```c
#define PIN_P12_0__I2S1_SDI_B ALIF_PINMUX(12, 0, 3)
```

端口（Port）12 的引脚（Pin）0：`I2S1_SDI_B`。

<a id="a7ee571ad8643801e9cb9daa958277eef"></a>

### `PIN_P12_0__LPUT0_T0_B`

```c
#define PIN_P12_0__LPUT0_T0_B ALIF_PINMUX(12, 0, 7)
```

端口（Port）12 的引脚（Pin）0：`LPUT0_T0_B`。

<a id="a28ee98d3dca437831995987eec236128"></a>

### `PIN_P12_0__OSPI0_SCLK_C`

```c
#define PIN_P12_0__OSPI0_SCLK_C ALIF_PINMUX(12, 0, 1)
```

端口（Port）12 的引脚（Pin）0：`OSPI0_SCLK_C`。

<a id="a53cacd2a917dba9f73429243bd7aa4b6"></a>

### `PIN_P12_0__OSPI1_D8_B`

```c
#define PIN_P12_0__OSPI1_D8_B ALIF_PINMUX(12, 0, 6)
```

端口（Port）12 的引脚（Pin）0：`OSPI1_D8_B`。

<a id="a2649935928ef15fe94aea023c53db7d0"></a>

### `PIN_P12_0__UT8_T0_C`

```c
#define PIN_P12_0__UT8_T0_C ALIF_PINMUX(12, 0, 4)
```

端口（Port）12 的引脚（Pin）0：`UT8_T0_C`。

<a id="a5ec1ec316fbad9d5102e079167cac94a"></a>

### `PIN_P12_1__CDC_D9_B`

```c
#define PIN_P12_1__CDC_D9_B ALIF_PINMUX(12, 1, 5)
```

端口（Port）12 的引脚（Pin）1：`CDC_D9_B`。

<a id="ace08c69e67060f4a71a24fb30dc509a8"></a>

### `PIN_P12_1__GPIO`

```c
#define PIN_P12_1__GPIO ALIF_PINMUX(12, 1, 0)
```

引脚 `P12.1` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）1：`GPIO`。

<a id="a6350f1bf23731e2613c38513ade47d49"></a>

### `PIN_P12_1__I2S1_SDO_B`

```c
#define PIN_P12_1__I2S1_SDO_B ALIF_PINMUX(12, 1, 3)
```

端口（Port）12 的引脚（Pin）1：`I2S1_SDO_B`。

<a id="a65a2680d02e24df11227fa9ba9abfeea"></a>

### `PIN_P12_1__LPUT0_T1_B`

```c
#define PIN_P12_1__LPUT0_T1_B ALIF_PINMUX(12, 1, 7)
```

端口（Port）12 的引脚（Pin）1：`LPUT0_T1_B`。

<a id="a8221b41b8fb28555926d5b85d15d5e34"></a>

### `PIN_P12_1__OSPI0_SCLKN_C`

```c
#define PIN_P12_1__OSPI0_SCLKN_C ALIF_PINMUX(12, 1, 1)
```

端口（Port）12 的引脚（Pin）1：`OSPI0_SCLKN_C`。

<a id="aa6c3f5c6a65b4a7a910ee860ce2769cd"></a>

### `PIN_P12_1__OSPI1_D9_B`

```c
#define PIN_P12_1__OSPI1_D9_B ALIF_PINMUX(12, 1, 6)
```

端口（Port）12 的引脚（Pin）1：`OSPI1_D9_B`。

<a id="acd826cd6a2b2c9da4090a449c87b096f"></a>

### `PIN_P12_1__UART4_RX_B`

```c
#define PIN_P12_1__UART4_RX_B ALIF_PINMUX(12, 1, 2)
```

端口（Port）12 的引脚（Pin）1：`UART4_RX_B`。

<a id="ac4acb53411c1a6e76660328524557cea"></a>

### `PIN_P12_1__UT8_T1_C`

```c
#define PIN_P12_1__UT8_T1_C ALIF_PINMUX(12, 1, 4)
```

端口（Port）12 的引脚（Pin）1：`UT8_T1_C`。

<a id="a11a8af8b4f8b44ec756ff5227326b660"></a>

### `PIN_P12_2__CDC_D10_B`

```c
#define PIN_P12_2__CDC_D10_B ALIF_PINMUX(12, 2, 5)
```

端口（Port）12 的引脚（Pin）2：`CDC_D10_B`。

<a id="a27c28839016ec48c161a409262ee9fd3"></a>

### `PIN_P12_2__GPIO`

```c
#define PIN_P12_2__GPIO ALIF_PINMUX(12, 2, 0)
```

引脚 `P12.2` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）2：`GPIO`。

<a id="ad949740e8031844551438d452ea9fd98"></a>

### `PIN_P12_2__I2S1_SCLK_B`

```c
#define PIN_P12_2__I2S1_SCLK_B ALIF_PINMUX(12, 2, 3)
```

端口（Port）12 的引脚（Pin）2：`I2S1_SCLK_B`。

<a id="a494c0abfb0d593e0a7ce48942956c678"></a>

### `PIN_P12_2__LPUT1_T0_B`

```c
#define PIN_P12_2__LPUT1_T0_B ALIF_PINMUX(12, 2, 7)
```

端口（Port）12 的引脚（Pin）2：`LPUT1_T0_B`。

<a id="a7dbe1289bb1eb6a5b2a9cfd35966346f"></a>

### `PIN_P12_2__OSPI0_RXDS_C`

```c
#define PIN_P12_2__OSPI0_RXDS_C ALIF_PINMUX(12, 2, 1)
```

端口（Port）12 的引脚（Pin）2：`OSPI0_RXDS_C`。

<a id="a31d26e22fa189f90cc1feaf47255ce58"></a>

### `PIN_P12_2__OSPI1_D10_B`

```c
#define PIN_P12_2__OSPI1_D10_B ALIF_PINMUX(12, 2, 6)
```

端口（Port）12 的引脚（Pin）2：`OSPI1_D10_B`。

<a id="a09c39aeecba670bd260b1c6a9c2206bc"></a>

### `PIN_P12_2__UART4_TX_B`

```c
#define PIN_P12_2__UART4_TX_B ALIF_PINMUX(12, 2, 2)
```

端口（Port）12 的引脚（Pin）2：`UART4_TX_B`。

<a id="a0d7147a61860a86ea3a8e14a6ec7fa1a"></a>

### `PIN_P12_2__UT9_T0_C`

```c
#define PIN_P12_2__UT9_T0_C ALIF_PINMUX(12, 2, 4)
```

端口（Port）12 的引脚（Pin）2：`UT9_T0_C`。

<a id="a4faa710258403e0879ba0b870caca58f"></a>

### `PIN_P12_3__CDC_D11_B`

```c
#define PIN_P12_3__CDC_D11_B ALIF_PINMUX(12, 3, 5)
```

端口（Port）12 的引脚（Pin）3：`CDC_D11_B`。

<a id="af1e08dc87d97396b75f809ae0af2d992"></a>

### `PIN_P12_3__GPIO`

```c
#define PIN_P12_3__GPIO ALIF_PINMUX(12, 3, 0)
```

引脚 `P12.3` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）3：`GPIO`。

<a id="a6ce1e66ccde7c94d44cd3ea5d1fe36a5"></a>

### `PIN_P12_3__I2S1_WS_B`

```c
#define PIN_P12_3__I2S1_WS_B ALIF_PINMUX(12, 3, 3)
```

端口（Port）12 的引脚（Pin）3：`I2S1_WS_B`。

<a id="a2e108a8f92ba50eb7959b099e3e2c976"></a>

### `PIN_P12_3__LPUT1_T1_B`

```c
#define PIN_P12_3__LPUT1_T1_B ALIF_PINMUX(12, 3, 7)
```

端口（Port）12 的引脚（Pin）3：`LPUT1_T1_B`。

<a id="ade9db8b6544f6e122d68929dbe159547"></a>

### `PIN_P12_3__OSPI0_SS0_C`

```c
#define PIN_P12_3__OSPI0_SS0_C ALIF_PINMUX(12, 3, 1)
```

端口（Port）12 的引脚（Pin）3：`OSPI0_SS0_C`。

<a id="a3f62884b90729ebee6430dc16eb6668d"></a>

### `PIN_P12_3__OSPI1_D11_B`

```c
#define PIN_P12_3__OSPI1_D11_B ALIF_PINMUX(12, 3, 6)
```

端口（Port）12 的引脚（Pin）3：`OSPI1_D11_B`。

<a id="a6a3faabad47ea4952ff4ebdf2b590504"></a>

### `PIN_P12_3__UART4_DE_B`

```c
#define PIN_P12_3__UART4_DE_B ALIF_PINMUX(12, 3, 2)
```

端口（Port）12 的引脚（Pin）3：`UART4_DE_B`。

<a id="a5a6847eb83cfba63b1a2f4d9ba263aaf"></a>

### `PIN_P12_3__UT9_T1_C`

```c
#define PIN_P12_3__UT9_T1_C ALIF_PINMUX(12, 3, 4)
```

端口（Port）12 的引脚（Pin）3：`UT9_T1_C`。

<a id="a4ff0a4748c5cda7cc3692d2e07f98df9"></a>

### `PIN_P12_4__CAN_RXD_C`

```c
#define PIN_P12_4__CAN_RXD_C ALIF_PINMUX(12, 4, 4)
```

端口（Port）12 的引脚（Pin）4：`CAN_RXD_C`。

<a id="ae7b3d27ae4e38b66820c3f52ba36aad6"></a>

### `PIN_P12_4__CDC_D12_B`

```c
#define PIN_P12_4__CDC_D12_B ALIF_PINMUX(12, 4, 5)
```

端口（Port）12 的引脚（Pin）4：`CDC_D12_B`。

<a id="adac47965f758c34ea5851e3c7994c684"></a>

### `PIN_P12_4__GPIO`

```c
#define PIN_P12_4__GPIO ALIF_PINMUX(12, 4, 0)
```

引脚 `P12.4` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）4：`GPIO`。

<a id="ad8c7034e3f90fa1f4af3aa7f3f7df47f"></a>

### `PIN_P12_4__LPUT2_T0_B`

```c
#define PIN_P12_4__LPUT2_T0_B ALIF_PINMUX(12, 4, 7)
```

端口（Port）12 的引脚（Pin）4：`LPUT2_T0_B`。

<a id="a68cf8ccca7a0c7a6673f31617965cfc0"></a>

### `PIN_P12_4__OSPI0_SS1_C`

```c
#define PIN_P12_4__OSPI0_SS1_C ALIF_PINMUX(12, 4, 1)
```

端口（Port）12 的引脚（Pin）4：`OSPI0_SS1_C`。

<a id="adc73498c5243f494e5bb9e564ff7d765"></a>

### `PIN_P12_4__OSPI1_D12_B`

```c
#define PIN_P12_4__OSPI1_D12_B ALIF_PINMUX(12, 4, 6)
```

端口（Port）12 的引脚（Pin）4：`OSPI1_D12_B`。

<a id="a127ff0a7e34f5ad312615ef2c902cd19"></a>

### `PIN_P12_4__SPI3_MISO_A`

```c
#define PIN_P12_4__SPI3_MISO_A ALIF_PINMUX(12, 4, 2)
```

端口（Port）12 的引脚（Pin）4：`SPI3_MISO_A`。

<a id="a982db257c715bf8b82cdbb30126527c3"></a>

### `PIN_P12_4__UT10_T0_C`

```c
#define PIN_P12_4__UT10_T0_C ALIF_PINMUX(12, 4, 3)
```

端口（Port）12 的引脚（Pin）4：`UT10_T0_C`。

<a id="ab78bc9a9078a306a8d10f6075ee31e6a"></a>

### `PIN_P12_5__CAN_TXD_C`

```c
#define PIN_P12_5__CAN_TXD_C ALIF_PINMUX(12, 5, 4)
```

端口（Port）12 的引脚（Pin）5：`CAN_TXD_C`。

<a id="a491b6de41ca668cb5d4b0b1d937949f3"></a>

### `PIN_P12_5__CDC_D13_B`

```c
#define PIN_P12_5__CDC_D13_B ALIF_PINMUX(12, 5, 5)
```

端口（Port）12 的引脚（Pin）5：`CDC_D13_B`。

<a id="a56334fbf74f9d40c512b30e00b5d59af"></a>

### `PIN_P12_5__GPIO`

```c
#define PIN_P12_5__GPIO ALIF_PINMUX(12, 5, 0)
```

引脚 `P12.5` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）5：`GPIO`。

<a id="a7b35f4e92b2fedbfd860f43f6b2692d8"></a>

### `PIN_P12_5__HSUART0_RX_B`

```c
#define PIN_P12_5__HSUART0_RX_B ALIF_PINMUX(12, 5, 1)
```

端口（Port）12 的引脚（Pin）5：`HSUART0_RX_B`。

<a id="a4e74f662d9f36465ea5de6bd8aa0d7bd"></a>

### `PIN_P12_5__LPUT2_T1_B`

```c
#define PIN_P12_5__LPUT2_T1_B ALIF_PINMUX(12, 5, 7)
```

端口（Port）12 的引脚（Pin）5：`LPUT2_T1_B`。

<a id="a13897033e94c85375684df80e4b1dbbd"></a>

### `PIN_P12_5__OSPI1_D13_B`

```c
#define PIN_P12_5__OSPI1_D13_B ALIF_PINMUX(12, 5, 6)
```

端口（Port）12 的引脚（Pin）5：`OSPI1_D13_B`。

<a id="a2942041be841278356e235fafad62bb5"></a>

### `PIN_P12_5__SPI3_MOSI_A`

```c
#define PIN_P12_5__SPI3_MOSI_A ALIF_PINMUX(12, 5, 2)
```

端口（Port）12 的引脚（Pin）5：`SPI3_MOSI_A`。

<a id="a841df0bcb5b3a75dbcb72ee691bfbb9d"></a>

### `PIN_P12_5__UT10_T1_C`

```c
#define PIN_P12_5__UT10_T1_C ALIF_PINMUX(12, 5, 3)
```

端口（Port）12 的引脚（Pin）5：`UT10_T1_C`。

<a id="a098e6097b45f7451f6cee83577d0c2c0"></a>

### `PIN_P12_6__CAN_STBY_C`

```c
#define PIN_P12_6__CAN_STBY_C ALIF_PINMUX(12, 6, 4)
```

端口（Port）12 的引脚（Pin）6：`CAN_STBY_C`。

<a id="a24a0e40fe3472fcde95cf3551881764f"></a>

### `PIN_P12_6__CDC_D14_B`

```c
#define PIN_P12_6__CDC_D14_B ALIF_PINMUX(12, 6, 5)
```

端口（Port）12 的引脚（Pin）6：`CDC_D14_B`。

<a id="a39b3372e2a2ef9ebb8f4a621c856089e"></a>

### `PIN_P12_6__GPIO`

```c
#define PIN_P12_6__GPIO ALIF_PINMUX(12, 6, 0)
```

引脚 `P12.6` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）6：`GPIO`。

<a id="a6c48c0632f27aec091208c2031a446a8"></a>

### `PIN_P12_6__HSUART0_TX_B`

```c
#define PIN_P12_6__HSUART0_TX_B ALIF_PINMUX(12, 6, 1)
```

端口（Port）12 的引脚（Pin）6：`HSUART0_TX_B`。

<a id="af15787d2609e9f9aac820e0b5d7ab776"></a>

### `PIN_P12_6__OSPI1_D14_B`

```c
#define PIN_P12_6__OSPI1_D14_B ALIF_PINMUX(12, 6, 6)
```

端口（Port）12 的引脚（Pin）6：`OSPI1_D14_B`。

<a id="a50613420302d014ae2000b32497b0fa0"></a>

### `PIN_P12_6__SPI3_SCLK_A`

```c
#define PIN_P12_6__SPI3_SCLK_A ALIF_PINMUX(12, 6, 2)
```

端口（Port）12 的引脚（Pin）6：`SPI3_SCLK_A`。

<a id="a67e9c045b7cd555d0060e3cc3964dd00"></a>

### `PIN_P12_6__UT11_T0_C`

```c
#define PIN_P12_6__UT11_T0_C ALIF_PINMUX(12, 6, 3)
```

端口（Port）12 的引脚（Pin）6：`UT11_T0_C`。

<a id="a6a19b3ceff99c8c3a88f010ca0e1c9e7"></a>

### `PIN_P12_7__CDC_D15_B`

```c
#define PIN_P12_7__CDC_D15_B ALIF_PINMUX(12, 7, 5)
```

端口（Port）12 的引脚（Pin）7：`CDC_D15_B`。

<a id="a7858fdaeed8a5e6f7fd673f67f8c7fdf"></a>

### `PIN_P12_7__GPIO`

```c
#define PIN_P12_7__GPIO ALIF_PINMUX(12, 7, 0)
```

引脚 `P12.7` 的复用功能（Alternate Functions）。

端口（Port）12 的引脚（Pin）7：`GPIO`。

<a id="a322aa6e6071783ea7ec6c3583031ebf5"></a>

### `PIN_P12_7__HSUART1_RX_B`

```c
#define PIN_P12_7__HSUART1_RX_B ALIF_PINMUX(12, 7, 2)
```

端口（Port）12 的引脚（Pin）7：`HSUART1_RX_B`。

<a id="a3bb480a483bbda13621751c2250647b8"></a>

### `PIN_P12_7__OSPI1_RXDS0_B`

```c
#define PIN_P12_7__OSPI1_RXDS0_B ALIF_PINMUX(12, 7, 1)
```

端口（Port）12 的引脚（Pin）7：`OSPI1_RXDS0_B`。

<a id="a2097584caa2b6da62fe7d6c78a5cd1c5"></a>

### `PIN_P12_7__SPI3_SS0_A`

```c
#define PIN_P12_7__SPI3_SS0_A ALIF_PINMUX(12, 7, 3)
```

端口（Port）12 的引脚（Pin）7：`SPI3_SS0_A`。

<a id="a4cfdb56dc6bec8fa75a054e75534c55b"></a>

### `PIN_P12_7__UT11_T1_C`

```c
#define PIN_P12_7__UT11_T1_C ALIF_PINMUX(12, 7, 4)
```

端口（Port）12 的引脚（Pin）7：`UT11_T1_C`。

<a id="ade80479d70d2edcd9ee57fb11afe656a"></a>

### `PIN_P13_0__CDC_D16_B`

```c
#define PIN_P13_0__CDC_D16_B ALIF_PINMUX(13, 0, 6)
```

端口（Port）13 的引脚（Pin）0：`CDC_D16_B`。

<a id="a15b1cf15c599d1f8b2b01dd0e6f08d70"></a>

### `PIN_P13_0__GPIO`

```c
#define PIN_P13_0__GPIO ALIF_PINMUX(13, 0, 0)
```

引脚 `P13.0` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）0：`GPIO`。

<a id="a2935d09e541aa1b42e37115e7f6f1710"></a>

### `PIN_P13_0__HSUART1_TX_B`

```c
#define PIN_P13_0__HSUART1_TX_B ALIF_PINMUX(13, 0, 2)
```

端口（Port）13 的引脚（Pin）0：`HSUART1_TX_B`。

<a id="a192323c04bd6e93e90c2fc5eacde9a4c"></a>

### `PIN_P13_0__OSPI0_D8_A`

```c
#define PIN_P13_0__OSPI0_D8_A ALIF_PINMUX(13, 0, 7)
```

端口（Port）13 的引脚（Pin）0：`OSPI0_D8_A`。

<a id="a6f3684172961cbfa4e19238b8e07dbae"></a>

### `PIN_P13_0__OSPI1_D0_B`

```c
#define PIN_P13_0__OSPI1_D0_B ALIF_PINMUX(13, 0, 1)
```

端口（Port）13 的引脚（Pin）0：`OSPI1_D0_B`。

<a id="ab3f16dacfc6ee3d596888fc83547b6d0"></a>

### `PIN_P13_0__QEC0_X_C`

```c
#define PIN_P13_0__QEC0_X_C ALIF_PINMUX(13, 0, 4)
```

端口（Port）13 的引脚（Pin）0：`QEC0_X_C`。

<a id="a6a38e02a116d40e4e50869ce0b7e134b"></a>

### `PIN_P13_0__SD_D0_B`

```c
#define PIN_P13_0__SD_D0_B ALIF_PINMUX(13, 0, 5)
```

端口（Port）13 的引脚（Pin）0：`SD_D0_B`。

<a id="aca67dc2ec0398fb093bdd6c27e7b1f90"></a>

### `PIN_P13_0__SPI3_SS1_A`

```c
#define PIN_P13_0__SPI3_SS1_A ALIF_PINMUX(13, 0, 3)
```

端口（Port）13 的引脚（Pin）0：`SPI3_SS1_A`。

<a id="acccdd7840c08eec4de7bd8da9954a2b1"></a>

### `PIN_P13_1__CDC_D17_B`

```c
#define PIN_P13_1__CDC_D17_B ALIF_PINMUX(13, 1, 5)
```

端口（Port）13 的引脚（Pin）1：`CDC_D17_B`。

<a id="ad680890bb2eb8d56701b7cab37482767"></a>

### `PIN_P13_1__GPIO`

```c
#define PIN_P13_1__GPIO ALIF_PINMUX(13, 1, 0)
```

引脚 `P13.1` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）1：`GPIO`。

<a id="a9f2874e10fbd465f2e48b565be1e7334"></a>

### `PIN_P13_1__OSPI0_D9_A`

```c
#define PIN_P13_1__OSPI0_D9_A ALIF_PINMUX(13, 1, 6)
```

端口（Port）13 的引脚（Pin）1：`OSPI0_D9_A`。

<a id="ad532a64dc6a56d13a81016031e4e30ed"></a>

### `PIN_P13_1__OSPI1_D1_B`

```c
#define PIN_P13_1__OSPI1_D1_B ALIF_PINMUX(13, 1, 1)
```

端口（Port）13 的引脚（Pin）1：`OSPI1_D1_B`。

<a id="a931706ab2e90060aa32a96f6cfe20763"></a>

### `PIN_P13_1__QEC0_Y_C`

```c
#define PIN_P13_1__QEC0_Y_C ALIF_PINMUX(13, 1, 3)
```

端口（Port）13 的引脚（Pin）1：`QEC0_Y_C`。

<a id="ac764057ca19fb5947b08f4550e9ec218"></a>

### `PIN_P13_1__SD_D1_B`

```c
#define PIN_P13_1__SD_D1_B ALIF_PINMUX(13, 1, 4)
```

端口（Port）13 的引脚（Pin）1：`SD_D1_B`。

<a id="a0d354def26be8822fdd3a5be9bcd81eb"></a>

### `PIN_P13_1__SPI3_SS2_A`

```c
#define PIN_P13_1__SPI3_SS2_A ALIF_PINMUX(13, 1, 2)
```

端口（Port）13 的引脚（Pin）1：`SPI3_SS2_A`。

<a id="a935b8f0ed9215a2eaa878655a8063cdc"></a>

### `PIN_P13_2__CDC_D18_B`

```c
#define PIN_P13_2__CDC_D18_B ALIF_PINMUX(13, 2, 5)
```

端口（Port）13 的引脚（Pin）2：`CDC_D18_B`。

<a id="aa087d0ade6968b63ff889cd05b975192"></a>

### `PIN_P13_2__GPIO`

```c
#define PIN_P13_2__GPIO ALIF_PINMUX(13, 2, 0)
```

引脚 `P13.2` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）2：`GPIO`。

<a id="ad511c284c7d0da7272fc448afd033f1a"></a>

### `PIN_P13_2__OSPI0_D10_A`

```c
#define PIN_P13_2__OSPI0_D10_A ALIF_PINMUX(13, 2, 6)
```

端口（Port）13 的引脚（Pin）2：`OSPI0_D10_A`。

<a id="a2c27142f1f5b8c87d9464692a792831a"></a>

### `PIN_P13_2__OSPI1_D2_B`

```c
#define PIN_P13_2__OSPI1_D2_B ALIF_PINMUX(13, 2, 1)
```

端口（Port）13 的引脚（Pin）2：`OSPI1_D2_B`。

<a id="a0f7d649cce0dda7a84c33277e2436d2d"></a>

### `PIN_P13_2__QEC0_Z_C`

```c
#define PIN_P13_2__QEC0_Z_C ALIF_PINMUX(13, 2, 3)
```

端口（Port）13 的引脚（Pin）2：`QEC0_Z_C`。

<a id="aa8d14eb950ebc23d1c98a32bfbde5495"></a>

### `PIN_P13_2__SD_D2_B`

```c
#define PIN_P13_2__SD_D2_B ALIF_PINMUX(13, 2, 4)
```

端口（Port）13 的引脚（Pin）2：`SD_D2_B`。

<a id="ab2a0c570e42d5602a13a74fa7667fffe"></a>

### `PIN_P13_2__SPI3_SS3_A`

```c
#define PIN_P13_2__SPI3_SS3_A ALIF_PINMUX(13, 2, 2)
```

端口（Port）13 的引脚（Pin）2：`SPI3_SS3_A`。

<a id="a48ad50a933711f1f56cdb3438a0a8647"></a>

### `PIN_P13_3__CDC_D19_B`

```c
#define PIN_P13_3__CDC_D19_B ALIF_PINMUX(13, 3, 5)
```

端口（Port）13 的引脚（Pin）3：`CDC_D19_B`。

<a id="aa75934dca9e234c0c0a7f284d4095d59"></a>

### `PIN_P13_3__GPIO`

```c
#define PIN_P13_3__GPIO ALIF_PINMUX(13, 3, 0)
```

引脚 `P13.3` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）3：`GPIO`。

<a id="add876fa4d66bc0f9b87b464175b36dfd"></a>

### `PIN_P13_3__OSPI0_D11_A`

```c
#define PIN_P13_3__OSPI0_D11_A ALIF_PINMUX(13, 3, 6)
```

端口（Port）13 的引脚（Pin）3：`OSPI0_D11_A`。

<a id="adf31b9cc8510d1cff024c469a301a57c"></a>

### `PIN_P13_3__OSPI1_D3_B`

```c
#define PIN_P13_3__OSPI1_D3_B ALIF_PINMUX(13, 3, 1)
```

端口（Port）13 的引脚（Pin）3：`OSPI1_D3_B`。

<a id="a0f12c337ed941d3f5e9d470ce92cad5b"></a>

### `PIN_P13_3__QEC1_X_C`

```c
#define PIN_P13_3__QEC1_X_C ALIF_PINMUX(13, 3, 3)
```

端口（Port）13 的引脚（Pin）3：`QEC1_X_C`。

<a id="aabf8b3713a85719ff1f18360bd59030a"></a>

### `PIN_P13_3__SD_D3_B`

```c
#define PIN_P13_3__SD_D3_B ALIF_PINMUX(13, 3, 4)
```

端口（Port）13 的引脚（Pin）3：`SD_D3_B`。

<a id="a3d41bd64e1a820e1cfbf40bb0bc43e21"></a>

### `PIN_P13_3__SPI2_SS3_A`

```c
#define PIN_P13_3__SPI2_SS3_A ALIF_PINMUX(13, 3, 2)
```

端口（Port）13 的引脚（Pin）3：`SPI2_SS3_A`。

<a id="a9897921b8d6b3fafa479463b8420ffad"></a>

### `PIN_P13_4__CDC_D20_B`

```c
#define PIN_P13_4__CDC_D20_B ALIF_PINMUX(13, 4, 5)
```

端口（Port）13 的引脚（Pin）4：`CDC_D20_B`。

<a id="ac67604479bd4bf8d4559a867553df01f"></a>

### `PIN_P13_4__GPIO`

```c
#define PIN_P13_4__GPIO ALIF_PINMUX(13, 4, 0)
```

引脚 `P13.4` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）4：`GPIO`。

<a id="ac316a1a39b1173a2121e2bb05c19d389"></a>

### `PIN_P13_4__LPI2S_SDI_C`

```c
#define PIN_P13_4__LPI2S_SDI_C ALIF_PINMUX(13, 4, 2)
```

端口（Port）13 的引脚（Pin）4：`LPI2S_SDI_C`。

<a id="a73a3e949def6b47cacfbab4c6a001f61"></a>

### `PIN_P13_4__OSPI0_D12_A`

```c
#define PIN_P13_4__OSPI0_D12_A ALIF_PINMUX(13, 4, 6)
```

端口（Port）13 的引脚（Pin）4：`OSPI0_D12_A`。

<a id="abacc197dea6924e35a8aa3e01b6ea71f"></a>

### `PIN_P13_4__OSPI1_D4_B`

```c
#define PIN_P13_4__OSPI1_D4_B ALIF_PINMUX(13, 4, 1)
```

端口（Port）13 的引脚（Pin）4：`OSPI1_D4_B`。

<a id="a6b47ac5773bf1c042efad0d88c963427"></a>

### `PIN_P13_4__QEC1_Y_C`

```c
#define PIN_P13_4__QEC1_Y_C ALIF_PINMUX(13, 4, 3)
```

端口（Port）13 的引脚（Pin）4：`QEC1_Y_C`。

<a id="a8b3d10ffbd5921896369eba148b7d919"></a>

### `PIN_P13_4__SD_D4_B`

```c
#define PIN_P13_4__SD_D4_B ALIF_PINMUX(13, 4, 4)
```

端口（Port）13 的引脚（Pin）4：`SD_D4_B`。

<a id="a7b37cc3713b8987aee7bd378959ff597"></a>

### `PIN_P13_5__CDC_D21_B`

```c
#define PIN_P13_5__CDC_D21_B ALIF_PINMUX(13, 5, 5)
```

端口（Port）13 的引脚（Pin）5：`CDC_D21_B`。

<a id="a5a16054a66476a1e2cbb11e5d6fac9fe"></a>

### `PIN_P13_5__GPIO`

```c
#define PIN_P13_5__GPIO ALIF_PINMUX(13, 5, 0)
```

引脚 `P13.5` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）5：`GPIO`。

<a id="af9307e64da01a7637f0d8df7883181a6"></a>

### `PIN_P13_5__LPI2S_SDO_C`

```c
#define PIN_P13_5__LPI2S_SDO_C ALIF_PINMUX(13, 5, 2)
```

端口（Port）13 的引脚（Pin）5：`LPI2S_SDO_C`。

<a id="ac5cbc603086cf6505246c22cbf5f14d9"></a>

### `PIN_P13_5__OSPI0_D13_A`

```c
#define PIN_P13_5__OSPI0_D13_A ALIF_PINMUX(13, 5, 6)
```

端口（Port）13 的引脚（Pin）5：`OSPI0_D13_A`。

<a id="ac66b3b045737b1b495bd3d43eabd8ab8"></a>

### `PIN_P13_5__OSPI1_D5_B`

```c
#define PIN_P13_5__OSPI1_D5_B ALIF_PINMUX(13, 5, 1)
```

端口（Port）13 的引脚（Pin）5：`OSPI1_D5_B`。

<a id="a35346a9168c7589d1e70fc685d330a71"></a>

### `PIN_P13_5__QEC1_Z_C`

```c
#define PIN_P13_5__QEC1_Z_C ALIF_PINMUX(13, 5, 3)
```

端口（Port）13 的引脚（Pin）5：`QEC1_Z_C`。

<a id="a49bba43520eeb4a0218b252dabe03613"></a>

### `PIN_P13_5__SD_D5_B`

```c
#define PIN_P13_5__SD_D5_B ALIF_PINMUX(13, 5, 4)
```

端口（Port）13 的引脚（Pin）5：`SD_D5_B`。

<a id="aa7eba7adaf6ccecf44391774c204928a"></a>

### `PIN_P13_6__CDC_D22_B`

```c
#define PIN_P13_6__CDC_D22_B ALIF_PINMUX(13, 6, 5)
```

端口（Port）13 的引脚（Pin）6：`CDC_D22_B`。

<a id="a1f29f9ca971127618363127bf894a719"></a>

### `PIN_P13_6__GPIO`

```c
#define PIN_P13_6__GPIO ALIF_PINMUX(13, 6, 0)
```

引脚 `P13.6` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）6：`GPIO`。

<a id="a90861db1213e8bf6795fb97a18cccd90"></a>

### `PIN_P13_6__LPI2S_SCLK_C`

```c
#define PIN_P13_6__LPI2S_SCLK_C ALIF_PINMUX(13, 6, 2)
```

端口（Port）13 的引脚（Pin）6：`LPI2S_SCLK_C`。

<a id="ac9ccede3204288a2fbb4a0eb0100ce46"></a>

### `PIN_P13_6__OSPI0_D14_A`

```c
#define PIN_P13_6__OSPI0_D14_A ALIF_PINMUX(13, 6, 6)
```

端口（Port）13 的引脚（Pin）6：`OSPI0_D14_A`。

<a id="af1c5fffce14d64485deb44043aa66295"></a>

### `PIN_P13_6__OSPI1_D6_B`

```c
#define PIN_P13_6__OSPI1_D6_B ALIF_PINMUX(13, 6, 1)
```

端口（Port）13 的引脚（Pin）6：`OSPI1_D6_B`。

<a id="ab8cba6146de31920e5ca261dd2b5b441"></a>

### `PIN_P13_6__QEC2_X_C`

```c
#define PIN_P13_6__QEC2_X_C ALIF_PINMUX(13, 6, 3)
```

端口（Port）13 的引脚（Pin）6：`QEC2_X_C`。

<a id="a3143074cd350459fac284ef487c3c028"></a>

### `PIN_P13_6__SD_D6_B`

```c
#define PIN_P13_6__SD_D6_B ALIF_PINMUX(13, 6, 4)
```

端口（Port）13 的引脚（Pin）6：`SD_D6_B`。

<a id="a2a8d8fdf7c1da386aec7cf8dc992cfe8"></a>

### `PIN_P13_7__CDC_D23_B`

```c
#define PIN_P13_7__CDC_D23_B ALIF_PINMUX(13, 7, 5)
```

端口（Port）13 的引脚（Pin）7：`CDC_D23_B`。

<a id="a42b654beaf5fb3f6722d69bafbd24beb"></a>

### `PIN_P13_7__GPIO`

```c
#define PIN_P13_7__GPIO ALIF_PINMUX(13, 7, 0)
```

引脚 `P13.7` 的复用功能（Alternate Functions）。

端口（Port）13 的引脚（Pin）7：`GPIO`。

<a id="af1c94f8937b181d916b96fe0ccb385dd"></a>

### `PIN_P13_7__LPI2S_WS_C`

```c
#define PIN_P13_7__LPI2S_WS_C ALIF_PINMUX(13, 7, 2)
```

端口（Port）13 的引脚（Pin）7：`LPI2S_WS_C`。

<a id="a9e813aca4f7934a6d468fc3a994fb043"></a>

### `PIN_P13_7__OSPI0_D15_A`

```c
#define PIN_P13_7__OSPI0_D15_A ALIF_PINMUX(13, 7, 6)
```

端口（Port）13 的引脚（Pin）7：`OSPI0_D15_A`。

<a id="a7f4ac9014f2a64e50e947e63a31fc6a3"></a>

### `PIN_P13_7__OSPI1_D7_B`

```c
#define PIN_P13_7__OSPI1_D7_B ALIF_PINMUX(13, 7, 1)
```

端口（Port）13 的引脚（Pin）7：`OSPI1_D7_B`。

<a id="a16b73c14e00b6780414435fc1f99a008"></a>

### `PIN_P13_7__QEC2_Y_C`

```c
#define PIN_P13_7__QEC2_Y_C ALIF_PINMUX(13, 7, 3)
```

端口（Port）13 的引脚（Pin）7：`QEC2_Y_C`。

<a id="a8df4b1ab413c637d7aa5e8f6601ab5a4"></a>

### `PIN_P13_7__SD_D7_B`

```c
#define PIN_P13_7__SD_D7_B ALIF_PINMUX(13, 7, 4)
```

端口（Port）13 的引脚（Pin）7：`SD_D7_B`。

<a id="a1cbf1f2e853f2d489eeb2d2a1daa54b1"></a>

### `PIN_P14_0__GPIO`

```c
#define PIN_P14_0__GPIO ALIF_PINMUX(14, 0, 0)
```

引脚 `P14.0` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）0：`GPIO`。

<a id="a3d35e77d076c4bc3f284a0270bddbbdf"></a>

### `PIN_P14_0__LFRC_OUT_B`

```c
#define PIN_P14_0__LFRC_OUT_B ALIF_PINMUX(14, 0, 5)
```

端口（Port）14 的引脚（Pin）0：`LFRC_OUT_B`。

<a id="a5ca2782d59baafba4a2e0295e3333753"></a>

### `PIN_P14_0__OSPI1_SCLK_B`

```c
#define PIN_P14_0__OSPI1_SCLK_B ALIF_PINMUX(14, 0, 1)
```

端口（Port）14 的引脚（Pin）0：`OSPI1_SCLK_B`。

<a id="a49aa7894468a1a50107ed45dba960049"></a>

### `PIN_P14_0__QEC2_Z_C`

```c
#define PIN_P14_0__QEC2_Z_C ALIF_PINMUX(14, 0, 3)
```

端口（Port）14 的引脚（Pin）0：`QEC2_Z_C`。

<a id="a4b5bd52ebe29d09d5aa76da653578978"></a>

### `PIN_P14_0__SD_CMD_B`

```c
#define PIN_P14_0__SD_CMD_B ALIF_PINMUX(14, 0, 4)
```

端口（Port）14 的引脚（Pin）0：`SD_CMD_B`。

<a id="a49b4d7291de66dc53a8b63746549b18d"></a>

### `PIN_P14_0__UART6_RX_C`

```c
#define PIN_P14_0__UART6_RX_C ALIF_PINMUX(14, 0, 2)
```

端口（Port）14 的引脚（Pin）0：`UART6_RX_C`。

<a id="a1ed2a56d90d62dc6537ca251a51d9f11"></a>

### `PIN_P14_1__APLL_OUT_C`

```c
#define PIN_P14_1__APLL_OUT_C ALIF_PINMUX(14, 1, 3)
```

端口（Port）14 的引脚（Pin）1：`APLL_OUT_C`。

<a id="a04f061154e4fe1cbc3bca5d7f66c79be"></a>

### `PIN_P14_1__GPIO`

```c
#define PIN_P14_1__GPIO ALIF_PINMUX(14, 1, 0)
```

引脚 `P14.1` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）1：`GPIO`。

<a id="a5309e7ad0e247402ec4f4668790c0f16"></a>

### `PIN_P14_1__LFXO_OUT_B`

```c
#define PIN_P14_1__LFXO_OUT_B ALIF_PINMUX(14, 1, 6)
```

端口（Port）14 的引脚（Pin）1：`LFXO_OUT_B`。

<a id="a20c4ce2960204844c6521a351c597ca5"></a>

### `PIN_P14_1__OSPI1_SCLKN_B`

```c
#define PIN_P14_1__OSPI1_SCLKN_B ALIF_PINMUX(14, 1, 1)
```

端口（Port）14 的引脚（Pin）1：`OSPI1_SCLKN_B`。

<a id="a1dd67381d31bf2a77432474b28c96171"></a>

### `PIN_P14_1__QEC3_X_C`

```c
#define PIN_P14_1__QEC3_X_C ALIF_PINMUX(14, 1, 4)
```

端口（Port）14 的引脚（Pin）1：`QEC3_X_C`。

<a id="a696067713fdb1bcaae580f9243fc532f"></a>

### `PIN_P14_1__SD_CLK_B`

```c
#define PIN_P14_1__SD_CLK_B ALIF_PINMUX(14, 1, 5)
```

端口（Port）14 的引脚（Pin）1：`SD_CLK_B`。

<a id="ad6eaa8dd8c5be5317ba78a60f4e52de8"></a>

### `PIN_P14_1__UART6_TX_C`

```c
#define PIN_P14_1__UART6_TX_C ALIF_PINMUX(14, 1, 2)
```

端口（Port）14 的引脚（Pin）1：`UART6_TX_C`。

<a id="a540585afd2427a265053f4033f1d0e92"></a>

### `PIN_P14_2__GPIO`

```c
#define PIN_P14_2__GPIO ALIF_PINMUX(14, 2, 0)
```

引脚 `P14.2` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）2：`GPIO`。

<a id="a33da038373513a8395f48823b06c3111"></a>

### `PIN_P14_2__LPI3C_SDA_C`

```c
#define PIN_P14_2__LPI3C_SDA_C ALIF_PINMUX(14, 2, 3)
```

端口（Port）14 的引脚（Pin）2：`LPI3C_SDA_C`。

<a id="aa17bd78fd8b8190e613d199761128602"></a>

### `PIN_P14_2__LPSPI_SS5_B`

```c
#define PIN_P14_2__LPSPI_SS5_B ALIF_PINMUX(14, 2, 6)
```

端口（Port）14 的引脚（Pin）2：`LPSPI_SS5_B`。

<a id="a7e8dfedc5e752f15125b114555451178"></a>

### `PIN_P14_2__OSPI1_SS0_B`

```c
#define PIN_P14_2__OSPI1_SS0_B ALIF_PINMUX(14, 2, 1)
```

端口（Port）14 的引脚（Pin）2：`OSPI1_SS0_B`。

<a id="ad04b7586c46f82324cd494ded92f1734"></a>

### `PIN_P14_2__QEC3_Y_C`

```c
#define PIN_P14_2__QEC3_Y_C ALIF_PINMUX(14, 2, 4)
```

端口（Port）14 的引脚（Pin）2：`QEC3_Y_C`。

<a id="a2b2afb838b4fc24227e5dc587b692938"></a>

### `PIN_P14_2__SD_RST_B`

```c
#define PIN_P14_2__SD_RST_B ALIF_PINMUX(14, 2, 5)
```

端口（Port）14 的引脚（Pin）2：`SD_RST_B`。

<a id="a94d4d9dd458f09d2f49db1bbe739fc89"></a>

### `PIN_P14_2__UART7_RX_C`

```c
#define PIN_P14_2__UART7_RX_C ALIF_PINMUX(14, 2, 2)
```

端口（Port）14 的引脚（Pin）2：`UART7_RX_C`。

<a id="a143e7d370589dab01e92dfbd48336c85"></a>

### `PIN_P14_3__GPIO`

```c
#define PIN_P14_3__GPIO ALIF_PINMUX(14, 3, 0)
```

引脚 `P14.3` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）3：`GPIO`。

<a id="a2c5f5373c98d4d1efb13e4b6f4650f00"></a>

### `PIN_P14_3__LPI3C_SCL_C`

```c
#define PIN_P14_3__LPI3C_SCL_C ALIF_PINMUX(14, 3, 3)
```

端口（Port）14 的引脚（Pin）3：`LPI3C_SCL_C`。

<a id="abd81a8224aa0eaeae2471a989abe24a5"></a>

### `PIN_P14_3__OSPI1_SS1_B`

```c
#define PIN_P14_3__OSPI1_SS1_B ALIF_PINMUX(14, 3, 1)
```

端口（Port）14 的引脚（Pin）3：`OSPI1_SS1_B`。

<a id="ae80e3c69274bbe71007d2ab84d822328"></a>

### `PIN_P14_3__QEC3_Z_C`

```c
#define PIN_P14_3__QEC3_Z_C ALIF_PINMUX(14, 3, 4)
```

端口（Port）14 的引脚（Pin）3：`QEC3_Z_C`。

<a id="a82039aa8a98ed309e89ca8996bd4d3fa"></a>

### `PIN_P14_3__UART7_TX_C`

```c
#define PIN_P14_3__UART7_TX_C ALIF_PINMUX(14, 3, 2)
```

端口（Port）14 的引脚（Pin）3：`UART7_TX_C`。

<a id="acee71b28db5d2fa95abfe302d44f5b25"></a>

### `PIN_P14_4__CMP3_OUT_B`

```c
#define PIN_P14_4__CMP3_OUT_B ALIF_PINMUX(14, 4, 1)
```

端口（Port）14 的引脚（Pin）4：`CMP3_OUT_B`。

<a id="ad5113822126585fe88b5f8ecafc2143f"></a>

### `PIN_P14_4__FAULT0_C`

```c
#define PIN_P14_4__FAULT0_C ALIF_PINMUX(14, 4, 3)
```

端口（Port）14 的引脚（Pin）4：`FAULT0_C`。

<a id="a394dc4720bf0af77b3a1bc0e1fd3bbd9"></a>

### `PIN_P14_4__GPIO`

```c
#define PIN_P14_4__GPIO ALIF_PINMUX(14, 4, 0)
```

引脚 `P14.4` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）4：`GPIO`。

<a id="afdd8de79f83cd6eeb27882eb915c1837"></a>

### `PIN_P14_4__LPSPI_SS1_B`

```c
#define PIN_P14_4__LPSPI_SS1_B ALIF_PINMUX(14, 4, 5)
```

端口（Port）14 的引脚（Pin）4：`LPSPI_SS1_B`。

<a id="a241b5f26d5b27d9713824727bbb56f67"></a>

### `PIN_P14_4__OSPI1_RXDS1_A`

```c
#define PIN_P14_4__OSPI1_RXDS1_A ALIF_PINMUX(14, 4, 4)
```

端口（Port）14 的引脚（Pin）4：`OSPI1_RXDS1_A`。

<a id="a6c6af82925d4c50ce7c0c50ace329326"></a>

### `PIN_P14_4__SPI1_MISO_C`

```c
#define PIN_P14_4__SPI1_MISO_C ALIF_PINMUX(14, 4, 2)
```

端口（Port）14 的引脚（Pin）4：`SPI1_MISO_C`。

<a id="aac41aa725e8c16a0b28a17fce43d6f11"></a>

### `PIN_P14_5__CMP2_OUT_B`

```c
#define PIN_P14_5__CMP2_OUT_B ALIF_PINMUX(14, 5, 1)
```

端口（Port）14 的引脚（Pin）5：`CMP2_OUT_B`。

<a id="af36139ef2ab829cbcd2e0417bcd3246e"></a>

### `PIN_P14_5__FAULT1_C`

```c
#define PIN_P14_5__FAULT1_C ALIF_PINMUX(14, 5, 3)
```

端口（Port）14 的引脚（Pin）5：`FAULT1_C`。

<a id="a8a95826bd89110378f6bf0885216d120"></a>

### `PIN_P14_5__GPIO`

```c
#define PIN_P14_5__GPIO ALIF_PINMUX(14, 5, 0)
```

引脚 `P14.5` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）5：`GPIO`。

<a id="a9cc5380a5984b10a1630f8755985fa71"></a>

### `PIN_P14_5__LPSPI_SS2_B`

```c
#define PIN_P14_5__LPSPI_SS2_B ALIF_PINMUX(14, 5, 5)
```

端口（Port）14 的引脚（Pin）5：`LPSPI_SS2_B`。

<a id="a385b2d31c016c30bd67c4cdba1011ead"></a>

### `PIN_P14_5__OSPI0_RXDS1_B`

```c
#define PIN_P14_5__OSPI0_RXDS1_B ALIF_PINMUX(14, 5, 4)
```

端口（Port）14 的引脚（Pin）5：`OSPI0_RXDS1_B`。

<a id="a2dc20aaefaebb6f454c03453904c1f42"></a>

### `PIN_P14_5__SPI1_MOSI_C`

```c
#define PIN_P14_5__SPI1_MOSI_C ALIF_PINMUX(14, 5, 2)
```

端口（Port）14 的引脚（Pin）5：`SPI1_MOSI_C`。

<a id="a0cb8498d547cb5b864d008a8744612c6"></a>

### `PIN_P14_6__CMP1_OUT_B`

```c
#define PIN_P14_6__CMP1_OUT_B ALIF_PINMUX(14, 6, 1)
```

端口（Port）14 的引脚（Pin）6：`CMP1_OUT_B`。

<a id="a7bc7b758724c5f381b917faa265a06cd"></a>

### `PIN_P14_6__FAULT2_C`

```c
#define PIN_P14_6__FAULT2_C ALIF_PINMUX(14, 6, 3)
```

端口（Port）14 的引脚（Pin）6：`FAULT2_C`。

<a id="a995ed7190261b83cede4eab37c6afdd8"></a>

### `PIN_P14_6__GPIO`

```c
#define PIN_P14_6__GPIO ALIF_PINMUX(14, 6, 0)
```

引脚 `P14.6` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）6：`GPIO`。

<a id="a639129b2cbcb7a39509533c748b719d2"></a>

### `PIN_P14_6__LPSPI_SS3_B`

```c
#define PIN_P14_6__LPSPI_SS3_B ALIF_PINMUX(14, 6, 5)
```

端口（Port）14 的引脚（Pin）6：`LPSPI_SS3_B`。

<a id="a52a6a685be88180e360e1a3b29a327f6"></a>

### `PIN_P14_6__OSPI1_D15_B`

```c
#define PIN_P14_6__OSPI1_D15_B ALIF_PINMUX(14, 6, 4)
```

端口（Port）14 的引脚（Pin）6：`OSPI1_D15_B`。

<a id="a117d335a297134a4af1f3e7a83bf15af"></a>

### `PIN_P14_6__SPI1_SCLK_C`

```c
#define PIN_P14_6__SPI1_SCLK_C ALIF_PINMUX(14, 6, 2)
```

端口（Port）14 的引脚（Pin）6：`SPI1_SCLK_C`。

<a id="a3c9b1256f40856381742ee1f656eb59f"></a>

### `PIN_P14_7__APLL_OUT_B`

```c
#define PIN_P14_7__APLL_OUT_B ALIF_PINMUX(14, 7, 4)
```

端口（Port）14 的引脚（Pin）7：`APLL_OUT_B`。

<a id="afa8df9c3a93767723e25958f5c37882c"></a>

### `PIN_P14_7__CMP0_OUT_B`

```c
#define PIN_P14_7__CMP0_OUT_B ALIF_PINMUX(14, 7, 1)
```

端口（Port）14 的引脚（Pin）7：`CMP0_OUT_B`。

<a id="a16d1531f14b3fd9138d362bef5e91339"></a>

### `PIN_P14_7__FAULT3_C`

```c
#define PIN_P14_7__FAULT3_C ALIF_PINMUX(14, 7, 3)
```

端口（Port）14 的引脚（Pin）7：`FAULT3_C`。

<a id="abd4fb434a55d691d2fa3a5267187ae9c"></a>

### `PIN_P14_7__GPIO`

```c
#define PIN_P14_7__GPIO ALIF_PINMUX(14, 7, 0)
```

引脚 `P14.7` 的复用功能（Alternate Functions）。

端口（Port）14 的引脚（Pin）7：`GPIO`。

<a id="ad43c40c9a544ed09eb334d772f8ce862"></a>

### `PIN_P14_7__LPSPI_SS4_B`

```c
#define PIN_P14_7__LPSPI_SS4_B ALIF_PINMUX(14, 7, 5)
```

端口（Port）14 的引脚（Pin）7：`LPSPI_SS4_B`。

<a id="aebe3294759cc2654a4dca1a81002bb03"></a>

### `PIN_P14_7__SPI1_SS0_C`

```c
#define PIN_P14_7__SPI1_SS0_C ALIF_PINMUX(14, 7, 2)
```

端口（Port）14 的引脚（Pin）7：`SPI1_SS0_C`。

<a id="a482ff296b3458b8da397d102f23bba34"></a>

### `PIN_P15_0__LPGPIO`

```c
#define PIN_P15_0__LPGPIO ALIF_PINMUX(15, 0, 0)
```

引脚 `P15.0` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）0：`LPGPIO`。

<a id="a87b1f1b590da3e225affcf5e22e0fde0"></a>

### `PIN_P15_1__LPGPIO`

```c
#define PIN_P15_1__LPGPIO ALIF_PINMUX(15, 1, 0)
```

引脚 `P15.1` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）1：`LPGPIO`。

<a id="a751069828ce828f0fde9e133d1cff1d8"></a>

### `PIN_P15_2__LPGPIO`

```c
#define PIN_P15_2__LPGPIO ALIF_PINMUX(15, 2, 0)
```

引脚 `P15.2` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）2：`LPGPIO`。

<a id="a53daed0b63bb612e52340e3d0bff6469"></a>

### `PIN_P15_3__LPGPIO`

```c
#define PIN_P15_3__LPGPIO ALIF_PINMUX(15, 3, 0)
```

引脚 `P15.3` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）3：`LPGPIO`。

<a id="a6d2b399ef4fc71146b02683ad8b922f4"></a>

### `PIN_P15_4__LPGPIO`

```c
#define PIN_P15_4__LPGPIO ALIF_PINMUX(15, 4, 0)
```

引脚 `P15.4` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）4：`LPGPIO`。

<a id="a59a4b7046f20d806ef14f465199ec07b"></a>

### `PIN_P15_5__LPGPIO`

```c
#define PIN_P15_5__LPGPIO ALIF_PINMUX(15, 5, 0)
```

引脚 `P15.5` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）5：`LPGPIO`。

<a id="adc15a08c93aafd26cea6eb6deced95a9"></a>

### `PIN_P15_6__LPGPIO`

```c
#define PIN_P15_6__LPGPIO ALIF_PINMUX(15, 6, 0)
```

引脚 `P15.6` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）6：`LPGPIO`。

<a id="a345e070b3f7cc4176a2d730829b248b9"></a>

### `PIN_P15_7__LPGPIO`

```c
#define PIN_P15_7__LPGPIO ALIF_PINMUX(15, 7, 0)
```

引脚 `P15.7` 的复用功能（Alternate Functions）。

端口（Port）15 的引脚（Pin）7：`LPGPIO`。

<a id="abfb6c484ca20ec0b083a4413b4dc3fc3"></a>

### `PIN_P16_0__GPIO`

```c
#define PIN_P16_0__GPIO ALIF_PINMUX(16, 0, 0)
```

引脚 `P16.0` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）0：`GPIO`。

<a id="a485d492961fdff6770233e4f41da383f"></a>

### `PIN_P16_0__OSPI0_D8_B`

```c
#define PIN_P16_0__OSPI0_D8_B ALIF_PINMUX(16, 0, 1)
```

端口（Port）16 的引脚（Pin）0：`OSPI0_D8_B`。

<a id="a02cd3d03d139cbf6522ab0cef61f665e"></a>

### `PIN_P16_1__GPIO`

```c
#define PIN_P16_1__GPIO ALIF_PINMUX(16, 1, 0)
```

引脚 `P16.1` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）1：`GPIO`。

<a id="a6ae160d4439825219291f521bdd5e378"></a>

### `PIN_P16_1__OSPI0_D9_B`

```c
#define PIN_P16_1__OSPI0_D9_B ALIF_PINMUX(16, 1, 1)
```

端口（Port）16 的引脚（Pin）1：`OSPI0_D9_B`。

<a id="aaf71f322736ae2427cd663318492a956"></a>

### `PIN_P16_2__GPIO`

```c
#define PIN_P16_2__GPIO ALIF_PINMUX(16, 2, 0)
```

引脚 `P16.2` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）2：`GPIO`。

<a id="ad1434cab1444cc0537314b8df3661b9b"></a>

### `PIN_P16_2__OSPI0_D10_B`

```c
#define PIN_P16_2__OSPI0_D10_B ALIF_PINMUX(16, 2, 1)
```

端口（Port）16 的引脚（Pin）2：`OSPI0_D10_B`。

<a id="a619c9544bbcf8b2e74be37cc140e097c"></a>

### `PIN_P16_3__GPIO`

```c
#define PIN_P16_3__GPIO ALIF_PINMUX(16, 3, 0)
```

引脚 `P16.3` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）3：`GPIO`。

<a id="a532efee68413e7a1213ca76dbd759b48"></a>

### `PIN_P16_3__OSPI0_D11_B`

```c
#define PIN_P16_3__OSPI0_D11_B ALIF_PINMUX(16, 3, 1)
```

端口（Port）16 的引脚（Pin）3：`OSPI0_D11_B`。

<a id="af904fe04f416c076c1bae945cd29ea09"></a>

### `PIN_P16_4__GPIO`

```c
#define PIN_P16_4__GPIO ALIF_PINMUX(16, 4, 0)
```

引脚 `P16.4` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）4：`GPIO`。

<a id="a28722750644304419fc81705c277904e"></a>

### `PIN_P16_4__OSPI0_D12_B`

```c
#define PIN_P16_4__OSPI0_D12_B ALIF_PINMUX(16, 4, 1)
```

端口（Port）16 的引脚（Pin）4：`OSPI0_D12_B`。

<a id="a44a5ae5fa1c9d027d52bed5b6e7ef6db"></a>

### `PIN_P16_5__GPIO`

```c
#define PIN_P16_5__GPIO ALIF_PINMUX(16, 5, 0)
```

引脚 `P16.5` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）5：`GPIO`。

<a id="adba8b9b4957cbfeb71144b05887ac040"></a>

### `PIN_P16_5__OSPI0_D13_B`

```c
#define PIN_P16_5__OSPI0_D13_B ALIF_PINMUX(16, 5, 1)
```

端口（Port）16 的引脚（Pin）5：`OSPI0_D13_B`。

<a id="a123ae5eee36c06a449bccf886b48806b"></a>

### `PIN_P16_6__GPIO`

```c
#define PIN_P16_6__GPIO ALIF_PINMUX(16, 6, 0)
```

引脚 `P16.6` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）6：`GPIO`。

<a id="a351e28f4ffc15bc8cbfc8febd24f6872"></a>

### `PIN_P16_6__OSPI0_D14_B`

```c
#define PIN_P16_6__OSPI0_D14_B ALIF_PINMUX(16, 6, 1)
```

端口（Port）16 的引脚（Pin）6：`OSPI0_D14_B`。

<a id="ab7acb4286b257f94f3a0051ae863dfa6"></a>

### `PIN_P16_7__GPIO`

```c
#define PIN_P16_7__GPIO ALIF_PINMUX(16, 7, 0)
```

引脚 `P16.7` 的复用功能（Alternate Functions）。

端口（Port）16 的引脚（Pin）7：`GPIO`。

<a id="aa87bbb168ea3a41c76cbd437d02bcfbe"></a>

### `PIN_P16_7__OSPI0_D15_B`

```c
#define PIN_P16_7__OSPI0_D15_B ALIF_PINMUX(16, 7, 1)
```

端口（Port）16 的引脚（Pin）7：`OSPI0_D15_B`。

<a id="a5c98a4c40236de006b32484b485bea65"></a>

### `PIN_P17_0__GPIO`

```c
#define PIN_P17_0__GPIO ALIF_PINMUX(17, 0, 0)
```

引脚 `P17.0` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）0：`GPIO`。

<a id="a63fc4d6d872ca13ab41154620c7cb6a3"></a>

### `PIN_P17_0__OSPI1_D8_C`

```c
#define PIN_P17_0__OSPI1_D8_C ALIF_PINMUX(17, 0, 1)
```

端口（Port）17 的引脚（Pin）0：`OSPI1_D8_C`。

<a id="abbb6a915fdb7d1a1b5949c0ec17bbdba"></a>

### `PIN_P17_1__GPIO`

```c
#define PIN_P17_1__GPIO ALIF_PINMUX(17, 1, 0)
```

引脚 `P17.1` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）1：`GPIO`。

<a id="a47038228f774e7d02197614267a65be5"></a>

### `PIN_P17_1__OSPI1_D9_C`

```c
#define PIN_P17_1__OSPI1_D9_C ALIF_PINMUX(17, 1, 1)
```

端口（Port）17 的引脚（Pin）1：`OSPI1_D9_C`。

<a id="a574598de77ccdb330be4c9f480d0c0c6"></a>

### `PIN_P17_2__GPIO`

```c
#define PIN_P17_2__GPIO ALIF_PINMUX(17, 2, 0)
```

引脚 `P17.2` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）2：`GPIO`。

<a id="a69a8a2c8793d9d827948a8c09786bd81"></a>

### `PIN_P17_2__OSPI1_D10_C`

```c
#define PIN_P17_2__OSPI1_D10_C ALIF_PINMUX(17, 2, 1)
```

端口（Port）17 的引脚（Pin）2：`OSPI1_D10_C`。

<a id="afd3b2e2d006b6b3f4c1323469d9366c0"></a>

### `PIN_P17_3__GPIO`

```c
#define PIN_P17_3__GPIO ALIF_PINMUX(17, 3, 0)
```

引脚 `P17.3` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）3：`GPIO`。

<a id="aa05d36fb2a03632ebbf31ef3025fa9a4"></a>

### `PIN_P17_3__OSPI1_D11_C`

```c
#define PIN_P17_3__OSPI1_D11_C ALIF_PINMUX(17, 3, 1)
```

端口（Port）17 的引脚（Pin）3：`OSPI1_D11_C`。

<a id="a3987a256ab19e5653c3cf2c39dd62722"></a>

### `PIN_P17_4__GPIO`

```c
#define PIN_P17_4__GPIO ALIF_PINMUX(17, 4, 0)
```

引脚 `P17.4` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）4：`GPIO`。

<a id="a224218094cfd29015cbb6702eb8c3ffb"></a>

### `PIN_P17_4__OSPI1_D12_C`

```c
#define PIN_P17_4__OSPI1_D12_C ALIF_PINMUX(17, 4, 1)
```

端口（Port）17 的引脚（Pin）4：`OSPI1_D12_C`。

<a id="a2a6dd0f9c58af43a8c0dec530b4eac31"></a>

### `PIN_P17_5__GPIO`

```c
#define PIN_P17_5__GPIO ALIF_PINMUX(17, 5, 0)
```

引脚 `P17.5` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）5：`GPIO`。

<a id="a8449a677fedbc254b014dc91de8eb7ec"></a>

### `PIN_P17_5__OSPI1_D13_C`

```c
#define PIN_P17_5__OSPI1_D13_C ALIF_PINMUX(17, 5, 1)
```

端口（Port）17 的引脚（Pin）5：`OSPI1_D13_C`。

<a id="ab7d0d3b92adf9ca32d37337c12df63d6"></a>

### `PIN_P17_6__GPIO`

```c
#define PIN_P17_6__GPIO ALIF_PINMUX(17, 6, 0)
```

引脚 `P17.6` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）6：`GPIO`。

<a id="aea275755208a04e1cf624d773f611015"></a>

### `PIN_P17_6__OSPI1_D14_C`

```c
#define PIN_P17_6__OSPI1_D14_C ALIF_PINMUX(17, 6, 1)
```

端口（Port）17 的引脚（Pin）6：`OSPI1_D14_C`。

<a id="a6bb6e4af895fa892866cb228c5b9413b"></a>

### `PIN_P17_7__GPIO`

```c
#define PIN_P17_7__GPIO ALIF_PINMUX(17, 7, 0)
```

引脚 `P17.7` 的复用功能（Alternate Functions）。

端口（Port）17 的引脚（Pin）7：`GPIO`。

<a id="a5efdaed363308f46af5032c61f7656a3"></a>

### `PIN_P17_7__OSPI1_D15_C`

```c
#define PIN_P17_7__OSPI1_D15_C ALIF_PINMUX(17, 7, 1)
```

端口（Port）17 的引脚（Pin）7：`OSPI1_D15_C`。

<a id="af46992d6adf393d9fffa0b3d6bdf4568"></a>

### `PIN_P1_0__ANA_S8`

```c
#define PIN_P1_0__ANA_S8 ALIF_PINMUX(1, 0, 7)
```

端口（Port）1 的引脚（Pin）0：`ANA_S8`。

<a id="a814937842bb7225f52db5bf2f9f8818b"></a>

### `PIN_P1_0__ETH_RXD0_C`

```c
#define PIN_P1_0__ETH_RXD0_C ALIF_PINMUX(1, 0, 6)
```

端口（Port）1 的引脚（Pin）0：`ETH_RXD0_C`。

<a id="af59cc6b851070a403399aa14ec9522d5"></a>

### `PIN_P1_0__GPIO`

```c
#define PIN_P1_0__GPIO ALIF_PINMUX(1, 0, 0)
```

引脚 `P1.0` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）0：`GPIO`。

<a id="a5b2648f183931a24604241319842e227"></a>

### `PIN_P1_0__I2C3_SDA_A`

```c
#define PIN_P1_0__I2C3_SDA_A ALIF_PINMUX(1, 0, 3)
```

端口（Port）1 的引脚（Pin）0：`I2C3_SDA_A`。

<a id="ae6e14263f73fe7b05294646dbb49c0bb"></a>

### `PIN_P1_0__LPCAM_HSYNC_C`

```c
#define PIN_P1_0__LPCAM_HSYNC_C ALIF_PINMUX(1, 0, 5)
```

端口（Port）1 的引脚（Pin）0：`LPCAM_HSYNC_C`。

<a id="a1b162fa1d3aa4c3dd720b47331a07a43"></a>

### `PIN_P1_0__SPI0_MISO_A`

```c
#define PIN_P1_0__SPI0_MISO_A ALIF_PINMUX(1, 0, 2)
```

端口（Port）1 的引脚（Pin）0：`SPI0_MISO_A`。

<a id="a86fd70e32e1fe8ef3ddb28394c1181b9"></a>

### `PIN_P1_0__UART2_RX_A`

```c
#define PIN_P1_0__UART2_RX_A ALIF_PINMUX(1, 0, 1)
```

端口（Port）1 的引脚（Pin）0：`UART2_RX_A`。

<a id="a3f3320201474237109dbd44284ccfedc"></a>

### `PIN_P1_0__UT4_T0_A`

```c
#define PIN_P1_0__UT4_T0_A ALIF_PINMUX(1, 0, 4)
```

端口（Port）1 的引脚（Pin）0：`UT4_T0_A`。

<a id="a86211d8e48dc86b32b17f2f6d1756ba9"></a>

### `PIN_P1_1__ANA_S9`

```c
#define PIN_P1_1__ANA_S9 ALIF_PINMUX(1, 1, 7)
```

端口（Port）1 的引脚（Pin）1：`ANA_S9`。

<a id="a4ef1406076debf4c5218543e138228e3"></a>

### `PIN_P1_1__ETH_RXD1_C`

```c
#define PIN_P1_1__ETH_RXD1_C ALIF_PINMUX(1, 1, 6)
```

端口（Port）1 的引脚（Pin）1：`ETH_RXD1_C`。

<a id="a5bde8570f8ee36a7dfa0e5d486dcb4d1"></a>

### `PIN_P1_1__GPIO`

```c
#define PIN_P1_1__GPIO ALIF_PINMUX(1, 1, 0)
```

引脚 `P1.1` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）1：`GPIO`。

<a id="a2399f5c76054a2d2d0f516faffd33dd0"></a>

### `PIN_P1_1__I2C3_SCL_A`

```c
#define PIN_P1_1__I2C3_SCL_A ALIF_PINMUX(1, 1, 3)
```

端口（Port）1 的引脚（Pin）1：`I2C3_SCL_A`。

<a id="a0eee3d62f2ee65deb0cd9f2b69882199"></a>

### `PIN_P1_1__LPCAM_VSYNC_C`

```c
#define PIN_P1_1__LPCAM_VSYNC_C ALIF_PINMUX(1, 1, 5)
```

端口（Port）1 的引脚（Pin）1：`LPCAM_VSYNC_C`。

<a id="a37f579415afac4b490325552b9a90197"></a>

### `PIN_P1_1__SPI0_MOSI_A`

```c
#define PIN_P1_1__SPI0_MOSI_A ALIF_PINMUX(1, 1, 2)
```

端口（Port）1 的引脚（Pin）1：`SPI0_MOSI_A`。

<a id="ae31470618a41e1fa01512589fd7d454d"></a>

### `PIN_P1_1__UART2_TX_A`

```c
#define PIN_P1_1__UART2_TX_A ALIF_PINMUX(1, 1, 1)
```

端口（Port）1 的引脚（Pin）1：`UART2_TX_A`。

<a id="a7f6c1d958eca3b932064e4fe6422536e"></a>

### `PIN_P1_1__UT4_T1_A`

```c
#define PIN_P1_1__UT4_T1_A ALIF_PINMUX(1, 1, 4)
```

端口（Port）1 的引脚（Pin）1：`UT4_T1_A`。

<a id="aa592bdbfcd49525f21feb3f9b9f5c0f9"></a>

### `PIN_P1_2__ANA_S10`

```c
#define PIN_P1_2__ANA_S10 ALIF_PINMUX(1, 2, 7)
```

端口（Port）1 的引脚（Pin）2：`ANA_S10`。

<a id="ace30b43016cff2a82db9893dd1eebd97"></a>

### `PIN_P1_2__ETH_RST_C`

```c
#define PIN_P1_2__ETH_RST_C ALIF_PINMUX(1, 2, 6)
```

端口（Port）1 的引脚（Pin）2：`ETH_RST_C`。

<a id="a6b0ea73c6cb252fda5ad10a28ceae4cf"></a>

### `PIN_P1_2__GPIO`

```c
#define PIN_P1_2__GPIO ALIF_PINMUX(1, 2, 0)
```

引脚 `P1.2` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）2：`GPIO`。

<a id="af47e1bc6844cd83ac416a61f08a496d0"></a>

### `PIN_P1_2__I3C_SDA_B`

```c
#define PIN_P1_2__I3C_SDA_B ALIF_PINMUX(1, 2, 3)
```

端口（Port）1 的引脚（Pin）2：`I3C_SDA_B`。

<a id="a9aeae29f48b994b81c2223e5eddd24c4"></a>

### `PIN_P1_2__LPCAM_PCLK_C`

```c
#define PIN_P1_2__LPCAM_PCLK_C ALIF_PINMUX(1, 2, 5)
```

端口（Port）1 的引脚（Pin）2：`LPCAM_PCLK_C`。

<a id="a80e2fc726f8004102da0cc8cf2acbaa3"></a>

### `PIN_P1_2__SPI0_SCLK_A`

```c
#define PIN_P1_2__SPI0_SCLK_A ALIF_PINMUX(1, 2, 2)
```

端口（Port）1 的引脚（Pin）2：`SPI0_SCLK_A`。

<a id="a75bdf22221574ac8f8d52c0ca11b9d01"></a>

### `PIN_P1_2__UART3_RX_A`

```c
#define PIN_P1_2__UART3_RX_A ALIF_PINMUX(1, 2, 1)
```

端口（Port）1 的引脚（Pin）2：`UART3_RX_A`。

<a id="ae2cf8fd83f09da752634bcd3be2c945e"></a>

### `PIN_P1_2__UT5_T0_A`

```c
#define PIN_P1_2__UT5_T0_A ALIF_PINMUX(1, 2, 4)
```

端口（Port）1 的引脚（Pin）2：`UT5_T0_A`。

<a id="ae90b82e11aa2b5d577d576047e1e5293"></a>

### `PIN_P1_3__ANA_S11`

```c
#define PIN_P1_3__ANA_S11 ALIF_PINMUX(1, 3, 7)
```

端口（Port）1 的引脚（Pin）3：`ANA_S11`。

<a id="a72dfb2f9baf5ced5aed74c89826aa0f5"></a>

### `PIN_P1_3__ETH_TXD0_C`

```c
#define PIN_P1_3__ETH_TXD0_C ALIF_PINMUX(1, 3, 6)
```

端口（Port）1 的引脚（Pin）3：`ETH_TXD0_C`。

<a id="a7ff354be10a7bcfd9418e346c2f860e5"></a>

### `PIN_P1_3__GPIO`

```c
#define PIN_P1_3__GPIO ALIF_PINMUX(1, 3, 0)
```

引脚 `P1.3` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）3：`GPIO`。

<a id="afed98f0a2042138d28a4bc1ddf9b1413"></a>

### `PIN_P1_3__I3C_SCL_B`

```c
#define PIN_P1_3__I3C_SCL_B ALIF_PINMUX(1, 3, 3)
```

端口（Port）1 的引脚（Pin）3：`I3C_SCL_B`。

<a id="aefe456eb61a82a883729e9ffb3fc6094"></a>

### `PIN_P1_3__LPCAM_XVCLK_C`

```c
#define PIN_P1_3__LPCAM_XVCLK_C ALIF_PINMUX(1, 3, 5)
```

端口（Port）1 的引脚（Pin）3：`LPCAM_XVCLK_C`。

<a id="acf307eea767cfd0532384afee6889ded"></a>

### `PIN_P1_3__SPI0_SS0_A`

```c
#define PIN_P1_3__SPI0_SS0_A ALIF_PINMUX(1, 3, 2)
```

端口（Port）1 的引脚（Pin）3：`SPI0_SS0_A`。

<a id="a8b0a4679230f962bd0847217bd78758d"></a>

### `PIN_P1_3__UART3_TX_A`

```c
#define PIN_P1_3__UART3_TX_A ALIF_PINMUX(1, 3, 1)
```

端口（Port）1 的引脚（Pin）3：`UART3_TX_A`。

<a id="ada6e4116bf669193c8cf1b1ed196fbf5"></a>

### `PIN_P1_3__UT5_T1_A`

```c
#define PIN_P1_3__UT5_T1_A ALIF_PINMUX(1, 3, 4)
```

端口（Port）1 的引脚（Pin）3：`UT5_T1_A`。

<a id="a93d7e266264960f84f8805cb86a31a88"></a>

### `PIN_P1_4__ANA_S12`

```c
#define PIN_P1_4__ANA_S12 ALIF_PINMUX(1, 4, 7)
```

端口（Port）1 的引脚（Pin）4：`ANA_S12`。

<a id="a46f5e6410d3fe7119511e8385ec1ca9b"></a>

### `PIN_P1_4__ETH_TXD1_C`

```c
#define PIN_P1_4__ETH_TXD1_C ALIF_PINMUX(1, 4, 6)
```

端口（Port）1 的引脚（Pin）4：`ETH_TXD1_C`。

<a id="ad1e50e7a0add033402abf705b503b80a"></a>

### `PIN_P1_4__GPIO`

```c
#define PIN_P1_4__GPIO ALIF_PINMUX(1, 4, 0)
```

引脚 `P1.4` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）4：`GPIO`。

<a id="a1142b9fb3e15c186d7267b63597e3b6b"></a>

### `PIN_P1_4__LPCAM_D0_C`

```c
#define PIN_P1_4__LPCAM_D0_C ALIF_PINMUX(1, 4, 5)
```

端口（Port）1 的引脚（Pin）4：`LPCAM_D0_C`。

<a id="ac80717bc4532eef10d5d26e2a23abe12"></a>

### `PIN_P1_4__OSPI0_SS0_A`

```c
#define PIN_P1_4__OSPI0_SS0_A ALIF_PINMUX(1, 4, 1)
```

端口（Port）1 的引脚（Pin）4：`OSPI0_SS0_A`。

<a id="a07943991a186c8d4bd34f439df430651"></a>

### `PIN_P1_4__SPI0_SS1_A`

```c
#define PIN_P1_4__SPI0_SS1_A ALIF_PINMUX(1, 4, 3)
```

端口（Port）1 的引脚（Pin）4：`SPI0_SS1_A`。

<a id="ab3d6a529ce7c2b8b8efccfb6a05f4130"></a>

### `PIN_P1_4__UART0_RX_B`

```c
#define PIN_P1_4__UART0_RX_B ALIF_PINMUX(1, 4, 2)
```

端口（Port）1 的引脚（Pin）4：`UART0_RX_B`。

<a id="a741fc08fdd89f80a78183ffebcc20a25"></a>

### `PIN_P1_4__UT6_T0_A`

```c
#define PIN_P1_4__UT6_T0_A ALIF_PINMUX(1, 4, 4)
```

端口（Port）1 的引脚（Pin）4：`UT6_T0_A`。

<a id="a4ddb6ff8be37b8c2ec9973fb5b316ce5"></a>

### `PIN_P1_5__ANA_S13`

```c
#define PIN_P1_5__ANA_S13 ALIF_PINMUX(1, 5, 7)
```

端口（Port）1 的引脚（Pin）5：`ANA_S13`。

<a id="a88a8bc7139c0e5e3b2aaf02d1f8bdde1"></a>

### `PIN_P1_5__ETH_TXEN_C`

```c
#define PIN_P1_5__ETH_TXEN_C ALIF_PINMUX(1, 5, 6)
```

端口（Port）1 的引脚（Pin）5：`ETH_TXEN_C`。

<a id="a0fb34153badcd47f16246988312d0275"></a>

### `PIN_P1_5__GPIO`

```c
#define PIN_P1_5__GPIO ALIF_PINMUX(1, 5, 0)
```

引脚 `P1.5` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）5：`GPIO`。

<a id="ab082a597cf3f000433c4c5dbff856357"></a>

### `PIN_P1_5__LPCAM_D1_C`

```c
#define PIN_P1_5__LPCAM_D1_C ALIF_PINMUX(1, 5, 5)
```

端口（Port）1 的引脚（Pin）5：`LPCAM_D1_C`。

<a id="a3dd514f984c015bb539a06b6d5167e90"></a>

### `PIN_P1_5__OSPI0_SS1_A`

```c
#define PIN_P1_5__OSPI0_SS1_A ALIF_PINMUX(1, 5, 1)
```

端口（Port）1 的引脚（Pin）5：`OSPI0_SS1_A`。

<a id="a33819bc403cac0989edef3e0002b5c26"></a>

### `PIN_P1_5__SPI0_SS2_A`

```c
#define PIN_P1_5__SPI0_SS2_A ALIF_PINMUX(1, 5, 3)
```

端口（Port）1 的引脚（Pin）5：`SPI0_SS2_A`。

<a id="a0d8f5efff85a27a618933da01782ceea"></a>

### `PIN_P1_5__UART0_TX_B`

```c
#define PIN_P1_5__UART0_TX_B ALIF_PINMUX(1, 5, 2)
```

端口（Port）1 的引脚（Pin）5：`UART0_TX_B`。

<a id="a3522647cc4e6bb11fdc53c388d1da8a9"></a>

### `PIN_P1_5__UT6_T1_A`

```c
#define PIN_P1_5__UT6_T1_A ALIF_PINMUX(1, 5, 4)
```

端口（Port）1 的引脚（Pin）5：`UT6_T1_A`。

<a id="aa1f2e27a7534f0db8518b4b8c68d5857"></a>

### `PIN_P1_6__ANA_S14`

```c
#define PIN_P1_6__ANA_S14 ALIF_PINMUX(1, 6, 7)
```

端口（Port）1 的引脚（Pin）6：`ANA_S14`。

<a id="a38276b33e082e4c6a044cd8baebf5107"></a>

### `PIN_P1_6__ETH_IRQ_C`

```c
#define PIN_P1_6__ETH_IRQ_C ALIF_PINMUX(1, 6, 6)
```

端口（Port）1 的引脚（Pin）6：`ETH_IRQ_C`。

<a id="ab6f0917e71cae608320a3c16b8edf1bf"></a>

### `PIN_P1_6__GPIO`

```c
#define PIN_P1_6__GPIO ALIF_PINMUX(1, 6, 0)
```

引脚 `P1.6` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）6：`GPIO`。

<a id="ab5b6fa72a51d06f2c315cdfb4ba8c4ad"></a>

### `PIN_P1_6__I2S0_SDI_A`

```c
#define PIN_P1_6__I2S0_SDI_A ALIF_PINMUX(1, 6, 3)
```

端口（Port）1 的引脚（Pin）6：`I2S0_SDI_A`。

<a id="aa28b285837812ca3bbb00f20610aceab"></a>

### `PIN_P1_6__LPCAM_D2_C`

```c
#define PIN_P1_6__LPCAM_D2_C ALIF_PINMUX(1, 6, 5)
```

端口（Port）1 的引脚（Pin）6：`LPCAM_D2_C`。

<a id="a00ced09f5db7ad96ec72a1375ba91254"></a>

### `PIN_P1_6__OSPI0_RXDS_B`

```c
#define PIN_P1_6__OSPI0_RXDS_B ALIF_PINMUX(1, 6, 1)
```

端口（Port）1 的引脚（Pin）6：`OSPI0_RXDS_B`。

<a id="a04e94f302847e57cdc54e8bfee7b0e46"></a>

### `PIN_P1_6__UART1_RX_B`

```c
#define PIN_P1_6__UART1_RX_B ALIF_PINMUX(1, 6, 2)
```

端口（Port）1 的引脚（Pin）6：`UART1_RX_B`。

<a id="a7220a9ebc489750752d69dad135e73e9"></a>

### `PIN_P1_6__UT7_T0_A`

```c
#define PIN_P1_6__UT7_T0_A ALIF_PINMUX(1, 6, 4)
```

端口（Port）1 的引脚（Pin）6：`UT7_T0_A`。

<a id="a92f2d3bd8b00e50624f60cc265b30551"></a>

### `PIN_P1_7__ANA_S15`

```c
#define PIN_P1_7__ANA_S15 ALIF_PINMUX(1, 7, 7)
```

端口（Port）1 的引脚（Pin）7：`ANA_S15`。

<a id="afd5a53c152a2c162e9e94c610d039f26"></a>

### `PIN_P1_7__ETH_REFCLK_C`

```c
#define PIN_P1_7__ETH_REFCLK_C ALIF_PINMUX(1, 7, 6)
```

端口（Port）1 的引脚（Pin）7：`ETH_REFCLK_C`。

<a id="a259e17b2ef415b6aed714af92b5f2ac5"></a>

### `PIN_P1_7__GPIO`

```c
#define PIN_P1_7__GPIO ALIF_PINMUX(1, 7, 0)
```

引脚 `P1.7` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）7：`GPIO`。

<a id="aba970af9b7ed5c4a767c77dba5342f9b"></a>

### `PIN_P1_7__I2S0_SDO_A`

```c
#define PIN_P1_7__I2S0_SDO_A ALIF_PINMUX(1, 7, 3)
```

端口（Port）1 的引脚（Pin）7：`I2S0_SDO_A`。

<a id="acf6622697cdb02583d3fc6a300ae1af2"></a>

### `PIN_P1_7__LPCAM_D3_C`

```c
#define PIN_P1_7__LPCAM_D3_C ALIF_PINMUX(1, 7, 5)
```

端口（Port）1 的引脚（Pin）7：`LPCAM_D3_C`。

<a id="a9e55d200e8e937a5b20a4924adaae8c3"></a>

### `PIN_P1_7__OSPI0_SCLK_A`

```c
#define PIN_P1_7__OSPI0_SCLK_A ALIF_PINMUX(1, 7, 1)
```

端口（Port）1 的引脚（Pin）7：`OSPI0_SCLK_A`。

<a id="ae8cbc076f0a1d507587fa57614314cca"></a>

### `PIN_P1_7__UART1_TX_B`

```c
#define PIN_P1_7__UART1_TX_B ALIF_PINMUX(1, 7, 2)
```

端口（Port）1 的引脚（Pin）7：`UART1_TX_B`。

<a id="aaef22b9773f6bcb90a55f76c500e1b25"></a>

### `PIN_P1_7__UT7_T1_A`

```c
#define PIN_P1_7__UT7_T1_A ALIF_PINMUX(1, 7, 4)
```

端口（Port）1 的引脚（Pin）7：`UT7_T1_A`。

<a id="a5fdc0b91384ca45874ca44628d9c8b22"></a>

### `PIN_P2_0__ANA_S16`

```c
#define PIN_P2_0__ANA_S16 ALIF_PINMUX(2, 0, 7)
```

端口（Port）2 的引脚（Pin）0：`ANA_S16`。

<a id="a9adb3410c6b24e5ca6ada558dfb3fbc4"></a>

### `PIN_P2_0__ETH_MDIO_C`

```c
#define PIN_P2_0__ETH_MDIO_C ALIF_PINMUX(2, 0, 6)
```

端口（Port）2 的引脚（Pin）0：`ETH_MDIO_C`。

<a id="a2ed50f7f44d929b517287eaae4560f33"></a>

### `PIN_P2_0__GPIO`

```c
#define PIN_P2_0__GPIO ALIF_PINMUX(2, 0, 0)
```

引脚 `P2.0` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）0：`GPIO`。

<a id="a3955ab4850804ac7b5b7f7301028f5bc"></a>

### `PIN_P2_0__LPCAM_D4_C`

```c
#define PIN_P2_0__LPCAM_D4_C ALIF_PINMUX(2, 0, 5)
```

端口（Port）2 的引脚（Pin）0：`LPCAM_D4_C`。

<a id="a577845dca48bd5b863e581412aebc03d"></a>

### `PIN_P2_0__LPPDM_DO_A`

```c
#define PIN_P2_0__LPPDM_DO_A ALIF_PINMUX(2, 0, 3)
```

端口（Port）2 的引脚（Pin）0：`LPPDM_DO_A`。

<a id="aa82957297e0601b509bfd324ee68c619"></a>

### `PIN_P2_0__OSPI0_D0_B`

```c
#define PIN_P2_0__OSPI0_D0_B ALIF_PINMUX(2, 0, 1)
```

端口（Port）2 的引脚（Pin）0：`OSPI0_D0_B`。

<a id="aaf2248797fce75459afa8361685c4f99"></a>

### `PIN_P2_0__UART2_RX_B`

```c
#define PIN_P2_0__UART2_RX_B ALIF_PINMUX(2, 0, 2)
```

端口（Port）2 的引脚（Pin）0：`UART2_RX_B`。

<a id="acc68e58a4a1b2d16f7cf1761763e69da"></a>

### `PIN_P2_0__UT8_T0_A`

```c
#define PIN_P2_0__UT8_T0_A ALIF_PINMUX(2, 0, 4)
```

端口（Port）2 的引脚（Pin）0：`UT8_T0_A`。

<a id="aeed5bdbf4e2c204b433b82007e816119"></a>

### `PIN_P2_1__ANA_S17`

```c
#define PIN_P2_1__ANA_S17 ALIF_PINMUX(2, 1, 7)
```

端口（Port）2 的引脚（Pin）1：`ANA_S17`。

<a id="ad40a374561a166ed81116bbc7e2e8388"></a>

### `PIN_P2_1__ETH_MDC_C`

```c
#define PIN_P2_1__ETH_MDC_C ALIF_PINMUX(2, 1, 6)
```

端口（Port）2 的引脚（Pin）1：`ETH_MDC_C`。

<a id="ac05af956aca2528e61e358c597c5b637"></a>

### `PIN_P2_1__GPIO`

```c
#define PIN_P2_1__GPIO ALIF_PINMUX(2, 1, 0)
```

引脚 `P2.1` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）1：`GPIO`。

<a id="aa30d906709b79bb5ac704517df51c6f8"></a>

### `PIN_P2_1__LPCAM_D5_C`

```c
#define PIN_P2_1__LPCAM_D5_C ALIF_PINMUX(2, 1, 5)
```

端口（Port）2 的引脚（Pin）1：`LPCAM_D5_C`。

<a id="adf29ae0357511182f97b1ff2753cc474"></a>

### `PIN_P2_1__LPPDM_CO_A`

```c
#define PIN_P2_1__LPPDM_CO_A ALIF_PINMUX(2, 1, 3)
```

端口（Port）2 的引脚（Pin）1：`LPPDM_CO_A`。

<a id="a842c077a7b7716b901c7c980f793e910"></a>

### `PIN_P2_1__OSPI0_D1_B`

```c
#define PIN_P2_1__OSPI0_D1_B ALIF_PINMUX(2, 1, 1)
```

端口（Port）2 的引脚（Pin）1：`OSPI0_D1_B`。

<a id="a001165a8acc638335d9794dda1595faa"></a>

### `PIN_P2_1__UART2_TX_B`

```c
#define PIN_P2_1__UART2_TX_B ALIF_PINMUX(2, 1, 2)
```

端口（Port）2 的引脚（Pin）1：`UART2_TX_B`。

<a id="a32110e2d98bfacf89cedebf7e4d737ce"></a>

### `PIN_P2_1__UT8_T1_A`

```c
#define PIN_P2_1__UT8_T1_A ALIF_PINMUX(2, 1, 4)
```

端口（Port）2 的引脚（Pin）1：`UT8_T1_A`。

<a id="a1c5aed6c5f029bf93595865c45c40ab8"></a>

### `PIN_P2_2__ANA_S18`

```c
#define PIN_P2_2__ANA_S18 ALIF_PINMUX(2, 2, 7)
```

端口（Port）2 的引脚（Pin）2：`ANA_S18`。

<a id="a79595ae2bb209452669c2e9080467b0a"></a>

### `PIN_P2_2__ETH_CRS_DV_C`

```c
#define PIN_P2_2__ETH_CRS_DV_C ALIF_PINMUX(2, 2, 6)
```

端口（Port）2 的引脚（Pin）2：`ETH_CRS_DV_C`。

<a id="a3fc212b07d980d4ae21a1743da443ac8"></a>

### `PIN_P2_2__GPIO`

```c
#define PIN_P2_2__GPIO ALIF_PINMUX(2, 2, 0)
```

引脚 `P2.2` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）2：`GPIO`。

<a id="aa3ddf0b435364b8b12f44ec46e6818a7"></a>

### `PIN_P2_2__LPCAM_D6_C`

```c
#define PIN_P2_2__LPCAM_D6_C ALIF_PINMUX(2, 2, 5)
```

端口（Port）2 的引脚（Pin）2：`LPCAM_D6_C`。

<a id="abc4c737fb7dfbda40f2451b15b3009e8"></a>

### `PIN_P2_2__LPPDM_D1_A`

```c
#define PIN_P2_2__LPPDM_D1_A ALIF_PINMUX(2, 2, 3)
```

端口（Port）2 的引脚（Pin）2：`LPPDM_D1_A`。

<a id="a58cecc0983fa40257343759dd563238c"></a>

### `PIN_P2_2__OSPI0_D2_B`

```c
#define PIN_P2_2__OSPI0_D2_B ALIF_PINMUX(2, 2, 1)
```

端口（Port）2 的引脚（Pin）2：`OSPI0_D2_B`。

<a id="a0e7ae0e5d25d567d45b82c69bf6c3449"></a>

### `PIN_P2_2__UART3_RX_B`

```c
#define PIN_P2_2__UART3_RX_B ALIF_PINMUX(2, 2, 2)
```

端口（Port）2 的引脚（Pin）2：`UART3_RX_B`。

<a id="aed1b4637862440bcf15ecf9e4a522a70"></a>

### `PIN_P2_2__UT9_T0_A`

```c
#define PIN_P2_2__UT9_T0_A ALIF_PINMUX(2, 2, 4)
```

端口（Port）2 的引脚（Pin）2：`UT9_T0_A`。

<a id="a278c1c69c1630a34e9614df51b00b23e"></a>

### `PIN_P2_3__ANA_S19`

```c
#define PIN_P2_3__ANA_S19 ALIF_PINMUX(2, 3, 7)
```

端口（Port）2 的引脚（Pin）3：`ANA_S19`。

<a id="a6b3f74c3429e0b1bcc951344dd2769ea"></a>

### `PIN_P2_3__CDC_PCLK_B`

```c
#define PIN_P2_3__CDC_PCLK_B ALIF_PINMUX(2, 3, 6)
```

端口（Port）2 的引脚（Pin）3：`CDC_PCLK_B`。

<a id="a8408f18132258a0ef9fb8c3fe4f33977"></a>

### `PIN_P2_3__GPIO`

```c
#define PIN_P2_3__GPIO ALIF_PINMUX(2, 3, 0)
```

引脚 `P2.3` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）3：`GPIO`。

<a id="a61e5f243810f4850f937ca8d1545e3fc"></a>

### `PIN_P2_3__LPCAM_D7_C`

```c
#define PIN_P2_3__LPCAM_D7_C ALIF_PINMUX(2, 3, 5)
```

端口（Port）2 的引脚（Pin）3：`LPCAM_D7_C`。

<a id="ada2c11fb58922dd44e9d8eab855e814e"></a>

### `PIN_P2_3__LPPDM_C1_A`

```c
#define PIN_P2_3__LPPDM_C1_A ALIF_PINMUX(2, 3, 3)
```

端口（Port）2 的引脚（Pin）3：`LPPDM_C1_A`。

<a id="a54f3045b17356a82629a1556aa7ff73a"></a>

### `PIN_P2_3__OSPI0_D3_B`

```c
#define PIN_P2_3__OSPI0_D3_B ALIF_PINMUX(2, 3, 1)
```

端口（Port）2 的引脚（Pin）3：`OSPI0_D3_B`。

<a id="a616776438eb862a4108a37992a632e67"></a>

### `PIN_P2_3__UART3_TX_B`

```c
#define PIN_P2_3__UART3_TX_B ALIF_PINMUX(2, 3, 2)
```

端口（Port）2 的引脚（Pin）3：`UART3_TX_B`。

<a id="afdeb160972e810f240b4702c2b1eeec9"></a>

### `PIN_P2_3__UT9_T1_A`

```c
#define PIN_P2_3__UT9_T1_A ALIF_PINMUX(2, 3, 4)
```

端口（Port）2 的引脚（Pin）3：`UT9_T1_A`。

<a id="a9a559ace0037b84ab5a1e40077ea8808"></a>

### `PIN_P2_4__ANA_S20`

```c
#define PIN_P2_4__ANA_S20 ALIF_PINMUX(2, 4, 7)
```

端口（Port）2 的引脚（Pin）4：`ANA_S20`。

<a id="a319dc0b42697fc3b306d26008b19a143"></a>

### `PIN_P2_4__CAM_D0_A`

```c
#define PIN_P2_4__CAM_D0_A ALIF_PINMUX(2, 4, 6)
```

端口（Port）2 的引脚（Pin）4：`CAM_D0_A`。

<a id="a649d4dc937e3cb6269408b128ed3aae3"></a>

### `PIN_P2_4__GPIO`

```c
#define PIN_P2_4__GPIO ALIF_PINMUX(2, 4, 0)
```

引脚 `P2.4` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）4：`GPIO`。

<a id="a45c1199b3ae89c34db01df5b52ee4b44"></a>

### `PIN_P2_4__LPCAM_D0_B`

```c
#define PIN_P2_4__LPCAM_D0_B ALIF_PINMUX(2, 4, 5)
```

端口（Port）2 的引脚（Pin）4：`LPCAM_D0_B`。

<a id="a0a7d9b1a52f563523232be9bf721b93c"></a>

### `PIN_P2_4__LPI2S_SDI_A`

```c
#define PIN_P2_4__LPI2S_SDI_A ALIF_PINMUX(2, 4, 2)
```

端口（Port）2 的引脚（Pin）4：`LPI2S_SDI_A`。

<a id="adf2f3b37102ca4d9b2f0911883bac38b"></a>

### `PIN_P2_4__OSPI0_D4_B`

```c
#define PIN_P2_4__OSPI0_D4_B ALIF_PINMUX(2, 4, 1)
```

端口（Port）2 的引脚（Pin）4：`OSPI0_D4_B`。

<a id="a2aa83e7a998c6c5bb3f50752acf36596"></a>

### `PIN_P2_4__SPI1_MISO_A`

```c
#define PIN_P2_4__SPI1_MISO_A ALIF_PINMUX(2, 4, 3)
```

端口（Port）2 的引脚（Pin）4：`SPI1_MISO_A`。

<a id="ab3881a977b071eea87195c775af58362"></a>

### `PIN_P2_4__UT10_T0_A`

```c
#define PIN_P2_4__UT10_T0_A ALIF_PINMUX(2, 4, 4)
```

端口（Port）2 的引脚（Pin）4：`UT10_T0_A`。

<a id="a3a52e20cf83881a4040b2923a908312d"></a>

### `PIN_P2_5__ANA_S21`

```c
#define PIN_P2_5__ANA_S21 ALIF_PINMUX(2, 5, 7)
```

端口（Port）2 的引脚（Pin）5：`ANA_S21`。

<a id="ac0a6ef529c49b06354fefd6006df80a8"></a>

### `PIN_P2_5__CAM_D1_A`

```c
#define PIN_P2_5__CAM_D1_A ALIF_PINMUX(2, 5, 6)
```

端口（Port）2 的引脚（Pin）5：`CAM_D1_A`。

<a id="ac399d584c2f7dbdf0a2ceeb91a9a9ea0"></a>

### `PIN_P2_5__GPIO`

```c
#define PIN_P2_5__GPIO ALIF_PINMUX(2, 5, 0)
```

引脚 `P2.5` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）5：`GPIO`。

<a id="a3c58d40ef3db239807b40c2c369f7340"></a>

### `PIN_P2_5__LPCAM_D1_B`

```c
#define PIN_P2_5__LPCAM_D1_B ALIF_PINMUX(2, 5, 5)
```

端口（Port）2 的引脚（Pin）5：`LPCAM_D1_B`。

<a id="a3ce54d780b1c7f8edd0a417884172658"></a>

### `PIN_P2_5__LPI2S_SDO_A`

```c
#define PIN_P2_5__LPI2S_SDO_A ALIF_PINMUX(2, 5, 2)
```

端口（Port）2 的引脚（Pin）5：`LPI2S_SDO_A`。

<a id="a34d5cf58f78ffdc01a47a4caf42f6d49"></a>

### `PIN_P2_5__OSPI0_D5_B`

```c
#define PIN_P2_5__OSPI0_D5_B ALIF_PINMUX(2, 5, 1)
```

端口（Port）2 的引脚（Pin）5：`OSPI0_D5_B`。

<a id="a3e7ab219ef183221184241ddbd94e7ed"></a>

### `PIN_P2_5__SPI1_MOSI_A`

```c
#define PIN_P2_5__SPI1_MOSI_A ALIF_PINMUX(2, 5, 3)
```

端口（Port）2 的引脚（Pin）5：`SPI1_MOSI_A`。

<a id="a6029e70b8f2cf154922af02809ee10f8"></a>

### `PIN_P2_5__UT10_T1_A`

```c
#define PIN_P2_5__UT10_T1_A ALIF_PINMUX(2, 5, 4)
```

端口（Port）2 的引脚（Pin）5：`UT10_T1_A`。

<a id="a5f155f536d36ca472970a8a88cd88fbf"></a>

### `PIN_P2_6__ANA_S22`

```c
#define PIN_P2_6__ANA_S22 ALIF_PINMUX(2, 6, 7)
```

端口（Port）2 的引脚（Pin）6：`ANA_S22`。

<a id="a63c496343932fe27c57ee6b43811b196"></a>

### `PIN_P2_6__CAM_D2_A`

```c
#define PIN_P2_6__CAM_D2_A ALIF_PINMUX(2, 6, 6)
```

端口（Port）2 的引脚（Pin）6：`CAM_D2_A`。

<a id="acf70da7d084f17a152af48ea6ef34527"></a>

### `PIN_P2_6__GPIO`

```c
#define PIN_P2_6__GPIO ALIF_PINMUX(2, 6, 0)
```

引脚 `P2.6` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）6：`GPIO`。

<a id="a4c8b29f25f52029b6cb08a5ec5afa779"></a>

### `PIN_P2_6__LPCAM_D2_B`

```c
#define PIN_P2_6__LPCAM_D2_B ALIF_PINMUX(2, 6, 5)
```

端口（Port）2 的引脚（Pin）6：`LPCAM_D2_B`。

<a id="a4a56c254577a79842f8d72c49bd72a39"></a>

### `PIN_P2_6__LPI2S_SCLK_A`

```c
#define PIN_P2_6__LPI2S_SCLK_A ALIF_PINMUX(2, 6, 2)
```

端口（Port）2 的引脚（Pin）6：`LPI2S_SCLK_A`。

<a id="a0e37543540f7a5debb4880c428e5d386"></a>

### `PIN_P2_6__OSPI0_D6_B`

```c
#define PIN_P2_6__OSPI0_D6_B ALIF_PINMUX(2, 6, 1)
```

端口（Port）2 的引脚（Pin）6：`OSPI0_D6_B`。

<a id="a13b12f2f3dd64b479f8823b630f7ca16"></a>

### `PIN_P2_6__SPI1_SCLK_A`

```c
#define PIN_P2_6__SPI1_SCLK_A ALIF_PINMUX(2, 6, 3)
```

端口（Port）2 的引脚（Pin）6：`SPI1_SCLK_A`。

<a id="ac79a307d2c8bd2e69bd0ca655e4d4fba"></a>

### `PIN_P2_6__UT11_T0_A`

```c
#define PIN_P2_6__UT11_T0_A ALIF_PINMUX(2, 6, 4)
```

端口（Port）2 的引脚（Pin）6：`UT11_T0_A`。

<a id="a2cf38a7fbf2e09a633cb3d5599739988"></a>

### `PIN_P2_7__ANA_S23`

```c
#define PIN_P2_7__ANA_S23 ALIF_PINMUX(2, 7, 7)
```

端口（Port）2 的引脚（Pin）7：`ANA_S23`。

<a id="a532ec1795ccf99a05c09f4546ebc9b09"></a>

### `PIN_P2_7__CAM_D3_A`

```c
#define PIN_P2_7__CAM_D3_A ALIF_PINMUX(2, 7, 6)
```

端口（Port）2 的引脚（Pin）7：`CAM_D3_A`。

<a id="ab3f711dc40129f35a38cec46e12f23dd"></a>

### `PIN_P2_7__GPIO`

```c
#define PIN_P2_7__GPIO ALIF_PINMUX(2, 7, 0)
```

引脚 `P2.7` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）7：`GPIO`。

<a id="ae5fd2294c685aa90b41f782ae19cc853"></a>

### `PIN_P2_7__LPCAM_D3_B`

```c
#define PIN_P2_7__LPCAM_D3_B ALIF_PINMUX(2, 7, 5)
```

端口（Port）2 的引脚（Pin）7：`LPCAM_D3_B`。

<a id="a7bb33b4187db11f73bb44771e06a1043"></a>

### `PIN_P2_7__LPI2S_WS_A`

```c
#define PIN_P2_7__LPI2S_WS_A ALIF_PINMUX(2, 7, 2)
```

端口（Port）2 的引脚（Pin）7：`LPI2S_WS_A`。

<a id="a5d48a8c10667866e552c55b82bfb8c72"></a>

### `PIN_P2_7__OSPI0_D7_B`

```c
#define PIN_P2_7__OSPI0_D7_B ALIF_PINMUX(2, 7, 1)
```

端口（Port）2 的引脚（Pin）7：`OSPI0_D7_B`。

<a id="afc70e6300e5e0b337be0dfca7c65dd60"></a>

### `PIN_P2_7__SPI1_SS0_A`

```c
#define PIN_P2_7__SPI1_SS0_A ALIF_PINMUX(2, 7, 3)
```

端口（Port）2 的引脚（Pin）7：`SPI1_SS0_A`。

<a id="a18f66ed0932d572410bdc86defb04969"></a>

### `PIN_P2_7__UT11_T1_A`

```c
#define PIN_P2_7__UT11_T1_A ALIF_PINMUX(2, 7, 4)
```

端口（Port）2 的引脚（Pin）7：`UT11_T1_A`。

<a id="a28c59ba78d7a8dec612833b49bf283f7"></a>

### `PIN_P3_0__CAM_D4_A`

```c
#define PIN_P3_0__CAM_D4_A ALIF_PINMUX(3, 0, 7)
```

端口（Port）3 的引脚（Pin）0：`CAM_D4_A`。

<a id="aeb39304438c089405b315935caa1d90b"></a>

### `PIN_P3_0__GPIO`

```c
#define PIN_P3_0__GPIO ALIF_PINMUX(3, 0, 0)
```

引脚 `P3.0` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）0：`GPIO`。

<a id="ae61620d2e6ad149c619c9abd41c6f265"></a>

### `PIN_P3_0__I2S0_SCLK_A`

```c
#define PIN_P3_0__I2S0_SCLK_A ALIF_PINMUX(3, 0, 4)
```

端口（Port）3 的引脚（Pin）0：`I2S0_SCLK_A`。

<a id="a4836305188a3a85d3af2dc45f6139629"></a>

### `PIN_P3_0__LPCAM_D4_B`

```c
#define PIN_P3_0__LPCAM_D4_B ALIF_PINMUX(3, 0, 6)
```

端口（Port）3 的引脚（Pin）0：`LPCAM_D4_B`。

<a id="a209d55bd85828cc2d2dd906ce00a54bc"></a>

### `PIN_P3_0__OSPI0_SCLK_B`

```c
#define PIN_P3_0__OSPI0_SCLK_B ALIF_PINMUX(3, 0, 1)
```

端口（Port）3 的引脚（Pin）0：`OSPI0_SCLK_B`。

<a id="ac15579dca0f426d4c98762b1e3e48a0b"></a>

### `PIN_P3_0__PDM_D0_B`

```c
#define PIN_P3_0__PDM_D0_B ALIF_PINMUX(3, 0, 3)
```

端口（Port）3 的引脚（Pin）0：`PDM_D0_B`。

<a id="aa7685bafaaf059dba920a3ff14f0946f"></a>

### `PIN_P3_0__QEC0_X_A`

```c
#define PIN_P3_0__QEC0_X_A ALIF_PINMUX(3, 0, 5)
```

端口（Port）3 的引脚（Pin）0：`QEC0_X_A`。

<a id="aa62f64668d791bbee277fe5d60c3e30c"></a>

### `PIN_P3_0__UART4_RX_A`

```c
#define PIN_P3_0__UART4_RX_A ALIF_PINMUX(3, 0, 2)
```

端口（Port）3 的引脚（Pin）0：`UART4_RX_A`。

<a id="a4234dfa64e59a21f8dceb1eb089e4c57"></a>

### `PIN_P3_1__CAM_D5_A`

```c
#define PIN_P3_1__CAM_D5_A ALIF_PINMUX(3, 1, 7)
```

端口（Port）3 的引脚（Pin）1：`CAM_D5_A`。

<a id="a6cd05b1a797d571a1d1d1981ba849f8f"></a>

### `PIN_P3_1__GPIO`

```c
#define PIN_P3_1__GPIO ALIF_PINMUX(3, 1, 0)
```

引脚 `P3.1` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）1：`GPIO`。

<a id="a328c1fc58286091b09614c0d462f99ed"></a>

### `PIN_P3_1__I2S0_WS_A`

```c
#define PIN_P3_1__I2S0_WS_A ALIF_PINMUX(3, 1, 4)
```

端口（Port）3 的引脚（Pin）1：`I2S0_WS_A`。

<a id="a1b63270ca2becba12cb7f760e083c15f"></a>

### `PIN_P3_1__LPCAM_D5_B`

```c
#define PIN_P3_1__LPCAM_D5_B ALIF_PINMUX(3, 1, 6)
```

端口（Port）3 的引脚（Pin）1：`LPCAM_D5_B`。

<a id="aaba2b57d35fa7d428a318a0dc9855025"></a>

### `PIN_P3_1__OSPI0_SCLKN_B`

```c
#define PIN_P3_1__OSPI0_SCLKN_B ALIF_PINMUX(3, 1, 1)
```

端口（Port）3 的引脚（Pin）1：`OSPI0_SCLKN_B`。

<a id="ac646919b01848e8b19e48b2bfd3c6d5e"></a>

### `PIN_P3_1__PDM_C0_B`

```c
#define PIN_P3_1__PDM_C0_B ALIF_PINMUX(3, 1, 3)
```

端口（Port）3 的引脚（Pin）1：`PDM_C0_B`。

<a id="a8194b8be869e35552ea43b5e0a010f1c"></a>

### `PIN_P3_1__QEC0_Y_A`

```c
#define PIN_P3_1__QEC0_Y_A ALIF_PINMUX(3, 1, 5)
```

端口（Port）3 的引脚（Pin）1：`QEC0_Y_A`。

<a id="a0512fcc221b1f4be00f7c0c07f4c05ad"></a>

### `PIN_P3_1__UART4_TX_A`

```c
#define PIN_P3_1__UART4_TX_A ALIF_PINMUX(3, 1, 2)
```

端口（Port）3 的引脚（Pin）1：`UART4_TX_A`。

<a id="a89dc9f0608bd14bc339aad2a6352b072"></a>

### `PIN_P3_2__CAM_D6_A`

```c
#define PIN_P3_2__CAM_D6_A ALIF_PINMUX(3, 2, 7)
```

端口（Port）3 的引脚（Pin）2：`CAM_D6_A`。

<a id="a4bfd126d24cab1669b9880c163e9b73a"></a>

### `PIN_P3_2__GPIO`

```c
#define PIN_P3_2__GPIO ALIF_PINMUX(3, 2, 0)
```

引脚 `P3.2` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）2：`GPIO`。

<a id="a14c39a4fe27d9ec9f126ce635873324b"></a>

### `PIN_P3_2__I2S1_SDI_A`

```c
#define PIN_P3_2__I2S1_SDI_A ALIF_PINMUX(3, 2, 3)
```

端口（Port）3 的引脚（Pin）2：`I2S1_SDI_A`。

<a id="a7fe93f89c7972565ea925b65e8c33ac3"></a>

### `PIN_P3_2__I3C_SDA_C`

```c
#define PIN_P3_2__I3C_SDA_C ALIF_PINMUX(3, 2, 4)
```

端口（Port）3 的引脚（Pin）2：`I3C_SDA_C`。

<a id="a6fbc5b2f77d7b2be8a6b89c2d4b0124b"></a>

### `PIN_P3_2__LPCAM_D6_B`

```c
#define PIN_P3_2__LPCAM_D6_B ALIF_PINMUX(3, 2, 6)
```

端口（Port）3 的引脚（Pin）2：`LPCAM_D6_B`。

<a id="a4d5b9cece4a56b2a102b1925ff1f9a1b"></a>

### `PIN_P3_2__OSPI0_SS0_B`

```c
#define PIN_P3_2__OSPI0_SS0_B ALIF_PINMUX(3, 2, 1)
```

端口（Port）3 的引脚（Pin）2：`OSPI0_SS0_B`。

<a id="a219f780cdd43c9ac60fc5e05a073dc2e"></a>

### `PIN_P3_2__PDM_D1_B`

```c
#define PIN_P3_2__PDM_D1_B ALIF_PINMUX(3, 2, 2)
```

端口（Port）3 的引脚（Pin）2：`PDM_D1_B`。

<a id="a4c9789730311f91c9f1535dde7b94e9d"></a>

### `PIN_P3_2__QEC0_Z_A`

```c
#define PIN_P3_2__QEC0_Z_A ALIF_PINMUX(3, 2, 5)
```

端口（Port）3 的引脚（Pin）2：`QEC0_Z_A`。

<a id="ae578ece739f190c58b879086a37f56f3"></a>

### `PIN_P3_3__CAM_D7_A`

```c
#define PIN_P3_3__CAM_D7_A ALIF_PINMUX(3, 3, 7)
```

端口（Port）3 的引脚（Pin）3：`CAM_D7_A`。

<a id="ac22b3e259b7eac30c576114860368ae4"></a>

### `PIN_P3_3__GPIO`

```c
#define PIN_P3_3__GPIO ALIF_PINMUX(3, 3, 0)
```

引脚 `P3.3` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）3：`GPIO`。

<a id="a3d84682d52ba3eb596c9c4eaa707ee17"></a>

### `PIN_P3_3__I2S1_SDO_A`

```c
#define PIN_P3_3__I2S1_SDO_A ALIF_PINMUX(3, 3, 3)
```

端口（Port）3 的引脚（Pin）3：`I2S1_SDO_A`。

<a id="a8cd7ccbaba7a127e079eeae5f3fb6df6"></a>

### `PIN_P3_3__I3C_SCL_C`

```c
#define PIN_P3_3__I3C_SCL_C ALIF_PINMUX(3, 3, 4)
```

端口（Port）3 的引脚（Pin）3：`I3C_SCL_C`。

<a id="ad2843f4084856d540a0936f609ea673f"></a>

### `PIN_P3_3__LPCAM_D7_B`

```c
#define PIN_P3_3__LPCAM_D7_B ALIF_PINMUX(3, 3, 6)
```

端口（Port）3 的引脚（Pin）3：`LPCAM_D7_B`。

<a id="aa5bf95d622e1c2284151ac4ff625ed63"></a>

### `PIN_P3_3__OSPI0_SS1_B`

```c
#define PIN_P3_3__OSPI0_SS1_B ALIF_PINMUX(3, 3, 1)
```

端口（Port）3 的引脚（Pin）3：`OSPI0_SS1_B`。

<a id="a762ad931b8b9351a3bb168a9aaccf7d6"></a>

### `PIN_P3_3__PDM_C1_B`

```c
#define PIN_P3_3__PDM_C1_B ALIF_PINMUX(3, 3, 2)
```

端口（Port）3 的引脚（Pin）3：`PDM_C1_B`。

<a id="aa1a195a08756e8d8afbb0c488b92103c"></a>

### `PIN_P3_3__QEC1_X_A`

```c
#define PIN_P3_3__QEC1_X_A ALIF_PINMUX(3, 3, 5)
```

端口（Port）3 的引脚（Pin）3：`QEC1_X_A`。

<a id="ae136906f8123c136a7e152663076a1fa"></a>

### `PIN_P3_4__CAM_D8_A`

```c
#define PIN_P3_4__CAM_D8_A ALIF_PINMUX(3, 4, 7)
```

端口（Port）3 的引脚（Pin）4：`CAM_D8_A`。

<a id="af826ee88e3ed085269f16bee4a1a5bd7"></a>

### `PIN_P3_4__GPIO`

```c
#define PIN_P3_4__GPIO ALIF_PINMUX(3, 4, 0)
```

引脚 `P3.4` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）4：`GPIO`。

<a id="aecbc53340aefc0c7177839de1f8a3e4d"></a>

### `PIN_P3_4__I2C0_SCL_B`

```c
#define PIN_P3_4__I2C0_SCL_B ALIF_PINMUX(3, 4, 5)
```

端口（Port）3 的引脚（Pin）4：`I2C0_SCL_B`。

<a id="adb9a325b5eb089330ba3c4e33396f8fe"></a>

### `PIN_P3_4__I2S1_SCLK_A`

```c
#define PIN_P3_4__I2S1_SCLK_A ALIF_PINMUX(3, 4, 4)
```

端口（Port）3 的引脚（Pin）4：`I2S1_SCLK_A`。

<a id="a9927106dac12e76682f04fb72f9696a4"></a>

### `PIN_P3_4__LPPDM_CO_B`

```c
#define PIN_P3_4__LPPDM_CO_B ALIF_PINMUX(3, 4, 3)
```

端口（Port）3 的引脚（Pin）4：`LPPDM_CO_B`。

<a id="aa814da0a75dab71857b6a875e2a60508"></a>

### `PIN_P3_4__OSPI0_RXDS_B`

```c
#define PIN_P3_4__OSPI0_RXDS_B ALIF_PINMUX(3, 4, 1)
```

端口（Port）3 的引脚（Pin）4：`OSPI0_RXDS_B`。

<a id="ad6e6395511f3c3839a42f634893ee164"></a>

### `PIN_P3_4__QEC1_Y_A`

```c
#define PIN_P3_4__QEC1_Y_A ALIF_PINMUX(3, 4, 6)
```

端口（Port）3 的引脚（Pin）4：`QEC1_Y_A`。

<a id="a8e810a67528a4d5be263dd1f9ad5010e"></a>

### `PIN_P3_4__UART5_RX_A`

```c
#define PIN_P3_4__UART5_RX_A ALIF_PINMUX(3, 4, 2)
```

端口（Port）3 的引脚（Pin）4：`UART5_RX_A`。

<a id="aeaa8655a99307bee669e168ef00aebf3"></a>

### `PIN_P3_5__CAM_D9_A`

```c
#define PIN_P3_5__CAM_D9_A ALIF_PINMUX(3, 5, 7)
```

端口（Port）3 的引脚（Pin）5：`CAM_D9_A`。

<a id="a3f53dddbffc228108e7c1eb17ee058a4"></a>

### `PIN_P3_5__GPIO`

```c
#define PIN_P3_5__GPIO ALIF_PINMUX(3, 5, 0)
```

引脚 `P3.5` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）5：`GPIO`。

<a id="a775a93715f9a556bbb359bc9d4483a0e"></a>

### `PIN_P3_5__I2C0_SDA_B`

```c
#define PIN_P3_5__I2C0_SDA_B ALIF_PINMUX(3, 5, 5)
```

端口（Port）3 的引脚（Pin）5：`I2C0_SDA_B`。

<a id="a7cf933b9c6211dd08668b2132b7fcb01"></a>

### `PIN_P3_5__LPPDM_DO_B`

```c
#define PIN_P3_5__LPPDM_DO_B ALIF_PINMUX(3, 5, 3)
```

端口（Port）3 的引脚（Pin）5：`LPPDM_DO_B`。

<a id="a7fc7acde9b754dffdaa864b5ee54fb44"></a>

### `PIN_P3_5__OSPI0_SCLKN_A`

```c
#define PIN_P3_5__OSPI0_SCLKN_A ALIF_PINMUX(3, 5, 1)
```

端口（Port）3 的引脚（Pin）5：`OSPI0_SCLKN_A`。

<a id="ac36f03cf5b7982ca0f93cc6f72166a8a"></a>

### `PIN_P3_5__QEC1_Z_A`

```c
#define PIN_P3_5__QEC1_Z_A ALIF_PINMUX(3, 5, 6)
```

端口（Port）3 的引脚（Pin）5：`QEC1_Z_A`。

<a id="a305645868ca565ed269a48043a6fb2d9"></a>

### `PIN_P3_5__SPI0_SS1_B`

```c
#define PIN_P3_5__SPI0_SS1_B ALIF_PINMUX(3, 5, 4)
```

端口（Port）3 的引脚（Pin）5：`SPI0_SS1_B`。

<a id="a089bc9a32dfe0c666bf67b1da11c200a"></a>

### `PIN_P3_5__UART5_TX_A`

```c
#define PIN_P3_5__UART5_TX_A ALIF_PINMUX(3, 5, 2)
```

端口（Port）3 的引脚（Pin）5：`UART5_TX_A`。

<a id="a3f1fdd1c8aaf26eb18c13ed71a5eb26a"></a>

### `PIN_P3_6__CAM_D10_A`

```c
#define PIN_P3_6__CAM_D10_A ALIF_PINMUX(3, 6, 7)
```

端口（Port）3 的引脚（Pin）6：`CAM_D10_A`。

<a id="a6de92753c75d2827828767a9ed529829"></a>

### `PIN_P3_6__GPIO`

```c
#define PIN_P3_6__GPIO ALIF_PINMUX(3, 6, 0)
```

引脚 `P3.6` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）6：`GPIO`。

<a id="a8dcc9473cc0421a6fc13f955d766706c"></a>

### `PIN_P3_6__HFXO_OUT_A`

```c
#define PIN_P3_6__HFXO_OUT_A ALIF_PINMUX(3, 6, 1)
```

端口（Port）3 的引脚（Pin）6：`HFXO_OUT_A`。

<a id="ab8537cba85090cfc2c9bbe72c6c7ccb7"></a>

### `PIN_P3_6__I2C1_SDA_B`

```c
#define PIN_P3_6__I2C1_SDA_B ALIF_PINMUX(3, 6, 5)
```

端口（Port）3 的引脚（Pin）6：`I2C1_SDA_B`。

<a id="aec50fbbc0ef5faf9e7f65e7a5975b273"></a>

### `PIN_P3_6__LPPDM_C1_B`

```c
#define PIN_P3_6__LPPDM_C1_B ALIF_PINMUX(3, 6, 3)
```

端口（Port）3 的引脚（Pin）6：`LPPDM_C1_B`。

<a id="ae73382d7e3ca133ff282b1f281d19cf2"></a>

### `PIN_P3_6__LPUART_CTS_B`

```c
#define PIN_P3_6__LPUART_CTS_B ALIF_PINMUX(3, 6, 2)
```

端口（Port）3 的引脚（Pin）6：`LPUART_CTS_B`。

<a id="af2adbee156a78c5c61512c7376bd39fb"></a>

### `PIN_P3_6__QEC2_X_A`

```c
#define PIN_P3_6__QEC2_X_A ALIF_PINMUX(3, 6, 6)
```

端口（Port）3 的引脚（Pin）6：`QEC2_X_A`。

<a id="a4474c1dae558d0a9ce5f113eab5c60ea"></a>

### `PIN_P3_6__SPI0_SS2_B`

```c
#define PIN_P3_6__SPI0_SS2_B ALIF_PINMUX(3, 6, 4)
```

端口（Port）3 的引脚（Pin）6：`SPI0_SS2_B`。

<a id="a48aaf47242ae02df16dd1689f6c5f155"></a>

### `PIN_P3_7__CAM_D11_A`

```c
#define PIN_P3_7__CAM_D11_A ALIF_PINMUX(3, 7, 7)
```

端口（Port）3 的引脚（Pin）7：`CAM_D11_A`。

<a id="a60d3cb4a00a06169c18eedd0593c0e3b"></a>

### `PIN_P3_7__GPIO`

```c
#define PIN_P3_7__GPIO ALIF_PINMUX(3, 7, 0)
```

引脚 `P3.7` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）7：`GPIO`。

<a id="af3466c0dca56a62cb762174d47b85118"></a>

### `PIN_P3_7__I2C1_SCL_B`

```c
#define PIN_P3_7__I2C1_SCL_B ALIF_PINMUX(3, 7, 5)
```

端口（Port）3 的引脚（Pin）7：`I2C1_SCL_B`。

<a id="a92596105a0f8236c4ef8cfc58580ce2a"></a>

### `PIN_P3_7__JTAG0_TRACECLK`

```c
#define PIN_P3_7__JTAG0_TRACECLK ALIF_PINMUX(3, 7, 1)
```

端口（Port）3 的引脚（Pin）7：`JTAG0_TRACECLK`。

<a id="a5d9255b7352d89afc3c8c43139d0ca2d"></a>

### `PIN_P3_7__LPPDM_D1_B`

```c
#define PIN_P3_7__LPPDM_D1_B ALIF_PINMUX(3, 7, 3)
```

端口（Port）3 的引脚（Pin）7：`LPPDM_D1_B`。

<a id="aca12188c280e9b043eb8af55b2b4bbf0"></a>

### `PIN_P3_7__LPUART_RTS_B`

```c
#define PIN_P3_7__LPUART_RTS_B ALIF_PINMUX(3, 7, 2)
```

端口（Port）3 的引脚（Pin）7：`LPUART_RTS_B`。

<a id="aa3c253cd1c5a3247ab412596d853c5f5"></a>

### `PIN_P3_7__QEC2_Y_A`

```c
#define PIN_P3_7__QEC2_Y_A ALIF_PINMUX(3, 7, 6)
```

端口（Port）3 的引脚（Pin）7：`QEC2_Y_A`。

<a id="affc5f0a75e96cc6327cec31adb4fb9d7"></a>

### `PIN_P3_7__SPI1_SS1_A`

```c
#define PIN_P3_7__SPI1_SS1_A ALIF_PINMUX(3, 7, 4)
```

端口（Port）3 的引脚（Pin）7：`SPI1_SS1_A`。

<a id="a4d64ab7e7d18c8f20d0cf177adf1b89b"></a>

### `PIN_P4_0__APLL_OUT_A`

```c
#define PIN_P4_0__APLL_OUT_A ALIF_PINMUX(4, 0, 2)
```

端口（Port）4 的引脚（Pin）0：`APLL_OUT_A`。

<a id="a3bb26e78e1b13d1b8334f62837a6d634"></a>

### `PIN_P4_0__CAM_D12_A`

```c
#define PIN_P4_0__CAM_D12_A ALIF_PINMUX(4, 0, 7)
```

端口（Port）4 的引脚（Pin）0：`CAM_D12_A`。

<a id="a2e463cc07539e43e956355a907627b26"></a>

### `PIN_P4_0__CDC_VSYNC_B`

```c
#define PIN_P4_0__CDC_VSYNC_B ALIF_PINMUX(4, 0, 6)
```

端口（Port）4 的引脚（Pin）0：`CDC_VSYNC_B`。

<a id="a1ab2ef5cf337828d3e4be24bba3391e6"></a>

### `PIN_P4_0__GPIO`

```c
#define PIN_P4_0__GPIO ALIF_PINMUX(4, 0, 0)
```

引脚 `P4.0` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）0：`GPIO`。

<a id="ab74dba96fd07a01a87937196a9cf5e37"></a>

### `PIN_P4_0__I2S1_WS_A`

```c
#define PIN_P4_0__I2S1_WS_A ALIF_PINMUX(4, 0, 3)
```

端口（Port）4 的引脚（Pin）0：`I2S1_WS_A`。

<a id="a86076829771e261af384c66974a9f7ff"></a>

### `PIN_P4_0__JTAG0_TDATA0`

```c
#define PIN_P4_0__JTAG0_TDATA0 ALIF_PINMUX(4, 0, 1)
```

端口（Port）4 的引脚（Pin）0：`JTAG0_TDATA0`。

<a id="a1de41f5582dd807e013ab8bfc440aba6"></a>

### `PIN_P4_0__QEC2_Z_A`

```c
#define PIN_P4_0__QEC2_Z_A ALIF_PINMUX(4, 0, 5)
```

端口（Port）4 的引脚（Pin）0：`QEC2_Z_A`。

<a id="a1dc4196c647c8e6b06737779c81ccbca"></a>

### `PIN_P4_0__SPI1_SS2_A`

```c
#define PIN_P4_0__SPI1_SS2_A ALIF_PINMUX(4, 0, 4)
```

端口（Port）4 的引脚（Pin）0：`SPI1_SS2_A`。

<a id="a446e9e914f59c6daa81d90d4929f7a3e"></a>

### `PIN_P4_1__CAM_D13_A`

```c
#define PIN_P4_1__CAM_D13_A ALIF_PINMUX(4, 1, 7)
```

端口（Port）4 的引脚（Pin）1：`CAM_D13_A`。

<a id="a81411c54132629886379f9795f0d3504"></a>

### `PIN_P4_1__CDC_HSYNC_B`

```c
#define PIN_P4_1__CDC_HSYNC_B ALIF_PINMUX(4, 1, 6)
```

端口（Port）4 的引脚（Pin）1：`CDC_HSYNC_B`。

<a id="a5fb4375020986c6656759f3223558f10"></a>

### `PIN_P4_1__GPIO`

```c
#define PIN_P4_1__GPIO ALIF_PINMUX(4, 1, 0)
```

引脚 `P4.1` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）1：`GPIO`。

<a id="aecb4db0667f7c228780c1eb21e7ebc67"></a>

### `PIN_P4_1__I2S0_SDI_B`

```c
#define PIN_P4_1__I2S0_SDI_B ALIF_PINMUX(4, 1, 2)
```

端口（Port）4 的引脚（Pin）1：`I2S0_SDI_B`。

<a id="ae3bdf81bc183b5b5f91d6e1cdff0ed9e"></a>

### `PIN_P4_1__JTAG0_TDATA1`

```c
#define PIN_P4_1__JTAG0_TDATA1 ALIF_PINMUX(4, 1, 1)
```

端口（Port）4 的引脚（Pin）1：`JTAG0_TDATA1`。

<a id="a33cf5fdcb6246f20e11294e3fe2ee5a8"></a>

### `PIN_P4_1__QEC3_X_A`

```c
#define PIN_P4_1__QEC3_X_A ALIF_PINMUX(4, 1, 4)
```

端口（Port）4 的引脚（Pin）1：`QEC3_X_A`。

<a id="a1cfa948cf149c9975a5a90f557f2ca5d"></a>

### `PIN_P4_1__SD_CLK_D`

```c
#define PIN_P4_1__SD_CLK_D ALIF_PINMUX(4, 1, 5)
```

端口（Port）4 的引脚（Pin）1：`SD_CLK_D`。

<a id="a724a7b36c0c03d06956eed86d907d195"></a>

### `PIN_P4_1__SPI1_SS3_A`

```c
#define PIN_P4_1__SPI1_SS3_A ALIF_PINMUX(4, 1, 3)
```

端口（Port）4 的引脚（Pin）1：`SPI1_SS3_A`。

<a id="a0354de3c1060268335afbded61177cc8"></a>

### `PIN_P4_2__CAM_D14_A`

```c
#define PIN_P4_2__CAM_D14_A ALIF_PINMUX(4, 2, 7)
```

端口（Port）4 的引脚（Pin）2：`CAM_D14_A`。

<a id="a2a9f0b7627d1f0149fa1cddc428e76f9"></a>

### `PIN_P4_2__GPIO`

```c
#define PIN_P4_2__GPIO ALIF_PINMUX(4, 2, 0)
```

引脚 `P4.2` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）2：`GPIO`。

<a id="a78f480ef1aa0d692eba930bceec76518"></a>

### `PIN_P4_2__I2S0_SDO_B`

```c
#define PIN_P4_2__I2S0_SDO_B ALIF_PINMUX(4, 2, 3)
```

端口（Port）4 的引脚（Pin）2：`I2S0_SDO_B`。

<a id="ad6ac79e681a0c110e38afde11bde0a91"></a>

### `PIN_P4_2__JTAG0_TDATA2`

```c
#define PIN_P4_2__JTAG0_TDATA2 ALIF_PINMUX(4, 2, 1)
```

端口（Port）4 的引脚（Pin）2：`JTAG0_TDATA2`。

<a id="a4826bd5accf8c5c35b4c9375ef68001f"></a>

### `PIN_P4_2__LPI2C1_SDA_A`

```c
#define PIN_P4_2__LPI2C1_SDA_A ALIF_PINMUX(4, 2, 2)
```

端口（Port）4 的引脚（Pin）2：`LPI2C1_SDA_A`。

<a id="a5d88b8bf2baae0426adfc982f54d7bd4"></a>

### `PIN_P4_2__QEC3_Y_A`

```c
#define PIN_P4_2__QEC3_Y_A ALIF_PINMUX(4, 2, 5)
```

端口（Port）4 的引脚（Pin）2：`QEC3_Y_A`。

<a id="a2a14d7d416fad7d60af53778a4b08edd"></a>

### `PIN_P4_2__SD_CMD_D`

```c
#define PIN_P4_2__SD_CMD_D ALIF_PINMUX(4, 2, 6)
```

端口（Port）4 的引脚（Pin）2：`SD_CMD_D`。

<a id="a2540b24293afcf26019769d63cf1a3fe"></a>

### `PIN_P4_2__SPI2_MISO_A`

```c
#define PIN_P4_2__SPI2_MISO_A ALIF_PINMUX(4, 2, 4)
```

端口（Port）4 的引脚（Pin）2：`SPI2_MISO_A`。

<a id="a6c31bd33f5f9199591339b4cbbf3a0f9"></a>

### `PIN_P4_3__CAM_D15_A`

```c
#define PIN_P4_3__CAM_D15_A ALIF_PINMUX(4, 3, 7)
```

端口（Port）4 的引脚（Pin）3：`CAM_D15_A`。

<a id="a97b4675f5259e06d48cdd30755a46f3e"></a>

### `PIN_P4_3__GPIO`

```c
#define PIN_P4_3__GPIO ALIF_PINMUX(4, 3, 0)
```

引脚 `P4.3` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）3：`GPIO`。

<a id="aa00669ae9c9416a1cc1c47311a5d8c93"></a>

### `PIN_P4_3__I2S0_SCLK_B`

```c
#define PIN_P4_3__I2S0_SCLK_B ALIF_PINMUX(4, 3, 3)
```

端口（Port）4 的引脚（Pin）3：`I2S0_SCLK_B`。

<a id="a2fcaaedf7a85609b19db31228eaed463"></a>

### `PIN_P4_3__JTAG0_TDATA3`

```c
#define PIN_P4_3__JTAG0_TDATA3 ALIF_PINMUX(4, 3, 1)
```

端口（Port）4 的引脚（Pin）3：`JTAG0_TDATA3`。

<a id="a3f6bdede6384a4038847b2272472c6a1"></a>

### `PIN_P4_3__LPI2C1_SCL_A`

```c
#define PIN_P4_3__LPI2C1_SCL_A ALIF_PINMUX(4, 3, 2)
```

端口（Port）4 的引脚（Pin）3：`LPI2C1_SCL_A`。

<a id="aedca512b9e51012bb05f50b67d045ee1"></a>

### `PIN_P4_3__QEC3_Z_A`

```c
#define PIN_P4_3__QEC3_Z_A ALIF_PINMUX(4, 3, 5)
```

端口（Port）4 的引脚（Pin）3：`QEC3_Z_A`。

<a id="a9f5b8736ca866c11f10d09d22ccdc2fd"></a>

### `PIN_P4_3__SD_RST_D`

```c
#define PIN_P4_3__SD_RST_D ALIF_PINMUX(4, 3, 6)
```

端口（Port）4 的引脚（Pin）3：`SD_RST_D`。

<a id="af3e803ca5495352c98a07f1451b13f55"></a>

### `PIN_P4_3__SPI2_MOSI_A`

```c
#define PIN_P4_3__SPI2_MOSI_A ALIF_PINMUX(4, 3, 4)
```

端口（Port）4 的引脚（Pin）3：`SPI2_MOSI_A`。

<a id="ac444c571b0be2a2a8683c04da4db9a85"></a>

### `PIN_P4_4__FAULT0_A`

```c
#define PIN_P4_4__FAULT0_A ALIF_PINMUX(4, 4, 4)
```

端口（Port）4 的引脚（Pin）4：`FAULT0_A`。

<a id="a71f56da2cfc34a4fa6dbbba7e9936d28"></a>

### `PIN_P4_4__GPIO`

```c
#define PIN_P4_4__GPIO ALIF_PINMUX(4, 4, 0)
```

引脚 `P4.4` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）4：`GPIO`。

<a id="a517a020d5c948995364f2312904b6018"></a>

### `PIN_P4_4__I2S0_WS_B`

```c
#define PIN_P4_4__I2S0_WS_B ALIF_PINMUX(4, 4, 2)
```

端口（Port）4 的引脚（Pin）4：`I2S0_WS_B`。

<a id="a026da00206cb806cf7e868c00dfa15de"></a>

### `PIN_P4_4__JTAG0_TCK`

```c
#define PIN_P4_4__JTAG0_TCK ALIF_PINMUX(4, 4, 1)
```

端口（Port）4 的引脚（Pin）4：`JTAG0_TCK`。

<a id="af5dff5e905e521347a9a9571c4fa6361"></a>

### `PIN_P4_4__SPI2_SCLK_A`

```c
#define PIN_P4_4__SPI2_SCLK_A ALIF_PINMUX(4, 4, 3)
```

端口（Port）4 的引脚（Pin）4：`SPI2_SCLK_A`。

<a id="afeedeeea96759b383282b0304e66941c"></a>

### `PIN_P4_5__FAULT1_A`

```c
#define PIN_P4_5__FAULT1_A ALIF_PINMUX(4, 5, 3)
```

端口（Port）4 的引脚（Pin）5：`FAULT1_A`。

<a id="a44781940091d6eadb753aa098a1c8a3a"></a>

### `PIN_P4_5__GPIO`

```c
#define PIN_P4_5__GPIO ALIF_PINMUX(4, 5, 0)
```

引脚 `P4.5` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）5：`GPIO`。

<a id="ac8c66019ed9ef1f3e1761b9676666d7c"></a>

### `PIN_P4_5__JTAG0_TMS`

```c
#define PIN_P4_5__JTAG0_TMS ALIF_PINMUX(4, 5, 1)
```

端口（Port）4 的引脚（Pin）5：`JTAG0_TMS`。

<a id="a96b572900d599f788751338a196db2ee"></a>

### `PIN_P4_5__SPI2_SS0_A`

```c
#define PIN_P4_5__SPI2_SS0_A ALIF_PINMUX(4, 5, 2)
```

端口（Port）4 的引脚（Pin）5：`SPI2_SS0_A`。

<a id="a4b838a52a7d7b92372f93c33d5ce32e8"></a>

### `PIN_P4_6__FAULT2_A`

```c
#define PIN_P4_6__FAULT2_A ALIF_PINMUX(4, 6, 3)
```

端口（Port）4 的引脚（Pin）6：`FAULT2_A`。

<a id="aae4c2f3f2743c6281127d761c2d3c952"></a>

### `PIN_P4_6__GPIO`

```c
#define PIN_P4_6__GPIO ALIF_PINMUX(4, 6, 0)
```

引脚 `P4.6` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）6：`GPIO`。

<a id="a64e905aad463ddb010ef5e31aa4bb355"></a>

### `PIN_P4_6__JTAG0_TDI`

```c
#define PIN_P4_6__JTAG0_TDI ALIF_PINMUX(4, 6, 1)
```

端口（Port）4 的引脚（Pin）6：`JTAG0_TDI`。

<a id="ada6fe7a94f5948aa450c52df17a1f6d3"></a>

### `PIN_P4_6__SPI2_SS1_A`

```c
#define PIN_P4_6__SPI2_SS1_A ALIF_PINMUX(4, 6, 2)
```

端口（Port）4 的引脚（Pin）6：`SPI2_SS1_A`。

<a id="a3708d4f0c3187f5c3e82e7be8d5b7e88"></a>

### `PIN_P4_7__FAULT3_A`

```c
#define PIN_P4_7__FAULT3_A ALIF_PINMUX(4, 7, 3)
```

端口（Port）4 的引脚（Pin）7：`FAULT3_A`。

<a id="a414ee602068915040eb8dab92a92bb61"></a>

### `PIN_P4_7__GPIO`

```c
#define PIN_P4_7__GPIO ALIF_PINMUX(4, 7, 0)
```

引脚 `P4.7` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）7：`GPIO`。

<a id="a1882c539a53276d676235207bd87494a"></a>

### `PIN_P4_7__JTAG0_TDO`

```c
#define PIN_P4_7__JTAG0_TDO ALIF_PINMUX(4, 7, 1)
```

端口（Port）4 的引脚（Pin）7：`JTAG0_TDO`。

<a id="a7f053b743ad776d35543bbd4aeed4291"></a>

### `PIN_P4_7__SPI2_SS2_A`

```c
#define PIN_P4_7__SPI2_SS2_A ALIF_PINMUX(4, 7, 2)
```

端口（Port）4 的引脚（Pin）7：`SPI2_SS2_A`。

<a id="a456e61913b22b9d8a56be8b0377ac81e"></a>

### `PIN_P5_0__GPIO`

```c
#define PIN_P5_0__GPIO ALIF_PINMUX(5, 0, 0)
```

引脚 `P5.0` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）0：`GPIO`。

<a id="a0a3d80a4b6d1716af1ad5ed469920c64"></a>

### `PIN_P5_0__I2C2_SDA_B`

```c
#define PIN_P5_0__I2C2_SDA_B ALIF_PINMUX(5, 0, 5)
```

端口（Port）5 的引脚（Pin）0：`I2C2_SDA_B`。

<a id="a38d38f8ae3bae90deab3ce80caf0ee09"></a>

### `PIN_P5_0__OSPI1_RXDS_A`

```c
#define PIN_P5_0__OSPI1_RXDS_A ALIF_PINMUX(5, 0, 1)
```

端口（Port）5 的引脚（Pin）0：`OSPI1_RXDS_A`。

<a id="a8251fa8634b4fca0caee874df82c0fe3"></a>

### `PIN_P5_0__PDM_D2_A`

```c
#define PIN_P5_0__PDM_D2_A ALIF_PINMUX(5, 0, 3)
```

端口（Port）5 的引脚（Pin）0：`PDM_D2_A`。

<a id="a2e92a4a046037ece8270c1279d22c177"></a>

### `PIN_P5_0__SD_D0_A`

```c
#define PIN_P5_0__SD_D0_A ALIF_PINMUX(5, 0, 7)
```

端口（Port）5 的引脚（Pin）0：`SD_D0_A`。

<a id="a8d7a46642529764190d788a4e6fd45ad"></a>

### `PIN_P5_0__SPI0_MISO_B`

```c
#define PIN_P5_0__SPI0_MISO_B ALIF_PINMUX(5, 0, 4)
```

端口（Port）5 的引脚（Pin）0：`SPI0_MISO_B`。

<a id="ae55f7b3bba263faff5336e5e704e68a1"></a>

### `PIN_P5_0__UART4_RX_C`

```c
#define PIN_P5_0__UART4_RX_C ALIF_PINMUX(5, 0, 2)
```

端口（Port）5 的引脚（Pin）0：`UART4_RX_C`。

<a id="a5d9ca9901b30db06b82c4b24f4b9a080"></a>

### `PIN_P5_0__UT0_T0_B`

```c
#define PIN_P5_0__UT0_T0_B ALIF_PINMUX(5, 0, 6)
```

端口（Port）5 的引脚（Pin）0：`UT0_T0_B`。

<a id="a98fa74bbdae6f1f210c490cdc73d7cb8"></a>

### `PIN_P5_1__GPIO`

```c
#define PIN_P5_1__GPIO ALIF_PINMUX(5, 1, 0)
```

引脚 `P5.1` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）1：`GPIO`。

<a id="a337b1b86add6bae57f8f3cf3e6b0316e"></a>

### `PIN_P5_1__I2C2_SCL_B`

```c
#define PIN_P5_1__I2C2_SCL_B ALIF_PINMUX(5, 1, 5)
```

端口（Port）5 的引脚（Pin）1：`I2C2_SCL_B`。

<a id="abe8b3c1281f707f6d860126f3ce452f5"></a>

### `PIN_P5_1__OSPI1_SS0_A`

```c
#define PIN_P5_1__OSPI1_SS0_A ALIF_PINMUX(5, 1, 1)
```

端口（Port）5 的引脚（Pin）1：`OSPI1_SS0_A`。

<a id="a6d88b7b2fe07955ec419faef9b0fc542"></a>

### `PIN_P5_1__PDM_D3_A`

```c
#define PIN_P5_1__PDM_D3_A ALIF_PINMUX(5, 1, 3)
```

端口（Port）5 的引脚（Pin）1：`PDM_D3_A`。

<a id="ad23c4691fc9bc556d010d12280678018"></a>

### `PIN_P5_1__SD_D1_A`

```c
#define PIN_P5_1__SD_D1_A ALIF_PINMUX(5, 1, 7)
```

端口（Port）5 的引脚（Pin）1：`SD_D1_A`。

<a id="a02c0d84f1ce09a7db4f16344ce7d6e0f"></a>

### `PIN_P5_1__SPI0_MOSI_B`

```c
#define PIN_P5_1__SPI0_MOSI_B ALIF_PINMUX(5, 1, 4)
```

端口（Port）5 的引脚（Pin）1：`SPI0_MOSI_B`。

<a id="aaaf94476a9b2113d129e1357b61cab88"></a>

### `PIN_P5_1__UART4_TX_C`

```c
#define PIN_P5_1__UART4_TX_C ALIF_PINMUX(5, 1, 2)
```

端口（Port）5 的引脚（Pin）1：`UART4_TX_C`。

<a id="a576645eb18a7f9b249aa745cdf2763bd"></a>

### `PIN_P5_1__UT0_T1_B`

```c
#define PIN_P5_1__UT0_T1_B ALIF_PINMUX(5, 1, 6)
```

端口（Port）5 的引脚（Pin）1：`UT0_T1_B`。

<a id="a97a74c55bf53c437a39b3f10cfa778bc"></a>

### `PIN_P5_2__GPIO`

```c
#define PIN_P5_2__GPIO ALIF_PINMUX(5, 2, 0)
```

引脚 `P5.2` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）2：`GPIO`。

<a id="a892bb2cd62f830b62180a28935584442"></a>

### `PIN_P5_2__LPI2C0_SCL_B`

```c
#define PIN_P5_2__LPI2C0_SCL_B ALIF_PINMUX(5, 2, 5)
```

端口（Port）5 的引脚（Pin）2：`LPI2C0_SCL_B`。

<a id="aeb292ae2d7a8c7fe6fcc98e89383d5bd"></a>

### `PIN_P5_2__OSPI1_SCLKN_A`

```c
#define PIN_P5_2__OSPI1_SCLKN_A ALIF_PINMUX(5, 2, 1)
```

端口（Port）5 的引脚（Pin）2：`OSPI1_SCLKN_A`。

<a id="a92b9e7a2225b7430c821afff772501b1"></a>

### `PIN_P5_2__PDM_C3_A`

```c
#define PIN_P5_2__PDM_C3_A ALIF_PINMUX(5, 2, 3)
```

端口（Port）5 的引脚（Pin）2：`PDM_C3_A`。

<a id="a2c66e34e62616968081d9b785c298e89"></a>

### `PIN_P5_2__SD_D2_A`

```c
#define PIN_P5_2__SD_D2_A ALIF_PINMUX(5, 2, 7)
```

端口（Port）5 的引脚（Pin）2：`SD_D2_A`。

<a id="ab94c708fa67f401c517167652262ee25"></a>

### `PIN_P5_2__SPI0_SS0_B`

```c
#define PIN_P5_2__SPI0_SS0_B ALIF_PINMUX(5, 2, 4)
```

端口（Port）5 的引脚（Pin）2：`SPI0_SS0_B`。

<a id="ab92d5af8661fa39bb5c5344fe8b5c5d2"></a>

### `PIN_P5_2__UART5_RX_C`

```c
#define PIN_P5_2__UART5_RX_C ALIF_PINMUX(5, 2, 2)
```

端口（Port）5 的引脚（Pin）2：`UART5_RX_C`。

<a id="a65e944abdcb0b4d0eec9d47cdc5ea36f"></a>

### `PIN_P5_2__UT1_T0_B`

```c
#define PIN_P5_2__UT1_T0_B ALIF_PINMUX(5, 2, 6)
```

端口（Port）5 的引脚（Pin）2：`UT1_T0_B`。

<a id="a238189907f455451e5d023d257b36ec0"></a>

### `PIN_P5_3__CDC_PCLK_A`

```c
#define PIN_P5_3__CDC_PCLK_A ALIF_PINMUX(5, 3, 7)
```

端口（Port）5 的引脚（Pin）3：`CDC_PCLK_A`。

<a id="af2c171dfdada8390ed0c80e115f024eb"></a>

### `PIN_P5_3__GPIO`

```c
#define PIN_P5_3__GPIO ALIF_PINMUX(5, 3, 0)
```

引脚 `P5.3` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）3：`GPIO`。

<a id="a2c4599b05f666b7ea53515be543afc47"></a>

### `PIN_P5_3__LPI2C0_SDA_B`

```c
#define PIN_P5_3__LPI2C0_SDA_B ALIF_PINMUX(5, 3, 4)
```

端口（Port）5 的引脚（Pin）3：`LPI2C0_SDA_B`。

<a id="ad770693b035fa8cdcf85199cdb6296f8"></a>

### `PIN_P5_3__OSPI1_SCLK_A`

```c
#define PIN_P5_3__OSPI1_SCLK_A ALIF_PINMUX(5, 3, 1)
```

端口（Port）5 的引脚（Pin）3：`OSPI1_SCLK_A`。

<a id="aab6554ba3e217bd60c778793a0637938"></a>

### `PIN_P5_3__SD_D3_A`

```c
#define PIN_P5_3__SD_D3_A ALIF_PINMUX(5, 3, 6)
```

端口（Port）5 的引脚（Pin）3：`SD_D3_A`。

<a id="a1bbacbdb5ebd7073e5dc46bdafa49467"></a>

### `PIN_P5_3__SPI0_SCLK_B`

```c
#define PIN_P5_3__SPI0_SCLK_B ALIF_PINMUX(5, 3, 3)
```

端口（Port）5 的引脚（Pin）3：`SPI0_SCLK_B`。

<a id="a984109f4b5194e919517f1a88ce2f173"></a>

### `PIN_P5_3__UART5_TX_C`

```c
#define PIN_P5_3__UART5_TX_C ALIF_PINMUX(5, 3, 2)
```

端口（Port）5 的引脚（Pin）3：`UART5_TX_C`。

<a id="a7cf30f670a605528e535e100cc7d6259"></a>

### `PIN_P5_3__UT1_T1_B`

```c
#define PIN_P5_3__UT1_T1_B ALIF_PINMUX(5, 3, 5)
```

端口（Port）5 的引脚（Pin）3：`UT1_T1_B`。

<a id="ab777f9158aae4ce2654f7b62430e50df"></a>

### `PIN_P5_4__CDC_DE_A`

```c
#define PIN_P5_4__CDC_DE_A ALIF_PINMUX(5, 4, 7)
```

端口（Port）5 的引脚（Pin）4：`CDC_DE_A`。

<a id="a6846e3f2b170cb7a3216f81e5ec3b30e"></a>

### `PIN_P5_4__GPIO`

```c
#define PIN_P5_4__GPIO ALIF_PINMUX(5, 4, 0)
```

引脚 `P5.4` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）4：`GPIO`。

<a id="a24bae128d43897cb5ad1e4e1fbeb9999"></a>

### `PIN_P5_4__OSPI1_SS1_A`

```c
#define PIN_P5_4__OSPI1_SS1_A ALIF_PINMUX(5, 4, 1)
```

端口（Port）5 的引脚（Pin）4：`OSPI1_SS1_A`。

<a id="a7e382ce13d0f82f75edfb660eba65867"></a>

### `PIN_P5_4__PDM_D2_B`

```c
#define PIN_P5_4__PDM_D2_B ALIF_PINMUX(5, 4, 3)
```

端口（Port）5 的引脚（Pin）4：`PDM_D2_B`。

<a id="a7293d170665dd2c6a04a211939a39134"></a>

### `PIN_P5_4__SD_D4_A`

```c
#define PIN_P5_4__SD_D4_A ALIF_PINMUX(5, 4, 6)
```

端口（Port）5 的引脚（Pin）4：`SD_D4_A`。

<a id="ae8083b7bfacd1411f63cda33c47fbd8a"></a>

### `PIN_P5_4__SPI0_SS3_A`

```c
#define PIN_P5_4__SPI0_SS3_A ALIF_PINMUX(5, 4, 4)
```

端口（Port）5 的引脚（Pin）4：`SPI0_SS3_A`。

<a id="ae8575f29fe033284403815de52e2b0b1"></a>

### `PIN_P5_4__UART3_CTS_A`

```c
#define PIN_P5_4__UART3_CTS_A ALIF_PINMUX(5, 4, 2)
```

端口（Port）5 的引脚（Pin）4：`UART3_CTS_A`。

<a id="a1ab3ffb8876342ce40588a35cded4e04"></a>

### `PIN_P5_4__UT2_T0_B`

```c
#define PIN_P5_4__UT2_T0_B ALIF_PINMUX(5, 4, 5)
```

端口（Port）5 的引脚（Pin）4：`UT2_T0_B`。

<a id="ab8c45949da634838ed5ab9cd77d5e108"></a>

### `PIN_P5_5__CDC_HSYNC_A`

```c
#define PIN_P5_5__CDC_HSYNC_A ALIF_PINMUX(5, 5, 7)
```

端口（Port）5 的引脚（Pin）5：`CDC_HSYNC_A`。

<a id="a5fe74885176a43241bd56514eb40a78d"></a>

### `PIN_P5_5__ETH_RXD0_A`

```c
#define PIN_P5_5__ETH_RXD0_A ALIF_PINMUX(5, 5, 6)
```

端口（Port）5 的引脚（Pin）5：`ETH_RXD0_A`。

<a id="a466c951ce8310bac71e4a36b062e3b48"></a>

### `PIN_P5_5__GPIO`

```c
#define PIN_P5_5__GPIO ALIF_PINMUX(5, 5, 0)
```

引脚 `P5.5` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）5：`GPIO`。

<a id="a8f88bd645e38b86560892fea67bd768e"></a>

### `PIN_P5_5__OSPI1_SCLK_C`

```c
#define PIN_P5_5__OSPI1_SCLK_C ALIF_PINMUX(5, 5, 1)
```

端口（Port）5 的引脚（Pin）5：`OSPI1_SCLK_C`。

<a id="a0c81622ee140b8913502807a6c560792"></a>

### `PIN_P5_5__PDM_D3_B`

```c
#define PIN_P5_5__PDM_D3_B ALIF_PINMUX(5, 5, 3)
```

端口（Port）5 的引脚（Pin）5：`PDM_D3_B`。

<a id="aeb2cd7eebb652c43aa0f1809e816ecf0"></a>

### `PIN_P5_5__SD_D5_A`

```c
#define PIN_P5_5__SD_D5_A ALIF_PINMUX(5, 5, 5)
```

端口（Port）5 的引脚（Pin）5：`SD_D5_A`。

<a id="aefd41d2a46a675a37216980f16e2fd58"></a>

### `PIN_P5_5__UART3_RTS_A`

```c
#define PIN_P5_5__UART3_RTS_A ALIF_PINMUX(5, 5, 2)
```

端口（Port）5 的引脚（Pin）5：`UART3_RTS_A`。

<a id="a05e05aac0465080bbbff700323a68631"></a>

### `PIN_P5_5__UT2_T1_B`

```c
#define PIN_P5_5__UT2_T1_B ALIF_PINMUX(5, 5, 4)
```

端口（Port）5 的引脚（Pin）5：`UT2_T1_B`。

<a id="ad052d0128c64793bf06c8235680591bc"></a>

### `PIN_P5_6__CDC_VSYNC_A`

```c
#define PIN_P5_6__CDC_VSYNC_A ALIF_PINMUX(5, 6, 6)
```

端口（Port）5 的引脚（Pin）6：`CDC_VSYNC_A`。

<a id="a122c965e0d825860f500690c068010ad"></a>

### `PIN_P5_6__ETH_RXD1_A`

```c
#define PIN_P5_6__ETH_RXD1_A ALIF_PINMUX(5, 6, 5)
```

端口（Port）5 的引脚（Pin）6：`ETH_RXD1_A`。

<a id="acd3416c5b74cd24d02c29e3144d63436"></a>

### `PIN_P5_6__GPIO`

```c
#define PIN_P5_6__GPIO ALIF_PINMUX(5, 6, 0)
```

引脚 `P5.6` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）6：`GPIO`。

<a id="a7bb8e7df55124de4d1d5d1e0136ec791"></a>

### `PIN_P5_6__I2C2_SCL_C`

```c
#define PIN_P5_6__I2C2_SCL_C ALIF_PINMUX(5, 6, 2)
```

端口（Port）5 的引脚（Pin）6：`I2C2_SCL_C`。

<a id="a255d5c869e69a05f60dbd2545133d6db"></a>

### `PIN_P5_6__SD_D6_A`

```c
#define PIN_P5_6__SD_D6_A ALIF_PINMUX(5, 6, 4)
```

端口（Port）5 的引脚（Pin）6：`SD_D6_A`。

<a id="a3bd03266c3d91de23071a3d0241e97e3"></a>

### `PIN_P5_6__UART1_CTS_B`

```c
#define PIN_P5_6__UART1_CTS_B ALIF_PINMUX(5, 6, 1)
```

端口（Port）5 的引脚（Pin）6：`UART1_CTS_B`。

<a id="a3b51e56aff1116a7f78c72b8d105a4f3"></a>

### `PIN_P5_6__UT3_T0_B`

```c
#define PIN_P5_6__UT3_T0_B ALIF_PINMUX(5, 6, 3)
```

端口（Port）5 的引脚（Pin）6：`UT3_T0_B`。

<a id="af90659a4ef350cc3759d00d4cc2df529"></a>

### `PIN_P5_7__ETH_RST_A`

```c
#define PIN_P5_7__ETH_RST_A ALIF_PINMUX(5, 7, 6)
```

端口（Port）5 的引脚（Pin）7：`ETH_RST_A`。

<a id="abc168fa2810d9a33b66d8899581c97ed"></a>

### `PIN_P5_7__GPIO`

```c
#define PIN_P5_7__GPIO ALIF_PINMUX(5, 7, 0)
```

引脚 `P5.7` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）7：`GPIO`。

<a id="a1eafcfc5a29262235cfca353e2cec793"></a>

### `PIN_P5_7__I2C2_SDA_C`

```c
#define PIN_P5_7__I2C2_SDA_C ALIF_PINMUX(5, 7, 3)
```

端口（Port）5 的引脚（Pin）7：`I2C2_SDA_C`。

<a id="a10109fc6ff0b3958f2bfbb530e9ec192"></a>

### `PIN_P5_7__OSPI1_SS0_C`

```c
#define PIN_P5_7__OSPI1_SS0_C ALIF_PINMUX(5, 7, 1)
```

端口（Port）5 的引脚（Pin）7：`OSPI1_SS0_C`。

<a id="afd5e370c63d9395a646422f878defdb8"></a>

### `PIN_P5_7__SD_D7_A`

```c
#define PIN_P5_7__SD_D7_A ALIF_PINMUX(5, 7, 5)
```

端口（Port）5 的引脚（Pin）7：`SD_D7_A`。

<a id="a16337846b4c79f3bf2b8601bd2b97f91"></a>

### `PIN_P5_7__UART1_RTS_B`

```c
#define PIN_P5_7__UART1_RTS_B ALIF_PINMUX(5, 7, 2)
```

端口（Port）5 的引脚（Pin）7：`UART1_RTS_B`。

<a id="ae4fc1d80ddbf968fee17d1487bc3a1e8"></a>

### `PIN_P5_7__UT3_T1_B`

```c
#define PIN_P5_7__UT3_T1_B ALIF_PINMUX(5, 7, 4)
```

端口（Port）5 的引脚（Pin）7：`UT3_T1_B`。

<a id="aed149da5f699fd5c2a29cd5a12e08ab5"></a>

### `PIN_P6_0__ETH_TXD0_A`

```c
#define PIN_P6_0__ETH_TXD0_A ALIF_PINMUX(6, 0, 6)
```

端口（Port）6 的引脚（Pin）0：`ETH_TXD0_A`。

<a id="ae7ade9dfd32e609fb86f13f6525953fc"></a>

### `PIN_P6_0__GPIO`

```c
#define PIN_P6_0__GPIO ALIF_PINMUX(6, 0, 0)
```

引脚 `P6.0` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）0：`GPIO`。

<a id="ae69d866c114aa4304b207ece8b102c8b"></a>

### `PIN_P6_0__LPSPI_SS1_A`

```c
#define PIN_P6_0__LPSPI_SS1_A ALIF_PINMUX(6, 0, 7)
```

端口（Port）6 的引脚（Pin）0：`LPSPI_SS1_A`。

<a id="af006833ac80c14da05e6a4599a24ac61"></a>

### `PIN_P6_0__OSPI0_D0_C`

```c
#define PIN_P6_0__OSPI0_D0_C ALIF_PINMUX(6, 0, 1)
```

端口（Port）6 的引脚（Pin）0：`OSPI0_D0_C`。

<a id="a5b804aab91d3d453bfa99b86da3136be"></a>

### `PIN_P6_0__PDM_D0_C`

```c
#define PIN_P6_0__PDM_D0_C ALIF_PINMUX(6, 0, 3)
```

端口（Port）6 的引脚（Pin）0：`PDM_D0_C`。

<a id="a9cee6c3cc19b52912293b79a4a264d0e"></a>

### `PIN_P6_0__SD_D0_D`

```c
#define PIN_P6_0__SD_D0_D ALIF_PINMUX(6, 0, 5)
```

端口（Port）6 的引脚（Pin）0：`SD_D0_D`。

<a id="ada38a2f1ef366ed1e1bc1a7283a1181e"></a>

### `PIN_P6_0__UART4_DE_A`

```c
#define PIN_P6_0__UART4_DE_A ALIF_PINMUX(6, 0, 2)
```

端口（Port）6 的引脚（Pin）0：`UART4_DE_A`。

<a id="a402739f36398287a0c22a91323b91e04"></a>

### `PIN_P6_0__UT4_T0_B`

```c
#define PIN_P6_0__UT4_T0_B ALIF_PINMUX(6, 0, 4)
```

端口（Port）6 的引脚（Pin）0：`UT4_T0_B`。

<a id="a8dd66a2e9cdd82b4e68015167b7bdcbc"></a>

### `PIN_P6_1__ETH_TXD1_A`

```c
#define PIN_P6_1__ETH_TXD1_A ALIF_PINMUX(6, 1, 6)
```

端口（Port）6 的引脚（Pin）1：`ETH_TXD1_A`。

<a id="ad55f5467ffabdbffd5b51ddfeaed9c4f"></a>

### `PIN_P6_1__GPIO`

```c
#define PIN_P6_1__GPIO ALIF_PINMUX(6, 1, 0)
```

引脚 `P6.1` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）1：`GPIO`。

<a id="a76a7ed4d6d4b4f9c8c733e84ede8e3e7"></a>

### `PIN_P6_1__LPSPI_SS2_A`

```c
#define PIN_P6_1__LPSPI_SS2_A ALIF_PINMUX(6, 1, 7)
```

端口（Port）6 的引脚（Pin）1：`LPSPI_SS2_A`。

<a id="aa0c327b4b44ee5068c84f65827555817"></a>

### `PIN_P6_1__OSPI0_D1_C`

```c
#define PIN_P6_1__OSPI0_D1_C ALIF_PINMUX(6, 1, 1)
```

端口（Port）6 的引脚（Pin）1：`OSPI0_D1_C`。

<a id="af3dc31906265cf8bba81d8fc925b180d"></a>

### `PIN_P6_1__PDM_C0_C`

```c
#define PIN_P6_1__PDM_C0_C ALIF_PINMUX(6, 1, 3)
```

端口（Port）6 的引脚（Pin）1：`PDM_C0_C`。

<a id="a1c445b43a94d1635e7174caf60e97515"></a>

### `PIN_P6_1__SD_D1_D`

```c
#define PIN_P6_1__SD_D1_D ALIF_PINMUX(6, 1, 5)
```

端口（Port）6 的引脚（Pin）1：`SD_D1_D`。

<a id="aeb4ee42999e56e3a6c98cf66e476be59"></a>

### `PIN_P6_1__UART5_DE_A`

```c
#define PIN_P6_1__UART5_DE_A ALIF_PINMUX(6, 1, 2)
```

端口（Port）6 的引脚（Pin）1：`UART5_DE_A`。

<a id="a1e1c46edc4c4a367c7c6d4e1f8fff335"></a>

### `PIN_P6_1__UT4_T1_B`

```c
#define PIN_P6_1__UT4_T1_B ALIF_PINMUX(6, 1, 4)
```

端口（Port）6 的引脚（Pin）1：`UT4_T1_B`。

<a id="abb3f78429006127f69d0bf3e5f2267b0"></a>

### `PIN_P6_2__ETH_TXEN_A`

```c
#define PIN_P6_2__ETH_TXEN_A ALIF_PINMUX(6, 2, 7)
```

端口（Port）6 的引脚（Pin）2：`ETH_TXEN_A`。

<a id="adae4d80fc2a0fb040a8eed5c89e72cdd"></a>

### `PIN_P6_2__GPIO`

```c
#define PIN_P6_2__GPIO ALIF_PINMUX(6, 2, 0)
```

引脚 `P6.2` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）2：`GPIO`。

<a id="a4a9f88b662c4b84e2f3a5528909fccee"></a>

### `PIN_P6_2__LPI3C_SDA_A`

```c
#define PIN_P6_2__LPI3C_SDA_A ALIF_PINMUX(6, 2, 3)
```

端口（Port）6 的引脚（Pin）2：`LPI3C_SDA_A`。

<a id="a1a29ae10d58edee6e97fd88d3057f1d6"></a>

### `PIN_P6_2__OSPI0_D2_C`

```c
#define PIN_P6_2__OSPI0_D2_C ALIF_PINMUX(6, 2, 1)
```

端口（Port）6 的引脚（Pin）2：`OSPI0_D2_C`。

<a id="ac4c16861bda7b2dbefcf702539014843"></a>

### `PIN_P6_2__PDM_D1_C`

```c
#define PIN_P6_2__PDM_D1_C ALIF_PINMUX(6, 2, 4)
```

端口（Port）6 的引脚（Pin）2：`PDM_D1_C`。

<a id="a097abf1cabcdb008ce0f09bae51eb06c"></a>

### `PIN_P6_2__SD_D2_D`

```c
#define PIN_P6_2__SD_D2_D ALIF_PINMUX(6, 2, 6)
```

端口（Port）6 的引脚（Pin）2：`SD_D2_D`。

<a id="a9bae739436d46b7844632df7afa34d94"></a>

### `PIN_P6_2__UART2_CTS_A`

```c
#define PIN_P6_2__UART2_CTS_A ALIF_PINMUX(6, 2, 2)
```

端口（Port）6 的引脚（Pin）2：`UART2_CTS_A`。

<a id="ad597d36c8c835cbf70d7f47e26b6d81a"></a>

### `PIN_P6_2__UT5_T0_B`

```c
#define PIN_P6_2__UT5_T0_B ALIF_PINMUX(6, 2, 5)
```

端口（Port）6 的引脚（Pin）2：`UT5_T0_B`。

<a id="a3fdfbc0ae95496472b9a0b95efa67009"></a>

### `PIN_P6_3__ETH_IRQ_A`

```c
#define PIN_P6_3__ETH_IRQ_A ALIF_PINMUX(6, 3, 7)
```

端口（Port）6 的引脚（Pin）3：`ETH_IRQ_A`。

<a id="a9c055a8795fbd5a4145bf758a72d1d23"></a>

### `PIN_P6_3__GPIO`

```c
#define PIN_P6_3__GPIO ALIF_PINMUX(6, 3, 0)
```

引脚 `P6.3` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）3：`GPIO`。

<a id="a4c6ef322bf1641221a89d79f80d9e54b"></a>

### `PIN_P6_3__LPI3C_SCL_A`

```c
#define PIN_P6_3__LPI3C_SCL_A ALIF_PINMUX(6, 3, 3)
```

端口（Port）6 的引脚（Pin）3：`LPI3C_SCL_A`。

<a id="ab9ef591fd0935f7082f8a08d31f3393f"></a>

### `PIN_P6_3__OSPI0_D3_C`

```c
#define PIN_P6_3__OSPI0_D3_C ALIF_PINMUX(6, 3, 1)
```

端口（Port）6 的引脚（Pin）3：`OSPI0_D3_C`。

<a id="a8445cb982e67a20abbd68ba9f0aa76bd"></a>

### `PIN_P6_3__PDM_C1_C`

```c
#define PIN_P6_3__PDM_C1_C ALIF_PINMUX(6, 3, 4)
```

端口（Port）6 的引脚（Pin）3：`PDM_C1_C`。

<a id="a3c17bec984f4e85d9f9f571a0b60e3fb"></a>

### `PIN_P6_3__SD_D3_D`

```c
#define PIN_P6_3__SD_D3_D ALIF_PINMUX(6, 3, 6)
```

端口（Port）6 的引脚（Pin）3：`SD_D3_D`。

<a id="a6407df773a1b7922599c36f9d5ba134f"></a>

### `PIN_P6_3__UART2_RTS_A`

```c
#define PIN_P6_3__UART2_RTS_A ALIF_PINMUX(6, 3, 2)
```

端口（Port）6 的引脚（Pin）3：`UART2_RTS_A`。

<a id="aaff27d0a5cff17c25bd2b1b46fcd4aec"></a>

### `PIN_P6_3__UT5_T1_B`

```c
#define PIN_P6_3__UT5_T1_B ALIF_PINMUX(6, 3, 5)
```

端口（Port）6 的引脚（Pin）3：`UT5_T1_B`。

<a id="a520b5fa720b201790a99eb45431a09f9"></a>

### `PIN_P6_4__ETH_REFCLK_A`

```c
#define PIN_P6_4__ETH_REFCLK_A ALIF_PINMUX(6, 4, 7)
```

端口（Port）6 的引脚（Pin）4：`ETH_REFCLK_A`。

<a id="a80712cd6a9a977af7a2f879634daf24d"></a>

### `PIN_P6_4__GPIO`

```c
#define PIN_P6_4__GPIO ALIF_PINMUX(6, 4, 0)
```

引脚 `P6.4` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）4：`GPIO`。

<a id="a4710b74789b94bdfb32c93bdde987275"></a>

### `PIN_P6_4__LRFC_OUT_A`

```c
#define PIN_P6_4__LRFC_OUT_A ALIF_PINMUX(6, 4, 3)
```

端口（Port）6 的引脚（Pin）4：`LRFC_OUT_A`。

<a id="a587f62993920d1f067ce5b5119b05aab"></a>

### `PIN_P6_4__OSPI0_D4_C`

```c
#define PIN_P6_4__OSPI0_D4_C ALIF_PINMUX(6, 4, 1)
```

端口（Port）6 的引脚（Pin）4：`OSPI0_D4_C`。

<a id="a5ca66e739931cdbbd828ac11f3625797"></a>

### `PIN_P6_4__SD_D4_D`

```c
#define PIN_P6_4__SD_D4_D ALIF_PINMUX(6, 4, 6)
```

端口（Port）6 的引脚（Pin）4：`SD_D4_D`。

<a id="a4097acd4e3c33280170dbea58ab20604"></a>

### `PIN_P6_4__SPI1_SS0_B`

```c
#define PIN_P6_4__SPI1_SS0_B ALIF_PINMUX(6, 4, 4)
```

端口（Port）6 的引脚（Pin）4：`SPI1_SS0_B`。

<a id="a3ce358cbdd477ef4755e0a59e5d62b22"></a>

### `PIN_P6_4__UART2_CTS_B`

```c
#define PIN_P6_4__UART2_CTS_B ALIF_PINMUX(6, 4, 2)
```

端口（Port）6 的引脚（Pin）4：`UART2_CTS_B`。

<a id="a6b587d186ecf998fcd206b77404c1c8f"></a>

### `PIN_P6_4__UT6_T0_B`

```c
#define PIN_P6_4__UT6_T0_B ALIF_PINMUX(6, 4, 5)
```

端口（Port）6 的引脚（Pin）4：`UT6_T0_B`。

<a id="a1acc616b5209cc593c2330115a14ac57"></a>

### `PIN_P6_5__ETH_MDIO_A`

```c
#define PIN_P6_5__ETH_MDIO_A ALIF_PINMUX(6, 5, 7)
```

端口（Port）6 的引脚（Pin）5：`ETH_MDIO_A`。

<a id="a4f8cb1991ad80690327a9272f790c7fa"></a>

### `PIN_P6_5__GPIO`

```c
#define PIN_P6_5__GPIO ALIF_PINMUX(6, 5, 0)
```

引脚 `P6.5` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）5：`GPIO`。

<a id="ab6c15149f8b91e22006b04b4ccc1ad20"></a>

### `PIN_P6_5__LPI2C1_SDA_B`

```c
#define PIN_P6_5__LPI2C1_SDA_B ALIF_PINMUX(6, 5, 3)
```

端口（Port）6 的引脚（Pin）5：`LPI2C1_SDA_B`。

<a id="ae178273fd0d60e578038153dfa3d44d2"></a>

### `PIN_P6_5__OSPI0_D5_C`

```c
#define PIN_P6_5__OSPI0_D5_C ALIF_PINMUX(6, 5, 1)
```

端口（Port）6 的引脚（Pin）5：`OSPI0_D5_C`。

<a id="a5e8205cbf5db34bf667639f7a32b212d"></a>

### `PIN_P6_5__SD_D5_D`

```c
#define PIN_P6_5__SD_D5_D ALIF_PINMUX(6, 5, 6)
```

端口（Port）6 的引脚（Pin）5：`SD_D5_D`。

<a id="af896508d8b1829141300d9c174c6a4dc"></a>

### `PIN_P6_5__SPI1_SS1_B`

```c
#define PIN_P6_5__SPI1_SS1_B ALIF_PINMUX(6, 5, 4)
```

端口（Port）6 的引脚（Pin）5：`SPI1_SS1_B`。

<a id="ac1b09ec40a2a0d186be393ce2a22bb6e"></a>

### `PIN_P6_5__UART2_RTS_B`

```c
#define PIN_P6_5__UART2_RTS_B ALIF_PINMUX(6, 5, 2)
```

端口（Port）6 的引脚（Pin）5：`UART2_RTS_B`。

<a id="a916adb647d27f3566a0b42449d85c4a9"></a>

### `PIN_P6_5__UT6_T1_B`

```c
#define PIN_P6_5__UT6_T1_B ALIF_PINMUX(6, 5, 5)
```

端口（Port）6 的引脚（Pin）5：`UT6_T1_B`。

<a id="affd24cc4890332ab2e6292bb5b34437d"></a>

### `PIN_P6_6__ETH_MDC_A`

```c
#define PIN_P6_6__ETH_MDC_A ALIF_PINMUX(6, 6, 7)
```

端口（Port）6 的引脚（Pin）6：`ETH_MDC_A`。

<a id="ae379d12c8cb8b76c585b3745eef14bfc"></a>

### `PIN_P6_6__GPIO`

```c
#define PIN_P6_6__GPIO ALIF_PINMUX(6, 6, 0)
```

引脚 `P6.6` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）6：`GPIO`。

<a id="aba610b37817ff9ca78102b5e39b8382c"></a>

### `PIN_P6_6__LPI2C1_SCL_B`

```c
#define PIN_P6_6__LPI2C1_SCL_B ALIF_PINMUX(6, 6, 3)
```

端口（Port）6 的引脚（Pin）6：`LPI2C1_SCL_B`。

<a id="a8adab274d4857b76f38a42a19c7af021"></a>

### `PIN_P6_6__OSPI0_D6_C`

```c
#define PIN_P6_6__OSPI0_D6_C ALIF_PINMUX(6, 6, 1)
```

端口（Port）6 的引脚（Pin）6：`OSPI0_D6_C`。

<a id="a7d30cf3447edf43ec02ea570fbaca29a"></a>

### `PIN_P6_6__SD_D6_D`

```c
#define PIN_P6_6__SD_D6_D ALIF_PINMUX(6, 6, 6)
```

端口（Port）6 的引脚（Pin）6：`SD_D6_D`。

<a id="a88f58696cc0671871bbf7e67d96411ba"></a>

### `PIN_P6_6__SPI1_SS2_B`

```c
#define PIN_P6_6__SPI1_SS2_B ALIF_PINMUX(6, 6, 4)
```

端口（Port）6 的引脚（Pin）6：`SPI1_SS2_B`。

<a id="a149c5ebf20984a0032f56170946e1b76"></a>

### `PIN_P6_6__UART0_CTS_B`

```c
#define PIN_P6_6__UART0_CTS_B ALIF_PINMUX(6, 6, 2)
```

端口（Port）6 的引脚（Pin）6：`UART0_CTS_B`。

<a id="a7a6a79728de2d21d2e9d8e1c4ef8d81f"></a>

### `PIN_P6_6__UT7_T0_B`

```c
#define PIN_P6_6__UT7_T0_B ALIF_PINMUX(6, 6, 5)
```

端口（Port）6 的引脚（Pin）6：`UT7_T0_B`。

<a id="afa6eac87bb7aa7316085bb6ec187adb1"></a>

### `PIN_P6_7__ETH_CRS_DV_A`

```c
#define PIN_P6_7__ETH_CRS_DV_A ALIF_PINMUX(6, 7, 7)
```

端口（Port）6 的引脚（Pin）7：`ETH_CRS_DV_A`。

<a id="a1e66098ffe67eddd23463192fcd1fbcd"></a>

### `PIN_P6_7__GPIO`

```c
#define PIN_P6_7__GPIO ALIF_PINMUX(6, 7, 0)
```

引脚 `P6.7` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）7：`GPIO`。

<a id="aef69daa6cb1613f9c4e417eaa709d9df"></a>

### `PIN_P6_7__OSPI0_D7_C`

```c
#define PIN_P6_7__OSPI0_D7_C ALIF_PINMUX(6, 7, 1)
```

端口（Port）6 的引脚（Pin）7：`OSPI0_D7_C`。

<a id="ae9d35ac26e71b26e7772f77cf7e90ddb"></a>

### `PIN_P6_7__PDM_C2_A`

```c
#define PIN_P6_7__PDM_C2_A ALIF_PINMUX(6, 7, 3)
```

端口（Port）6 的引脚（Pin）7：`PDM_C2_A`。

<a id="a391061e40809b0bc10035a3850709364"></a>

### `PIN_P6_7__SD_D7_D`

```c
#define PIN_P6_7__SD_D7_D ALIF_PINMUX(6, 7, 6)
```

端口（Port）6 的引脚（Pin）7：`SD_D7_D`。

<a id="aa7ffcbeb2e8ffd0f250fa1c144c90944"></a>

### `PIN_P6_7__SPI1_SS3_B`

```c
#define PIN_P6_7__SPI1_SS3_B ALIF_PINMUX(6, 7, 4)
```

端口（Port）6 的引脚（Pin）7：`SPI1_SS3_B`。

<a id="ae4dd7c19afbead2d7459b0e317238ae4"></a>

### `PIN_P6_7__UART0_RTS_B`

```c
#define PIN_P6_7__UART0_RTS_B ALIF_PINMUX(6, 7, 2)
```

端口（Port）6 的引脚（Pin）7：`UART0_RTS_B`。

<a id="a55c1a3571873fc72ef41cdf77589af42"></a>

### `PIN_P6_7__UT7_T1_B`

```c
#define PIN_P6_7__UT7_T1_B ALIF_PINMUX(6, 7, 5)
```

端口（Port）6 的引脚（Pin）7：`UT7_T1_B`。

<a id="a315b39b900cb690c70021e36cb57a52e"></a>

### `PIN_P7_0__CAN_RXD_A`

```c
#define PIN_P7_0__CAN_RXD_A ALIF_PINMUX(7, 0, 7)
```

端口（Port）7 的引脚（Pin）0：`CAN_RXD_A`。

<a id="a573f0d4279a1715761d6676bcb2e6694"></a>

### `PIN_P7_0__CMP3_OUT_A`

```c
#define PIN_P7_0__CMP3_OUT_A ALIF_PINMUX(7, 0, 2)
```

端口（Port）7 的引脚（Pin）0：`CMP3_OUT_A`。

<a id="ac5e4bcb47b0ccd35d7458401dbe81233"></a>

### `PIN_P7_0__GPIO`

```c
#define PIN_P7_0__GPIO ALIF_PINMUX(7, 0, 0)
```

引脚 `P7.0` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）0：`GPIO`。

<a id="a1fde60e018d010f91f259fe2684f2bef"></a>

### `PIN_P7_0__I2C0_SDA_C`

```c
#define PIN_P7_0__I2C0_SDA_C ALIF_PINMUX(7, 0, 4)
```

端口（Port）7 的引脚（Pin）0：`I2C0_SDA_C`。

<a id="ae22354ee8a017c5e71ec62a007ca6b11"></a>

### `PIN_P7_0__LPUT0_T0_A`

```c
#define PIN_P7_0__LPUT0_T0_A ALIF_PINMUX(7, 0, 1)
```

端口（Port）7 的引脚（Pin）0：`LPUT0_T0_A`。

<a id="af19527b153d09b5a76baaaf5ee394509"></a>

### `PIN_P7_0__SD_CMD_A`

```c
#define PIN_P7_0__SD_CMD_A ALIF_PINMUX(7, 0, 6)
```

端口（Port）7 的引脚（Pin）0：`SD_CMD_A`。

<a id="af0831316631026230f9038d7fadf92e7"></a>

### `PIN_P7_0__SPI0_MISO_C`

```c
#define PIN_P7_0__SPI0_MISO_C ALIF_PINMUX(7, 0, 3)
```

端口（Port）7 的引脚（Pin）0：`SPI0_MISO_C`。

<a id="aa2090c10fe53165b850dd0cfbd00b28e"></a>

### `PIN_P7_0__UT8_T0_B`

```c
#define PIN_P7_0__UT8_T0_B ALIF_PINMUX(7, 0, 5)
```

端口（Port）7 的引脚（Pin）0：`UT8_T0_B`。

<a id="a0c095cb41bcce62e68f99852527fb472"></a>

### `PIN_P7_1__CAN_TXD_A`

```c
#define PIN_P7_1__CAN_TXD_A ALIF_PINMUX(7, 1, 7)
```

端口（Port）7 的引脚（Pin）1：`CAN_TXD_A`。

<a id="a0f00923007990dc5d99c9e68cb9b8bea"></a>

### `PIN_P7_1__CMP2_OUT_A`

```c
#define PIN_P7_1__CMP2_OUT_A ALIF_PINMUX(7, 1, 2)
```

端口（Port）7 的引脚（Pin）1：`CMP2_OUT_A`。

<a id="afd333ffdddac335d52e506deb72eacaf"></a>

### `PIN_P7_1__GPIO`

```c
#define PIN_P7_1__GPIO ALIF_PINMUX(7, 1, 0)
```

引脚 `P7.1` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）1：`GPIO`。

<a id="af1c7a7f1fc1d87b7036a5ac346c435a7"></a>

### `PIN_P7_1__I2C0_SCL_C`

```c
#define PIN_P7_1__I2C0_SCL_C ALIF_PINMUX(7, 1, 4)
```

端口（Port）7 的引脚（Pin）1：`I2C0_SCL_C`。

<a id="a5934e917d97771544a2de6f7df6b177c"></a>

### `PIN_P7_1__LPUT0_T1_A`

```c
#define PIN_P7_1__LPUT0_T1_A ALIF_PINMUX(7, 1, 1)
```

端口（Port）7 的引脚（Pin）1：`LPUT0_T1_A`。

<a id="a644faaea1fba0a87fabe761141752c1f"></a>

### `PIN_P7_1__SD_CLK_A`

```c
#define PIN_P7_1__SD_CLK_A ALIF_PINMUX(7, 1, 6)
```

端口（Port）7 的引脚（Pin）1：`SD_CLK_A`。

<a id="aeb314afb125e7530cd9002ff3dc3b107"></a>

### `PIN_P7_1__SPI0_MOSI_C`

```c
#define PIN_P7_1__SPI0_MOSI_C ALIF_PINMUX(7, 1, 3)
```

端口（Port）7 的引脚（Pin）1：`SPI0_MOSI_C`。

<a id="a2cf53f369584f6c900545f79981f24ca"></a>

### `PIN_P7_1__UT8_T1_B`

```c
#define PIN_P7_1__UT8_T1_B ALIF_PINMUX(7, 1, 5)
```

端口（Port）7 的引脚（Pin）1：`UT8_T1_B`。

<a id="a9741c146d7f9b394e10e8ecbc2547bb5"></a>

### `PIN_P7_2__CMP1_OUT_A`

```c
#define PIN_P7_2__CMP1_OUT_A ALIF_PINMUX(7, 2, 3)
```

端口（Port）7 的引脚（Pin）2：`CMP1_OUT_A`。

<a id="adc16259fec5582a1e6ebc9cb8a825c03"></a>

### `PIN_P7_2__GPIO`

```c
#define PIN_P7_2__GPIO ALIF_PINMUX(7, 2, 0)
```

引脚 `P7.2` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）2：`GPIO`。

<a id="a803ef3f2d107d05670bba596998fca2a"></a>

### `PIN_P7_2__I2C1_SDA_C`

```c
#define PIN_P7_2__I2C1_SDA_C ALIF_PINMUX(7, 2, 5)
```

端口（Port）7 的引脚（Pin）2：`I2C1_SDA_C`。

<a id="ac414182ecfa6cdfc7249c7aa2d59681a"></a>

### `PIN_P7_2__LPUT1_T0_A`

```c
#define PIN_P7_2__LPUT1_T0_A ALIF_PINMUX(7, 2, 1)
```

端口（Port）7 的引脚（Pin）2：`LPUT1_T0_A`。

<a id="aa1020e341c285beed6019cf5c9e7cd0f"></a>

### `PIN_P7_2__SD_RST_A`

```c
#define PIN_P7_2__SD_RST_A ALIF_PINMUX(7, 2, 7)
```

端口（Port）7 的引脚（Pin）2：`SD_RST_A`。

<a id="ad36e1683e60fe5a8ac68fff42ea59029"></a>

### `PIN_P7_2__SPI0_SCLK_C`

```c
#define PIN_P7_2__SPI0_SCLK_C ALIF_PINMUX(7, 2, 4)
```

端口（Port）7 的引脚（Pin）2：`SPI0_SCLK_C`。

<a id="a0228bb15a003556d45cdba01039e5fb3"></a>

### `PIN_P7_2__UART3_CTS_B`

```c
#define PIN_P7_2__UART3_CTS_B ALIF_PINMUX(7, 2, 2)
```

端口（Port）7 的引脚（Pin）2：`UART3_CTS_B`。

<a id="a827131e3b96c2ff6166e10b6bf8a714a"></a>

### `PIN_P7_2__UT9_T0_B`

```c
#define PIN_P7_2__UT9_T0_B ALIF_PINMUX(7, 2, 6)
```

端口（Port）7 的引脚（Pin）2：`UT9_T0_B`。

<a id="a4736c7a65fab9ad1788b1b333ecd9048"></a>

### `PIN_P7_3__CAN_STBY_A`

```c
#define PIN_P7_3__CAN_STBY_A ALIF_PINMUX(7, 3, 7)
```

端口（Port）7 的引脚（Pin）3：`CAN_STBY_A`。

<a id="afad69246b1edd640cbc69277c6dea5f7"></a>

### `PIN_P7_3__CMP0_OUT_A`

```c
#define PIN_P7_3__CMP0_OUT_A ALIF_PINMUX(7, 3, 3)
```

端口（Port）7 的引脚（Pin）3：`CMP0_OUT_A`。

<a id="a75dbeec7072793acd5eaa20f0d0d1055"></a>

### `PIN_P7_3__GPIO`

```c
#define PIN_P7_3__GPIO ALIF_PINMUX(7, 3, 0)
```

引脚 `P7.3` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）3：`GPIO`。

<a id="a62c7010c5c2ec0aa887cdc198dc4ab61"></a>

### `PIN_P7_3__I2C1_SCL_C`

```c
#define PIN_P7_3__I2C1_SCL_C ALIF_PINMUX(7, 3, 5)
```

端口（Port）7 的引脚（Pin）3：`I2C1_SCL_C`。

<a id="a286332f2ba4230cc9d065d89dd366ee8"></a>

### `PIN_P7_3__LPUT1_T1_A`

```c
#define PIN_P7_3__LPUT1_T1_A ALIF_PINMUX(7, 3, 1)
```

端口（Port）7 的引脚（Pin）3：`LPUT1_T1_A`。

<a id="a6d6173bcd02b0ae215e1c1dd4756ea49"></a>

### `PIN_P7_3__SPI0_SS0_C`

```c
#define PIN_P7_3__SPI0_SS0_C ALIF_PINMUX(7, 3, 4)
```

端口（Port）7 的引脚（Pin）3：`SPI0_SS0_C`。

<a id="a70267fe4f07b3962dc3f82831eaec387"></a>

### `PIN_P7_3__UART3_RTS_B`

```c
#define PIN_P7_3__UART3_RTS_B ALIF_PINMUX(7, 3, 2)
```

端口（Port）7 的引脚（Pin）3：`UART3_RTS_B`。

<a id="a70d270eee3fd69cf7b2a0baf848829bd"></a>

### `PIN_P7_3__UT9_T1_B`

```c
#define PIN_P7_3__UT9_T1_B ALIF_PINMUX(7, 3, 6)
```

端口（Port）7 的引脚（Pin）3：`UT9_T1_B`。

<a id="ae4761d31982dad9a275346a237d734c7"></a>

### `PIN_P7_4__GPIO`

```c
#define PIN_P7_4__GPIO ALIF_PINMUX(7, 4, 0)
```

引脚 `P7.4` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）4：`GPIO`。

<a id="a60f056cd47fb1a96f4fafa3e2c069766"></a>

### `PIN_P7_4__LPI2C0_SCL_A`

```c
#define PIN_P7_4__LPI2C0_SCL_A ALIF_PINMUX(7, 4, 5)
```

端口（Port）7 的引脚（Pin）4：`LPI2C0_SCL_A`。

<a id="a59af3f76078b27d2140424517cc75344"></a>

### `PIN_P7_4__LPPDM_C2_A`

```c
#define PIN_P7_4__LPPDM_C2_A ALIF_PINMUX(7, 4, 3)
```

端口（Port）7 的引脚（Pin）4：`LPPDM_C2_A`。

<a id="a78ee9a3bf488866f266cba2bfac445c3"></a>

### `PIN_P7_4__LPSPI_MISO_A`

```c
#define PIN_P7_4__LPSPI_MISO_A ALIF_PINMUX(7, 4, 4)
```

端口（Port）7 的引脚（Pin）4：`LPSPI_MISO_A`。

<a id="af9b0f86a16481eaa6ba6158c3c4a1f27"></a>

### `PIN_P7_4__LPUART_CTS_A`

```c
#define PIN_P7_4__LPUART_CTS_A ALIF_PINMUX(7, 4, 2)
```

端口（Port）7 的引脚（Pin）4：`LPUART_CTS_A`。

<a id="a4a2ce8e3f9a8ee8c6cc63189fd4f1b2b"></a>

### `PIN_P7_4__LPUT2_T0_A`

```c
#define PIN_P7_4__LPUT2_T0_A ALIF_PINMUX(7, 4, 1)
```

端口（Port）7 的引脚（Pin）4：`LPUT2_T0_A`。

<a id="a29e164a0438f28339ce98a0fb9575e78"></a>

### `PIN_P7_4__UT10_T0_B`

```c
#define PIN_P7_4__UT10_T0_B ALIF_PINMUX(7, 4, 6)
```

端口（Port）7 的引脚（Pin）4：`UT10_T0_B`。

<a id="ac47d162d1d4eb774e733fe27673c7c6b"></a>

### `PIN_P7_5__GPIO`

```c
#define PIN_P7_5__GPIO ALIF_PINMUX(7, 5, 0)
```

引脚 `P7.5` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）5：`GPIO`。

<a id="aa749c8fc95bb1b08d0e30577bf16ea25"></a>

### `PIN_P7_5__LFXO_OUT_A`

```c
#define PIN_P7_5__LFXO_OUT_A ALIF_PINMUX(7, 5, 3)
```

端口（Port）7 的引脚（Pin）5：`LFXO_OUT_A`。

<a id="af08809b51ad5dfd7d5bdd46aa2bc5072"></a>

### `PIN_P7_5__LPI2C0_SDA_A`

```c
#define PIN_P7_5__LPI2C0_SDA_A ALIF_PINMUX(7, 5, 6)
```

端口（Port）7 的引脚（Pin）5：`LPI2C0_SDA_A`。

<a id="a8c7a9903bb1ee74e9e3d008269a9208c"></a>

### `PIN_P7_5__LPPDM_D2_A`

```c
#define PIN_P7_5__LPPDM_D2_A ALIF_PINMUX(7, 5, 4)
```

端口（Port）7 的引脚（Pin）5：`LPPDM_D2_A`。

<a id="a6b1969e563d7224a9056d36904d6e3db"></a>

### `PIN_P7_5__LPSPI_MOSI_A`

```c
#define PIN_P7_5__LPSPI_MOSI_A ALIF_PINMUX(7, 5, 5)
```

端口（Port）7 的引脚（Pin）5：`LPSPI_MOSI_A`。

<a id="a528ac9bd32e60609a78a980cdf5599c7"></a>

### `PIN_P7_5__LPUART_RTS_A`

```c
#define PIN_P7_5__LPUART_RTS_A ALIF_PINMUX(7, 5, 2)
```

端口（Port）7 的引脚（Pin）5：`LPUART_RTS_A`。

<a id="a6d6127b10c8091e50322519c6dfd7717"></a>

### `PIN_P7_5__LPUT2_T1_A`

```c
#define PIN_P7_5__LPUT2_T1_A ALIF_PINMUX(7, 5, 1)
```

端口（Port）7 的引脚（Pin）5：`LPUT2_T1_A`。

<a id="a8a91b43d2f6023ae6d6e60347456613c"></a>

### `PIN_P7_5__UT10_T1_B`

```c
#define PIN_P7_5__UT10_T1_B ALIF_PINMUX(7, 5, 7)
```

端口（Port）7 的引脚（Pin）5：`UT10_T1_B`。

<a id="ab95fc52f53c6a1703df290ac307871e4"></a>

### `PIN_P7_6__GPIO`

```c
#define PIN_P7_6__GPIO ALIF_PINMUX(7, 6, 0)
```

引脚 `P7.6` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）6：`GPIO`。

<a id="aede5f0616ee5550e1865a79632851405"></a>

### `PIN_P7_6__I3C_SDA_D`

```c
#define PIN_P7_6__I3C_SDA_D ALIF_PINMUX(7, 6, 6)
```

端口（Port）7 的引脚（Pin）6：`I3C_SDA_D`。

<a id="aec52e333e3549d491bf248f21537c997"></a>

### `PIN_P7_6__LPI2C1_SDA_C`

```c
#define PIN_P7_6__LPI2C1_SDA_C ALIF_PINMUX(7, 6, 1)
```

端口（Port）7 的引脚（Pin）6：`LPI2C1_SDA_C`。

<a id="af6c6d6ca80af88d9bda2d5c721942271"></a>

### `PIN_P7_6__LPI3C_SDA_B`

```c
#define PIN_P7_6__LPI3C_SDA_B ALIF_PINMUX(7, 6, 3)
```

端口（Port）7 的引脚（Pin）6：`LPI3C_SDA_B`。

<a id="aa762aaa39051c078d337fd65c3af5594"></a>

### `PIN_P7_6__LPPDM_C3_A`

```c
#define PIN_P7_6__LPPDM_C3_A ALIF_PINMUX(7, 6, 4)
```

端口（Port）7 的引脚（Pin）6：`LPPDM_C3_A`。

<a id="ae1366010110318f0f429f912b5372cbf"></a>

### `PIN_P7_6__LPSPI_SCLK_A`

```c
#define PIN_P7_6__LPSPI_SCLK_A ALIF_PINMUX(7, 6, 5)
```

端口（Port）7 的引脚（Pin）6：`LPSPI_SCLK_A`。

<a id="a8e8245f9ad371815fe2ecde177626055"></a>

### `PIN_P7_6__LPUART_RX_A`

```c
#define PIN_P7_6__LPUART_RX_A ALIF_PINMUX(7, 6, 2)
```

端口（Port）7 的引脚（Pin）6：`LPUART_RX_A`。

<a id="af25f44d0c6c3a9ffc6277d47de0faf20"></a>

### `PIN_P7_6__UT11_T0_B`

```c
#define PIN_P7_6__UT11_T0_B ALIF_PINMUX(7, 6, 7)
```

端口（Port）7 的引脚（Pin）6：`UT11_T0_B`。

<a id="ae3abc19efe0b06fc7f3dc73c1eb040c7"></a>

### `PIN_P7_7__GPIO`

```c
#define PIN_P7_7__GPIO ALIF_PINMUX(7, 7, 0)
```

引脚 `P7.7` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）7：`GPIO`。

<a id="a6757d24d4e447acbfcb834c22859ea2f"></a>

### `PIN_P7_7__I3C_SCL_D`

```c
#define PIN_P7_7__I3C_SCL_D ALIF_PINMUX(7, 7, 6)
```

端口（Port）7 的引脚（Pin）7：`I3C_SCL_D`。

<a id="a2aced875528e0e6570a05f0b8aa9a8f4"></a>

### `PIN_P7_7__LPI2C1_SCL_C`

```c
#define PIN_P7_7__LPI2C1_SCL_C ALIF_PINMUX(7, 7, 1)
```

端口（Port）7 的引脚（Pin）7：`LPI2C1_SCL_C`。

<a id="a51f939dd65c588c9fee6bb08ff1d014c"></a>

### `PIN_P7_7__LPI3C_SCL_B`

```c
#define PIN_P7_7__LPI3C_SCL_B ALIF_PINMUX(7, 7, 3)
```

端口（Port）7 的引脚（Pin）7：`LPI3C_SCL_B`。

<a id="ac9968fc164932e8c44c9211dbfda8c23"></a>

### `PIN_P7_7__LPPDM_D3_A`

```c
#define PIN_P7_7__LPPDM_D3_A ALIF_PINMUX(7, 7, 4)
```

端口（Port）7 的引脚（Pin）7：`LPPDM_D3_A`。

<a id="afb80459bd6c6c944fa257a46ca978070"></a>

### `PIN_P7_7__LPSPI_SS0_A`

```c
#define PIN_P7_7__LPSPI_SS0_A ALIF_PINMUX(7, 7, 5)
```

端口（Port）7 的引脚（Pin）7：`LPSPI_SS0_A`。

<a id="a4a121c7800a2c7bf027101c8e6be0981"></a>

### `PIN_P7_7__LPUART_TX_A`

```c
#define PIN_P7_7__LPUART_TX_A ALIF_PINMUX(7, 7, 2)
```

端口（Port）7 的引脚（Pin）7：`LPUART_TX_A`。

<a id="a74bcedf4c0f0de4ef1fdd168e7f5ac07"></a>

### `PIN_P7_7__UT11_T1_B`

```c
#define PIN_P7_7__UT11_T1_B ALIF_PINMUX(7, 7, 7)
```

端口（Port）7 的引脚（Pin）7：`UT11_T1_B`。

<a id="afd9b154a630faffbb4ed569a1b1728e5"></a>

### `PIN_P8_0__AUDIO_CLK_A`

```c
#define PIN_P8_0__AUDIO_CLK_A ALIF_PINMUX(8, 0, 2)
```

端口（Port）8 的引脚（Pin）0：`AUDIO_CLK_A`。

<a id="a46242fe0b6bef22903ee8521cc2f7114"></a>

### `PIN_P8_0__CAM_D0_B`

```c
#define PIN_P8_0__CAM_D0_B ALIF_PINMUX(8, 0, 7)
```

端口（Port）8 的引脚（Pin）0：`CAM_D0_B`。

<a id="afe19a4d1634357b733f1256f1af834d8"></a>

### `PIN_P8_0__CDC_D0_A`

```c
#define PIN_P8_0__CDC_D0_A ALIF_PINMUX(8, 0, 6)
```

端口（Port）8 的引脚（Pin）0：`CDC_D0_A`。

<a id="ae7ea63c6f45c50ee3dbe6c4c5fb885b0"></a>

### `PIN_P8_0__FAULT0_B`

```c
#define PIN_P8_0__FAULT0_B ALIF_PINMUX(8, 0, 3)
```

端口（Port）8 的引脚（Pin）0：`FAULT0_B`。

<a id="afae07d2c2c36cf28b58d3025bd312bcd"></a>

### `PIN_P8_0__GPIO`

```c
#define PIN_P8_0__GPIO ALIF_PINMUX(8, 0, 0)
```

引脚 `P8.0` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）0：`GPIO`。

<a id="a2cd736bf19d6192bf3e3c3f5d32af663"></a>

### `PIN_P8_0__LPCAM_D0_A`

```c
#define PIN_P8_0__LPCAM_D0_A ALIF_PINMUX(8, 0, 4)
```

端口（Port）8 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="ac170e16e07731581b3efa51fd5f5e87b"></a>

### `PIN_P8_0__OSPI1_SCLKN_C`

```c
#define PIN_P8_0__OSPI1_SCLKN_C ALIF_PINMUX(8, 0, 1)
```

端口（Port）8 的引脚（Pin）0：`OSPI1_SCLKN_C`。

<a id="a985d8090a059e89d8f08cca3ced6b4ee"></a>

### `PIN_P8_0__SD_D0_C`

```c
#define PIN_P8_0__SD_D0_C ALIF_PINMUX(8, 0, 5)
```

端口（Port）8 的引脚（Pin）0：`SD_D0_C`。

<a id="a3b536ef4e1eb1a398f4b5fca65268578"></a>

### `PIN_P8_1__CAM_D1_B`

```c
#define PIN_P8_1__CAM_D1_B ALIF_PINMUX(8, 1, 6)
```

端口（Port）8 的引脚（Pin）1：`CAM_D1_B`。

<a id="ad7959cb731c45e0fdbdaa316ce9b46b3"></a>

### `PIN_P8_1__CDC_D1_A`

```c
#define PIN_P8_1__CDC_D1_A ALIF_PINMUX(8, 1, 5)
```

端口（Port）8 的引脚（Pin）1：`CDC_D1_A`。

<a id="ade34846e1cde4f9d437200205354fc49"></a>

### `PIN_P8_1__FAULT1_B`

```c
#define PIN_P8_1__FAULT1_B ALIF_PINMUX(8, 1, 2)
```

端口（Port）8 的引脚（Pin）1：`FAULT1_B`。

<a id="ab7545d1438381ff91c47907abe36bde2"></a>

### `PIN_P8_1__GPIO`

```c
#define PIN_P8_1__GPIO ALIF_PINMUX(8, 1, 0)
```

引脚 `P8.1` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）1：`GPIO`。

<a id="aed14311308ba4434e797d9755927571c"></a>

### `PIN_P8_1__I2S2_SDI_A`

```c
#define PIN_P8_1__I2S2_SDI_A ALIF_PINMUX(8, 1, 1)
```

端口（Port）8 的引脚（Pin）1：`I2S2_SDI_A`。

<a id="a8619f56c0d93c514ae9e3087e3658d57"></a>

### `PIN_P8_1__LPCAM_D1_A`

```c
#define PIN_P8_1__LPCAM_D1_A ALIF_PINMUX(8, 1, 3)
```

端口（Port）8 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="ab945bad6f40aeb586d3bedd041cddc8e"></a>

### `PIN_P8_1__OSPI1_SS1_C`

```c
#define PIN_P8_1__OSPI1_SS1_C ALIF_PINMUX(8, 1, 7)
```

端口（Port）8 的引脚（Pin）1：`OSPI1_SS1_C`。

<a id="a270654843e3737dde6343aeb430381aa"></a>

### `PIN_P8_1__SD_D1_C`

```c
#define PIN_P8_1__SD_D1_C ALIF_PINMUX(8, 1, 4)
```

端口（Port）8 的引脚（Pin）1：`SD_D1_C`。

<a id="a782d57f5a111a3fc8b226aefc82ade9b"></a>

### `PIN_P8_2__CAM_D2_B`

```c
#define PIN_P8_2__CAM_D2_B ALIF_PINMUX(8, 2, 7)
```

端口（Port）8 的引脚（Pin）2：`CAM_D2_B`。

<a id="a14ec0433913ab0ca33bf7324459fd430"></a>

### `PIN_P8_2__CDC_D2_A`

```c
#define PIN_P8_2__CDC_D2_A ALIF_PINMUX(8, 2, 6)
```

端口（Port）8 的引脚（Pin）2：`CDC_D2_A`。

<a id="a150dc67f0f284e49967bd0d01f4ed834"></a>

### `PIN_P8_2__FAULT2_B`

```c
#define PIN_P8_2__FAULT2_B ALIF_PINMUX(8, 2, 3)
```

端口（Port）8 的引脚（Pin）2：`FAULT2_B`。

<a id="a60cd1313b5dbd2f3e804024add367802"></a>

### `PIN_P8_2__GPIO`

```c
#define PIN_P8_2__GPIO ALIF_PINMUX(8, 2, 0)
```

引脚 `P8.2` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）2：`GPIO`。

<a id="a9ea5544fe5b2c4576dd82884e13395df"></a>

### `PIN_P8_2__I2S2_SDO_A`

```c
#define PIN_P8_2__I2S2_SDO_A ALIF_PINMUX(8, 2, 1)
```

端口（Port）8 的引脚（Pin）2：`I2S2_SDO_A`。

<a id="a3b1ede5fe15c4d88a3bd13dc3ee334d4"></a>

### `PIN_P8_2__LPCAM_D2_A`

```c
#define PIN_P8_2__LPCAM_D2_A ALIF_PINMUX(8, 2, 4)
```

端口（Port）8 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="aa5d039fdf4e676090df9ff678fd4e519"></a>

### `PIN_P8_2__SD_D2_C`

```c
#define PIN_P8_2__SD_D2_C ALIF_PINMUX(8, 2, 5)
```

端口（Port）8 的引脚（Pin）2：`SD_D2_C`。

<a id="a6d412afabb6859b510829773e835fc0d"></a>

### `PIN_P8_2__SPI0_SS3_B`

```c
#define PIN_P8_2__SPI0_SS3_B ALIF_PINMUX(8, 2, 2)
```

端口（Port）8 的引脚（Pin）2：`SPI0_SS3_B`。

<a id="af221fa9c7c280f0fc9ca550e58151be0"></a>

### `PIN_P8_3__CAM_D3_B`

```c
#define PIN_P8_3__CAM_D3_B ALIF_PINMUX(8, 3, 7)
```

端口（Port）8 的引脚（Pin）3：`CAM_D3_B`。

<a id="a70b935056e53ed2c964488bc1848d876"></a>

### `PIN_P8_3__CDC_D3_A`

```c
#define PIN_P8_3__CDC_D3_A ALIF_PINMUX(8, 3, 6)
```

端口（Port）8 的引脚（Pin）3：`CDC_D3_A`。

<a id="ace81371f4c2d6ad8f4769ca638c92737"></a>

### `PIN_P8_3__FAULT3_B`

```c
#define PIN_P8_3__FAULT3_B ALIF_PINMUX(8, 3, 3)
```

端口（Port）8 的引脚（Pin）3：`FAULT3_B`。

<a id="ada60da6343aec9d7f341d29d6c0f7d6e"></a>

### `PIN_P8_3__GPIO`

```c
#define PIN_P8_3__GPIO ALIF_PINMUX(8, 3, 0)
```

引脚 `P8.3` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）3：`GPIO`。

<a id="a7fe15caced34ecf53b4b0fce1872cd5a"></a>

### `PIN_P8_3__I2S2_SCLK_A`

```c
#define PIN_P8_3__I2S2_SCLK_A ALIF_PINMUX(8, 3, 1)
```

端口（Port）8 的引脚（Pin）3：`I2S2_SCLK_A`。

<a id="a2bdc2a068101da6a91f67764fa027a94"></a>

### `PIN_P8_3__LPCAM_D3_A`

```c
#define PIN_P8_3__LPCAM_D3_A ALIF_PINMUX(8, 3, 4)
```

端口（Port）8 的引脚（Pin）3：`LPCAM_D3_A`。

<a id="a1d349e741c7483151b7bb795040ff91f"></a>

### `PIN_P8_3__SD_D3_C`

```c
#define PIN_P8_3__SD_D3_C ALIF_PINMUX(8, 3, 5)
```

端口（Port）8 的引脚（Pin）3：`SD_D3_C`。

<a id="a1603e457c636619279c6ed35e69a3cf2"></a>

### `PIN_P8_3__SPI1_MISO_B`

```c
#define PIN_P8_3__SPI1_MISO_B ALIF_PINMUX(8, 3, 2)
```

端口（Port）8 的引脚（Pin）3：`SPI1_MISO_B`。

<a id="a7a3f80febc5c72fd959aea6d11fc6868"></a>

### `PIN_P8_4__CAM_D4_B`

```c
#define PIN_P8_4__CAM_D4_B ALIF_PINMUX(8, 4, 7)
```

端口（Port）8 的引脚（Pin）4：`CAM_D4_B`。

<a id="ab79b6cd1f13c929a09782df627f4f41a"></a>

### `PIN_P8_4__CDC_D4_A`

```c
#define PIN_P8_4__CDC_D4_A ALIF_PINMUX(8, 4, 6)
```

端口（Port）8 的引脚（Pin）4：`CDC_D4_A`。

<a id="a077f91c6d32af478832d2f868a03ce92"></a>

### `PIN_P8_4__GPIO`

```c
#define PIN_P8_4__GPIO ALIF_PINMUX(8, 4, 0)
```

引脚 `P8.4` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）4：`GPIO`。

<a id="ad6ec829cafb61c3ca9f5cde62add27cc"></a>

### `PIN_P8_4__I2S2_WS_A`

```c
#define PIN_P8_4__I2S2_WS_A ALIF_PINMUX(8, 4, 1)
```

端口（Port）8 的引脚（Pin）4：`I2S2_WS_A`。

<a id="a45eb5a3acd40b9e97f88a179b2e16284"></a>

### `PIN_P8_4__LPCAM_D4_A`

```c
#define PIN_P8_4__LPCAM_D4_A ALIF_PINMUX(8, 4, 4)
```

端口（Port）8 的引脚（Pin）4：`LPCAM_D4_A`。

<a id="a60238f03990fa811ca84e9bd6c607a86"></a>

### `PIN_P8_4__QEC0_X_B`

```c
#define PIN_P8_4__QEC0_X_B ALIF_PINMUX(8, 4, 3)
```

端口（Port）8 的引脚（Pin）4：`QEC0_X_B`。

<a id="a831ed2e8215f6ba12ac665ef3dcfbc4f"></a>

### `PIN_P8_4__SD_D4_C`

```c
#define PIN_P8_4__SD_D4_C ALIF_PINMUX(8, 4, 5)
```

端口（Port）8 的引脚（Pin）4：`SD_D4_C`。

<a id="a08a61462ce55c049a6e607ca104fad5c"></a>

### `PIN_P8_4__SPI1_MOSI_B`

```c
#define PIN_P8_4__SPI1_MOSI_B ALIF_PINMUX(8, 4, 2)
```

端口（Port）8 的引脚（Pin）4：`SPI1_MOSI_B`。

<a id="a0eda6c75336d02a21d83e14ffa02275c"></a>

### `PIN_P8_5__CAM_D5_B`

```c
#define PIN_P8_5__CAM_D5_B ALIF_PINMUX(8, 5, 7)
```

端口（Port）8 的引脚（Pin）5：`CAM_D5_B`。

<a id="a9b890e71e9480f5d6f15abaf29b984a0"></a>

### `PIN_P8_5__CDC_D5_A`

```c
#define PIN_P8_5__CDC_D5_A ALIF_PINMUX(8, 5, 6)
```

端口（Port）8 的引脚（Pin）5：`CDC_D5_A`。

<a id="a3d1dbbf65ec7141c08cbdf70186faa0a"></a>

### `PIN_P8_5__GPIO`

```c
#define PIN_P8_5__GPIO ALIF_PINMUX(8, 5, 0)
```

引脚 `P8.5` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）5：`GPIO`。

<a id="a7ee0f06bc2b5d3ef1f91815d61372987"></a>

### `PIN_P8_5__LPCAM_D5_A`

```c
#define PIN_P8_5__LPCAM_D5_A ALIF_PINMUX(8, 5, 4)
```

端口（Port）8 的引脚（Pin）5：`LPCAM_D5_A`。

<a id="a5aaf1e1d094132d176d5b5b706168240"></a>

### `PIN_P8_5__OSPI0_RXDS1_A`

```c
#define PIN_P8_5__OSPI0_RXDS1_A ALIF_PINMUX(8, 5, 1)
```

端口（Port）8 的引脚（Pin）5：`OSPI0_RXDS1_A`。

<a id="a5a1f1e7e28cfc2e35f2acd079226872c"></a>

### `PIN_P8_5__QEC0_Y_B`

```c
#define PIN_P8_5__QEC0_Y_B ALIF_PINMUX(8, 5, 3)
```

端口（Port）8 的引脚（Pin）5：`QEC0_Y_B`。

<a id="acc5f05b73b0370106e7ffc49e4bff2c2"></a>

### `PIN_P8_5__SD_D5_C`

```c
#define PIN_P8_5__SD_D5_C ALIF_PINMUX(8, 5, 5)
```

端口（Port）8 的引脚（Pin）5：`SD_D5_C`。

<a id="a01fa8957cb94ee6e829a876fb0af631f"></a>

### `PIN_P8_5__SPI1_SCLK_B`

```c
#define PIN_P8_5__SPI1_SCLK_B ALIF_PINMUX(8, 5, 2)
```

端口（Port）8 的引脚（Pin）5：`SPI1_SCLK_B`。

<a id="a505e16163e7d4506f77d5efef0bd4091"></a>

### `PIN_P8_6__CAM_D6_B`

```c
#define PIN_P8_6__CAM_D6_B ALIF_PINMUX(8, 6, 7)
```

端口（Port）8 的引脚（Pin）6：`CAM_D6_B`。

<a id="a4601228b6c06379cf97f14a93ea46a7c"></a>

### `PIN_P8_6__CDC_D6_A`

```c
#define PIN_P8_6__CDC_D6_A ALIF_PINMUX(8, 6, 6)
```

端口（Port）8 的引脚（Pin）6：`CDC_D6_A`。

<a id="aac04079cc075adb9c60dc629fb9e544e"></a>

### `PIN_P8_6__GPIO`

```c
#define PIN_P8_6__GPIO ALIF_PINMUX(8, 6, 0)
```

引脚 `P8.6` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）6：`GPIO`。

<a id="aa0dcf82c495888b3589f6233ee96a9ea"></a>

### `PIN_P8_6__I2S3_SCLK_B`

```c
#define PIN_P8_6__I2S3_SCLK_B ALIF_PINMUX(8, 6, 2)
```

端口（Port）8 的引脚（Pin）6：`I2S3_SCLK_B`。

<a id="afe04f9d7665f3818e7f66b567a69f10e"></a>

### `PIN_P8_6__LPCAM_D6_A`

```c
#define PIN_P8_6__LPCAM_D6_A ALIF_PINMUX(8, 6, 4)
```

端口（Port）8 的引脚（Pin）6：`LPCAM_D6_A`。

<a id="af28764146f32632aa6c0a740defff893"></a>

### `PIN_P8_6__OSPI1_RXDS1_B`

```c
#define PIN_P8_6__OSPI1_RXDS1_B ALIF_PINMUX(8, 6, 1)
```

端口（Port）8 的引脚（Pin）6：`OSPI1_RXDS1_B`。

<a id="a942f076af1c013b2d500cdd85bbbd7a2"></a>

### `PIN_P8_6__QEC0_Z_B`

```c
#define PIN_P8_6__QEC0_Z_B ALIF_PINMUX(8, 6, 3)
```

端口（Port）8 的引脚（Pin）6：`QEC0_Z_B`。

<a id="aae6cb48371c69ec68657716554d99f5a"></a>

### `PIN_P8_6__SD_D6_C`

```c
#define PIN_P8_6__SD_D6_C ALIF_PINMUX(8, 6, 5)
```

端口（Port）8 的引脚（Pin）6：`SD_D6_C`。

<a id="a5d417264ffe4cba745f1db5b9416bc26"></a>

### `PIN_P8_7__CAM_D7_B`

```c
#define PIN_P8_7__CAM_D7_B ALIF_PINMUX(8, 7, 7)
```

端口（Port）8 的引脚（Pin）7：`CAM_D7_B`。

<a id="a1275cdc5c8fbd8d744c38e5ad16b3d83"></a>

### `PIN_P8_7__CDC_D7_A`

```c
#define PIN_P8_7__CDC_D7_A ALIF_PINMUX(8, 7, 6)
```

端口（Port）8 的引脚（Pin）7：`CDC_D7_A`。

<a id="adeed03c5ceab2806bff7df654f45982d"></a>

### `PIN_P8_7__GPIO`

```c
#define PIN_P8_7__GPIO ALIF_PINMUX(8, 7, 0)
```

引脚 `P8.7` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）7：`GPIO`。

<a id="a4f4921bd231e42c104f884b50019a779"></a>

### `PIN_P8_7__I2S3_WS_B`

```c
#define PIN_P8_7__I2S3_WS_B ALIF_PINMUX(8, 7, 2)
```

端口（Port）8 的引脚（Pin）7：`I2S3_WS_B`。

<a id="ad78a16e7892b71380e4fef2afc9bcc78"></a>

### `PIN_P8_7__LPCAM_D7_A`

```c
#define PIN_P8_7__LPCAM_D7_A ALIF_PINMUX(8, 7, 4)
```

端口（Port）8 的引脚（Pin）7：`LPCAM_D7_A`。

<a id="a3a15a5d9c88f736f38a9054133847e18"></a>

### `PIN_P8_7__OSPI0_RXDS1_C`

```c
#define PIN_P8_7__OSPI0_RXDS1_C ALIF_PINMUX(8, 7, 1)
```

端口（Port）8 的引脚（Pin）7：`OSPI0_RXDS1_C`。

<a id="a662c47d7f293a00715e2d94948bcba17"></a>

### `PIN_P8_7__QEC1_X_B`

```c
#define PIN_P8_7__QEC1_X_B ALIF_PINMUX(8, 7, 3)
```

端口（Port）8 的引脚（Pin）7：`QEC1_X_B`。

<a id="ab02bc30a86ad95d16bf0c51e5d90f133"></a>

### `PIN_P8_7__SD_D7_C`

```c
#define PIN_P8_7__SD_D7_C ALIF_PINMUX(8, 7, 5)
```

端口（Port）8 的引脚（Pin）7：`SD_D7_C`。

<a id="aea987334f62371b27ec6bb42168ff87f"></a>

### `PIN_P9_0__CAM_D8_B`

```c
#define PIN_P9_0__CAM_D8_B ALIF_PINMUX(9, 0, 6)
```

端口（Port）9 的引脚（Pin）0：`CAM_D8_B`。

<a id="a509eb405b8f384e617d11de1852866f9"></a>

### `PIN_P9_0__CDC_D8_A`

```c
#define PIN_P9_0__CDC_D8_A ALIF_PINMUX(9, 0, 5)
```

端口（Port）9 的引脚（Pin）0：`CDC_D8_A`。

<a id="a6c39dd61a6f51d3877bd1c31274d96d2"></a>

### `PIN_P9_0__GPIO`

```c
#define PIN_P9_0__GPIO ALIF_PINMUX(9, 0, 0)
```

引脚 `P9.0` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）0：`GPIO`。

<a id="a595fa627a03ebc400663b5dbccba599b"></a>

### `PIN_P9_0__I2S3_SDI_B`

```c
#define PIN_P9_0__I2S3_SDI_B ALIF_PINMUX(9, 0, 2)
```

端口（Port）9 的引脚（Pin）0：`I2S3_SDI_B`。

<a id="aed687e7b6d3de8b66abb80a6f30dc7ee"></a>

### `PIN_P9_0__LPSPI_SS3_A`

```c
#define PIN_P9_0__LPSPI_SS3_A ALIF_PINMUX(9, 0, 7)
```

端口（Port）9 的引脚（Pin）0：`LPSPI_SS3_A`。

<a id="a876adc4eec0f56c60d601b76e71e4e27"></a>

### `PIN_P9_0__OSPI1_RXDS1_C`

```c
#define PIN_P9_0__OSPI1_RXDS1_C ALIF_PINMUX(9, 0, 1)
```

端口（Port）9 的引脚（Pin）0：`OSPI1_RXDS1_C`。

<a id="ab5aefebdeac0bb35f8f5a98b5430b4a5"></a>

### `PIN_P9_0__QEC1_Y_B`

```c
#define PIN_P9_0__QEC1_Y_B ALIF_PINMUX(9, 0, 3)
```

端口（Port）9 的引脚（Pin）0：`QEC1_Y_B`。

<a id="abce9d55757744ded12d9044b3bc62967"></a>

### `PIN_P9_0__SD_CMD_C`

```c
#define PIN_P9_0__SD_CMD_C ALIF_PINMUX(9, 0, 4)
```

端口（Port）9 的引脚（Pin）0：`SD_CMD_C`。

<a id="ab99d67b8e8b6c7a3f279dc999eb1f045"></a>

### `PIN_P9_1__CAM_D9_B`

```c
#define PIN_P9_1__CAM_D9_B ALIF_PINMUX(9, 1, 6)
```

端口（Port）9 的引脚（Pin）1：`CAM_D9_B`。

<a id="aef6e841520a75a2a61a2783e5aaa1147"></a>

### `PIN_P9_1__CDC_D9_A`

```c
#define PIN_P9_1__CDC_D9_A ALIF_PINMUX(9, 1, 5)
```

端口（Port）9 的引脚（Pin）1：`CDC_D9_A`。

<a id="aab6b8b8f040a3f5afe7fbd03d3853b7a"></a>

### `PIN_P9_1__GPIO`

```c
#define PIN_P9_1__GPIO ALIF_PINMUX(9, 1, 0)
```

引脚 `P9.1` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）1：`GPIO`。

<a id="a468c77663dba4ffebd41e72ec28ce6b6"></a>

### `PIN_P9_1__I2S3_SDO_B`

```c
#define PIN_P9_1__I2S3_SDO_B ALIF_PINMUX(9, 1, 2)
```

端口（Port）9 的引脚（Pin）1：`I2S3_SDO_B`。

<a id="acd54d522aeb121ff465149fa6c3a123c"></a>

### `PIN_P9_1__LPSPI_SS4_A`

```c
#define PIN_P9_1__LPSPI_SS4_A ALIF_PINMUX(9, 1, 7)
```

端口（Port）9 的引脚（Pin）1：`LPSPI_SS4_A`。

<a id="a859e9d9dd96e1662c274caf7d12cfda6"></a>

### `PIN_P9_1__LPUART_RX_B`

```c
#define PIN_P9_1__LPUART_RX_B ALIF_PINMUX(9, 1, 1)
```

端口（Port）9 的引脚（Pin）1：`LPUART_RX_B`。

<a id="a36e98da75fa758bac27102d2f2d0ab05"></a>

### `PIN_P9_1__QEC1_Z_B`

```c
#define PIN_P9_1__QEC1_Z_B ALIF_PINMUX(9, 1, 3)
```

端口（Port）9 的引脚（Pin）1：`QEC1_Z_B`。

<a id="a0c5ce6459107866e3498303ea38afe09"></a>

### `PIN_P9_1__SD_CLK_C`

```c
#define PIN_P9_1__SD_CLK_C ALIF_PINMUX(9, 1, 4)
```

端口（Port）9 的引脚（Pin）1：`SD_CLK_C`。

<a id="a8b454fcb18e8070c814632929bfb9234"></a>

### `PIN_P9_2__CAM_D10_B`

```c
#define PIN_P9_2__CAM_D10_B ALIF_PINMUX(9, 2, 7)
```

端口（Port）9 的引脚（Pin）2：`CAM_D10_B`。

<a id="a42a94c1c7e34d8f7e709c86d594b62b0"></a>

### `PIN_P9_2__CDC_D10_A`

```c
#define PIN_P9_2__CDC_D10_A ALIF_PINMUX(9, 2, 6)
```

端口（Port）9 的引脚（Pin）2：`CDC_D10_A`。

<a id="a0049a6c751eb2db4593b4d7e3e830932"></a>

### `PIN_P9_2__GPIO`

```c
#define PIN_P9_2__GPIO ALIF_PINMUX(9, 2, 0)
```

引脚 `P9.2` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）2：`GPIO`。

<a id="af249d8b7910f0eb2232b8b1f11ad81ab"></a>

### `PIN_P9_2__I2S3_SDI_A`

```c
#define PIN_P9_2__I2S3_SDI_A ALIF_PINMUX(9, 2, 2)
```

端口（Port）9 的引脚（Pin）2：`I2S3_SDI_A`。

<a id="a2354961e2101a008a5a00ded07bae5f4"></a>

### `PIN_P9_2__LPUART_TX_B`

```c
#define PIN_P9_2__LPUART_TX_B ALIF_PINMUX(9, 2, 1)
```

端口（Port）9 的引脚（Pin）2：`LPUART_TX_B`。

<a id="a3c759baab9b5d753382b5630724786e8"></a>

### `PIN_P9_2__QEC2_X_B`

```c
#define PIN_P9_2__QEC2_X_B ALIF_PINMUX(9, 2, 4)
```

端口（Port）9 的引脚（Pin）2：`QEC2_X_B`。

<a id="acd7551ce812d7813b846ed6e2366157e"></a>

### `PIN_P9_2__SD_RST_C`

```c
#define PIN_P9_2__SD_RST_C ALIF_PINMUX(9, 2, 5)
```

端口（Port）9 的引脚（Pin）2：`SD_RST_C`。

<a id="ac59323909944702a56f068e8583781be"></a>

### `PIN_P9_2__SPI2_MISO_B`

```c
#define PIN_P9_2__SPI2_MISO_B ALIF_PINMUX(9, 2, 3)
```

端口（Port）9 的引脚（Pin）2：`SPI2_MISO_B`。

<a id="a820e7fd4aa0a9db16fb91ad00d8129e4"></a>

### `PIN_P9_3__CAM_D11_B`

```c
#define PIN_P9_3__CAM_D11_B ALIF_PINMUX(9, 3, 7)
```

端口（Port）9 的引脚（Pin）3：`CAM_D11_B`。

<a id="ac10618ac25d3fa32572beca9747930ea"></a>

### `PIN_P9_3__CDC_D11_A`

```c
#define PIN_P9_3__CDC_D11_A ALIF_PINMUX(9, 3, 6)
```

端口（Port）9 的引脚（Pin）3：`CDC_D11_A`。

<a id="a6343335b0acb9b74ddb08de62c328033"></a>

### `PIN_P9_3__GPIO`

```c
#define PIN_P9_3__GPIO ALIF_PINMUX(9, 3, 0)
```

引脚 `P9.3` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）3：`GPIO`。

<a id="a1374eb963d78b099332a18ebd9852d74"></a>

### `PIN_P9_3__HFXO_OUT_B`

```c
#define PIN_P9_3__HFXO_OUT_B ALIF_PINMUX(9, 3, 1)
```

端口（Port）9 的引脚（Pin）3：`HFXO_OUT_B`。

<a id="a20aa8587904237b969887d925da63126"></a>

### `PIN_P9_3__I2S3_SDO_A`

```c
#define PIN_P9_3__I2S3_SDO_A ALIF_PINMUX(9, 3, 3)
```

端口（Port）9 的引脚（Pin）3：`I2S3_SDO_A`。

<a id="a1739a3d7f0caa394957aa363664b747e"></a>

### `PIN_P9_3__QEC2_Y_B`

```c
#define PIN_P9_3__QEC2_Y_B ALIF_PINMUX(9, 3, 5)
```

端口（Port）9 的引脚（Pin）3：`QEC2_Y_B`。

<a id="a33a6f2669041c50a2274db4bcf089664"></a>

### `PIN_P9_3__SPI2_MOSI_B`

```c
#define PIN_P9_3__SPI2_MOSI_B ALIF_PINMUX(9, 3, 4)
```

端口（Port）9 的引脚（Pin）3：`SPI2_MOSI_B`。

<a id="a76dce03300f4eed2b0e94506295c3afe"></a>

### `PIN_P9_3__UART7_RX_B`

```c
#define PIN_P9_3__UART7_RX_B ALIF_PINMUX(9, 3, 2)
```

端口（Port）9 的引脚（Pin）3：`UART7_RX_B`。

<a id="a30980382d11bab5cee6798d0aeedd6d1"></a>

### `PIN_P9_4__CAM_D12_B`

```c
#define PIN_P9_4__CAM_D12_B ALIF_PINMUX(9, 4, 7)
```

端口（Port）9 的引脚（Pin）4：`CAM_D12_B`。

<a id="aeb8e8cc88d8e4918aa4e03eb62506002"></a>

### `PIN_P9_4__CDC_D12_A`

```c
#define PIN_P9_4__CDC_D12_A ALIF_PINMUX(9, 4, 6)
```

端口（Port）9 的引脚（Pin）4：`CDC_D12_A`。

<a id="aceea4881f07d17df9389a9bb2b5687b1"></a>

### `PIN_P9_4__GPIO`

```c
#define PIN_P9_4__GPIO ALIF_PINMUX(9, 4, 0)
```

引脚 `P9.4` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）4：`GPIO`。

<a id="a6013125ed1a4918027ffa0112b5e4dac"></a>

### `PIN_P9_4__I2C3_SDA_C`

```c
#define PIN_P9_4__I2C3_SDA_C ALIF_PINMUX(9, 4, 4)
```

端口（Port）9 的引脚（Pin）4：`I2C3_SDA_C`。

<a id="aab63b1b5e74ed1b493d64ee065f67ff9"></a>

### `PIN_P9_4__I2S3_SCLK_A`

```c
#define PIN_P9_4__I2S3_SCLK_A ALIF_PINMUX(9, 4, 2)
```

端口（Port）9 的引脚（Pin）4：`I2S3_SCLK_A`。

<a id="a49adce0d28a3dcb38967895905666e50"></a>

### `PIN_P9_4__QEC2_Z_B`

```c
#define PIN_P9_4__QEC2_Z_B ALIF_PINMUX(9, 4, 5)
```

端口（Port）9 的引脚（Pin）4：`QEC2_Z_B`。

<a id="acab28fd9dabc6f1ac721b078b6c7208a"></a>

### `PIN_P9_4__SPI2_SCLK_B`

```c
#define PIN_P9_4__SPI2_SCLK_B ALIF_PINMUX(9, 4, 3)
```

端口（Port）9 的引脚（Pin）4：`SPI2_SCLK_B`。

<a id="a310700b8fee4462929d48f363b88922a"></a>

### `PIN_P9_4__UART7_TX_B`

```c
#define PIN_P9_4__UART7_TX_B ALIF_PINMUX(9, 4, 1)
```

端口（Port）9 的引脚（Pin）4：`UART7_TX_B`。

<a id="a1f23bf2d9d927de033d8a479449ba284"></a>

### `PIN_P9_5__CAM_D13_B`

```c
#define PIN_P9_5__CAM_D13_B ALIF_PINMUX(9, 5, 7)
```

端口（Port）9 的引脚（Pin）5：`CAM_D13_B`。

<a id="ac48cfbf8f1f08bd5a6fd3a8b155b19e8"></a>

### `PIN_P9_5__CDC_D13_A`

```c
#define PIN_P9_5__CDC_D13_A ALIF_PINMUX(9, 5, 6)
```

端口（Port）9 的引脚（Pin）5：`CDC_D13_A`。

<a id="ad2941c38b5b4bd08db9cd7c9e5832ae3"></a>

### `PIN_P9_5__GPIO`

```c
#define PIN_P9_5__GPIO ALIF_PINMUX(9, 5, 0)
```

引脚 `P9.5` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）5：`GPIO`。

<a id="a728309c21e6482c2c6e2b683ef9c15a8"></a>

### `PIN_P9_5__I2C3_SCL_C`

```c
#define PIN_P9_5__I2C3_SCL_C ALIF_PINMUX(9, 5, 4)
```

端口（Port）9 的引脚（Pin）5：`I2C3_SCL_C`。

<a id="ac7aca81f38fb5faf22864186816c7680"></a>

### `PIN_P9_5__I2S3_WS_A`

```c
#define PIN_P9_5__I2S3_WS_A ALIF_PINMUX(9, 5, 2)
```

端口（Port）9 的引脚（Pin）5：`I2S3_WS_A`。

<a id="a5603b3daa4c24a6676468412da316b29"></a>

### `PIN_P9_5__OSPI1_D0_C`

```c
#define PIN_P9_5__OSPI1_D0_C ALIF_PINMUX(9, 5, 1)
```

端口（Port）9 的引脚（Pin）5：`OSPI1_D0_C`。

<a id="a15ab6ecc8d267121c684c4cf70255710"></a>

### `PIN_P9_5__QEC3_X_B`

```c
#define PIN_P9_5__QEC3_X_B ALIF_PINMUX(9, 5, 5)
```

端口（Port）9 的引脚（Pin）5：`QEC3_X_B`。

<a id="aad885f3710e8a8751f138066dcad8d2d"></a>

### `PIN_P9_5__SPI2_SS0_B`

```c
#define PIN_P9_5__SPI2_SS0_B ALIF_PINMUX(9, 5, 3)
```

端口（Port）9 的引脚（Pin）5：`SPI2_SS0_B`。

<a id="a96e81f854bec0687cfc9632a9bd4c9f9"></a>

### `PIN_P9_6__AUDIO_CLK_B`

```c
#define PIN_P9_6__AUDIO_CLK_B ALIF_PINMUX(9, 6, 2)
```

端口（Port）9 的引脚（Pin）6：`AUDIO_CLK_B`。

<a id="a77a3725429d3642ef80caf75d9338676"></a>

### `PIN_P9_6__CAM_D14_B`

```c
#define PIN_P9_6__CAM_D14_B ALIF_PINMUX(9, 6, 7)
```

端口（Port）9 的引脚（Pin）6：`CAM_D14_B`。

<a id="a077fa99bd66774a7dbde71b74867ff14"></a>

### `PIN_P9_6__CDC_D14_A`

```c
#define PIN_P9_6__CDC_D14_A ALIF_PINMUX(9, 6, 6)
```

端口（Port）9 的引脚（Pin）6：`CDC_D14_A`。

<a id="adebbf408f66abe66612efca4e0d40308"></a>

### `PIN_P9_6__GPIO`

```c
#define PIN_P9_6__GPIO ALIF_PINMUX(9, 6, 0)
```

引脚 `P9.6` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）6：`GPIO`。

<a id="aba985f9582cb768cba020cb5a937e808"></a>

### `PIN_P9_6__I2C3_SDA_B`

```c
#define PIN_P9_6__I2C3_SDA_B ALIF_PINMUX(9, 6, 4)
```

端口（Port）9 的引脚（Pin）6：`I2C3_SDA_B`。

<a id="aa519282029b6903e371928229f1e296d"></a>

### `PIN_P9_6__OSPI1_D1_C`

```c
#define PIN_P9_6__OSPI1_D1_C ALIF_PINMUX(9, 6, 1)
```

端口（Port）9 的引脚（Pin）6：`OSPI1_D1_C`。

<a id="a2221154ae285caa9f2ffe8381bb8645f"></a>

### `PIN_P9_6__QEC3_Y_B`

```c
#define PIN_P9_6__QEC3_Y_B ALIF_PINMUX(9, 6, 5)
```

端口（Port）9 的引脚（Pin）6：`QEC3_Y_B`。

<a id="a9247ba0566dd4266b13a372703b86cc1"></a>

### `PIN_P9_6__SPI2_SS1_B`

```c
#define PIN_P9_6__SPI2_SS1_B ALIF_PINMUX(9, 6, 3)
```

端口（Port）9 的引脚（Pin）6：`SPI2_SS1_B`。

<a id="aabf3438a1cd4b3663259241a7d5109a1"></a>

### `PIN_P9_7__CAM_D15_B`

```c
#define PIN_P9_7__CAM_D15_B ALIF_PINMUX(9, 7, 7)
```

端口（Port）9 的引脚（Pin）7：`CAM_D15_B`。

<a id="a246965bab24ee029b2f6306a2220dbb9"></a>

### `PIN_P9_7__CDC_D15_A`

```c
#define PIN_P9_7__CDC_D15_A ALIF_PINMUX(9, 7, 6)
```

端口（Port）9 的引脚（Pin）7：`CDC_D15_A`。

<a id="a76cb3601b18a43915bbeb240086db0c9"></a>

### `PIN_P9_7__GPIO`

```c
#define PIN_P9_7__GPIO ALIF_PINMUX(9, 7, 0)
```

引脚 `P9.7` 的复用功能（Alternate Functions）。

端口（Port）9 的引脚（Pin）7：`GPIO`。

<a id="a9fc6d8aba93de436b35c7dcac4c9c09c"></a>

### `PIN_P9_7__I2C3_SCL_B`

```c
#define PIN_P9_7__I2C3_SCL_B ALIF_PINMUX(9, 7, 4)
```

端口（Port）9 的引脚（Pin）7：`I2C3_SCL_B`。

<a id="a4b8484edd05564fb0a4688bda8de446f"></a>

### `PIN_P9_7__OSPI1_D2_C`

```c
#define PIN_P9_7__OSPI1_D2_C ALIF_PINMUX(9, 7, 1)
```

端口（Port）9 的引脚（Pin）7：`OSPI1_D2_C`。

<a id="ac4e8e4fca41208c4f4ca9f20d3fa40ed"></a>

### `PIN_P9_7__QEC3_Z_B`

```c
#define PIN_P9_7__QEC3_Z_B ALIF_PINMUX(9, 7, 5)
```

端口（Port）9 的引脚（Pin）7：`QEC3_Z_B`。

<a id="a22df37e2123ac9b1a6fb570f84aef07f"></a>

### `PIN_P9_7__SPI2_SS2_B`

```c
#define PIN_P9_7__SPI2_SS2_B ALIF_PINMUX(9, 7, 3)
```

端口（Port）9 的引脚（Pin）7：`SPI2_SS2_B`。

<a id="ac7e2363181acbefadb542099a9fb5537"></a>

### `PIN_P9_7__UART7_DE_B`

```c
#define PIN_P9_7__UART7_DE_B ALIF_PINMUX(9, 7, 2)
```

端口（Port）9 的引脚（Pin）7：`UART7_DE_B`。


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P024_alif-ensemble-pinctrl.h_源码浏览.md)
- [ALIF_PINMUX_PORT_MASK](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#a280dd67858770ceb0a88153aa29e09da)
- [ALIF_PINMUX_PORT_POS](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#a5d3f4f922452dc948bcc7727d9875107)
- [ALIF_PINMUX_PIN_MASK](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#a723a8df1e91c947c25af42db8b9f73dd)
- [ALIF_PINMUX_PIN_POS](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#a8c94e09e787a9fb1079e5fbe0aa875d2)
- [ALIF_PINMUX_FUNC_MASK](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#a195b3893d9913e77419e111178923a3d)
- [ALIF_PINMUX_FUNC_POS](P001_zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考.md#ab8529e7ad1002e2e112bf1286d4d6c62)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a195b3893d9913e77419e111178923a3d"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a280dd67858770ceb0a88153aa29e09da"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a5d3f4f922452dc948bcc7727d9875107"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a723a8df1e91c947c25af42db8b9f73dd"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a8c94e09e787a9fb1079e5fbe0aa875d2"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_ab8529e7ad1002e2e112bf1286d4d6c62"></a>

---

[上一章](P002_zephyr__dt-bindings__pinctrl__alif-ensemble-e1c-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__pinctrl__amebag2-pinctrl.h_文件参考.md)
