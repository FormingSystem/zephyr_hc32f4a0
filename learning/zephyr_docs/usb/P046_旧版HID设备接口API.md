---
id: learning.zephyr-docs.usb.api-46
title: 旧版HID设备接口API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__device__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_旧版HID设备接口API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__device__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 46.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

## 46.2\_数据结构（Data Structures）

<a id="r_hid_5Fops"></a>

```c
struct hid_ops
```

USB HID 设备接口。

相关声明：[hid_ops](P047_旧版HID回调接口.md)。

## 46.3\_类型定义（Typedefs）

<a id="r_ga04ec088255198d1597df8d70db6257ee"></a>

```c
typedef int(* hid_cb_t) (const struct device *dev, struct usb_setup_packet *setup, int32_t *len, uint8_t **data)
```



相关声明：[hid_cb_t](P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)、[device](../device_reference/P002_设备对象结构.md)、[usb_setup_packet](P160_USB控制请求包.md)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaed433e24f8487d4e451d9f9daa08c5b0"></a>

```c
typedef void(* hid_int_ready_callback) (const struct device *dev)
```



相关声明：[hid_int_ready_callback](P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gae3d308c55f5594cc0c926b52aaa28fc7"></a>

```c
typedef void(* hid_protocol_cb_t) (const struct device *dev, uint8_t protocol)
```



相关声明：[hid_protocol_cb_t](P046_旧版HID设备接口API.md#gae3d308c55f5594cc0c926b52aaa28fc7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga61b4facfbfb729159135f5c7534ca593"></a>

```c
typedef void(* hid_idle_cb_t) (const struct device *dev, uint16_t report_id)
```



相关声明：[hid_idle_cb_t](P046_旧版HID设备接口API.md#ga61b4facfbfb729159135f5c7534ca593)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

## 46.4\_函数（Functions）

<a id="r_ga8b08b633472ceb1323f09ef81176520f"></a>

```c
void usb_hid_register_device (const struct device *dev, const uint8_t *desc, size_t size, const struct hid_ops *op)
```

注册 HID 设备。

相关声明：[usb_hid_register_device](P046_旧版HID设备接口API.md#ga8b08b633472ceb1323f09ef81176520f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hid_ops](P047_旧版HID回调接口.md)。

<a id="r_ga9d82d48c9c6c94ad90e01f44c1f0e72b"></a>

```c
int hid_int_ep_write (const struct device *dev, const uint8_t *data, uint32_t data_len, uint32_t *bytes_ret)
```

向 USB HID 中断端点缓冲区写入数据。

相关声明：[hid_int_ep_write](P046_旧版HID设备接口API.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ga7d1b97dd70c25c816a2c78447be13c84"></a>

```c
int hid_int_ep_read (const struct device *dev, uint8_t *data, uint32_t max_data_len, uint32_t *ret_bytes)
```

从 USB HID 中断端点缓冲区读取数据。

相关声明：[hid_int_ep_read](P046_旧版HID设备接口API.md#ga7d1b97dd70c25c816a2c78447be13c84)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_gafb6073889bf17eb6a93bb8f182cd3f79"></a>

```c
int usb_hid_set_proto_code (const struct device *dev, uint8_t proto_code)
```

设置 USB HID 类协议代码（Protocol Code）。

相关声明：[usb_hid_set_proto_code](P046_旧版HID设备接口API.md#gafb6073889bf17eb6a93bb8f182cd3f79)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga88c23fc42f45f4ac05d9b2c1f6d7ec9b"></a>

```c
int usb_hid_init (const struct device *dev)
```

初始化 USB HID 类支持。

相关声明：[usb_hid_init](P046_旧版HID设备接口API.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)、[device](../device_reference/P002_设备对象结构.md)。

## 46.5\_详细说明（Detailed Documentation）

<a id="ga04ec088255198d1597df8d70db6257ee"></a>

### `hid_cb_t`

```c
typedef int(* hid_cb_t) (const struct device *dev, struct usb_setup_packet *setup, int32_t *len, uint8_t **data)
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

<a id="ga61b4facfbfb729159135f5c7534ca593"></a>

### `hid_idle_cb_t`

```c
typedef void(* hid_idle_cb_t) (const struct device *dev, uint16_t report_id)
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

<a id="gaed433e24f8487d4e451d9f9daa08c5b0"></a>

### `hid_int_ready_callback`

```c
typedef void(* hid_int_ready_callback) (const struct device *dev)
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

<a id="gae3d308c55f5594cc0c926b52aaa28fc7"></a>

### `hid_protocol_cb_t`

```c
typedef void(* hid_protocol_cb_t) (const struct device *dev, uint8_t protocol)
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

<a id="ga7d1b97dd70c25c816a2c78447be13c84"></a>

### `hid_int_ep_read()`

```c
int hid_int_ep_read ( const struct device * dev, uint8_t * data, uint32_t max_data_len, uint32_t * ret_bytes )
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

从 USB HID 中断端点缓冲区读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 USB HID 设备的指针。 |
| `[in] data` | 指向数据缓冲区的指针。 |
| `[in] max_data_len` | 要复制的数据的最大长度。 |
| `[out] ret_bytes` | 要复制的字节数。如果 data 为 NULL 且 max_data_len 为 0，则返回缓冲区中的可用字节数。 |

**已弃用（Deprecated）**：请改用[新版HID设备API](P042_新版HID设备API.md)。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：旧版设备栈启用 CONFIG_ENABLE_HID_INT_OUT_EP 时调用 usb_read()，否则返回 -ENOTSUP。新版栈提供的同名兼容包装则直接返回 -ENOTSUP；不能仅因符号可链接就假定旧版OUT读取行为仍可用。新版使用 output_report 或 set_report 回调。

<a id="ga9d82d48c9c6c94ad90e01f44c1f0e72b"></a>

### `hid_int_ep_write()`

```c
int hid_int_ep_write ( const struct device * dev, const uint8_t * data, uint32_t data_len, uint32_t * bytes_ret )
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

向 USB HID 中断端点缓冲区写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 USB HID 设备的指针。 |
| `[in] data` | 指向数据缓冲区的指针。 |
| `[in] data_len` | 要复制的数据长度。 |
| `[out] bytes_ret` | 写入端点缓冲区的字节数。 |

**已弃用（Deprecated）**：请改用[新版HID设备API](P042_新版HID设备API.md)。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：旧版实现经 usb_write() 写入；新版兼容包装转发到 hid_device_submit_report()，并把成功时的输入长度写入 bytes_ret。两条实现路径的缓冲区与完成约定不同，迁移时应阅读新版提交接口。

<a id="ga88c23fc42f45f4ac05d9b2c1f6d7ec9b"></a>

### `usb_hid_init()`

```c
int usb_hid_init ( const struct device * dev)
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

初始化 USB HID 类支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 USB HID 设备的指针。 |

**已弃用（Deprecated）**：请改用[新版HID设备API](P042_新版HID设备API.md)。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：旧版实现建立类描述符相关信息；新版兼容包装仅记录日志并返回0，不初始化新版设备栈。不能以这一返回值证明已完成 usbd_init() 或已被主机枚举。

<a id="ga8b08b633472ceb1323f09ef81176520f"></a>

### `usb_hid_register_device()`

```c
void usb_hid_register_device ( const struct device * dev, const uint8_t * desc, size_t size, const struct hid_ops * op )
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

注册 HID 设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 USB HID 设备的指针。 |
| `[in] desc` | 指向 HID 报告描述符的指针。 |
| `[in] size` | HID 报告描述符的大小。 |
| `[in] op` | 指向 USB HID 设备中断结构的指针。 |

**已弃用（Deprecated）**：请改用[新版HID设备API](P042_新版HID设备API.md)。

> 译注（源码核对）：此旧接口返回 void。新版兼容包装保存旧回调指针并调用 hid_device_register()，失败时仅记录日志；不能从该接口获得新版注册的返回错误码。新增实现优先直接使用新版接口。

<a id="gafb6073889bf17eb6a93bb8f182cd3f79"></a>

### `usb_hid_set_proto_code()`

```c
int usb_hid_set_proto_code ( const struct device * dev, uint8_t proto_code )
```

```c
#include <zephyr/usb/class/usb_hid.h>
```

设置 USB HID 类协议代码（Protocol Code）。

应在 usb_hid_init() 之前调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 USB HID 设备的指针。 |
| `[in] proto_code` | 用于 bInterfaceProtocol 的协议代码。 |

**已弃用（Deprecated）**：请改用[新版HID设备API](P042_新版HID设备API.md)。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：原接口约定在初始化前设置接口协议代码；旧版实现仅在 CONFIG_USB_HID_BOOT_PROTOCOL 启用时写入描述符，否则返回 -ENOTSUP；新版兼容包装不修改它，而是提示使用设备树 protocol-code 属性，随后返回0。协议代码 bInterfaceProtocol 与主机 Set Protocol 选择的协议状态不是同一字段。

> 译注：本页保留已弃用接口用于迁移和源码对照；新实现参阅[新版HID设备API](P042_新版HID设备API.md)。

## 46.6\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P045_旧版HID类API.md) · [返回大纲](大纲.md) · [下一章](P047_旧版HID回调接口.md)
