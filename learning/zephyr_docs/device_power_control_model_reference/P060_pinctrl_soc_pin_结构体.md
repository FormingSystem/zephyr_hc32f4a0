---
id: learning.zephyr-docs.device-power-control-model-reference.page-60
title: pinctrl_soc_pin_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpinctrl__soc__pin.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_pinctrl\_soc\_pin\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpinctrl__soc__pin.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

R-Car引脚（Pin）的类型。

```c
#include <zephyr/drivers/pinctrl/pinctrl_rcar_common.h>
```

<a id="details"></a>

R-Car引脚（Pin）的类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a0a2ceae237c3321a4ce1a3dd7a031322"></a>

```c
uint16_t pin
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pin](#a0a2ceae237c3321a4ce1a3dd7a031322)。

引脚 ID。

<a id="r_aa1e68145488d654ab03e114c3f9949a9"></a>

```c
struct rcar_pin_func func
```

相关声明：[rcar_pin_func](P072_rcar_pin_func_结构体.md)、[func](#aa1e68145488d654ab03e114c3f9949a9)。

引脚功能。

<a id="r_a8e7c595f1e24e227da45a2b5d5fad501"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a8e7c595f1e24e227da45a2b5d5fad501)。

标志，包括偏置（Bias）和引脚模式。

<a id="r_a0784ff8fd0192c54997ab5841153c82b"></a>

```c
uint8_t drive_strength
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[drive_strength](#a0784ff8fd0192c54997ab5841153c82b)。

<a id="r_a37e11e6cc80fdd3cedbbbee555e062ae"></a>

```c
uint8_t voltage
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[voltage](#a37e11e6cc80fdd3cedbbbee555e062ae)。

<a id="r_ae23bf05694cea7ddf3ebcafaf9f1c44d"></a>

```c
uint16_t drive_strength_microamp
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[drive_strength_microamp](#ae23bf05694cea7ddf3ebcafaf9f1c44d)。

驱动强度（Drive strength），适用于输出。

## 60.2\_详细说明（Detailed Documentation）

<a id="a0784ff8fd0192c54997ab5841153c82b"></a>

### `drive_strength`

```c
uint8_t pinctrl_soc_pin::drive_strength
```

<a id="ae23bf05694cea7ddf3ebcafaf9f1c44d"></a>

### `drive_strength_microamp`

```c
uint16_t pinctrl_soc_pin::drive_strength_microamp
```

驱动强度（Drive strength），适用于输出。

<a id="a8e7c595f1e24e227da45a2b5d5fad501"></a>

### `flags`

```c
uint8_t pinctrl_soc_pin::flags
```

标志，包括偏置（Bias）和引脚模式。

<a id="aa1e68145488d654ab03e114c3f9949a9"></a>

### `func`

```c
struct rcar_pin_func pinctrl_soc_pin::func
```

引脚功能。

<a id="a0a2ceae237c3321a4ce1a3dd7a031322"></a>

### `pin`

```c
uint16_t pinctrl_soc_pin::pin
```

引脚 ID。

<a id="a37e11e6cc80fdd3cedbbbee555e062ae"></a>

### `voltage`

```c
uint8_t pinctrl_soc_pin::voltage
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pinctrl/pinctrl_rcar_common.h`
- `zephyr/drivers/pinctrl/pinctrl_rcar_x5h_common.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pinctrl/pinctrl_rcar_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [rcar_pin_func](P072_rcar_pin_func_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pinctrl_rcar_x5h_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_pfm_exop_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_pulse_cell_结构体.md)
