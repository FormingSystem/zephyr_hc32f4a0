---
id: learning.zephyr-docs.api-file-display-chat-reference.page-13
title: zephyr__dt-bindings__clock__imx_ccm_rev3.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_clock\_\_imx\_ccm\_rev3.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP i.MX CCM rev3与片上系统无关的时钟说明符编码（Clock-Specifier Encoding）。

查看此文件的源码。

<a id="details"></a>

NXP i.MX CCM rev3 与 SoC 无关的时钟说明符编码（Clock-specifier Encoding）。近期 i.MX RT 系列采用的 i.MX CCM 将外设时钟建模为两个独立部分：门控（Gate，LPCG）负责开启和关闭外设的总线时钟及功能时钟；时钟根（Clock Root）的复用器（Mux）与分频器（Divider）设置决定外设实际获得的频率。这两个标识符空间之间不存在可通过算法推导的关系，因此两者都必须传给时钟驱动。共享的 NXP 外设驱动读取单个时钟单元（Clock Cell）——DT_INST_CLOCKS_CELL(n, name)——并将这一个值同样传给 clock_control_on()、clock_control_get_rate() 和 clock_control_configure()，因此它们无法看到第二个设备树单元。于是，将两个标识符打包到同一个单元中：

```dts
clocks = <&ccm IMX_CCM_CLK(<gate-id>, <root-id>)>;
```

将两个标识符打包到一个单元，也是 nxp,imx-ccm-rev2 已采用的外设编号与实例编号编码方式。对于没有独立门控的外设，使用 IMX_CCM_GATE_NONE；对于没有专用时钟根的外设，使用 IMX_CCM_ROOT_NONE，查询这类外设的频率会得到 -ENOTSUP，而不会返回虚构的数值。标识符的具体值与 SoC 相关，并生成在 hal_nxp 模块内、所依据的 fsl_clock.h 旁边，例如 `<nxp/imxrt/imxrt266x/clock/imx_ccm_rev3_rt266x.h>`。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_acc1ac3d3ea89595b8e3abda5d5223a40"></a>

```c
#define IMX_CCM_ID_BITS 16U
```

