---
id: learning.zephyr-docs.api-source-reference.page-857
title: tcpci_priv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第857章\_tcpci\_priv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html)。

## 857.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="agroup__usb__power__delivery_html_gab68c6b6e33449c5ceadfc9217dd7a700"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga4687047910cad0dd970bbd28adcf22ed"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gafd8253dfa6abc80d0717b17271ed8916"></a>
<a id="agroup__usb__type__c_html_ga0200c820510eb786f3ca30a9b5f7aada"></a>
<a id="agroup__usb__type__c_html_ga4e0eec97f7c5c97b87eff9561deea2d5"></a>
<a id="agroup__usb__type__c_html_ga64e32ec2da97f70fd5b96975317cb92c"></a>
<a id="agroup__usb__type__c_html_ga6b98bbe238e62cfd5531688494a63de2"></a>
<a id="agroup__usb__type__c_html_gaa6dda0612045b5f55b9d8ba63d2b9f9d"></a>
<a id="agroup__usb__type__c_html_gac5b4b58840c9b076a869a5816ba100db"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructi2c__dt__spec_html"></a>
<a id="astructpd__msg_html"></a>
<a id="astructtcpc__chip__info_html"></a>
<a id="astructtcpci__reg__dump__map_html"></a>
<a id="astructtcpci__reg__dump__map_html_a316d7f2a6b4b5fd42eb6450a810b7dd8"></a>
<a id="astructtcpci__reg__dump__map_html_a6e84093c1d027233230d8f27b0698756"></a>
<a id="astructtcpci__reg__dump__map_html_ad68dd201d76bfb2193567b8db2ec514a"></a>
<a id="atcpci__priv_8h_html_a00557a03647d6bd1ecba157ffff40e46"></a>
<a id="atcpci__priv_8h_html_a005a5b7130913ba80ff21d89f6d0c8a7"></a>
<a id="atcpci__priv_8h_html_a01b6202cf0978d608689d36fdbc9416a"></a>
<a id="atcpci__priv_8h_html_a0223089c1ab73b1ec8c5a2e9de9b2932"></a>
<a id="atcpci__priv_8h_html_a031fe5b188cbe9b4e80e9cff0c845eda"></a>
<a id="atcpci__priv_8h_html_a0b0efcd606bdd19925ebaaaed017e5f9"></a>
<a id="atcpci__priv_8h_html_a2233ff710864ba8ec40f7792e6baf002"></a>
<a id="atcpci__priv_8h_html_a269a35fb98ec53dba41fa53c78683ae2"></a>
<a id="atcpci__priv_8h_html_a2f4e5571a7f272dd968dc002d70ef3f4"></a>
<a id="atcpci__priv_8h_html_a338bd0bfb0df0fa3e4004dce85a7336b"></a>
<a id="atcpci__priv_8h_html_a33e3ccf31b7449667b3cf6429c243baa"></a>
<a id="atcpci__priv_8h_html_a3da565a529db5a6d337cf7f8642be8ab"></a>
<a id="atcpci__priv_8h_html_a49a2f453d03c75aaea608a17a85a6c6f"></a>
<a id="atcpci__priv_8h_html_a56b77c066ecd306d98a9e8e7ca249dc6"></a>
<a id="atcpci__priv_8h_html_a75bab88b3a68acf79a3f2dae53756333"></a>
<a id="atcpci__priv_8h_html_a7db13212d494bcc8c98190f8670fcd34"></a>
<a id="atcpci__priv_8h_html_a87aec00974ff403a0e60b1ee1346ec73"></a>
<a id="atcpci__priv_8h_html_a8ac9f08daf0f50749e9df389d1c8d41f"></a>
<a id="atcpci__priv_8h_html_a9be63be44b19198cd8d49f95e971ee6d"></a>
<a id="atcpci__priv_8h_html_aa2fe9bdb8a6dc0d451f26fb854d2bb15"></a>
<a id="atcpci__priv_8h_html_aa86dd25de3d91ac61abc06f0c734046f"></a>
<a id="atcpci__priv_8h_html_aaad4be0dbc4c31e9d3438b7f8a3e8433"></a>
<a id="atcpci__priv_8h_html_aadac3408a1aea5e56c2578f3843c032a"></a>
<a id="atcpci__priv_8h_html_aadbf2ef0350b8c54c4da53b7ab79f7d6"></a>
<a id="atcpci__priv_8h_html_ab2204d54c7483fb06f02dda83b0066f8"></a>
<a id="atcpci__priv_8h_html_abafd9380a335483525d8ff5b2b9e2306"></a>
<a id="atcpci__priv_8h_html_abbe63527659134a5bc14d6ecefabb0af"></a>
<a id="atcpci__priv_8h_html_ac37957893c769d805d997a93198827a7"></a>
<a id="atcpci__priv_8h_html_ac6848fa7e70af270d4471309589100f4"></a>
<a id="atcpci__priv_8h_html_ac72769df523625b5ac60e9eb1807bbab"></a>
<a id="atcpci__priv_8h_html_acf5218a19598dcec80ab3f7c16b637e9"></a>
<a id="atcpci__priv_8h_html_add2b2c0859e4ab1cf2f0e290e1d71d19"></a>
<a id="atcpci__priv_8h_html_ade1aa43041be0cc1abcf074b8e4e07e9"></a>
<a id="atcpci__priv_8h_html_ae2a60d3000187f640331816edbbcbcb6"></a>
<a id="atcpci__priv_8h_html_aef29ca84b4cc68a55b840e987ec87f28"></a>
<a id="ausbc_8h_html"></a>

