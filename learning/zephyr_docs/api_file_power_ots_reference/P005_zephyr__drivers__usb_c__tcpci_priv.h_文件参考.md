---
id: learning.zephyr-docs.api-file-power-ots-reference.page-5
title: zephyr__drivers__usb_c__tcpci_priv.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_usb\_c\_\_tcpci\_priv.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

符合Type-C端口控制器接口（TCPCI）的驱动所用的辅助函数。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/usb_c/usbc.h>
```

查看此文件的源码。

供兼容 Type-C 端口控制器接口（TCPCI）的驱动使用的辅助函数。此文件包含通用 TCPCI 函数，面向希望实现厂商特定功能的兼容 TCPCI 设备驱动，使其无需重新实现 TCPCI 通用功能与寄存器操作。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_tcpci_5Freg_5Fdump_5Fmap"></a>

```c
struct tcpci_reg_dump_map
```

相关声明：[tcpci_reg_dump_map](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md)。

在寄存器转储（Register Dump）中将寄存器地址绑定到名称的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a031fe5b188cbe9b4e80e9cff0c845eda"></a>

```c
#define TCPCI_STD_REGS_SIZE 38
```

相关声明：[TCPCI_STD_REGS_SIZE](#a031fe5b188cbe9b4e80e9cff0c845eda)。

包含 `tcpci dump` 命令所用标准寄存器的数组大小。

<a id="r_afdb5a5ec3c04cba9b8ec1eec1195156c"></a>

```c
#define PD_INT_REV10 0x10
```

相关声明：[PD_INT_REV10](#afdb5a5ec3c04cba9b8ec1eec1195156c)。

《Type-C 端口控制器接口规范》（Type-C Port Controller Interface Specification）修订版 1.0。

<a id="r_afe46df9f6080d8f5070f0bc81b68a6b6"></a>

```c
#define PD_INT_REV20 0x20
```

相关声明：[PD_INT_REV20](#afe46df9f6080d8f5070f0bc81b68a6b6)。

《Type-C 端口控制器接口规范》（Type-C Port Controller Interface Specification）修订版 2.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_aaad4be0dbc4c31e9d3438b7f8a3e8433"></a>

```c
int tcpci_read_reg8 (const struct i2c_dt_spec *bus, uint8_t reg, uint8_t *value)
```

相关声明：[tcpci_read_reg8](#aaad4be0dbc4c31e9d3438b7f8a3e8433)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TCPCI 设备 8 位寄存器（Register）的函数。

<a id="r_abbe63527659134a5bc14d6ecefabb0af"></a>

```c
int tcpci_write_reg8 (const struct i2c_dt_spec *bus, uint8_t reg, uint8_t value)
```

相关声明：[tcpci_write_reg8](#abbe63527659134a5bc14d6ecefabb0af)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 TCPCI 设备 8 位寄存器（Register）写入数值的函数。

<a id="r_a2f4e5571a7f272dd968dc002d70ef3f4"></a>

```c
int tcpci_update_reg8 (const struct i2c_dt_spec *bus, uint8_t reg, uint8_t mask, uint8_t value)
```

相关声明：[tcpci_update_reg8](#a2f4e5571a7f272dd968dc002d70ef3f4)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取并更新 TCPCI 设备 8 位寄存器部分位的函数。此函数不以原子方式（Atomically）执行该操作。

<a id="r_a00557a03647d6bd1ecba157ffff40e46"></a>

```c
int tcpci_read_reg16 (const struct i2c_dt_spec *bus, uint8_t reg, uint16_t *value)
```

相关声明：[tcpci_read_reg16](#a00557a03647d6bd1ecba157ffff40e46)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 TCPCI 设备 16 位寄存器（Register）的函数。

<a id="r_a7db13212d494bcc8c98190f8670fcd34"></a>

```c
int tcpci_write_reg16 (const struct i2c_dt_spec *bus, uint8_t reg, uint16_t value)
```

相关声明：[tcpci_write_reg16](#a7db13212d494bcc8c98190f8670fcd34)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 TCPCI 设备 16 位寄存器（Register）写入数值的函数。

<a id="r_abafd9380a335483525d8ff5b2b9e2306"></a>

```c
enum tcpc_alert tcpci_alert_reg_to_enum (uint16_t reg)
```

相关声明：[tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)、[tcpci_alert_reg_to_enum](#abafd9380a335483525d8ff5b2b9e2306)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将 TCPCI 告警寄存器（Alert Register）转换为 `tcpc_alert` 枚举的函数。硬复位（Hard Reset）值优先，其余值按位位置从最低有效位到最高有效位的顺序返回。

<a id="r_ade1aa43041be0cc1abcf074b8e4e07e9"></a>

```c
int tcpci_tcpm_get_cc (const struct i2c_dt_spec *bus, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

相关声明：[tcpci_tcpm_get_cc](#ade1aa43041be0cc1abcf074b8e4e07e9)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

读取 CC 状态寄存器（CC Status Registers），并将读取值转换为表示电压状态和伙伴检测状态（Partner Detection Status）的枚举的函数。

<a id="r_a49a2f453d03c75aaea608a17a85a6c6f"></a>

```c
int tcpci_tcpm_get_chip_info (const struct i2c_dt_spec *bus, struct tcpc_chip_info *chip_info)
```

相关声明：[tcpci_tcpm_get_chip_info](#a49a2f453d03c75aaea608a17a85a6c6f)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

获取 TCPCI 芯片信息（Chip Information）的函数。

<a id="r_a005a5b7130913ba80ff21d89f6d0c8a7"></a>

```c
int tcpci_tcpm_dump_std_reg (const struct i2c_dt_spec *bus)
```

相关声明：[tcpci_tcpm_dump_std_reg](#a005a5b7130913ba80ff21d89f6d0c8a7)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)。

转储 TCPCI 标准寄存器（Standard Registers）的函数。

<a id="r_add2b2c0859e4ab1cf2f0e290e1d71d19"></a>

```c
int tcpci_tcpm_set_bist_test_mode (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_bist_test_mode](#add2b2c0859e4ab1cf2f0e290e1d71d19)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用内建自测试（Built-In Self-Test，BIST）模式的函数。

<a id="r_a8ac9f08daf0f50749e9df389d1c8d41f"></a>

```c
int tcpci_tcpm_transmit_data (const struct i2c_dt_spec *bus, struct pd_msg *msg, const uint8_t retries)
```

相关声明：[tcpci_tcpm_transmit_data](#a8ac9f08daf0f50749e9df389d1c8d41f)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送电力传输（Power Delivery，PD）消息的函数。

<a id="r_ae2a60d3000187f640331816edbbcbcb6"></a>

```c
int tcpci_tcpm_select_rp_value (const struct i2c_dt_spec *bus, enum tc_rp_value rp)
```

相关声明：[tcpci_tcpm_select_rp_value](#ae2a60d3000187f640331816edbbcbcb6)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

选择上拉电阻（Pull-Up Resistor，Rp）值的函数。

<a id="r_a2233ff710864ba8ec40f7792e6baf002"></a>

```c
int tcpci_tcpm_get_rp_value (const struct i2c_dt_spec *bus, enum tc_rp_value *rp)
```

相关声明：[tcpci_tcpm_get_rp_value](#a2233ff710864ba8ec40f7792e6baf002)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取当前选定上拉电阻（Rp）值的函数。

<a id="r_a56b77c066ecd306d98a9e8e7ca249dc6"></a>

```c
int tcpci_tcpm_set_cc (const struct i2c_dt_spec *bus, enum tc_cc_pull pull)
```

相关声明：[tcpci_tcpm_set_cc](#a56b77c066ecd306d98a9e8e7ca249dc6)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)。

设置 CC 上拉／下拉电阻（Pull Resistor），并将角色设为供电端（Source）或受电端（Sink）的函数。

<a id="r_a3da565a529db5a6d337cf7f8642be8ab"></a>

```c
int tcpci_tcpm_set_drp_toggle (const struct i2c_dt_spec *bus, uint8_t pd_int_rev, bool enable)
```

相关声明：[tcpci_tcpm_set_drp_toggle](#a3da565a529db5a6d337cf7f8642be8ab)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用 TCPC 自动双角色切换（Auto Dual Role Toggle）的函数。

<a id="r_a0b0efcd606bdd19925ebaaaed017e5f9"></a>

```c
int tcpci_tcpm_set_roles (const struct i2c_dt_spec *bus, enum pd_rev_type pd_rev, enum tc_power_role power_role, enum tc_data_role data_role)
```

相关声明：[tcpci_tcpm_set_roles](#a0b0efcd606bdd19925ebaaaed017e5f9)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)、[tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)。

设置 PD 消息头中的电源角色（Power Role）和数据角色（Data Role）的函数。

<a id="r_a0223089c1ab73b1ec8c5a2e9de9b2932"></a>

```c
int tcpci_tcpm_set_rx_type (const struct i2c_dt_spec *bus, uint8_t type)
```

相关声明：[tcpci_tcpm_set_rx_type](#a0223089c1ab73b1ec8c5a2e9de9b2932)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置接收类型（RX Type）的函数。

<a id="r_a87aec00974ff403a0e60b1ee1346ec73"></a>

```c
int tcpci_tcpm_set_cc_polarity (const struct i2c_dt_spec *bus, enum tc_cc_polarity polarity)
```

相关声明：[tcpci_tcpm_set_cc_polarity](#a87aec00974ff403a0e60b1ee1346ec73)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)。

设置 CC 线路极性（Polarity）的函数。

<a id="r_ac37957893c769d805d997a93198827a7"></a>

```c
int tcpci_tcpm_set_vconn (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_vconn](#ac37957893c769d805d997a93198827a7)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用 VCONN 的函数。

<a id="r_a33e3ccf31b7449667b3cf6429c243baa"></a>

```c
int tcpci_tcpm_get_alert_status (const struct i2c_dt_spec *bus, uint16_t *status)
```

相关声明：[tcpci_tcpm_get_alert_status](#a33e3ccf31b7449667b3cf6429c243baa)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 TCPCI 告警寄存器（Alert Register）状态的函数。

<a id="r_aa2fe9bdb8a6dc0d451f26fb854d2bb15"></a>

```c
int tcpci_tcpm_get_cc_status (const struct i2c_dt_spec *bus, uint8_t *status)
```

相关声明：[tcpci_tcpm_get_cc_status](#aa2fe9bdb8a6dc0d451f26fb854d2bb15)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 TCPCI CC 状态寄存器（CC Status Register）状态的函数。

<a id="r_a75bab88b3a68acf79a3f2dae53756333"></a>

```c
int tcpci_tcpm_get_power_status (const struct i2c_dt_spec *bus, uint8_t *status)
```

相关声明：[tcpci_tcpm_get_power_status](#a75bab88b3a68acf79a3f2dae53756333)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 TCPCI 电源状态寄存器（Power Status Register）状态的函数。

<a id="r_acf5218a19598dcec80ab3f7c16b637e9"></a>

```c
int tcpci_tcpm_get_fault_status (const struct i2c_dt_spec *bus, uint8_t *status)
```

相关声明：[tcpci_tcpm_get_fault_status](#acf5218a19598dcec80ab3f7c16b637e9)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 TCPCI 故障状态寄存器（Fault Status Register）状态的函数。

<a id="r_a01b6202cf0978d608689d36fdbc9416a"></a>

```c
int tcpci_tcpm_get_extended_status (const struct i2c_dt_spec *bus, uint8_t *status)
```

相关声明：[tcpci_tcpm_get_extended_status](#a01b6202cf0978d608689d36fdbc9416a)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 TCPCI 扩展状态寄存器（Extended Status Register）状态的函数。

<a id="r_ac72769df523625b5ac60e9eb1807bbab"></a>

```c
int tcpci_tcpm_get_extended_alert_status (const struct i2c_dt_spec *bus, uint8_t *status)
```

相关声明：[tcpci_tcpm_get_extended_alert_status](#ac72769df523625b5ac60e9eb1807bbab)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 TCPCI 扩展告警状态寄存器（Extended Alert Status Register）状态的函数。

<a id="r_aef29ca84b4cc68a55b840e987ec87f28"></a>

```c
int tcpci_tcpm_clear_status_register (const struct i2c_dt_spec *bus, enum tcpc_status_reg reg, uint16_t mask)
```

相关声明：[tcpci_tcpm_clear_status_register](#aef29ca84b4cc68a55b840e987ec87f28)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

清除 TCPCI 状态寄存器（Status Register）中指定位的函数。

<a id="r_aadbf2ef0350b8c54c4da53b7ab79f7d6"></a>

```c
int tcpci_tcpm_mask_status_register (const struct i2c_dt_spec *bus, enum tcpc_status_reg reg, uint16_t mask)
```

相关声明：[tcpci_tcpm_mask_status_register](#aadbf2ef0350b8c54c4da53b7ab79f7d6)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 TCPCI 状态寄存器（Status Register）掩码的函数。

<a id="r_a338bd0bfb0df0fa3e4004dce85a7336b"></a>

```c
int tcpci_tcpm_get_snk_ctrl (const struct i2c_dt_spec *bus, bool *sinking)
```

相关声明：[tcpci_tcpm_get_snk_ctrl](#a338bd0bfb0df0fa3e4004dce85a7336b)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPCI 当前的受电状态（Sinking State）。

<a id="r_a9be63be44b19198cd8d49f95e971ee6d"></a>

```c
int tcpci_tcpm_get_src_ctrl (const struct i2c_dt_spec *bus, bool *sourcing)
```

相关声明：[tcpci_tcpm_get_src_ctrl](#a9be63be44b19198cd8d49f95e971ee6d)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPCI 当前的供电状态（Sourcing State）。

<a id="r_ac6848fa7e70af270d4471309589100f4"></a>

```c
int tcpci_tcpm_set_snk_ctrl (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_snk_ctrl](#ac6848fa7e70af270d4471309589100f4)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用通过 VBUS 受电（Sinking Power）的函数。

<a id="r_aadac3408a1aea5e56c2578f3843c032a"></a>

```c
int tcpci_tcpm_set_src_ctrl (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_src_ctrl](#aadac3408a1aea5e56c2578f3843c032a)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用通过 VBUS 供电（Sourcing Power）的函数。

<a id="r_a269a35fb98ec53dba41fa53c78683ae2"></a>

```c
int tcpci_tcpm_set_debug_accessory (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_debug_accessory](#a269a35fb98ec53dba41fa53c78683ae2)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用调试附件模式（Debug Accessory Mode）的函数。

<a id="r_aa86dd25de3d91ac61abc06f0c734046f"></a>

```c
int tcpci_tcpm_set_low_power_mode (const struct i2c_dt_spec *bus, bool enable)
```

相关声明：[tcpci_tcpm_set_low_power_mode](#aa86dd25de3d91ac61abc06f0c734046f)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用低功耗模式（Low Power Mode）的函数。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 5.4\_变量（Variables）

<a id="r_ab2204d54c7483fb06f02dda83b0066f8"></a>

```c
const struct tcpci_reg_dump_map tcpci_std_regs [38]
```

相关声明：[tcpci_reg_dump_map](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md)、[tcpci_std_regs](#ab2204d54c7483fb06f02dda83b0066f8)。

包含 TCPCI 标准寄存器列表（Standard Registers List）的数组。

## 5.5\_详细说明（Detailed Documentation）

<a id="afdb5a5ec3c04cba9b8ec1eec1195156c"></a>

### `PD_INT_REV10`

```c
#define PD_INT_REV10 0x10
```

《Type-C 端口控制器接口规范》（Type-C Port Controller Interface Specification）修订版 1.0。

<a id="afe46df9f6080d8f5070f0bc81b68a6b6"></a>

### `PD_INT_REV20`

```c
#define PD_INT_REV20 0x20
```

《Type-C 端口控制器接口规范》（Type-C Port Controller Interface Specification）修订版 2.0。

<a id="a031fe5b188cbe9b4e80e9cff0c845eda"></a>

### `TCPCI_STD_REGS_SIZE`

```c
#define TCPCI_STD_REGS_SIZE 38
```

包含 `tcpci dump` 命令所用标准寄存器的数组大小。

<a id="abafd9380a335483525d8ff5b2b9e2306"></a>

### `tcpci_alert_reg_to_enum()`

```c
enum tcpc_alert tcpci_alert_reg_to_enum ( uint16_t reg)
```

将 TCPCI 告警寄存器（Alert Register）转换为 `tcpc_alert` 枚举的函数。硬复位（Hard Reset）值优先，其余值按位位置从最低有效位到最高有效位的顺序返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | TCPCI 告警寄存器（Alert Register）的值。此参数必须非零。 |

**返回（Returns）**：返回值（Returns）：`enum tcpc_alert`；告警寄存器中某个已置位标志对应的值。

<a id="a00557a03647d6bd1ecba157ffff40e46"></a>

### `tcpci_read_reg16()`

```c
int tcpci_read_reg16 ( const struct i2c_dt_spec * bus, uint8_t reg, uint16_t * value )
```

读取 TCPCI 设备 16 位寄存器（Register）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | TCPCI 寄存器地址（Register Address）。 |
| `value` | 指向用于存储寄存器值的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="aaad4be0dbc4c31e9d3438b7f8a3e8433"></a>

### `tcpci_read_reg8()`

```c
int tcpci_read_reg8 ( const struct i2c_dt_spec * bus, uint8_t reg, uint8_t * value )
```

读取 TCPCI 设备 8 位寄存器（Register）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | TCPCI 寄存器地址（Register Address）。 |
| `value` | 指向用于存储寄存器值的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="aef29ca84b4cc68a55b840e987ec87f28"></a>

### `tcpci_tcpm_clear_status_register()`

```c
int tcpci_tcpm_clear_status_register ( const struct i2c_dt_spec * bus, enum tcpc_status_reg reg, uint16_t mask )
```

清除 TCPCI 状态寄存器（Status Register）中指定位的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | 表示要清除的状态寄存器（Status Register）的枚举。 |
| `mask` | 指定要清除哪些位的位掩码（Bitmask）。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a005a5b7130913ba80ff21d89f6d0c8a7"></a>

### `tcpci_tcpm_dump_std_reg()`

```c
int tcpci_tcpm_dump_std_reg ( const struct i2c_dt_spec * bus)
```

转储 TCPCI 标准寄存器（Standard Registers）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a33e3ccf31b7449667b3cf6429c243baa"></a>

### `tcpci_tcpm_get_alert_status()`

```c
int tcpci_tcpm_get_alert_status ( const struct i2c_dt_spec * bus, uint16_t * status )
```

获取 TCPCI 告警寄存器（Alert Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ade1aa43041be0cc1abcf074b8e4e07e9"></a>

### `tcpci_tcpm_get_cc()`

```c
int tcpci_tcpm_get_cc ( const struct i2c_dt_spec * bus, enum tc_cc_voltage_state * cc1, enum tc_cc_voltage_state * cc2 )
```

读取 CC 状态寄存器（CC Status Registers），并将读取值转换为表示电压状态和伙伴检测状态（Partner Detection Status）的枚举的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `cc1` | 指向用于存储检测到的 CC1 电压状态（Voltage State）的变量的指针。 |
| `cc2` | 指向用于存储检测到的 CC2 电压状态（Voltage State）的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`cc1` 或 `cc2` 指针为 `NULL` 时返回 `-EINVAL`；否则返回 `int` 类型的 I2C 操作状态，成功时为 0。

<a id="aa2fe9bdb8a6dc0d451f26fb854d2bb15"></a>

### `tcpci_tcpm_get_cc_status()`

```c
int tcpci_tcpm_get_cc_status ( const struct i2c_dt_spec * bus, uint8_t * status )
```

获取 TCPCI CC 状态寄存器（CC Status Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a49a2f453d03c75aaea608a17a85a6c6f"></a>

### `tcpci_tcpm_get_chip_info()`

```c
int tcpci_tcpm_get_chip_info ( const struct i2c_dt_spec * bus, struct tcpc_chip_info * chip_info )
```

获取 TCPCI 芯片信息（Chip Information）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `chip_info` | 指向用于存储芯片信息（Chip Information）的结构体的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ac72769df523625b5ac60e9eb1807bbab"></a>

### `tcpci_tcpm_get_extended_alert_status()`

```c
int tcpci_tcpm_get_extended_alert_status ( const struct i2c_dt_spec * bus, uint8_t * status )
```

获取 TCPCI 扩展告警状态寄存器（Extended Alert Status Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a01b6202cf0978d608689d36fdbc9416a"></a>

### `tcpci_tcpm_get_extended_status()`

```c
int tcpci_tcpm_get_extended_status ( const struct i2c_dt_spec * bus, uint8_t * status )
```

获取 TCPCI 扩展状态寄存器（Extended Status Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="acf5218a19598dcec80ab3f7c16b637e9"></a>

### `tcpci_tcpm_get_fault_status()`

```c
int tcpci_tcpm_get_fault_status ( const struct i2c_dt_spec * bus, uint8_t * status )
```

获取 TCPCI 故障状态寄存器（Fault Status Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a75bab88b3a68acf79a3f2dae53756333"></a>

### `tcpci_tcpm_get_power_status()`

```c
int tcpci_tcpm_get_power_status ( const struct i2c_dt_spec * bus, uint8_t * status )
```

获取 TCPCI 电源状态寄存器（Power Status Register）状态的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `status` | 指向用于存储状态的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a2233ff710864ba8ec40f7792e6baf002"></a>

### `tcpci_tcpm_get_rp_value()`

```c
int tcpci_tcpm_get_rp_value ( const struct i2c_dt_spec * bus, enum tc_rp_value * rp )
```

获取当前选定上拉电阻（Rp）值的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `rp` | 指向用于存储上拉电阻（Rp）值的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a338bd0bfb0df0fa3e4004dce85a7336b"></a>

### `tcpci_tcpm_get_snk_ctrl()`

```c
int tcpci_tcpm_get_snk_ctrl ( const struct i2c_dt_spec * bus, bool * sinking )
```

查询 TCPCI 当前的受电状态（Sinking State）。

此函数检查设备是否正在从 VBUS 受电（Sinking），并向系统负载供电。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `sinking` | 指向用于存储受电状态（Sinking State）的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a9be63be44b19198cd8d49f95e971ee6d"></a>

### `tcpci_tcpm_get_src_ctrl()`

```c
int tcpci_tcpm_get_src_ctrl ( const struct i2c_dt_spec * bus, bool * sourcing )
```

查询 TCPCI 当前的供电状态（Sourcing State）。

此函数检查设备是否正在向 VBUS 供电（Sourcing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `sourcing` | 指向用于存储供电状态（Sourcing State）的变量的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="aadbf2ef0350b8c54c4da53b7ab79f7d6"></a>

### `tcpci_tcpm_mask_status_register()`

```c
int tcpci_tcpm_mask_status_register ( const struct i2c_dt_spec * bus, enum tcpc_status_reg reg, uint16_t mask )
```

设置 TCPCI 状态寄存器（Status Register）掩码的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | 表示要设置掩码的状态寄存器（Status Register）的枚举。 |
| `mask` | 指定哪些位需要设置掩码的位掩码（Bitmask）。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ae2a60d3000187f640331816edbbcbcb6"></a>

### `tcpci_tcpm_select_rp_value()`

```c
int tcpci_tcpm_select_rp_value ( const struct i2c_dt_spec * bus, enum tc_rp_value rp )
```

选择上拉电阻（Pull-Up Resistor，Rp）值的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `rp` | 表示要设置的上拉电阻（Rp）值的枚举。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="add2b2c0859e4ab1cf2f0e290e1d71d19"></a>

### `tcpci_tcpm_set_bist_test_mode()`

```c
int tcpci_tcpm_set_bist_test_mode ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用内建自测试（Built-In Self-Test，BIST）模式的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用内建自测试（BIST）模式，`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a56b77c066ecd306d98a9e8e7ca249dc6"></a>

### `tcpci_tcpm_set_cc()`

```c
int tcpci_tcpm_set_cc ( const struct i2c_dt_spec * bus, enum tc_cc_pull pull )
```

设置 CC 上拉／下拉电阻（Pull Resistor），并将角色设为供电端（Source）或受电端（Sink）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `pull` | 表示要设置的 CC 上拉／下拉电阻（Pull Resistor）的枚举。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a87aec00974ff403a0e60b1ee1346ec73"></a>

### `tcpci_tcpm_set_cc_polarity()`

```c
int tcpci_tcpm_set_cc_polarity ( const struct i2c_dt_spec * bus, enum tc_cc_polarity polarity )
```

设置 CC 线路极性（Polarity）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `polarity` | 表示要设置的 CC 极性（Polarity）的枚举。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a269a35fb98ec53dba41fa53c78683ae2"></a>

### `tcpci_tcpm_set_debug_accessory()`

```c
int tcpci_tcpm_set_debug_accessory ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用调试附件模式（Debug Accessory Mode）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用调试附件模式（Debug Accessory Mode），`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a3da565a529db5a6d337cf7f8642be8ab"></a>

### `tcpci_tcpm_set_drp_toggle()`

```c
int tcpci_tcpm_set_drp_toggle ( const struct i2c_dt_spec * bus, uint8_t pd_int_rev, bool enable )
```

启用／禁用 TCPC 自动双角色切换（Auto Dual Role Toggle）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `pd_int_rev` | `TCPC_REG_PD_INT_REV` 的 `[15..8]` 位的值。 |
| `enable` | 布尔标志：`true` 启用双角色电源切换模式（DRP Toggle Mode），`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="aa86dd25de3d91ac61abc06f0c734046f"></a>

### `tcpci_tcpm_set_low_power_mode()`

```c
int tcpci_tcpm_set_low_power_mode ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用低功耗模式（Low Power Mode）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用低功耗模式（Low Power Mode），`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a0b0efcd606bdd19925ebaaaed017e5f9"></a>

### `tcpci_tcpm_set_roles()`

```c
int tcpci_tcpm_set_roles ( const struct i2c_dt_spec * bus, enum pd_rev_type pd_rev, enum tc_power_role power_role, enum tc_data_role data_role )
```

设置 PD 消息头中的电源角色（Power Role）和数据角色（Data Role）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `pd_rev` | 表示要设置的 USB-PD 规范修订版（USB-PD Specification Revision）的枚举。 |
| `power_role` | 表示要设置的电源角色（Power Role）的枚举。 |
| `data_role` | 表示要设置的数据角色（Data Role）的枚举。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a0223089c1ab73b1ec8c5a2e9de9b2932"></a>

### `tcpci_tcpm_set_rx_type()`

```c
int tcpci_tcpm_set_rx_type ( const struct i2c_dt_spec * bus, uint8_t type )
```

设置接收类型（RX Type）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `type` | 表示要设置的接收类型（RX Type）的值。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ac6848fa7e70af270d4471309589100f4"></a>

### `tcpci_tcpm_set_snk_ctrl()`

```c
int tcpci_tcpm_set_snk_ctrl ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用通过 VBUS 受电（Sinking Power）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用受电（Sinking Power），`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="aadac3408a1aea5e56c2578f3843c032a"></a>

### `tcpci_tcpm_set_src_ctrl()`

```c
int tcpci_tcpm_set_src_ctrl ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用通过 VBUS 供电（Sourcing Power）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用供电（Sourcing Power），`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ac37957893c769d805d997a93198827a7"></a>

### `tcpci_tcpm_set_vconn()`

```c
int tcpci_tcpm_set_vconn ( const struct i2c_dt_spec * bus, bool enable )
```

启用／禁用 VCONN 的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `enable` | 布尔标志：`true` 启用 VCONN，`false` 禁用。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a8ac9f08daf0f50749e9df389d1c8d41f"></a>

### `tcpci_tcpm_transmit_data()`

```c
int tcpci_tcpm_transmit_data ( const struct i2c_dt_spec * bus, struct pd_msg * msg, const uint8_t retries )
```

发送电力传输（Power Delivery，PD）消息的函数。

发送消息时，若失败则按指定次数重试（Retries）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `msg` | 指向要发送的 PD 消息结构体（PD Message Structure）的指针。 |
| `retries` | 发送失败时的重试次数（Number of Retries）。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a2f4e5571a7f272dd968dc002d70ef3f4"></a>

### `tcpci_update_reg8()`

```c
int tcpci_update_reg8 ( const struct i2c_dt_spec * bus, uint8_t reg, uint8_t mask, uint8_t value )
```

读取并更新 TCPCI 设备 8 位寄存器部分位的函数。此函数不以原子方式（Atomically）执行该操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | TCPCI 寄存器地址（Register Address）。 |
| `mask` | 指定设备寄存器哪些位将被修改的位掩码（Bitmask）。 |
| `value` | 与 `mask` 按位与（AND）之后要写入设备寄存器的值。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="a7db13212d494bcc8c98190f8670fcd34"></a>

### `tcpci_write_reg16()`

```c
int tcpci_write_reg16 ( const struct i2c_dt_spec * bus, uint8_t reg, uint16_t value )
```

向 TCPCI 设备 16 位寄存器（Register）写入数值的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | TCPCI 寄存器地址（Register Address）。 |
| `value` | 要写入设备寄存器的值。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="abbe63527659134a5bc14d6ecefabb0af"></a>

### `tcpci_write_reg8()`

```c
int tcpci_write_reg8 ( const struct i2c_dt_spec * bus, uint8_t reg, uint8_t value )
```

向 TCPCI 设备 8 位寄存器（Register）写入数值的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | I2C总线（Inter-Integrated Circuit）。 |
| `reg` | TCPCI 寄存器地址（Register Address）。 |
| `value` | 要写入设备寄存器的值。 |

**返回（Returns）**：返回值（Returns）：`int`，I2C 操作状态；成功时为 0。

<a id="ab2204d54c7483fb06f02dda83b0066f8"></a>

### `tcpci_std_regs`

```c
const struct tcpci_reg_dump_map tcpci_std_regs[38]
```

声明属性：`extern`。

包含 TCPCI 标准寄存器列表（Standard Registers List）的数组。

如果 TCPC 驱动包含厂商特定寄存器（Vendor-Specific Registers），可覆盖 TCPCI 的 `dump_std_reg` 函数以转储这些寄存器；同时也应使用此数组转储标准寄存器。


## 5.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/usb_c/usbc.h](../api_source_reference/P889_usbc.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P857_tcpci_priv.h_源码浏览.md)
- [tcpci_reg_dump_map](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)
- [tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)
- [pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)
- [tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)
- [tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)
- [tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P004_zephyr__bluetooth__services__ots.h_文件参考.md) · [返回大纲](大纲.md)
