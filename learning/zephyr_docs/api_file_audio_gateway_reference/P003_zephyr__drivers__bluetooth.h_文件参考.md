---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-3
title: zephyr__drivers__bluetooth.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_bluetooth.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙主机控制器接口（HCI）的驱动API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/hci_vs.h>
#include <zephyr/device.h>
```

查看此文件的源码。

蓝牙 HCI 驱动 API（Bluetooth HCI Driver API）的主头文件。Copyright (c) 2024 Johan Hedberg SPDX-License-Identifier: Apache-2.0

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Fsetup_5Fparams"></a>

```c
struct bt_hci_setup_params
```

相关声明：[bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)。

驱动 API 操作 `setup()` 的参数。

<a id="r_bt_5Fhci_5Fdriver_5Fconfig"></a>

```c
struct bt_hci_driver_config
```

相关声明：[bt_hci_driver_config](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md)。

蓝牙 HCI 驱动通用配置（Common Driver Configuration）。

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga5e61116282ab2555f1dcd93c2858157e"></a>

```c
#define BT_DT_HCI_QUIRK_OR(node_id, prop, idx)
```

相关声明：[BT_DT_HCI_QUIRK_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga5e61116282ab2555f1dcd93c2858157e)。

<a id="r_ga73fc76e779a3dd45a680b09063471887"></a>

```c
#define BT_DT_HCI_QUIRKS_GET(node_id)
```

相关声明：[BT_DT_HCI_QUIRKS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga73fc76e779a3dd45a680b09063471887)。

<a id="r_ga9e97337a538670bbc2dde4b35a6c8a25"></a>

```c
#define BT_DT_HCI_QUIRKS_INST_GET(inst)
```

相关声明：[BT_DT_HCI_QUIRKS_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9e97337a538670bbc2dde4b35a6c8a25)。

<a id="r_gaf66891071ade556e5906e71f0f0d2678"></a>

```c
#define BT_DT_HCI_NAME_GET(node_id)
```

相关声明：[BT_DT_HCI_NAME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf66891071ade556e5906e71f0f0d2678)。

<a id="r_gae14d26da17a9b761226f9c68537d4161"></a>

```c
#define BT_DT_HCI_NAME_INST_GET(inst)
```

相关声明：[BT_DT_HCI_NAME_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gae14d26da17a9b761226f9c68537d4161)。

<a id="r_gaa9e7164af99dba0d6e8d409d79249e65"></a>

```c
#define BT_PRIV_HCI_BUS_DEFAULT (0)
```

相关声明：[BT_PRIV_HCI_BUS_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaa9e7164af99dba0d6e8d409d79249e65)。

<a id="r_ga766eaafe5d88d9d1efa0b3f09a334fc8"></a>

```c
#define BT_DT_HCI_BUS_GET(node_id)
```

相关声明：[BT_DT_HCI_BUS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga766eaafe5d88d9d1efa0b3f09a334fc8)。

<a id="r_gafb7922cf9937229bb75ab7b4fd7c37bb"></a>

```c
#define BT_DT_HCI_BUS_INST_GET(inst)
```

相关声明：[BT_DT_HCI_BUS_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gafb7922cf9937229bb75ab7b4fd7c37bb)。

<a id="r_ga3c8d5a12ea0c52d0934ee57c213f1fbe"></a>

```c
#define BT_DT_HCI_DRIVER_CONFIG_GET(node_id)
```

相关声明：[BT_DT_HCI_DRIVER_CONFIG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga3c8d5a12ea0c52d0934ee57c213f1fbe)。

bt_hci_driver_config 结构体的静态初始化器（Static Initializer）。

<a id="r_ga6814df9213fa7e3d6506dcf25d6feae4"></a>

```c
#define BT_DT_HCI_DRIVER_CONFIG_INST_GET(inst)
```

相关声明：[BT_DT_HCI_DRIVER_CONFIG_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga6814df9213fa7e3d6506dcf25d6feae4)。

由 DT_DRV_COMPAT 实例生成的 bt_hci_driver_config 结构体静态初始化器（Static Initializer）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga79b12569871b2b6c8420c245e9505aed"></a>

```c
typedef int(* bt_hci_recv_t) (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga79b12569871b2b6c8420c245e9505aed)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 HCI 数据从控制器（Controller）交付给主机（Host）。

