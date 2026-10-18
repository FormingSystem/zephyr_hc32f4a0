---
id: learning.zephyr-docs.api-file-service-reference.page-31
title: zephyr__dt-bindings__gpio__nxp-imx-igpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-imx-igpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_dt-bindings\_\_gpio\_\_nxp-imx-igpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-imx-igpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 上下拉强度标志（Pull Strength Flags）

上下拉强度标志（Pull Strength Flags）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。

仅适用于 NXP IMX 片上系统（SoCs）。

此接口支持两种上下拉强度（Pull Strengths）：`WEAK` 表示硬件（HW）支持的最低强度，`STRONG` 表示硬件支持的最高强度。

<a id="r_a0cdc8d4cade4e2411fa3686a5375a276"></a>

```c
#define NXP_IGPIO_PULL_WEAK (0x0U << NXP_IGPIO_PULL_STRENGTH_POS)
```

相关声明：[NXP_IGPIO_PULL_WEAK](#a0cdc8d4cade4e2411fa3686a5375a276)。

上拉／下拉强度（Pull-Up / Pull-Down Strengths），仅适用于 `CONFIG_SOC_SERIES_IMXRT10XX`。

<a id="r_a59c07b2a497ed2f8659d456986cc0702"></a>

```c
#define NXP_IGPIO_PULL_STRONG (0x1U << NXP_IGPIO_PULL_STRENGTH_POS)
```

相关声明：[NXP_IGPIO_PULL_STRONG](#a59c07b2a497ed2f8659d456986cc0702)。

## 31.2\_详细说明（Detailed Documentation）

<a id="a59c07b2a497ed2f8659d456986cc0702"></a>

### `NXP_IGPIO_PULL_STRONG`

```c
#define NXP_IGPIO_PULL_STRONG (0x1U << NXP_IGPIO_PULL_STRENGTH_POS)
```

<a id="a0cdc8d4cade4e2411fa3686a5375a276"></a>

### `NXP_IGPIO_PULL_WEAK`

```c
#define NXP_IGPIO_PULL_WEAK (0x0U << NXP_IGPIO_PULL_STRENGTH_POS)
```

上拉／下拉强度（Pull-Up / Pull-Down Strengths），仅适用于 `CONFIG_SOC_SERIES_IMXRT10XX`。


## 31.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P611_nxp-imx-igpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P030_zephyr__dt-bindings__gpio__nordic-npm2100-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__dt-bindings__gpio__nxp-siul2-gpio.h_文件参考.md)
