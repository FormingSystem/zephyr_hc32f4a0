---
id: learning.zephyr-docs.api-file-display-management-reference.page-8
title: zephyr__dt-bindings__mipi_dbi__mipi_dbi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_dt-bindings\_\_mipi\_dbi\_\_mipi\_dbi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga9aeeeef78898e1d649f96feccae2fcac"></a>

```c
#define MIPI_DBI_MODE_SPI_3WIRE 0x1
```

相关声明：[MIPI_DBI_MODE_SPI_3WIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga9aeeeef78898e1d649f96feccae2fcac)。

三线 SPI（SPI 3 Wire），Type C1。

<a id="r_ga5c27ef3aa3256e60495a7c511cbaf7a5"></a>

```c
#define MIPI_DBI_MODE_SPI_4WIRE 0x2
```

相关声明：[MIPI_DBI_MODE_SPI_4WIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga5c27ef3aa3256e60495a7c511cbaf7a5)。

四线 SPI（SPI 4 Wire），Type C3。

<a id="r_gad73dfe18498d59ed4bc2a9f15306d695"></a>

```c
#define MIPI_DBI_TE_NO_EDGE 0x0
```

相关声明：[MIPI_DBI_TE_NO_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad73dfe18498d59ed4bc2a9f15306d695)。

禁用 MIPI 显示总线接口（DBI）的撕裂效应使能信号同步（Tearing Enable Synchronization）。

<a id="r_gaa83bb6eb37251b1a5b4cd8b60b076d17"></a>

```c
#define MIPI_DBI_TE_RISING_EDGE 0x1
```

相关声明：[MIPI_DBI_TE_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa83bb6eb37251b1a5b4cd8b60b076d17)。

在撕裂效应使能（TE）信号上升沿进行 MIPI DBI 同步。

<a id="r_gad1ebe36d7048bca248d3a03b63e1e9c7"></a>

```c
#define MIPI_DBI_TE_FALLING_EDGE 0x2
```

相关声明：[MIPI_DBI_TE_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad1ebe36d7048bca248d3a03b63e1e9c7)。

在撕裂效应使能（TE）信号下降沿进行 MIPI DBI 同步。

<a id="r_ga900ba99dbfe81a0856a008809e9f1273"></a>

```c
#define MIPI_DBI_SPI_XFR_8BIT 8
```

相关声明：[MIPI_DBI_SPI_XFR_8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga900ba99dbfe81a0856a008809e9f1273)。

以 8 位块通过 SPI 传输 DBI 命令，这是四线 SPI（Type C3）模式的默认行为。

<a id="r_ga55bd42d5252cedb919cc0b0bd1d6cdf7"></a>

```c
#define MIPI_DBI_SPI_XFR_16BIT 16
```

相关声明：[MIPI_DBI_SPI_XFR_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga55bd42d5252cedb919cc0b0bd1d6cdf7)。

以 16 位块通过 SPI 传输 DBI 命令，这是四线 SPI（Type C3）模式中少见的行为。

<a id="define-members-0"></a>

### 基于 Motorola 6800 总线的 MIPI DBI Type A 并行总线协议（Parallel Bus Protocol）

原始示例（Example）：

```text
         -.   .--------.      .------------------------
CS        '---'        '---'

         -------------------------------------------
RESX

                   .--------------------------------
D/CX     ----------'


R/WX     -------------------------------------------

         -------------------------------------------
E

          .--------.   .--------------------------.
D[15:0]/ -| COMMAND|---|  DATA                    |
D[8:0]/   '--------'   '--------------------------'
D[7:0]
```

详细周期图（Cycle Diagram）请参阅 MIPI 显示总线接口（DBI）规范。

<a id="r_ga4e59f3d57007cea38ae04aac74c2b5dc"></a>

```c
#define MIPI_DBI_MODE_6800_BUS_16_BIT 0x3
```

相关声明：[MIPI_DBI_MODE_6800_BUS_16_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga4e59f3d57007cea38ae04aac74c2b5dc)。

Motorola 6800 并行总线（Parallel Bus），16 位宽。

<a id="r_gaa89b584bc5bf5a153926ba808de49131"></a>

```c
#define MIPI_DBI_MODE_6800_BUS_9_BIT 0x4
```

相关声明：[MIPI_DBI_MODE_6800_BUS_9_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa89b584bc5bf5a153926ba808de49131)。

Motorola 6800 并行总线（Parallel Bus），9 位宽。

<a id="r_gab9b80bb367e7bd084ae490bbff9034b9"></a>

```c
#define MIPI_DBI_MODE_6800_BUS_8_BIT 0x5
```

相关声明：[MIPI_DBI_MODE_6800_BUS_8_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab9b80bb367e7bd084ae490bbff9034b9)。

Motorola 6800 并行总线（Parallel Bus），8 位宽。

<a id="define-members-1"></a>

### 基于 Intel 8080 总线的 MIPI DBI Type B 并行总线协议（Parallel Bus Protocol）

原始示例（Example）：

```text
         -.                                       .-
CS        '---------------------------------------'

         -------------------------------------------
RESX

         --.           .----------------------------
D/CX       '-----------'

         ---.   .--------.   .----------------------
WRX         '---'        '---'

         -------------------------------------------
RDX

            .--------.   .--------------------------.
D[15:0]/ ---| COMMAND|---|  DATA                    |
D[8:0]/     '--------'   '--------------------------'
D[7:0]
```

详细周期图（Cycle Diagram）请参阅 MIPI 显示总线接口（DBI）规范。

<a id="r_ga3c3d1c379c4bc07847412b3bd5b76cb1"></a>

```c
#define MIPI_DBI_MODE_8080_BUS_16_BIT 0x6
```