<a id="r_gad45ae0f5e6f085f7a787257f1315df86"></a>

```c
typedef int(* bt_hci_api_open_t) (const struct device *dev)
```

相关声明：[bt_hci_api_open_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#gad45ae0f5e6f085f7a787257f1315df86)、[device](../device_reference/P002_设备对象结构.md)。

打开 HCI 传输的回调 API。

<a id="r_ga93b2a7f403463aa7a1eaf94d7f17c01c"></a>

```c
typedef int(* bt_hci_api_close_t) (const struct device *dev)
```

相关声明：[bt_hci_api_close_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga93b2a7f403463aa7a1eaf94d7f17c01c)、[device](../device_reference/P002_设备对象结构.md)。

关闭 HCI 传输的回调 API。

<a id="r_ga29f6af67c9ba45d0945c6de1424ea617"></a>

```c
typedef int(* bt_hci_api_send_t) (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_api_send_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga29f6af67c9ba45d0945c6de1424ea617)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 HCI 缓冲区发送给控制器的回调 API。

<a id="r_gaa3205fd69fa1e7f00ea94a492fa9140f"></a>

```c
typedef int(* bt_hci_api_setup_t) (const struct device *dev, const struct bt_hci_setup_params *param)
```

相关声明：[bt_hci_api_setup_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#gaa3205fd69fa1e7f00ea94a492fa9140f)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)。

执行 HCI 厂商专用设置（Vendor-specific Setup）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga687e88a53cddde1d7cbf3057678e66c5"></a>

```c
enum { BT_HCI_QUIRK_NO_RESET = BIT(0) , BT_HCI_QUIRK_NO_AUTO_DLE = BIT(1) , BT_HCI_QUIRK_NO_FLOW_CONTROL = BIT(2) }
```

相关声明：[BT_HCI_QUIRK_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)、[BT_HCI_QUIRK_NO_AUTO_DLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)、[BT_HCI_QUIRK_NO_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_gaad2dc7f911913468a1440fad91cb3d62"></a>

```c
static int bt_hci_recv_err (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从驱动交付 HCI 数据包（HCI Packet）。

<a id="r_ga407beb20238b8fe6fdbd4ef199eb1f6c"></a>

```c
static void bt_hci_recv (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从驱动交付 HCI 数据包（HCI Packet）。

<a id="r_gac744c98801cea5afd13d6774154e71c8"></a>

```c
static int bt_hci_open (const struct device *dev, bt_hci_recv_t recv)
```

相关声明：[bt_hci_open](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_recv_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga79b12569871b2b6c8420c245e9505aed)、[recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)。

打开 HCI 传输通道（HCI Transport）。

<a id="r_ga4baab0790149536873e5d9e0cb14359f"></a>

```c
static bool bt_hci_can_close (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_hci_can_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga4baab0790149536873e5d9e0cb14359f)、[device](../device_reference/P002_设备对象结构.md)。

检查 HCI 传输通道（HCI Transport）是否可以关闭。

<a id="r_gad187f0aff959a4756b281aa33d1b4394"></a>

```c
static int bt_hci_close (const struct device *dev)
```

相关声明：[bt_hci_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)、[device](../device_reference/P002_设备对象结构.md)。

关闭 HCI 传输通道（HCI Transport）。

<a id="r_ga64079b6f03479561c1c7d09b3af81ede"></a>

```c
static int bt_hci_send (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向控制器（Controller）发送 HCI 缓冲区。

<a id="r_ga45ce7bf5fe86f5fff3d8838d247b1d47"></a>

```c
static int bt_hci_setup (const struct device *dev, struct bt_hci_setup_params *params)
```

相关声明：[bt_hci_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)。

HCI 厂商专有设置（Vendor-specific Setup）。

<a id="r_ga9df830679cdec440f96e37b608c7fdf7"></a>

```c
void bt_hci_set_public_addr (const struct device *dev, const bt_addr_t *addr)
```

相关声明：[bt_hci_set_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9df830679cdec440f96e37b608c7fdf7)、[device](../device_reference/P002_设备对象结构.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

设置控制器的公共身份地址（Public Identity Address）。

<a id="r_gaf2f4e86132f321c6c7f20965dd5c1f0d"></a>

```c
const bt_addr_t * bt_hci_get_public_addr (const struct device *dev)
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_hci_get_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)、[device](../device_reference/P002_设备对象结构.md)。

获取驱动应配置的公共身份地址（Public Identity Address）。

<a id="r_add813c1343955a7bb95135eb0fbe9cd5"></a>

```c
int bt_hci_transport_setup (const struct device *dev)
```

相关声明：[bt_hci_transport_setup](#add813c1343955a7bb95135eb0fbe9cd5)、[device](../device_reference/P002_设备对象结构.md)。

设置 HCI 传输通道（HCI Transport），通常意味着复位蓝牙芯片（IC）。

<a id="r_ae29dbf165252ddf9085c7387706fd09c"></a>

```c
int bt_hci_transport_teardown (const struct device *dev)
```

相关声明：[bt_hci_transport_teardown](#ae29dbf165252ddf9085c7387706fd09c)、[device](../device_reference/P002_设备对象结构.md)。

拆除 HCI 传输通道（Teardown HCI Transport）。

<a id="r_a362df79e2f782159f7e85d63817421bb"></a>

```c
struct net_buf * bt_hci_evt_create (uint8_t evt, uint8_t len)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hci_evt_create](#a362df79e2f782159f7e85d63817421bb)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 HCI 事件缓冲区（Event Buffer）。

<a id="r_a8ab7dc7d38f3bc7be72e34d7a9f14212"></a>

```c
struct net_buf * bt_hci_cmd_complete_create (uint16_t op, uint8_t plen)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hci_cmd_complete_create](#a8ab7dc7d38f3bc7be72e34d7a9f14212)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 HCI 命令完成事件缓冲区（Command Complete Event Buffer）。

<a id="r_ab6b790e6dd0e8251d6cf10b0a7cce5f7"></a>

```c
struct net_buf * bt_hci_cmd_status_create (uint16_t op, uint8_t status)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hci_cmd_status_create](#ab6b790e6dd0e8251d6cf10b0a7cce5f7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 HCI 命令状态事件缓冲区（Command Status Event Buffer）。

## 3.6\_详细说明（Detailed Documentation）

<a id="a8ab7dc7d38f3bc7be72e34d7a9f14212"></a>

### `bt_hci_cmd_complete_create()`

```c
struct net_buf * bt_hci_cmd_complete_create ( uint16_t op, uint8_t plen )
```

分配 HCI 命令完成事件缓冲区（Command Complete Event Buffer）。

为 HCI 命令完成事件（Command Complete Event）分配新缓冲区。输入为操作码（OpCode，例如使用 BT_OP 宏编码）和参数总长度。成功返回后，即可将参数编码到缓冲区中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `op` | HCI 命令操作码（OpCode）。 |
| `plen` | 命令参数长度。 |

**返回（Returns）**：返回值（Returns）：新分配的缓冲区。

<a id="ab6b790e6dd0e8251d6cf10b0a7cce5f7"></a>

### `bt_hci_cmd_status_create()`

```c
struct net_buf * bt_hci_cmd_status_create ( uint16_t op, uint8_t status )
```

分配 HCI 命令状态事件缓冲区（Command Status Event Buffer）。

为 HCI 命令状态事件（Command Status Event）分配新缓冲区。输入为操作码（OpCode，例如使用 BT_OP 宏编码）和状态码。成功返回后，即可将参数编码到缓冲区中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `op` | HCI 命令操作码（OpCode）。 |
| `status` | 状态码（Status code）。 |

**返回（Returns）**：返回值（Returns）：新分配的缓冲区。

<a id="a362df79e2f782159f7e85d63817421bb"></a>

### `bt_hci_evt_create()`

```c
struct net_buf * bt_hci_evt_create ( uint8_t evt, uint8_t len )
```

分配 HCI 事件缓冲区（Event Buffer）。

为 HCI 事件（HCI Event）分配新缓冲区。输入为事件码和参数总长度。成功返回后，即可将参数编码到缓冲区中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `evt` | HCI 事件操作码（OpCode）。 |
| `len` | 事件参数长度。 |

**返回（Returns）**：返回值（Returns）：新分配的缓冲区。

<a id="add813c1343955a7bb95135eb0fbe9cd5"></a>

### `bt_hci_transport_setup()`

```c
int bt_hci_transport_setup ( const struct device * dev)
```

设置 HCI 传输通道（HCI Transport），通常意味着复位蓝牙芯片（IC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 连接该芯片（IC）的总线的设备结构体 |

**说明（Note）**：注意（Note）：H4 驱动中包含此函数的弱定义版本（Weak Version），因此每块开发板可选择是否定义它。

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负错误值。

<a id="ae29dbf165252ddf9085c7387706fd09c"></a>

### `bt_hci_transport_teardown()`

```c
int bt_hci_transport_teardown ( const struct device * dev)
```

拆除 HCI 传输通道（Teardown HCI Transport）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 连接该芯片（IC）的总线的设备结构体 |

**说明（Note）**：注意（Note）：IPC 驱动中包含此函数的弱定义版本（Weak Version），因此可以选择是否定义它。NRF5340 支持将网络核（Network Core）置于复位状态。

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负错误值。


## 3.7\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/bluetooth/buf.h](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/hci_vs.h](../api_source_device_reference/P020_hci_vs.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_device_reference/P007_bluetooth.h_源码浏览.md)
- [bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)
- [bt_hci_driver_config](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md)
- [bt_hci_driver_data](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md)
- [bt_hci_driver_api](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md)
- [BT_DT_HCI_QUIRK_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga5e61116282ab2555f1dcd93c2858157e)
- [BT_DT_HCI_QUIRKS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga73fc76e779a3dd45a680b09063471887)
- [BT_DT_HCI_QUIRKS_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9e97337a538670bbc2dde4b35a6c8a25)
- [BT_DT_HCI_NAME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf66891071ade556e5906e71f0f0d2678)
- [BT_DT_HCI_NAME_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gae14d26da17a9b761226f9c68537d4161)
- [BT_PRIV_HCI_BUS_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaa9e7164af99dba0d6e8d409d79249e65)
- [BT_DT_HCI_BUS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga766eaafe5d88d9d1efa0b3f09a334fc8)
- [BT_DT_HCI_BUS_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gafb7922cf9937229bb75ab7b4fd7c37bb)
- [BT_DT_HCI_DRIVER_CONFIG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga3c8d5a12ea0c52d0934ee57c213f1fbe)
- [BT_DT_HCI_DRIVER_CONFIG_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga6814df9213fa7e3d6506dcf25d6feae4)
- [bt_hci_recv_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga79b12569871b2b6c8420c245e9505aed)
- [device](../device_reference/P002_设备对象结构.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hci_api_open_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#gad45ae0f5e6f085f7a787257f1315df86)
- [bt_hci_api_close_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga93b2a7f403463aa7a1eaf94d7f17c01c)
- [bt_hci_api_send_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga29f6af67c9ba45d0945c6de1424ea617)
- [bt_hci_api_setup_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#gaa3205fd69fa1e7f00ea94a492fa9140f)
- [BT_HCI_QUIRK_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)
- [BT_HCI_QUIRK_NO_AUTO_DLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)
- [BT_HCI_QUIRK_NO_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea)
- [bt_hci_recv_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)
- [bt_hci_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)
- [bt_hci_open](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_hci_can_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga4baab0790149536873e5d9e0cb14359f)
- [bt_hci_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)
- [bt_hci_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)
- [bt_hci_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)
- [bt_hci_set_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9df830679cdec440f96e37b608c7fdf7)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bt_hci_get_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_zephyr__audio__codec.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__led.h_文件参考.md)
