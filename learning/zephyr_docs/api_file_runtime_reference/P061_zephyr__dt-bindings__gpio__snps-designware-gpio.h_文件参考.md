---
id: learning.zephyr-docs.api-file-runtime-reference.page-61
title: zephyr__dt-bindings__gpio__snps-designware-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/snps-designware-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_zephyr\_\_dt-bindings\_\_gpio\_\_snps-designware-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/snps-designware-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 61.1\_宏定义（Macros）

<a id="r_a696fec562551fe17259140fe16cdcc1d"></a>

```c
#define DW_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[DW_GPIO_DEBOUNCE](#a696fec562551fe17259140fe16cdcc1d)。

启用 GPIO 引脚去抖（Debounce）。

<a id="r_a3791bd298cf7a44819a59fc967ee6b3b"></a>

```c
#define DW_GPIO_HW_MODE (1U << 9)
```

相关声明：[DW_GPIO_HW_MODE](#a3791bd298cf7a44819a59fc967ee6b3b)。

为引脚启用硬件控制／数据源（Hardware Control / Data Source）。

## 61.2\_详细说明（Detailed Documentation）

<a id="a696fec562551fe17259140fe16cdcc1d"></a>

### `DW_GPIO_DEBOUNCE`

```c
#define DW_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 SNPS DesignWare GPIO 控制器（Controllers）。

<a id="a3791bd298cf7a44819a59fc967ee6b3b"></a>

### `DW_GPIO_HW_MODE`

```c
#define DW_GPIO_HW_MODE (1U << 9)
```

为引脚启用硬件控制／数据源（Hardware Control / Data Source）。

配置引脚，使其由硬件数据源（Hardware Data Source）控制，前提是硬件支持此功能。


## 61.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P799_snps-designware-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P060_zephyr__mgmt__mcumgr__transport__smp_udp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P062_zephyr__drivers__spi_emul.h_文件参考.md)
