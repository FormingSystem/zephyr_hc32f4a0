---
id: learning.zephyr-docs.api-file-runtime-reference.page-47
title: zephyr__dt-bindings__gpio__numicro-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numicro-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_dt-bindings\_\_gpio\_\_numicro-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/numicro-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.1\_宏定义（Macros）

<a id="r_a81afdc677d616d7da3340c1b81e51a7c"></a>

```c
#define NUMICRO_GPIO_INPUT_DEBOUNCE (1U << 8)
```

相关声明：[NUMICRO_GPIO_INPUT_DEBOUNCE](#a81afdc677d616d7da3340c1b81e51a7c)。

启用 GPIO 引脚去抖（Debounce）。

<a id="r_a21e7cae6ea58a6ce04487e9083d00556"></a>

```c
#define NUMICRO_GPIO_INPUT_SCHMITT (1U << 9)
```

相关声明：[NUMICRO_GPIO_INPUT_SCHMITT](#a21e7cae6ea58a6ce04487e9083d00556)。

在输入端启用施密特触发器（Schmitt Trigger）。

## 47.2\_详细说明（Detailed Documentation）

<a id="a81afdc677d616d7da3340c1b81e51a7c"></a>

### `NUMICRO_GPIO_INPUT_DEBOUNCE`

```c
#define NUMICRO_GPIO_INPUT_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Nuvoton NuMicro 片上系统（SoCs）。

<a id="a21e7cae6ea58a6ce04487e9083d00556"></a>

### `NUMICRO_GPIO_INPUT_SCHMITT`

```c
#define NUMICRO_GPIO_INPUT_SCHMITT (1U << 9)
```

在输入端启用施密特触发器（Schmitt Trigger）。

施密特触发器标志（Schmitt Trigger Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Nuvoton NuMicro 片上系统（SoCs）。


## 47.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P607_numicro-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P046_zephyr__drivers__flash__nrf_qspi_nor.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__dt-bindings__gpio__nuvoton-npcx-gpio.h_文件参考.md)
