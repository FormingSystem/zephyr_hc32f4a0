---
id: learning.zephyr-docs.api-source-runtime-reference.page-1
title: arm-mps2-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_arm-mps2-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h.html)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>

```c
/*
 * Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS2_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS2_PINCTRL_H_

#define MPS2_ALT_FUNC_POS 0
#define MPS2_ALT_FUNC_MASK 0x3

#define MPS2_EXP_NUM_POS 2
#define MPS2_EXP_NUM_MASK 0x3F

#define MPS2_PINCTRL_FUNC_UART 0
#define MPS2_PINCTRL_FUNC_GPIO 1
#define MPS2_PINCTRL_FUNC_I2C 2
#define MPS2_PINCTRL_FUNC_SPI 3


#define MPS2_PINMUX(alt_func, exp_num) (exp_num << MPS2_EXP_NUM_POS | \
        alt_func << MPS2_ALT_FUNC_POS)



/*
 * This is the mapping from the ARM MPS2 Board pins to GPIO
 * controllers.
 *
 * D0 : EXT_0
 * D1 : EXT_4
 * D2 : EXT_2
 * D3 : EXT_3
 * D4 : EXT_1
 * D5 : EXT_6
 * D6 : EXT_7
 * D7 : EXT_8
 * D8 : EXT_9
 * D9 : EXT_10
 * D10 : EXT_12
 * D11 : EXT_13
 * D12 : EXT_14
 * D13 : EXT_11
 * D14 : EXT_15
 * D15 : EXT_5
 * D16 : EXT_16
 * D17 : EXT_17
 * D18 : EXT_18
 * D19 : EXT_19
 * D20 : EXT_20
 * D21 : EXT_21
 * D22 : EXT_22
 * D23 : EXT_23
 * D24 : EXT_24
 * D25 : EXT_25
 * D26 : EXT_26
 * D27 : EXT_30
 * D28 : EXT_28
 * D29 : EXT_29
 * D30 : EXT_27
 * D31 : EXT_32
 * D32 : EXT_33
 * D33 : EXT_34
 * D34 : EXT_35
 * D35 : EXT_36
 * D36 : EXT_38
 * D37 : EXT_39
 * D38 : EXT_40
 * D39 : EXT_44
 * D40 : EXT_41
 * D41 : EXT_31
 * D42 : EXT_37
 * D43 : EXT_42
 * D44 : EXT_43
 * D45 : EXT_45
 * D46 : EXT_46
 * D47 : EXT_47
 * D48 : EXT_48
 * D49 : EXT_49
 * D50 : EXT_50
 * D51 : EXT_51
 *
 * UART_3_RX : D0
 * UART_3_TX : D1
 * SPI_3_CS : D10
 * SPI_3_MOSI : D11
 * SPI_3_MISO : D12
 * SPI_3_SCLK : D13
 * I2C_3_SDA : D14
 * I2C_3_SCL : D15
 * UART_4_RX : D26
 * UART_4_TX : D30
 * SPI_4_CS : D36
 * SPI_4_MOSI : D37
 * SPI_4_MISO : D38
 * SPI_4_SCK : D39
 * I2C_4_SDA : D40
 * I2C_4_SCL : D41
 *
 */

/* GPIO 0 */
#define UART3_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 0)
#define UART3_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 4)
#define SBCON2_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 5)
#define SBCON2_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 15)
#define SPI3_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 11)
#define SPI3_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 12)
#define SPI3_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 13)
#define SPI3_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 14)

/* GPIO 1 */
#define SPI2_SS_EXP  MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 16)
#define SPI2_MISO_EXP  MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 17)
#define SPI2_MOSI_EXP  MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 18)
#define SPI2_SCK_EXP  MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 19)
#define UART4_RXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 26)
#define UART4_TXD_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_UART, 30)
#define SBCON3_SCL_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 31)

/* GPIO 2 */
#define SBCON3_SDA_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_I2C, 41)
#define SPI4_SS_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 38)
#define SPI4_MOSI_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 39)
#define SPI4_MISO_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 40)
#define SPI4_SCK_EXP MPS2_PINMUX(MPS2_PINCTRL_FUNC_SPI, 44)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS2_PINCTRL_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Arm Limited and/or its affiliates <open-source-office@arm.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

以下给出 ARM MPS2 开发板引脚到 GPIO 控制器的映射，以及外设信号所使用的开发板引脚。

| 开发板引脚（Board pin） | GPIO 控制器连接（GPIO controller connection） |
| --- | --- |
| `D0` | `EXT_0` |
| `D1` | `EXT_4` |
| `D2` | `EXT_2` |
| `D3` | `EXT_3` |
| `D4` | `EXT_1` |
| `D5` | `EXT_6` |
| `D6` | `EXT_7` |
| `D7` | `EXT_8` |
| `D8` | `EXT_9` |
| `D9` | `EXT_10` |
| `D10` | `EXT_12` |
| `D11` | `EXT_13` |
| `D12` | `EXT_14` |
| `D13` | `EXT_11` |
| `D14` | `EXT_15` |
| `D15` | `EXT_5` |
| `D16` | `EXT_16` |
| `D17` | `EXT_17` |
| `D18` | `EXT_18` |
| `D19` | `EXT_19` |
| `D20` | `EXT_20` |
| `D21` | `EXT_21` |
| `D22` | `EXT_22` |
| `D23` | `EXT_23` |
| `D24` | `EXT_24` |
| `D25` | `EXT_25` |
| `D26` | `EXT_26` |
| `D27` | `EXT_30` |
| `D28` | `EXT_28` |
| `D29` | `EXT_29` |
| `D30` | `EXT_27` |
| `D31` | `EXT_32` |
| `D32` | `EXT_33` |
| `D33` | `EXT_34` |
| `D34` | `EXT_35` |
| `D35` | `EXT_36` |
| `D36` | `EXT_38` |
| `D37` | `EXT_39` |
| `D38` | `EXT_40` |
| `D39` | `EXT_44` |
| `D40` | `EXT_41` |
| `D41` | `EXT_31` |
| `D42` | `EXT_37` |
| `D43` | `EXT_42` |
| `D44` | `EXT_43` |
| `D45` | `EXT_45` |
| `D46` | `EXT_46` |
| `D47` | `EXT_47` |
| `D48` | `EXT_48` |
| `D49` | `EXT_49` |
| `D50` | `EXT_50` |
| `D51` | `EXT_51` |

| 外设信号（Peripheral signal） | 开发板引脚（Board pin） |
| --- | --- |
| `UART_3_RX` | `D0` |
| `UART_3_TX` | `D1` |
| `SPI_3_CS` | `D10` |
| `SPI_3_MOSI` | `D11` |
| `SPI_3_MISO` | `D12` |
| `SPI_3_SCLK` | `D13` |
| `I2C_3_SDA` | `D14` |
| `I2C_3_SCL` | `D15` |
| `UART_4_RX` | `D26` |
| `UART_4_TX` | `D30` |
| `SPI_4_CS` | `D36` |
| `SPI_4_MOSI` | `D37` |
| `SPI_4_MISO` | `D38` |
| `SPI_4_SCK` | `D39` |
| `I2C_4_SDA` | `D40` |
| `I2C_4_SCL` | `D41` |

### 注释 3：原第 103 行

GPIO 0。

### 注释 4：原第 113 行

GPIO 1。

### 注释 5：原第 122 行

GPIO 2。

### 注释 6：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS2_PINCTRL_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps2-pinctrl_8h.html)

---

[返回大纲](大纲.md) · [下一章](P002_blob_srv.h_源码浏览.md)
