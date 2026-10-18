---
id: learning.zephyr-docs.api-file-service-interface-reference.page-46
title: zephyr__drivers__firmware__scmi__shmem.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_shmem.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）共享内存（Shared Memory）的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/arch/cpu.h>
#include <errno.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）共享内存（Shared Memory）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.1\_函数（Functions）

<a id="r_gaf36f95840d1a62582edcf53e0482aeb5"></a>

```c
int scmi_shmem_write_message (const struct device *shmem, struct scmi_message *msg, bool use_polling)
```

相关声明：[scmi_shmem_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf36f95840d1a62582edcf53e0482aeb5)、[device](../device_reference/P002_设备对象结构.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在共享内存（SHMEM）区域写入消息。

<a id="r_ga6e2330af169f33b768dcacf5e2dba5a2"></a>

```c
int scmi_shmem_read_hdr (const struct device *shmem, uint32_t *hdr)
```

相关声明：[scmi_shmem_read_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga6e2330af169f33b768dcacf5e2dba5a2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从共享内存（SHMEM）区域读取消息头（Message Header）。

<a id="r_gaf0f9657082d02048c2d5df7c14833228"></a>

```c
int scmi_shmem_read_message (const struct device *shmem, struct scmi_message *msg)
```

相关声明：[scmi_shmem_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf0f9657082d02048c2d5df7c14833228)、[device](../device_reference/P002_设备对象结构.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)。

从共享内存（SHMEM）区域读取消息。

<a id="r_gaa61c9eea220cc353b97c316bc94e0072"></a>

```c
void scmi_shmem_update_flags (const struct device *shmem, uint32_t mask, uint32_t val)
```

相关声明：[scmi_shmem_update_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaa61c9eea220cc353b97c316bc94e0072)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新通道标志（Channel Flags）。

<a id="r_ga32f0c9fdfca8450b5ab2dc33ce64896c"></a>

```c
uint32_t scmi_shmem_channel_status (const struct device *shmem)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_shmem_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga32f0c9fdfca8450b5ab2dc33ce64896c)、[device](../device_reference/P002_设备对象结构.md)。

读取通道状态（Channel Status）。

<a id="r_gaab6dca2dc06cb108f40e358479b19426"></a>

```c
int scmi_shmem_vendor_write_message (struct scmi_shmem_layout *layout)
```

相关声明：[scmi_shmem_vendor_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaab6dca2dc06cb108f40e358479b19426)。

写入消息时处理厂商专用功能（Vendor-specific Features）。

<a id="r_ga5e1978cff70bd92d233fdacf7ae0de48"></a>

```c
int scmi_shmem_vendor_read_message (const struct scmi_shmem_layout *layout)
```

相关声明：[scmi_shmem_vendor_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga5e1978cff70bd92d233fdacf7ae0de48)。

读取消息时处理厂商专用功能（Vendor-specific Features）。

<a id="r_gabb1c2c847a723adc45e936e1c771af0d"></a>

```c
void scmi_shmem_mark_channel_free (const struct device *dev)
```

相关声明：[scmi_shmem_mark_channel_free](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gabb1c2c847a723adc45e936e1c771af0d)、[device](../device_reference/P002_设备对象结构.md)。

将共享内存（SHMEM）通道标记为空闲，以确认消息已被消费。


## 46.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/arch/cpu.h](../api_source_supplement_reference/P009_cpu.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P780_shmem.h_源码浏览.md)
- [scmi_shmem_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf36f95840d1a62582edcf53e0482aeb5)
- [device](../device_reference/P002_设备对象结构.md)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [scmi_shmem_read_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga6e2330af169f33b768dcacf5e2dba5a2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_shmem_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf0f9657082d02048c2d5df7c14833228)
- [scmi_shmem_update_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaa61c9eea220cc353b97c316bc94e0072)
- [scmi_shmem_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga32f0c9fdfca8450b5ab2dc33ce64896c)
- [scmi_shmem_vendor_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaab6dca2dc06cb108f40e358479b19426)
- [scmi_shmem_vendor_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga5e1978cff70bd92d233fdacf7ae0de48)
- [scmi_shmem_mark_channel_free](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gabb1c2c847a723adc45e936e1c771af0d)

<a id="header-details"></a>

---

[上一章](P045_zephyr__drivers__sensor_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__mgmt__mcumgr__smp__smp_client.h_文件参考.md)
