---
id: learning.zephyr-docs.api-platform-topic-reference.page-26
title: ITE IT8XXX2唤醒控制器（Wake-up Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_ITE IT8XXX2唤醒控制器（Wake-up Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT8XXX2 唤醒控制器（WUC）的设备树宏。

<a id="details"></a>

ITE IT8XXX2 唤醒控制器（Wake-Up Controller，WUC）的设备树宏（Devicetree Macros）。这些宏用于描述与 `ite,it8xxx2-wuc` 和 `ite,it8xxx2-wuc-map` 兼容控制器配合使用的唤醒控制器单元（Cells）。WUC 映射引用 WUC 组节点（Group Node）及该组内唤醒输入（Wake-Up Input）的位掩码（Bit Mask）；当某组没有关联的边沿触发寄存器（Edge-Trigger Register）时，使用 `IT8XXX2_WUC_UNUSED_REG`。`WUC_TYPE_EDGE_*` 标志选择唤醒输入的边沿触发模式（Edge Trigger Mode）。

```c
wuc_wu20: wu20 {
        wucs = <&wuc2 BIT(0)>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 26.1\_文件（Files）

<a id="r_it8xxx2-wuc_2Eh"></a>

```c
file it8xxx2-wuc.h
```

相关声明：[it8xxx2-wuc.h](../api_file_runtime_reference/P029_zephyr__dt-bindings__interrupt-controller__it8xxx2-wuc.h_文件参考.md)。

ITE IT8XXX2唤醒控制器（Wake-Up Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.2\_宏定义（Macros）

<a id="r_ga61868a556512e102778c74ea81c0583f"></a>

```c
#define IT8XXX2_WUC_UNUSED_REG 0
```

相关声明：[IT8XXX2_WUC_UNUSED_REG](#ga61868a556512e102778c74ea81c0583f)。

`reg` 属性中的唤醒控制器保留寄存器（WUC Reserved Register）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 26.3\_唤醒控制器标志（Wakeup Controller Flags）

<a id="r_ga679ab1940f920cfe6c0fa1d5ed14a468"></a>

```c
#define WUC_TYPE_EDGE_RISING BIT(0)
```

相关声明：[WUC_TYPE_EDGE_RISING](#ga679ab1940f920cfe6c0fa1d5ed14a468)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器上升沿触发模式（WUC Rising Edge Trigger Mode）。

<a id="r_ga21b4240f97f62e69f23ea614de699955"></a>

```c
#define WUC_TYPE_EDGE_FALLING BIT(1)
```

相关声明：[WUC_TYPE_EDGE_FALLING](#ga21b4240f97f62e69f23ea614de699955)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器下降沿触发模式（WUC Falling Edge Trigger Mode）。

<a id="r_ga824c451f35efc9b287cd694a0c674095"></a>

```c
#define WUC_TYPE_EDGE_BOTH (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)
```

相关声明：[WUC_TYPE_EDGE_BOTH](#ga824c451f35efc9b287cd694a0c674095)、[WUC_TYPE_EDGE_RISING](#ga679ab1940f920cfe6c0fa1d5ed14a468)、[WUC_TYPE_EDGE_FALLING](#ga21b4240f97f62e69f23ea614de699955)。

唤醒控制器双边沿触发模式（WUC Both Edge Trigger Mode）。

## 26.4\_详细说明（Detailed Documentation）

<a id="ga61868a556512e102778c74ea81c0583f"></a>

### `IT8XXX2_WUC_UNUSED_REG`

```c
#define IT8XXX2_WUC_UNUSED_REG 0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/it8xxx2-wuc.h>
```

`reg` 属性中的唤醒控制器保留寄存器（WUC Reserved Register）。

<a id="ga824c451f35efc9b287cd694a0c674095"></a>

### `WUC_TYPE_EDGE_BOTH`

```c
#define WUC_TYPE_EDGE_BOTH (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/it8xxx2-wuc.h>
```

唤醒控制器双边沿触发模式（WUC Both Edge Trigger Mode）。

<a id="ga21b4240f97f62e69f23ea614de699955"></a>

### `WUC_TYPE_EDGE_FALLING`

```c
#define WUC_TYPE_EDGE_FALLING BIT(1)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/it8xxx2-wuc.h>
```

唤醒控制器下降沿触发模式（WUC Falling Edge Trigger Mode）。

<a id="ga679ab1940f920cfe6c0fa1d5ed14a468"></a>

### `WUC_TYPE_EDGE_RISING`

```c
#define WUC_TYPE_EDGE_RISING BIT(0)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/it8xxx2-wuc.h>
```

唤醒控制器上升沿触发模式（WUC Rising Edge Trigger Mode）。


## 26.5\_原页交叉引用（Cross References）

- [it8xxx2-wuc.h](../api_file_runtime_reference/P029_zephyr__dt-bindings__interrupt-controller__it8xxx2-wuc.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P025_ITE IT51XXX唤醒控制器（Wake-up Controller）.md) · [返回大纲](大纲.md) · [下一章](P027_Microchip SmartFusion2中断控制器（Interrupt Controller）.md)
