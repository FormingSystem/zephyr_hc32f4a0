---
id: learning.zephyr-docs.api-file-clock-network-reference.page-7
title: zephyr__dt-bindings__pinctrl__esp-pinctrl-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_esp-pinctrl-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_a14b1575596d4a3c7f349e140a206e7fc"></a>

```c
#define ESP32_PIN_NUM_SHIFT 0U
```

相关声明：[ESP32_PIN_NUM_SHIFT](#a14b1575596d4a3c7f349e140a206e7fc)。

GPIO 引脚编号字段（Pin Number Field）。

<a id="r_aff8c7306c9eb06955c069a08700b9602"></a>

```c
#define ESP32_PIN_NUM_MASK 0x3FU
```

相关声明：[ESP32_PIN_NUM_MASK](#aff8c7306c9eb06955c069a08700b9602)。

<a id="r_a0069fd5363ff598a903823729ac7b785"></a>

```c
#define ESP32_PIN_SIGI_MASK 0x1FFU
```

相关声明：[ESP32_PIN_SIGI_MASK](#a0069fd5363ff598a903823729ac7b785)。

用于提取 I/O 信号索引（Signal Indexes）的定义。

<a id="r_a457b5af6f423f5d743b81317f331f175"></a>

```c
#define ESP32_PIN_SIGI_SHIFT 6U
```

相关声明：[ESP32_PIN_SIGI_SHIFT](#a457b5af6f423f5d743b81317f331f175)。

<a id="r_a97e539c13c42cabdb31c53dba9573bb8"></a>

```c
#define ESP32_PIN_SIGO_MASK 0x1FFU
```

相关声明：[ESP32_PIN_SIGO_MASK](#a97e539c13c42cabdb31c53dba9573bb8)。

<a id="r_ab7b2f3303e89bb59c9fc0aec216678fd"></a>

```c
#define ESP32_PIN_SIGO_SHIFT 15U
```

相关声明：[ESP32_PIN_SIGO_SHIFT](#ab7b2f3303e89bb59c9fc0aec216678fd)。

<a id="r_ae0d2e726ab8d90343e5c80e1d9b85ad8"></a>

```c
#define ESP_SIG_INVAL ESP32_PIN_SIGI_MASK
```

相关声明：[ESP_SIG_INVAL](#ae0d2e726ab8d90343e5c80e1d9b85ad8)、[ESP32_PIN_SIGI_MASK](#a0069fd5363ff598a903823729ac7b785)。

<a id="r_a932ca0617135c66cc96fba696ac06e7e"></a>

```c
#define ESP32_PINMUX(pin, sig_i, sig_o)
```

相关声明：[ESP32_PINMUX](#a932ca0617135c66cc96fba696ac06e7e)。

根据引脚编号及 GPIO 矩阵信号（GPIO Matrix Signals）构建 ESP32 引脚复用值（Pinmux Value）。

<a id="r_ab397163b12f1539ab42faec88ad63ef2"></a>

```c
#define ESP32_RMII_SLOT_SHIFT 24U
```

相关声明：[ESP32_RMII_SLOT_SHIFT](#ab397163b12f1539ab42faec88ad63ef2)。

以太网 RMII 引脚编码（Pin Encoding）。

<a id="r_a0550ba7d14ee1488fd60e2345ee01756"></a>

```c
#define ESP32_RMII_SLOT_MASK 0xFU
```

相关声明：[ESP32_RMII_SLOT_MASK](#a0550ba7d14ee1488fd60e2345ee01756)。

RMII 信号槽位字段掩码（Signal Slot Field Mask）。

<a id="r_af4ce081c5ff7fa1521443b4d1fe9a8f0"></a>

```c
#define ESP32_RMII_MARKER BIT(30)
```

相关声明：[ESP32_RMII_MARKER](#af4ce081c5ff7fa1521443b4d1fe9a8f0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将一个单元（Cell）标记为 RMII 引脚复用（Pinmux）。

<a id="r_a3d10ffea4cfc02a4694cb879a034b886"></a>

```c
#define ESP32_RMII_PINMUX(pin, slot)
```

相关声明：[ESP32_RMII_PINMUX](#a3d10ffea4cfc02a4694cb879a034b886)。

构建以太网 RMII 引脚复用值（Pinmux Value）。

<a id="define-members-0"></a>

### 以太网 RMII 信号槽位（Ethernet RMII Signal Slots）

<a id="r_a05b408148518137228c814967ae1bd05"></a>

```c
#define ESP_RMII_CLK 0
```

相关声明：[ESP_RMII_CLK](#a05b408148518137228c814967ae1bd05)。

RMII 参考时钟（Reference Clock）。

<a id="r_afdd83fa40a18fd541850e560c0c267bd"></a>

```c
#define ESP_RMII_TX_EN 1
```

相关声明：[ESP_RMII_TX_EN](#afdd83fa40a18fd541850e560c0c267bd)。

RMII 发送使能（Transmit Enable）。

<a id="r_ae74823edbeb6ef6fd0ed31fa84bfcde8"></a>

```c
#define ESP_RMII_TXD0 2
```

相关声明：[ESP_RMII_TXD0](#ae74823edbeb6ef6fd0ed31fa84bfcde8)。

RMII 发送数据 0（Transmit Data 0）。

<a id="r_a50855f7d38e6fa343c4e7e7bc2e58bb7"></a>

```c
#define ESP_RMII_TXD1 3
```

相关声明：[ESP_RMII_TXD1](#a50855f7d38e6fa343c4e7e7bc2e58bb7)。

RMII 发送数据 1（Transmit Data 1）。

<a id="r_ab018a7ca7dc9c30ab2b229e020fad1db"></a>

```c
#define ESP_RMII_CRS_DV 4
```

相关声明：[ESP_RMII_CRS_DV](#ab018a7ca7dc9c30ab2b229e020fad1db)。

RMII 载波侦听／数据有效（Carrier Sense / Data Valid）。

<a id="r_aeea7819bdae58e8c5824a506c081308d"></a>

```c
#define ESP_RMII_RXD0 5
```

相关声明：[ESP_RMII_RXD0](#aeea7819bdae58e8c5824a506c081308d)。

RMII 接收数据 0（Receive Data 0）。

<a id="r_a584740b275282125d939c3e4e2879088"></a>

```c
#define ESP_RMII_RXD1 6
```

相关声明：[ESP_RMII_RXD1](#a584740b275282125d939c3e4e2879088)。

RMII 接收数据 1（Receive Data 1）。

<a id="r_a53dc181757ceb98c3c016dda67ec84db"></a>

```c
#define ESP_RMII_SLOT_COUNT 7
```

相关声明：[ESP_RMII_SLOT_COUNT](#a53dc181757ceb98c3c016dda67ec84db)。

上述 ESP_RMII_* 信号槽位（Signal Slots）的数量。

<a id="define-members-1"></a>

### ESP32 引脚配置位字段布局（Pin Configuration Bit Field Layout）

ESP32 引脚配置位字段（Pin Configuration Bit Field）。

此字段编码 ESP32 引脚控制驱动（Pinctrl Driver）使用的引脚配置选项。

字段（Fields）：

这些值组合为一个整数，随后由驱动转换为 GPIO 配置标志（Configuration Flags）。

<a id="r_a47498f4ba429ddaedc5b2547888bfa00"></a>

```c
#define ESP32_PIN_BIAS_SHIFT 0U
```

相关声明：[ESP32_PIN_BIAS_SHIFT](#a47498f4ba429ddaedc5b2547888bfa00)。

<a id="r_a65d2b03b1a813cb4d2921c7cc8deec79"></a>

```c
#define ESP32_PIN_BIAS_MASK 0x3U
```

相关声明：[ESP32_PIN_BIAS_MASK](#a65d2b03b1a813cb4d2921c7cc8deec79)。

<a id="r_abfdf0aa9a8a5116f3ca66e54e72552ac"></a>

```c
#define ESP32_PIN_DRV_SHIFT 2U
```

相关声明：[ESP32_PIN_DRV_SHIFT](#abfdf0aa9a8a5116f3ca66e54e72552ac)。

<a id="r_a4d05215be796ff091633a5f0de2a6748"></a>

```c
#define ESP32_PIN_DRV_MASK 0x3U
```

相关声明：[ESP32_PIN_DRV_MASK](#a4d05215be796ff091633a5f0de2a6748)。

<a id="r_af20225f7ed095e083c3b7a2fa55a5313"></a>

```c
#define ESP32_PIN_OUT_SHIFT 4U
```

相关声明：[ESP32_PIN_OUT_SHIFT](#af20225f7ed095e083c3b7a2fa55a5313)。

<a id="r_a0c806899f6fb854f50c3a88a40240691"></a>

```c
#define ESP32_PIN_OUT_MASK 0x3U
```

相关声明：[ESP32_PIN_OUT_MASK](#a0c806899f6fb854f50c3a88a40240691)。

<a id="r_ada547ab4673154f6645f8d262196bf54"></a>

```c
#define ESP32_PIN_EN_DIR_SHIFT 6U
```

相关声明：[ESP32_PIN_EN_DIR_SHIFT](#ada547ab4673154f6645f8d262196bf54)。

<a id="r_a8941e50a06706315fcddfd327f10e7f2"></a>

```c
#define ESP32_PIN_EN_DIR_MASK 0x3U
```

相关声明：[ESP32_PIN_EN_DIR_MASK](#a8941e50a06706315fcddfd327f10e7f2)。

<a id="r_a5c86d31f9a9b04547a38da127bbde794"></a>

```c
#define ESP32_PIN_SLEEP_HOLD_SHIFT 8U
```

相关声明：[ESP32_PIN_SLEEP_HOLD_SHIFT](#a5c86d31f9a9b04547a38da127bbde794)。

休眠保持位（Sleep Hold Bit）。

<a id="r_a452691a1d8588110a8777c9da37245c6"></a>

```c
#define ESP32_PIN_SLEEP_HOLD_MASK 0x1U
```

相关声明：[ESP32_PIN_SLEEP_HOLD_MASK](#a452691a1d8588110a8777c9da37245c6)。

休眠保持掩码（Sleep Hold Mask）。

<a id="define-members-2"></a>

### ESP32 引脚偏置配置值（Pin Bias Configuration Values）

<a id="r_a843a0a112fd4aedae1620f0f0f02905c"></a>

```c
#define ESP32_NO_PULL 0x1
```

相关声明：[ESP32_NO_PULL](#a843a0a112fd4aedae1620f0f0f02905c)。

<a id="r_a13dba444526c095aa0a49dce05b1c161"></a>

```c
#define ESP32_PULL_UP 0x2
```

相关声明：[ESP32_PULL_UP](#a13dba444526c095aa0a49dce05b1c161)。

<a id="r_a5b49098dcea17780e9a9aedcd28ca562"></a>

```c
#define ESP32_PULL_DOWN 0x3
```

相关声明：[ESP32_PULL_DOWN](#a5b49098dcea17780e9a9aedcd28ca562)。

<a id="define-members-3"></a>

### ESP32 引脚驱动配置值（Pin Drive Configuration Values）

<a id="r_a02095f7bdbede933c2cb8990cd998570"></a>

```c
#define ESP32_PUSH_PULL 0x1
```

相关声明：[ESP32_PUSH_PULL](#a02095f7bdbede933c2cb8990cd998570)。

<a id="r_a567b521d9f62935c1d608941224eb4b0"></a>

```c
#define ESP32_OPEN_DRAIN 0x2
```

相关声明：[ESP32_OPEN_DRAIN](#a567b521d9f62935c1d608941224eb4b0)。

<a id="define-members-4"></a>

### ESP32 引脚输出电平值（Pin Output Level Values）

<a id="r_a387522c15cab88fb55679561b6c23afe"></a>

```c
#define ESP32_PIN_OUT_HIGH 0x1
```

相关声明：[ESP32_PIN_OUT_HIGH](#a387522c15cab88fb55679561b6c23afe)。

<a id="r_acedc77d7c4c6f60dc7e532045ea51702"></a>

```c
#define ESP32_PIN_OUT_LOW 0x2
```

相关声明：[ESP32_PIN_OUT_LOW](#acedc77d7c4c6f60dc7e532045ea51702)。

<a id="define-members-5"></a>

### ESP32 输入／输出使能覆盖值（Input/Output Enable Override Values）

<a id="r_a8678e26aae080bf67117515bac2256bc"></a>

```c
#define ESP32_PIN_OUT_EN 0x1
```

相关声明：[ESP32_PIN_OUT_EN](#a8678e26aae080bf67117515bac2256bc)。

<a id="r_a173eddf7263f3323721d71c287cffced"></a>

```c
#define ESP32_PIN_IN_EN 0x2
```

相关声明：[ESP32_PIN_IN_EN](#a173eddf7263f3323721d71c287cffced)。

<a id="define-members-6"></a>

### ESP32 休眠保持配置（Sleep Hold Configuration）

<a id="r_a833e2e7f7325e35392d632ce8fd4b5c0"></a>

```c
#define ESP32_PIN_SLEEP_HOLD_EN 0x1
```

相关声明：[ESP32_PIN_SLEEP_HOLD_EN](#a833e2e7f7325e35392d632ce8fd4b5c0)。

休眠保持使能（Sleep Hold Enable）。

<a id="define-members-7"></a>

### ESP32 引脚控制内部标志（Pinctrl Internal Flags）

ESP32 引脚控制驱动（Pinctrl Driver）使用的内部标志（Internal Flags）。

这些标志从引脚配置位字段（Pin Configuration Bit Field）派生，控制 GPIO 驱动行为。

<a id="r_a8bb1e084e133c0ac847cd909e554d0dc"></a>

```c
#define ESP32_NO_PULL_FLAG BIT(0)
```

相关声明：[ESP32_NO_PULL_FLAG](#a8bb1e084e133c0ac847cd909e554d0dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a56386d98e542dacf1a8495f87818245d"></a>

```c
#define ESP32_PULL_UP_FLAG BIT(1)
```

相关声明：[ESP32_PULL_UP_FLAG](#a56386d98e542dacf1a8495f87818245d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abbf4dd79f73d03949d23879f17957c68"></a>

```c
#define ESP32_PULL_DOWN_FLAG BIT(2)
```

相关声明：[ESP32_PULL_DOWN_FLAG](#abbf4dd79f73d03949d23879f17957c68)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a74692459ddf10cf6ad3025082c5938e1"></a>

```c
#define ESP32_PUSH_PULL_FLAG BIT(3)
```

相关声明：[ESP32_PUSH_PULL_FLAG](#a74692459ddf10cf6ad3025082c5938e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaa112a5822fa5277ffcecf2b6a8e867b"></a>

```c
#define ESP32_OPEN_DRAIN_FLAG BIT(4)
```

相关声明：[ESP32_OPEN_DRAIN_FLAG](#aaa112a5822fa5277ffcecf2b6a8e867b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4edea1a8b44a94e4ddaa824d9ed386ac"></a>

```c
#define ESP32_DIR_INP_FLAG BIT(5)
```

相关声明：[ESP32_DIR_INP_FLAG](#a4edea1a8b44a94e4ddaa824d9ed386ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a963fadb9794622bc4ad325d7033b0aa8"></a>

```c
#define ESP32_DIR_OUT_FLAG BIT(6)
```

相关声明：[ESP32_DIR_OUT_FLAG](#a963fadb9794622bc4ad325d7033b0aa8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a05728ca8ec232cc7c681e7b8fc60250a"></a>

```c
#define ESP32_PIN_OUT_HIGH_FLAG BIT(7)
```

相关声明：[ESP32_PIN_OUT_HIGH_FLAG](#a05728ca8ec232cc7c681e7b8fc60250a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac5bc7889673a30b546c4c2044f71fc68"></a>

```c
#define ESP32_PIN_OUT_LOW_FLAG BIT(8)
```

相关声明：[ESP32_PIN_OUT_LOW_FLAG](#ac5bc7889673a30b546c4c2044f71fc68)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a427e8a8be0caa57aa81879f0fcb965c6"></a>

```c
#define ESP32_PIN_OUT_EN_FLAG BIT(9)
```

相关声明：[ESP32_PIN_OUT_EN_FLAG](#a427e8a8be0caa57aa81879f0fcb965c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a314dc3e3e178119062625bbcc1601caf"></a>

```c
#define ESP32_PIN_IN_EN_FLAG BIT(10)
```

相关声明：[ESP32_PIN_IN_EN_FLAG](#a314dc3e3e178119062625bbcc1601caf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa52465f9bc52e3b93fb81036b8d620b7"></a>

```c
#define ESP32_SLEEP_HOLD_FLAG BIT(11)
```

相关声明：[ESP32_SLEEP_HOLD_FLAG](#aa52465f9bc52e3b93fb81036b8d620b7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

休眠保持使能位（Sleep Hold Enable Bit）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a4edea1a8b44a94e4ddaa824d9ed386ac"></a>

### `ESP32_DIR_INP_FLAG`

```c
#define ESP32_DIR_INP_FLAG BIT(5)
```

<a id="a963fadb9794622bc4ad325d7033b0aa8"></a>

### `ESP32_DIR_OUT_FLAG`

```c
#define ESP32_DIR_OUT_FLAG BIT(6)
```

<a id="a843a0a112fd4aedae1620f0f0f02905c"></a>

### `ESP32_NO_PULL`

```c
#define ESP32_NO_PULL 0x1
```

<a id="a8bb1e084e133c0ac847cd909e554d0dc"></a>

### `ESP32_NO_PULL_FLAG`

```c
#define ESP32_NO_PULL_FLAG BIT(0)
```

<a id="a567b521d9f62935c1d608941224eb4b0"></a>

### `ESP32_OPEN_DRAIN`

```c
#define ESP32_OPEN_DRAIN 0x2
```

<a id="aaa112a5822fa5277ffcecf2b6a8e867b"></a>

### `ESP32_OPEN_DRAIN_FLAG`

```c
#define ESP32_OPEN_DRAIN_FLAG BIT(4)
```

<a id="a65d2b03b1a813cb4d2921c7cc8deec79"></a>

### `ESP32_PIN_BIAS_MASK`

```c
#define ESP32_PIN_BIAS_MASK 0x3U
```

<a id="a47498f4ba429ddaedc5b2547888bfa00"></a>

### `ESP32_PIN_BIAS_SHIFT`

```c
#define ESP32_PIN_BIAS_SHIFT 0U
```

<a id="a4d05215be796ff091633a5f0de2a6748"></a>

### `ESP32_PIN_DRV_MASK`

```c
#define ESP32_PIN_DRV_MASK 0x3U
```

<a id="abfdf0aa9a8a5116f3ca66e54e72552ac"></a>

### `ESP32_PIN_DRV_SHIFT`

```c
#define ESP32_PIN_DRV_SHIFT 2U
```

<a id="a8941e50a06706315fcddfd327f10e7f2"></a>

### `ESP32_PIN_EN_DIR_MASK`

```c
#define ESP32_PIN_EN_DIR_MASK 0x3U
```

<a id="ada547ab4673154f6645f8d262196bf54"></a>

### `ESP32_PIN_EN_DIR_SHIFT`

```c
#define ESP32_PIN_EN_DIR_SHIFT 6U
```

<a id="a173eddf7263f3323721d71c287cffced"></a>

### `ESP32_PIN_IN_EN`

```c
#define ESP32_PIN_IN_EN 0x2
```

<a id="a314dc3e3e178119062625bbcc1601caf"></a>

### `ESP32_PIN_IN_EN_FLAG`

```c
#define ESP32_PIN_IN_EN_FLAG BIT(10)
```

<a id="aff8c7306c9eb06955c069a08700b9602"></a>

### `ESP32_PIN_NUM_MASK`

```c
#define ESP32_PIN_NUM_MASK 0x3FU
```

<a id="a14b1575596d4a3c7f349e140a206e7fc"></a>

### `ESP32_PIN_NUM_SHIFT`

```c
#define ESP32_PIN_NUM_SHIFT 0U
```

GPIO 引脚编号字段（Pin Number Field）。

<a id="a8678e26aae080bf67117515bac2256bc"></a>

### `ESP32_PIN_OUT_EN`

```c
#define ESP32_PIN_OUT_EN 0x1
```

<a id="a427e8a8be0caa57aa81879f0fcb965c6"></a>

### `ESP32_PIN_OUT_EN_FLAG`

```c
#define ESP32_PIN_OUT_EN_FLAG BIT(9)
```

<a id="a387522c15cab88fb55679561b6c23afe"></a>

### `ESP32_PIN_OUT_HIGH`

```c
#define ESP32_PIN_OUT_HIGH 0x1
```

<a id="a05728ca8ec232cc7c681e7b8fc60250a"></a>

### `ESP32_PIN_OUT_HIGH_FLAG`

```c
#define ESP32_PIN_OUT_HIGH_FLAG BIT(7)
```

<a id="acedc77d7c4c6f60dc7e532045ea51702"></a>

### `ESP32_PIN_OUT_LOW`

```c
#define ESP32_PIN_OUT_LOW 0x2
```

<a id="ac5bc7889673a30b546c4c2044f71fc68"></a>

### `ESP32_PIN_OUT_LOW_FLAG`

```c
#define ESP32_PIN_OUT_LOW_FLAG BIT(8)
```

<a id="a0c806899f6fb854f50c3a88a40240691"></a>

### `ESP32_PIN_OUT_MASK`

```c
#define ESP32_PIN_OUT_MASK 0x3U
```

<a id="af20225f7ed095e083c3b7a2fa55a5313"></a>

### `ESP32_PIN_OUT_SHIFT`

```c
#define ESP32_PIN_OUT_SHIFT 4U
```

<a id="a0069fd5363ff598a903823729ac7b785"></a>

### `ESP32_PIN_SIGI_MASK`

```c
#define ESP32_PIN_SIGI_MASK 0x1FFU
```

用于提取 I/O 信号索引（Signal Indexes）的定义。

这些字段编码 GPIO 矩阵信号路由机制（GPIO Matrix Signal Routing Mechanism），允许把内部外设信号连接到 GPIO 引脚。

<a id="a457b5af6f423f5d743b81317f331f175"></a>

### `ESP32_PIN_SIGI_SHIFT`

```c
#define ESP32_PIN_SIGI_SHIFT 6U
```

<a id="a97e539c13c42cabdb31c53dba9573bb8"></a>

### `ESP32_PIN_SIGO_MASK`

```c
#define ESP32_PIN_SIGO_MASK 0x1FFU
```

<a id="ab7b2f3303e89bb59c9fc0aec216678fd"></a>

### `ESP32_PIN_SIGO_SHIFT`

```c
#define ESP32_PIN_SIGO_SHIFT 15U
```

<a id="a833e2e7f7325e35392d632ce8fd4b5c0"></a>

### `ESP32_PIN_SLEEP_HOLD_EN`

```c
#define ESP32_PIN_SLEEP_HOLD_EN 0x1
```

休眠保持使能（Sleep Hold Enable）。

<a id="a452691a1d8588110a8777c9da37245c6"></a>

### `ESP32_PIN_SLEEP_HOLD_MASK`

```c
#define ESP32_PIN_SLEEP_HOLD_MASK 0x1U
```

休眠保持掩码（Sleep Hold Mask）。

<a id="a5c86d31f9a9b04547a38da127bbde794"></a>

### `ESP32_PIN_SLEEP_HOLD_SHIFT`

```c
#define ESP32_PIN_SLEEP_HOLD_SHIFT 8U
```

休眠保持位（Sleep Hold Bit）。

<a id="a932ca0617135c66cc96fba696ac06e7e"></a>

### `ESP32_PINMUX`

```c
#define ESP32_PINMUX ( pin, sig_i, sig_o )
```

展开值（Value）：

```c
(((pin & ESP32_PIN_NUM_MASK) << ESP32_PIN_NUM_SHIFT) |                                     \
 ((sig_i & ESP32_PIN_SIGI_MASK) << ESP32_PIN_SIGI_SHIFT) |                                 \
 ((sig_o & ESP32_PIN_SIGO_MASK) << ESP32_PIN_SIGO_SHIFT))
```

根据引脚编号及 GPIO 矩阵信号（GPIO Matrix Signals）构建 ESP32 引脚复用值（Pinmux Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | GPIO引脚编号。 |
| `sig_i` | 输入信号索引（Input Signal Index） |
| `sig_o` | 输出信号索引（Output Signal Index） |

<a id="a5b49098dcea17780e9a9aedcd28ca562"></a>

### `ESP32_PULL_DOWN`

```c
#define ESP32_PULL_DOWN 0x3
```

<a id="abbf4dd79f73d03949d23879f17957c68"></a>

### `ESP32_PULL_DOWN_FLAG`

```c
#define ESP32_PULL_DOWN_FLAG BIT(2)
```

<a id="a13dba444526c095aa0a49dce05b1c161"></a>

### `ESP32_PULL_UP`

```c
#define ESP32_PULL_UP 0x2
```

<a id="a56386d98e542dacf1a8495f87818245d"></a>

### `ESP32_PULL_UP_FLAG`

```c
#define ESP32_PULL_UP_FLAG BIT(1)
```

<a id="a02095f7bdbede933c2cb8990cd998570"></a>

### `ESP32_PUSH_PULL`

```c
#define ESP32_PUSH_PULL 0x1
```

<a id="a74692459ddf10cf6ad3025082c5938e1"></a>

### `ESP32_PUSH_PULL_FLAG`

```c
#define ESP32_PUSH_PULL_FLAG BIT(3)
```

<a id="af4ce081c5ff7fa1521443b4d1fe9a8f0"></a>

### `ESP32_RMII_MARKER`

```c
#define ESP32_RMII_MARKER BIT(30)
```

将一个单元（Cell）标记为 RMII 引脚复用（Pinmux）。

<a id="a3d10ffea4cfc02a4694cb879a034b886"></a>

### `ESP32_RMII_PINMUX`

```c
#define ESP32_RMII_PINMUX ( pin, slot )
```

展开值（Value）：

```c
(ESP32_RMII_MARKER | (((slot) & ESP32_RMII_SLOT_MASK) << ESP32_RMII_SLOT_SHIFT) |          \
 (((pin) & ESP32_PIN_NUM_MASK) << ESP32_PIN_NUM_SHIFT))
```

构建以太网 RMII 引脚复用值（Pinmux Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | GPIO引脚编号。 |
| `slot` | RMII 信号槽位（Signal Slot，ESP_RMII_*） |

<a id="a0550ba7d14ee1488fd60e2345ee01756"></a>

### `ESP32_RMII_SLOT_MASK`

```c
#define ESP32_RMII_SLOT_MASK 0xFU
```

RMII 信号槽位字段掩码（Signal Slot Field Mask）。

<a id="ab397163b12f1539ab42faec88ad63ef2"></a>

### `ESP32_RMII_SLOT_SHIFT`

```c
#define ESP32_RMII_SLOT_SHIFT 24U
```

以太网 RMII 引脚编码（Pin Encoding）。

RMII 焊盘（Pads）使用专用 EMAC IOMUX 功能，而非 GPIO 矩阵，因此不能使用 ESP32_PINMUX() 编码。RMII 单元（Cell）仅携带信号槽位和 GPIO 编号，由以太网驱动解析并应用 IOMUX 功能。ESP32_RMII_MARKER 位区分此类单元与 ESP32_PINMUX() 单元。RMII 信号槽位字段移位量（Signal Slot Field Shift）。

<a id="aa52465f9bc52e3b93fb81036b8d620b7"></a>

### `ESP32_SLEEP_HOLD_FLAG`

```c
#define ESP32_SLEEP_HOLD_FLAG BIT(11)
```

休眠保持使能位（Sleep Hold Enable Bit）。

<a id="a05b408148518137228c814967ae1bd05"></a>

### `ESP_RMII_CLK`

```c
#define ESP_RMII_CLK 0
```

RMII 参考时钟（Reference Clock）。

<a id="ab018a7ca7dc9c30ab2b229e020fad1db"></a>

### `ESP_RMII_CRS_DV`

```c
#define ESP_RMII_CRS_DV 4
```

RMII 载波侦听／数据有效（Carrier Sense / Data Valid）。

<a id="aeea7819bdae58e8c5824a506c081308d"></a>

### `ESP_RMII_RXD0`

```c
#define ESP_RMII_RXD0 5
```

RMII 接收数据 0（Receive Data 0）。

<a id="a584740b275282125d939c3e4e2879088"></a>

### `ESP_RMII_RXD1`

```c
#define ESP_RMII_RXD1 6
```

RMII 接收数据 1（Receive Data 1）。

<a id="a53dc181757ceb98c3c016dda67ec84db"></a>

### `ESP_RMII_SLOT_COUNT`

```c
#define ESP_RMII_SLOT_COUNT 7
```

上述 ESP_RMII_* 信号槽位（Signal Slots）的数量。

<a id="afdd83fa40a18fd541850e560c0c267bd"></a>

### `ESP_RMII_TX_EN`

```c
#define ESP_RMII_TX_EN 1
```

RMII 发送使能（Transmit Enable）。

<a id="ae74823edbeb6ef6fd0ed31fa84bfcde8"></a>

### `ESP_RMII_TXD0`

```c
#define ESP_RMII_TXD0 2
```

RMII 发送数据 0（Transmit Data 0）。

<a id="a50855f7d38e6fa343c4e7e7bc2e58bb7"></a>

### `ESP_RMII_TXD1`

```c
#define ESP_RMII_TXD1 3
```

RMII 发送数据 1（Transmit Data 1）。

<a id="ae0d2e726ab8d90343e5c80e1d9b85ad8"></a>

### `ESP_SIG_INVAL`

```c
#define ESP_SIG_INVAL ESP32_PIN_SIGI_MASK
```


## 7.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P235_esp-pinctrl-common.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aesp-pinctrl-common_8h_html_a0069fd5363ff598a903823729ac7b785"></a>
<a id="aesp-pinctrl-common_8h_html_a14b1575596d4a3c7f349e140a206e7fc"></a>
<a id="aesp-pinctrl-common_8h_html_a457b5af6f423f5d743b81317f331f175"></a>
<a id="aesp-pinctrl-common_8h_html_a97e539c13c42cabdb31c53dba9573bb8"></a>
<a id="aesp-pinctrl-common_8h_html_ab7b2f3303e89bb59c9fc0aec216678fd"></a>
<a id="aesp-pinctrl-common_8h_html_aff8c7306c9eb06955c069a08700b9602"></a>
<a id="aesp-pinctrl-common_8h_html_a0550ba7d14ee1488fd60e2345ee01756"></a>
<a id="aesp-pinctrl-common_8h_html_ab397163b12f1539ab42faec88ad63ef2"></a>
<a id="aesp-pinctrl-common_8h_html_af4ce081c5ff7fa1521443b4d1fe9a8f0"></a>

---

[上一章](P006_zephyr__net__dns_resolve.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dt-bindings__clock__esp32c5_clock.h_文件参考.md)
