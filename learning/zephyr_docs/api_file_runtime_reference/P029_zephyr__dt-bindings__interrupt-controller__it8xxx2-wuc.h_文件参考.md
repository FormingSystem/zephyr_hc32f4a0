---
id: learning.zephyr-docs.api-file-runtime-reference.page-29
title: zephyr__dt-bindings__interrupt-controller__it8xxx2-wuc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_it8xxx2-wuc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT8XXX2唤醒控制器（Wake-Up Controller）的设备树宏。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

ITE IT8XXX2唤醒控制器（Wake-Up Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="r_ga61868a556512e102778c74ea81c0583f"></a>

```c
#define IT8XXX2_WUC_UNUSED_REG 0
```

相关声明：[IT8XXX2_WUC_UNUSED_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga61868a556512e102778c74ea81c0583f)。

`reg` 属性中的唤醒控制器保留寄存器（WUC Reserved Register）。

<a id="define-members-0"></a>

### 唤醒控制器标志（Wakeup Controller Flags）

<a id="r_ga679ab1940f920cfe6c0fa1d5ed14a468"></a>

```c
#define WUC_TYPE_EDGE_RISING BIT(0)
```

相关声明：[WUC_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga679ab1940f920cfe6c0fa1d5ed14a468)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器上升沿触发模式（WUC Rising Edge Trigger Mode）。

<a id="r_ga21b4240f97f62e69f23ea614de699955"></a>

```c
#define WUC_TYPE_EDGE_FALLING BIT(1)
```

相关声明：[WUC_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga21b4240f97f62e69f23ea614de699955)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

唤醒控制器下降沿触发模式（WUC Falling Edge Trigger Mode）。

<a id="r_ga824c451f35efc9b287cd694a0c674095"></a>

```c
#define WUC_TYPE_EDGE_BOTH (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)
```

相关声明：[WUC_TYPE_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga824c451f35efc9b287cd694a0c674095)、[WUC_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga679ab1940f920cfe6c0fa1d5ed14a468)、[WUC_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga21b4240f97f62e69f23ea614de699955)。

唤醒控制器双边沿触发模式（WUC Both Edge Trigger Mode）。


## 29.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P420_it8xxx2-wuc.h_源码浏览.md)
- [IT8XXX2_WUC_UNUSED_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga61868a556512e102778c74ea81c0583f)
- [WUC_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga679ab1940f920cfe6c0fa1d5ed14a468)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [WUC_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga21b4240f97f62e69f23ea614de699955)
- [WUC_TYPE_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it8xxx2__wuc.html#ga824c451f35efc9b287cd694a0c674095)

<a id="header-details"></a>

---

[上一章](P028_zephyr__dt-bindings__sensor__it51xxx_tach.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__sensor__it8xxx2_tach.h_文件参考.md)
