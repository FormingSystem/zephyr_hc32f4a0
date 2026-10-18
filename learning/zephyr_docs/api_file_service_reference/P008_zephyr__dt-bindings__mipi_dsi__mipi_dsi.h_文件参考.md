---
id: learning.zephyr-docs.api-file-service-reference.page-8
title: zephyr__dt-bindings__mipi_dsi__mipi_dsi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dsi_2mipi__dsi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_dt-bindings\_\_mipi\_dsi\_\_mipi\_dsi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dsi_2mipi__dsi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="define-members-0"></a>

### MIPI 显示串行接口像素格式（MIPI-DSI Pixel Formats）

<a id="r_gafb9cb05fbca552449bab635544517d25"></a>

```c
#define MIPI_DSI_PIXFMT_RGB888 0U
```

相关声明：[MIPI_DSI_PIXFMT_RGB888](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gafb9cb05fbca552449bab635544517d25)。

RGB888 格式，每像素 24 位（24 bpp）。

<a id="r_gad7288299bb5248e8fab55d07c310cd85"></a>

```c
#define MIPI_DSI_PIXFMT_RGB666 1U
```

相关声明：[MIPI_DSI_PIXFMT_RGB666](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad7288299bb5248e8fab55d07c310cd85)。

RGB666 格式，每像素 24 位（24 bpp）。

<a id="r_gadad1c9a93585a16c643bc33ef280b38b"></a>

```c
#define MIPI_DSI_PIXFMT_RGB666_PACKED 2U
```

相关声明：[MIPI_DSI_PIXFMT_RGB666_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gadad1c9a93585a16c643bc33ef280b38b)。

紧凑 RGB666 格式（Packed RGB666），每像素 18 位（18 bpp）。

<a id="r_gab74cc16bec1613c5e1eff30de2aa25c6"></a>

```c
#define MIPI_DSI_PIXFMT_RGB565 3U
```

相关声明：[MIPI_DSI_PIXFMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gab74cc16bec1613c5e1eff30de2aa25c6)。

RGB565 格式，每像素 16 位（16 bpp）。


## 8.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P192_mipi_dsi.h_源码浏览.md)
- [MIPI_DSI_PIXFMT_RGB888](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gafb9cb05fbca552449bab635544517d25)
- [MIPI_DSI_PIXFMT_RGB666](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad7288299bb5248e8fab55d07c310cd85)
- [MIPI_DSI_PIXFMT_RGB666_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gadad1c9a93585a16c643bc33ef280b38b)
- [MIPI_DSI_PIXFMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gab74cc16bec1613c5e1eff30de2aa25c6)

---

[上一章](P007_zephyr__net__dhcpv6_server.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__gpio__ene-kb106x-gpio.h_文件参考.md)
