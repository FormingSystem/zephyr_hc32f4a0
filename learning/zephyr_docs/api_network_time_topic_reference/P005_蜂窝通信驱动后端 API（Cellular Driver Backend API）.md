---
id: learning.zephyr-docs.api-network-time-topic-reference.page-5
title: 蜂窝通信驱动后端 API（Cellular Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_蜂窝通信驱动后端 API（Cellular Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现蜂窝网络（Cellular）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-groups"></a>
<a id="groups"></a>

## 5.1\_主题（Topics）

<a id="r_modem_5Fcellular_5Fbackend"></a>

相关声明：[蜂窝调制解调器辅助功能（Cellular modem helpers）](../api_protocol_topic_reference/P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md)。

使用通用的 AT 交互（Chat）、连接多路复用（CMUX）、点对点协议（PPP）和电源管理支持，实现供应商特定的蜂窝调制解调器驱动。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.2\_数据结构（Data Structures）

<a id="r_cellular_5Fdriver_5Fapi"></a>

```c
struct cellular_driver_api
```

相关声明：[cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)。

驱动操作（Driver Operations）：蜂窝通信（Cellular）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_ga71ddc5b9e09da398d02caadc91ef3cfc"></a>

```c
typedef int(* cellular_api_configure_networks) (const struct device *dev, const struct cellular_network *networks, uint8_t size)
```

