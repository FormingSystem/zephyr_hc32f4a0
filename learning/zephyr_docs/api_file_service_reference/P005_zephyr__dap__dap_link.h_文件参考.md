---
id: learning.zephyr-docs.api-file-service-reference.page-5
title: zephyr__dap__dap_link.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dap__link_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dap\_\_dap\_link.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dap__link_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DAP链路（DAP Link）API的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/swdp.h>
```

查看此文件的源码。

DAP链路（DAP Link）API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_dap_5Flink_5Fcontext"></a>

```c
struct dap_link_context
```

相关声明：[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

DAP链路（DAP Link）的运行时上下文，为不透明类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga5c14bcee98d7ef19b2c9bdb6da4cc400"></a>

```c
#define DAP_LINK_CONTEXT_DEFINE(ctx_name, ctx_dev)
```

相关声明：[DAP_LINK_CONTEXT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#ga5c14bcee98d7ef19b2c9bdb6da4cc400)。

静态定义调试访问端口链接上下文（DAP Link Context）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_gaebd8b888c2befaa8674247850f040145"></a>

```c
int dap_link_init (struct dap_link_context *const dap_link_ctx)
```

相关声明：[dap_link_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaebd8b888c2befaa8674247850f040145)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

初始化调试访问端口链接上下文（DAP Link Context）。

<a id="r_gaa2057dca6fdac21d4fe7dd919c37af1b"></a>

```c
void dap_link_set_pkt_size (struct dap_link_context *const dap_link_ctx, const uint16_t pkt_size)
```

相关声明：[dap_link_set_pkt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaa2057dca6fdac21d4fe7dd919c37af1b)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 DAP Link 后端（Backend）使用的数据包大小（Packet Size）。

<a id="r_ga6748c204c222c52155263592713e2291"></a>

```c
int dap_link_backend_usb_init (struct dap_link_context *const dap_link_ctx)
```

相关声明：[dap_link_backend_usb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#ga6748c204c222c52155263592713e2291)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

初始化 DAP Link USB 后端（Backend）。


## 5.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/swdp.h](../peripheral_bus_storage_source_reference/P028_zephyr__drivers__swdp.h_头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/dap__link_8h_source.html)
- [dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)
- [DAP_LINK_CONTEXT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#ga5c14bcee98d7ef19b2c9bdb6da4cc400)
- [dap_link_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaebd8b888c2befaa8674247850f040145)
- [dap_link_set_pkt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaa2057dca6fdac21d4fe7dd919c37af1b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [dap_link_backend_usb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#ga6748c204c222c52155263592713e2291)

<a id="header-details"></a>

---

[上一章](P004_zephyr__net__coap_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__bluetooth__mesh__dfu.h_文件参考.md)
