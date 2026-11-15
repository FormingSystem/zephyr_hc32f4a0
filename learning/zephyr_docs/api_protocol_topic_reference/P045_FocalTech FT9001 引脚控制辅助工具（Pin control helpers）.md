---
id: learning.zephyr-docs.api-protocol-topic-reference.page-45
title: FocalTech FT9001 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_FocalTech FT9001 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__focaltech__ft9001.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 FocalTech FT9001 引脚复用（Pin multiplexing）的宏。

<a id="details"></a>

FocalTech FT9001 引脚复用（pin multiplexing）配置宏。这些辅助宏描述与 `focaltech,ft9001-pinctrl` 兼容的设备树节点所用的 I/O 复用选择。`pinmux` 属性中的每个条目均使用 `FOCALTECH_PINMUX` 构造，依次传入“FT9001 IOCTRL 寄存器偏移量”中某个 I/O 控制器寄存器偏移量、该寄存器中控制相应焊盘（pad）或信号的位索引，以及该字段的复用选择值（0 为默认功能，1 为替代功能）。下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>

&pinctrl {
    usart3_default: usart3_default {
        group1 {
            pinmux = <FOCALTECH_PINMUX(FOCALTECH_IOCTRL_SCICR_OFFSET, 25, 1)>,
                     <FOCALTECH_PINMUX(FOCALTECH_IOCTRL_SCICR_OFFSET, 26, 1)>;
        };
    };
};
```

<a id="header-groups"></a>
<a id="groups"></a>

## 45.1\_主题（Topics）

<a id="r_focaltech_5Fpinctrl_5Fregs"></a>

相关声明：[FT9001 IOCTRL 寄存器偏移量（Register offsets）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html)。

用作 `FOCALTECH_PINMUX` 的 `reg` 参数的寄存器偏移量。

<a id="header-files"></a>
<a id="files"></a>

## 45.2\_文件（Files）

<a id="r_focaltech_5Fft9001_5Fpinctrl_2Eh"></a>

```c
file focaltech_ft9001_pinctrl.h
```

相关声明：[focaltech_ft9001_pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h.html)。

FocalTech FT9001的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 45.3\_宏定义（Macros）

<a id="r_ga7298e4f2acb3abbdbf4e45c54fdc612e"></a>

```c
#define FOCALTECH_PINMUX(reg, bit, value)
```

相关声明：[FOCALTECH_PINMUX](#ga7298e4f2acb3abbdbf4e45c54fdc612e)。

为 FT9001 引脚控制设备树属性编码一个引脚复用单元（pinmux cell）。

## 45.4\_详细说明（Detailed Documentation）

<a id="ga7298e4f2acb3abbdbf4e45c54fdc612e"></a>

### `FOCALTECH_PINMUX`

```c
#define FOCALTECH_PINMUX ( reg, bit, value )
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

展开值（Value）：

```c
(((reg) << FOCALTECH_PINCTRL_REG_POS) | ((bit) << FOCALTECH_PINCTRL_BIT_POS) |             \
 ((value) << FOCALTECH_PINCTRL_VALUE_POS))
```

为 FT9001 引脚控制设备树属性编码一个引脚复用单元（pinmux cell）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | I/O 复用寄存器偏移量，使用 `FOCALTECH_IOCTRL_*_OFFSET`。 |
| `bit` | 此复用控制字段在 `reg` 中的位索引（bit index）。 |
| `value` | 写入该字段的复用选择值（mux selection）。 |


## 45.5\_原页交叉引用（Cross References）

- [FT9001 IOCTRL 寄存器偏移量（Register offsets）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html)
- [focaltech_ft9001_pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P044_PECI 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P046_Renesas RA 引脚控制辅助工具（Pin control helpers）.md)