相关声明：[cellular_api_configure_networks](#ga71ddc5b9e09da398d02caadc91ef3cfc)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于配置网络的 API。

<a id="r_ga6aa2c51fa80d5420593021c35444308a"></a>

```c
typedef int(* cellular_api_get_supported_networks) (const struct device *dev, const struct cellular_network **networks, uint8_t *size)
```

相关声明：[cellular_api_get_supported_networks](#ga6aa2c51fa80d5420593021c35444308a)、[device](../device_reference/P002_设备对象结构.md)、[cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于获取支持的网络的 API。

<a id="r_ga75cac77838970288d4d23647eaafd30b"></a>

```c
typedef int(* cellular_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

相关声明：[cellular_api_get_signal](#ga75cac77838970288d4d23647eaafd30b)、[device](../device_reference/P002_设备对象结构.md)、[cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

用于获取网络信号强度（signal strength）的 API。

<a id="r_ga03095206ae2b77ce232dd05b172bd56d"></a>

```c
typedef int(* cellular_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

相关声明：[cellular_api_get_modem_info](#ga03095206ae2b77ce232dd05b172bd56d)、[device](../device_reference/P002_设备对象结构.md)、[cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)。

用于获取调制解调器（modem）信息的 API。

<a id="r_ga08a0966933caa70d7044342ed2ad8eb6"></a>

```c
typedef int(* cellular_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

相关声明：[cellular_api_get_registration_status](#ga08a0966933caa70d7044342ed2ad8eb6)、[device](../device_reference/P002_设备对象结构.md)、[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)。

用于获取注册状态（registration status）的 API。

<a id="r_ga30f5fef993f17b001e2df9c89bdaf288"></a>

```c
typedef int(* cellular_api_get_network_status) (const struct device *dev, struct cellular_evt_network_status *status)
```

相关声明：[cellular_api_get_network_status](#ga30f5fef993f17b001e2df9c89bdaf288)、[device](../device_reference/P002_设备对象结构.md)、[cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)。

用于获取最近一次上报的网络（服务小区，serving cell）状态的 API。

<a id="r_gabf5bd5a939a300b8493f7c803b9128f0"></a>

```c
typedef int(* cellular_api_set_apn) (const struct device *dev, const char *apn)
```

相关声明：[cellular_api_set_apn](#gabf5bd5a939a300b8493f7c803b9128f0)、[device](../device_reference/P002_设备对象结构.md)。

用于编程设置接入点名称（APN）的 API。

<a id="r_gacbf9c85b2ea95321beee0ba75d5977f7"></a>

```c
typedef int(* cellular_api_set_callback) (const struct device *dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void *user_data)
```

相关声明：[cellular_api_set_callback](#gacbf9c85b2ea95321beee0ba75d5977f7)、[device](../device_reference/P002_设备对象结构.md)、[cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)、[cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)。

用于注册异步回调的 API。

<a id="r_ga975fe3a63ed2dd936faa619846f8b701"></a>

```c
typedef const struct cellular_stats *(* cellular_api_get_stats) (const struct device *dev)
```

相关声明：[cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)、[cellular_api_get_stats](#ga975fe3a63ed2dd936faa619846f8b701)、[device](../device_reference/P002_设备对象结构.md)。

用于读取运行统计信息（operational statistics）的 API。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga71ddc5b9e09da398d02caadc91ef3cfc"></a>

### `cellular_api_configure_networks`

```c
typedef int(* cellular_api_configure_networks) (const struct device *dev, const struct cellular_network *networks, uint8_t size)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于配置网络的 API。

<a id="ga03095206ae2b77ce232dd05b172bd56d"></a>

### `cellular_api_get_modem_info`

```c
typedef int(* cellular_api_get_modem_info) (const struct device *dev, const enum cellular_modem_info_type type, char *info, size_t size)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于获取调制解调器（modem）信息的 API。

<a id="ga30f5fef993f17b001e2df9c89bdaf288"></a>

### `cellular_api_get_network_status`

```c
typedef int(* cellular_api_get_network_status) (const struct device *dev, struct cellular_evt_network_status *status)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于获取最近一次上报的网络（服务小区，serving cell）状态的 API。

<a id="ga08a0966933caa70d7044342ed2ad8eb6"></a>

### `cellular_api_get_registration_status`

```c
typedef int(* cellular_api_get_registration_status) (const struct device *dev, enum cellular_access_technology tech, enum cellular_registration_status *status)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于获取注册状态（registration status）的 API。

<a id="ga75cac77838970288d4d23647eaafd30b"></a>

### `cellular_api_get_signal`

```c
typedef int(* cellular_api_get_signal) (const struct device *dev, const enum cellular_signal_type type, int16_t *value)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于获取网络信号强度（signal strength）的 API。

<a id="ga975fe3a63ed2dd936faa619846f8b701"></a>

### `cellular_api_get_stats`

```c
typedef const struct cellular_stats *(* cellular_api_get_stats) (const struct device *dev)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于读取运行统计信息（operational statistics）的 API。

<a id="ga6aa2c51fa80d5420593021c35444308a"></a>

### `cellular_api_get_supported_networks`

```c
typedef int(* cellular_api_get_supported_networks) (const struct device *dev, const struct cellular_network **networks, uint8_t *size)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于获取支持的网络的 API。

<a id="gabf5bd5a939a300b8493f7c803b9128f0"></a>

### `cellular_api_set_apn`

```c
typedef int(* cellular_api_set_apn) (const struct device *dev, const char *apn)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于编程设置接入点名称（APN）的 API。

<a id="gacbf9c85b2ea95321beee0ba75d5977f7"></a>

### `cellular_api_set_callback`

```c
typedef int(* cellular_api_set_callback) (const struct device *dev, cellular_event_mask_t mask, cellular_event_cb_t cb, void *user_data)
```

```c
#include <zephyr/drivers/cellular.h>
```

用于注册异步回调的 API。


## 5.5\_原页交叉引用（Cross References）

- [蜂窝调制解调器辅助功能（Cellular modem helpers）](../api_protocol_topic_reference/P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md)
- [cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [cellular_network](../modem_wireless_model_reference/P007_cellular_network_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)
- [cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)
- [cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)
- [cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P004_蓝牙 Mesh 私有信标客户端（Private Beacon Client）.md) · [返回大纲](大纲.md) · [下一章](P006_亚德诺（Analog Devices）MAX32.md)
