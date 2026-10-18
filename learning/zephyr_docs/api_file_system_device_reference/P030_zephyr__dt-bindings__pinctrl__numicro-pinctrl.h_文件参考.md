---
id: learning.zephyr-docs.api-file-system-device-reference.page-30
title: zephyr__dt-bindings__pinctrl__numicro-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_numicro-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 30.1\_宏定义（Macros）

<a id="r_ade38f6532bffc69965d508f87d8e1df8"></a>

```c
#define NUMICRO_MFP_SHIFT 0U
```

相关声明：[NUMICRO_MFP_SHIFT](#ade38f6532bffc69965d508f87d8e1df8)。

<a id="r_ac9f4334d26beb00d4dea13d857d5e7ec"></a>

```c
#define NUMICRO_MFP_MASK 0xFU
```

相关声明：[NUMICRO_MFP_MASK](#ac9f4334d26beb00d4dea13d857d5e7ec)。

<a id="r_a478aaec941e205a651ec9dd5e50739eb"></a>

```c
#define NUMICRO_PIN_SHIFT 4U
```

相关声明：[NUMICRO_PIN_SHIFT](#a478aaec941e205a651ec9dd5e50739eb)。

<a id="r_ad6e70da52aa12c4b62e8793bd3d64435"></a>

```c
#define NUMICRO_PIN_MASK 0xFU
```

相关声明：[NUMICRO_PIN_MASK](#ad6e70da52aa12c4b62e8793bd3d64435)。

<a id="r_aa189da0ec8b427feabb6e0bfe82d6e88"></a>

```c
#define NUMICRO_PORT_SHIFT 8U
```

相关声明：[NUMICRO_PORT_SHIFT](#aa189da0ec8b427feabb6e0bfe82d6e88)。

<a id="r_a82825df678162bc24705348ac1ac74ca"></a>

```c
#define NUMICRO_PORT_MASK 0xFU
```

相关声明：[NUMICRO_PORT_MASK](#a82825df678162bc24705348ac1ac74ca)。

<a id="r_a0309131a80b52c3c5ba0561b7cbd943f"></a>

```c
#define NUMICRO_PINMUX(port, pin, mfp)
```

相关声明：[NUMICRO_PINMUX](#a0309131a80b52c3c5ba0561b7cbd943f)。

引脚配置位域（pin configuration bit field）。

<a id="r_a23e9fef3fcbdab7aec502bd71c9e64cc"></a>

```c
#define NUMICRO_PORT(pinmux)
```

相关声明：[NUMICRO_PORT](#a23e9fef3fcbdab7aec502bd71c9e64cc)。

<a id="r_a1ab973be84bf86ae6c286b26379ac0dd"></a>

```c
#define NUMICRO_PIN(pinmux)
```

相关声明：[NUMICRO_PIN](#a1ab973be84bf86ae6c286b26379ac0dd)。

<a id="r_ac2c31c43ea1a65f7a5e9dae18ff39b0c"></a>

```c
#define NUMICRO_MFP(pinmux)
```

相关声明：[NUMICRO_MFP](#ac2c31c43ea1a65f7a5e9dae18ff39b0c)。

## 30.2\_详细说明（Detailed Documentation）

<a id="ac2c31c43ea1a65f7a5e9dae18ff39b0c"></a>

### `NUMICRO_MFP`

```c
#define NUMICRO_MFP ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> NUMICRO_MFP_SHIFT) & NUMICRO_MFP_MASK)
```

<a id="ac9f4334d26beb00d4dea13d857d5e7ec"></a>

### `NUMICRO_MFP_MASK`

```c
#define NUMICRO_MFP_MASK 0xFU
```

<a id="ade38f6532bffc69965d508f87d8e1df8"></a>

### `NUMICRO_MFP_SHIFT`

```c
#define NUMICRO_MFP_SHIFT 0U
```

<a id="a1ab973be84bf86ae6c286b26379ac0dd"></a>

### `NUMICRO_PIN`

```c
#define NUMICRO_PIN ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> NUMICRO_PIN_SHIFT) & NUMICRO_PIN_MASK)
```

<a id="ad6e70da52aa12c4b62e8793bd3d64435"></a>

### `NUMICRO_PIN_MASK`

```c
#define NUMICRO_PIN_MASK 0xFU
```

<a id="a478aaec941e205a651ec9dd5e50739eb"></a>

### `NUMICRO_PIN_SHIFT`

```c
#define NUMICRO_PIN_SHIFT 4U
```

<a id="a0309131a80b52c3c5ba0561b7cbd943f"></a>

### `NUMICRO_PINMUX`

```c
#define NUMICRO_PINMUX ( port, pin, mfp )
```

展开值（Value）：

```c
(((((port) - 'A') & NUMICRO_PORT_MASK) << NUMICRO_PORT_SHIFT) | \
(((pin) & NUMICRO_PIN_MASK) << NUMICRO_PIN_SHIFT) |             \
(((mfp) & NUMICRO_MFP_MASK) << NUMICRO_MFP_SHIFT))
```

引脚配置位域（pin configuration bit field）。

字段（Fields）：

- 多功能引脚字段 `mfp`：位 `[0:3]`。
- 引脚字段 `pin`：位 `[4:7]`。
- 端口字段 `port`：位 `[8:11]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port），取值为 `A` 至 `H`。 |
| `pin` | 引脚（Pin），取值为 0–15。 |
| `mfp` | 多功能值（multi-function value），取值为 0–15。 |

<a id="a23e9fef3fcbdab7aec502bd71c9e64cc"></a>

### `NUMICRO_PORT`

```c
#define NUMICRO_PORT ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> NUMICRO_PORT_SHIFT) & NUMICRO_PORT_MASK)
```

<a id="a82825df678162bc24705348ac1ac74ca"></a>

### `NUMICRO_PORT_MASK`

```c
#define NUMICRO_PORT_MASK 0xFU
```

<a id="aa189da0ec8b427feabb6e0bfe82d6e88"></a>

### `NUMICRO_PORT_SHIFT`

```c
#define NUMICRO_PORT_SHIFT 8U
```


## 30.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P608_numicro-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="anumicro-pinctrl_8h_html_ac9f4334d26beb00d4dea13d857d5e7ec"></a>
<a id="anumicro-pinctrl_8h_html_ade38f6532bffc69965d508f87d8e1df8"></a>
<a id="anumicro-pinctrl_8h_html_a478aaec941e205a651ec9dd5e50739eb"></a>
<a id="anumicro-pinctrl_8h_html_ad6e70da52aa12c4b62e8793bd3d64435"></a>
<a id="anumicro-pinctrl_8h_html_a82825df678162bc24705348ac1ac74ca"></a>
<a id="anumicro-pinctrl_8h_html_aa189da0ec8b427feabb6e0bfe82d6e88"></a>

---

[上一章](P029_zephyr__net__net_linkaddr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__dt-bindings__pinctrl__nxp-siul2-pinctrl.h_文件参考.md)
