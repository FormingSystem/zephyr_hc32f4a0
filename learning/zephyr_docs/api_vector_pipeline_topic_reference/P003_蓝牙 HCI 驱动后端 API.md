---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-3
title: 蓝牙 HCI 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙 HCI 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现蓝牙主机控制器接口（Bluetooth HCI）驱动所需的 API 类型定义、回调签名及其他辅助项。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Fdriver_5Fdata"></a>

```c
struct bt_hci_driver_data
```

相关声明：[bt_hci_driver_data](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md)。

蓝牙 HCI 驱动通用数据（Common Driver Data）。

<a id="r_bt_5Fhci_5Fdriver_5Fapi"></a>

```c
struct bt_hci_driver_api
```

相关声明：[bt_hci_driver_api](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md)。

驱动操作（Driver Operations）：蓝牙 HCI 驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_ga79b12569871b2b6c8420c245e9505aed"></a>

```c
typedef int(* bt_hci_recv_t) (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv_t](#ga79b12569871b2b6c8420c245e9505aed)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 HCI 数据从控制器（Controller）交付给主机（Host）。

<a id="r_gad45ae0f5e6f085f7a787257f1315df86"></a>

```c
typedef int(* bt_hci_api_open_t) (const struct device *dev)
```

相关声明：[bt_hci_api_open_t](#gad45ae0f5e6f085f7a787257f1315df86)、[device](../device_reference/P002_设备对象结构.md)。

打开 HCI 传输的回调 API。

<a id="r_ga93b2a7f403463aa7a1eaf94d7f17c01c"></a>

```c
typedef int(* bt_hci_api_close_t) (const struct device *dev)
```

相关声明：[bt_hci_api_close_t](#ga93b2a7f403463aa7a1eaf94d7f17c01c)、[device](../device_reference/P002_设备对象结构.md)。

关闭 HCI 传输的回调 API。

<a id="r_ga29f6af67c9ba45d0945c6de1424ea617"></a>

```c
typedef int(* bt_hci_api_send_t) (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_api_send_t](#ga29f6af67c9ba45d0945c6de1424ea617)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 HCI 缓冲区发送给控制器的回调 API。

<a id="r_gaa3205fd69fa1e7f00ea94a492fa9140f"></a>

```c
typedef int(* bt_hci_api_setup_t) (const struct device *dev, const struct bt_hci_setup_params *param)
```

相关声明：[bt_hci_api_setup_t](#gaa3205fd69fa1e7f00ea94a492fa9140f)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)。

执行 HCI 厂商专用设置（Vendor-specific Setup）的回调 API。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga93b2a7f403463aa7a1eaf94d7f17c01c"></a>

### `bt_hci_api_close_t`

```c
typedef int(* bt_hci_api_close_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

关闭 HCI 传输的回调 API。

参数说明参见 `bt_hci_close()`。

<a id="gad45ae0f5e6f085f7a787257f1315df86"></a>

### `bt_hci_api_open_t`

```c
typedef int(* bt_hci_api_open_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

打开 HCI 传输的回调 API。

参数说明参见 `bt_hci_open()`。

<a id="ga29f6af67c9ba45d0945c6de1424ea617"></a>

### `bt_hci_api_send_t`

```c
typedef int(* bt_hci_api_send_t) (const struct device *dev, struct net_buf *buf)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

将 HCI 缓冲区发送给控制器的回调 API。

参数说明参见 `bt_hci_send()`。

<a id="gaa3205fd69fa1e7f00ea94a492fa9140f"></a>

### `bt_hci_api_setup_t`

```c
typedef int(* bt_hci_api_setup_t) (const struct device *dev, const struct bt_hci_setup_params *param)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

执行 HCI 厂商专用设置（Vendor-specific Setup）的回调 API。

参数说明参见 `bt_hci_setup()`。

**已弃用（Deprecated）**：已弃用（Deprecated）：参见 `bt_hci_setup()`。

<a id="ga79b12569871b2b6c8420c245e9505aed"></a>

### `bt_hci_recv_t`

```c
typedef int(* bt_hci_recv_t) (const struct device *dev, struct net_buf *buf)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

将 HCI 数据从控制器（Controller）交付给主机（Host）。

使用 `bt_hci_open()` 注册。HCI 驱动在线程上下文（Thread Context）调用此回调；在 `bt_hci_open()` 返回前就可能调用，而在 `bt_hci_close()` 成功返回后不再调用。


## 3.4\_原页交叉引用（Cross References）

- [bt_hci_driver_data](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md)
- [bt_hci_driver_api](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)
- [zephyr/drivers/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html)
- [bt_hci_close()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)
- [bt_hci_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)
- [bt_hci_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)
- [bt_hci_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)
- [Deprecated](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000003)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P002_GOEP 的 RFCOMM 传输.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据.md)
