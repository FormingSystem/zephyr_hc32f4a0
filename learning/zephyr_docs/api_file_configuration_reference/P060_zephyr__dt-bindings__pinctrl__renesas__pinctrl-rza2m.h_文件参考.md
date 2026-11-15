---
id: learning.zephyr-docs.api-file-configuration-reference.page-60
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza2m_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rza2m.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza2m_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RZ/A2M的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

Renesas RZ/A2M的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 60.1\_宏定义（Macros）

<a id="r_ga60489d9b02b45ebc8fd95f0a7f9bcbe4"></a>

```c
#define RZA2M_PIN_NUM_IN_PORT 8
```

相关声明：[RZA2M_PIN_NUM_IN_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html#ga60489d9b02b45ebc8fd95f0a7f9bcbe4)。

每个端口（Port）的引脚数量（Number of Pins）。

<a id="r_ga40b2ad5eef6bf7984d65b6daa89fdba6"></a>

```c
#define RZA2M_PINMUX(b, p, f)
```

相关声明：[RZA2M_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html#ga40b2ad5eef6bf7984d65b6daa89fdba6)。

根据端口、引脚和功能（Port / Pin / Function）创建编码后的引脚复用值（Encoded Pinmux Value）。


## 60.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza2m_8h_source.html)
- [RZA2M_PIN_NUM_IN_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html#ga60489d9b02b45ebc8fd95f0a7f9bcbe4)
- [RZA2M_PINMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html#ga40b2ad5eef6bf7984d65b6daa89fdba6)

<a id="header-details"></a>

---

[上一章](P059_zephyr__net__net_stats.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P061_zephyr__posix__sched.h_文件参考.md)