```c
/*
 * Copyright 2024 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_TCPCI_PRIV_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_TCPCI_PRIV_H_

#include <stdint.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/usb_c/usbc.h>

struct tcpci_reg_dump_map {
        uint8_t addr;
        const char *name;
        uint8_t size;
};

#define TCPCI_STD_REGS_SIZE 38
extern const struct tcpci_reg_dump_map tcpci_std_regs[TCPCI_STD_REGS_SIZE];

#define PD_INT_REV10 0x10
#define PD_INT_REV20 0x20

int tcpci_read_reg8(const struct i2c_dt_spec *bus, uint8_t reg, uint8_t *value);

int tcpci_write_reg8(const struct i2c_dt_spec *bus, uint8_t reg, uint8_t value);

int tcpci_update_reg8(const struct i2c_dt_spec *bus, uint8_t reg, uint8_t mask, uint8_t value);

int tcpci_read_reg16(const struct i2c_dt_spec *bus, uint8_t reg, uint16_t *value);

int tcpci_write_reg16(const struct i2c_dt_spec *bus, uint8_t reg, uint16_t value);

enum tcpc_alert tcpci_alert_reg_to_enum(uint16_t reg);

int tcpci_tcpm_get_cc(const struct i2c_dt_spec *bus, enum tc_cc_voltage_state *cc1,
                      enum tc_cc_voltage_state *cc2);

int tcpci_tcpm_get_chip_info(const struct i2c_dt_spec *bus, struct tcpc_chip_info *chip_info);

int tcpci_tcpm_dump_std_reg(const struct i2c_dt_spec *bus);

int tcpci_tcpm_set_bist_test_mode(const struct i2c_dt_spec *bus, bool enable);

int tcpci_tcpm_transmit_data(const struct i2c_dt_spec *bus, struct pd_msg *msg,
                             const uint8_t retries);

int tcpci_tcpm_select_rp_value(const struct i2c_dt_spec *bus, enum tc_rp_value rp);

int tcpci_tcpm_get_rp_value(const struct i2c_dt_spec *bus, enum tc_rp_value *rp);

int tcpci_tcpm_set_cc(const struct i2c_dt_spec *bus, enum tc_cc_pull pull);

int tcpci_tcpm_set_drp_toggle(const struct i2c_dt_spec *bus, uint8_t pd_int_rev, bool enable);

int tcpci_tcpm_set_roles(const struct i2c_dt_spec *bus, enum pd_rev_type pd_rev,
                         enum tc_power_role power_role, enum tc_data_role data_role);

int tcpci_tcpm_set_rx_type(const struct i2c_dt_spec *bus, uint8_t type);

int tcpci_tcpm_set_cc_polarity(const struct i2c_dt_spec *bus, enum tc_cc_polarity polarity);

int tcpci_tcpm_set_vconn(const struct i2c_dt_spec *bus, bool enable);

int tcpci_tcpm_get_alert_status(const struct i2c_dt_spec *bus, uint16_t *status);

int tcpci_tcpm_get_cc_status(const struct i2c_dt_spec *bus, uint8_t *status);

int tcpci_tcpm_get_power_status(const struct i2c_dt_spec *bus, uint8_t *status);

int tcpci_tcpm_get_fault_status(const struct i2c_dt_spec *bus, uint8_t *status);

int tcpci_tcpm_get_extended_status(const struct i2c_dt_spec *bus, uint8_t *status);

int tcpci_tcpm_get_extended_alert_status(const struct i2c_dt_spec *bus, uint8_t *status);

int tcpci_tcpm_clear_status_register(const struct i2c_dt_spec *bus, enum tcpc_status_reg reg,
                                     uint16_t mask);

int tcpci_tcpm_mask_status_register(const struct i2c_dt_spec *bus, enum tcpc_status_reg reg,
                                    uint16_t mask);

int tcpci_tcpm_get_snk_ctrl(const struct i2c_dt_spec *bus, bool *sinking);

int tcpci_tcpm_get_src_ctrl(const struct i2c_dt_spec *bus, bool *sourcing);

int tcpci_tcpm_set_snk_ctrl(const struct i2c_dt_spec *bus, bool enable);

int tcpci_tcpm_set_src_ctrl(const struct i2c_dt_spec *bus, bool enable);

int tcpci_tcpm_set_debug_accessory(const struct i2c_dt_spec *bus, bool enable);

int tcpci_tcpm_set_low_power_mode(const struct i2c_dt_spec *bus, bool enable);

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_TCPCI_PRIV_H_ */
```

