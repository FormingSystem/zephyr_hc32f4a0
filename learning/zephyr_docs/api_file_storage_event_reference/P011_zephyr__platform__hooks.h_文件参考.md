---
id: learning.zephyr-docs.api-file-storage-event-reference.page-11
title: zephyr__platform__hooks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_platform\_\_hooks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

片上系统与开发板钩子（SoC and Board Hooks）。

查看此文件的源码。

<a id="details"></a>

SoC 与开发板钩子（SoC and Board Hooks）。本头文件提供函数原型，用于连接 Zephyr 架构／初始化代码与 `boards/`、`soc/` 下的 SoC／开发板专用逻辑。**注意（Note）：**这些都是由 SoC／开发板专用逻辑导出给操作系统内部逻辑的标准接口。应用代码不得直接访问，但可在操作系统内部自由使用。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_ad8a7ba989faae8d2f35ddbad9f5b4233"></a>

```c
void soc_early_reset_hook (void)
```

相关声明：[soc_early_reset_hook](#ad8a7ba989faae8d2f35ddbad9f5b4233)。

在数据 RAM 初始化之前、复位向量（Reset Vector）开始处执行的 SoC 钩子（Hook）。

<a id="r_ad6e8df1eefd1add03ad8379802bd989e"></a>

```c
void soc_reset_hook (void)
```

相关声明：[soc_reset_hook](#ad6e8df1eefd1add03ad8379802bd989e)。

在复位向量（Reset Vector）开始处执行的 SoC 钩子（Hook）。

<a id="r_adc333ec5f401d3d8311a496736bd1aa4"></a>

```c
void soc_prep_hook (void)
```

相关声明：[soc_prep_hook](#adc333ec5f401d3d8311a496736bd1aa4)。

在复位向量（Reset Vector）之后执行的 SoC 钩子（Hook）。

<a id="r_a5ee95ec1991b2083210194fe485b3a02"></a>

```c
void soc_early_init_hook (void)
```

相关声明：[soc_early_init_hook](#a5ee95ec1991b2083210194fe485b3a02)。

在内核与设备初始化之前执行的 SoC 钩子（Hook）。

<a id="r_ad3d12da84a31f3d4db5621635f5df687"></a>

```c
void soc_late_init_hook (void)
```

相关声明：[soc_late_init_hook](#ad3d12da84a31f3d4db5621635f5df687)。

在内核与设备初始化之后执行的 SoC 钩子（Hook）。

<a id="r_aed3aa074849066c29086ea37f8f9ef8a"></a>

```c
void soc_per_core_init_hook (void)
```

相关声明：[soc_per_core_init_hook](#aed3aa074849066c29086ea37f8f9ef8a)。

SoC 每核初始化（Per-core Initialization）。

<a id="r_a684e5461ecf7657b5ab646cdb9e41a51"></a>

```c
void board_early_init_hook (void)
```

相关声明：[board_early_init_hook](#a684e5461ecf7657b5ab646cdb9e41a51)。

在内核启动之前执行的开发板钩子（Board Hook）。

<a id="r_adc6098773fbea0f7ba1575f4a47649b1"></a>

```c
void board_late_init_hook (void)
```

相关声明：[board_late_init_hook](#adc6098773fbea0f7ba1575f4a47649b1)。

在内核启动之后执行的开发板钩子（Board Hook）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a684e5461ecf7657b5ab646cdb9e41a51"></a>

### `board_early_init_hook()`

```c
void board_early_init_hook ( void )
```

在内核启动之前执行的开发板钩子（Board Hook）。

在内核启动之前调用。此钩子（Hook）由开发板实现，可执行任何开发板专用初始化（Board-specific Initialization）。

<a id="adc6098773fbea0f7ba1575f4a47649b1"></a>

### `board_late_init_hook()`

```c
void board_late_init_hook ( void )
```

在内核启动之后执行的开发板钩子（Board Hook）。

在内核启动之后、调用 `main` 函数之前调用。此钩子（Hook）由开发板实现，可执行任何开发板专用初始化。

<a id="a5ee95ec1991b2083210194fe485b3a02"></a>

### `soc_early_init_hook()`

```c
void soc_early_init_hook ( void )
```

在内核与设备初始化之前执行的 SoC 钩子（Hook）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用初始化（SoC-specific Initialization）。

<a id="ad8a7ba989faae8d2f35ddbad9f5b4233"></a>

### `soc_early_reset_hook()`

```c
void soc_early_reset_hook ( void )
```

在数据 RAM 初始化之前、复位向量（Reset Vector）开始处执行的 SoC 钩子（Hook）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用初始化。详情参见 `SOC_EARLY_RESET_HOOK` Kconfig 选项，以及相应架构的 zephyr-rtos 启动实现（Startup Implementation）。

<a id="ad3d12da84a31f3d4db5621635f5df687"></a>

### `soc_late_init_hook()`

```c
void soc_late_init_hook ( void )
```

在内核与设备初始化之后执行的 SoC 钩子（Hook）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用初始化（SoC-specific Initialization）。

<a id="aed3aa074849066c29086ea37f8f9ef8a"></a>

### `soc_per_core_init_hook()`

```c
void soc_per_core_init_hook ( void )
```

SoC 每核初始化（Per-core Initialization）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用每核初始化（Per-core Initialization）。

<a id="adc333ec5f401d3d8311a496736bd1aa4"></a>

### `soc_prep_hook()`

```c
void soc_prep_hook ( void )
```

在复位向量（Reset Vector）之后执行的 SoC 钩子（Hook）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用初始化（SoC-specific Initialization）。

<a id="ad6e8df1eefd1add03ad8379802bd989e"></a>

### `soc_reset_hook()`

```c
void soc_reset_hook ( void )
```

在复位向量（Reset Vector）开始处执行的 SoC 钩子（Hook）。

此钩子（Hook）由 SoC 实现，可执行任何 SoC 专用初始化（SoC-specific Initialization）。


## 11.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P321_hooks.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__bluetooth__classic__hid_host.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__net__ieee802154.h_文件参考.md)
