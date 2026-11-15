---
id: learning.zephyr-docs.api-file-reference.page-76
title: zephyr__dt-bindings__pinctrl__ene-kb106x-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ene-kb106x-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ene-kb106x-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb106x-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 76.1\_宏定义（Macros）

<a id="r_ab5585e56327f2b23ec89ba9debba0ee2"></a>

```c
#define PINMUX_FUNC_GPIO 0x00
```

相关声明：[PINMUX_FUNC_GPIO](#ab5585e56327f2b23ec89ba9debba0ee2)。

<a id="r_a98cfa6f81cd2d924b4b8410cc58dcced"></a>

```c
#define PINMUX_FUNC_A 0x00
```

相关声明：[PINMUX_FUNC_A](#a98cfa6f81cd2d924b4b8410cc58dcced)。

<a id="r_a1f94697f2a9f866e751fad5fa50ac54a"></a>

```c
#define PINMUX_FUNC_B 0x01
```

相关声明：[PINMUX_FUNC_B](#a1f94697f2a9f866e751fad5fa50ac54a)。

<a id="r_ad65d0f30a98080f3e21e2db0d6f63e90"></a>

```c
#define PINMUX_FUNC_C 0x02
```

相关声明：[PINMUX_FUNC_C](#ad65d0f30a98080f3e21e2db0d6f63e90)。

<a id="r_abcab76c799f9fefa55d8814c820f212a"></a>

```c
#define PINMUX_FUNC_D 0x03
```

相关声明：[PINMUX_FUNC_D](#abcab76c799f9fefa55d8814c820f212a)。

<a id="r_a74d6d35ca16164b0a0b68ee271b16e0d"></a>

```c
#define PINMUX_FUNC_MAX 0x04
```

相关声明：[PINMUX_FUNC_MAX](#a74d6d35ca16164b0a0b68ee271b16e0d)。

<a id="r_abac4bfb212bc96557b44d5f912939202"></a>

```c
#define ENE_KB106X_NO_PUD_POS 12
```

相关声明：[ENE_KB106X_NO_PUD_POS](#abac4bfb212bc96557b44d5f912939202)。

<a id="r_a3d996e8da6fd27b2e409f95d60c6d969"></a>

```c
#define ENE_KB106X_PD_POS 13
```

相关声明：[ENE_KB106X_PD_POS](#a3d996e8da6fd27b2e409f95d60c6d969)。

<a id="r_ae8011d97ae2c4a1626a5c060c75be8da"></a>

```c
#define ENE_KB106X_PU_POS 14
```

相关声明：[ENE_KB106X_PU_POS](#ae8011d97ae2c4a1626a5c060c75be8da)。

<a id="r_a2ba1fa41dfd21090130f7ae0849ccb9a"></a>

```c
#define ENE_KB106X_PUSH_PULL_POS 15
```

相关声明：[ENE_KB106X_PUSH_PULL_POS](#a2ba1fa41dfd21090130f7ae0849ccb9a)。

<a id="r_a88576538346e2c249ef5307487619dce"></a>

```c
#define ENE_KB106X_OPEN_DRAIN_POS 16
```

相关声明：[ENE_KB106X_OPEN_DRAIN_POS](#a88576538346e2c249ef5307487619dce)。

<a id="r_a969b0d246bc93d27662806924490134b"></a>

```c
#define ENE_KB106X_OUT_DIS_POS 17
```

相关声明：[ENE_KB106X_OUT_DIS_POS](#a969b0d246bc93d27662806924490134b)。

<a id="r_a57c26614d9fe66812dfdd6addc57e724"></a>

```c
#define ENE_KB106X_OUT_EN_POS 18
```

相关声明：[ENE_KB106X_OUT_EN_POS](#a57c26614d9fe66812dfdd6addc57e724)。

<a id="r_a5a6ed3b1af11083f5f424a47280369f5"></a>

```c
#define ENE_KB106X_OUT_HI_POS 19
```

相关声明：[ENE_KB106X_OUT_HI_POS](#a5a6ed3b1af11083f5f424a47280369f5)。

<a id="r_a61b2e54a54dee416d674fb71fe450319"></a>

```c
#define ENE_KB106X_OUT_LO_POS 20
```

相关声明：[ENE_KB106X_OUT_LO_POS](#a61b2e54a54dee416d674fb71fe450319)。

<a id="r_aad562cc00835aa70b1ebfc0d73cacb87"></a>

```c
#define ENE_KB106X_PIN_LOW_POWER_POS 21
```

相关声明：[ENE_KB106X_PIN_LOW_POWER_POS](#aad562cc00835aa70b1ebfc0d73cacb87)。

<a id="r_a040e843e147d311107bc2217440a3feb"></a>

```c
#define ENE_KB106X_IN_DIS_POS 22
```

相关声明：[ENE_KB106X_IN_DIS_POS](#a040e843e147d311107bc2217440a3feb)。

<a id="r_af66fd6f73d773180f6b4c2a5e55d2ee7"></a>

```c
#define ENE_KB106X_IN_EN_POS 23
```

相关声明：[ENE_KB106X_IN_EN_POS](#af66fd6f73d773180f6b4c2a5e55d2ee7)。

<a id="r_a7fda7bb531cdddc3c040352b33c6bc34"></a>

```c
#define ENE_KB106X_DRIVING_POS 31
```

相关声明：[ENE_KB106X_DRIVING_POS](#a7fda7bb531cdddc3c040352b33c6bc34)。

<a id="r_a87c5ce1628625ff0bf8ab57e58c952a3"></a>

```c
#define ENE_KB106X_PINMUX_PORT_POS 5
```

相关声明：[ENE_KB106X_PINMUX_PORT_POS](#a87c5ce1628625ff0bf8ab57e58c952a3)。

<a id="r_a14853b5c05a4c4d8a70ac2b257a0e2b2"></a>

```c
#define ENE_KB106X_PINMUX_PORT_MSK 0x7
```

相关声明：[ENE_KB106X_PINMUX_PORT_MSK](#a14853b5c05a4c4d8a70ac2b257a0e2b2)。

<a id="r_afe8dfa7a9f85d9bff0a3a066fbd5b4be"></a>

```c
#define ENE_KB106X_PINMUX_PIN_POS 0
```

相关声明：[ENE_KB106X_PINMUX_PIN_POS](#afe8dfa7a9f85d9bff0a3a066fbd5b4be)。

<a id="r_a48b9755d0765d1a78b259a7864e966f2"></a>

```c
#define ENE_KB106X_PINMUX_PIN_MSK 0x1f
```

相关声明：[ENE_KB106X_PINMUX_PIN_MSK](#a48b9755d0765d1a78b259a7864e966f2)。

<a id="r_a02262fa6f75e8574b61f65cc94eaa233"></a>

```c
#define ENE_KB106X_PINMUX_FUNC_POS 8
```

相关声明：[ENE_KB106X_PINMUX_FUNC_POS](#a02262fa6f75e8574b61f65cc94eaa233)。

<a id="r_a744daeb1e891195cf3735ffb7440f746"></a>

```c
#define ENE_KB106X_PINMUX_FUNC_MSK 0xf
```

相关声明：[ENE_KB106X_PINMUX_FUNC_MSK](#a744daeb1e891195cf3735ffb7440f746)。

<a id="r_a346c95084c7edb51010f04201c298205"></a>

```c
#define ENE_KB106X_EXTENDED_BANK 0x80
```

相关声明：[ENE_KB106X_EXTENDED_BANK](#a346c95084c7edb51010f04201c298205)。

<a id="r_a2df12498c98fe54610bf619d68f76a55"></a>

```c
#define ENE_KB106X_PINMUX(n, f)
```

相关声明：[ENE_KB106X_PINMUX](#a2df12498c98fe54610bf619d68f76a55)。

## 76.2\_详细说明（Detailed Documentation）

<a id="a7fda7bb531cdddc3c040352b33c6bc34"></a>

### `ENE_KB106X_DRIVING_POS`

```c
#define ENE_KB106X_DRIVING_POS 31
```

<a id="a346c95084c7edb51010f04201c298205"></a>

### `ENE_KB106X_EXTENDED_BANK`

```c
#define ENE_KB106X_EXTENDED_BANK 0x80
```

<a id="a040e843e147d311107bc2217440a3feb"></a>

### `ENE_KB106X_IN_DIS_POS`

```c
#define ENE_KB106X_IN_DIS_POS 22
```

<a id="af66fd6f73d773180f6b4c2a5e55d2ee7"></a>

### `ENE_KB106X_IN_EN_POS`

```c
#define ENE_KB106X_IN_EN_POS 23
```

<a id="abac4bfb212bc96557b44d5f912939202"></a>

### `ENE_KB106X_NO_PUD_POS`

```c
#define ENE_KB106X_NO_PUD_POS 12
```

<a id="a88576538346e2c249ef5307487619dce"></a>

### `ENE_KB106X_OPEN_DRAIN_POS`

```c
#define ENE_KB106X_OPEN_DRAIN_POS 16
```

<a id="a969b0d246bc93d27662806924490134b"></a>

### `ENE_KB106X_OUT_DIS_POS`

```c
#define ENE_KB106X_OUT_DIS_POS 17
```

<a id="a57c26614d9fe66812dfdd6addc57e724"></a>

### `ENE_KB106X_OUT_EN_POS`

```c
#define ENE_KB106X_OUT_EN_POS 18
```

<a id="a5a6ed3b1af11083f5f424a47280369f5"></a>

### `ENE_KB106X_OUT_HI_POS`

```c
#define ENE_KB106X_OUT_HI_POS 19
```

<a id="a61b2e54a54dee416d674fb71fe450319"></a>

### `ENE_KB106X_OUT_LO_POS`

```c
#define ENE_KB106X_OUT_LO_POS 20
```

<a id="a3d996e8da6fd27b2e409f95d60c6d969"></a>

### `ENE_KB106X_PD_POS`

```c
#define ENE_KB106X_PD_POS 13
```

<a id="aad562cc00835aa70b1ebfc0d73cacb87"></a>

### `ENE_KB106X_PIN_LOW_POWER_POS`

```c
#define ENE_KB106X_PIN_LOW_POWER_POS 21
```

<a id="a2df12498c98fe54610bf619d68f76a55"></a>

### `ENE_KB106X_PINMUX`

```c
#define ENE_KB106X_PINMUX ( n, f )
```

展开值（Value）：

```c
(((((n) >> 5) & ENE_KB106X_PINMUX_PORT_MSK) << ENE_KB106X_PINMUX_PORT_POS) |               \
 (((n) & ENE_KB106X_PINMUX_PIN_MSK) << ENE_KB106X_PINMUX_PIN_POS) |                        \
 (((f) & ENE_KB106X_PINMUX_FUNC_MSK) << ENE_KB106X_PINMUX_FUNC_POS))
```

<a id="a744daeb1e891195cf3735ffb7440f746"></a>

### `ENE_KB106X_PINMUX_FUNC_MSK`

```c
#define ENE_KB106X_PINMUX_FUNC_MSK 0xf
```

<a id="a02262fa6f75e8574b61f65cc94eaa233"></a>

### `ENE_KB106X_PINMUX_FUNC_POS`

```c
#define ENE_KB106X_PINMUX_FUNC_POS 8
```

<a id="a48b9755d0765d1a78b259a7864e966f2"></a>

### `ENE_KB106X_PINMUX_PIN_MSK`

```c
#define ENE_KB106X_PINMUX_PIN_MSK 0x1f
```

<a id="afe8dfa7a9f85d9bff0a3a066fbd5b4be"></a>

### `ENE_KB106X_PINMUX_PIN_POS`

```c
#define ENE_KB106X_PINMUX_PIN_POS 0
```

<a id="a14853b5c05a4c4d8a70ac2b257a0e2b2"></a>

### `ENE_KB106X_PINMUX_PORT_MSK`

```c
#define ENE_KB106X_PINMUX_PORT_MSK 0x7
```

<a id="a87c5ce1628625ff0bf8ab57e58c952a3"></a>

### `ENE_KB106X_PINMUX_PORT_POS`

```c
#define ENE_KB106X_PINMUX_PORT_POS 5
```

<a id="ae8011d97ae2c4a1626a5c060c75be8da"></a>

### `ENE_KB106X_PU_POS`

```c
#define ENE_KB106X_PU_POS 14
```

<a id="a2ba1fa41dfd21090130f7ae0849ccb9a"></a>

### `ENE_KB106X_PUSH_PULL_POS`

```c
#define ENE_KB106X_PUSH_PULL_POS 15
```

<a id="a98cfa6f81cd2d924b4b8410cc58dcced"></a>

### `PINMUX_FUNC_A`

```c
#define PINMUX_FUNC_A 0x00
```

<a id="a1f94697f2a9f866e751fad5fa50ac54a"></a>

### `PINMUX_FUNC_B`

```c
#define PINMUX_FUNC_B 0x01
```

<a id="ad65d0f30a98080f3e21e2db0d6f63e90"></a>

### `PINMUX_FUNC_C`

```c
#define PINMUX_FUNC_C 0x02
```

<a id="abcab76c799f9fefa55d8814c820f212a"></a>

### `PINMUX_FUNC_D`

```c
#define PINMUX_FUNC_D 0x03
```

<a id="ab5585e56327f2b23ec89ba9debba0ee2"></a>

### `PINMUX_FUNC_GPIO`

```c
#define PINMUX_FUNC_GPIO 0x00
```

<a id="a74d6d35ca16164b0a0b68ee271b16e0d"></a>

### `PINMUX_FUNC_MAX`

```c
#define PINMUX_FUNC_MAX 0x04
```


## 76.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P050_ene-kb106x-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aene-kb106x-pinctrl_8h_html_a02262fa6f75e8574b61f65cc94eaa233"></a>
<a id="aene-kb106x-pinctrl_8h_html_a14853b5c05a4c4d8a70ac2b257a0e2b2"></a>
<a id="aene-kb106x-pinctrl_8h_html_a48b9755d0765d1a78b259a7864e966f2"></a>
<a id="aene-kb106x-pinctrl_8h_html_a744daeb1e891195cf3735ffb7440f746"></a>
<a id="aene-kb106x-pinctrl_8h_html_a87c5ce1628625ff0bf8ab57e58c952a3"></a>
<a id="aene-kb106x-pinctrl_8h_html_afe8dfa7a9f85d9bff0a3a066fbd5b4be"></a>

---

[上一章](P075_zephyr__dt-bindings__pinctrl__emsdp-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P077_zephyr__dt-bindings__pinctrl__ene-kb1200-pinctrl.h_文件参考.md)
