---
id: learning.zephyr-docs.usb.api-63
title: USB固件升级镜像结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__dfu__image.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_USB固件升级镜像结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__dfu__image.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 63.1\_阅读说明与来源

译注：本页说明USB大容量存储（MSC）或设备固件升级（DFU）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/usb/class/usbd_dfu.h>
```

## 63.2\_数据成员（Data Fields）

<a id="r_a3e2d6339752919988f3c113ca87a543e"></a>

```c
const char * name
```



相关声明：[name](P063_USB固件升级镜像结构.md#a3e2d6339752919988f3c113ca87a543e)。

<a id="r_a4df9017274c5094ed49fd8e6964b4379"></a>

```c
struct usb_if_descriptor *const if_desc
```



相关声明：[usb_if_descriptor](P165_USB接口描述符.md)、[if_desc](P063_USB固件升级镜像结构.md#a4df9017274c5094ed49fd8e6964b4379)。

<a id="r_a2aade79d72faef1fe8a6fe846189daf0"></a>

```c
void *const priv
```



相关声明：[priv](P063_USB固件升级镜像结构.md#a2aade79d72faef1fe8a6fe846189daf0)。

<a id="r_aff741ab9145292e9b7a30fe3a93a4615"></a>

```c
struct usbd_desc_node *const sd_nd
```



相关声明：[usbd_desc_node](P021_USB描述符节点.md)、[sd_nd](P063_USB固件升级镜像结构.md#aff741ab9145292e9b7a30fe3a93a4615)。

<a id="r_a2202146c73e3b2300200f04eff05c888"></a>

```c
bool(* next_cb )(void *const priv, const enum usb_dfu_state state, const enum usb_dfu_state next)
```



相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[next_cb](P063_USB固件升级镜像结构.md#a2202146c73e3b2300200f04eff05c888)、[priv](P063_USB固件升级镜像结构.md#a2aade79d72faef1fe8a6fe846189daf0)、[usb_dfu_state](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01e)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_a03ee7685c90ac7ec8c2c4d87a6389e62"></a>

```c
int(* read_cb )(void *const priv, const uint32_t block, const uint16_t size, uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
```



相关声明：[read_cb](P063_USB固件升级镜像结构.md#a03ee7685c90ac7ec8c2c4d87a6389e62)、[priv](P063_USB固件升级镜像结构.md#a2aade79d72faef1fe8a6fe846189daf0)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_aad9a4efbf3649373328b6b6b12fa1922"></a>

```c
int(* write_cb )(void *const priv, const uint32_t block, const uint16_t size, const uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
```



相关声明：[write_cb](P063_USB固件升级镜像结构.md#aad9a4efbf3649373328b6b6b12fa1922)、[priv](P063_USB固件升级镜像结构.md#a2aade79d72faef1fe8a6fe846189daf0)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 63.3\_详细说明（Detailed Documentation）

<a id="a4df9017274c5094ed49fd8e6964b4379"></a>

### 63.3.1\_`if\_desc`

```c
struct usb_if_descriptor* const usbd_dfu_image::if_desc
```

> 译注（源码核对）：指向该镜像的USB接口描述符；宏创建的各镜像通过接口备用设置（Alternate Setting）区分。

<a id="a3e2d6339752919988f3c113ca87a543e"></a>

### 63.3.2\_`name`

```c
const char* usbd_dfu_image::name
```

> 译注（源码核对）：镜像名称，用于接口字符串描述符，不是主机文件路径。

<a id="a2202146c73e3b2300200f04eff05c888"></a>

### 63.3.3\_`next\_cb`

```c
bool(* usbd_dfu_image::next_cb) (void *const priv, const enum usb_dfu_state state, const enum usb_dfu_state next)
```

> 译注（源码核对）：通知后端当前状态和拟进入的下一状态，部分状态转换用其布尔结果决定能否继续；未提供回调时内部辅助函数返回true。它不是统一的下载成功通知，false的处理取决于状态机调用位置。

<a id="a2aade79d72faef1fe8a6fe846189daf0"></a>

### 63.3.4\_`priv`

```c
void* const usbd_dfu_image::priv
```

> 译注（源码核对）：后端私有上下文指针，由类传给读、写及状态回调。类不会把它解释为通用磁盘名或文件路径。

<a id="a03ee7685c90ac7ec8c2c4d87a6389e62"></a>

### 63.3.5\_`read\_cb`

```c
int(* usbd_dfu_image::read_cb) (void *const priv, const uint32_t block, const uint16_t size, uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
```

> 译注（源码核对）：当前类按CONFIG_USBD_DFU_TRANSFER_SIZE分配缓冲区，将size限制为主机请求长度与该配置的较小值；回调返回实际读取字节数，负值使类进入错误状态。后端必须自行遵守size，不能返回超出缓冲容量的长度。

<a id="aff741ab9145292e9b7a30fe3a93a4615"></a>

### 63.3.6\_`sd\_nd`

```c
struct usbd_desc_node* const usbd_dfu_image::sd_nd
```

> 译注（源码核对）：接口名称的字符串描述符节点（String Descriptor Node），由定义镜像的宏建立。

<a id="aad9a4efbf3649373328b6b6b12fa1922"></a>

### 63.3.7\_`write\_cb`

```c
int(* usbd_dfu_image::write_cb) (void *const priv, const uint32_t block, const uint16_t size, const uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
```

> 译注（源码核对）：当前类向回调传递收到的数据；最终零长度下载请求可能传入size=0、buf=NULL，后端必须处理。负返回值使类进入错误状态；内置Flash后端成功返回0，并以零长度块触发尾部缓冲刷新。

## 63.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)和[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)，摘要见[来源记录](../SOURCES.md)。可沿本仓库的[头文件](../../../include/zephyr/usb/class/usbd_dfu.h)和[类实现](../../../subsys/usb/device_next/class/usbd_dfu.c)跟踪符号；仓库源码可能与网页版本不同。本批没有执行固件构建或硬件操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P062_USB设备固件升级API.md) · [返回大纲](大纲.md) · [下一章](P064_USB设备固件升级示例.md)
