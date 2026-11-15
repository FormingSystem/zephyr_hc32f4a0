---
id: learning.zephyr-docs.device-power-control-model-reference.page-72
title: rcar_pin_func_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrcar__pin__func.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_rcar\_pin\_func\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrcar__pin__func.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

R-Car引脚功能（Pin Function）的类型。

```c
#include <zephyr/drivers/pinctrl/pinctrl_rcar_common.h>
```

<a id="details"></a>

R-Car引脚功能（Pin Function）的类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_abc0b9a433a3b0e00da4a5fe733c31c7d"></a>

```c
uint8_t bank:5
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bank](#abc0b9a433a3b0e00da4a5fe733c31c7d)。

<a id="r_acf66a4904ab66054f9f8c0f680157481"></a>

```c
uint8_t shift:5
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[shift](#acf66a4904ab66054f9f8c0f680157481)。

<a id="r_aeafc3b430ee3137afdc362027c6b058c"></a>

```c
uint8_t func:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[func](#aeafc3b430ee3137afdc362027c6b058c)。

复用功能（Alternate function），取值为 0–15。

<a id="r_a90ca45273500d81009fb245d7e10fd84"></a>

```c
uint8_t group: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[group](#a90ca45273500d81009fb245d7e10fd84)。

GPIO 组，取值为 0–10。

<a id="r_a0e714822c49f80b771652183bd85f25a"></a>

```c
uint8_t bit: 5
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bit](#a0e714822c49f80b771652183bd85f25a)。

位编号，即：

## 72.2\_详细说明（Detailed Documentation）

<a id="abc0b9a433a3b0e00da4a5fe733c31c7d"></a>

### `bank`

```c
uint8_t rcar_pin_func::bank
```

<a id="a0e714822c49f80b771652183bd85f25a"></a>

### `bit`

```c
uint8_t rcar_pin_func::bit
```

位编号，即：

引脚编号，取值为 0–31。

<a id="aeafc3b430ee3137afdc362027c6b058c"></a>

### `func`

```c
uint8_t rcar_pin_func::func
```

复用功能（Alternate function），取值为 0–15。

<a id="a90ca45273500d81009fb245d7e10fd84"></a>

### `group`

```c
uint8_t rcar_pin_func::group
```

GPIO 组，取值为 0–10。

<a id="acf66a4904ab66054f9f8c0f680157481"></a>

### `shift`

```c
uint8_t rcar_pin_func::shift
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pinctrl/pinctrl_rcar_common.h`
- `zephyr/drivers/pinctrl/pinctrl_rcar_x5h_common.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pinctrl/pinctrl_rcar_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pinctrl_rcar_x5h_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_rcar_cpg_clk_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_renesas_elc_dt_spec_结构体.md)
