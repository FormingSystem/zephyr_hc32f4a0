---
id: learning.zephyr-docs.api-file-reference.page-251
title: zephyr__dt-bindings__clock__npcx_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第251章\_zephyr\_\_dt-bindings\_\_clock\_\_npcx\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcx__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 251.1\_宏定义（Macros）

<a id="r_a9f3fc618897763975a65f66c619854ac"></a>

```c
#define NPCX_CLOCK_BUS_FREERUN 0
```

相关声明：[NPCX_CLOCK_BUS_FREERUN](#a9f3fc618897763975a65f66c619854ac)。

<a id="r_a382491652e75bde69fbac082e3402913"></a>

```c
#define NPCX_CLOCK_BUS_LFCLK 1
```

相关声明：[NPCX_CLOCK_BUS_LFCLK](#a382491652e75bde69fbac082e3402913)。

<a id="r_a0425fca091b81a5b9d1052a7d34b4de4"></a>

```c
#define NPCX_CLOCK_BUS_OSC 2
```

相关声明：[NPCX_CLOCK_BUS_OSC](#a0425fca091b81a5b9d1052a7d34b4de4)。

<a id="r_ab2bc8744b107a91a609f76f9efc57866"></a>

```c
#define NPCX_CLOCK_BUS_FIU 3
```

相关声明：[NPCX_CLOCK_BUS_FIU](#ab2bc8744b107a91a609f76f9efc57866)。

<a id="r_aef0bb3e64c85a87af7006b81616fbeac"></a>

```c
#define NPCX_CLOCK_BUS_CORE 4
```

相关声明：[NPCX_CLOCK_BUS_CORE](#aef0bb3e64c85a87af7006b81616fbeac)。

<a id="r_aa8598937aaed8d93dba381bfc407af6e"></a>

```c
#define NPCX_CLOCK_BUS_APB1 5
```

相关声明：[NPCX_CLOCK_BUS_APB1](#aa8598937aaed8d93dba381bfc407af6e)。

<a id="r_acf61d3dd0d38a2052effd4d86e3d1cd9"></a>

```c
#define NPCX_CLOCK_BUS_APB2 6
```

相关声明：[NPCX_CLOCK_BUS_APB2](#acf61d3dd0d38a2052effd4d86e3d1cd9)。

<a id="r_a652de72b9824db8f2c8401c337cd8ca0"></a>

```c
#define NPCX_CLOCK_BUS_APB3 7
```

相关声明：[NPCX_CLOCK_BUS_APB3](#a652de72b9824db8f2c8401c337cd8ca0)。

<a id="r_afb9bea70ff6783393a846602fa04ccf2"></a>

```c
#define NPCX_CLOCK_BUS_APB4 8
```

相关声明：[NPCX_CLOCK_BUS_APB4](#afb9bea70ff6783393a846602fa04ccf2)。

<a id="r_a4cdc44708ecbbe475c641f90e165da46"></a>

```c
#define NPCX_CLOCK_BUS_AHB6 9
```

相关声明：[NPCX_CLOCK_BUS_AHB6](#a4cdc44708ecbbe475c641f90e165da46)。

<a id="r_ac7df6df2fba5420e5d5f2c6752b0eb36"></a>

```c
#define NPCX_CLOCK_BUS_FMCLK 10
```

相关声明：[NPCX_CLOCK_BUS_FMCLK](#ac7df6df2fba5420e5d5f2c6752b0eb36)。

<a id="r_a1be6f0a37effd6c311efa0c6d0de09a8"></a>

```c
#define NPCX_CLOCK_BUS_FIU0 NPCX_CLOCK_BUS_FIU
```

相关声明：[NPCX_CLOCK_BUS_FIU0](#a1be6f0a37effd6c311efa0c6d0de09a8)、[NPCX_CLOCK_BUS_FIU](#ab2bc8744b107a91a609f76f9efc57866)。

<a id="r_a6ec4f8868b227546318d4fe54f7c020f"></a>

```c
#define NPCX_CLOCK_BUS_FIU1 11
```

相关声明：[NPCX_CLOCK_BUS_FIU1](#a6ec4f8868b227546318d4fe54f7c020f)。

<a id="r_afee88c3b0aaa96d84a72fa5978084d8e"></a>

```c
#define NPCX_CLOCK_BUS_MCLKD 12
```

相关声明：[NPCX_CLOCK_BUS_MCLKD](#afee88c3b0aaa96d84a72fa5978084d8e)。

<a id="r_a258041058970382aa34e7a0b58376341"></a>

```c
#define NPCX_PWDWN_CTL0 0
```

相关声明：[NPCX_PWDWN_CTL0](#a258041058970382aa34e7a0b58376341)。

<a id="r_a3cfc03c2f2b22b58bfaa62f8e753050f"></a>

```c
#define NPCX_PWDWN_CTL1 1
```

相关声明：[NPCX_PWDWN_CTL1](#a3cfc03c2f2b22b58bfaa62f8e753050f)。

<a id="r_a2253e4b15af7daf3ff65d90ba86c421c"></a>

```c
#define NPCX_PWDWN_CTL2 2
```

相关声明：[NPCX_PWDWN_CTL2](#a2253e4b15af7daf3ff65d90ba86c421c)。

<a id="r_afcd2d828dadff9fb0d76a20519bc5e79"></a>

```c
#define NPCX_PWDWN_CTL3 3
```

相关声明：[NPCX_PWDWN_CTL3](#afcd2d828dadff9fb0d76a20519bc5e79)。

<a id="r_a4019557265432cccae4e51784f0ad727"></a>

```c
#define NPCX_PWDWN_CTL4 4
```

相关声明：[NPCX_PWDWN_CTL4](#a4019557265432cccae4e51784f0ad727)。

<a id="r_ac18e443a37a88218a4224e0eab242ba2"></a>

```c
#define NPCX_PWDWN_CTL5 5
```

相关声明：[NPCX_PWDWN_CTL5](#ac18e443a37a88218a4224e0eab242ba2)。

<a id="r_ab3a1cbb76c0157237f668a1e33a61f1d"></a>

```c
#define NPCX_PWDWN_CTL6 6
```

相关声明：[NPCX_PWDWN_CTL6](#ab3a1cbb76c0157237f668a1e33a61f1d)。

<a id="r_a9134426b5250e98c1a5e81b7cf0a4c2a"></a>

```c
#define NPCX_PWDWN_CTL7 7
```

相关声明：[NPCX_PWDWN_CTL7](#a9134426b5250e98c1a5e81b7cf0a4c2a)。

<a id="r_a635ddd778df9d5c850c88ce6257b8443"></a>

```c
#define NPCX_PWDWN_CTL8 8
```

相关声明：[NPCX_PWDWN_CTL8](#a635ddd778df9d5c850c88ce6257b8443)。

<a id="r_ac126ce32d3110a50f89f60bd3defabb9"></a>

```c
#define NPCX_PWDWN_CTL9 9
```

相关声明：[NPCX_PWDWN_CTL9](#ac126ce32d3110a50f89f60bd3defabb9)。

<a id="r_a7fccea2270c428253610ebd8df38e851"></a>

```c
#define NPCX_PWDWN_CTL_COUNT 10
```

相关声明：[NPCX_PWDWN_CTL_COUNT](#a7fccea2270c428253610ebd8df38e851)。

## 251.2\_详细说明（Detailed Documentation）

<a id="a4cdc44708ecbbe475c641f90e165da46"></a>

### `NPCX_CLOCK_BUS_AHB6`

```c
#define NPCX_CLOCK_BUS_AHB6 9
```

<a id="aa8598937aaed8d93dba381bfc407af6e"></a>

### `NPCX_CLOCK_BUS_APB1`

```c
#define NPCX_CLOCK_BUS_APB1 5
```

<a id="acf61d3dd0d38a2052effd4d86e3d1cd9"></a>

### `NPCX_CLOCK_BUS_APB2`

```c
#define NPCX_CLOCK_BUS_APB2 6
```

<a id="a652de72b9824db8f2c8401c337cd8ca0"></a>

### `NPCX_CLOCK_BUS_APB3`

```c
#define NPCX_CLOCK_BUS_APB3 7
```

<a id="afb9bea70ff6783393a846602fa04ccf2"></a>

### `NPCX_CLOCK_BUS_APB4`

```c
#define NPCX_CLOCK_BUS_APB4 8
```

<a id="aef0bb3e64c85a87af7006b81616fbeac"></a>

### `NPCX_CLOCK_BUS_CORE`

```c
#define NPCX_CLOCK_BUS_CORE 4
```

<a id="ab2bc8744b107a91a609f76f9efc57866"></a>

### `NPCX_CLOCK_BUS_FIU`

```c
#define NPCX_CLOCK_BUS_FIU 3
```

<a id="a1be6f0a37effd6c311efa0c6d0de09a8"></a>

### `NPCX_CLOCK_BUS_FIU0`

```c
#define NPCX_CLOCK_BUS_FIU0 NPCX_CLOCK_BUS_FIU
```

<a id="a6ec4f8868b227546318d4fe54f7c020f"></a>

### `NPCX_CLOCK_BUS_FIU1`

```c
#define NPCX_CLOCK_BUS_FIU1 11
```

<a id="ac7df6df2fba5420e5d5f2c6752b0eb36"></a>

### `NPCX_CLOCK_BUS_FMCLK`

```c
#define NPCX_CLOCK_BUS_FMCLK 10
```

<a id="a9f3fc618897763975a65f66c619854ac"></a>

### `NPCX_CLOCK_BUS_FREERUN`

```c
#define NPCX_CLOCK_BUS_FREERUN 0
```

<a id="a382491652e75bde69fbac082e3402913"></a>

### `NPCX_CLOCK_BUS_LFCLK`

```c
#define NPCX_CLOCK_BUS_LFCLK 1
```

<a id="afee88c3b0aaa96d84a72fa5978084d8e"></a>

### `NPCX_CLOCK_BUS_MCLKD`

```c
#define NPCX_CLOCK_BUS_MCLKD 12
```

<a id="a0425fca091b81a5b9d1052a7d34b4de4"></a>

### `NPCX_CLOCK_BUS_OSC`

```c
#define NPCX_CLOCK_BUS_OSC 2
```

<a id="a258041058970382aa34e7a0b58376341"></a>

### `NPCX_PWDWN_CTL0`

```c
#define NPCX_PWDWN_CTL0 0
```

<a id="a3cfc03c2f2b22b58bfaa62f8e753050f"></a>

### `NPCX_PWDWN_CTL1`

```c
#define NPCX_PWDWN_CTL1 1
```

<a id="a2253e4b15af7daf3ff65d90ba86c421c"></a>

### `NPCX_PWDWN_CTL2`

```c
#define NPCX_PWDWN_CTL2 2
```

<a id="afcd2d828dadff9fb0d76a20519bc5e79"></a>

### `NPCX_PWDWN_CTL3`

```c
#define NPCX_PWDWN_CTL3 3
```

<a id="a4019557265432cccae4e51784f0ad727"></a>

### `NPCX_PWDWN_CTL4`

```c
#define NPCX_PWDWN_CTL4 4
```

<a id="ac18e443a37a88218a4224e0eab242ba2"></a>

### `NPCX_PWDWN_CTL5`

```c
#define NPCX_PWDWN_CTL5 5
```

<a id="ab3a1cbb76c0157237f668a1e33a61f1d"></a>

### `NPCX_PWDWN_CTL6`

```c
#define NPCX_PWDWN_CTL6 6
```

<a id="a9134426b5250e98c1a5e81b7cf0a4c2a"></a>

### `NPCX_PWDWN_CTL7`

```c
#define NPCX_PWDWN_CTL7 7
```

<a id="a635ddd778df9d5c850c88ce6257b8443"></a>

### `NPCX_PWDWN_CTL8`

```c
#define NPCX_PWDWN_CTL8 8
```

<a id="ac126ce32d3110a50f89f60bd3defabb9"></a>

### `NPCX_PWDWN_CTL9`

```c
#define NPCX_PWDWN_CTL9 9
```

<a id="a7fccea2270c428253610ebd8df38e851"></a>

### `NPCX_PWDWN_CTL_COUNT`

```c
#define NPCX_PWDWN_CTL_COUNT 10
```


## 251.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P129_npcx_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P250_zephyr__dt-bindings__reset__npcx9_reset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P252_zephyr__dt-bindings__espi__npcx_espi.h_文件参考.md)
