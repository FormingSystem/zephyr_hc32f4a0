---
id: learning.zephyr-docs.api-file-reference.page-77
title: zephyr__dt-bindings__pinctrl__ene-kb1200-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ene-kb1200-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 77.1\_宏定义（Macros）

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

<a id="r_a4079f1e59701aa562027b6ad1656caad"></a>

```c
#define ENE_KB1200_NO_PUD_POS 12
```

相关声明：[ENE_KB1200_NO_PUD_POS](#a4079f1e59701aa562027b6ad1656caad)。

<a id="r_a49849bc4e85bd82ebc9bb4d14dd2668c"></a>

```c
#define ENE_KB1200_PD_POS 13
```

相关声明：[ENE_KB1200_PD_POS](#a49849bc4e85bd82ebc9bb4d14dd2668c)。

<a id="r_af4297d42dd80877ce174a3d855df01b6"></a>

```c
#define ENE_KB1200_PU_POS 14
```

相关声明：[ENE_KB1200_PU_POS](#af4297d42dd80877ce174a3d855df01b6)。

<a id="r_a2fd07082dd0f55f0fcb33847476d52b1"></a>

```c
#define ENE_KB1200_PUSH_PULL_POS 15
```

相关声明：[ENE_KB1200_PUSH_PULL_POS](#a2fd07082dd0f55f0fcb33847476d52b1)。

<a id="r_af0eeb505113d97cdbe2afa0436718829"></a>

```c
#define ENE_KB1200_OPEN_DRAIN_POS 16
```

相关声明：[ENE_KB1200_OPEN_DRAIN_POS](#af0eeb505113d97cdbe2afa0436718829)。

<a id="r_ae7915329e0bf4a3961fdcf3a3bd706ac"></a>

```c
#define ENE_KB1200_OUT_DIS_POS 17
```

相关声明：[ENE_KB1200_OUT_DIS_POS](#ae7915329e0bf4a3961fdcf3a3bd706ac)。

<a id="r_af87d58a86781f6db2b698aeb598d8f80"></a>

```c
#define ENE_KB1200_OUT_EN_POS 18
```

相关声明：[ENE_KB1200_OUT_EN_POS](#af87d58a86781f6db2b698aeb598d8f80)。

<a id="r_ae7289ea9757e87dba5eca26b0d8ea869"></a>

```c
#define ENE_KB1200_OUT_HI_POS 19
```

相关声明：[ENE_KB1200_OUT_HI_POS](#ae7289ea9757e87dba5eca26b0d8ea869)。

<a id="r_a31048a09bc76aa17796ac29093c94c17"></a>

```c
#define ENE_KB1200_OUT_LO_POS 20
```

相关声明：[ENE_KB1200_OUT_LO_POS](#a31048a09bc76aa17796ac29093c94c17)。

<a id="r_ab68aefd0fa096ce5541f07d4b65881c0"></a>

```c
#define ENE_KB1200_PIN_LOW_POWER_POS 21
```

相关声明：[ENE_KB1200_PIN_LOW_POWER_POS](#ab68aefd0fa096ce5541f07d4b65881c0)。

<a id="r_ade268ffe7669879fbef2c7bf4600ffc2"></a>

```c
#define ENE_KB1200_PINMUX_PORT_POS 5
```

相关声明：[ENE_KB1200_PINMUX_PORT_POS](#ade268ffe7669879fbef2c7bf4600ffc2)。

<a id="r_ad673befbb525dba683cc65b64fdd3abd"></a>

```c
#define ENE_KB1200_PINMUX_PORT_MSK 0x7
```

相关声明：[ENE_KB1200_PINMUX_PORT_MSK](#ad673befbb525dba683cc65b64fdd3abd)。

<a id="r_abee9ef573bd89f90dc1bc2d65cfb2507"></a>

```c
#define ENE_KB1200_PINMUX_PIN_POS 0
```

相关声明：[ENE_KB1200_PINMUX_PIN_POS](#abee9ef573bd89f90dc1bc2d65cfb2507)。

<a id="r_ac1666ff38512cea6f97afc30b22dda0f"></a>

```c
#define ENE_KB1200_PINMUX_PIN_MSK 0x1f
```

相关声明：[ENE_KB1200_PINMUX_PIN_MSK](#ac1666ff38512cea6f97afc30b22dda0f)。

<a id="r_aff29cfeb36d2bb8a9ac5792b30f6c627"></a>

```c
#define ENE_KB1200_PINMUX_FUNC_POS 8
```

相关声明：[ENE_KB1200_PINMUX_FUNC_POS](#aff29cfeb36d2bb8a9ac5792b30f6c627)。

<a id="r_aa077424a43590e43f9067f3ab0a655ff"></a>

```c
#define ENE_KB1200_PINMUX_FUNC_MSK 0xf
```

相关声明：[ENE_KB1200_PINMUX_FUNC_MSK](#aa077424a43590e43f9067f3ab0a655ff)。

<a id="r_a2c86608b7173b6e66f3e55015035a41b"></a>

```c
#define ENE_KB1200_PINMUX(n, f)
```

相关声明：[ENE_KB1200_PINMUX](#a2c86608b7173b6e66f3e55015035a41b)。

## 77.2\_详细说明（Detailed Documentation）

<a id="a4079f1e59701aa562027b6ad1656caad"></a>

### `ENE_KB1200_NO_PUD_POS`

```c
#define ENE_KB1200_NO_PUD_POS 12
```

<a id="af0eeb505113d97cdbe2afa0436718829"></a>

### `ENE_KB1200_OPEN_DRAIN_POS`

```c
#define ENE_KB1200_OPEN_DRAIN_POS 16
```

<a id="ae7915329e0bf4a3961fdcf3a3bd706ac"></a>

### `ENE_KB1200_OUT_DIS_POS`

```c
#define ENE_KB1200_OUT_DIS_POS 17
```

<a id="af87d58a86781f6db2b698aeb598d8f80"></a>

### `ENE_KB1200_OUT_EN_POS`

```c
#define ENE_KB1200_OUT_EN_POS 18
```

<a id="ae7289ea9757e87dba5eca26b0d8ea869"></a>

### `ENE_KB1200_OUT_HI_POS`

```c
#define ENE_KB1200_OUT_HI_POS 19
```

<a id="a31048a09bc76aa17796ac29093c94c17"></a>

### `ENE_KB1200_OUT_LO_POS`

```c
#define ENE_KB1200_OUT_LO_POS 20
```

<a id="a49849bc4e85bd82ebc9bb4d14dd2668c"></a>

### `ENE_KB1200_PD_POS`

```c
#define ENE_KB1200_PD_POS 13
```

<a id="ab68aefd0fa096ce5541f07d4b65881c0"></a>

### `ENE_KB1200_PIN_LOW_POWER_POS`

```c
#define ENE_KB1200_PIN_LOW_POWER_POS 21
```

<a id="a2c86608b7173b6e66f3e55015035a41b"></a>

### `ENE_KB1200_PINMUX`

```c
#define ENE_KB1200_PINMUX ( n, f )
```

展开值（Value）：

```c
(((((n) >> 5) & ENE_KB1200_PINMUX_PORT_MSK) << ENE_KB1200_PINMUX_PORT_POS) |               \
 (((n) & ENE_KB1200_PINMUX_PIN_MSK) << ENE_KB1200_PINMUX_PIN_POS) |                        \
 (((f) & ENE_KB1200_PINMUX_FUNC_MSK) << ENE_KB1200_PINMUX_FUNC_POS))
```

<a id="aa077424a43590e43f9067f3ab0a655ff"></a>

### `ENE_KB1200_PINMUX_FUNC_MSK`

```c
#define ENE_KB1200_PINMUX_FUNC_MSK 0xf
```

<a id="aff29cfeb36d2bb8a9ac5792b30f6c627"></a>

### `ENE_KB1200_PINMUX_FUNC_POS`

```c
#define ENE_KB1200_PINMUX_FUNC_POS 8
```

<a id="ac1666ff38512cea6f97afc30b22dda0f"></a>

### `ENE_KB1200_PINMUX_PIN_MSK`

```c
#define ENE_KB1200_PINMUX_PIN_MSK 0x1f
```

<a id="abee9ef573bd89f90dc1bc2d65cfb2507"></a>

### `ENE_KB1200_PINMUX_PIN_POS`

```c
#define ENE_KB1200_PINMUX_PIN_POS 0
```

<a id="ad673befbb525dba683cc65b64fdd3abd"></a>

### `ENE_KB1200_PINMUX_PORT_MSK`

```c
#define ENE_KB1200_PINMUX_PORT_MSK 0x7
```

<a id="ade268ffe7669879fbef2c7bf4600ffc2"></a>

### `ENE_KB1200_PINMUX_PORT_POS`

```c
#define ENE_KB1200_PINMUX_PORT_POS 5
```

<a id="af4297d42dd80877ce174a3d855df01b6"></a>

### `ENE_KB1200_PU_POS`

```c
#define ENE_KB1200_PU_POS 14
```

<a id="a2fd07082dd0f55f0fcb33847476d52b1"></a>

### `ENE_KB1200_PUSH_PULL_POS`

```c
#define ENE_KB1200_PUSH_PULL_POS 15
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


## 77.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P051_ene-kb1200-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aene-kb1200-pinctrl_8h_html_aa077424a43590e43f9067f3ab0a655ff"></a>
<a id="aene-kb1200-pinctrl_8h_html_abee9ef573bd89f90dc1bc2d65cfb2507"></a>
<a id="aene-kb1200-pinctrl_8h_html_ac1666ff38512cea6f97afc30b22dda0f"></a>
<a id="aene-kb1200-pinctrl_8h_html_ad673befbb525dba683cc65b64fdd3abd"></a>
<a id="aene-kb1200-pinctrl_8h_html_ade268ffe7669879fbef2c7bf4600ffc2"></a>
<a id="aene-kb1200-pinctrl_8h_html_aff29cfeb36d2bb8a9ac5792b30f6c627"></a>

---

[上一章](P076_zephyr__dt-bindings__pinctrl__ene-kb106x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P078_zephyr__dt-bindings__dai__esai.h_文件参考.md)
