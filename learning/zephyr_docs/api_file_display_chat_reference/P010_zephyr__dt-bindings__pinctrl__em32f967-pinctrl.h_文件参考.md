---
id: learning.zephyr-docs.api-file-display-chat-reference.page-10
title: zephyr__dt-bindings__pinctrl__em32f967-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_em32f967-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_a27b90d0f9e7f6789f143eb5634bb56c2"></a>

```c
#define EM32F967_GPIO 0 /* 000: GPIO function */
```

相关声明：[EM32F967_GPIO](#a27b90d0f9e7f6789f143eb5634bb56c2)。

GPIO 复用功能选择器（Mux Function Selector），mux 字段值为 0。

<a id="r_a81cb36dc3f02ed12c64172b42d325b15"></a>

```c
#define EM32F967_AF1 1 /* 001: Alternate function 1 (SPI1, etc.) */
```

相关声明：[EM32F967_AF1](#a81cb36dc3f02ed12c64172b42d325b15)。

<a id="r_a5821e6ec4bd3aa762db55a581be4439f"></a>

```c
#define EM32F967_AF2 2 /* 010: Alternate function 2 (UART, etc.) */
```

相关声明：[EM32F967_AF2](#a5821e6ec4bd3aa762db55a581be4439f)。

<a id="r_a79c2ac8fb4e35ba8f13ac4834e1b3fdc"></a>

```c
#define EM32F967_AF3 3 /* 011: Alternate function 3 (Timer, 7816, etc.) */
```

相关声明：[EM32F967_AF3](#a79c2ac8fb4e35ba8f13ac4834e1b3fdc)。

<a id="r_aa67185d03eac868e472bd6e224c7e143"></a>

```c
#define EM32F967_AF4 4 /* 100: Alternate function 4 (I2C, etc.) */
```

相关声明：[EM32F967_AF4](#aa67185d03eac868e472bd6e224c7e143)。

<a id="r_a4453c83819265ff9e9a857ef0853597d"></a>

```c
#define EM32F967_AF5 5 /* 101: Alternate function 5 (I2C, WKUP, etc.) */
```

相关声明：[EM32F967_AF5](#a4453c83819265ff9e9a857ef0853597d)。

<a id="r_a1cf36994c6b1b8bb87aee507be1fb4ee"></a>

```c
#define EM32F967_AF6 6 /* 110: Alternate function 6 (SSP2, etc.) */
```

相关声明：[EM32F967_AF6](#a1cf36994c6b1b8bb87aee507be1fb4ee)。

<a id="r_a11c5466ff1ae7d4ffce3e4b49bd582b0"></a>

```c
#define EM32F967_AF7 7 /* 111: Alternate function 7 (PWM, etc.) */
```

相关声明：[EM32F967_AF7](#a11c5466ff1ae7d4ffce3e4b49bd582b0)。

<a id="r_ab91e901fcce847624af03e49ccfb785e"></a>

```c
#define EM32F967_MUX_SHIFT 0U
```

相关声明：[EM32F967_MUX_SHIFT](#ab91e901fcce847624af03e49ccfb785e)。

引脚配置位字段编码（Pin Configuration Bit Field Encoding），采用 EM32 风格。

<a id="r_add1cca26494694aa34c31e1f3a41e297"></a>

```c
#define EM32F967_MUX_MASK 0x7U
```

相关声明：[EM32F967_MUX_MASK](#add1cca26494694aa34c31e1f3a41e297)。

<a id="r_a415fe4032ba9029ecbb915036558f216"></a>

```c
#define EM32F967_PIN_SHIFT 3U
```

相关声明：[EM32F967_PIN_SHIFT](#a415fe4032ba9029ecbb915036558f216)。

<a id="r_ade0b89bc6283e9fa47fbdb1a63224567"></a>

```c
#define EM32F967_PIN_MASK 0xFU
```

相关声明：[EM32F967_PIN_MASK](#ade0b89bc6283e9fa47fbdb1a63224567)。

<a id="r_a70d272163e70075e409ece520ab3df05"></a>

```c
#define EM32F967_PORT_SHIFT 7U
```

相关声明：[EM32F967_PORT_SHIFT](#a70d272163e70075e409ece520ab3df05)。

<a id="r_a68fdd9bcb324f906cde4e7f2779c20ee"></a>

```c
#define EM32F967_PORT_MASK 0x1U
```

相关声明：[EM32F967_PORT_MASK](#a68fdd9bcb324f906cde4e7f2779c20ee)。

<a id="r_a33870f76f04772632963b4433747b0f5"></a>

```c
#define EM32F967_PINMUX(port, pin, mux)
```

相关声明：[EM32F967_PINMUX](#a33870f76f04772632963b4433747b0f5)。

EM32F967 引脚复用宏（Pin Multiplexing Macro），采用 EM32 风格。

<a id="r_a1099aa5788757f372497468304b19cd9"></a>

```c
#define EM32F967_DT_PINMUX_PORT(pinmux)
```

相关声明：[EM32F967_DT_PINMUX_PORT](#a1099aa5788757f372497468304b19cd9)。

<a id="r_acaa7f0d52ed6636449af43fbbfe76803"></a>

```c
#define EM32F967_DT_PINMUX_PIN(pinmux)
```

相关声明：[EM32F967_DT_PINMUX_PIN](#acaa7f0d52ed6636449af43fbbfe76803)。

<a id="r_a8865bd2bbb701c22f755a237ef7cc7be"></a>

```c
#define EM32F967_DT_PINMUX_MUX(pinmux)
```

相关声明：[EM32F967_DT_PINMUX_MUX](#a8865bd2bbb701c22f755a237ef7cc7be)。

<a id="r_a132c694b104108ee3bdab8493466ccdf"></a>

```c
#define EM32F967_PULL_NONE_5V 0 /* 00: Floating */
```

相关声明：[EM32F967_PULL_NONE_5V](#a132c694b104108ee3bdab8493466ccdf)。

<a id="r_a15e15b874c30415817d74534af9048e2"></a>

```c
#define EM32F967_PULL_UP0_5V 1 /* 01: PU0 (66KΩ@5V, 101KΩ@3.3V, 238KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_UP0_5V](#a15e15b874c30415817d74534af9048e2)。

<a id="r_a31e365dede45b78c88b7adc00229cc79"></a>

```c
#define EM32F967_PULL_UP1_5V 2 /* 10: PU1 (4.7KΩ@5V, 6.41KΩ@3.3V, 12.7KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_UP1_5V](#a31e365dede45b78c88b7adc00229cc79)。

<a id="r_a53bb0ef38ab66505e00bb6fa945c3ee7"></a>

```c
#define EM32F967_PULL_DOWN_5V 3 /* 11: PD (15KΩ@5V, 21.8KΩ@3.3V, 49.6KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_DOWN_5V](#a53bb0ef38ab66505e00bb6fa945c3ee7)。

<a id="r_a254e0b8c5245a97239e9d51216f7e03f"></a>

```c
#define EM32F967_PULL_NONE_3V 0 /* 00: Floating */
```

相关声明：[EM32F967_PULL_NONE_3V](#a254e0b8c5245a97239e9d51216f7e03f)。

<a id="r_a06b93f47492b64939e7e3709aa807be9"></a>

```c
#define EM32F967_PULL_UP0_3V 1 /* 01: PU0 (66KΩ@3.3V, 140KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_UP0_3V](#a06b93f47492b64939e7e3709aa807be9)。

<a id="r_a153386a1e74f1fc572d2761d6b5136f1"></a>

```c
#define EM32F967_PULL_UP1_3V 2 /* 10: PU1 (4.7KΩ@3.3V, 8.53KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_UP1_3V](#a153386a1e74f1fc572d2761d6b5136f1)。

<a id="r_afe8add9c6b17be78f01ced071ab3a0ec"></a>

```c
#define EM32F967_PULL_DOWN_3V 3 /* 11: PD (15KΩ@3.3V, 25.2KΩ@1.8V) */
```

相关声明：[EM32F967_PULL_DOWN_3V](#afe8add9c6b17be78f01ced071ab3a0ec)。

<a id="r_af7bd8d8bed93440ad557e50976840275"></a>

```c
#define EM32F967_DRIVE_NORMAL 0 /* Normal drive strength */
```

相关声明：[EM32F967_DRIVE_NORMAL](#af7bd8d8bed93440ad557e50976840275)。

<a id="r_aaf4836ffb67af34b563f818f3e0577d8"></a>

```c
#define EM32F967_DRIVE_HIGH 1 /* High drive strength (Load=30pF) */
```

相关声明：[EM32F967_DRIVE_HIGH](#aaf4836ffb67af34b563f818f3e0577d8)。

<a id="r_aef613aabc331e2c875bf7f990e363c54"></a>

```c
#define EM32F967_IO_NONE 0U
```

相关声明：[EM32F967_IO_NONE](#aef613aabc331e2c875bf7f990e363c54)。

携带在 pinmux 单元中的嵌入式 IP_SHARE 操作（Embedded IP_SHARE Operations）。

<a id="r_a1c0555f650a6bb6949006801c75be023"></a>

```c
#define EM32F967_IO1(shift, width, val)
```

相关声明：[EM32F967_IO1](#a1c0555f650a6bb6949006801c75be023)。

构造第一个嵌入式 IP_SHARE 操作（槽位 1，Slot 1）。

<a id="r_a34914d50d53d18b9de37407c463c0718"></a>

```c
#define EM32F967_IO2(shift, width, val)
```

相关声明：[EM32F967_IO2](#a34914d50d53d18b9de37407c463c0718)。

构造第二个嵌入式 IP_SHARE 操作（槽位 2，Slot 2）。

<a id="r_a10463a0f449b174af9f9e6338a97ac72"></a>

```c
#define EM32F967_IO_SET_BIT(pos)
```

相关声明：[EM32F967_IO_SET_BIT](#a10463a0f449b174af9f9e6338a97ac72)。

槽位 1 辅助宏（Slot 1 Helper）：设置单个 IP_SHARE 位。

<a id="r_a4b83a385de1ec4737f3c8fd505a2aba4"></a>

```c
#define EM32F967_IO_CLR_BIT(pos)
```

相关声明：[EM32F967_IO_CLR_BIT](#a4b83a385de1ec4737f3c8fd505a2aba4)。

槽位 1 辅助宏（Slot 1 Helper）：清除单个 IP_SHARE 位。

<a id="r_ae3d7d30dc7a11d41db0585fbcf976735"></a>

```c
#define EM32F967_IO_SET_2BIT(pos, val)
```

相关声明：[EM32F967_IO_SET_2BIT](#ae3d7d30dc7a11d41db0585fbcf976735)。

槽位 1 辅助宏（Slot 1 Helper）：写入一个 2 位 IP_SHARE 字段。

<a id="r_afe73c3c740a1b2a0b4904f116a72668f"></a>

```c
#define EM32F967_IO_CLR_2BIT(pos)
```

相关声明：[EM32F967_IO_CLR_2BIT](#afe73c3c740a1b2a0b4904f116a72668f)。

槽位 1 辅助宏（Slot 1 Helper）：清除一个 2 位 IP_SHARE 字段。

<a id="r_a95012f2112abe8d306d598dbb7dc0d71"></a>

```c
#define EM32F967_PINMUX_IO(port, pin, mux, ioshare)
```

相关声明：[EM32F967_PINMUX_IO](#a95012f2112abe8d306d598dbb7dc0d71)。

包含嵌入式 IP_SHARE 操作的 EM32F967 引脚复用宏（Pinmux Macro）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a81cb36dc3f02ed12c64172b42d325b15"></a>

### `EM32F967_AF1`

```c
#define EM32F967_AF1 1 /* 001: Alternate function 1 (SPI1, etc.) */
```

<a id="a5821e6ec4bd3aa762db55a581be4439f"></a>

### `EM32F967_AF2`

```c
#define EM32F967_AF2 2 /* 010: Alternate function 2 (UART, etc.) */
```

<a id="a79c2ac8fb4e35ba8f13ac4834e1b3fdc"></a>

### `EM32F967_AF3`

```c
#define EM32F967_AF3 3 /* 011: Alternate function 3 (Timer, 7816, etc.) */
```

<a id="aa67185d03eac868e472bd6e224c7e143"></a>

### `EM32F967_AF4`

```c
#define EM32F967_AF4 4 /* 100: Alternate function 4 (I2C, etc.) */
```

<a id="a4453c83819265ff9e9a857ef0853597d"></a>

### `EM32F967_AF5`

```c
#define EM32F967_AF5 5 /* 101: Alternate function 5 (I2C, WKUP, etc.) */
```

<a id="a1cf36994c6b1b8bb87aee507be1fb4ee"></a>

### `EM32F967_AF6`

```c
#define EM32F967_AF6 6 /* 110: Alternate function 6 (SSP2, etc.) */
```

<a id="a11c5466ff1ae7d4ffce3e4b49bd582b0"></a>

### `EM32F967_AF7`

```c
#define EM32F967_AF7 7 /* 111: Alternate function 7 (PWM, etc.) */
```

<a id="aaf4836ffb67af34b563f818f3e0577d8"></a>

### `EM32F967_DRIVE_HIGH`

```c
#define EM32F967_DRIVE_HIGH 1 /* High drive strength (Load=30pF) */
```

<a id="af7bd8d8bed93440ad557e50976840275"></a>

### `EM32F967_DRIVE_NORMAL`

```c
#define EM32F967_DRIVE_NORMAL 0 /* Normal drive strength */
```

<a id="a8865bd2bbb701c22f755a237ef7cc7be"></a>

### `EM32F967_DT_PINMUX_MUX`

```c
#define EM32F967_DT_PINMUX_MUX ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> EM32F967_MUX_SHIFT) & EM32F967_MUX_MASK)
```

<a id="acaa7f0d52ed6636449af43fbbfe76803"></a>

### `EM32F967_DT_PINMUX_PIN`

```c
#define EM32F967_DT_PINMUX_PIN ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> EM32F967_PIN_SHIFT) & EM32F967_PIN_MASK)
```

<a id="a1099aa5788757f372497468304b19cd9"></a>

### `EM32F967_DT_PINMUX_PORT`

```c
#define EM32F967_DT_PINMUX_PORT ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> EM32F967_PORT_SHIFT) & EM32F967_PORT_MASK)
```

<a id="a27b90d0f9e7f6789f143eb5634bb56c2"></a>

### `EM32F967_GPIO`

```c
#define EM32F967_GPIO 0 /* 000: GPIO function */
```

GPIO 复用功能选择器（Mux Function Selector），mux 字段值为 0。

作为 EM32F967_PINMUX / EM32F967_PINMUX_IO 的 mux 参数时，为引脚选择普通 GPIO 功能，不使用复用功能（Alternate Function）。

<a id="a1c0555f650a6bb6949006801c75be023"></a>

### `EM32F967_IO1`

```c
#define EM32F967_IO1 ( shift, width, val )
```

展开值（Value）：

```c
((1U << 8) | (((shift) & 0x1FU) << 9) | ((((width) - 1U) & 0x3U) << 14) |                  \
 (((val) & 0xFU) << 16))
```

构造第一个嵌入式 IP_SHARE 操作（槽位 1，Slot 1）。

将单个 IP_SHARE 读改写操作（Read-modify-write Operation）编码到 pinmux 的位 [19:8]，包含有效标志（Valid Flag）、移位量（Shift）、宽度减一（Width-1）和值（Value）。与 EM32F967_IO2 按位或组合可编码第二个操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shift` | 字段在 IP_SHARE 寄存器中的位位置（Bit Position），范围为 0–31。 |
| `width` | 字段宽度（Field Width），单位为位，范围为 1–4。 |
| `val` | 要写入字段的值（Value）。 |

<a id="a34914d50d53d18b9de37407c463c0718"></a>

### `EM32F967_IO2`

```c
#define EM32F967_IO2 ( shift, width, val )
```

展开值（Value）：

```c
((1U << 20) | (((shift) & 0x1FU) << 21) | ((((width) - 1U) & 0x3U) << 26) |                \
 (((val) & 0xFU) << 28))
```

构造第二个嵌入式 IP_SHARE 操作（槽位 2，Slot 2）。

将单个 IP_SHARE 读改写操作（Read-modify-write Operation）编码到 pinmux 的位 [31:20]，包含有效标志（Valid Flag）、移位量（Shift）、宽度减一（Width-1）和值（Value）。与 EM32F967_IO1 或其便捷辅助宏按位或组合，可在同一 pinmux 单元中编码第二个操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shift` | 字段在 IP_SHARE 寄存器中的位位置（Bit Position），范围为 0–31。 |
| `width` | 字段宽度（Field Width），单位为位，范围为 1–4。 |
| `val` | 要写入字段的值（Value）。 |

<a id="afe73c3c740a1b2a0b4904f116a72668f"></a>

### `EM32F967_IO_CLR_2BIT`

```c
#define EM32F967_IO_CLR_2BIT ( pos)
```

展开值（Value）：

```c
EM32F967_IO1((pos), 2U, 0U)
```

槽位 1 辅助宏（Slot 1 Helper）：清除一个 2 位 IP_SHARE 字段。

等价于将 EM32F967_IO1 用于值为 0 的 2 位字段（2-bit Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pos` | 2 位字段在 IP_SHARE 寄存器中的位位置（Bit Position），范围为 0–31。 |

<a id="a4b83a385de1ec4737f3c8fd505a2aba4"></a>

### `EM32F967_IO_CLR_BIT`

```c
#define EM32F967_IO_CLR_BIT ( pos)
```

展开值（Value）：

```c
EM32F967_IO1((pos), 1U, 0U)
```

槽位 1 辅助宏（Slot 1 Helper）：清除单个 IP_SHARE 位。

等价于将 EM32F967_IO1 用于值为 0 的 1 位字段（1-bit Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pos` | IP_SHARE 寄存器中要清除的位位置（Bit Position），范围为 0–31。 |

<a id="aef613aabc331e2c875bf7f990e363c54"></a>

### `EM32F967_IO_NONE`

```c
#define EM32F967_IO_NONE 0U
```

携带在 pinmux 单元中的嵌入式 IP_SHARE 操作（Embedded IP_SHARE Operations）。

pinmux 值的高 24 位（位 [31:8]）最多可编码两个 IP_SHARE 读改写操作（Read-modify-write Operations）。引脚控制驱动（Pinctrl Driver，drivers/pinctrl/pinctrl_em32.c 中的 em32_apply_ioshare_from_pinmux()）在存在这些操作时解码并应用它们，不再回退到内建的 em32_ioshare_table[] 查表过程。

位布局（Bit Layout），必须与驱动中的 `PINMUX_IO*` 定义保持一致：

位 [8] 为 io1_valid（1 表示存在第一个 IP_SHARE 操作）；位 [13:9] 为 io1_shift（IP_SHARE 内的位位置，范围为 0–31）；位 [15:14] 为 io1_width_m1（字段宽度减一，0 表示 1 位）；位 [19:16] 为 io1_value（写入 io1_shift 位置的值）；位 [20] 为 io2_valid（1 表示存在第二个 IP_SHARE 操作）；位 [25:21] 为 io2_shift；位 [27:26] 为 io2_width_m1；位 [31:28] 为 io2_value。

<a id="ae3d7d30dc7a11d41db0585fbcf976735"></a>

### `EM32F967_IO_SET_2BIT`

```c
#define EM32F967_IO_SET_2BIT ( pos, val )
```

展开值（Value）：

```c
EM32F967_IO1((pos), 2U, (val))
```

槽位 1 辅助宏（Slot 1 Helper）：写入一个 2 位 IP_SHARE 字段。

等价于将 EM32F967_IO1 用于 2 位字段（2-bit Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pos` | 2 位字段在 IP_SHARE 寄存器中的位位置（Bit Position），范围为 0–31。 |
| `val` | 要写入字段的值（Value），范围为 0–3。 |

<a id="a10463a0f449b174af9f9e6338a97ac72"></a>

### `EM32F967_IO_SET_BIT`

```c
#define EM32F967_IO_SET_BIT ( pos)
```

展开值（Value）：

```c
EM32F967_IO1((pos), 1U, 1U)
```

槽位 1 辅助宏（Slot 1 Helper）：设置单个 IP_SHARE 位。

等价于将 EM32F967_IO1 用于值为 1 的 1 位字段（1-bit Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pos` | IP_SHARE 寄存器中要设置的位位置（Bit Position），范围为 0–31。 |

<a id="add1cca26494694aa34c31e1f3a41e297"></a>

### `EM32F967_MUX_MASK`

```c
#define EM32F967_MUX_MASK 0x7U
```

<a id="ab91e901fcce847624af03e49ccfb785e"></a>

### `EM32F967_MUX_SHIFT`

```c
#define EM32F967_MUX_SHIFT 0U
```

引脚配置位字段编码（Pin Configuration Bit Field Encoding），采用 EM32 风格。

字段（Fields）：

- mux [0:2]：复用功能（Multiplexing Function），3 位。
- pin [3:6]：引脚编号（Pin Number），4 位，范围为 0–15。
- port [7:7]：端口标识符（Port Identifier），1 位，0 表示 PA，1 表示 PB。

此编码（Encoding）最多支持 2 个端口、每端口 16 个引脚以及 8 种复用功能。

<a id="ade0b89bc6283e9fa47fbdb1a63224567"></a>

### `EM32F967_PIN_MASK`

```c
#define EM32F967_PIN_MASK 0xFU
```

<a id="a415fe4032ba9029ecbb915036558f216"></a>

### `EM32F967_PIN_SHIFT`

```c
#define EM32F967_PIN_SHIFT 3U
```

<a id="a33870f76f04772632963b4433747b0f5"></a>

### `EM32F967_PINMUX`

```c
#define EM32F967_PINMUX ( port, pin, mux )
```

展开值（Value）：

```c
(((((port) - 'A') & EM32F967_PORT_MASK) << EM32F967_PORT_SHIFT) |                          \
 (((pin) & EM32F967_PIN_MASK) << EM32F967_PIN_SHIFT) |                                     \
 (((EM32F967_##mux) & EM32F967_MUX_MASK) << EM32F967_MUX_SHIFT))
```

EM32F967 引脚复用宏（Pin Multiplexing Macro），采用 EM32 风格。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），为 'A' 或 'B'。 |
| `pin` | 引脚编号（Pin Number），范围为 0–15。 |
| `mux` | 复用功能（Multiplexing Function）：GPIO 或 AF1–AF7。 |

<a id="a95012f2112abe8d306d598dbb7dc0d71"></a>

### `EM32F967_PINMUX_IO`

```c
#define EM32F967_PINMUX_IO ( port, pin, mux, ioshare )
```

展开值（Value）：

```c
(EM32F967_PINMUX(port, pin, mux) | (ioshare))
```

包含嵌入式 IP_SHARE 操作的 EM32F967 引脚复用宏（Pinmux Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），为 'A' 或 'B'。 |
| `pin` | 引脚编号（Pin Number），范围为 0–15。 |
| `mux` | 复用功能（Multiplexing Function）：GPIO 或 AF1–AF7。 |
| `ioshare` | 使用 `EM32F967_IO_*` / EM32F967_IO1 / EM32F967_IO2 构造的一个或两个 IP_SHARE 操作，或者 EM32F967_IO_NONE。 |

<a id="a68fdd9bcb324f906cde4e7f2779c20ee"></a>

### `EM32F967_PORT_MASK`

```c
#define EM32F967_PORT_MASK 0x1U
```

<a id="a70d272163e70075e409ece520ab3df05"></a>

### `EM32F967_PORT_SHIFT`

```c
#define EM32F967_PORT_SHIFT 7U
```

<a id="afe8add9c6b17be78f01ced071ab3a0ec"></a>

### `EM32F967_PULL_DOWN_3V`

```c
#define EM32F967_PULL_DOWN_3V 3 /* 11: PD (15KΩ@3.3V, 25.2KΩ@1.8V) */
```

<a id="a53bb0ef38ab66505e00bb6fa945c3ee7"></a>

### `EM32F967_PULL_DOWN_5V`

```c
#define EM32F967_PULL_DOWN_5V 3 /* 11: PD (15KΩ@5V, 21.8KΩ@3.3V, 49.6KΩ@1.8V) */
```

<a id="a254e0b8c5245a97239e9d51216f7e03f"></a>

### `EM32F967_PULL_NONE_3V`

```c
#define EM32F967_PULL_NONE_3V 0 /* 00: Floating */
```

<a id="a132c694b104108ee3bdab8493466ccdf"></a>

### `EM32F967_PULL_NONE_5V`

```c
#define EM32F967_PULL_NONE_5V 0 /* 00: Floating */
```

<a id="a06b93f47492b64939e7e3709aa807be9"></a>

### `EM32F967_PULL_UP0_3V`

```c
#define EM32F967_PULL_UP0_3V 1 /* 01: PU0 (66KΩ@3.3V, 140KΩ@1.8V) */
```

<a id="a15e15b874c30415817d74534af9048e2"></a>

### `EM32F967_PULL_UP0_5V`

```c
#define EM32F967_PULL_UP0_5V 1 /* 01: PU0 (66KΩ@5V, 101KΩ@3.3V, 238KΩ@1.8V) */
```

<a id="a153386a1e74f1fc572d2761d6b5136f1"></a>

### `EM32F967_PULL_UP1_3V`

```c
#define EM32F967_PULL_UP1_3V 2 /* 10: PU1 (4.7KΩ@3.3V, 8.53KΩ@1.8V) */
```

<a id="a31e365dede45b78c88b7adc00229cc79"></a>

### `EM32F967_PULL_UP1_5V`

```c
#define EM32F967_PULL_UP1_5V 2 /* 10: PU1 (4.7KΩ@5V, 6.41KΩ@3.3V, 12.7KΩ@1.8V) */
```


## 10.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_pcie_hid_reference/P002_em32f967-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aem32f967-pinctrl_8h_html_ab91e901fcce847624af03e49ccfb785e"></a>
<a id="aem32f967-pinctrl_8h_html_add1cca26494694aa34c31e1f3a41e297"></a>
<a id="aem32f967-pinctrl_8h_html_a415fe4032ba9029ecbb915036558f216"></a>
<a id="aem32f967-pinctrl_8h_html_ade0b89bc6283e9fa47fbdb1a63224567"></a>
<a id="aem32f967-pinctrl_8h_html_a68fdd9bcb324f906cde4e7f2779c20ee"></a>
<a id="aem32f967-pinctrl_8h_html_a70d272163e70075e409ece520ab3df05"></a>
<a id="aem32f967-pinctrl_8h_html_a1c0555f650a6bb6949006801c75be023"></a>
<a id="aem32f967-pinctrl_8h_html_a33870f76f04772632963b4433747b0f5"></a>

---

[上一章](P009_zephyr__drivers__video.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__i2s.h_文件参考.md)
