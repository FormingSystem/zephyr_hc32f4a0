---
id: learning.zephyr-docs.api-network-time-topic-reference.page-8
title: 调试访问端口链路（DAP Link）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_调试访问端口链路（DAP Link）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调试访问端口（Debug Access Port，DAP）链路后端接口。

<a id="details"></a>

调试访问端口（Debug Access Port，DAP）Link 后端接口。自 Zephyr 4.4 起提供；API 版本为 0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_dap_5Flink_2Eh"></a>

```c
file dap_link.h
```

相关声明：[dap_link.h](../api_file_service_reference/P005_zephyr__dap__dap_link.h_文件参考.md)。

DAP链路（DAP Link）API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

<a id="r_dap_5Flink_5Fcontext"></a>

```c
struct dap_link_context
```

相关声明：[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

DAP链路（DAP Link）的运行时上下文，为不透明类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.3\_宏定义（Macros）

<a id="r_ga5c14bcee98d7ef19b2c9bdb6da4cc400"></a>

```c
#define DAP_LINK_CONTEXT_DEFINE(ctx_name, ctx_dev)
```

相关声明：[DAP_LINK_CONTEXT_DEFINE](#ga5c14bcee98d7ef19b2c9bdb6da4cc400)。

静态定义调试访问端口链接上下文（DAP Link Context）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_gaebd8b888c2befaa8674247850f040145"></a>

```c
int dap_link_init (struct dap_link_context *const dap_link_ctx)
```

相关声明：[dap_link_init](#gaebd8b888c2befaa8674247850f040145)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

初始化调试访问端口链接上下文（DAP Link Context）。

<a id="r_gaa2057dca6fdac21d4fe7dd919c37af1b"></a>

```c
void dap_link_set_pkt_size (struct dap_link_context *const dap_link_ctx, const uint16_t pkt_size)
```

相关声明：[dap_link_set_pkt_size](#gaa2057dca6fdac21d4fe7dd919c37af1b)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 DAP Link 后端（Backend）使用的数据包大小（Packet Size）。

<a id="r_ga6748c204c222c52155263592713e2291"></a>

```c
int dap_link_backend_usb_init (struct dap_link_context *const dap_link_ctx)
```

相关声明：[dap_link_backend_usb_init](#ga6748c204c222c52155263592713e2291)、[dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)。

初始化 DAP Link USB 后端（Backend）。

## 8.5\_详细说明（Detailed Documentation）

<a id="ga5c14bcee98d7ef19b2c9bdb6da4cc400"></a>

### `DAP_LINK_CONTEXT_DEFINE`

```c
#define DAP_LINK_CONTEXT_DEFINE ( ctx_name, ctx_dev )
```

```c
#include <zephyr/dap/dap_link.h>
```

展开值（Value）：

```c
static struct dap_link_context ctx_name = {                             \
        .dev = ctx_dev,                                                 \
}
```

静态定义调试访问端口链接上下文（DAP Link Context）。

使用示例：

原始示例（Example）：

```c
DAP_LINK_CONTEXT_DEFINE(sample_link_ctx,
                        DEVICE_DT_GET_ONE(zephyr_swdp_gpio));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx_name` | 要定义的静态上下文对象（static context object）名称。 |
| `ctx_dev` | DAP Link 后端使用的串行线调试端口（SWDP）设备。 |

<a id="ga6748c204c222c52155263592713e2291"></a>

### `dap_link_backend_usb_init()`

```c
int dap_link_backend_usb_init ( struct dap_link_context *const dap_link_ctx)
```

```c
#include <zephyr/dap/dap_link.h>
```

初始化 DAP Link USB 后端（Backend）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dap_link_ctx` | 要绑定到 USB 后端的上下文。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功初始化 USB 后端。 |
| `-errno` | 失败时返回负错误码。 |

<a id="gaebd8b888c2befaa8674247850f040145"></a>

### `dap_link_init()`

```c
int dap_link_init ( struct dap_link_context *const dap_link_ctx)
```

```c
#include <zephyr/dap/dap_link.h>
```

初始化调试访问端口链接上下文（DAP Link Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dap_link_ctx` | 要初始化的上下文。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功初始化上下文。 |
| `-errno` | 失败时返回负错误码。 |

<a id="gaa2057dca6fdac21d4fe7dd919c37af1b"></a>

### `dap_link_set_pkt_size()`

```c
void dap_link_set_pkt_size ( struct dap_link_context *const dap_link_ctx, const uint16_t pkt_size )
```

```c
#include <zephyr/dap/dap_link.h>
```

设置 DAP Link 后端（Backend）使用的数据包大小（Packet Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dap_link_ctx` | 要更新的上下文。 |
| `[in] pkt_size` | 数据包大小，单位为字节。 |


## 8.6\_原页交叉引用（Cross References）

- [dap_link.h](../api_file_service_reference/P005_zephyr__dap__dap_link.h_文件参考.md)
- [dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [DEVICE_DT_GET_ONE](../device_reference/P001_设备模型公共接口.md#ga39c760429534ef9ae77f3d996987cd2b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructdap__link__context_html"></a>
<a id="agroup__dap__link__interface_html_ga5c14bcee98d7ef19b2c9bdb6da4cc400"></a>
<a id="agroup__device__model_html_ga39c760429534ef9ae77f3d996987cd2b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_德州仪器（TI）.md) · [返回大纲](大纲.md) · [下一章](P009_DHCPv6 服务器.md)
