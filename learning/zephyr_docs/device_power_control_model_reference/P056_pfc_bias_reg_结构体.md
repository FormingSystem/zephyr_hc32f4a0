---
id: learning.zephyr-docs.device-power-control-model-reference.page-56
title: pfc_bias_reg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpfc__bias__reg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_pfc\_bias\_reg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpfc__bias__reg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

R-Car偏置寄存器（Bias Registers）的类型。

```c
#include <zephyr/drivers/pinctrl/pinctrl_rcar_common.h>
```

<a id="details"></a>

R-Car偏置寄存器（Bias Registers）的类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_af52bea8a971a9d529b88de56a96ba2f6"></a>

```c
uint32_t puen
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[puen](#af52bea8a971a9d529b88de56a96ba2f6)。

上拉/下拉使能寄存器（Pull-enable register）。

<a id="r_ad5b3f9a184e18852279224bc8bd410f1"></a>

```c
uint32_t pud
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pud](#ad5b3f9a184e18852279224bc8bd410f1)。

上拉/下拉使能或上拉控制寄存器。

<a id="r_aa096ddd0c55e1874be418e96a5824e48"></a>

```c
const uint16_t pins [32]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pins](#aa096ddd0c55e1874be418e96a5824e48)。

上拉/下拉选择或下拉控制寄存器。

## 56.2\_详细说明（Detailed Documentation）

<a id="aa096ddd0c55e1874be418e96a5824e48"></a>

### `pins`

```c
const uint16_t pfc_bias_reg::pins
```

上拉/下拉选择或下拉控制寄存器。

引脚 ID。

<a id="ad5b3f9a184e18852279224bc8bd410f1"></a>

### `pud`

```c
uint32_t pfc_bias_reg::pud
```

上拉/下拉使能或上拉控制寄存器。

上拉/下拉控制寄存器。

<a id="af52bea8a971a9d529b88de56a96ba2f6"></a>

### `puen`

```c
uint32_t pfc_bias_reg::puen
```

上拉/下拉使能寄存器（Pull-enable register）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pinctrl/pinctrl_rcar_common.h`
- `zephyr/drivers/pinctrl/pinctrl_rcar_x5h_common.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pinctrl/pinctrl_rcar_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pinctrl_rcar_x5h_common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_pd_msg_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_pfc_drive_reg_结构体.md)
