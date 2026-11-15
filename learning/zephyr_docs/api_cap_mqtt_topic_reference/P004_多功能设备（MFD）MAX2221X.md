---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-4
title: 多功能设备（MFD）MAX2221X
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__max2221x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_多功能设备（MFD）MAX2221X

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__max2221x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_max2221x_2Eh"></a>

```c
file max2221x.h
```

相关声明：[max2221x.h](../api_file_power_ots_reference/P002_zephyr__drivers__mfd__max2221x.h_文件参考.md)。

MAX2221X多功能设备（MFD）驱动的公共API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga9850df3217df58783c6538a3fb46ea6a"></a>

```c
#define MAX2221X_NUM_CHANNELS 4
```

相关声明：[MAX2221X_NUM_CHANNELS](#ga9850df3217df58783c6538a3fb46ea6a)。

MAX2221X 通道数量（Number of Channels）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga18675d06cfed3daef49f22b4ee5df5c9"></a>

```c
int max2221x_reg_read (const struct device *dev, uint8_t addr, uint16_t *value)
```

相关声明：[max2221x_reg_read](#ga18675d06cfed3daef49f22b4ee5df5c9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 的寄存器（Register）。

<a id="r_gaf1eb751764b13b03e6ef732621baf942"></a>

```c
int max2221x_reg_write (const struct device *dev, uint8_t addr, uint16_t value)
```

相关声明：[max2221x_reg_write](#gaf1eb751764b13b03e6ef732621baf942)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

写入 MAX2221X 的寄存器（Register）。

<a id="r_gaa79d4e3e8f43e88872db2a8bd100707e"></a>

```c
int max2221x_reg_update (const struct device *dev, uint8_t addr, uint16_t mask, uint16_t val)
```

相关声明：[max2221x_reg_update](#gaa79d4e3e8f43e88872db2a8bd100707e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新 MAX2221X 的寄存器（Register）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.4\_MAX2221X SPI事务字段（MAX2221X SPI Transaction Fields）

<a id="r_gaedd5316c50cabb422e47927e2c9c1039"></a>

```c
#define MAX2221X_SPI_TRANS_ADDR GENMASK(6, 0)
```

相关声明：[MAX2221X_SPI_TRANS_ADDR](#gaedd5316c50cabb422e47927e2c9c1039)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

SPI 事务寄存器地址字段掩码（Register Address Field Mask）。

<a id="r_ga08bc444215b31d90f1128c0736f6f21a"></a>

```c
#define MAX2221X_SPI_TRANS_DIR BIT(7)
```

相关声明：[MAX2221X_SPI_TRANS_DIR](#ga08bc444215b31d90f1128c0736f6f21a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SPI 事务读／写方向位（Read/Write Direction Bit）。

## 4.5\_MAX2221X寄存器地址（MAX2221X Register Addresses）

<a id="r_ga1ef3d73859f871fd44a6583312083752"></a>

```c
#define MAX2221X_REG_GLOBAL_CTRL 0x00
```

相关声明：[MAX2221X_REG_GLOBAL_CTRL](#ga1ef3d73859f871fd44a6583312083752)。

全局控制寄存器地址（Global Control Register Address）。

<a id="r_ga6ea173e70a91aac91069096f9ab746ed"></a>

```c
#define MAX2221X_REG_GLOBAL_CFG 0x01
```

相关声明：[MAX2221X_REG_GLOBAL_CFG](#ga6ea173e70a91aac91069096f9ab746ed)。

全局配置寄存器地址（Global Configuration Register Address）。

<a id="r_gab3e7e855f98d2c6a4f80e12326aba8ca"></a>

```c
#define MAX2221X_REG_STATUS 0x02
```

相关声明：[MAX2221X_REG_STATUS](#gab3e7e855f98d2c6a4f80e12326aba8ca)。

状态寄存器地址（Status Register Address）。

<a id="r_ga072c147f6c0f7a9a179a3a3f67afc3bd"></a>

```c
#define MAX2221X_REG_DC_H2L 0x03
```

相关声明：[MAX2221X_REG_DC_H2L](#ga072c147f6c0f7a9a179a3a3f67afc3bd)。

退磁占空比由高到低寄存器地址（Demagnetization Duty Cycle High-to-Low Register Address）。

<a id="r_ga0c092ca1da2d34768fe63abf208d59cb"></a>

```c
#define MAX2221X_REG_VM_MONITOR 0x05
```

相关声明：[MAX2221X_REG_VM_MONITOR](#ga0c092ca1da2d34768fe63abf208d59cb)。

电压监视寄存器地址（Voltage Monitor Register Address）。

<a id="r_gab40470b5fb432dde27208f3233ab727b"></a>

```c
#define MAX2221X_REG_VM_THRESHOLD 0x06
```

相关声明：[MAX2221X_REG_VM_THRESHOLD](#gab40470b5fb432dde27208f3233ab727b)。

电压监视阈值寄存器地址（Voltage Monitor Threshold Register Address）。

<a id="r_gabc173632479d896452cd7f3b749c5848"></a>

```c
#define MAX2221X_REG_CFG_DC_L2H(x)
```

相关声明：[MAX2221X_REG_CFG_DC_L2H](#gabc173632479d896452cd7f3b749c5848)。

通道占空比由低到高配置寄存器地址（Channel Duty Cycle Low-to-High Configuration Register Address）。

<a id="r_ga46a038e5a2c9e9d294c143e2c1eff33a"></a>

```c
#define MAX2221X_REG_CFG_DC_H(x)
```

相关声明：[MAX2221X_REG_CFG_DC_H](#ga46a038e5a2c9e9d294c143e2c1eff33a)。

通道高占空比配置寄存器地址（Channel Duty Cycle High Configuration Register Address）。

<a id="r_gaf19fb778adfe9e8794c1ee14058856f3"></a>

```c
#define MAX2221X_REG_CFG_DC_L(x)
```

相关声明：[MAX2221X_REG_CFG_DC_L](#gaf19fb778adfe9e8794c1ee14058856f3)。

通道低占空比配置寄存器地址（Channel Duty Cycle Low Configuration Register Address）。

<a id="r_ga2980e35f7958ab77dc97411f53bccde8"></a>

```c
#define MAX2221X_REG_CFG_TIME_L2H(x)
```

相关声明：[MAX2221X_REG_CFG_TIME_L2H](#ga2980e35f7958ab77dc97411f53bccde8)。

通道由低到高时间配置寄存器地址（Channel Time Low-to-High Configuration Register Address）。

<a id="r_ga119fe235e2dddb4e044b51e14e305e47"></a>

```c
#define MAX2221X_REG_CFG_CTRL0(x)
```

相关声明：[MAX2221X_REG_CFG_CTRL0](#ga119fe235e2dddb4e044b51e14e305e47)。

通道控制 0 配置寄存器地址（Channel Control 0 Configuration Register Address）。

<a id="r_ga5d21beb99b3647ae9a367b62681e8108"></a>

```c
#define MAX2221X_REG_CFG_CTRL1(x)
```

相关声明：[MAX2221X_REG_CFG_CTRL1](#ga5d21beb99b3647ae9a367b62681e8108)。

通道控制 1 配置寄存器地址（Channel Control 1 Configuration Register Address）。

<a id="r_ga7ba68b3a283ecaaac443714b4ab0b1ec"></a>

```c
#define MAX2221X_REG_PWM_DUTY(x)
```

相关声明：[MAX2221X_REG_PWM_DUTY](#ga7ba68b3a283ecaaac443714b4ab0b1ec)。

通道 PWM 占空比寄存器地址（Channel PWM Duty Cycle Register Address）。

<a id="r_gae311958c9f915b18592aeeaecc5e4ccf"></a>

```c
#define MAX2221X_REG_FAULT0 0x65
```

相关声明：[MAX2221X_REG_FAULT0](#gae311958c9f915b18592aeeaecc5e4ccf)。

故障 0 寄存器地址（Fault 0 Register Address）。

<a id="r_ga5fd1b8fd8cdc680ba9e11417384c1e4a"></a>

```c
#define MAX2221X_REG_FAULT1 0x66
```

相关声明：[MAX2221X_REG_FAULT1](#ga5fd1b8fd8cdc680ba9e11417384c1e4a)。

故障 1 寄存器地址（Fault 1 Register Address）。

## 4.6\_MAX2221X全局配置掩码（MAX2221X Global Configuration Masks）

<a id="r_ga760fd1ea1c372081cac24f4c9f80f39f"></a>

```c
#define MAX2221X_F_PWM_M_MASK GENMASK(7, 4)
```

相关声明：[MAX2221X_F_PWM_M_MASK](#ga760fd1ea1c372081cac24f4c9f80f39f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

全局配置寄存器中的主斩波频率掩码（Master Chopping Frequency Mask）。

<a id="r_ga66a1a1bca915b1c3f739cb70722204cb"></a>

```c
#define MAX2221X_CNTL0_MASK BIT(0)
```

相关声明：[MAX2221X_CNTL0_MASK](#ga66a1a1bca915b1c3f739cb70722204cb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 控制使能掩码（Control Enable Mask）。

<a id="r_gaa2f0279abca92b05b5d813f2a14fbca2"></a>

```c
#define MAX2221X_CNTL1_MASK BIT(1)
```

相关声明：[MAX2221X_CNTL1_MASK](#gaa2f0279abca92b05b5d813f2a14fbca2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 控制使能掩码（Control Enable Mask）。

<a id="r_ga71030b0ac70bd81fd029845a973f7e4a"></a>

```c
#define MAX2221X_CNTL2_MASK BIT(2)
```

相关声明：[MAX2221X_CNTL2_MASK](#ga71030b0ac70bd81fd029845a973f7e4a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 控制使能掩码（Control Enable Mask）。

<a id="r_gab3ea43fc79cc89d009fc00c4a4d3ebc2"></a>

```c
#define MAX2221X_CNTL3_MASK BIT(3)
```

相关声明：[MAX2221X_CNTL3_MASK](#gab3ea43fc79cc89d009fc00c4a4d3ebc2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 控制使能掩码（Control Enable Mask）。

## 4.7\_MAX2221X全局控制掩码（MAX2221X Global Control Masks）

<a id="r_ga00056c6a7408e9c4030449403f9c902c"></a>

```c
#define MAX2221X_ACTIVE_MASK BIT(15)
```

相关声明：[MAX2221X_ACTIVE_MASK](#ga00056c6a7408e9c4030449403f9c902c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

活动模式使能掩码（Active Mode Enable Mask）。

<a id="r_ga85b5d95fe89a571ddc83e43dffb08acf"></a>

```c
#define MAX2221X_M_UVM_MASK BIT(8)
```

相关声明：[MAX2221X_M_UVM_MASK](#ga85b5d95fe89a571ddc83e43dffb08acf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

欠压监视掩码（Under-Voltage Monitor Mask）。

<a id="r_gaec89bbd558f23064f678ff4c3a6632e8"></a>

```c
#define MAX2221X_VDRNVDRDUTY_MASK BIT(4)
```

相关声明：[MAX2221X_VDRNVDRDUTY_MASK](#gaec89bbd558f23064f678ff4c3a6632e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VDR／VDRDUTY 模式选择掩码（Mode Selection Mask）。

## 4.8\_MAX2221X状态寄存器掩码（MAX2221X Status Register Masks）

<a id="r_gae1c68ba7dbb6d88198fceed26e29e121"></a>

```c
#define MAX2221X_STATUS_STT3_MASK BIT(14)
```

相关声明：[MAX2221X_STATUS_STT3_MASK](#gae1c68ba7dbb6d88198fceed26e29e121)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

状态位 3 的掩码（Status Bit Mask）。

<a id="r_ga7db46819804b9a3f3d80e4037f1c906d"></a>

```c
#define MAX2221X_STATUS_STT2_MASK BIT(13)
```

相关声明：[MAX2221X_STATUS_STT2_MASK](#ga7db46819804b9a3f3d80e4037f1c906d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

状态位 2 的掩码（Status Bit Mask）。

<a id="r_gacf4c8532880ce7ab67b72938dba527b3"></a>

```c
#define MAX2221X_STATUS_STT1_MASK BIT(12)
```

相关声明：[MAX2221X_STATUS_STT1_MASK](#gacf4c8532880ce7ab67b72938dba527b3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

状态位 1 的掩码（Status Bit Mask）。

<a id="r_gae9bcaf9188d9b19d77491bd3fa9b773f"></a>

```c
#define MAX2221X_STATUS_STT0_MASK BIT(11)
```

相关声明：[MAX2221X_STATUS_STT0_MASK](#gae9bcaf9188d9b19d77491bd3fa9b773f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

状态位 0 的掩码（Status Bit Mask）。

<a id="r_gaab816d44a3cc2b7d9d93a3aa9ec2218f"></a>

```c
#define MAX2221X_STATUS_MIN_T_ON_MASK BIT(10)
```

相关声明：[MAX2221X_STATUS_MIN_T_ON_MASK](#gaab816d44a3cc2b7d9d93a3aa9ec2218f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

最小导通时间故障状态掩码（Minimum On-Time Fault Status Mask）。

<a id="r_ga3cead261bb81ad06b1af7b1c35644da8"></a>

```c
#define MAX2221X_STATUS_RES_MASK BIT(9)
```

相关声明：[MAX2221X_STATUS_RES_MASK](#ga3cead261bb81ad06b1af7b1c35644da8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电阻测量状态掩码（Resistance Measurement Status Mask）。

<a id="r_ga838ba035e998eb39c9ff8f6a473bd264"></a>

```c
#define MAX2221X_STATUS_IND_MASK BIT(8)
```

相关声明：[MAX2221X_STATUS_IND_MASK](#ga838ba035e998eb39c9ff8f6a473bd264)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电感测量状态掩码（Inductance Measurement Status Mask）。

<a id="r_ga41c3dd5472f9a6902d48a66245f136b8"></a>

```c
#define MAX2221X_STATUS_OVT_MASK BIT(7)
```

相关声明：[MAX2221X_STATUS_OVT_MASK](#ga41c3dd5472f9a6902d48a66245f136b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

过温故障状态掩码（Over-Temperature Fault Status Mask）。

<a id="r_ga5632d8b38de2c3b68a816d41ca45d77f"></a>

```c
#define MAX2221X_STATUS_OCP_MASK BIT(6)
```

相关声明：[MAX2221X_STATUS_OCP_MASK](#ga5632d8b38de2c3b68a816d41ca45d77f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

过流保护故障状态掩码（Over-Current Protection Fault Status Mask）。

<a id="r_ga77aa2ecaabe17104d418e040c1067e71"></a>

```c
#define MAX2221X_STATUS_OLF_MASK BIT(5)
```

相关声明：[MAX2221X_STATUS_OLF_MASK](#ga77aa2ecaabe17104d418e040c1067e71)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

开路负载故障状态掩码（Open-Load Fault Status Mask）。

<a id="r_ga58646784ba7aea973c9253394095c63c"></a>

```c
#define MAX2221X_STATUS_HHF_MASK BIT(4)
```

相关声明：[MAX2221X_STATUS_HHF_MASK](#ga58646784ba7aea973c9253394095c63c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

未达到吸合电流故障状态掩码（Hit Current Not Reached Fault Status Mask）。

<a id="r_gaba0107d7195f03ac4150416f09b6c739"></a>

```c
#define MAX2221X_STATUS_DPM_MASK BIT(3)
```

相关声明：[MAX2221X_STATUS_DPM_MASK](#gaba0107d7195f03ac4150416f09b6c739)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

DPM 错误故障状态掩码（DPM Error Fault Status Mask）。

<a id="r_ga040658a951cbc304d0c8a563938e3836"></a>

```c
#define MAX2221X_STATUS_COMER_MASK BIT(2)
```

相关声明：[MAX2221X_STATUS_COMER_MASK](#ga040658a951cbc304d0c8a563938e3836)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通信错误故障状态掩码（Communication Error Fault Status Mask）。

<a id="r_gac9f0cfb941c55888bd8785b846b27aba"></a>

```c
#define MAX2221X_STATUS_UVM_MASK BIT(1)
```

相关声明：[MAX2221X_STATUS_UVM_MASK](#gac9f0cfb941c55888bd8785b846b27aba)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

欠压监视故障状态掩码（Under-Voltage Monitor Fault Status Mask）。

## 4.9\_MAX2221X电压监视掩码（MAX2221X VM Monitor Masks）

<a id="r_ga8a241d8e5a7530a624fed4603af1f352"></a>

```c
#define MAX2221X_VM_MONITOR_MASK GENMASK(12, 0)
```

相关声明：[MAX2221X_VM_MONITOR_MASK](#ga8a241d8e5a7530a624fed4603af1f352)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压监视测量值掩码（Voltage Monitor Measurement Value Mask）。

## 4.10\_MAX2221X电压监视阈值掩码（MAX2221X VM Threshold Masks）

<a id="r_ga99d548ae7681c6d5b9e297679d594518"></a>

```c
#define MAX2221X_VM_THLD_UP_MASK GENMASK(7, 4)
```

相关声明：[MAX2221X_VM_THLD_UP_MASK](#ga99d548ae7681c6d5b9e297679d594518)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压监视上限阈值掩码（Upper Voltage Monitor Threshold Mask）。

<a id="r_ga41ab1fc286e224183a21904a68172dc9"></a>

```c
#define MAX2221X_VM_THLD_DOWN_MASK GENMASK(3, 0)
```

相关声明：[MAX2221X_VM_THLD_DOWN_MASK](#ga41ab1fc286e224183a21904a68172dc9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压监视下限阈值掩码（Lower Voltage Monitor Threshold Mask）。

## 4.11\_MAX2221X通道控制0掩码（MAX2221X Channel Control 0 Masks）

<a id="r_ga0b627dfbda552737e25cd6de9bd1bbbe"></a>

```c
#define MAX2221X_CTRL_MODE_MASK GENMASK(15, 14)
```

相关声明：[MAX2221X_CTRL_MODE_MASK](#ga0b627dfbda552737e25cd6de9bd1bbbe)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

控制模式选择掩码（Control Mode Selection Mask）。

<a id="r_ga776a504229c90e1fba219078ee6a31f8"></a>

```c
#define MAX2221X_RDWE_MASK BIT(10)
```

相关声明：[MAX2221X_RDWE_MASK](#ga776a504229c90e1fba219078ee6a31f8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

下降斜坡使能掩码（Ramp-down Enable Mask）。

<a id="r_ga7528406875c4d70cc1bc712d96b77eef"></a>

```c
#define MAX2221X_RMDE_MASK BIT(9)
```

相关声明：[MAX2221X_RMDE_MASK](#ga7528406875c4d70cc1bc712d96b77eef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

中间斜坡使能掩码（Ramp-middle Enable Mask）。

<a id="r_ga7eebb941c340887a56d0a05faf138c4e"></a>

```c
#define MAX2221X_RUPE_MASK BIT(8)
```

相关声明：[MAX2221X_RUPE_MASK](#ga7eebb941c340887a56d0a05faf138c4e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上升斜坡使能掩码（Ramp-up Enable Mask）。

<a id="r_ga4f3bc6647ecac99c3601c3d15e59b57f"></a>

```c
#define MAX2221X_RAMP_MASK GENMASK(7, 0)
```

相关声明：[MAX2221X_RAMP_MASK](#ga4f3bc6647ecac99c3601c3d15e59b57f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

斜坡变化率值掩码（Ramp Slew Rate Value Mask）。

## 4.12\_MAX2221X通道控制1掩码（MAX2221X Channel Control 1 Masks）

<a id="r_ga908330f1896dd68a843fe751e5ff9976"></a>

```c
#define MAX2221X_F_PWM_MASK GENMASK(9, 8)
```

相关声明：[MAX2221X_F_PWM_MASK](#ga908330f1896dd68a843fe751e5ff9976)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

通道斩波频率分频系数掩码（Channel Chopping Frequency Divisor Mask）。

<a id="r_ga484349100da619c9eda6abafd5a768e9"></a>

```c
#define MAX2221X_SLEW_RATE_MASK GENMASK(5, 4)
```

相关声明：[MAX2221X_SLEW_RATE_MASK](#ga484349100da619c9eda6abafd5a768e9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

输出转换速率选择掩码（Output Slew Rate Selection Mask）。

<a id="r_ga6b8216024653da81031e0205cc1e74c1"></a>

```c
#define MAX2221X_GAIN_MASK GENMASK(3, 2)
```

相关声明：[MAX2221X_GAIN_MASK](#ga6b8216024653da81031e0205cc1e74c1)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

数字增益选择掩码（Digital Gain Selection Mask）。

<a id="r_ga323fd84aa33f7dffc0ca0c4deeef2707"></a>

```c
#define MAX2221X_SNSF_MASK GENMASK(1, 0)
```

相关声明：[MAX2221X_SNSF_MASK](#ga323fd84aa33f7dffc0ca0c4deeef2707)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

检测缩放系数选择掩码（Sense Scaling Factor Selection Mask）。

## 4.13\_MAX2221X故障0寄存器掩码（MAX2221X Fault 0 Register Masks）

<a id="r_gaa6af3b799ba8824544151a95241bb12d"></a>

```c
#define MAX2221X_FAULT_DPM3_MASK BIT(15)
```

相关声明：[MAX2221X_FAULT_DPM3_MASK](#gaa6af3b799ba8824544151a95241bb12d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的DPM故障掩码（Fault Mask）。

<a id="r_gaea7bef2b3e16ee5f479482cfc80790f7"></a>

```c
#define MAX2221X_FAULT_DPM2_MASK BIT(14)
```

相关声明：[MAX2221X_FAULT_DPM2_MASK](#gaea7bef2b3e16ee5f479482cfc80790f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的DPM故障掩码（Fault Mask）。

<a id="r_gafbe38d0ce3360ee931d30ad94db196d0"></a>

```c
#define MAX2221X_FAULT_DPM1_MASK BIT(13)
```

相关声明：[MAX2221X_FAULT_DPM1_MASK](#gafbe38d0ce3360ee931d30ad94db196d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的DPM故障掩码（Fault Mask）。

<a id="r_ga7e458804af0c00525ef79ab3b864fa07"></a>

```c
#define MAX2221X_FAULT_DPM0_MASK BIT(12)
```

相关声明：[MAX2221X_FAULT_DPM0_MASK](#ga7e458804af0c00525ef79ab3b864fa07)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的DPM故障掩码（Fault Mask）。

<a id="r_ga6c1044ea58a009f30e4b1950444f97d3"></a>

```c
#define MAX2221X_FAULT_OLF3_MASK BIT(11)
```

相关声明：[MAX2221X_FAULT_OLF3_MASK](#ga6c1044ea58a009f30e4b1950444f97d3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="r_ga64cfcfcc438091438b30d5ca46cf69c1"></a>

```c
#define MAX2221X_FAULT_OLF2_MASK BIT(10)
```

相关声明：[MAX2221X_FAULT_OLF2_MASK](#ga64cfcfcc438091438b30d5ca46cf69c1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="r_gaf2672d3b8b402a633084d8d76aabe0e6"></a>

```c
#define MAX2221X_FAULT_OLF1_MASK BIT(9)
```

相关声明：[MAX2221X_FAULT_OLF1_MASK](#gaf2672d3b8b402a633084d8d76aabe0e6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="r_ga5a1625a41e29e081c8043c935bb0957e"></a>

```c
#define MAX2221X_FAULT_OLF0_MASK BIT(8)
```

相关声明：[MAX2221X_FAULT_OLF0_MASK](#ga5a1625a41e29e081c8043c935bb0957e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="r_gafde9561d6ca9df65d22b71352413cccb"></a>

```c
#define MAX2221X_FAULT_HHF3_MASK BIT(7)
```

相关声明：[MAX2221X_FAULT_HHF3_MASK](#gafde9561d6ca9df65d22b71352413cccb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="r_ga6e707daf78a9cfda737cdb212b109de6"></a>

```c
#define MAX2221X_FAULT_HHF2_MASK BIT(6)
```

相关声明：[MAX2221X_FAULT_HHF2_MASK](#ga6e707daf78a9cfda737cdb212b109de6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="r_ga5f10d7335f163772ae9665f6fd8232d6"></a>

```c
#define MAX2221X_FAULT_HHF1_MASK BIT(5)
```

相关声明：[MAX2221X_FAULT_HHF1_MASK](#ga5f10d7335f163772ae9665f6fd8232d6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="r_ga383f57398a9c623389071abb7e1c7e3e"></a>

```c
#define MAX2221X_FAULT_HHF0_MASK BIT(4)
```

相关声明：[MAX2221X_FAULT_HHF0_MASK](#ga383f57398a9c623389071abb7e1c7e3e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="r_gac5eda83f9551dcde84dc08b4c91a4987"></a>

```c
#define MAX2221X_FAULT_OCP3_MASK BIT(3)
```

相关声明：[MAX2221X_FAULT_OCP3_MASK](#gac5eda83f9551dcde84dc08b4c91a4987)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="r_ga2888752d3f3c3b03ff71acdfb9bbedc1"></a>

```c
#define MAX2221X_FAULT_OCP2_MASK BIT(2)
```

相关声明：[MAX2221X_FAULT_OCP2_MASK](#ga2888752d3f3c3b03ff71acdfb9bbedc1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="r_ga127f8c9caa18a90185a03e6e674dddfe"></a>

```c
#define MAX2221X_FAULT_OCP1_MASK BIT(1)
```

相关声明：[MAX2221X_FAULT_OCP1_MASK](#ga127f8c9caa18a90185a03e6e674dddfe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="r_ga991d4facb655d1a57e1fd6a476ba3a72"></a>

```c
#define MAX2221X_FAULT_OCP0_MASK BIT(0)
```

相关声明：[MAX2221X_FAULT_OCP0_MASK](#ga991d4facb655d1a57e1fd6a476ba3a72)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

## 4.14\_MAX2221X故障1寄存器掩码（MAX2221X Fault 1 Register Masks）

<a id="r_gadaea9ec689b2e095c923d55d43a0ebd3"></a>

```c
#define MAX2221X_FAULT_RES3_MASK BIT(10)
```

相关声明：[MAX2221X_FAULT_RES3_MASK](#gadaea9ec689b2e095c923d55d43a0ebd3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="r_ga7014a427898d3cda982244d14993197f"></a>

```c
#define MAX2221X_FAULT_RES2_MASK BIT(9)
```

相关声明：[MAX2221X_FAULT_RES2_MASK](#ga7014a427898d3cda982244d14993197f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="r_ga84008bbccb8debc97712d2757f73a8a1"></a>

```c
#define MAX2221X_FAULT_RES1_MASK BIT(8)
```

相关声明：[MAX2221X_FAULT_RES1_MASK](#ga84008bbccb8debc97712d2757f73a8a1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="r_ga5a9049970177e5e64a15928409209ac4"></a>

```c
#define MAX2221X_FAULT_RES0_MASK BIT(7)
```

相关声明：[MAX2221X_FAULT_RES0_MASK](#ga5a9049970177e5e64a15928409209ac4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="r_ga404f11e24e22b4b5150515c95e994aaf"></a>

```c
#define MAX2221X_FAULT_OVT_MASK BIT(6)
```

相关声明：[MAX2221X_FAULT_OVT_MASK](#ga404f11e24e22b4b5150515c95e994aaf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

过温故障掩码（Over-Temperature Fault Mask）。

<a id="r_gaab6ef388aeaffd7d14606ed5c85912d0"></a>

```c
#define MAX2221X_FAULT_COMER_MASK BIT(5)
```

相关声明：[MAX2221X_FAULT_COMER_MASK](#gaab6ef388aeaffd7d14606ed5c85912d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通信错误故障掩码（Communication Error Fault Mask）。

<a id="r_gabb5c0a375201ed650c293dff44d86df9"></a>

```c
#define MAX2221X_FAULT_UVM_MASK BIT(4)
```

相关声明：[MAX2221X_FAULT_UVM_MASK](#gabb5c0a375201ed650c293dff44d86df9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

欠压监视故障掩码（Under-Voltage Monitor Fault Mask）。

<a id="r_ga989c0f00dc24d9eb24bcac7ce59523a8"></a>

```c
#define MAX2221X_FAULT_IND3_MASK BIT(3)
```

相关声明：[MAX2221X_FAULT_IND3_MASK](#ga989c0f00dc24d9eb24bcac7ce59523a8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 3 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="r_gaa56c1c43f53dcdba8f96c9c2f001a7b0"></a>

```c
#define MAX2221X_FAULT_IND2_MASK BIT(2)
```

相关声明：[MAX2221X_FAULT_IND2_MASK](#gaa56c1c43f53dcdba8f96c9c2f001a7b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 2 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="r_gad15ccd7622c4aceff30fe8bbf444d5cf"></a>

```c
#define MAX2221X_FAULT_IND1_MASK BIT(1)
```

相关声明：[MAX2221X_FAULT_IND1_MASK](#gad15ccd7622c4aceff30fe8bbf444d5cf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 1 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="r_gabaeb9e6b869bc4ebd9c07109427934ae"></a>

```c
#define MAX2221X_FAULT_IND0_MASK BIT(0)
```

相关声明：[MAX2221X_FAULT_IND0_MASK](#gabaeb9e6b869bc4ebd9c07109427934ae)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通道 0 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

## 4.15\_详细说明（Detailed Documentation）

<a id="ga00056c6a7408e9c4030449403f9c902c"></a>

### `MAX2221X_ACTIVE_MASK`

```c
#define MAX2221X_ACTIVE_MASK BIT(15)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

活动模式使能掩码（Active Mode Enable Mask）。

<a id="ga66a1a1bca915b1c3f739cb70722204cb"></a>

### `MAX2221X_CNTL0_MASK`

```c
#define MAX2221X_CNTL0_MASK BIT(0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 控制使能掩码（Control Enable Mask）。

<a id="gaa2f0279abca92b05b5d813f2a14fbca2"></a>

### `MAX2221X_CNTL1_MASK`

```c
#define MAX2221X_CNTL1_MASK BIT(1)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 控制使能掩码（Control Enable Mask）。

<a id="ga71030b0ac70bd81fd029845a973f7e4a"></a>

### `MAX2221X_CNTL2_MASK`

```c
#define MAX2221X_CNTL2_MASK BIT(2)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 控制使能掩码（Control Enable Mask）。

<a id="gab3ea43fc79cc89d009fc00c4a4d3ebc2"></a>

### `MAX2221X_CNTL3_MASK`

```c
#define MAX2221X_CNTL3_MASK BIT(3)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 控制使能掩码（Control Enable Mask）。

<a id="ga0b627dfbda552737e25cd6de9bd1bbbe"></a>

### `MAX2221X_CTRL_MODE_MASK`

```c
#define MAX2221X_CTRL_MODE_MASK GENMASK(15, 14)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

控制模式选择掩码（Control Mode Selection Mask）。

<a id="ga760fd1ea1c372081cac24f4c9f80f39f"></a>

### `MAX2221X_F_PWM_M_MASK`

```c
#define MAX2221X_F_PWM_M_MASK GENMASK(7, 4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

全局配置寄存器中的主斩波频率掩码（Master Chopping Frequency Mask）。

<a id="ga908330f1896dd68a843fe751e5ff9976"></a>

### `MAX2221X_F_PWM_MASK`

```c
#define MAX2221X_F_PWM_MASK GENMASK(9, 8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道斩波频率分频系数掩码（Channel Chopping Frequency Divisor Mask）。

<a id="gaab6ef388aeaffd7d14606ed5c85912d0"></a>

### `MAX2221X_FAULT_COMER_MASK`

```c
#define MAX2221X_FAULT_COMER_MASK BIT(5)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通信错误故障掩码（Communication Error Fault Mask）。

<a id="ga7e458804af0c00525ef79ab3b864fa07"></a>

### `MAX2221X_FAULT_DPM0_MASK`

```c
#define MAX2221X_FAULT_DPM0_MASK BIT(12)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的DPM故障掩码（Fault Mask）。

<a id="gafbe38d0ce3360ee931d30ad94db196d0"></a>

### `MAX2221X_FAULT_DPM1_MASK`

```c
#define MAX2221X_FAULT_DPM1_MASK BIT(13)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的DPM故障掩码（Fault Mask）。

<a id="gaea7bef2b3e16ee5f479482cfc80790f7"></a>

### `MAX2221X_FAULT_DPM2_MASK`

```c
#define MAX2221X_FAULT_DPM2_MASK BIT(14)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的DPM故障掩码（Fault Mask）。

<a id="gaa6af3b799ba8824544151a95241bb12d"></a>

### `MAX2221X_FAULT_DPM3_MASK`

```c
#define MAX2221X_FAULT_DPM3_MASK BIT(15)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的DPM故障掩码（Fault Mask）。

<a id="ga383f57398a9c623389071abb7e1c7e3e"></a>

### `MAX2221X_FAULT_HHF0_MASK`

```c
#define MAX2221X_FAULT_HHF0_MASK BIT(4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="ga5f10d7335f163772ae9665f6fd8232d6"></a>

### `MAX2221X_FAULT_HHF1_MASK`

```c
#define MAX2221X_FAULT_HHF1_MASK BIT(5)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="ga6e707daf78a9cfda737cdb212b109de6"></a>

### `MAX2221X_FAULT_HHF2_MASK`

```c
#define MAX2221X_FAULT_HHF2_MASK BIT(6)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="gafde9561d6ca9df65d22b71352413cccb"></a>

### `MAX2221X_FAULT_HHF3_MASK`

```c
#define MAX2221X_FAULT_HHF3_MASK BIT(7)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的未达到吸合电流（Hit Current Not Reached）故障掩码（Fault Mask）。

<a id="gabaeb9e6b869bc4ebd9c07109427934ae"></a>

### `MAX2221X_FAULT_IND0_MASK`

```c
#define MAX2221X_FAULT_IND0_MASK BIT(0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="gad15ccd7622c4aceff30fe8bbf444d5cf"></a>

### `MAX2221X_FAULT_IND1_MASK`

```c
#define MAX2221X_FAULT_IND1_MASK BIT(1)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="gaa56c1c43f53dcdba8f96c9c2f001a7b0"></a>

### `MAX2221X_FAULT_IND2_MASK`

```c
#define MAX2221X_FAULT_IND2_MASK BIT(2)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="ga989c0f00dc24d9eb24bcac7ce59523a8"></a>

### `MAX2221X_FAULT_IND3_MASK`

```c
#define MAX2221X_FAULT_IND3_MASK BIT(3)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的电感测量（Inductance Measurement）故障掩码（Fault Mask）。

<a id="ga991d4facb655d1a57e1fd6a476ba3a72"></a>

### `MAX2221X_FAULT_OCP0_MASK`

```c
#define MAX2221X_FAULT_OCP0_MASK BIT(0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="ga127f8c9caa18a90185a03e6e674dddfe"></a>

### `MAX2221X_FAULT_OCP1_MASK`

```c
#define MAX2221X_FAULT_OCP1_MASK BIT(1)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="ga2888752d3f3c3b03ff71acdfb9bbedc1"></a>

### `MAX2221X_FAULT_OCP2_MASK`

```c
#define MAX2221X_FAULT_OCP2_MASK BIT(2)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="gac5eda83f9551dcde84dc08b4c91a4987"></a>

### `MAX2221X_FAULT_OCP3_MASK`

```c
#define MAX2221X_FAULT_OCP3_MASK BIT(3)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的过流保护（Over-Current Protection）故障掩码（Fault Mask）。

<a id="ga5a1625a41e29e081c8043c935bb0957e"></a>

### `MAX2221X_FAULT_OLF0_MASK`

```c
#define MAX2221X_FAULT_OLF0_MASK BIT(8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="gaf2672d3b8b402a633084d8d76aabe0e6"></a>

### `MAX2221X_FAULT_OLF1_MASK`

```c
#define MAX2221X_FAULT_OLF1_MASK BIT(9)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="ga64cfcfcc438091438b30d5ca46cf69c1"></a>

### `MAX2221X_FAULT_OLF2_MASK`

```c
#define MAX2221X_FAULT_OLF2_MASK BIT(10)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="ga6c1044ea58a009f30e4b1950444f97d3"></a>

### `MAX2221X_FAULT_OLF3_MASK`

```c
#define MAX2221X_FAULT_OLF3_MASK BIT(11)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的开路负载（Open-Load）故障掩码（Fault Mask）。

<a id="ga404f11e24e22b4b5150515c95e994aaf"></a>

### `MAX2221X_FAULT_OVT_MASK`

```c
#define MAX2221X_FAULT_OVT_MASK BIT(6)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

过温故障掩码（Over-Temperature Fault Mask）。

<a id="ga5a9049970177e5e64a15928409209ac4"></a>

### `MAX2221X_FAULT_RES0_MASK`

```c
#define MAX2221X_FAULT_RES0_MASK BIT(7)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 0 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="ga84008bbccb8debc97712d2757f73a8a1"></a>

### `MAX2221X_FAULT_RES1_MASK`

```c
#define MAX2221X_FAULT_RES1_MASK BIT(8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 1 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="ga7014a427898d3cda982244d14993197f"></a>

### `MAX2221X_FAULT_RES2_MASK`

```c
#define MAX2221X_FAULT_RES2_MASK BIT(9)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 2 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="gadaea9ec689b2e095c923d55d43a0ebd3"></a>

### `MAX2221X_FAULT_RES3_MASK`

```c
#define MAX2221X_FAULT_RES3_MASK BIT(10)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通道 3 的电阻测量（Resistance Measurement）故障掩码（Fault Mask）。

<a id="gabb5c0a375201ed650c293dff44d86df9"></a>

### `MAX2221X_FAULT_UVM_MASK`

```c
#define MAX2221X_FAULT_UVM_MASK BIT(4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

欠压监视故障掩码（Under-Voltage Monitor Fault Mask）。

<a id="ga6b8216024653da81031e0205cc1e74c1"></a>

### `MAX2221X_GAIN_MASK`

```c
#define MAX2221X_GAIN_MASK GENMASK(3, 2)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

数字增益选择掩码（Digital Gain Selection Mask）。

<a id="ga85b5d95fe89a571ddc83e43dffb08acf"></a>

### `MAX2221X_M_UVM_MASK`

```c
#define MAX2221X_M_UVM_MASK BIT(8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

欠压监视掩码（Under-Voltage Monitor Mask）。

<a id="ga9850df3217df58783c6538a3fb46ea6a"></a>

### `MAX2221X_NUM_CHANNELS`

```c
#define MAX2221X_NUM_CHANNELS 4
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

MAX2221X 通道数量（Number of Channels）。

<a id="ga4f3bc6647ecac99c3601c3d15e59b57f"></a>

### `MAX2221X_RAMP_MASK`

```c
#define MAX2221X_RAMP_MASK GENMASK(7, 0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

斜坡变化率值掩码（Ramp Slew Rate Value Mask）。

<a id="ga776a504229c90e1fba219078ee6a31f8"></a>

### `MAX2221X_RDWE_MASK`

```c
#define MAX2221X_RDWE_MASK BIT(10)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

下降斜坡使能掩码（Ramp-down Enable Mask）。

<a id="ga119fe235e2dddb4e044b51e14e305e47"></a>

### `MAX2221X_REG_CFG_CTRL0`

```c
#define MAX2221X_REG_CFG_CTRL0 ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x0D + ((x) * 0xE))
```

通道控制 0 配置寄存器地址（Channel Control 0 Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="ga5d21beb99b3647ae9a367b62681e8108"></a>

### `MAX2221X_REG_CFG_CTRL1`

```c
#define MAX2221X_REG_CFG_CTRL1 ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x0E + ((x) * 0xE))
```

通道控制 1 配置寄存器地址（Channel Control 1 Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="ga46a038e5a2c9e9d294c143e2c1eff33a"></a>

### `MAX2221X_REG_CFG_DC_H`

```c
#define MAX2221X_REG_CFG_DC_H ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x0A + ((x) * 0xE))
```

通道高占空比配置寄存器地址（Channel Duty Cycle High Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="gaf19fb778adfe9e8794c1ee14058856f3"></a>

### `MAX2221X_REG_CFG_DC_L`

```c
#define MAX2221X_REG_CFG_DC_L ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x0B + ((x) * 0xE))
```

通道低占空比配置寄存器地址（Channel Duty Cycle Low Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="gabc173632479d896452cd7f3b749c5848"></a>

### `MAX2221X_REG_CFG_DC_L2H`

```c
#define MAX2221X_REG_CFG_DC_L2H ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x09 + ((x) * 0xE))
```

通道占空比由低到高配置寄存器地址（Channel Duty Cycle Low-to-High Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="ga2980e35f7958ab77dc97411f53bccde8"></a>

### `MAX2221X_REG_CFG_TIME_L2H`

```c
#define MAX2221X_REG_CFG_TIME_L2H ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x0C + ((x) * 0xE))
```

通道由低到高时间配置寄存器地址（Channel Time Low-to-High Configuration Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="ga072c147f6c0f7a9a179a3a3f67afc3bd"></a>

### `MAX2221X_REG_DC_H2L`

```c
#define MAX2221X_REG_DC_H2L 0x03
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

退磁占空比由高到低寄存器地址（Demagnetization Duty Cycle High-to-Low Register Address）。

<a id="gae311958c9f915b18592aeeaecc5e4ccf"></a>

### `MAX2221X_REG_FAULT0`

```c
#define MAX2221X_REG_FAULT0 0x65
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

故障 0 寄存器地址（Fault 0 Register Address）。

<a id="ga5fd1b8fd8cdc680ba9e11417384c1e4a"></a>

### `MAX2221X_REG_FAULT1`

```c
#define MAX2221X_REG_FAULT1 0x66
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

故障 1 寄存器地址（Fault 1 Register Address）。

<a id="ga6ea173e70a91aac91069096f9ab746ed"></a>

### `MAX2221X_REG_GLOBAL_CFG`

```c
#define MAX2221X_REG_GLOBAL_CFG 0x01
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

全局配置寄存器地址（Global Configuration Register Address）。

<a id="ga1ef3d73859f871fd44a6583312083752"></a>

### `MAX2221X_REG_GLOBAL_CTRL`

```c
#define MAX2221X_REG_GLOBAL_CTRL 0x00
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

全局控制寄存器地址（Global Control Register Address）。

<a id="ga7ba68b3a283ecaaac443714b4ab0b1ec"></a>

### `MAX2221X_REG_PWM_DUTY`

```c
#define MAX2221X_REG_PWM_DUTY ( x)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

展开值（Value）：

```c
(0x49 + ((x) * 0xE))
```

通道 PWM 占空比寄存器地址（Channel PWM Duty Cycle Register Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 通道编号。 |

<a id="gab3e7e855f98d2c6a4f80e12326aba8ca"></a>

### `MAX2221X_REG_STATUS`

```c
#define MAX2221X_REG_STATUS 0x02
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

状态寄存器地址（Status Register Address）。

<a id="ga0c092ca1da2d34768fe63abf208d59cb"></a>

### `MAX2221X_REG_VM_MONITOR`

```c
#define MAX2221X_REG_VM_MONITOR 0x05
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电压监视寄存器地址（Voltage Monitor Register Address）。

<a id="gab40470b5fb432dde27208f3233ab727b"></a>

### `MAX2221X_REG_VM_THRESHOLD`

```c
#define MAX2221X_REG_VM_THRESHOLD 0x06
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电压监视阈值寄存器地址（Voltage Monitor Threshold Register Address）。

<a id="ga7528406875c4d70cc1bc712d96b77eef"></a>

### `MAX2221X_RMDE_MASK`

```c
#define MAX2221X_RMDE_MASK BIT(9)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

中间斜坡使能掩码（Ramp-middle Enable Mask）。

<a id="ga7eebb941c340887a56d0a05faf138c4e"></a>

### `MAX2221X_RUPE_MASK`

```c
#define MAX2221X_RUPE_MASK BIT(8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

上升斜坡使能掩码（Ramp-up Enable Mask）。

<a id="ga484349100da619c9eda6abafd5a768e9"></a>

### `MAX2221X_SLEW_RATE_MASK`

```c
#define MAX2221X_SLEW_RATE_MASK GENMASK(5, 4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

输出转换速率选择掩码（Output Slew Rate Selection Mask）。

<a id="ga323fd84aa33f7dffc0ca0c4deeef2707"></a>

### `MAX2221X_SNSF_MASK`

```c
#define MAX2221X_SNSF_MASK GENMASK(1, 0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

检测缩放系数选择掩码（Sense Scaling Factor Selection Mask）。

<a id="gaedd5316c50cabb422e47927e2c9c1039"></a>

### `MAX2221X_SPI_TRANS_ADDR`

```c
#define MAX2221X_SPI_TRANS_ADDR GENMASK(6, 0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

SPI 事务寄存器地址字段掩码（Register Address Field Mask）。

<a id="ga08bc444215b31d90f1128c0736f6f21a"></a>

### `MAX2221X_SPI_TRANS_DIR`

```c
#define MAX2221X_SPI_TRANS_DIR BIT(7)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

SPI 事务读／写方向位（Read/Write Direction Bit）。

<a id="ga040658a951cbc304d0c8a563938e3836"></a>

### `MAX2221X_STATUS_COMER_MASK`

```c
#define MAX2221X_STATUS_COMER_MASK BIT(2)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

通信错误故障状态掩码（Communication Error Fault Status Mask）。

<a id="gaba0107d7195f03ac4150416f09b6c739"></a>

### `MAX2221X_STATUS_DPM_MASK`

```c
#define MAX2221X_STATUS_DPM_MASK BIT(3)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

DPM 错误故障状态掩码（DPM Error Fault Status Mask）。

<a id="ga58646784ba7aea973c9253394095c63c"></a>

### `MAX2221X_STATUS_HHF_MASK`

```c
#define MAX2221X_STATUS_HHF_MASK BIT(4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

未达到吸合电流故障状态掩码（Hit Current Not Reached Fault Status Mask）。

<a id="ga838ba035e998eb39c9ff8f6a473bd264"></a>

### `MAX2221X_STATUS_IND_MASK`

```c
#define MAX2221X_STATUS_IND_MASK BIT(8)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电感测量状态掩码（Inductance Measurement Status Mask）。

<a id="gaab816d44a3cc2b7d9d93a3aa9ec2218f"></a>

### `MAX2221X_STATUS_MIN_T_ON_MASK`

```c
#define MAX2221X_STATUS_MIN_T_ON_MASK BIT(10)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

最小导通时间故障状态掩码（Minimum On-Time Fault Status Mask）。

<a id="ga5632d8b38de2c3b68a816d41ca45d77f"></a>

### `MAX2221X_STATUS_OCP_MASK`

```c
#define MAX2221X_STATUS_OCP_MASK BIT(6)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

过流保护故障状态掩码（Over-Current Protection Fault Status Mask）。

<a id="ga77aa2ecaabe17104d418e040c1067e71"></a>

### `MAX2221X_STATUS_OLF_MASK`

```c
#define MAX2221X_STATUS_OLF_MASK BIT(5)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

开路负载故障状态掩码（Open-Load Fault Status Mask）。

<a id="ga41c3dd5472f9a6902d48a66245f136b8"></a>

### `MAX2221X_STATUS_OVT_MASK`

```c
#define MAX2221X_STATUS_OVT_MASK BIT(7)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

过温故障状态掩码（Over-Temperature Fault Status Mask）。

<a id="ga3cead261bb81ad06b1af7b1c35644da8"></a>

### `MAX2221X_STATUS_RES_MASK`

```c
#define MAX2221X_STATUS_RES_MASK BIT(9)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电阻测量状态掩码（Resistance Measurement Status Mask）。

<a id="gae9bcaf9188d9b19d77491bd3fa9b773f"></a>

### `MAX2221X_STATUS_STT0_MASK`

```c
#define MAX2221X_STATUS_STT0_MASK BIT(11)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

状态位 0 的掩码（Status Bit Mask）。

<a id="gacf4c8532880ce7ab67b72938dba527b3"></a>

### `MAX2221X_STATUS_STT1_MASK`

```c
#define MAX2221X_STATUS_STT1_MASK BIT(12)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

状态位 1 的掩码（Status Bit Mask）。

<a id="ga7db46819804b9a3f3d80e4037f1c906d"></a>

### `MAX2221X_STATUS_STT2_MASK`

```c
#define MAX2221X_STATUS_STT2_MASK BIT(13)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

状态位 2 的掩码（Status Bit Mask）。

<a id="gae1c68ba7dbb6d88198fceed26e29e121"></a>

### `MAX2221X_STATUS_STT3_MASK`

```c
#define MAX2221X_STATUS_STT3_MASK BIT(14)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

状态位 3 的掩码（Status Bit Mask）。

<a id="gac9f0cfb941c55888bd8785b846b27aba"></a>

### `MAX2221X_STATUS_UVM_MASK`

```c
#define MAX2221X_STATUS_UVM_MASK BIT(1)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

欠压监视故障状态掩码（Under-Voltage Monitor Fault Status Mask）。

<a id="gaec89bbd558f23064f678ff4c3a6632e8"></a>

### `MAX2221X_VDRNVDRDUTY_MASK`

```c
#define MAX2221X_VDRNVDRDUTY_MASK BIT(4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

VDR／VDRDUTY 模式选择掩码（Mode Selection Mask）。

<a id="ga8a241d8e5a7530a624fed4603af1f352"></a>

### `MAX2221X_VM_MONITOR_MASK`

```c
#define MAX2221X_VM_MONITOR_MASK GENMASK(12, 0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电压监视测量值掩码（Voltage Monitor Measurement Value Mask）。

<a id="ga41ab1fc286e224183a21904a68172dc9"></a>

### `MAX2221X_VM_THLD_DOWN_MASK`

```c
#define MAX2221X_VM_THLD_DOWN_MASK GENMASK(3, 0)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电压监视下限阈值掩码（Lower Voltage Monitor Threshold Mask）。

<a id="ga99d548ae7681c6d5b9e297679d594518"></a>

### `MAX2221X_VM_THLD_UP_MASK`

```c
#define MAX2221X_VM_THLD_UP_MASK GENMASK(7, 4)
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

电压监视上限阈值掩码（Upper Voltage Monitor Threshold Mask）。

<a id="ga18675d06cfed3daef49f22b4ee5df5c9"></a>

### `max2221x_reg_read()`

```c
int max2221x_reg_read ( const struct device * dev, uint8_t addr, uint16_t * value )
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

读取 MAX2221X 的寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MAX2221X 多功能设备（MFD）。 |
| `addr` | 要读取的寄存器地址（register address）。 |
| `value` | 指向接收数据缓冲区的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 发生任何错误时，参见 `spi_transceive_dt()`。 |

<a id="gaa79d4e3e8f43e88872db2a8bd100707e"></a>

### `max2221x_reg_update()`

```c
int max2221x_reg_update ( const struct device * dev, uint8_t addr, uint16_t mask, uint16_t val )
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

更新 MAX2221X 的寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MAX2221X 多功能设备（MFD）。 |
| `addr` | 要更新的寄存器地址（Register Address）。 |
| `mask` | 应用于寄存器的掩码（Mask）。 |
| `val` | 要写入寄存器的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 发生任何错误时，参见 `spi_transceive_dt()`。 |

<a id="gaf1eb751764b13b03e6ef732621baf942"></a>

### `max2221x_reg_write()`

```c
int max2221x_reg_write ( const struct device * dev, uint8_t addr, uint16_t value )
```

```c
#include <zephyr/drivers/mfd/max2221x.h>
```

写入 MAX2221X 的寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MAX2221X 多功能设备（MFD）。 |
| `addr` | 要写入的寄存器地址。 |
| `value` | 要写入的内容。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 发生任何错误时，参见 `spi_write_dt()`。 |


## 4.16\_原页交叉引用（Cross References）

- [max2221x.h](../api_file_power_ots_reference/P002_zephyr__drivers__mfd__max2221x.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [spi_transceive_dt()](../hardware/P318_SPI公共接口.md#ga52c017066736414b31ff709ddc67c4ff)
- [spi_write_dt()](../hardware/P318_SPI公共接口.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_嵌入式控制器主机命令接口（EC Host Command Interface）.md) · [返回大纲](大纲.md) · [下一章](P005_MFD NPM10XX 接口.md)
