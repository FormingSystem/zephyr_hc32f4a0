---
id: learning.zephyr-docs.api-file-reference.page-21
title: zephyr__dt-bindings__clock__ast10x0_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_dt-bindings\_\_clock\_\_ast10x0\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_a037d8cf6fe0039675c6d0b3ace4421d9"></a>

```c
#define ASPEED_CLK_GRP_0_OFFSET (0)
```

相关声明：[ASPEED_CLK_GRP_0_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9)。

<a id="r_ab37a99b66163853d3e6ca8f4a9f4d57f"></a>

```c
#define ASPEED_CLK_GRP_1_OFFSET (32)
```

相关声明：[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a608fc420936e936d77ef94427419184d"></a>

```c
#define ASPEED_CLK_GRP_2_OFFSET (64)
```

相关声明：[ASPEED_CLK_GRP_2_OFFSET](#a608fc420936e936d77ef94427419184d)。

<a id="r_a3b37b31cba1a39e9d641c9f97ed32a28"></a>

```c
#define ASPEED_CLK_MCLK (ASPEED_CLK_GRP_0_OFFSET + 0)
```

相关声明：[ASPEED_CLK_MCLK](#a3b37b31cba1a39e9d641c9f97ed32a28)、[ASPEED_CLK_GRP_0_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9)。

<a id="r_a165a6862679163abf282c0eb67e94def"></a>

```c
#define ASPEED_CLK_USB_DEVICE (ASPEED_CLK_GRP_0_OFFSET + 7)
```

相关声明：[ASPEED_CLK_USB_DEVICE](#a165a6862679163abf282c0eb67e94def)、[ASPEED_CLK_GRP_0_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9)。

<a id="r_a74d307980b4aa1dcb0ad90c306d15448"></a>

```c
#define ASPEED_CLK_YCLK (ASPEED_CLK_GRP_0_OFFSET + 13)
```

相关声明：[ASPEED_CLK_YCLK](#a74d307980b4aa1dcb0ad90c306d15448)、[ASPEED_CLK_GRP_0_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9)。

<a id="r_a52b659f282d1bf17122e8d6cc4cb89ac"></a>

```c
#define ASPEED_CLK_LCLK (ASPEED_CLK_GRP_1_OFFSET + 0)
```

相关声明：[ASPEED_CLK_LCLK](#a52b659f282d1bf17122e8d6cc4cb89ac)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a601a84a17a471f751ae260374e39d66c"></a>

```c
#define ASPEED_CLK_ESPI (ASPEED_CLK_GRP_1_OFFSET + 1)
```

相关声明：[ASPEED_CLK_ESPI](#a601a84a17a471f751ae260374e39d66c)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a27b8f6c3f72aebbf0559e85bd43e8641"></a>

```c
#define ASPEED_CLK_REFCLK (ASPEED_CLK_GRP_1_OFFSET + 2)
```

相关声明：[ASPEED_CLK_REFCLK](#a27b8f6c3f72aebbf0559e85bd43e8641)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a75e3ccf175dbbfd553b0fe4bf4c8b63c"></a>

```c
#define ASPEED_CLK_LHCCLK (ASPEED_CLK_GRP_1_OFFSET + 5)
```

相关声明：[ASPEED_CLK_LHCCLK](#a75e3ccf175dbbfd553b0fe4bf4c8b63c)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_ab111e4dccb054d2b38c7acdda204ed19"></a>

```c
#define ASPEED_CLK_RSACLK (ASPEED_CLK_GRP_1_OFFSET + 6)
```

相关声明：[ASPEED_CLK_RSACLK](#ab111e4dccb054d2b38c7acdda204ed19)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a410403d49c1bb708d71bf8247dbdc0e2"></a>

```c
#define ASPEED_CLK_I3C0 (ASPEED_CLK_GRP_1_OFFSET + 8)
```

相关声明：[ASPEED_CLK_I3C0](#a410403d49c1bb708d71bf8247dbdc0e2)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_ae7e435ba8c54b91d2f0b4d244fe8c052"></a>

```c
#define ASPEED_CLK_I3C1 (ASPEED_CLK_GRP_1_OFFSET + 9)
```

相关声明：[ASPEED_CLK_I3C1](#ae7e435ba8c54b91d2f0b4d244fe8c052)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a1d189580a83d1167491ca053ef22b7fa"></a>

```c
#define ASPEED_CLK_I3C2 (ASPEED_CLK_GRP_1_OFFSET + 10)
```

相关声明：[ASPEED_CLK_I3C2](#a1d189580a83d1167491ca053ef22b7fa)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a755ef8cfe6c78e01a06113f2b3e78204"></a>

```c
#define ASPEED_CLK_I3C3 (ASPEED_CLK_GRP_1_OFFSET + 11)
```

相关声明：[ASPEED_CLK_I3C3](#a755ef8cfe6c78e01a06113f2b3e78204)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a3d645146fe6742ed4d56ece6265fc6e2"></a>

```c
#define ASPEED_CLK_UART1 (ASPEED_CLK_GRP_1_OFFSET + 16)
```

相关声明：[ASPEED_CLK_UART1](#a3d645146fe6742ed4d56ece6265fc6e2)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a2c86ad831ad2d720edd3a9c63ad9acb3"></a>

```c
#define ASPEED_CLK_UART2 (ASPEED_CLK_GRP_1_OFFSET + 17)
```

相关声明：[ASPEED_CLK_UART2](#a2c86ad831ad2d720edd3a9c63ad9acb3)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a8d1afc478750f1746f2bd280ec6aff74"></a>

```c
#define ASPEED_CLK_UART3 (ASPEED_CLK_GRP_1_OFFSET + 18)
```

相关声明：[ASPEED_CLK_UART3](#a8d1afc478750f1746f2bd280ec6aff74)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a5eb5ae4923c04c925b8763330ead0062"></a>

```c
#define ASPEED_CLK_UART4 (ASPEED_CLK_GRP_1_OFFSET + 19)
```

相关声明：[ASPEED_CLK_UART4](#a5eb5ae4923c04c925b8763330ead0062)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_ade068404e397460803ec43eac6bf2380"></a>

```c
#define ASPEED_CLK_MAC (ASPEED_CLK_GRP_1_OFFSET + 20)
```

相关声明：[ASPEED_CLK_MAC](#ade068404e397460803ec43eac6bf2380)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_ab834e06518b4054ade5ad5f43971c262"></a>

```c
#define ASPEED_CLK_UART6 (ASPEED_CLK_GRP_1_OFFSET + 22)
```

相关声明：[ASPEED_CLK_UART6](#ab834e06518b4054ade5ad5f43971c262)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a607209d0fc0eae0b7e16f9caf2e9266f"></a>

```c
#define ASPEED_CLK_UART7 (ASPEED_CLK_GRP_1_OFFSET + 23)
```

相关声明：[ASPEED_CLK_UART7](#a607209d0fc0eae0b7e16f9caf2e9266f)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_adde45b96aa4dfcacfe9830f0d18c08e7"></a>

```c
#define ASPEED_CLK_UART8 (ASPEED_CLK_GRP_1_OFFSET + 24)
```

相关声明：[ASPEED_CLK_UART8](#adde45b96aa4dfcacfe9830f0d18c08e7)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a5a99a566a02c34e68a56d2953e885457"></a>

```c
#define ASPEED_CLK_UART9 (ASPEED_CLK_GRP_1_OFFSET + 25)
```

相关声明：[ASPEED_CLK_UART9](#a5a99a566a02c34e68a56d2953e885457)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_afc181e59d2e1deca6af256d34d57e25c"></a>

```c
#define ASPEED_CLK_UART10 (ASPEED_CLK_GRP_1_OFFSET + 26)
```

相关声明：[ASPEED_CLK_UART10](#afc181e59d2e1deca6af256d34d57e25c)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_adbd0d3f7c91d1281e785363095a48077"></a>

```c
#define ASPEED_CLK_UART11 (ASPEED_CLK_GRP_1_OFFSET + 27)
```

相关声明：[ASPEED_CLK_UART11](#adbd0d3f7c91d1281e785363095a48077)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a7d6f4a6d172b574d4a28ff4b6777df69"></a>

```c
#define ASPEED_CLK_UART12 (ASPEED_CLK_GRP_1_OFFSET + 28)
```

相关声明：[ASPEED_CLK_UART12](#a7d6f4a6d172b574d4a28ff4b6777df69)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_ad2e83af2a4c95f211c9d5f65fb1991d7"></a>

```c
#define ASPEED_CLK_UART13 (ASPEED_CLK_GRP_1_OFFSET + 29)
```

相关声明：[ASPEED_CLK_UART13](#ad2e83af2a4c95f211c9d5f65fb1991d7)、[ASPEED_CLK_GRP_1_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)。

<a id="r_a9f9b71ba0ba43b4cebf27a077fd596ed"></a>

```c
#define ASPEED_CLK_PCLK (ASPEED_CLK_GRP_2_OFFSET + 0)
```

相关声明：[ASPEED_CLK_PCLK](#a9f9b71ba0ba43b4cebf27a077fd596ed)、[ASPEED_CLK_GRP_2_OFFSET](#a608fc420936e936d77ef94427419184d)。

<a id="r_abc5d16026e5da37c2a09fdef727fe7ce"></a>

```c
#define ASPEED_CLK_HCLK (ASPEED_CLK_GRP_2_OFFSET + 1)
```

相关声明：[ASPEED_CLK_HCLK](#abc5d16026e5da37c2a09fdef727fe7ce)、[ASPEED_CLK_GRP_2_OFFSET](#a608fc420936e936d77ef94427419184d)。

<a id="r_a9a92e4a9a3024f13c9ba2c73a73c2ddb"></a>

```c
#define ASPEED_CLK_UART5 (ASPEED_CLK_GRP_2_OFFSET + 2)
```

相关声明：[ASPEED_CLK_UART5](#a9a92e4a9a3024f13c9ba2c73a73c2ddb)、[ASPEED_CLK_GRP_2_OFFSET](#a608fc420936e936d77ef94427419184d)。

## 21.2\_详细说明（Detailed Documentation）

<a id="a601a84a17a471f751ae260374e39d66c"></a>

### `ASPEED_CLK_ESPI`

```c
#define ASPEED_CLK_ESPI (ASPEED_CLK_GRP_1_OFFSET + 1)
```

<a id="a037d8cf6fe0039675c6d0b3ace4421d9"></a>

### `ASPEED_CLK_GRP_0_OFFSET`

```c
#define ASPEED_CLK_GRP_0_OFFSET (0)
```

<a id="ab37a99b66163853d3e6ca8f4a9f4d57f"></a>

### `ASPEED_CLK_GRP_1_OFFSET`

```c
#define ASPEED_CLK_GRP_1_OFFSET (32)
```

<a id="a608fc420936e936d77ef94427419184d"></a>

### `ASPEED_CLK_GRP_2_OFFSET`

```c
#define ASPEED_CLK_GRP_2_OFFSET (64)
```

<a id="abc5d16026e5da37c2a09fdef727fe7ce"></a>

### `ASPEED_CLK_HCLK`

```c
#define ASPEED_CLK_HCLK (ASPEED_CLK_GRP_2_OFFSET + 1)
```

<a id="a410403d49c1bb708d71bf8247dbdc0e2"></a>

### `ASPEED_CLK_I3C0`

```c
#define ASPEED_CLK_I3C0 (ASPEED_CLK_GRP_1_OFFSET + 8)
```

<a id="ae7e435ba8c54b91d2f0b4d244fe8c052"></a>

### `ASPEED_CLK_I3C1`

```c
#define ASPEED_CLK_I3C1 (ASPEED_CLK_GRP_1_OFFSET + 9)
```

<a id="a1d189580a83d1167491ca053ef22b7fa"></a>

### `ASPEED_CLK_I3C2`

```c
#define ASPEED_CLK_I3C2 (ASPEED_CLK_GRP_1_OFFSET + 10)
```

<a id="a755ef8cfe6c78e01a06113f2b3e78204"></a>

### `ASPEED_CLK_I3C3`

```c
#define ASPEED_CLK_I3C3 (ASPEED_CLK_GRP_1_OFFSET + 11)
```

<a id="a52b659f282d1bf17122e8d6cc4cb89ac"></a>

### `ASPEED_CLK_LCLK`

```c
#define ASPEED_CLK_LCLK (ASPEED_CLK_GRP_1_OFFSET + 0)
```

<a id="a75e3ccf175dbbfd553b0fe4bf4c8b63c"></a>

### `ASPEED_CLK_LHCCLK`

```c
#define ASPEED_CLK_LHCCLK (ASPEED_CLK_GRP_1_OFFSET + 5)
```

<a id="ade068404e397460803ec43eac6bf2380"></a>

### `ASPEED_CLK_MAC`

```c
#define ASPEED_CLK_MAC (ASPEED_CLK_GRP_1_OFFSET + 20)
```

<a id="a3b37b31cba1a39e9d641c9f97ed32a28"></a>

### `ASPEED_CLK_MCLK`

```c
#define ASPEED_CLK_MCLK (ASPEED_CLK_GRP_0_OFFSET + 0)
```

<a id="a9f9b71ba0ba43b4cebf27a077fd596ed"></a>

### `ASPEED_CLK_PCLK`

```c
#define ASPEED_CLK_PCLK (ASPEED_CLK_GRP_2_OFFSET + 0)
```

<a id="a27b8f6c3f72aebbf0559e85bd43e8641"></a>

### `ASPEED_CLK_REFCLK`

```c
#define ASPEED_CLK_REFCLK (ASPEED_CLK_GRP_1_OFFSET + 2)
```

<a id="ab111e4dccb054d2b38c7acdda204ed19"></a>

### `ASPEED_CLK_RSACLK`

```c
#define ASPEED_CLK_RSACLK (ASPEED_CLK_GRP_1_OFFSET + 6)
```

<a id="a3d645146fe6742ed4d56ece6265fc6e2"></a>

### `ASPEED_CLK_UART1`

```c
#define ASPEED_CLK_UART1 (ASPEED_CLK_GRP_1_OFFSET + 16)
```

<a id="afc181e59d2e1deca6af256d34d57e25c"></a>

### `ASPEED_CLK_UART10`

```c
#define ASPEED_CLK_UART10 (ASPEED_CLK_GRP_1_OFFSET + 26)
```

<a id="adbd0d3f7c91d1281e785363095a48077"></a>

### `ASPEED_CLK_UART11`

```c
#define ASPEED_CLK_UART11 (ASPEED_CLK_GRP_1_OFFSET + 27)
```

<a id="a7d6f4a6d172b574d4a28ff4b6777df69"></a>

### `ASPEED_CLK_UART12`

```c
#define ASPEED_CLK_UART12 (ASPEED_CLK_GRP_1_OFFSET + 28)
```

<a id="ad2e83af2a4c95f211c9d5f65fb1991d7"></a>

### `ASPEED_CLK_UART13`

```c
#define ASPEED_CLK_UART13 (ASPEED_CLK_GRP_1_OFFSET + 29)
```

<a id="a2c86ad831ad2d720edd3a9c63ad9acb3"></a>

### `ASPEED_CLK_UART2`

```c
#define ASPEED_CLK_UART2 (ASPEED_CLK_GRP_1_OFFSET + 17)
```

<a id="a8d1afc478750f1746f2bd280ec6aff74"></a>

### `ASPEED_CLK_UART3`

```c
#define ASPEED_CLK_UART3 (ASPEED_CLK_GRP_1_OFFSET + 18)
```

<a id="a5eb5ae4923c04c925b8763330ead0062"></a>

### `ASPEED_CLK_UART4`

```c
#define ASPEED_CLK_UART4 (ASPEED_CLK_GRP_1_OFFSET + 19)
```

<a id="a9a92e4a9a3024f13c9ba2c73a73c2ddb"></a>

### `ASPEED_CLK_UART5`

```c
#define ASPEED_CLK_UART5 (ASPEED_CLK_GRP_2_OFFSET + 2)
```

<a id="ab834e06518b4054ade5ad5f43971c262"></a>

### `ASPEED_CLK_UART6`

```c
#define ASPEED_CLK_UART6 (ASPEED_CLK_GRP_1_OFFSET + 22)
```

<a id="a607209d0fc0eae0b7e16f9caf2e9266f"></a>

### `ASPEED_CLK_UART7`

```c
#define ASPEED_CLK_UART7 (ASPEED_CLK_GRP_1_OFFSET + 23)
```

<a id="adde45b96aa4dfcacfe9830f0d18c08e7"></a>

### `ASPEED_CLK_UART8`

```c
#define ASPEED_CLK_UART8 (ASPEED_CLK_GRP_1_OFFSET + 24)
```

<a id="a5a99a566a02c34e68a56d2953e885457"></a>

### `ASPEED_CLK_UART9`

```c
#define ASPEED_CLK_UART9 (ASPEED_CLK_GRP_1_OFFSET + 25)
```

<a id="a165a6862679163abf282c0eb67e94def"></a>

### `ASPEED_CLK_USB_DEVICE`

```c
#define ASPEED_CLK_USB_DEVICE (ASPEED_CLK_GRP_0_OFFSET + 7)
```

<a id="a74d307980b4aa1dcb0ad90c306d15448"></a>

### `ASPEED_CLK_YCLK`

```c
#define ASPEED_CLK_YCLK (ASPEED_CLK_GRP_0_OFFSET + 13)
```


## 21.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P041_ast10x0_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P020_zephyr__dt-bindings__pinctrl__arm-v2m_beetle-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__dt-bindings__reset__ast10x0_reset.h_文件参考.md)
