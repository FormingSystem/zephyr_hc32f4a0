---
id: learning.zephyr-docs.usb.api-89
title: USB音频2设备API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uac2__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_USB音频2设备API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__uac2__device.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 89.1\_阅读说明与来源

译注：本页说明USB音频类2（USB Audio Class 2，UAC2）的接口与回调。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 音频类 2（USB Audio Class 2）设备 API。

USB 音频类 2（USB Audio Class 2）设备 API。

引入版本（Since）：3.6。

接口版本（Version）：0.2.0。

## 89.2\_数据结构（Data Structures）

<a id="r_uac2_5Fops"></a>

```c
struct uac2_ops
```

USB 音频 2 应用事件处理程序（Application Event Handlers）。

相关声明：[uac2_ops](P090_USB音频2回调接口.md)。

## 89.3\_宏定义（Macros）

<a id="r_gaa35265e83d894896806fcca28feb84a3"></a>

```c
#define UAC2_ENTITY_ID(node)
```

获取实体标识符（Entity ID）。

相关声明：[UAC2_ENTITY_ID](P089_USB音频2设备API.md#gaa35265e83d894896806fcca28feb84a3)。

## 89.4\_函数（Functions）

<a id="r_ga802a727c1a201c26a3bd74f0e7f0900c"></a>

```c
void usbd_uac2_set_ops (const struct device *dev, const struct uac2_ops *ops, void *user_data)
```

注册 USB 音频 2 应用回调（Application Callbacks）。

相关声明：[usbd_uac2_set_ops](P089_USB音频2设备API.md#ga802a727c1a201c26a3bd74f0e7f0900c)、[device](../device_reference/P002_设备对象结构.md)、[uac2_ops](P090_USB音频2回调接口.md)。

<a id="r_gae899d75d786f5b1df86db48de88d1254"></a>

```c
int usbd_uac2_send (const struct device *dev, uint8_t terminal, void *data, uint16_t size)
```

向输出终端（Output Terminal）发送音频数据。

相关声明：[usbd_uac2_send](P089_USB音频2设备API.md#gae899d75d786f5b1df86db48de88d1254)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

## 89.5\_详细说明（Detailed Documentation）

<a id="gaa35265e83d894896806fcca28feb84a3"></a>

### 89.5.1\_`UAC2\_ENTITY\_ID`

```c
#define UAC2_ENTITY_ID ( node)
```

```c
#include <zephyr/usb/class/usbd_uac2.h>
```

**宏展开值（Value）**

```c
({                                                                      \
        BUILD_ASSERT(DT_NODE_HAS_COMPAT(DT_PARENT(node), zephyr_uac2)); \
        UTIL_INC(DT_NODE_CHILD_IDX(node));                              \
})
```

获取实体标识符（Entity ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 节点标识符（Node Identifier）。 |

<a id="gae899d75d786f5b1df86db48de88d1254"></a>

### 89.5.2\_`usbd\_uac2\_send()`

```c
int usbd_uac2_send ( const struct device * dev, uint8_t terminal, void * data, uint16_t size )
```

```c
#include <zephyr/usb/class/usbd_uac2.h>
```

向输出终端（Output Terminal）发送音频数据。

数据缓冲区必须满足 USB 设备控制器（UDC）驱动的对齐及其他使用要求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB 音频 2 设备。 |
| `terminal` | 与音频流（AudioStreaming）接口关联的输出终端 ID。 |
| `data` | 包含待发送数据的缓冲区。 |
| `size` | 要发送的字节数。 |

**注意（Note）**：成功时，缓冲区所有权（Buffer Ownership）转移给协议栈；出错时，调用者仍拥有缓冲区。

**返回（Returns）**：成功返回 0，出错返回负值。

> 译注（源码核对）：当前实现中，终端未激活时会立即调用buf_release_cb并返回0，因此成功不一定表示数据已通过USB发出，释放回调也可能在send返回前发生。没有对应端点时返回-ENOENT，已双重排队时返回-EAGAIN，缓冲包装分配失败时返回-ENOMEM；入队失败则返回底层错误，调用者保留原始数据缓冲区的所有权。

<a id="ga802a727c1a201c26a3bd74f0e7f0900c"></a>

### 89.5.3\_`usbd\_uac2\_set\_ops()`

```c
void usbd_uac2_set_ops ( const struct device * dev, const struct uac2_ops * ops, void * user_data )
```

```c
#include <zephyr/usb/class/usbd_uac2.h>
```

注册 USB 音频 2 应用回调（Application Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB 音频 2 设备实例（Device Instance）。 |
| `ops` | USB 音频 2 回调结构体。 |
| `user_data` | 传给 ops 回调的不透明用户数据（Opaque User Data）。 |

> 译注（源码核对）：当前实现保存ops和user_data指针，不复制回调表；所指对象必须在使用期间保持有效。必需回调通过断言检查，不能依赖关闭断言来省略接口要求。

## 89.6\_源码跟踪与使用边界

译注依据保存的[官方UAC2头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_uac2.h)与[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_uac2.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/usb/class/usbd_uac2.h)及[类驱动源码](../../../subsys/usb/device_next/class/usbd_uac2.c)可用于跟踪，版本可能与网页不同。本批未执行固件构建、音频播放或硬件验证。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_gad8912ba5db980713e72257472ded3ced"></a>
<a id="agroup__devicetree-generic-id_html_ga34452788d4fed1fce3e6650d61246866"></a>
<a id="agroup__devicetree-generic-id_html_ga3ac56d491510275ee1321446796ab63b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P088_USB音频2设备API说明.md) · [返回大纲](大纲.md) · [下一章](P090_USB音频2回调接口.md)
