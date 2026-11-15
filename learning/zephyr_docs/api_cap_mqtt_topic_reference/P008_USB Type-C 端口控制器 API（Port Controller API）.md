---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-8
title: USB Type-C 端口控制器 API（Port Controller API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_USB Type-C 端口控制器 API（Port Controller API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB Type-C 端口控制器 API（Port Controller API）

<a id="details"></a>

USB Type-C 端口控制器 API（Port Controller API）。自（Since）3.1 起提供，版本（Version）0.1.1。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_usb_5Ftype_5Fc_5Fport_5Fcontroller_5Fapi_5Fbackend"></a>

相关声明：[USB Type-C 端口控制器驱动后端 API](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 8.2\_文件（Files）

<a id="r_tcpci_5Fpriv_2Eh"></a>

```c
file tcpci_priv.h
```

相关声明：[tcpci_priv.h](../api_file_power_ots_reference/P005_zephyr__drivers__usb_c__tcpci_priv.h_文件参考.md)。

符合Type-C端口控制器接口（TCPCI）的驱动所用的辅助函数。

<a id="r_usbc_5Ftcpc_2Eh"></a>

```c
file usbc_tcpc.h
```

相关声明：[usbc_tcpc.h](../api_file_network_pcie_reference/P014_zephyr__drivers__usb_c__usbc_tcpc.h_文件参考.md)。

USB-C Type-C端口控制器（Port Controller）的设备API。

<a id="r_tcpci_2Eh"></a>

```c
file tcpci.h
```

相关声明：[tcpci.h](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html)。

Type-C端口控制器接口（Port Controller Interface）的寄存器与字段定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.3\_数据结构（Data Structures）

<a id="r_tcpc_5Fchip_5Finfo"></a>

```c
struct tcpc_chip_info
```

相关声明：[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

Type-C端口控制器（TCPC）的芯片信息。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.4\_类型定义（Typedefs）

<a id="r_ga073ad4a46a5ea1f9e5cad45488d672f0"></a>

```c
typedef int(* tcpc_vconn_control_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

相关声明：[tcpc_vconn_control_cb_t](#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

VCONN 控制回调类型（VCONN Control Callback Type）。

<a id="r_ga4d2b77f6ee685d1bff1117843150e664"></a>

```c
typedef int(* tcpc_vconn_discharge_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

相关声明：[tcpc_vconn_discharge_cb_t](#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

VCONN 放电回调类型（VCONN Discharge Callback Type）。

<a id="r_ga5f42fa12f90d34961eeeb67c0dc4f925"></a>

```c
typedef void(* tcpc_alert_handler_cb_t) (const struct device *dev, void *data, enum tcpc_alert alert)
```

相关声明：[tcpc_alert_handler_cb_t](#ga5f42fa12f90d34961eeeb67c0dc4f925)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert](#ga4687047910cad0dd970bbd28adcf22ed)。

处理 TCPC 警报事件（TCPC Alert Events）的回调类型（Callback Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.5\_枚举（Enumerations）

<a id="r_ga4687047910cad0dd970bbd28adcf22ed"></a>

```c
enum tcpc_alert { TCPC_ALERT_CC_STATUS , TCPC_ALERT_POWER_STATUS , TCPC_ALERT_MSG_STATUS , TCPC_ALERT_HARD_RESET_RECEIVED , TCPC_ALERT_TRANSMIT_MSG_FAILED , TCPC_ALERT_TRANSMIT_MSG_DISCARDED , TCPC_ALERT_TRANSMIT_MSG_SUCCESS , TCPC_ALERT_VBUS_ALARM_HI , TCPC_ALERT_VBUS_ALARM_LO , TCPC_ALERT_FAULT_STATUS , TCPC_ALERT_RX_BUFFER_OVERFLOW , TCPC_ALERT_VBUS_SNK_DISCONNECT , TCPC_ALERT_BEGINNING_MSG_STATUS , TCPC_ALERT_EXTENDED_STATUS , TCPC_ALERT_EXTENDED , TCPC_ALERT_VENDOR_DEFINED }
```

相关声明：[tcpc_alert](#ga4687047910cad0dd970bbd28adcf22ed)、[TCPC_ALERT_CC_STATUS](#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f)、[TCPC_ALERT_POWER_STATUS](#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4)、[TCPC_ALERT_MSG_STATUS](#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb)、[TCPC_ALERT_HARD_RESET_RECEIVED](#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0)、[TCPC_ALERT_TRANSMIT_MSG_FAILED](#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec)、[TCPC_ALERT_TRANSMIT_MSG_DISCARDED](#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe)、[TCPC_ALERT_TRANSMIT_MSG_SUCCESS](#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2)、[TCPC_ALERT_VBUS_ALARM_HI](#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66)、[TCPC_ALERT_VBUS_ALARM_LO](#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0)、[TCPC_ALERT_FAULT_STATUS](#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e)、[TCPC_ALERT_RX_BUFFER_OVERFLOW](#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752)、[TCPC_ALERT_VBUS_SNK_DISCONNECT](#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd)、[TCPC_ALERT_BEGINNING_MSG_STATUS](#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb)、[TCPC_ALERT_EXTENDED_STATUS](#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9)、[TCPC_ALERT_EXTENDED](#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25)、[TCPC_ALERT_VENDOR_DEFINED](#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)。

TCPC 警报位（Alert Bits）。

<a id="r_gafd8253dfa6abc80d0717b17271ed8916"></a>

```c
enum tcpc_status_reg { TCPC_ALERT_STATUS , TCPC_CC_STATUS , TCPC_POWER_STATUS , TCPC_FAULT_STATUS , TCPC_EXTENDED_STATUS , TCPC_EXTENDED_ALERT_STATUS , TCPC_VENDOR_DEFINED_STATUS }
```

相关声明：[tcpc_status_reg](#gafd8253dfa6abc80d0717b17271ed8916)、[TCPC_ALERT_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b)、[TCPC_CC_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4)、[TCPC_POWER_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f)、[TCPC_FAULT_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440)、[TCPC_EXTENDED_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d)、[TCPC_EXTENDED_ALERT_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db)、[TCPC_VENDOR_DEFINED_STATUS](#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)。

TCPC 状态寄存器（Status Register）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.6\_函数（Functions）

<a id="r_ga6dfd68915ffe093058f6187b770a2436"></a>

```c
static int tcpc_is_cc_rp (enum tc_cc_voltage_state cc)
```

相关声明：[tcpc_is_cc_rp](#ga6dfd68915ffe093058f6187b770a2436)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

返回受电端（Sink）是否在对端检测到 Rp 电阻。

<a id="r_ga0db896e395812603a03548b8faac6791"></a>

```c
static int tcpc_is_cc_open (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_open](#ga0db896e395812603a03548b8faac6791)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

两条 CC 线路都完全开路（Completely Open）时返回 `true`。

<a id="r_gaa0d2059c3a53df986150141f73b9a98a"></a>

```c
static int tcpc_is_cc_snk_dbg_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_snk_dbg_acc](#gaa0d2059c3a53df986150141f73b9a98a)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

检测到端口伙伴（Port Partner）为受电端调试附件（Sink Debug Accessory）时返回 `true`。

<a id="r_ga03849a7a4fd7f468b18838c443d1ecd8"></a>

```c
static int tcpc_is_cc_src_dbg_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_src_dbg_acc](#ga03849a7a4fd7f468b18838c443d1ecd8)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

检测到端口伙伴（Port Partner）为供电端调试附件（Source Debug Accessory）时返回 `true`。

<a id="r_ga153054be89d5f21148fe3ee750c718ee"></a>

```c
static int tcpc_is_cc_audio_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_audio_acc](#ga153054be89d5f21148fe3ee750c718ee)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）为音频附件（Audio Accessory）时返回 `true`。

<a id="r_gab4e9cc812679cf8cb0189f73a28d7cd2"></a>

```c
static int tcpc_is_cc_at_least_one_rd (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_at_least_one_rd](#gab4e9cc812679cf8cb0189f73a28d7cd2)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）至少接入了一个 Rd 电阻时返回 `true`。

<a id="r_ga91c3c40ea82ce5a081918183d8b76c06"></a>

```c
static int tcpc_is_cc_only_one_rd (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_only_one_rd](#ga91c3c40ea82ce5a081918183d8b76c06)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）仅在一条 CC 线路上接入 Rd 电阻时返回 `true`。

<a id="r_gabc50daa9cc713b1d0e340007e3850ca8"></a>

```c
static int tcpc_init (const struct device *dev)
```

相关声明：[tcpc_init](#gabc50daa9cc713b1d0e340007e3850ca8)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Type-C 端口控制器（TCPC）。

<a id="r_ga66ab7a9f3cd1b80cd5bc8e99040c5627"></a>

```c
static int tcpc_get_cc (const struct device *dev, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

相关声明：[tcpc_get_cc](#ga66ab7a9f3cd1b80cd5bc8e99040c5627)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

读取 CC 线路状态（CC Line Status）。

<a id="r_ga3958eac0cc0b9b2ac782e0cdb235036c"></a>

```c
static int tcpc_select_rp_value (const struct device *dev, enum tc_rp_value rp)
```

相关声明：[tcpc_select_rp_value](#ga3958eac0cc0b9b2ac782e0cdb235036c)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

设置作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

<a id="r_ga25a110be90977e768623f3a0c9a222d5"></a>

```c
static int tcpc_get_rp_value (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[tcpc_get_rp_value](#ga25a110be90977e768623f3a0c9a222d5)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

<a id="r_gac5737d02caa2b9e649b469bcd648440f"></a>

```c
static int tcpc_set_cc (const struct device *dev, enum tc_cc_pull pull)
```

相关声明：[tcpc_set_cc](#gac5737d02caa2b9e649b469bcd648440f)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)。

设置 CC 上拉／下拉电阻（CC Pull Resistor），并将角色设为供电端（Source）或受电端（Sink）。

<a id="r_ga1f057bcddc5a7757370f2e6de8170128"></a>

```c
static void tcpc_set_vconn_cb (const struct device *dev, tcpc_vconn_control_cb_t vconn_cb, const struct device *usbc_dev)
```

相关声明：[tcpc_set_vconn_cb](#ga1f057bcddc5a7757370f2e6de8170128)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)。

设置可启用或禁用 VCONN 的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

<a id="r_ga71981a635ad82b9db41d549f29ad5c68"></a>

```c
static void tcpc_set_vconn_discharge_cb (const struct device *dev, tcpc_vconn_discharge_cb_t cb, const struct device *usbc_dev)
```

相关声明：[tcpc_set_vconn_discharge_cb](#ga71981a635ad82b9db41d549f29ad5c68)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)。

设置可启用 VCONN 或对其放电的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

<a id="r_ga3937d66636a2b22422caf11c48f7628a"></a>

```c
static int tcpc_vconn_discharge (const struct device *dev, bool enable)
```

相关声明：[tcpc_vconn_discharge](#ga3937d66636a2b22422caf11c48f7628a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

对 VCONN 放电（Discharge VCONN）。

<a id="r_ga247f0ea91249753d6f5eefe006617e41"></a>

```c
static int tcpc_set_vconn (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_vconn](#ga247f0ea91249753d6f5eefe006617e41)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN。

<a id="r_ga8d30c961335f62faa33aa7d842422da0"></a>

```c
static int tcpc_set_roles (const struct device *dev, enum tc_power_role power_role, enum tc_data_role data_role)
```

相关声明：[tcpc_set_roles](#ga8d30c961335f62faa33aa7d842422da0)、[device](../device_reference/P002_设备对象结构.md)、[tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)。

设置 PD 消息头部（PD Message Header）的电源角色（Power Role）和数据角色（Data Role）。

<a id="r_ga34e4caefb0f660b170f97956ac57b707"></a>

```c
static int tcpc_get_rx_pending_msg (const struct device *dev, struct pd_msg *buf)
```

相关声明：[tcpc_get_rx_pending_msg](#ga34e4caefb0f660b170f97956ac57b707)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

从 TCPC 获取电力传输消息（Power Delivery Message）。

<a id="r_ga905176a77ff127f4df8f6a4f2c61a1b7"></a>

```c
static int tcpc_set_rx_enable (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_rx_enable](#ga905176a77ff127f4df8f6a4f2c61a1b7)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 SOP* 消息类型的接收（Reception）。

<a id="r_ga53f0207ecb63011c6dfc3c298a841ed4"></a>

```c
static int tcpc_set_cc_polarity (const struct device *dev, enum tc_cc_polarity polarity)
```

相关声明：[tcpc_set_cc_polarity](#ga53f0207ecb63011c6dfc3c298a841ed4)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)。

设置 CC 线路极性（CC Line Polarity）。

<a id="r_ga8bf8fd202d582a4cc179a0fc4aff35e1"></a>

```c
static int tcpc_transmit_data (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_transmit_data](#ga8bf8fd202d582a4cc179a0fc4aff35e1)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

发送电力传输消息（Power Delivery Message）。

<a id="r_ga91eef7084b523f1991e000f0592b8cbd"></a>

```c
static int tcpc_dump_std_reg (const struct device *dev)
```

相关声明：[tcpc_dump_std_reg](#ga91eef7084b523f1991e000f0592b8cbd)、[device](../device_reference/P002_设备对象结构.md)。

转储一组 TCPC 寄存器（Registers）。

<a id="r_ga75f0dc246dac576f14c5ac51b45fd489"></a>

```c
static int tcpc_set_alert_handler_cb (const struct device *dev, tcpc_alert_handler_cb_t handler, void *data)
```

相关声明：[tcpc_set_alert_handler_cb](#ga75f0dc246dac576f14c5ac51b45fd489)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert_handler_cb_t](#ga5f42fa12f90d34961eeeb67c0dc4f925)。

设置警报函数（Alert Function），由警报位（Alert Bit）触发中断时调用。

<a id="r_ga0d1868d555e99877e062fb7135d9db8f"></a>

```c
static int tcpc_mask_status_register (const struct device *dev, enum tcpc_status_reg reg, uint32_t mask)
```

相关声明：[tcpc_mask_status_register](#ga0d1868d555e99877e062fb7135d9db8f)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_status_reg](#gafd8253dfa6abc80d0717b17271ed8916)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 TCPC 状态寄存器的掩码（Status Register Mask）。

<a id="r_ga01687aa218b25ba137e994a2a55bce23"></a>

```c
static int tcpc_set_debug_accessory (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_debug_accessory](#ga01687aa218b25ba137e994a2a55bce23)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

手动控制 TCPC 调试附件控制功能（DebugAccessory Control）。

<a id="r_gaaa38e56e6bc8c41e936d8ed70aaa8a23"></a>

```c
static int tcpc_set_debug_detach (const struct device *dev)
```

相关声明：[tcpc_set_debug_detach](#gaaa38e56e6bc8c41e936d8ed70aaa8a23)、[device](../device_reference/P002_设备对象结构.md)。

从调试连接（Debug Connection）断开。

<a id="r_gaa06e156bef46ff3f70cc8c302ddf0a4d"></a>

```c
static int tcpc_set_drp_toggle (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_drp_toggle](#gaa06e156bef46ff3f70cc8c302ddf0a4d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 TCPC 自动双角色切换（Auto Dual Role Toggle）。

<a id="r_ga0c1cd7bc86c89abf5e348987d34e4623"></a>

```c
static int tcpc_get_snk_ctrl (const struct device *dev)
```

相关声明：[tcpc_get_snk_ctrl](#ga0c1cd7bc86c89abf5e348987d34e4623)、[device](../device_reference/P002_设备对象结构.md)。

查询 TCPC 当前受电状态（Sinking State）。

<a id="r_ga7a63d55cbe5de1d89aa76e10df0140ed"></a>

```c
static int tcpc_set_snk_ctrl (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_snk_ctrl](#ga7a63d55cbe5de1d89aa76e10df0140ed)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 TCPC 的 VBUS 受电状态（VBUS Sinking State）。

<a id="r_ga03c8c6fc6f4c6adefacbc809588e1f85"></a>

```c
static int tcpc_get_src_ctrl (const struct device *dev)
```

相关声明：[tcpc_get_src_ctrl](#ga03c8c6fc6f4c6adefacbc809588e1f85)、[device](../device_reference/P002_设备对象结构.md)。

查询 TCPC 当前供电状态（Sourcing State）。

<a id="r_ga8f06b257d1bd0a17eb3042d204b2e6cd"></a>

```c
static int tcpc_set_src_ctrl (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_src_ctrl](#ga8f06b257d1bd0a17eb3042d204b2e6cd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 TCPC 的 VBUS 供电状态（VBUS Sourcing State）。

<a id="r_gaccc728a1f27c59a163a5c0a221ab7c18"></a>

```c
static int tcpc_set_bist_test_mode (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_bist_test_mode](#gaccc728a1f27c59a163a5c0a221ab7c18)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制 TCPC 的内建自测试模式（BIST Mode）。

<a id="r_ga894d24140f8675b4f48d759c27f52076"></a>

```c
static int tcpc_get_chip_info (const struct device *dev, struct tcpc_chip_info *chip_info)
```

相关声明：[tcpc_get_chip_info](#ga894d24140f8675b4f48d759c27f52076)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

获取 TCPC 固件版本（Firmware Version）。

<a id="r_ga961a4dc393d58dc44ea19a62c943ed48"></a>

```c
static int tcpc_set_low_power_mode (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_low_power_mode](#ga961a4dc393d58dc44ea19a62c943ed48)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

指示 TCPC 进入或退出低功耗模式（Low Power Mode）。

<a id="r_gab0f1f5d47c1e2b8ee9eb3d7875a0051e"></a>

```c
static int tcpc_sop_prime_enable (const struct device *dev, bool enable)
```

相关声明：[tcpc_sop_prime_enable](#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 SOP Prime 消息的接收，并可选择启用 SOP Double Prime 消息的接收。

<a id="r_gaac29d0958fd377db24f1911cfa03188c"></a>

```c
static int tcpc_dead_battery_enabled (const struct device *dev, bool *enabled)
```

相关声明：[tcpc_dead_battery_enabled](#gaac29d0958fd377db24f1911cfa03188c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPC 是否施加 USB-C 电池耗尽端接（Dead Battery Terminations）。

## 8.7\_详细说明（Detailed Documentation）

<a id="ga5f42fa12f90d34961eeeb67c0dc4f925"></a>

### `tcpc_alert_handler_cb_t`

```c
typedef void(* tcpc_alert_handler_cb_t) (const struct device *dev, void *data, enum tcpc_alert alert)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

处理 TCPC 警报事件（TCPC Alert Events）的回调类型（Callback Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `data` | 通过 `tcpc_set_alert_handler_cb` 注册回调时传入的用户数据（User Data）。 |
| `alert` | 触发的告警类型（Alert Type）。 |

<a id="ga073ad4a46a5ea1f9e5cad45488d672f0"></a>

### `tcpc_vconn_control_cb_t`

```c
typedef int(* tcpc_vconn_control_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

VCONN 控制回调类型（VCONN Control Callback Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tcpc_dev` | 运行时 `tcpc` 设备结构体（Device Structure）。 |
| `usbc_dev` | 运行时 `usbc` 设备结构体（Device Structure）。 |
| `pol` | CC 极性（Polarity），指示哪条 CC 线路承载 VCONN。 |
| `enable` | 为 `true` 时启用 VCONN，为 `false` 时禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |

<a id="ga4d2b77f6ee685d1bff1117843150e664"></a>

### `tcpc_vconn_discharge_cb_t`

```c
typedef int(* tcpc_vconn_discharge_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

VCONN 放电回调类型（VCONN Discharge Callback Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tcpc_dev` | 运行时 `tcpc` 设备结构体（Device Structure）。 |
| `usbc_dev` | 运行时 `usbc` 设备结构体（Device Structure）。 |
| `pol` | CC 极性（Polarity），指示哪条 CC 线路承载 VCONN。 |
| `enable` | 为 `true` 时启用 VCONN 放电（Discharge），为 `false` 时禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |

<a id="ga4687047910cad0dd970bbd28adcf22ed"></a>

### `tcpc_alert`

```c
enum tcpc_alert
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

TCPC 警报位（Alert Bits）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TCPC_ALERT_CC_STATUS` | CC 状态（CC Status）已改变。 |
| `TCPC_ALERT_POWER_STATUS` | 电源状态（Power Status）已改变。 |
| `TCPC_ALERT_MSG_STATUS` | 接收缓冲区寄存器（Receive Buffer Register）已改变。 |
| `TCPC_ALERT_HARD_RESET_RECEIVED` | 收到硬复位消息（Hard Reset Message）。 |
| `TCPC_ALERT_TRANSMIT_MSG_FAILED` | SOP* 消息发送未成功。 |
| `TCPC_ALERT_TRANSMIT_MSG_DISCARDED` | 由于有接收消息到达，未发送复位或 SOP* 消息。 |
| `TCPC_ALERT_TRANSMIT_MSG_SUCCESS` | 复位或 SOP* 消息发送成功。 |
| `TCPC_ALERT_VBUS_ALARM_HI` | 发生高电压告警（High-Voltage Alarm）。 |
| `TCPC_ALERT_VBUS_ALARM_LO` | 发生低电压告警（Low-Voltage Alarm）。 |
| `TCPC_ALERT_FAULT_STATUS` | 发生故障（Fault）。读取 `FAULT_STATUS` 寄存器。 |
| `TCPC_ALERT_RX_BUFFER_OVERFLOW` | TCPC 接收缓冲区（RX Buffer）已溢出。 |
| `TCPC_ALERT_VBUS_SNK_DISCONNECT` | 处于 `Attached.SNK` 状态的 TCPC 检测到受电端断开（Sink Disconnect）。 |
| `TCPC_ALERT_BEGINNING_MSG_STATUS` | 接收缓冲区寄存器（Receive Buffer Register）已改变。 |
| `TCPC_ALERT_EXTENDED_STATUS` | 扩展状态（Extended Status）已改变。 |
| `TCPC_ALERT_EXTENDED` | 发生扩展中断事件（Extended Interrupt Event）。读取 `alert_extended` 寄存器。 |
| `TCPC_ALERT_VENDOR_DEFINED` | 检测到厂商定义告警（Vendor Defined Alert）。 |

<a id="gafd8253dfa6abc80d0717b17271ed8916"></a>

### `tcpc_status_reg`

```c
enum tcpc_status_reg
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

TCPC 状态寄存器（Status Register）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TCPC_ALERT_STATUS` | 告警寄存器（Alert Register）。 |
| `TCPC_CC_STATUS` | CC 状态寄存器（CC Status Register）。 |
| `TCPC_POWER_STATUS` | 电源状态寄存器（Power Status Register）。 |
| `TCPC_FAULT_STATUS` | 故障状态寄存器（Fault Status Register）。 |
| `TCPC_EXTENDED_STATUS` | 扩展状态寄存器（Extended Status Register）。 |
| `TCPC_EXTENDED_ALERT_STATUS` | 扩展告警状态寄存器（Extended Alert Status Register）。 |
| `TCPC_VENDOR_DEFINED_STATUS` | 厂商定义状态寄存器（Vendor Defined Status Register）。 |

<a id="gaac29d0958fd377db24f1911cfa03188c"></a>

### `tcpc_dead_battery_enabled()`

```c
int tcpc_dead_battery_enabled ( const struct device * dev, bool * enabled )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 TCPC 是否施加 USB-C 电池耗尽端接（Dead Battery Terminations）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enabled` | TCPC 应用了电池耗尽终端配置（Dead Battery Terminations）时为 `true`，否则为 `false`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga91eef7084b523f1991e000f0592b8cbd"></a>

### `tcpc_dump_std_reg()`

```c
int tcpc_dump_std_reg ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

转储一组 TCPC 寄存器（Registers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga66ab7a9f3cd1b80cd5bc8e99040c5627"></a>

### `tcpc_get_cc()`

```c
int tcpc_get_cc ( const struct device * dev, enum tc_cc_voltage_state * cc1, enum tc_cc_voltage_state * cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

读取 CC 线路状态（CC Line Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cc1` | 用于写入 CC1 状态的指针。 |
| `cc2` | 用于写入 CC2 状态的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga894d24140f8675b4f48d759c27f52076"></a>

### `tcpc_get_chip_info()`

```c
int tcpc_get_chip_info ( const struct device * dev, struct tcpc_chip_info * chip_info )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

获取 TCPC 固件版本（Firmware Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `chip_info` | 指向用于存储版本信息的 TCPC 芯片信息（Chip Info）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga25a110be90977e768623f3a0c9a222d5"></a>

### `tcpc_get_rp_value()`

```c
int tcpc_get_rp_value ( const struct device * dev, enum tc_rp_value * rp )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

获取作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `rp` | 用于存储上拉电阻（Pull-Up Resistor）值的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现时。 |
| `-EIO` | 失败。 |

<a id="ga34e4caefb0f660b170f97956ac57b707"></a>

### `tcpc_get_rx_pending_msg()`

```c
int tcpc_get_rx_pending_msg ( const struct device * dev, struct pd_msg * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

从 TCPC 获取电力传输消息（Power Delivery Message）。

`buf` 为 `NULL` 时，仅返回状态：0 表示有待处理消息，`-ENODATA` 表示没有待处理消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `buf` | 用于写入 `pd_buf` 指针的位置；仅检查状态时为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Greater` | 提供 `buf` 参数时，大于或等于 0 的返回值表示收到的字节数。 |
| `0` | 存在待处理消息，且 `buf` 参数为 `NULL` 时。 |
| `-EIO` | 失败。 |
| `-ENODATA` | 没有待处理消息时。 |

<a id="ga0c1cd7bc86c89abf5e348987d34e4623"></a>

### `tcpc_get_snk_ctrl()`

```c
int tcpc_get_snk_ctrl ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 TCPC 当前受电状态（Sinking State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 正在受电（Sinking Power）时。 |
| `false` | 未在受电（Sinking Power）时。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga03c8c6fc6f4c6adefacbc809588e1f85"></a>

### `tcpc_get_src_ctrl()`

```c
int tcpc_get_src_ctrl ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 TCPC 当前供电状态（Sourcing State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 正在供电（Sourcing Power）时。 |
| `false` | 未在供电（Sourcing Power）时。 |
| `-ENOSYS` | 未实现时。 |

<a id="gabc50daa9cc713b1d0e340007e3850ca8"></a>

### `tcpc_init()`

```c
int tcpc_init ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

初始化 Type-C 端口控制器（TCPC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-EAGAIN` | 应推迟初始化（Initialization）时。 |

<a id="gab4e9cc812679cf8cb0189f73a28d7cd2"></a>

### `tcpc_is_cc_at_least_one_rd()`

```c
int tcpc_is_cc_at_least_one_rd ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

端口伙伴（Port Partner）至少接入了一个 Rd 电阻时返回 `true`。

<a id="ga153054be89d5f21148fe3ee750c718ee"></a>

### `tcpc_is_cc_audio_acc()`

```c
int tcpc_is_cc_audio_acc ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

端口伙伴（Port Partner）为音频附件（Audio Accessory）时返回 `true`。

<a id="ga91c3c40ea82ce5a081918183d8b76c06"></a>

### `tcpc_is_cc_only_one_rd()`

```c
int tcpc_is_cc_only_one_rd ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

端口伙伴（Port Partner）仅在一条 CC 线路上接入 Rd 电阻时返回 `true`。

<a id="ga0db896e395812603a03548b8faac6791"></a>

### `tcpc_is_cc_open()`

```c
int tcpc_is_cc_open ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

两条 CC 线路都完全开路（Completely Open）时返回 `true`。

<a id="ga6dfd68915ffe093058f6187b770a2436"></a>

### `tcpc_is_cc_rp()`

```c
int tcpc_is_cc_rp ( enum tc_cc_voltage_state cc)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

返回受电端（Sink）是否在对端检测到 Rp 电阻。

<a id="gaa0d2059c3a53df986150141f73b9a98a"></a>

### `tcpc_is_cc_snk_dbg_acc()`

```c
int tcpc_is_cc_snk_dbg_acc ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

检测到端口伙伴（Port Partner）为受电端调试附件（Sink Debug Accessory）时返回 `true`。

<a id="ga03849a7a4fd7f468b18838c443d1ecd8"></a>

### `tcpc_is_cc_src_dbg_acc()`

```c
int tcpc_is_cc_src_dbg_acc ( enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

检测到端口伙伴（Port Partner）为供电端调试附件（Source Debug Accessory）时返回 `true`。

<a id="ga0d1868d555e99877e062fb7135d9db8f"></a>

### `tcpc_mask_status_register()`

```c
int tcpc_mask_status_register ( const struct device * dev, enum tcpc_status_reg reg, uint32_t mask )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 TCPC 状态寄存器的掩码（Status Register Mask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `reg` | 要读取的状态寄存器（Status Register）。 |
| `mask` | 状态寄存器的位掩码（Bit Mask）。对应位为 0 时屏蔽该状态位，否则不屏蔽。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga3958eac0cc0b9b2ac782e0cdb235036c"></a>

### `tcpc_select_rp_value()`

```c
int tcpc_select_rp_value ( const struct device * dev, enum tc_rp_value rp )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `rp` | 上拉电阻（Pull-Up Resistor）的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现时。 |
| `-EIO` | 失败。 |

<a id="ga75f0dc246dac576f14c5ac51b45fd489"></a>

### `tcpc_set_alert_handler_cb()`

```c
int tcpc_set_alert_handler_cb ( const struct device * dev, tcpc_alert_handler_cb_t handler, void * data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置警报函数（Alert Function），由警报位（Alert Bit）触发中断时调用。

调用此函数会启用特定的告警位（Alert Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `handler` | 该位置位时调用的回调函数（Callback Function）。 |
| `data` | 传给回调的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 失败。 |

<a id="gaccc728a1f27c59a163a5c0a221ab7c18"></a>

### `tcpc_set_bist_test_mode()`

```c
int tcpc_set_bist_test_mode ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

控制 TCPC 的内建自测试模式（BIST Mode）。

此模式激活期间禁用接收告警（RX Alerts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时，TCPC 进入内建自测试模式（BIST TEST Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="gac5737d02caa2b9e649b469bcd648440f"></a>

### `tcpc_set_cc()`

```c
int tcpc_set_cc ( const struct device * dev, enum tc_cc_pull pull )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 CC 上拉／下拉电阻（CC Pull Resistor），并将角色设为供电端（Source）或受电端（Sink）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `pull` | 要设置的上拉／下拉电阻（Pull Resistor）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |

<a id="ga53f0207ecb63011c6dfc3c298a841ed4"></a>

### `tcpc_set_cc_polarity()`

```c
int tcpc_set_cc_polarity ( const struct device * dev, enum tc_cc_polarity polarity )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 CC 线路极性（CC Line Polarity）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `polarity` | CC 线路的极性（Polarity）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |

<a id="ga01687aa218b25ba137e994a2a55bce23"></a>

### `tcpc_set_debug_accessory()`

```c
int tcpc_set_debug_accessory ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

手动控制 TCPC 调试附件控制功能（DebugAccessory Control）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时启用调试附件（Debug Accessory），否则禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="gaaa38e56e6bc8c41e936d8ed70aaa8a23"></a>

### `tcpc_set_debug_detach()`

```c
int tcpc_set_debug_detach ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

从调试连接（Debug Connection）断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="gaa06e156bef46ff3f70cc8c302ddf0a4d"></a>

### `tcpc_set_drp_toggle()`

```c
int tcpc_set_drp_toggle ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用 TCPC 自动双角色切换（Auto Dual Role Toggle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时启用自动双角色切换（Auto Dual Role Toggle），否则禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga961a4dc393d58dc44ea19a62c943ed48"></a>

### `tcpc_set_low_power_mode()`

```c
int tcpc_set_low_power_mode ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

指示 TCPC 进入或退出低功耗模式（Low Power Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时，TCPC 进入低功耗模式（Low Power Mode），否则退出。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga8d30c961335f62faa33aa7d842422da0"></a>

### `tcpc_set_roles()`

```c
int tcpc_set_roles ( const struct device * dev, enum tc_power_role power_role, enum tc_data_role data_role )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 PD 消息头部（PD Message Header）的电源角色（Power Role）和数据角色（Data Role）。

每次数据角色／电源角色（Data/Power Role）改变，只需调用此函数一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `power_role` | 当前电源角色（Power Role）。 |
| `data_role` | 当前数据角色（Data Role）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga905176a77ff127f4df8f6a4f2c61a1b7"></a>

### `tcpc_set_rx_enable()`

```c
int tcpc_set_rx_enable ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用 SOP* 消息类型的接收（Reception）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时启用电力传输（Power Delivery），否则禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga7a63d55cbe5de1d89aa76e10df0140ed"></a>

### `tcpc_set_snk_ctrl()`

```c
int tcpc_set_snk_ctrl ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 TCPC 的 VBUS 受电状态（VBUS Sinking State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 要启用受电（Sinking）时为 `true`，要禁用时为 `false`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga8f06b257d1bd0a17eb3042d204b2e6cd"></a>

### `tcpc_set_src_ctrl()`

```c
int tcpc_set_src_ctrl ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 TCPC 的 VBUS 供电状态（VBUS Sourcing State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 要启用供电（Sourcing）时为 `true`，要禁用时为 `false`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga247f0ea91249753d6f5eefe006617e41"></a>

### `tcpc_set_vconn()`

```c
int tcpc_set_vconn ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 VCONN。

此函数在可能的情况下使用 TCPC 测量 VCONN，否则调用通过 `tcpc_set_vconn_cb` 设置的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时启用 VCONN，否则禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga1f057bcddc5a7757370f2e6de8170128"></a>

### `tcpc_set_vconn_cb()`

```c
void tcpc_set_vconn_cb ( const struct device * dev, tcpc_vconn_control_cb_t vconn_cb, const struct device * usbc_dev )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置可启用或禁用 VCONN 的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

`vconn_cb` 不为 `NULL` 时，在 `tcpc_set_vconn` 函数中调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `vconn_cb` | 指向控制 VCONN 的回调函数的指针。 |
| `usbc_dev` | USB-C 连接器设备（Connector Device）。 |

<a id="ga71981a635ad82b9db41d549f29ad5c68"></a>

### `tcpc_set_vconn_discharge_cb()`

```c
void tcpc_set_vconn_discharge_cb ( const struct device * dev, tcpc_vconn_discharge_cb_t cb, const struct device * usbc_dev )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置可启用 VCONN 或对其放电的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

`cb` 不为 `NULL` 时，在 `tcpc_vconn_discharge` 函数中调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 指向使 VCONN 放电（Discharge）的回调函数的指针。 |
| `usbc_dev` | USB-C 连接器设备（Connector Device）。 |

<a id="gab0f1f5d47c1e2b8ee9eb3d7875a0051e"></a>

### `tcpc_sop_prime_enable()`

```c
int tcpc_sop_prime_enable ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用 SOP Prime 消息的接收，并可选择启用 SOP Double Prime 消息的接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时可接收 SOP Prime 与 SOP Double Prime 消息，否则不能接收。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga8bf8fd202d582a4cc179a0fc4aff35e1"></a>

### `tcpc_transmit_data()`

```c
int tcpc_transmit_data ( const struct device * dev, struct pd_msg * msg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

发送电力传输消息（Power Delivery Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `msg` | 要发送的电力传输消息（Power Delivery Message）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |

<a id="ga3937d66636a2b22422caf11c48f7628a"></a>

### `tcpc_vconn_discharge()`

```c
int tcpc_vconn_discharge ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

对 VCONN 放电（Discharge VCONN）。

此函数在可能的情况下使用 TCPC 对 VCONN 放电（Discharge），否则调用通过 `tcpc_set_vconn_cb` 设置的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 `true` 时启用 VCONN 放电（Discharge），否则禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOSYS` | 未实现时。 |


## 8.8\_原页交叉引用（Cross References）

- [USB Type-C 端口控制器驱动后端 API](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md)
- [tcpci_priv.h](../api_file_power_ots_reference/P005_zephyr__drivers__usb_c__tcpci_priv.h_文件参考.md)
- [usbc_tcpc.h](../api_file_network_pcie_reference/P014_zephyr__drivers__usb_c__usbc_tcpc.h_文件参考.md)
- [tcpci.h](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)
- [tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)
- [tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9"></a>
<a id="gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25"></a>
<a id="gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db"></a>
<a id="ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_MQTT 客户端库.md) · [返回大纲](大纲.md)
