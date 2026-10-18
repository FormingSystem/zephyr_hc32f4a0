---
id: learning.zephyr-docs.api-file-system-device-reference.page-31
title: zephyr__dt-bindings__pinctrl__nxp-siul2-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_nxp-siul2-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="r_a745f1f0626464975ac3dfd223ac4fcb8"></a>

```c
#define NXP_SIUL2_MSCR_SSS_SHIFT 0U
```

相关声明：[NXP_SIUL2_MSCR_SSS_SHIFT](#a745f1f0626464975ac3dfd223ac4fcb8)。

<a id="r_af095432bb6b277f1c9888bbb1d417db7"></a>

```c
#define NXP_SIUL2_MSCR_SSS_MASK BIT_MASK(3)
```

相关声明：[NXP_SIUL2_MSCR_SSS_MASK](#af095432bb6b277f1c9888bbb1d417db7)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_afa8e493fe699a0d5e64cfac23b1d0d72"></a>

```c
#define NXP_SIUL2_IMCR_SSS_SHIFT 3U
```

相关声明：[NXP_SIUL2_IMCR_SSS_SHIFT](#afa8e493fe699a0d5e64cfac23b1d0d72)。

<a id="r_aeefbbd5e3e5ab906492d72a5ab716c19"></a>

```c
#define NXP_SIUL2_IMCR_SSS_MASK BIT_MASK(4)
```

相关声明：[NXP_SIUL2_IMCR_SSS_MASK](#aeefbbd5e3e5ab906492d72a5ab716c19)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a316d51cda9462e7bda0049b30f853e37"></a>

```c
#define NXP_SIUL2_IMCR_IDX_SHIFT 7U
```

相关声明：[NXP_SIUL2_IMCR_IDX_SHIFT](#a316d51cda9462e7bda0049b30f853e37)。

<a id="r_a2c2a33e5586eaf07dd3764b54f055821"></a>

```c
#define NXP_SIUL2_IMCR_IDX_MASK BIT_MASK(9)
```

相关声明：[NXP_SIUL2_IMCR_IDX_MASK](#a2c2a33e5586eaf07dd3764b54f055821)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a4c8b05a8993805af069bde77a5fc23f4"></a>

```c
#define NXP_SIUL2_MSCR_IDX_SHIFT 16U
```

相关声明：[NXP_SIUL2_MSCR_IDX_SHIFT](#a4c8b05a8993805af069bde77a5fc23f4)。

<a id="r_a93cb0632aba129160b8acfcfe9ab70c3"></a>

```c
#define NXP_SIUL2_MSCR_IDX_MASK BIT_MASK(9)
```

相关声明：[NXP_SIUL2_MSCR_IDX_MASK](#a93cb0632aba129160b8acfcfe9ab70c3)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a239c909d58b0e8f688c0111f7e0913fe"></a>

```c
#define NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT 25U
```

相关声明：[NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT](#a239c909d58b0e8f688c0111f7e0913fe)。

<a id="r_af6831507d4ccc5872a62e7174defcad3"></a>

```c
#define NXP_SIUL2_MSCR_SIUL2_IDX_MASK BIT_MASK(3)
```

相关声明：[NXP_SIUL2_MSCR_SIUL2_IDX_MASK](#af6831507d4ccc5872a62e7174defcad3)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a3dddd8eb69be748526a73ac5525329f3"></a>

```c
#define NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT 28U
```

相关声明：[NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT](#a3dddd8eb69be748526a73ac5525329f3)。

<a id="r_a42c0ca664d1a31f74f1bd13e7709192b"></a>

```c
#define NXP_SIUL2_IMCR_SIUL2_IDX_MASK BIT_MASK(3)
```

相关声明：[NXP_SIUL2_IMCR_SIUL2_IDX_MASK](#a42c0ca664d1a31f74f1bd13e7709192b)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a6863890f8fc8c0137ecfa1fd13612be8"></a>

```c
#define NXP_SIUL2_PINMUX_MSCR_SSS(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_MSCR_SSS](#a6863890f8fc8c0137ecfa1fd13612be8)。

<a id="r_a1e5eca64c385376038ba7c1e39bcc742"></a>

```c
#define NXP_SIUL2_PINMUX_IMCR_SSS(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_IMCR_SSS](#a1e5eca64c385376038ba7c1e39bcc742)。

<a id="r_a3029b55eec45043889d081b9cabb2ee9"></a>

```c
#define NXP_SIUL2_PINMUX_IMCR_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_IMCR_IDX](#a3029b55eec45043889d081b9cabb2ee9)。

<a id="r_a848b07d7b369606f3152c3eca72093aa"></a>

```c
#define NXP_SIUL2_PINMUX_MSCR_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_MSCR_IDX](#a848b07d7b369606f3152c3eca72093aa)。

<a id="r_aa577d3c3330b31a52c5d54bd09207b3e"></a>

```c
#define NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX](#aa577d3c3330b31a52c5d54bd09207b3e)。

<a id="r_a943e1ac9c1150e6214c413275282ff15"></a>

```c
#define NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX](#a943e1ac9c1150e6214c413275282ff15)。

<a id="r_a16e9ed31915244fbec867833ab9f2318"></a>

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_SSS(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_MSCR_SSS](#a16e9ed31915244fbec867833ab9f2318)。

<a id="r_a33cb58d26acc34048d4d929276ea1fe7"></a>

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_SSS(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_IMCR_SSS](#a33cb58d26acc34048d4d929276ea1fe7)。

<a id="r_adff0c48a90ec439f51cd5d75d5848cf6"></a>

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_IMCR_IDX](#adff0c48a90ec439f51cd5d75d5848cf6)。

<a id="r_a8878e7774bb91df3317094d881f3ff6f"></a>

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_MSCR_IDX](#a8878e7774bb91df3317094d881f3ff6f)。

<a id="r_a340f3ad31a281a7a1cdf9490ef8777b5"></a>

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_SIUL2_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_MSCR_SIUL2_IDX](#a340f3ad31a281a7a1cdf9490ef8777b5)。

<a id="r_af688d718cffd86b8c52af7517c786782"></a>

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_SIUL2_IDX(cfg)
```

相关声明：[NXP_SIUL2_PINMUX_GET_IMCR_SIUL2_IDX](#af688d718cffd86b8c52af7517c786782)。

<a id="r_a1868bbbebae4daf3d1a1df7c34eef660"></a>

```c
#define NXP_SIUL2_PINMUX(mscr_siul2_idx, imcr_siul2_idx, mscr_idx, mscr_sss, imcr_idx, imcr_sss)
```

相关声明：[NXP_SIUL2_PINMUX](#a1868bbbebae4daf3d1a1df7c34eef660)。

用于为引脚控制（pinctrl）节点构造 NXP S32 `pinmux` 属性的工具宏。

## 31.2\_详细说明（Detailed Documentation）

<a id="a2c2a33e5586eaf07dd3764b54f055821"></a>

### `NXP_SIUL2_IMCR_IDX_MASK`

```c
#define NXP_SIUL2_IMCR_IDX_MASK BIT_MASK(9)
```

<a id="a316d51cda9462e7bda0049b30f853e37"></a>

### `NXP_SIUL2_IMCR_IDX_SHIFT`

```c
#define NXP_SIUL2_IMCR_IDX_SHIFT 7U
```

<a id="a42c0ca664d1a31f74f1bd13e7709192b"></a>

### `NXP_SIUL2_IMCR_SIUL2_IDX_MASK`

```c
#define NXP_SIUL2_IMCR_SIUL2_IDX_MASK BIT_MASK(3)
```

<a id="a3dddd8eb69be748526a73ac5525329f3"></a>

### `NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT`

```c
#define NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT 28U
```

<a id="aeefbbd5e3e5ab906492d72a5ab716c19"></a>

### `NXP_SIUL2_IMCR_SSS_MASK`

```c
#define NXP_SIUL2_IMCR_SSS_MASK BIT_MASK(4)
```

<a id="afa8e493fe699a0d5e64cfac23b1d0d72"></a>

### `NXP_SIUL2_IMCR_SSS_SHIFT`

```c
#define NXP_SIUL2_IMCR_SSS_SHIFT 3U
```

<a id="a93cb0632aba129160b8acfcfe9ab70c3"></a>

### `NXP_SIUL2_MSCR_IDX_MASK`

```c
#define NXP_SIUL2_MSCR_IDX_MASK BIT_MASK(9)
```

<a id="a4c8b05a8993805af069bde77a5fc23f4"></a>

### `NXP_SIUL2_MSCR_IDX_SHIFT`

```c
#define NXP_SIUL2_MSCR_IDX_SHIFT 16U
```

<a id="af6831507d4ccc5872a62e7174defcad3"></a>

### `NXP_SIUL2_MSCR_SIUL2_IDX_MASK`

```c
#define NXP_SIUL2_MSCR_SIUL2_IDX_MASK BIT_MASK(3)
```

<a id="a239c909d58b0e8f688c0111f7e0913fe"></a>

### `NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT`

```c
#define NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT 25U
```

<a id="af095432bb6b277f1c9888bbb1d417db7"></a>

### `NXP_SIUL2_MSCR_SSS_MASK`

```c
#define NXP_SIUL2_MSCR_SSS_MASK BIT_MASK(3)
```

<a id="a745f1f0626464975ac3dfd223ac4fcb8"></a>

### `NXP_SIUL2_MSCR_SSS_SHIFT`

```c
#define NXP_SIUL2_MSCR_SSS_SHIFT 0U
```

<a id="a1868bbbebae4daf3d1a1df7c34eef660"></a>

### `NXP_SIUL2_PINMUX`

```c
#define NXP_SIUL2_PINMUX ( mscr_siul2_idx, imcr_siul2_idx, mscr_idx, mscr_sss, imcr_idx, imcr_sss )
```

展开值（Value）：

```c
(NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX(mscr_siul2_idx) |                                         \
 NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX(imcr_siul2_idx) |                                         \
 NXP_SIUL2_PINMUX_MSCR_IDX(mscr_idx) |                                                     \
 NXP_SIUL2_PINMUX_MSCR_SSS(mscr_sss) |                                                     \
 NXP_SIUL2_PINMUX_IMCR_IDX(imcr_idx) |                                                     \
 NXP_SIUL2_PINMUX_IMCR_SSS(imcr_sss))
```

用于为引脚控制（pinctrl）节点构造 NXP S32 `pinmux` 属性的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mscr_siul2_idx` | MSCR 所属 SIUL2 实例索引。 |
| `imcr_siul2_idx` | IMCR 所属 SIUL2 实例索引。 |
| `mscr_idx` | 多路复用信号配置寄存器（Multiplexed Signal Configuration Register，MSCR）索引。 |
| `mscr_sss` | 输出复用的源信号选择（Source Signal Selection），即 `MSCR.SSS`。 |
| `imcr_idx` | 输入多路复用信号配置寄存器（Input Multiplexed Signal Configuration Register，IMCR）索引。 |
| `imcr_sss` | 输入复用的源信号选择（Source Signal Selection），即 `IMCR.SSS`。 |

<a id="adff0c48a90ec439f51cd5d75d5848cf6"></a>

### `NXP_SIUL2_PINMUX_GET_IMCR_IDX`

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_IMCR_IDX_SHIFT) & NXP_SIUL2_IMCR_IDX_MASK)
```

<a id="af688d718cffd86b8c52af7517c786782"></a>

### `NXP_SIUL2_PINMUX_GET_IMCR_SIUL2_IDX`

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_SIUL2_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT) & NXP_SIUL2_IMCR_SIUL2_IDX_MASK)
```

<a id="a33cb58d26acc34048d4d929276ea1fe7"></a>

### `NXP_SIUL2_PINMUX_GET_IMCR_SSS`

```c
#define NXP_SIUL2_PINMUX_GET_IMCR_SSS ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_IMCR_SSS_SHIFT) & NXP_SIUL2_IMCR_SSS_MASK)
```

<a id="a8878e7774bb91df3317094d881f3ff6f"></a>

### `NXP_SIUL2_PINMUX_GET_MSCR_IDX`

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_MSCR_IDX_SHIFT) & NXP_SIUL2_MSCR_IDX_MASK)
```

<a id="a340f3ad31a281a7a1cdf9490ef8777b5"></a>

### `NXP_SIUL2_PINMUX_GET_MSCR_SIUL2_IDX`

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_SIUL2_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT) & NXP_SIUL2_MSCR_SIUL2_IDX_MASK)
```

<a id="a16e9ed31915244fbec867833ab9f2318"></a>

### `NXP_SIUL2_PINMUX_GET_MSCR_SSS`

```c
#define NXP_SIUL2_PINMUX_GET_MSCR_SSS ( cfg)
```

展开值（Value）：

```c
(((cfg) >> NXP_SIUL2_MSCR_SSS_SHIFT) & NXP_SIUL2_MSCR_SSS_MASK)
```

<a id="a3029b55eec45043889d081b9cabb2ee9"></a>

### `NXP_SIUL2_PINMUX_IMCR_IDX`

```c
#define NXP_SIUL2_PINMUX_IMCR_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_IMCR_IDX_MASK) << NXP_SIUL2_IMCR_IDX_SHIFT)
```

<a id="a943e1ac9c1150e6214c413275282ff15"></a>

### `NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX`

```c
#define NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_IMCR_SIUL2_IDX_MASK) << NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT)
```

<a id="a1e5eca64c385376038ba7c1e39bcc742"></a>

### `NXP_SIUL2_PINMUX_IMCR_SSS`

```c
#define NXP_SIUL2_PINMUX_IMCR_SSS ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_IMCR_SSS_MASK) << NXP_SIUL2_IMCR_SSS_SHIFT)
```

<a id="a848b07d7b369606f3152c3eca72093aa"></a>

### `NXP_SIUL2_PINMUX_MSCR_IDX`

```c
#define NXP_SIUL2_PINMUX_MSCR_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_MSCR_IDX_MASK) << NXP_SIUL2_MSCR_IDX_SHIFT)
```

<a id="aa577d3c3330b31a52c5d54bd09207b3e"></a>

### `NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX`

```c
#define NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_MSCR_SIUL2_IDX_MASK) << NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT)
```

<a id="a6863890f8fc8c0137ecfa1fd13612be8"></a>

### `NXP_SIUL2_PINMUX_MSCR_SSS`

```c
#define NXP_SIUL2_PINMUX_MSCR_SSS ( cfg)
```

展开值（Value）：

```c
(((cfg) & NXP_SIUL2_MSCR_SSS_MASK) << NXP_SIUL2_MSCR_SSS_SHIFT)
```


## 31.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P137_nxp-siul2-pinctrl.h_源码浏览.md)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="anxp-siul2-pinctrl_8h_html_aa577d3c3330b31a52c5d54bd09207b3e"></a>
<a id="anxp-siul2-pinctrl_8h_html_a2c2a33e5586eaf07dd3764b54f055821"></a>
<a id="anxp-siul2-pinctrl_8h_html_a316d51cda9462e7bda0049b30f853e37"></a>
<a id="anxp-siul2-pinctrl_8h_html_a3dddd8eb69be748526a73ac5525329f3"></a>
<a id="anxp-siul2-pinctrl_8h_html_a42c0ca664d1a31f74f1bd13e7709192b"></a>
<a id="anxp-siul2-pinctrl_8h_html_aeefbbd5e3e5ab906492d72a5ab716c19"></a>
<a id="anxp-siul2-pinctrl_8h_html_afa8e493fe699a0d5e64cfac23b1d0d72"></a>
<a id="anxp-siul2-pinctrl_8h_html_a4c8b05a8993805af069bde77a5fc23f4"></a>
<a id="anxp-siul2-pinctrl_8h_html_a93cb0632aba129160b8acfcfe9ab70c3"></a>
<a id="anxp-siul2-pinctrl_8h_html_a239c909d58b0e8f688c0111f7e0913fe"></a>
<a id="anxp-siul2-pinctrl_8h_html_af6831507d4ccc5872a62e7174defcad3"></a>
<a id="anxp-siul2-pinctrl_8h_html_a745f1f0626464975ac3dfd223ac4fcb8"></a>
<a id="anxp-siul2-pinctrl_8h_html_af095432bb6b277f1c9888bbb1d417db7"></a>

---

[上一章](P030_zephyr__dt-bindings__pinctrl__numicro-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__drivers__firmware__scmi__nxp__system.h_文件参考.md)
