---
id: learning.zephyr-docs.api-file-supplement-reference.page-123
title: zephyr__drivers__firmware__scmi__transport.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transport_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_transport.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）传输层（Transport Layer）的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）传输层（Transport Layer）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 123.1\_数据结构（Data Structures）

<a id="r_scmi_5Fchannel"></a>

```c
struct scmi_channel
```

相关声明：[scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)。

系统控制与管理接口（SCMI）的通道结构。

<a id="r_scmi_5Ftransport_5Fapi"></a>

```c
struct scmi_transport_api
```

相关声明：[scmi_transport_api](../platform_security_model_reference/P052_scmi_transport_api_结构体.md)。

系统控制与管理接口（SCMI）的传输驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 123.2\_类型定义（Typedefs）

<a id="r_ga4c6cccb4e76fef22ec9f3527a96a8de5"></a>

```c
typedef void(* scmi_channel_cb) (struct scmi_channel *chan, uint32_t hdr)
```

相关声明：[scmi_channel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html#ga4c6cccb4e76fef22ec9f3527a96a8de5)、[scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于消息回复（Message Replies）的回调函数（Callback Function）。


## 123.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P876_transport.h_源码浏览.md)
- [scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)
- [scmi_transport_api](../platform_security_model_reference/P052_scmi_transport_api_结构体.md)
- [scmi_channel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html#ga4c6cccb4e76fef22ec9f3527a96a8de5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P124_zephyr__arch__tricore__exception.h_文件参考.md)