## 857.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 373 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_TCPCI_PRIV_H_`。

## 857.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [zephyr/usb_c/usbc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)
- [tcpci_reg_dump_map](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#ad68dd201d76bfb2193567b8db2ec514a)
- [name](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#a316d7f2a6b4b5fd42eb6450a810b7dd8)
- [size](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#a6e84093c1d027233230d8f27b0698756)
- [tcpci_std_regs](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ab2204d54c7483fb06f02dda83b0066f8)
- [TCPCI_STD_REGS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a031fe5b188cbe9b4e80e9cff0c845eda)
- [tcpci_read_reg8](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aaad4be0dbc4c31e9d3438b7f8a3e8433)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)
- [tcpci_write_reg8](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#abbe63527659134a5bc14d6ecefabb0af)
- [tcpci_update_reg8](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a2f4e5571a7f272dd968dc002d70ef3f4)
- [tcpci_read_reg16](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a00557a03647d6bd1ecba157ffff40e46)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [tcpci_write_reg16](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a7db13212d494bcc8c98190f8670fcd34)
- [tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)
- [tcpci_alert_reg_to_enum](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#abafd9380a335483525d8ff5b2b9e2306)
- [tcpci_tcpm_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ade1aa43041be0cc1abcf074b8e4e07e9)
- [tc_cc_voltage_state](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga64e32ec2da97f70fd5b96975317cb92c)
- [tcpci_tcpm_get_chip_info](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a49a2f453d03c75aaea608a17a85a6c6f)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [tcpci_tcpm_dump_std_reg](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a005a5b7130913ba80ff21d89f6d0c8a7)
- [tcpci_tcpm_set_bist_test_mode](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#add2b2c0859e4ab1cf2f0e290e1d71d19)
- [tcpci_tcpm_transmit_data](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a8ac9f08daf0f50749e9df389d1c8d41f)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [tcpci_tcpm_select_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ae2a60d3000187f640331816edbbcbcb6)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tcpci_tcpm_get_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a2233ff710864ba8ec40f7792e6baf002)
- [tcpci_tcpm_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a56b77c066ecd306d98a9e8e7ca249dc6)
- [tc_cc_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga0200c820510eb786f3ca30a9b5f7aada)
- [tcpci_tcpm_set_drp_toggle](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a3da565a529db5a6d337cf7f8642be8ab)
- [tcpci_tcpm_set_roles](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a0b0efcd606bdd19925ebaaaed017e5f9)
- [pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)
- [tc_power_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga6b98bbe238e62cfd5531688494a63de2)
- [tcpci_tcpm_set_rx_type](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a0223089c1ab73b1ec8c5a2e9de9b2932)
- [tcpci_tcpm_set_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a87aec00974ff403a0e60b1ee1346ec73)
- [tc_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gac5b4b58840c9b076a869a5816ba100db)
- [tcpci_tcpm_set_vconn](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ac37957893c769d805d997a93198827a7)
- [tcpci_tcpm_get_alert_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a33e3ccf31b7449667b3cf6429c243baa)
- [tcpci_tcpm_get_cc_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aa2fe9bdb8a6dc0d451f26fb854d2bb15)
- [tcpci_tcpm_get_power_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a75bab88b3a68acf79a3f2dae53756333)
- [tcpci_tcpm_get_fault_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#acf5218a19598dcec80ab3f7c16b637e9)
- [tcpci_tcpm_get_extended_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a01b6202cf0978d608689d36fdbc9416a)
- [tcpci_tcpm_get_extended_alert_status](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ac72769df523625b5ac60e9eb1807bbab)
- [tcpci_tcpm_clear_status_register](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aef29ca84b4cc68a55b840e987ec87f28)
- [tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)
- [tcpci_tcpm_mask_status_register](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aadbf2ef0350b8c54c4da53b7ab79f7d6)
- [tcpci_tcpm_get_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a338bd0bfb0df0fa3e4004dce85a7336b)
- [tcpci_tcpm_get_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a9be63be44b19198cd8d49f95e971ee6d)
- [tcpci_tcpm_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#ac6848fa7e70af270d4471309589100f4)
- [tcpci_tcpm_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aadac3408a1aea5e56c2578f3843c032a)
- [tcpci_tcpm_set_debug_accessory](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#a269a35fb98ec53dba41fa53c78683ae2)
- [tcpci_tcpm_set_low_power_mode](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h.html#aa86dd25de3d91ac61abc06f0c734046f)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [tcpci_reg_dump_map::name](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#a316d7f2a6b4b5fd42eb6450a810b7dd8)
- [tcpci_reg_dump_map::size](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#a6e84093c1d027233230d8f27b0698756)
- [tcpci_reg_dump_map::addr](../device_power_control_model_reference/P095_tcpci_reg_dump_map_结构体.md#ad68dd201d76bfb2193567b8db2ec514a)
- [usbc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)

---

[上一章](P856_tcp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P858_tcs3400.h_源码浏览.md)
