---
id: learning.zephyr-docs.api-file-storage-event-reference.page-2
title: zephyr__drivers__can__can_fake.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_can\_\_can\_fake.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/can__fake_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟CAN控制器（Fake CAN Controller）驱动的API函数。

<a id="details"></a>

```c
#include <zephyr/drivers/can.h>
#include <zephyr/fff.h>
```

查看此文件的源码。

模拟CAN控制器（Fake CAN Controller）驱动的API函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.1\_函数（Functions）

<a id="r_ga336125a9f719700f59c5b36c8f6c9701"></a>

```c
int fake_can_start (const struct device *)
```

相关声明：[fake_can_start](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga336125a9f719700f59c5b36c8f6c9701)、[device](../device_reference/P002_设备对象结构.md)。

`can_driver_api::start` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga14053f40abcd885d5039342a48691afc"></a>

```c
int fake_can_stop (const struct device *)
```

相关声明：[fake_can_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga14053f40abcd885d5039342a48691afc)、[device](../device_reference/P002_设备对象结构.md)。

`can_driver_api::stop` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga37fb033aa3e1df477a2e879a5a823034"></a>

```c
int fake_can_set_timing (const struct device *, const struct can_timing *)
```

相关声明：[fake_can_set_timing](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga37fb033aa3e1df477a2e879a5a823034)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

`can_driver_api::set_timing` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga12660dfbe19e04500673df058093da39"></a>

```c
int fake_can_set_timing_data (const struct device *, const struct can_timing *)
```

相关声明：[fake_can_set_timing_data](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga12660dfbe19e04500673df058093da39)、[device](../device_reference/P002_设备对象结构.md)、[can_timing](../hardware/P366_CAN时序结构.md)。

`can_driver_api::set_timing_data` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga5ab6c1a56f20e14e7a3ee7f41f77e722"></a>

```c
int fake_can_get_capabilities (const struct device *, can_mode_t *)
```

相关声明：[fake_can_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga5ab6c1a56f20e14e7a3ee7f41f77e722)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

`can_driver_api::get_capabilities` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga28f41cee87de64240f5a4c173bcc13ee"></a>

```c
int fake_can_set_mode (const struct device *, can_mode_t)
```

相关声明：[fake_can_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga28f41cee87de64240f5a4c173bcc13ee)、[device](../device_reference/P002_设备对象结构.md)、[can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)。

`can_driver_api::set_mode` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gae27f8832b6bca338bc40d4b75ba07a2d"></a>

```c
int fake_can_send (const struct device *, const struct can_frame *, k_timeout_t, can_tx_callback_t, void *)
```

相关声明：[fake_can_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae27f8832b6bca338bc40d4b75ba07a2d)、[device](../device_reference/P002_设备对象结构.md)、[can_frame](../hardware/P363_CAN帧结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)。

`can_driver_api::send` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gae42496e147592f98352c5fa6f6a1a665"></a>

```c
int fake_can_add_rx_filter (const struct device *, can_rx_callback_t, void *, const struct can_filter *)
```

