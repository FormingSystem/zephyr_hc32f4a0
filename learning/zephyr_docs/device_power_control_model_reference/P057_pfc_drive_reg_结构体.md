---
id: learning.zephyr-docs.device-power-control-model-reference.page-57
title: pfc_drive_reg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpfc__drive__reg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_pfc\_drive\_reg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpfc__drive__reg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

R-Car DRVCTRLn寄存器的类型。

```c
#include <zephyr/drivers/pinctrl/pinctrl_rcar_common.h>
```

<a id="details"></a>

R-Car DRVCTRLn寄存器的类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_ab9ae8bee56ea46c08ede93f67d1c520c"></a>

```c
uint32_t reg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reg](#ab9ae8bee56ea46c08ede93f67d1c520c)。

<a id="r_a92e5c3d645c3a1278f6e0b1afed677f4"></a>

```c
const struct pfc_drive_reg_field fields [8]
```

相关声明：[pfc_drive_reg_field](P058_pfc_drive_reg_field_结构体.md)、[fields](#a92e5c3d645c3a1278f6e0b1afed677f4)。

<a id="r_aaf9d7e2d485f6eb0801c31f9749ee096"></a>

```c
uint32_t drvctrl0
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[drvctrl0](#aaf9d7e2d485f6eb0801c31f9749ee096)。

驱动控制寄存器（Driving control register）0。

<a id="r_a7fdf928c9474496c086cbcebfec6cd15"></a>

```c
uint32_t drvctrl1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[drvctrl1](#a7fdf928c9474496c086cbcebfec6cd15)。

驱动控制寄存器 1。

<a id="r_a716001404ab11edd9fe7a1281afc41d3"></a>

```c
uint32_t drvctrl2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[drvctrl2](#a716001404ab11edd9fe7a1281afc41d3)。

驱动控制寄存器 2。

<a id="r_aaa4d83e9f4b91295c57e04420c80fddb"></a>

```c
const uint16_t pins [32]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pins](#aaa4d83e9f4b91295c57e04420c80fddb)。

引脚 ID。

## 57.2\_详细说明（Detailed Documentation）

<a id="aaf9d7e2d485f6eb0801c31f9749ee096"></a>

### `drvctrl0`

```c
uint32_t pfc_drive_reg::drvctrl0
```

驱动控制寄存器（Driving control register）0。

<a id="a7fdf928c9474496c086cbcebfec6cd15"></a>

### `drvctrl1`

```c
uint32_t pfc_drive_reg::drvctrl1
```

驱动控制寄存器 1。

<a id="a716001404ab11edd9fe7a1281afc41d3"></a>

### `drvctrl2`

```c
uint32_t pfc_drive_reg::drvctrl2
```

驱动控制寄存器 2。

<a id="a92e5c3d645c3a1278f6e0b1afed677f4"></a>

### `fields`

```c
const struct pfc_drive_reg_field pfc_drive_reg::fields[8]
```

<a id="aaa4d83e9f4b91295c57e04420c80fddb"></a>

### `pins`

```c
const uint16_t pfc_drive_reg::pins[32]
```

引脚 ID。

<a id="ab9ae8bee56ea46c08ede93f67d1c520c"></a>

### `reg`

```c
uint32_t pfc_drive_reg::reg
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pinctrl/pinctrl_rcar_common.h`
- `zephyr/drivers/pinctrl/pinctrl_rcar_x5h_common.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pinctrl/pinctrl_rcar_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pfc_drive_reg_field](P058_pfc_drive_reg_field_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pinctrl_rcar_x5h_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_pfc_bias_reg_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_pfc_drive_reg_field_结构体.md)
