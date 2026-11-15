---
id: learning.zephyr-docs.hardware.dacapi-1
title: Infineon连续时间DAC设备树常量
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第820章\_Infineon连续时间DAC设备树常量

原文：[infineon-autanalog-ctdac_8h](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html)。读取日期：2026-10-13，`latest`。

头文件 `zephyr/dt-bindings/dac/infineon-autanalog-ctdac.h` 提供Infineon自主模拟（Autonomous Analog，AutAnalog）子系统连续时间数模转换器（Continuous-Time Digital-to-Analog Converter，CTDAC）的设备树绑定常量（Devicetree Binding Constants）。常量数值与外设驱动库（Peripheral Driver Library，PDL）枚举一致，用于配置AutAnalog连续时间DAC的设备树属性。

[官方源码浏览](P835_Infineon连续时间DAC常量源码.md)提供原始定义；配置条件和电气档位见[CTDAC绑定](P778_Infineon自主模拟连续时间数模转换器绑定.md)。本页不重复添加原页未给出的电气数值。

## 820.1\_参考缓冲器功耗模式

对应PDL枚举类型 `cy_en_autanalog_dac_ref_buf_pwr_t`。

功耗模式（Power Mode）控制缓冲器（Buffer），RAIL系列说明涉及电荷泵（Charge Pump）开启状态。