相关声明：[MIPI_DBI_MODE_8080_BUS_16_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga3c3d1c379c4bc07847412b3bd5b76cb1)。

Intel 8080 并行总线（Parallel Bus），16 位宽。

<a id="r_gad4c61d48021f38c0759daf9a401f24c7"></a>

```c
#define MIPI_DBI_MODE_8080_BUS_9_BIT 0x7
```

相关声明：[MIPI_DBI_MODE_8080_BUS_9_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad4c61d48021f38c0759daf9a401f24c7)。

Intel 8080 并行总线（Parallel Bus），9 位宽。

<a id="r_ga3d26bb4556822d12567c62c7ff2c3bb9"></a>

```c
#define MIPI_DBI_MODE_8080_BUS_8_BIT 0x8
```

相关声明：[MIPI_DBI_MODE_8080_BUS_8_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga3d26bb4556822d12567c62c7ff2c3bb9)。

Intel 8080 并行总线（Parallel Bus），8 位宽。

<a id="define-members-2"></a>

### MIPI DBI Type A 或 Type B 接口的颜色编码（Color Coding）

<a id="r_ga11d68e3a9a449ec8fce4bbae637af08c"></a>

```c
#define MIPI_DBI_MODE_RGB332 (0x1 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB332](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga11d68e3a9a449ec8fce4bbae637af08c)。

RGB332，每像素 8 位（8 bpp）。

<a id="r_gac18f3926b86551908300f055ebe9212a"></a>

```c
#define MIPI_DBI_MODE_RGB444 (0x2 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB444](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gac18f3926b86551908300f055ebe9212a)。

RGB444，每像素 12 位（12 bpp）。

<a id="r_ga53bbca5860b8845e892d3605c44877b4"></a>

```c
#define MIPI_DBI_MODE_RGB565 (0x3 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga53bbca5860b8845e892d3605c44877b4)。

RGB565，每像素 16 位（16 bpp）。

<a id="r_gaa264bb127fbbece867bf444c8168b6f4"></a>

```c
#define MIPI_DBI_MODE_RGB666_1 (0x4 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB666_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa264bb127fbbece867bf444c8168b6f4)。

RGB666，每像素 18 位（18 bpp）。

<a id="r_gafb1d7ae963a9cfedadaa4c4299ad7f99"></a>

```c
#define MIPI_DBI_MODE_RGB666_2 (0x5 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB666_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafb1d7ae963a9cfedadaa4c4299ad7f99)。

RGB666，每像素 18 位（18 bpp）。

<a id="r_gad7195e4b6aad08002b4b61a3052bf8e7"></a>

```c
#define MIPI_DBI_MODE_RGB888_1 (0x6 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB888_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad7195e4b6aad08002b4b61a3052bf8e7)。

RGB888，每像素 24 位（24 bpp）。

<a id="r_ga0edb36a8b62a252bff686f0463bd83fc"></a>

```c
#define MIPI_DBI_MODE_RGB888_2 (0x7 << 4U)
```

相关声明：[MIPI_DBI_MODE_RGB888_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga0edb36a8b62a252bff686f0463bd83fc)。

RGB888，每像素 24 位（24 bpp）。


## 8.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P191_mipi_dbi.h_源码浏览.md)
- [MIPI_DBI_MODE_SPI_3WIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga9aeeeef78898e1d649f96feccae2fcac)
- [MIPI_DBI_MODE_SPI_4WIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga5c27ef3aa3256e60495a7c511cbaf7a5)
- [MIPI_DBI_TE_NO_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad73dfe18498d59ed4bc2a9f15306d695)
- [MIPI_DBI_TE_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa83bb6eb37251b1a5b4cd8b60b076d17)
- [MIPI_DBI_TE_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad1ebe36d7048bca248d3a03b63e1e9c7)
- [MIPI_DBI_SPI_XFR_8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga900ba99dbfe81a0856a008809e9f1273)
- [MIPI_DBI_SPI_XFR_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga55bd42d5252cedb919cc0b0bd1d6cdf7)
- [MIPI_DBI_MODE_6800_BUS_16_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga4e59f3d57007cea38ae04aac74c2b5dc)
- [MIPI_DBI_MODE_6800_BUS_9_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa89b584bc5bf5a153926ba808de49131)
- [MIPI_DBI_MODE_6800_BUS_8_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab9b80bb367e7bd084ae490bbff9034b9)
- [MIPI_DBI_MODE_8080_BUS_16_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga3c3d1c379c4bc07847412b3bd5b76cb1)
- [MIPI_DBI_MODE_8080_BUS_9_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad4c61d48021f38c0759daf9a401f24c7)
- [MIPI_DBI_MODE_8080_BUS_8_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga3d26bb4556822d12567c62c7ff2c3bb9)
- [MIPI_DBI_MODE_RGB332](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga11d68e3a9a449ec8fce4bbae637af08c)
- [MIPI_DBI_MODE_RGB444](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gac18f3926b86551908300f055ebe9212a)
- [MIPI_DBI_MODE_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga53bbca5860b8845e892d3605c44877b4)
- [MIPI_DBI_MODE_RGB666_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa264bb127fbbece867bf444c8168b6f4)
- [MIPI_DBI_MODE_RGB666_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafb1d7ae963a9cfedadaa4c4299ad7f99)
- [MIPI_DBI_MODE_RGB888_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad7195e4b6aad08002b4b61a3052bf8e7)
- [MIPI_DBI_MODE_RGB888_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga0edb36a8b62a252bff686f0463bd83fc)

---

[上一章](P007_zephyr__drivers__mipi_dsi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__misc__ft8xx__ft8xx_dl.h_文件参考.md)
