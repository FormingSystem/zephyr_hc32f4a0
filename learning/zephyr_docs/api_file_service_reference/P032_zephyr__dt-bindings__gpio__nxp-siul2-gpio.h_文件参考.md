---
id: learning.zephyr-docs.api-file-service-reference.page-32
title: zephyr__dt-bindings__gpio__nxp-siul2-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_dt-bindings\_\_gpio\_\_nxp-siul2-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="define-members-0"></a>

### NXP SIUL2 GPIO 中断控制器路由标志（Interrupt Controller Routing Flags）。

NXP SIUL2 GPIO 专用标志（Specific Flags）。

驱动标志（Driver Flags）编码在 `gpio_dt_flags_t` 的高 8 位，具体如下：

NXP SIUL2 GPIO 中断控制器路由标志（Interrupt Controller Routing Flags）。

<a id="r_a6d3cd1e26c9e8cc5880dee8b2687b539"></a>

```c
#define NXP_SIUL2_GPIO_INT_WKPU (0x1U << NXP_SIUL2_GPIO_INT_CONTROLLER_POS)
```

相关声明：[NXP_SIUL2_GPIO_INT_WKPU](#a6d3cd1e26c9e8cc5880dee8b2687b539)。

中断（Interrupt）路由到唤醒单元控制器（WKPU Controller）。

## 32.2\_详细说明（Detailed Documentation）

<a id="a6d3cd1e26c9e8cc5880dee8b2687b539"></a>

### `NXP_SIUL2_GPIO_INT_WKPU`

```c
#define NXP_SIUL2_GPIO_INT_WKPU (0x1U << NXP_SIUL2_GPIO_INT_CONTROLLER_POS)
```

中断（Interrupt）路由到唤醒单元控制器（WKPU Controller）。


## 32.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P613_nxp-siul2-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P031_zephyr__dt-bindings__gpio__nxp-imx-igpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__bluetooth__mesh__od_priv_proxy_cli.h_文件参考.md)