相关声明：[fake_can_add_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae42496e147592f98352c5fa6f6a1a665)、[device](../device_reference/P002_设备对象结构.md)、[can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

`can_driver_api::add_rx_filter` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gad2ef4f3a82cf93968123ac7f24ee5162"></a>

```c
void fake_can_remove_rx_filter (const struct device *, int)
```

相关声明：[fake_can_remove_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gad2ef4f3a82cf93968123ac7f24ee5162)、[device](../device_reference/P002_设备对象结构.md)。

`can_driver_api::remove_rx_filter` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0"></a>

```c
int fake_can_recover (const struct device *, k_timeout_t)
```

相关声明：[fake_can_recover](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

`can_driver_api::recover` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga18314694d1939ec4983ef33681a8dcb3"></a>

```c
int fake_can_get_state (const struct device *, enum can_state *, struct can_bus_err_cnt *)
```

相关声明：[fake_can_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga18314694d1939ec4983ef33681a8dcb3)、[device](../device_reference/P002_设备对象结构.md)、[can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)、[can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)。

`can_driver_api::get_state` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga0378d66c4a1d72d5431751e094c6f21a"></a>

```c
int fake_can_state_change_callbacks_enabled (const struct device *, bool)
```

相关声明：[fake_can_state_change_callbacks_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga0378d66c4a1d72d5431751e094c6f21a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

`can_driver_api::state_change_callbacks_enabled` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga4d396abead1d8ed677f00b64198f2597"></a>

```c
int fake_can_get_max_filters (const struct device *, bool)
```

相关声明：[fake_can_get_max_filters](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga4d396abead1d8ed677f00b64198f2597)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

`can_driver_api::get_max_filters` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga657de26af4b7860d1b485640ce979535"></a>

```c
int fake_can_get_core_clock (const struct device *, uint32_t *)
```

相关声明：[fake_can_get_core_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga657de26af4b7860d1b485640ce979535)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

`can_driver_api::get_core_clock` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。


## 2.2\_原页交叉引用（Cross References）

- [zephyr/drivers/can.h](../can_driver_reference/P002_CAN驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P084_can_fake.h_源码浏览.md)
- [fake_can_start](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga336125a9f719700f59c5b36c8f6c9701)
- [device](../device_reference/P002_设备对象结构.md)
- [can_driver_api::start](../hardware/P370_CAN驱动函数表.md#ac42f6d438d3e88f0db8e64c236621f8a)
- [fake_can_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga14053f40abcd885d5039342a48691afc)
- [can_driver_api::stop](../hardware/P370_CAN驱动函数表.md#a3ca1cb8bcd6713bfdf20f76cee3bc3a4)
- [fake_can_set_timing](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga37fb033aa3e1df477a2e879a5a823034)
- [can_timing](../hardware/P366_CAN时序结构.md)
- [can_driver_api::set_timing](../hardware/P370_CAN驱动函数表.md#a356b3761926c2a5a85fcc80b2e8a4643)
- [fake_can_set_timing_data](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga12660dfbe19e04500673df058093da39)
- [can_driver_api::set_timing_data](../hardware/P370_CAN驱动函数表.md#a1951bfc3135824e364d5f18aa9b15d09)
- [fake_can_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga5ab6c1a56f20e14e7a3ee7f41f77e722)
- [can_mode_t](../hardware/P362_CAN控制器接口.md#ga0b2a1456e66f4522a30cf1400fdfced7)
- [can_driver_api::get_capabilities](../hardware/P370_CAN驱动函数表.md#a11d2ff416d459faf84905e7ffdc1a536)
- [fake_can_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga28f41cee87de64240f5a4c173bcc13ee)
- [can_driver_api::set_mode](../hardware/P370_CAN驱动函数表.md#accfe8e3e40e5bae33b8c31b1af55c644)
- [fake_can_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae27f8832b6bca338bc40d4b75ba07a2d)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [can_tx_callback_t](../hardware/P362_CAN控制器接口.md#gab3675297d3e528bf19e2072f6a84bfca)
- [can_driver_api::send](../hardware/P370_CAN驱动函数表.md#a9b5ec5c71a126798c24a19d1c91f879b)
- [fake_can_add_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gae42496e147592f98352c5fa6f6a1a665)
- [can_rx_callback_t](../hardware/P362_CAN控制器接口.md#gaab9525fafab78c0da0a78a2dae39bd6f)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [can_driver_api::add_rx_filter](../hardware/P370_CAN驱动函数表.md#a56225a8cb458baa0d1745ff5e9202ae6)
- [fake_can_remove_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#gad2ef4f3a82cf93968123ac7f24ee5162)
- [can_driver_api::remove_rx_filter](../hardware/P370_CAN驱动函数表.md#ac264f4d66a29a5f42aaf2b6c9665f8f3)
- [fake_can_recover](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga6b2569d7a1e1409fbbc0a6fb8cb3b4d0)
- [can_driver_api::recover](../hardware/P370_CAN驱动函数表.md#aba563aff4e114b7956bb824efdebb0c6)
- [fake_can_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga18314694d1939ec4983ef33681a8dcb3)
- [can_state](../hardware/P362_CAN控制器接口.md#gac7ec472c26c564dd7067c49f67c8d2f7)
- [can_bus_err_cnt](../hardware/P365_CAN错误计数结构.md)
- [can_driver_api::get_state](../hardware/P370_CAN驱动函数表.md#aa6b8b2b7c544cf78930b45cab1e6dbb4)
- [fake_can_state_change_callbacks_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga0378d66c4a1d72d5431751e094c6f21a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [can_driver_api::state_change_callbacks_enabled](../hardware/P370_CAN驱动函数表.md#a90547b28015e2b7eea6a548b0ab2b576)
- [fake_can_get_max_filters](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga4d396abead1d8ed677f00b64198f2597)
- [can_driver_api::get_max_filters](../hardware/P370_CAN驱动函数表.md#a24a90bc4d49818985479bfe101cc21d4)
- [fake_can_get_core_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html#ga657de26af4b7860d1b485640ce979535)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [can_driver_api::get_core_clock](../hardware/P370_CAN驱动函数表.md#ae969c18839dc5f1cb4356df6d1ee1e20)

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__classic__hid.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__mgmt__hawkbit__config.h_文件参考.md)