相关声明：[IMX_CCM_ID_BITS](#acc1ac3d3ea89595b8e3abda5d5223a40)。

各标识符字段的宽度（Identifier Field Width），单位为位。

<a id="r_a6e5b91ee452e9492806a43c608bebedc"></a>

```c
#define IMX_CCM_ID_MASK 0xFFFFU
```

相关声明：[IMX_CCM_ID_MASK](#a6e5b91ee452e9492806a43c608bebedc)。

单个标识符字段的掩码（Identifier Field Mask）。

<a id="r_a55f9a0d4c0133f03be98fe6b90d47c3a"></a>

```c
#define IMX_CCM_GATE_SHIFT 0U
```

相关声明：[IMX_CCM_GATE_SHIFT](#a55f9a0d4c0133f03be98fe6b90d47c3a)。

门控标识符（Gate Identifier）在时钟说明符中的位位置。

<a id="r_accdfe9dfe7a381b7f7482d21cefe52c8"></a>

```c
#define IMX_CCM_ROOT_SHIFT 16U
```

相关声明：[IMX_CCM_ROOT_SHIFT](#accdfe9dfe7a381b7f7482d21cefe52c8)。

时钟根标识符（Clock-root Identifier）在时钟说明符中的位位置。

<a id="r_a833bfe5a7b6d66e0f79794333c57456f"></a>

```c
#define IMX_CCM_GATE_NONE IMX_CCM_ID_MASK
```

相关声明：[IMX_CCM_GATE_NONE](#a833bfe5a7b6d66e0f79794333c57456f)、[IMX_CCM_ID_MASK](#a6e5b91ee452e9492806a43c608bebedc)。

此外设没有独立的时钟门控（Clock Gate）。

<a id="r_a9ec92eb8207b144989c7c7fbbb50fdb9"></a>

```c
#define IMX_CCM_ROOT_NONE IMX_CCM_ID_MASK
```

相关声明：[IMX_CCM_ROOT_NONE](#a9ec92eb8207b144989c7c7fbbb50fdb9)、[IMX_CCM_ID_MASK](#a6e5b91ee452e9492806a43c608bebedc)。

此外设没有专用时钟根（Clock Root），因此频率未知。

<a id="r_ad22822596b59164d0a0a7d4cdec659a0"></a>

```c
#define IMX_CCM_CLK(gate, root)
```

相关声明：[IMX_CCM_CLK](#ad22822596b59164d0a0a7d4cdec659a0)。

通过门控（Gate）和时钟根（Clock Root）组合出外设时钟说明符（Clock Specifier）。

<a id="r_a633b4546a93de8fca8ef41596425d266"></a>

```c
#define IMX_CCM_CLK_GATE(spec)
```

相关声明：[IMX_CCM_CLK_GATE](#a633b4546a93de8fca8ef41596425d266)。

从时钟说明符中提取门控标识符（Gate Identifier）。

<a id="r_a26b71088eb299c516462d11f35e04f6f"></a>

```c
#define IMX_CCM_CLK_ROOT(spec)
```

相关声明：[IMX_CCM_CLK_ROOT](#a26b71088eb299c516462d11f35e04f6f)。

从时钟说明符中提取时钟根标识符（Clock-root Identifier）。

<a id="define-members-0"></a>

### 设备专用时钟根配置单元（Per-device Clock-root Configuration Cell）

如果外设希望自行控制其时钟根（Clock Root）的复用器／分频器设置，而不沿用 SoC 时钟初始化配置的固定时钟根，就需要在 clocks 属性中添加第二项，并在 clock-names 中将它命名为 "source"。这遵循 Zephyr 现有时钟绑定惯例：在门控（Gate）条目之外，另设第二个用于时钟源选择（Source-select）的 clocks 条目，即 `clocks = <&ctlr GATE>, <&ctlr SRC SEL>;`。

该条目是一个打包的 IMX_CCM_ROOT_CFG 单元（Cell）。IP 驱动读取它，并按值原样将其作为 clock_control_configure() 的 subsystem 参数传入，data 为 NULL；rev3 控制器解包该值并发出一次 CLOCK_SetRootClock 调用。

必须能够将该单元与旧式 IMX_CCM_CLK 门控单元（Gate Cell）区分开，因为共享驱动也会将门控单元传给 clock_control_configure()，这是原有允许的调用方式。门控单元用两个 16 位标识符填满全部 32 位，其最高半字节（Top Nibble）是时钟根标识符的高半字节：所有实际时钟根（最大标识符为 217）在这里均为 0，仅 IMX_CCM_ROOT_NONE 为 0xF。根配置单元（Root-config Cell）使用低 28 位存放各字段，并在最高半字节写入固定的 0xA 标签，这是门控单元永远不会产生的值。因此，IMX_CCM_ROOT_CFG_IS() 能依据编码结构区分这两类单元。

字段宽度（Field Widths）：root 为 8 位（最大标识符 217），mux 为 4 位（最大值 3），div 为 8 位，snd_div 为 8 位，总计 28 位，已验证足以覆盖全部 RT2660 外设时钟根。分频值（Divider Value）不能为 0：HAL 写入的是 value - 1，因此 0 会使寄存器字段全为 1，得到最慢的分频输出。不分频的值为 1。

<a id="r_ad761c5b189972a8c4db4e68a0169fa2e"></a>

```c
#define IMX_CCM_ROOT_CFG_ROOT_SHIFT 0U
```

相关声明：[IMX_CCM_ROOT_CFG_ROOT_SHIFT](#ad761c5b189972a8c4db4e68a0169fa2e)。

根标识符（Root ID）在根配置单元（Root-config Cell）中的位位置。

<a id="r_ae3cf67187fdc7e3e443b948124af589b"></a>

```c
#define IMX_CCM_ROOT_CFG_MUX_SHIFT 8U
```

相关声明：[IMX_CCM_ROOT_CFG_MUX_SHIFT](#ae3cf67187fdc7e3e443b948124af589b)。

复用器选择值（Mux Selector）在根配置单元（Root-config Cell）中的位位置。

<a id="r_a704a85d1b4085b1146bb81c61fecf2f9"></a>

```c
#define IMX_CCM_ROOT_CFG_DIV_SHIFT 12U
```

相关声明：[IMX_CCM_ROOT_CFG_DIV_SHIFT](#a704a85d1b4085b1146bb81c61fecf2f9)。

一级分频值（Primary Divider）在根配置单元（Root-config Cell）中的位位置。

<a id="r_a3fc5ddae6c58480056102f3d3d0505a3"></a>

```c
#define IMX_CCM_ROOT_CFG_SND_DIV_SHIFT 20U
```

相关声明：[IMX_CCM_ROOT_CFG_SND_DIV_SHIFT](#a3fc5ddae6c58480056102f3d3d0505a3)。

二级分频值（Secondary Divider）在根配置单元（Root-config Cell）中的位位置。

<a id="r_ad26802407ca9d211b55e6d3cd1f8cd7c"></a>

```c
#define IMX_CCM_ROOT_CFG_TAG_SHIFT 28U
```

相关声明：[IMX_CCM_ROOT_CFG_TAG_SHIFT](#ad26802407ca9d211b55e6d3cd1f8cd7c)。

区分标签（Discriminator Tag）在根配置单元（Root-config Cell）中的位位置。

<a id="r_a3f3699beaa65b97d9abe1170186af25d"></a>

```c
#define IMX_CCM_ROOT_CFG_ROOT_MASK 0xFFU
```

相关声明：[IMX_CCM_ROOT_CFG_ROOT_MASK](#a3f3699beaa65b97d9abe1170186af25d)。

字段掩码（Field Masks），尚未移位。

<a id="r_a35be464f13936b44ed09c1517cd94e3c"></a>

```c
#define IMX_CCM_ROOT_CFG_MUX_MASK 0xFU
```

相关声明：[IMX_CCM_ROOT_CFG_MUX_MASK](#a35be464f13936b44ed09c1517cd94e3c)。

<a id="r_a13572921fd191208b5a69a5a45116365"></a>

```c
#define IMX_CCM_ROOT_CFG_DIV_MASK 0xFFU
```

相关声明：[IMX_CCM_ROOT_CFG_DIV_MASK](#a13572921fd191208b5a69a5a45116365)。

<a id="r_af7cc465c08df3b9b4ac5f8aa8396bbcf"></a>

```c
#define IMX_CCM_ROOT_CFG_SND_DIV_MASK 0xFFU
```

相关声明：[IMX_CCM_ROOT_CFG_SND_DIV_MASK](#af7cc465c08df3b9b4ac5f8aa8396bbcf)。

<a id="r_adb5580dece3d9235dcc17ae04845dde2"></a>

```c
#define IMX_CCM_ROOT_CFG_TAG_MASK 0xFU
```

相关声明：[IMX_CCM_ROOT_CFG_TAG_MASK](#adb5580dece3d9235dcc17ae04845dde2)。

<a id="r_a13914f3ba65156f77bf52c687fd07ad8"></a>

```c
#define IMX_CCM_ROOT_CFG_TAG 0xAU
```

相关声明：[IMX_CCM_ROOT_CFG_TAG](#a13914f3ba65156f77bf52c687fd07ad8)。

写入最高半字节（Top Nibble）以标记根配置单元（Root-config Cell）的标签值。

<a id="r_a4c6d40008e30fbc9ab2dd8b293b37502"></a>

```c
#define IMX_CCM_ROOT_CFG(root, mux, div, snd_div)
```

相关声明：[IMX_CCM_ROOT_CFG](#a4c6d40008e30fbc9ab2dd8b293b37502)。

构造设备专用的时钟根配置说明符（Clock-root Configuration Specifier）。

<a id="r_a13a96f27234f9d3c0834dee41ef9ba34"></a>

```c
#define IMX_CCM_ROOT_CFG_IS(cell)
```

相关声明：[IMX_CCM_ROOT_CFG_IS](#a13a96f27234f9d3c0834dee41ef9ba34)。

如果单元是根配置单元（Root-config Cell），而非旧式门控单元（Legacy Gate Cell），则为真。

<a id="r_afd8529b62d76ee8f0bcf4ffc0bc720dd"></a>

```c
#define IMX_CCM_ROOT_CFG_ROOT(cell)
```

相关声明：[IMX_CCM_ROOT_CFG_ROOT](#afd8529b62d76ee8f0bcf4ffc0bc720dd)。

从根配置单元中提取根标识符（Root ID）。

<a id="r_a06f8bf2caf61dcd522ed9251022418cf"></a>

```c
#define IMX_CCM_ROOT_CFG_MUX(cell)
```

相关声明：[IMX_CCM_ROOT_CFG_MUX](#a06f8bf2caf61dcd522ed9251022418cf)。

从根配置单元中提取复用器选择值（Mux Selector）。

<a id="r_a3a50fedb0134902dcec78cd42c1ca4b0"></a>

```c
#define IMX_CCM_ROOT_CFG_DIV(cell)
```

相关声明：[IMX_CCM_ROOT_CFG_DIV](#a3a50fedb0134902dcec78cd42c1ca4b0)。

从根配置单元中提取一级分频值（Primary Divider）。

<a id="r_a218ec43f3066d0cbf608ced147583186"></a>

```c
#define IMX_CCM_ROOT_CFG_SND_DIV(cell)
```

相关声明：[IMX_CCM_ROOT_CFG_SND_DIV](#a218ec43f3066d0cbf608ced147583186)。

从根配置单元中提取二级分频值（Secondary Divider）。

## 13.2\_详细说明（Detailed Documentation）

<a id="ad22822596b59164d0a0a7d4cdec659a0"></a>

### `IMX_CCM_CLK`

```c
#define IMX_CCM_CLK ( gate, root )
```

展开值（Value）：

```c
((((root) & IMX_CCM_ID_MASK) << IMX_CCM_ROOT_SHIFT) |                                      \
 (((gate) & IMX_CCM_ID_MASK) << IMX_CCM_GATE_SHIFT))
```

通过门控（Gate）和时钟根（Clock Root）组合出外设时钟说明符（Clock Specifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gate` | 门控（Gate，LPCG）标识符，或 IMX_CCM_GATE_NONE。 |
| `root` | 时钟根标识符（Clock-root Identifier），或 IMX_CCM_ROOT_NONE。 |

<a id="a633b4546a93de8fca8ef41596425d266"></a>

### `IMX_CCM_CLK_GATE`

```c
#define IMX_CCM_CLK_GATE ( spec)
```

展开值（Value）：

```c
(((spec) >> IMX_CCM_GATE_SHIFT) & IMX_CCM_ID_MASK)
```

从时钟说明符中提取门控标识符（Gate Identifier）。

<a id="a26b71088eb299c516462d11f35e04f6f"></a>

### `IMX_CCM_CLK_ROOT`

```c
#define IMX_CCM_CLK_ROOT ( spec)
```

展开值（Value）：

```c
(((spec) >> IMX_CCM_ROOT_SHIFT) & IMX_CCM_ID_MASK)
```

从时钟说明符中提取时钟根标识符（Clock-root Identifier）。

<a id="a833bfe5a7b6d66e0f79794333c57456f"></a>

### `IMX_CCM_GATE_NONE`

```c
#define IMX_CCM_GATE_NONE IMX_CCM_ID_MASK
```

此外设没有独立的时钟门控（Clock Gate）。

<a id="a55f9a0d4c0133f03be98fe6b90d47c3a"></a>

### `IMX_CCM_GATE_SHIFT`

```c
#define IMX_CCM_GATE_SHIFT 0U
```

门控标识符（Gate Identifier）在时钟说明符中的位位置。

<a id="acc1ac3d3ea89595b8e3abda5d5223a40"></a>

### `IMX_CCM_ID_BITS`

```c
#define IMX_CCM_ID_BITS 16U
```

各标识符字段的宽度（Identifier Field Width），单位为位。

<a id="a6e5b91ee452e9492806a43c608bebedc"></a>

### `IMX_CCM_ID_MASK`

```c
#define IMX_CCM_ID_MASK 0xFFFFU
```

单个标识符字段的掩码（Identifier Field Mask）。

<a id="a4c6d40008e30fbc9ab2dd8b293b37502"></a>

### `IMX_CCM_ROOT_CFG`

```c
#define IMX_CCM_ROOT_CFG ( root, mux, div, snd_div )
```

展开值（Value）：

```c
(((IMX_CCM_ROOT_CFG_TAG) << IMX_CCM_ROOT_CFG_TAG_SHIFT) |                                  \
 (((snd_div) & IMX_CCM_ROOT_CFG_SND_DIV_MASK) << IMX_CCM_ROOT_CFG_SND_DIV_SHIFT) |         \
 (((div) & IMX_CCM_ROOT_CFG_DIV_MASK) << IMX_CCM_ROOT_CFG_DIV_SHIFT) |                     \
 (((mux) & IMX_CCM_ROOT_CFG_MUX_MASK) << IMX_CCM_ROOT_CFG_MUX_SHIFT) |                     \
 (((root) & IMX_CCM_ROOT_CFG_ROOT_MASK) << IMX_CCM_ROOT_CFG_ROOT_SHIFT))
```

构造设备专用的时钟根配置说明符（Clock-root Configuration Specifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `root` | 需要编程配置复用器／分频器的时钟根标识符（Clock-root Identifier）。 |
| `mux` | 根复用器选择值（Root Mux Selector），即选择哪个已在运行的上游源。 |
| `div` | 根一级分频值（Primary Root Divider）：1 表示不分频，0 非法。 |
| `snd_div` | 根二级分频值（Secondary Root Divider）：1 表示不分频，0 非法。 |

<a id="a3a50fedb0134902dcec78cd42c1ca4b0"></a>

### `IMX_CCM_ROOT_CFG_DIV`

```c
#define IMX_CCM_ROOT_CFG_DIV ( cell)
```

展开值（Value）：

```c
(((cell) >> IMX_CCM_ROOT_CFG_DIV_SHIFT) & IMX_CCM_ROOT_CFG_DIV_MASK)
```

从根配置单元中提取一级分频值（Primary Divider）。

<a id="a13572921fd191208b5a69a5a45116365"></a>

### `IMX_CCM_ROOT_CFG_DIV_MASK`

```c
#define IMX_CCM_ROOT_CFG_DIV_MASK 0xFFU
```

<a id="a704a85d1b4085b1146bb81c61fecf2f9"></a>

### `IMX_CCM_ROOT_CFG_DIV_SHIFT`

```c
#define IMX_CCM_ROOT_CFG_DIV_SHIFT 12U
```

一级分频值（Primary Divider）在根配置单元（Root-config Cell）中的位位置。

<a id="a13a96f27234f9d3c0834dee41ef9ba34"></a>

### `IMX_CCM_ROOT_CFG_IS`

```c
#define IMX_CCM_ROOT_CFG_IS ( cell)
```

展开值（Value）：

```c
((((cell) >> IMX_CCM_ROOT_CFG_TAG_SHIFT) & IMX_CCM_ROOT_CFG_TAG_MASK) ==                   \
 IMX_CCM_ROOT_CFG_TAG)
```

如果单元是根配置单元（Root-config Cell），而非旧式门控单元（Legacy Gate Cell），则为真。

<a id="a06f8bf2caf61dcd522ed9251022418cf"></a>

### `IMX_CCM_ROOT_CFG_MUX`

```c
#define IMX_CCM_ROOT_CFG_MUX ( cell)
```

展开值（Value）：

```c
(((cell) >> IMX_CCM_ROOT_CFG_MUX_SHIFT) & IMX_CCM_ROOT_CFG_MUX_MASK)
```

从根配置单元中提取复用器选择值（Mux Selector）。

<a id="a35be464f13936b44ed09c1517cd94e3c"></a>

### `IMX_CCM_ROOT_CFG_MUX_MASK`

```c
#define IMX_CCM_ROOT_CFG_MUX_MASK 0xFU
```

<a id="ae3cf67187fdc7e3e443b948124af589b"></a>

### `IMX_CCM_ROOT_CFG_MUX_SHIFT`

```c
#define IMX_CCM_ROOT_CFG_MUX_SHIFT 8U
```

复用器选择值（Mux Selector）在根配置单元（Root-config Cell）中的位位置。

<a id="afd8529b62d76ee8f0bcf4ffc0bc720dd"></a>

### `IMX_CCM_ROOT_CFG_ROOT`

```c
#define IMX_CCM_ROOT_CFG_ROOT ( cell)
```

展开值（Value）：

```c
(((cell) >> IMX_CCM_ROOT_CFG_ROOT_SHIFT) & IMX_CCM_ROOT_CFG_ROOT_MASK)
```

从根配置单元中提取根标识符（Root ID）。

<a id="a3f3699beaa65b97d9abe1170186af25d"></a>

### `IMX_CCM_ROOT_CFG_ROOT_MASK`

```c
#define IMX_CCM_ROOT_CFG_ROOT_MASK 0xFFU
```

字段掩码（Field Masks），尚未移位。

<a id="ad761c5b189972a8c4db4e68a0169fa2e"></a>

### `IMX_CCM_ROOT_CFG_ROOT_SHIFT`

```c
#define IMX_CCM_ROOT_CFG_ROOT_SHIFT 0U
```

根标识符（Root ID）在根配置单元（Root-config Cell）中的位位置。

<a id="a218ec43f3066d0cbf608ced147583186"></a>

### `IMX_CCM_ROOT_CFG_SND_DIV`

```c
#define IMX_CCM_ROOT_CFG_SND_DIV ( cell)
```

展开值（Value）：

```c
(((cell) >> IMX_CCM_ROOT_CFG_SND_DIV_SHIFT) & IMX_CCM_ROOT_CFG_SND_DIV_MASK)
```

从根配置单元中提取二级分频值（Secondary Divider）。

<a id="af7cc465c08df3b9b4ac5f8aa8396bbcf"></a>

### `IMX_CCM_ROOT_CFG_SND_DIV_MASK`

```c
#define IMX_CCM_ROOT_CFG_SND_DIV_MASK 0xFFU
```

<a id="a3fc5ddae6c58480056102f3d3d0505a3"></a>

### `IMX_CCM_ROOT_CFG_SND_DIV_SHIFT`

```c
#define IMX_CCM_ROOT_CFG_SND_DIV_SHIFT 20U
```

二级分频值（Secondary Divider）在根配置单元（Root-config Cell）中的位位置。

<a id="a13914f3ba65156f77bf52c687fd07ad8"></a>

### `IMX_CCM_ROOT_CFG_TAG`

```c
#define IMX_CCM_ROOT_CFG_TAG 0xAU
```

写入最高半字节（Top Nibble）以标记根配置单元（Root-config Cell）的标签值。

<a id="adb5580dece3d9235dcc17ae04845dde2"></a>

### `IMX_CCM_ROOT_CFG_TAG_MASK`

```c
#define IMX_CCM_ROOT_CFG_TAG_MASK 0xFU
```

<a id="ad26802407ca9d211b55e6d3cd1f8cd7c"></a>

### `IMX_CCM_ROOT_CFG_TAG_SHIFT`

```c
#define IMX_CCM_ROOT_CFG_TAG_SHIFT 28U
```

区分标签（Discriminator Tag）在根配置单元（Root-config Cell）中的位位置。

<a id="a9ec92eb8207b144989c7c7fbbb50fdb9"></a>

### `IMX_CCM_ROOT_NONE`

```c
#define IMX_CCM_ROOT_NONE IMX_CCM_ID_MASK
```

此外设没有专用时钟根（Clock Root），因此频率未知。

<a id="accdfe9dfe7a381b7f7482d21cefe52c8"></a>

### `IMX_CCM_ROOT_SHIFT`

```c
#define IMX_CCM_ROOT_SHIFT 16U
```

时钟根标识符（Clock-root Identifier）在时钟说明符中的位位置。


## 13.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P355_imx_ccm_rev3.h_源码浏览.md)
- [clock_control_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaf5e4b13798955fcc891c080b9967ab06)
- [DT_INST_CLOCKS_CELL(n, name)](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#gad6a9584690066548b8d61489ad615a45)
- [clock_control_on()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaec69b0989cefad79ffd5c92f060150b9)
- [clock_control_get_rate()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#ga00f6af6d2668c2dfff0640fe176e89ff)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aimx__ccm__rev3_8h_html_a55f9a0d4c0133f03be98fe6b90d47c3a"></a>
<a id="aimx__ccm__rev3_8h_html_a6e5b91ee452e9492806a43c608bebedc"></a>
<a id="aimx__ccm__rev3_8h_html_accdfe9dfe7a381b7f7482d21cefe52c8"></a>
<a id="aimx__ccm__rev3_8h_html_a13572921fd191208b5a69a5a45116365"></a>
<a id="aimx__ccm__rev3_8h_html_a13914f3ba65156f77bf52c687fd07ad8"></a>
<a id="aimx__ccm__rev3_8h_html_a35be464f13936b44ed09c1517cd94e3c"></a>
<a id="aimx__ccm__rev3_8h_html_a3f3699beaa65b97d9abe1170186af25d"></a>
<a id="aimx__ccm__rev3_8h_html_a3fc5ddae6c58480056102f3d3d0505a3"></a>
<a id="aimx__ccm__rev3_8h_html_a704a85d1b4085b1146bb81c61fecf2f9"></a>
<a id="aimx__ccm__rev3_8h_html_ad26802407ca9d211b55e6d3cd1f8cd7c"></a>
<a id="aimx__ccm__rev3_8h_html_ad761c5b189972a8c4db4e68a0169fa2e"></a>
<a id="aimx__ccm__rev3_8h_html_ae3cf67187fdc7e3e443b948124af589b"></a>
<a id="aimx__ccm__rev3_8h_html_af7cc465c08df3b9b4ac5f8aa8396bbcf"></a>
<a id="aimx__ccm__rev3_8h_html_adb5580dece3d9235dcc17ae04845dde2"></a>

---

[上一章](P012_zephyr__net__ieee802154_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__input__input_crsf.h_文件参考.md)
