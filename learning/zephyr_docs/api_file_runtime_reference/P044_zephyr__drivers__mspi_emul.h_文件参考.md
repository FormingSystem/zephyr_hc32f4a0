---
id: learning.zephyr-docs.api-file-runtime-reference.page-44
title: zephyr__drivers__mspi_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_drivers\_\_mspi\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI仿真驱动（Emulation Drivers）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/mspi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

MSPI仿真驱动（Emulation Drivers）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 44.1\_数据结构（Data Structures）

<a id="r_emul_5Fmspi_5Fdevice_5Fapi"></a>

```c
struct emul_mspi_device_api
```

相关声明：[emul_mspi_device_api](../hardware/P483_MSPI仿真设备API结构.md)。

MSPI设备仿真器（Device Emulator）API的定义。

<a id="r_mspi_5Femul"></a>

```c
struct mspi_emul
```

相关声明：[mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)。

MSPI设备仿真器链表（Linked List）中的节点。

<a id="r_emul_5Fmspi_5Fdriver_5Fapi"></a>

```c
struct emul_mspi_driver_api
```

相关声明：[emul_mspi_driver_api](../hardware/P484_MSPI仿真驱动API结构.md)。

MSPI控制器仿真器（Controller Emulator）API的定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 44.2\_类型定义（Typedefs）

<a id="r_gabecb33236ed3a6a93a28edef0a4c3ae7"></a>

```c
typedef struct mspi_emul *(* mspi_emul_find_emul) (const struct device *dev, uint16_t dev_idx)
```

相关声明：[mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)、[mspi_emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gabecb33236ed3a6a93a28edef0a4c3ae7)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找 MSPI 总线（Bus）上的仿真器（Emulator）。

<a id="r_gaaa0c99ea6582cacba89f8630d8d554be"></a>

```c
typedef int(* mspi_emul_trigger_event) (const struct device *dev, enum mspi_bus_event evt_type)
```

相关声明：[mspi_emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gaaa0c99ea6582cacba89f8630d8d554be)、[device](../device_reference/P002_设备对象结构.md)、[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)。

在 MSPI 控制器侧仿真器（Controller-Side Emulator）上触发事件（Event），从而调用特定回调（Callbacks）。

<a id="r_ga15df8cc9ccc2831c5446002e864f1717"></a>

```c
typedef int(* emul_mspi_dev_api_transceive) (const struct emul *target, const struct mspi_xfer_packet *packets, uint32_t num_packet, bool async, uint32_t timeout)
```

相关声明：[emul_mspi_dev_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga15df8cc9ccc2831c5446002e864f1717)、[emul](../hardware/P477_仿真器实例结构.md)、[mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在未连接真实硬件时，将 MSPI 收发请求（Transceive Request）环回（Loopback）到设备仿真器（Device Emulator）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 44.3\_函数（Functions）

<a id="r_ga98c9a359f3385f49fbfe52b27254d261"></a>

```c
int mspi_emul_register (const struct device *dev, struct mspi_emul *emul)
```

相关声明：[mspi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga98c9a359f3385f49fbfe52b27254d261)、[device](../device_reference/P002_设备对象结构.md)、[mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)、[emul](../hardware/P477_仿真器实例结构.md)。

在控制器（Controller）上注册仿真设备（Emulated Device）。


## 44.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_source_reference/P017_zephyr__drivers__mspi.h_头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P567_mspi_emul.h_源码浏览.md)
- [emul_mspi_device_api](../hardware/P483_MSPI仿真设备API结构.md)
- [mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)
- [emul_mspi_driver_api](../hardware/P484_MSPI仿真驱动API结构.md)
- [mspi_emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gabecb33236ed3a6a93a28edef0a4c3ae7)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mspi_emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gaaa0c99ea6582cacba89f8630d8d554be)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [emul_mspi_dev_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga15df8cc9ccc2831c5446002e864f1717)
- [emul](../hardware/P477_仿真器实例结构.md)
- [mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mspi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga98c9a359f3385f49fbfe52b27254d261)

<a id="header-details"></a>

---

[上一章](P043_zephyr__mpipe__base__mpipe_tee.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__drivers__flash__npcx_flash_api_ex.h_文件参考.md)
