---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-14
title: 共享内存（Shared Memory）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_共享内存（Shared Memory）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCMI 的共享内存传输定义。

<a id="details"></a>

SCMI 的共享内存传输定义。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_shmem_2Eh"></a>

```c
file shmem.h
```

相关声明：[shmem.h](../api_file_service_interface_reference/P046_zephyr__drivers__firmware__scmi__shmem.h_文件参考.md)。

系统控制与管理接口（SCMI）共享内存（Shared Memory）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.2\_函数（Functions）

<a id="r_gaf36f95840d1a62582edcf53e0482aeb5"></a>

```c
int scmi_shmem_write_message (const struct device *shmem, struct scmi_message *msg, bool use_polling)
```

相关声明：[scmi_shmem_write_message](#gaf36f95840d1a62582edcf53e0482aeb5)、[device](../device_reference/P002_设备对象结构.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在共享内存（SHMEM）区域写入消息。

<a id="r_ga6e2330af169f33b768dcacf5e2dba5a2"></a>

```c
int scmi_shmem_read_hdr (const struct device *shmem, uint32_t *hdr)
```

相关声明：[scmi_shmem_read_hdr](#ga6e2330af169f33b768dcacf5e2dba5a2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从共享内存（SHMEM）区域读取消息头（Message Header）。

<a id="r_gaf0f9657082d02048c2d5df7c14833228"></a>

```c
int scmi_shmem_read_message (const struct device *shmem, struct scmi_message *msg)
```

相关声明：[scmi_shmem_read_message](#gaf0f9657082d02048c2d5df7c14833228)、[device](../device_reference/P002_设备对象结构.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)。

从共享内存（SHMEM）区域读取消息。

<a id="r_gaa61c9eea220cc353b97c316bc94e0072"></a>

```c
void scmi_shmem_update_flags (const struct device *shmem, uint32_t mask, uint32_t val)
```

相关声明：[scmi_shmem_update_flags](#gaa61c9eea220cc353b97c316bc94e0072)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新通道标志（Channel Flags）。

<a id="r_ga32f0c9fdfca8450b5ab2dc33ce64896c"></a>

```c
uint32_t scmi_shmem_channel_status (const struct device *shmem)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_shmem_channel_status](#ga32f0c9fdfca8450b5ab2dc33ce64896c)、[device](../device_reference/P002_设备对象结构.md)。

读取通道状态（Channel Status）。

<a id="r_gaab6dca2dc06cb108f40e358479b19426"></a>

```c
int scmi_shmem_vendor_write_message (struct scmi_shmem_layout *layout)
```

相关声明：[scmi_shmem_vendor_write_message](#gaab6dca2dc06cb108f40e358479b19426)。

写入消息时处理厂商专用功能（Vendor-specific Features）。

<a id="r_ga5e1978cff70bd92d233fdacf7ae0de48"></a>

```c
int scmi_shmem_vendor_read_message (const struct scmi_shmem_layout *layout)
```

相关声明：[scmi_shmem_vendor_read_message](#ga5e1978cff70bd92d233fdacf7ae0de48)。

读取消息时处理厂商专用功能（Vendor-specific Features）。

<a id="r_gabb1c2c847a723adc45e936e1c771af0d"></a>

```c
void scmi_shmem_mark_channel_free (const struct device *dev)
```

相关声明：[scmi_shmem_mark_channel_free](#gabb1c2c847a723adc45e936e1c771af0d)、[device](../device_reference/P002_设备对象结构.md)。

将共享内存（SHMEM）通道标记为空闲，以确认消息已被消费。

## 14.3\_详细说明（Detailed Documentation）

<a id="ga32f0c9fdfca8450b5ab2dc33ce64896c"></a>

### `scmi_shmem_channel_status()`

```c
uint32_t scmi_shmem_channel_status ( const struct device * shmem)
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

读取通道状态（Channel Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shmem` | 指向共享内存（SHMEM）设备的指针。 |

<a id="gabb1c2c847a723adc45e936e1c771af0d"></a>

### `scmi_shmem_mark_channel_free()`

```c
void scmi_shmem_mark_channel_free ( const struct device * dev)
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

将共享内存（SHMEM）通道标记为空闲，以确认消息已被消费。

根据系统控制与管理接口（SCMI）规范，`Bit[0]=1` 表示空闲（FREE），`Bit[0]=0` 表示忙（BUSY）。本辅助函数设置 BUSY 位，以指示通道空闲。

> 译注：原文后一处确实写为“sets the BUSY bit”，与前一句的位值说明容易混淆；此处保留原文表述，未擅自改写位定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向共享内存（SHMEM）设备的指针。 |

<a id="ga6e2330af169f33b768dcacf5e2dba5a2"></a>

### `scmi_shmem_read_hdr()`

```c
int scmi_shmem_read_hdr ( const struct device * shmem, uint32_t * hdr )
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

从共享内存（SHMEM）区域读取消息头（Message Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shmem` | 指向共享内存（SHMEM）设备的指针。 |
| `hdr` | 用于接收写入数据的消息（Message）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="gaf0f9657082d02048c2d5df7c14833228"></a>

### `scmi_shmem_read_message()`

```c
int scmi_shmem_read_message ( const struct device * shmem, struct scmi_message * msg )
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

从共享内存（SHMEM）区域读取消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shmem` | 指向共享内存（SHMEM）设备的指针。 |
| `msg` | 用于接收写入数据的消息（Message）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa61c9eea220cc353b97c316bc94e0072"></a>

### `scmi_shmem_update_flags()`

```c
void scmi_shmem_update_flags ( const struct device * shmem, uint32_t mask, uint32_t val )
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

更新通道标志（Channel Flags）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shmem` | 指向共享内存（SHMEM）设备的指针。 |
| `mask` | 对该值按位取反后，与原通道标志值进行按位与（Bitwise AND）的值。 |
| `val` | 先与掩码（Mask）进行按位与，再与掩码处理后的旧值进行按位或（Bitwise OR）的值。 |

<a id="ga5e1978cff70bd92d233fdacf7ae0de48"></a>

### `scmi_shmem_vendor_read_message()`

```c
int scmi_shmem_vendor_read_message ( const struct scmi_shmem_layout * layout)
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

读取消息时处理厂商专用功能（Vendor-specific Features）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `layout` | 消息布局（Message Layout）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaab6dca2dc06cb108f40e358479b19426"></a>

### `scmi_shmem_vendor_write_message()`

```c
int scmi_shmem_vendor_write_message ( struct scmi_shmem_layout * layout)
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

写入消息时处理厂商专用功能（Vendor-specific Features）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `layout` | 消息布局（Message Layout）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf36f95840d1a62582edcf53e0482aeb5"></a>

### `scmi_shmem_write_message()`

```c
int scmi_shmem_write_message ( const struct device * shmem, struct scmi_message * msg, bool use_polling )
```

```c
#include <zephyr/drivers/firmware/scmi/shmem.h>
```

在共享内存（SHMEM）区域写入消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `shmem` | 指向共享内存（SHMEM）设备的指针。 |
| `msg` | 要写入的消息（Message）。 |
| `use_polling` | 应使用轮询（Polling）时为 `true`，否则为 `false`。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 14.4\_原页交叉引用（Cross References）

- [shmem.h](../api_file_service_interface_reference/P046_zephyr__drivers__firmware__scmi__shmem.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_PAC194X API主题.md) · [返回大纲](大纲.md) · [下一章](P015_Trickle 算法库（Trickle Algorithm Library）.md)
