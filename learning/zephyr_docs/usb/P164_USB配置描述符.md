---
id: learning.zephyr-docs.usb.api-164
title: USB配置描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__cfg__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第164章\_USB配置描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__cfg__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 164.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 标准配置描述符（Standard Configuration Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 标准配置描述符（Standard Configuration Descriptor）。

参见规范中的表 9-10。

## 164.2\_数据成员（Data Fields）

<a id="r_a04fb3193880a8676f686f0f2ad8adbf4"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P164_USB配置描述符.md#a04fb3193880a8676f686f0f2ad8adbf4)。

<a id="r_aa89fd9e8dd2bace7709d77de1d0b2588"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P164_USB配置描述符.md#aa89fd9e8dd2bace7709d77de1d0b2588)。

<a id="r_ae7f2a2fde3210e6460b20b0d17b820de"></a>

```c
uint16_t wTotalLength
```

配置的总长度（Total Length of Configuration）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTotalLength](P164_USB配置描述符.md#ae7f2a2fde3210e6460b20b0d17b820de)。

<a id="r_adcb6ff8c1accd4b950c9ebfd4f98718f"></a>

```c
uint8_t bNumInterfaces
```

接口数量（Number of Interfaces）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumInterfaces](P164_USB配置描述符.md#adcb6ff8c1accd4b950c9ebfd4f98718f)。

<a id="r_a7500c52ffbb63ece0be5cde7c672615d"></a>

```c
uint8_t bConfigurationValue
```

配置值（Configuration Value）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bConfigurationValue](P164_USB配置描述符.md#a7500c52ffbb63ece0be5cde7c672615d)。

<a id="r_ac3b8ca556e08a9b31fd0de906e000038"></a>

```c
uint8_t iConfiguration
```

配置字符串索引（Configuration String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iConfiguration](P164_USB配置描述符.md#ac3b8ca556e08a9b31fd0de906e000038)。

<a id="r_a6cc23afd69dd7fb77f4bc5ea55315f4c"></a>

```c
uint8_t bmAttributes
```

配置特性（Configuration Characteristics）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmAttributes](P164_USB配置描述符.md#a6cc23afd69dd7fb77f4bc5ea55315f4c)。

<a id="r_a717343eaf80cb0012cf87c9bc0c1c08f"></a>

```c
uint8_t bMaxPower
```

最大功耗（Maximum Power Consumption）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bMaxPower](P164_USB配置描述符.md#a717343eaf80cb0012cf87c9bc0c1c08f)。

## 164.3\_详细说明（Detailed Documentation）

<a id="a7500c52ffbb63ece0be5cde7c672615d"></a>

### 164.3.1\_`bConfigurationValue`

```c
uint8_t usb_cfg_descriptor::bConfigurationValue
```

配置值（Configuration Value）。

> 译注（源码核对）：这是选择配置的值。`sreq_set_configuration()` 从请求的 `wValue` 读取它，并检查相应配置是否存在；不要将设备描述符中的配置数量 `bNumConfigurations` 当成同一字段。

<a id="aa89fd9e8dd2bace7709d77de1d0b2588"></a>

### 164.3.2\_`bDescriptorType`

```c
uint8_t usb_cfg_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="a04fb3193880a8676f686f0f2ad8adbf4"></a>

### 164.3.3\_`bLength`

```c
uint8_t usb_cfg_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="a6cc23afd69dd7fb77f4bc5ea55315f4c"></a>

### 164.3.4\_`bmAttributes`

```c
uint8_t usb_cfg_descriptor::bmAttributes
```

配置特性（Configuration Characteristics）。

<a id="a717343eaf80cb0012cf87c9bc0c1c08f"></a>

### 164.3.5\_`bMaxPower`

```c
uint8_t usb_cfg_descriptor::bMaxPower
```

最大功耗（Maximum Power Consumption）。

<a id="adcb6ff8c1accd4b950c9ebfd4f98718f"></a>

### 164.3.6\_`bNumInterfaces`

```c
uint8_t usb_cfg_descriptor::bNumInterfaces
```

接口数量（Number of Interfaces）。

<a id="ac3b8ca556e08a9b31fd0de906e000038"></a>

### 164.3.7\_`iConfiguration`

```c
uint8_t usb_cfg_descriptor::iConfiguration
```

配置字符串索引（Configuration String Index）。

<a id="ae7f2a2fde3210e6460b20b0d17b820de"></a>

### 164.3.8\_`wTotalLength`

```c
uint16_t usb_cfg_descriptor::wTotalLength
```

配置的总长度（Total Length of Configuration）。

> 译注（源码核对）：这里包含配置描述符及其后续描述符的总长度。`sreq_get_desc_cfg()` 先复制配置头，再遍历各类的描述符列表，按 `bLength` 追加，最终响应还受设置包 `wLength` 限制；因此不能用配置头自身的 `bLength` 代替总长度。

## 164.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P163_USB设备描述符.md) · [返回大纲](大纲.md) · [下一章](P165_USB接口描述符.md)
