---
id: learning.zephyr-docs.api-file-management-reference.page-45
title: zephyr__drivers__i3c__target_device.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_drivers\_\_i3c\_\_target\_device.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <errno.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 45.1\_数据结构（Data Structures）

<a id="r_i3c_5Fconfig_5Ftarget"></a>

```c
struct i3c_config_target
```

相关声明：[i3c_config_target](../hardware/P392_I3C目标硬件配置.md)。

使I3C硬件充当目标设备（Target Device）的配置参数。

<a id="r_i3c_5Ftarget_5Fconfig"></a>

```c
struct i3c_target_config
```

相关声明：[i3c_target_config](../hardware/P388_I3C目标设备配置.md)。

描述支持I3C目标API（Target API）的设备的结构。

<a id="r_i3c_5Ftarget_5Fcallbacks"></a>

```c
struct i3c_target_callbacks
```

相关声明：[i3c_target_callbacks](../hardware/P389_I3C目标设备回调表.md)。

<a id="r_i3c_5Ftarget_5Fdriver_5Fapi"></a>

```c
struct i3c_target_driver_api
```

相关声明：[i3c_target_driver_api](../hardware/P390_I3C目标设备驱动函数表.md)。

驱动操作（Driver Operations）：I3C目标设备（Target Device）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 45.2\_类型定义（Typedefs）

<a id="r_gae6b75cf65f1715ff36bc0aa1a0908b07"></a>

```c
typedef int(* i3c_target_api_driver_register_t) (const struct device *dev)
```

相关声明：[i3c_target_api_driver_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#gae6b75cf65f1715ff36bc0aa1a0908b07)、[device](../device_reference/P002_设备对象结构.md)。

指示 I3C 目标设备驱动向其总线控制器注册自身。

<a id="r_ga5b45ad9e1388ac39093cd5374a9f5c4c"></a>

```c
typedef int(* i3c_target_api_driver_unregister_t) (const struct device *dev)
```

相关声明：[i3c_target_api_driver_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#ga5b45ad9e1388ac39093cd5374a9f5c4c)、[device](../device_reference/P002_设备对象结构.md)。

指示 I3C 目标设备驱动从其总线控制器注销自身。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 45.3\_函数（Functions）

<a id="r_ga09be7f73861bede0071fd8ade344d092"></a>

```c
static int i3c_target_controller_handoff (const struct device *dev, bool accept)
```

相关声明：[i3c_target_controller_handoff](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga09be7f73861bede0071fd8ade344d092)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[accept](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)。

接受或拒绝控制器移交（Controller Handoffs）。

<a id="r_gafb5ebdfd5536ee265a3719beb8ae81dc"></a>

```c
static int i3c_target_tx_write (const struct device *dev, uint8_t *buf, uint16_t len, uint8_t hdr_mode)
```

相关声明：[i3c_target_tx_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gafb5ebdfd5536ee265a3719beb8ae81dc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向目标设备的发送先进先出队列（TX FIFO）写入数据。

<a id="r_gaf13d2b84a91e17d5ec49a41e9c553d42"></a>

```c
static int i3c_target_register (const struct device *dev, struct i3c_target_config *cfg)
```

相关声明：[i3c_target_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gaf13d2b84a91e17d5ec49a41e9c553d42)、[device](../device_reference/P002_设备对象结构.md)、[i3c_target_config](../hardware/P388_I3C目标设备配置.md)。

使用所提供配置，向控制器注册目标设备（target device）。

<a id="r_ga3dc0e6451fb13fa063c5ec3e18fe22e4"></a>

```c
static int i3c_target_unregister (const struct device *dev, struct i3c_target_config *cfg)
```

相关声明：[i3c_target_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga3dc0e6451fb13fa063c5ec3e18fe22e4)、[device](../device_reference/P002_设备对象结构.md)、[i3c_target_config](../hardware/P388_I3C目标设备配置.md)。

注销由所提供配置描述的目标设备。


## 45.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P854_target_device.h_源码浏览.md)
- [i3c_config_target](../hardware/P392_I3C目标硬件配置.md)
- [i3c_target_config](../hardware/P388_I3C目标设备配置.md)
- [i3c_target_callbacks](../hardware/P389_I3C目标设备回调表.md)
- [i3c_target_driver_api](../hardware/P390_I3C目标设备驱动函数表.md)
- [i3c_target_api_driver_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#gae6b75cf65f1715ff36bc0aa1a0908b07)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_target_api_driver_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#ga5b45ad9e1388ac39093cd5374a9f5c4c)
- [i3c_target_controller_handoff](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga09be7f73861bede0071fd8ade344d092)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [accept](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [i3c_target_tx_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gafb5ebdfd5536ee265a3719beb8ae81dc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [i3c_target_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gaf13d2b84a91e17d5ec49a41e9c553d42)
- [i3c_target_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga3dc0e6451fb13fa063c5ec3e18fe22e4)

---

[上一章](P044_zephyr__sys__speculation.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_zephyr__dt-bindings__gpio__ti-cc13xx-cc26xx-gpio.h_文件参考.md)
