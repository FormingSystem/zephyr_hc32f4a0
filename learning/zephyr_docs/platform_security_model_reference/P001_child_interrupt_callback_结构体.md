---
id: learning.zephyr-docs.platform-security-model-reference.page-1
title: child_interrupt_callback_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structchild__interrupt__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_child\_interrupt\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structchild__interrupt__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

子设备中断（Child Device Interrupt）的回调结构。

```c
#include <zephyr/drivers/mfd/adp5360.h>
```

<a id="details"></a>

子设备中断（Child Device Interrupt）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_afbc9665751acb8a988ae26c0f9a9234b"></a>

```c
mfd_adp5360_interrupt_callback handler
```

相关声明：[mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)、[handler](#afbc9665751acb8a988ae26c0f9a9234b)。

中断处理回调（Interrupt handler callback）。

<a id="r_adaea37814d1ee4167271cadc7b45255c"></a>

```c
void * user_data
```

相关声明：[user_data](#adaea37814d1ee4167271cadc7b45255c)。

回调的用户数据。

## 1.2\_详细说明（Detailed Documentation）

<a id="afbc9665751acb8a988ae26c0f9a9234b"></a>

### `handler`

```c
mfd_adp5360_interrupt_callback child_interrupt_callback::handler
```

中断处理回调（Interrupt handler callback）。

<a id="adaea37814d1ee4167271cadc7b45255c"></a>

### `user_data`

```c
void* child_interrupt_callback::user_data
```

回调的用户数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/adp5360.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/adp5360.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2adp5360_8h_source.html)
- [mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_dw_ace_v1_ictl_driver_api_结构体.md)