```c
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_OFF 0
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW 1
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW_RAIL 2
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_LOW_RAIL 4
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_MEDIUM_RAIL 6
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH 7
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH_RAIL 8
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_HIGH_RAIL 10
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a5964395b876feaf336ff0570c4d56227) | `0` | 参考缓冲器断电 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a7eb3379959d7526aa78f3b9c182ddd09) | `1` | 超低功耗，电荷泵关闭 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ac0e566338c0f98fb841aec9859286f20) | `2` | 超低功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_LOW_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a4379fc85bcc3d40ce11323d3d5c6ec71) | `4` | 低功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_MEDIUM_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a97ecd39cfb9dd15c7c7977095755cc37) | `6` | 中等功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#aaff8f8fbf790e827130001d882a5ecf6) | `7` | 高功耗模式 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#af2ca9697497a90fd79484f778d794992) | `8` | 高功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_HIGH_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a0be8592ce262bd9a7cc4b2c6f50ba26c) | `10` | 超高功耗，电荷泵开启 |

## 820.2\_输出缓冲器功耗模式

对应PDL枚举类型 `cy_en_autanalog_dac_out_buf_pwr_t`。

功耗模式（Power Mode）控制缓冲器（Buffer），RAIL系列说明涉及电荷泵（Charge Pump）开启状态。

```c
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_OFF 0
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW 1
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW_RAIL 2
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_LOW_RAIL 4
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_MEDIUM_RAIL 6
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_HIGH_RAIL 8
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_HIGH_RAIL 10
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#af640431595c2834723aa7914c6c0a176) | `0` | 输出缓冲器断电 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a208bb820083b2f550b3644e08fc07e30) | `1` | 超低功耗，电荷泵关闭 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a121f3dee9e4b02492b50b92f258e7f7b) | `2` | 超低功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_LOW_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a9fc33889d0d0357d592fca7fc3890d17) | `4` | 低功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_MEDIUM_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a45ae6055e8ca8e385b489391539ec7ed) | `6` | 中等功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_HIGH_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#aa423a9d6bde696a99291a1b89e3fdd5e) | `8` | 高功耗，电荷泵开启 |
| [`IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_HIGH_RAIL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a544900e67ab9f16217151d38efc82d7b) | `10` | 超高功耗，电荷泵开启 |

## 820.3\_参考电压源编码

对应PDL枚举类型 `cy_en_autanalog_dac_vref_mux_t`。

参考电压源（Vref Source）使用合并的 `vrefSel + vrefMux` 编码。VDDA使用位8作为标志；其余值直接对应上述PDL枚举编码。CTB指连续时间模块（Continuous Time Block），OA指运算放大器（Operational Amplifier），PRB指可编程参考模块（Programmable Reference Block）；VDDA为模拟供电，VBGR为带隙参考（Bandgap Reference）标识。CTB0、CTB1分别表示连续时间模块0和1。

```c
#define IFX_AUTANALOG_CTDAC_VREF_VDDA 0x100
#define IFX_AUTANALOG_CTDAC_VREF_VBGR 0
#define IFX_AUTANALOG_CTDAC_VREF_CTB0_OA0 1
#define IFX_AUTANALOG_CTDAC_VREF_CTB0_OA1 2
#define IFX_AUTANALOG_CTDAC_VREF_CTB1_OA0 3
#define IFX_AUTANALOG_CTDAC_VREF_CTB1_OA1 4
#define IFX_AUTANALOG_CTDAC_VREF_PRB_OUT0 6
#define IFX_AUTANALOG_CTDAC_VREF_PRB_OUT1 7
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_VREF_VDDA`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a082d1519f4a6057657de93198ce496a9) | `0x100` | VDDA供电 |
| [`IFX_AUTANALOG_CTDAC_VREF_VBGR`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a25cf3e47402c4f18f8f4720b033cb5c4) | `0` | 带隙参考 |
| [`IFX_AUTANALOG_CTDAC_VREF_CTB0_OA0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a19afb7e5ccc14cd0ee0d7299a371f680) | `1` | CTB0运放0输出 |
| [`IFX_AUTANALOG_CTDAC_VREF_CTB0_OA1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ac0c0472635b642a3d3c175cb2daa6b8b) | `2` | CTB0运放1输出 |
| [`IFX_AUTANALOG_CTDAC_VREF_CTB1_OA0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ae4934e484aafa35ad26a7d7e3ff28042) | `3` | CTB1运放0输出 |
| [`IFX_AUTANALOG_CTDAC_VREF_CTB1_OA1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a699e909ba9f69427c3cad5e6e2d17e7d) | `4` | CTB1运放1输出 |
| [`IFX_AUTANALOG_CTDAC_VREF_PRB_OUT0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a53414a835620fb03327e91c6766507d4) | `6` | PRB输出0 |
| [`IFX_AUTANALOG_CTDAC_VREF_PRB_OUT1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a19cf55bac92ffc090d7e6c7b26e1e67c) | `7` | PRB输出1 |

## 820.4\_输出拓扑

对应PDL枚举类型 `cy_en_autanalog_dac_topo_cfg_t`。

拓扑（Topology）定义输出连接形式。下表保留头文件原说明中的内部／外部缓冲名称；[设备树绑定](P778_Infineon自主模拟连续时间数模转换器绑定.md)进一步说明，BUFFERED_INTERNAL用于仅内部连接，BUFFERED_EXTERNAL用于内部和外部连接，不应仅凭宏名推断需要外接缓冲器。

```c
#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT 0
#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_CAP 1
#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_HOLD 2
#define IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_INTERNAL 3
#define IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_EXTERNAL 4
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_TOPO_DIRECT`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a95d11f5606a147a373f86de08cf90cc3) | `0` | 直接输出（Direct Output） |
| [`IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_CAP`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a858e46267a4d05a56298390698b39f4f) | `1` | 带跟踪电容（Track Capacitor）的直接输出 |
| [`IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_HOLD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ae121c7091c3cf5b92e9aab72afd3b927) | `2` | 带跟踪保持（Track-and-Hold）的直接输出 |
| [`IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_INTERNAL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ab298b5ac13366833ed7f94ffeee56403) | `3` | 内部缓冲输出（Internally Buffered Output） |
| [`IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_EXTERNAL`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a3713804ef03a6d114f7729057a718a97) | `4` | 外部缓冲输出（Externally Buffered Output） |

## 820.5\_波形工作模式

对应PDL枚举类型 `cy_en_autanalog_dac_oper_mode_t`。

波形模式（Waveform Operating Mode）区分单次（One-Shot）、连续（Continuous）、象限（Quadrant）数量及波形表模式（Waveform Table Mode）。

```c
#define IFX_AUTANALOG_CTDAC_OP_OS_ONE_QUAD 0
#define IFX_AUTANALOG_CTDAC_OP_OS_TWO_QUAD 1
#define IFX_AUTANALOG_CTDAC_OP_OS_FOUR_QUAD 2
#define IFX_AUTANALOG_CTDAC_OP_CONT_ONE_QUAD 3
#define IFX_AUTANALOG_CTDAC_OP_CONT_TWO_QUAD 4
#define IFX_AUTANALOG_CTDAC_OP_CONT_FOUR_QUAD 5
#define IFX_AUTANALOG_CTDAC_OP_ADDR 6
#define IFX_AUTANALOG_CTDAC_OP_DATA 7
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_OP_OS_ONE_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a945ac2f2555acb7f998e17ecbcf4aadb) | `0` | 单次，一个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_OS_TWO_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a329b7a073b1c4c3113274667eb5e273b) | `1` | 单次，两个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_OS_FOUR_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a984655ad839d82476c6b720eb6d5994e) | `2` | 单次，四个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_CONT_ONE_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#afc7bd814232f202a76a8db9de82cbf85) | `3` | 连续，一个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_CONT_TWO_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#afc732556fbc7ff06e9cafaa15e7b6388) | `4` | 连续，两个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_CONT_FOUR_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a8470f22063f7ddce8a63f970a021b7c6) | `5` | 连续，四个象限 |
| [`IFX_AUTANALOG_CTDAC_OP_ADDR`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a3dccf4ae03f839189390e50ed15d5b74) | `6` | 地址波形表模式（Address Waveform Table Mode） |
| [`IFX_AUTANALOG_CTDAC_OP_DATA`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ab5bfb4e95b6a984c41fb1c11591f4e1e) | `7` | 数据波形表模式（Data Waveform Table Mode） |

