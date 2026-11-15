---
id: learning.zephyr-docs.api-file-runtime-reference.page-48
title: zephyr__dt-bindings__gpio__nuvoton-npcx-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_dt-bindings\_\_gpio\_\_nuvoton-npcx-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 48.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 引脚电压标志（Voltage Flags）

电压标志（Voltage Flags）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展，供 Nuvoton NPCX 片上系统（SoCs）使用。

<a id="r_a92bcad554a75078ab25a13c59075cdff"></a>

```c
#define NPCX_GPIO_VOLTAGE_DEFAULT (0U << NPCX_GPIO_VOLTAGE_POS)
```

相关声明：[NPCX_GPIO_VOLTAGE_DEFAULT](#a92bcad554a75078ab25a13c59075cdff)。

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。

<a id="r_a21a9db9e72ea60be4a01c65113693fcb"></a>

```c
#define NPCX_GPIO_VOLTAGE_1P8 (1U << NPCX_GPIO_VOLTAGE_POS)
```

相关声明：[NPCX_GPIO_VOLTAGE_1P8](#a21a9db9e72ea60be4a01c65113693fcb)。

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

## 48.2\_详细说明（Detailed Documentation）

<a id="a21a9db9e72ea60be4a01c65113693fcb"></a>

### `NPCX_GPIO_VOLTAGE_1P8`

```c
#define NPCX_GPIO_VOLTAGE_1P8 (1U << NPCX_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="a92bcad554a75078ab25a13c59075cdff"></a>

### `NPCX_GPIO_VOLTAGE_DEFAULT`

```c
#define NPCX_GPIO_VOLTAGE_DEFAULT (0U << NPCX_GPIO_VOLTAGE_POS)
```

将引脚设置为默认电压电平（Default Voltage Level）：3.3 V。


## 48.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P610_nuvoton-npcx-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P047_zephyr__dt-bindings__gpio__numicro-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__net__offloaded_netdev.h_文件参考.md)
