---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-23
title: zephyr__dt-bindings__pinctrl__renesas__pinctrl-rx-pfs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_renesas\_\_pinctrl-rx-pfs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX引脚功能选择器（Pin Function Selector）的设备树绑定。

查看此文件的源码。

<a id="details"></a>

瑞萨 RX 引脚功能选择器设备树绑定（Renesas RX Pin Function Selector Devicetree Bindings）。本头文件为设备树源文件提供 Renesas RX 系列微控制器的引脚控制定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.1\_宏定义（Macros）

<a id="r_a33c8631dc344fa69c4e14e4cb43b490b"></a>

```c
#define RX_PORT_NUM_POS 0
```

相关声明：[RX_PORT_NUM_POS](#a33c8631dc344fa69c4e14e4cb43b490b)。

端口编号位位置（Port Number Bit Position）。

<a id="r_af32dac5bcf375bbcf33375877f6e49e3"></a>

```c
#define RX_PORT_NUM_MASK 0xf
```

相关声明：[RX_PORT_NUM_MASK](#af32dac5bcf375bbcf33375877f6e49e3)。

端口编号掩码（Port Number Mask）。

<a id="r_a8d620aa7e9514a75e3affc1ef8e950c9"></a>

```c
#define RX_PIN_NUM_POS 5
```

相关声明：[RX_PIN_NUM_POS](#a8d620aa7e9514a75e3affc1ef8e950c9)。

引脚编号位位置（Pin Number Bit Position）。

<a id="r_a5b11958c204ab0c6008ba32445d3c5b1"></a>

```c
#define RX_PIN_NUM_MASK 0xf
```

相关声明：[RX_PIN_NUM_MASK](#a5b11958c204ab0c6008ba32445d3c5b1)。

引脚编号掩码（Pin Number Mask）。

<a id="r_a9f028cbb20ee3e67568bd0d6608c07f9"></a>

```c
#define RX_PSEL_HIZ_JTAG_SWD 0x0
```

相关声明：[RX_PSEL_HIZ_JTAG_SWD](#a9f028cbb20ee3e67568bd0d6608c07f9)。

引脚功能选择器（Pin Function Selector）：高阻态（High Impedance）、JTAG/SWD。

<a id="r_acf5bb1af41634141f290b5e20d93afcc"></a>

```c
#define RX_PSEL_SCI_0 0xA
```

相关声明：[RX_PSEL_SCI_0](#acf5bb1af41634141f290b5e20d93afcc)。

引脚功能选择器（Pin Function Selector）：SCI 通道 0。

<a id="r_a38e670f045b13291e3fc6a23bb2aa9ee"></a>

```c
#define RX_PSEL_SCI_2 0xA
```

相关声明：[RX_PSEL_SCI_2](#a38e670f045b13291e3fc6a23bb2aa9ee)。

引脚功能选择器（Pin Function Selector）：SCI 通道 2。

<a id="r_a3a253315670fff9e86cf32f04883e621"></a>

```c
#define RX_PSEL_SCI_4 0xA
```

相关声明：[RX_PSEL_SCI_4](#a3a253315670fff9e86cf32f04883e621)。

引脚功能选择器（Pin Function Selector）：SCI 通道 4。

<a id="r_a5275129885c5edd8dfff443723a59022"></a>

```c
#define RX_PSEL_SCI_6 0xA
```

相关声明：[RX_PSEL_SCI_6](#a5275129885c5edd8dfff443723a59022)。

引脚功能选择器（Pin Function Selector）：SCI 通道 6。

<a id="r_a5e520286014c3b76e08ac50f4a924cb5"></a>

```c
#define RX_PSEL_SCI_8 0xA
```

相关声明：[RX_PSEL_SCI_8](#a5e520286014c3b76e08ac50f4a924cb5)。

引脚功能选择器（Pin Function Selector）：SCI 通道 8。

<a id="r_a8c433581d8fef984446ce90e715ee8e4"></a>

```c
#define RX_PSEL_SCI_10 0xA
```

相关声明：[RX_PSEL_SCI_10](#a8c433581d8fef984446ce90e715ee8e4)。

引脚功能选择器（Pin Function Selector）：SCI 通道 10。

<a id="r_aa119430e2fae726e7659560c32ee5fff"></a>

```c
#define RX_PSEL_SCI_12 0xA
```

相关声明：[RX_PSEL_SCI_12](#aa119430e2fae726e7659560c32ee5fff)。

引脚功能选择器（Pin Function Selector）：SCI 通道 12。

<a id="r_a0fd7aa971c81e73658b9ad99408ff61f"></a>

```c
#define RX_PSEL_SCI_1 0xD
```

相关声明：[RX_PSEL_SCI_1](#a0fd7aa971c81e73658b9ad99408ff61f)。

引脚功能选择器（Pin Function Selector）：SCI 通道 1。

<a id="r_a2eeec0d98516be4a6b0d65c756751040"></a>

```c
#define RX_PSEL_SCI_3 0xD
```

相关声明：[RX_PSEL_SCI_3](#a2eeec0d98516be4a6b0d65c756751040)。

引脚功能选择器（Pin Function Selector）：SCI 通道 3。

<a id="r_a5c4529ffae4e274de987b1f7e9dff93f"></a>

```c
#define RX_PSEL_SCI_5 0xD
```

相关声明：[RX_PSEL_SCI_5](#a5c4529ffae4e274de987b1f7e9dff93f)。

引脚功能选择器（Pin Function Selector）：SCI 通道 5。

<a id="r_ae44e1f5eadf852d905658a53a6469856"></a>

```c
#define RX_PSEL_SCI_7 0xD
```

相关声明：[RX_PSEL_SCI_7](#ae44e1f5eadf852d905658a53a6469856)。

引脚功能选择器（Pin Function Selector）：SCI 通道 7。

<a id="r_a988babe92287550d8407e312be45c969"></a>

```c
#define RX_PSEL_SCI_9 0xD
```

相关声明：[RX_PSEL_SCI_9](#a988babe92287550d8407e312be45c969)。

引脚功能选择器（Pin Function Selector）：SCI 通道 9。

<a id="r_a2fb7f1340aadbd0e4075d75b6f13afdc"></a>

```c
#define RX_PSEL_SCI_11 0xD
```

相关声明：[RX_PSEL_SCI_11](#a2fb7f1340aadbd0e4075d75b6f13afdc)。

引脚功能选择器（Pin Function Selector）：SCI 通道 11。

<a id="r_a58e6ba874d0ff5290cae17d3a6f11905"></a>

```c
#define RX_PSEL_POS 9
```

相关声明：[RX_PSEL_POS](#a58e6ba874d0ff5290cae17d3a6f11905)。

引脚功能选择器位位置（Pin Function Selector Bit Position）。

<a id="r_af0ee9eb8939cfd4e527a66c3d0f58f32"></a>

```c
#define RX_PSEL_MASK 0x1f
```

相关声明：[RX_PSEL_MASK](#af0ee9eb8939cfd4e527a66c3d0f58f32)。

引脚功能选择器掩码（Pin Function Selector Mask）。

<a id="r_ab999ef2eb7e81834e49ca2ac94599a74"></a>

```c
#define RX_MODE_POS 16
```

相关声明：[RX_MODE_POS](#ab999ef2eb7e81834e49ca2ac94599a74)。

模式位位置（Mode Bit Position）。

<a id="r_ae5abfee90a4ca5afe9d38f7123abb25c"></a>

```c
#define RX_MODE_MASK 0x1
```

相关声明：[RX_MODE_MASK](#ae5abfee90a4ca5afe9d38f7123abb25c)。

模式掩码（Mode Mask）。

<a id="r_ab1a754c6466137c60093291517676f24"></a>

```c
#define RX_PSEL(psel, port_num, pin_num)
```

相关声明：[RX_PSEL](#ab1a754c6466137c60093291517676f24)。

创建引脚功能选择器配置值（Pin Function Selector Configuration Value）。

## 23.2\_详细说明（Detailed Documentation）

<a id="ae5abfee90a4ca5afe9d38f7123abb25c"></a>

### `RX_MODE_MASK`

```c
#define RX_MODE_MASK 0x1
```

模式掩码（Mode Mask）。

<a id="ab999ef2eb7e81834e49ca2ac94599a74"></a>

### `RX_MODE_POS`

```c
#define RX_MODE_POS 16
```

模式位位置（Mode Bit Position）。

<a id="a5b11958c204ab0c6008ba32445d3c5b1"></a>

### `RX_PIN_NUM_MASK`

```c
#define RX_PIN_NUM_MASK 0xf
```

引脚编号掩码（Pin Number Mask）。

<a id="a8d620aa7e9514a75e3affc1ef8e950c9"></a>

### `RX_PIN_NUM_POS`

```c
#define RX_PIN_NUM_POS 5
```

引脚编号位位置（Pin Number Bit Position）。

<a id="af32dac5bcf375bbcf33375877f6e49e3"></a>

### `RX_PORT_NUM_MASK`

```c
#define RX_PORT_NUM_MASK 0xf
```

端口编号掩码（Port Number Mask）。

<a id="a33c8631dc344fa69c4e14e4cb43b490b"></a>

### `RX_PORT_NUM_POS`

```c
#define RX_PORT_NUM_POS 0
```

端口编号位位置（Port Number Bit Position）。

<a id="ab1a754c6466137c60093291517676f24"></a>

### `RX_PSEL`

```c
#define RX_PSEL ( psel, port_num, pin_num )
```

展开值（Value）：

```c
(1 << RX_MODE_POS | psel << RX_PSEL_POS | port_num << RX_PORT_NUM_POS |                    \
 pin_num << RX_PIN_NUM_POS)
```

创建引脚功能选择器配置值（Pin Function Selector Configuration Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `psel` | 引脚功能选择器值（Pin Function Selector Value） |
| `port_num` | 端口号（Port number）。 |
| `pin_num` | 引脚编号。 |

**返回（Returns）**：返回值（Returns）：配置后的引脚控制值（Pin Control Value）。

<a id="a9f028cbb20ee3e67568bd0d6608c07f9"></a>

### `RX_PSEL_HIZ_JTAG_SWD`

```c
#define RX_PSEL_HIZ_JTAG_SWD 0x0
```

引脚功能选择器（Pin Function Selector）：高阻态（High Impedance）、JTAG/SWD。

<a id="af0ee9eb8939cfd4e527a66c3d0f58f32"></a>

### `RX_PSEL_MASK`

```c
#define RX_PSEL_MASK 0x1f
```

引脚功能选择器掩码（Pin Function Selector Mask）。

<a id="a58e6ba874d0ff5290cae17d3a6f11905"></a>

### `RX_PSEL_POS`

```c
#define RX_PSEL_POS 9
```

引脚功能选择器位位置（Pin Function Selector Bit Position）。

<a id="acf5bb1af41634141f290b5e20d93afcc"></a>

### `RX_PSEL_SCI_0`

```c
#define RX_PSEL_SCI_0 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 0。

<a id="a0fd7aa971c81e73658b9ad99408ff61f"></a>

### `RX_PSEL_SCI_1`

```c
#define RX_PSEL_SCI_1 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 1。

<a id="a8c433581d8fef984446ce90e715ee8e4"></a>

### `RX_PSEL_SCI_10`

```c
#define RX_PSEL_SCI_10 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 10。

<a id="a2fb7f1340aadbd0e4075d75b6f13afdc"></a>

### `RX_PSEL_SCI_11`

```c
#define RX_PSEL_SCI_11 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 11。

<a id="aa119430e2fae726e7659560c32ee5fff"></a>

### `RX_PSEL_SCI_12`

```c
#define RX_PSEL_SCI_12 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 12。

<a id="a38e670f045b13291e3fc6a23bb2aa9ee"></a>

### `RX_PSEL_SCI_2`

```c
#define RX_PSEL_SCI_2 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 2。

<a id="a2eeec0d98516be4a6b0d65c756751040"></a>

### `RX_PSEL_SCI_3`

```c
#define RX_PSEL_SCI_3 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 3。

<a id="a3a253315670fff9e86cf32f04883e621"></a>

### `RX_PSEL_SCI_4`

```c
#define RX_PSEL_SCI_4 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 4。

<a id="a5c4529ffae4e274de987b1f7e9dff93f"></a>

### `RX_PSEL_SCI_5`

```c
#define RX_PSEL_SCI_5 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 5。

<a id="a5275129885c5edd8dfff443723a59022"></a>

### `RX_PSEL_SCI_6`

```c
#define RX_PSEL_SCI_6 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 6。

<a id="ae44e1f5eadf852d905658a53a6469856"></a>

### `RX_PSEL_SCI_7`

```c
#define RX_PSEL_SCI_7 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 7。

<a id="a5e520286014c3b76e08ac50f4a924cb5"></a>

### `RX_PSEL_SCI_8`

```c
#define RX_PSEL_SCI_8 0xA
```

引脚功能选择器（Pin Function Selector）：SCI 通道 8。

<a id="a988babe92287550d8407e312be45c969"></a>

### `RX_PSEL_SCI_9`

```c
#define RX_PSEL_SCI_9 0xD
```

引脚功能选择器（Pin Function Selector）：SCI 通道 9。


## 23.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P651_pinctrl-rx-pfs.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="apinctrl-rx-pfs_8h_html_a33c8631dc344fa69c4e14e4cb43b490b"></a>
<a id="apinctrl-rx-pfs_8h_html_a58e6ba874d0ff5290cae17d3a6f11905"></a>
<a id="apinctrl-rx-pfs_8h_html_a8d620aa7e9514a75e3affc1ef8e950c9"></a>
<a id="apinctrl-rx-pfs_8h_html_ab999ef2eb7e81834e49ca2ac94599a74"></a>

---

[上一章](P022_zephyr__dt-bindings__clock-monitor__nxp-fmeas.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__bluetooth__classic__rfcomm.h_文件参考.md)