## 820.6\_步长选择器

对应PDL枚举类型 `cy_en_autanalog_dac_step_sel_t`。

步长选择器（Step Value Selector）选择预先配置的步长编号。

```c
#define IFX_AUTANALOG_CTDAC_STEP_SEL_DISABLED 0
#define IFX_AUTANALOG_CTDAC_STEP_SEL_0 1
#define IFX_AUTANALOG_CTDAC_STEP_SEL_1 2
#define IFX_AUTANALOG_CTDAC_STEP_SEL_2 3
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_STEP_SEL_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#aea162a5fcac3a763ede8637100691a19) | `0` | 禁用步长选择 |
| [`IFX_AUTANALOG_CTDAC_STEP_SEL_0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a1c564f25fa663c14268d5564a0618cc6) | `1` | 使用步长0 |
| [`IFX_AUTANALOG_CTDAC_STEP_SEL_1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a4eec07306f0c4a9289531cdb4e8c6d0a) | `2` | 使用步长1 |
| [`IFX_AUTANALOG_CTDAC_STEP_SEL_2`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a1c86a9af799fe6992f2fe49d7b5c37ce) | `3` | 使用步长2 |

## 820.7\_状态与范围检测选择器

对应PDL枚举类型 `cy_en_autanalog_dac_stat_sel_t`。

状态选择器（Status Selector）选择状态与范围检测（Range Detection）配置编号。

```c
#define IFX_AUTANALOG_CTDAC_STAT_SEL_DISABLED 0
#define IFX_AUTANALOG_CTDAC_STAT_SEL_0 1
#define IFX_AUTANALOG_CTDAC_STAT_SEL_1 2
#define IFX_AUTANALOG_CTDAC_STAT_SEL_2 3
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_STAT_SEL_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a06df5f6fea959af7a8eafd38eb924155) | `0` | 禁用状态选择 |
| [`IFX_AUTANALOG_CTDAC_STAT_SEL_0`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#acac06594312e0a7511a3ad50c6605de8) | `1` | 使用状态选择器0 |
| [`IFX_AUTANALOG_CTDAC_STAT_SEL_1`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a09c92f98bdbf17e9db2f9862bf5b690d) | `2` | 使用状态选择器1 |
| [`IFX_AUTANALOG_CTDAC_STAT_SEL_2`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ab69d84cf3219ef6d98e89a19e7f3e4d8) | `3` | 使用状态选择器2 |

## 820.8\_通道限值与范围检测条件

对应PDL枚举类型 `cy_en_autanalog_dac_limit_t`。

限值条件（Limit Condition）描述结果与已配置范围之间的关系。

```c
#define IFX_AUTANALOG_CTDAC_LIMIT_BELOW 0
#define IFX_AUTANALOG_CTDAC_LIMIT_INSIDE 1
#define IFX_AUTANALOG_CTDAC_LIMIT_ABOVE 2
#define IFX_AUTANALOG_CTDAC_LIMIT_OUTSIDE 3
```

| 宏 | 值 | 中文说明 |
| --- | --- | --- |
| [`IFX_AUTANALOG_CTDAC_LIMIT_BELOW`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a22a1602f18734edbc66418afe4e6e770) | `0` | 结果低于配置范围 |
| [`IFX_AUTANALOG_CTDAC_LIMIT_INSIDE`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#ae2d561c8be6d2248839dcddfc9c0e4d8) | `1` | 结果位于配置范围内 |
| [`IFX_AUTANALOG_CTDAC_LIMIT_ABOVE`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a0c7765c94f1d59c559e7a0aa9a5f7eb2) | `2` | 结果高于配置范围 |
| [`IFX_AUTANALOG_CTDAC_LIMIT_OUTSIDE`](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h.html#a13eab148d0d6fa684bd0ceb6f7ccb0fc) | `3` | 结果位于配置范围外 |


---

[上一章：DACx0508设备树常量](P819_DACx0508设备树常量.md) · [下一章：SiliconLabsVDAC设备树常量](P821_SiliconLabsVDAC设备树常量.md) · [返回大纲](大纲.md)
