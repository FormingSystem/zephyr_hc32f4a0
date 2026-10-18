---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-5
title: 蓝牙主机控制器接口（Bluetooth HCI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_蓝牙主机控制器接口（Bluetooth HCI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙主机控制器接口（Host Controller Interface，HCI）的相关接口。

<a id="details"></a>

蓝牙主机控制器接口（Host Controller Interface，HCI）。引入版本（Since）：3.7；API 版本（Version）：0.3.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 5.1\_主题（Topics）

<a id="r_bt_5Fhci_5Fh4"></a>

相关声明：[蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。](../api_connection_topic_reference/P003_蓝牙H_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。.md)。

蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。

<a id="r_bt_5Fhci_5Fapi_5Fbackend"></a>

相关声明：[蓝牙 HCI 驱动后端 API](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md)。

<a id="r_bt_5Fhci_5Flockstep"></a>

相关声明：[蓝牙HCI锁步命令（Lockstep Command）的辅助接口。](../api_radio_permission_topic_reference/P003_蓝牙HCI锁步命令（Lockstep Command）的辅助接口。.md)。

蓝牙HCI锁步命令（Lockstep Command）的辅助接口。

<a id="header-files"></a>
<a id="files"></a>

## 5.2\_文件（Files）

<a id="r_bluetooth_2Eh"></a>

```c
file bluetooth.h
```

相关声明：[bluetooth.h](../api_file_audio_gateway_reference/P003_zephyr__drivers__bluetooth.h_文件参考.md)。

蓝牙主机控制器接口（HCI）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.4\_宏定义（Macros）

<a id="r_ga5e61116282ab2555f1dcd93c2858157e"></a>

```c
#define BT_DT_HCI_QUIRK_OR(node_id, prop, idx)
```

相关声明：[BT_DT_HCI_QUIRK_OR](#ga5e61116282ab2555f1dcd93c2858157e)。

<a id="r_ga73fc76e779a3dd45a680b09063471887"></a>

```c
#define BT_DT_HCI_QUIRKS_GET(node_id)
```

相关声明：[BT_DT_HCI_QUIRKS_GET](#ga73fc76e779a3dd45a680b09063471887)。

<a id="r_ga9e97337a538670bbc2dde4b35a6c8a25"></a>

```c
#define BT_DT_HCI_QUIRKS_INST_GET(inst)
```

相关声明：[BT_DT_HCI_QUIRKS_INST_GET](#ga9e97337a538670bbc2dde4b35a6c8a25)。

<a id="r_gaf66891071ade556e5906e71f0f0d2678"></a>

```c
#define BT_DT_HCI_NAME_GET(node_id)
```

相关声明：[BT_DT_HCI_NAME_GET](#gaf66891071ade556e5906e71f0f0d2678)。

<a id="r_gae14d26da17a9b761226f9c68537d4161"></a>

```c
#define BT_DT_HCI_NAME_INST_GET(inst)
```

相关声明：[BT_DT_HCI_NAME_INST_GET](#gae14d26da17a9b761226f9c68537d4161)。

<a id="r_gaa9e7164af99dba0d6e8d409d79249e65"></a>

```c
#define BT_PRIV_HCI_BUS_DEFAULT (0)
```

相关声明：[BT_PRIV_HCI_BUS_DEFAULT](#gaa9e7164af99dba0d6e8d409d79249e65)。

<a id="r_ga766eaafe5d88d9d1efa0b3f09a334fc8"></a>

```c
#define BT_DT_HCI_BUS_GET(node_id)
```

相关声明：[BT_DT_HCI_BUS_GET](#ga766eaafe5d88d9d1efa0b3f09a334fc8)。

<a id="r_gafb7922cf9937229bb75ab7b4fd7c37bb"></a>

```c
#define BT_DT_HCI_BUS_INST_GET(inst)
```

相关声明：[BT_DT_HCI_BUS_INST_GET](#gafb7922cf9937229bb75ab7b4fd7c37bb)。

<a id="r_ga3c8d5a12ea0c52d0934ee57c213f1fbe"></a>

```c
#define BT_DT_HCI_DRIVER_CONFIG_GET(node_id)
```

相关声明：[BT_DT_HCI_DRIVER_CONFIG_GET](#ga3c8d5a12ea0c52d0934ee57c213f1fbe)。

bt_hci_driver_config 结构体的静态初始化器（Static Initializer）。

<a id="r_ga6814df9213fa7e3d6506dcf25d6feae4"></a>

```c
#define BT_DT_HCI_DRIVER_CONFIG_INST_GET(inst)
```

相关声明：[BT_DT_HCI_DRIVER_CONFIG_INST_GET](#ga6814df9213fa7e3d6506dcf25d6feae4)。

由 DT_DRV_COMPAT 实例生成的 bt_hci_driver_config 结构体静态初始化器（Static Initializer）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.5\_枚举（Enumerations）

<a id="r_ga687e88a53cddde1d7cbf3057678e66c5"></a>

```c
enum { BT_HCI_QUIRK_NO_RESET = BIT(0) , BT_HCI_QUIRK_NO_AUTO_DLE = BIT(1) , BT_HCI_QUIRK_NO_FLOW_CONTROL = BIT(2) }
```

相关声明：[BT_HCI_QUIRK_NO_RESET](#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)、[BT_HCI_QUIRK_NO_AUTO_DLE](#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)、[BT_HCI_QUIRK_NO_FLOW_CONTROL](#gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.6\_函数（Functions）

<a id="r_gaad2dc7f911913468a1440fad91cb3d62"></a>

```c
static int bt_hci_recv_err (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv_err](#gaad2dc7f911913468a1440fad91cb3d62)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从驱动交付 HCI 数据包（HCI Packet）。

<a id="r_ga407beb20238b8fe6fdbd4ef199eb1f6c"></a>

```c
static void bt_hci_recv (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_recv](#ga407beb20238b8fe6fdbd4ef199eb1f6c)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从驱动交付 HCI 数据包（HCI Packet）。

<a id="r_gac744c98801cea5afd13d6774154e71c8"></a>

```c
static int bt_hci_open (const struct device *dev, bt_hci_recv_t recv)
```

相关声明：[bt_hci_open](#gac744c98801cea5afd13d6774154e71c8)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_recv_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga79b12569871b2b6c8420c245e9505aed)、[recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)。

打开 HCI 传输通道（HCI Transport）。

<a id="r_ga4baab0790149536873e5d9e0cb14359f"></a>

```c
static bool bt_hci_can_close (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_hci_can_close](#ga4baab0790149536873e5d9e0cb14359f)、[device](../device_reference/P002_设备对象结构.md)。

检查 HCI 传输通道（HCI Transport）是否可以关闭。

<a id="r_gad187f0aff959a4756b281aa33d1b4394"></a>

```c
static int bt_hci_close (const struct device *dev)
```

相关声明：[bt_hci_close](#gad187f0aff959a4756b281aa33d1b4394)、[device](../device_reference/P002_设备对象结构.md)。

关闭 HCI 传输通道（HCI Transport）。

<a id="r_ga64079b6f03479561c1c7d09b3af81ede"></a>

```c
static int bt_hci_send (const struct device *dev, struct net_buf *buf)
```

相关声明：[bt_hci_send](#ga64079b6f03479561c1c7d09b3af81ede)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向控制器（Controller）发送 HCI 缓冲区。

<a id="r_ga45ce7bf5fe86f5fff3d8838d247b1d47"></a>

```c
static int bt_hci_setup (const struct device *dev, struct bt_hci_setup_params *params)
```

相关声明：[bt_hci_setup](#ga45ce7bf5fe86f5fff3d8838d247b1d47)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)。

HCI 厂商专有设置（Vendor-specific Setup）。

<a id="r_ga9df830679cdec440f96e37b608c7fdf7"></a>

```c
void bt_hci_set_public_addr (const struct device *dev, const bt_addr_t *addr)
```

相关声明：[bt_hci_set_public_addr](#ga9df830679cdec440f96e37b608c7fdf7)、[device](../device_reference/P002_设备对象结构.md)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

设置控制器的公共身份地址（Public Identity Address）。

<a id="r_gaf2f4e86132f321c6c7f20965dd5c1f0d"></a>

```c
const bt_addr_t * bt_hci_get_public_addr (const struct device *dev)
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_hci_get_public_addr](#gaf2f4e86132f321c6c7f20965dd5c1f0d)、[device](../device_reference/P002_设备对象结构.md)。

获取驱动应配置的公共身份地址（Public Identity Address）。

## 5.7\_详细说明（Detailed Documentation）

<a id="ga766eaafe5d88d9d1efa0b3f09a334fc8"></a>

### `BT_DT_HCI_BUS_GET`

```c
#define BT_DT_HCI_BUS_GET ( node_id)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
DT_ENUM_IDX_OR(node_id, bt_hci_bus, BT_PRIV_HCI_BUS_DEFAULT)
```

<a id="gafb7922cf9937229bb75ab7b4fd7c37bb"></a>

### `BT_DT_HCI_BUS_INST_GET`

```c
#define BT_DT_HCI_BUS_INST_GET ( inst)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
BT_DT_HCI_BUS_GET(DT_DRV_INST(inst))
```

<a id="ga3c8d5a12ea0c52d0934ee57c213f1fbe"></a>

### `BT_DT_HCI_DRIVER_CONFIG_GET`

```c
#define BT_DT_HCI_DRIVER_CONFIG_GET ( node_id)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
{                                                                                       \
        .quirks = (uint32_t)BT_DT_HCI_QUIRKS_GET(node_id),                                \
}
```

bt_hci_driver_config 结构体的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |

<a id="ga6814df9213fa7e3d6506dcf25d6feae4"></a>

### `BT_DT_HCI_DRIVER_CONFIG_INST_GET`

```c
#define BT_DT_HCI_DRIVER_CONFIG_INST_GET ( inst)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
BT_DT_HCI_DRIVER_CONFIG_GET(DT_DRV_INST(inst))
```

由 DT_DRV_COMPAT 实例生成的 bt_hci_driver_config 结构体静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |

**参阅（See Also）**：另请参阅（See Also）：BT_DT_HCI_DRIVER_CONFIG_GET()。

<a id="gaf66891071ade556e5906e71f0f0d2678"></a>

### `BT_DT_HCI_NAME_GET`

```c
#define BT_DT_HCI_NAME_GET ( node_id)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
DT_PROP_OR(node_id, bt_hci_name, "HCI")
```

<a id="gae14d26da17a9b761226f9c68537d4161"></a>

### `BT_DT_HCI_NAME_INST_GET`

```c
#define BT_DT_HCI_NAME_INST_GET ( inst)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
BT_DT_HCI_NAME_GET(DT_DRV_INST(inst))
```

<a id="ga5e61116282ab2555f1dcd93c2858157e"></a>

### `BT_DT_HCI_QUIRK_OR`

```c
#define BT_DT_HCI_QUIRK_OR ( node_id, prop, idx )
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
UTIL_CAT(BT_HCI_QUIRK_, DT_STRING_UPPER_TOKEN_BY_IDX(node_id, prop, idx))
```

<a id="ga73fc76e779a3dd45a680b09063471887"></a>

### `BT_DT_HCI_QUIRKS_GET`

```c
#define BT_DT_HCI_QUIRKS_GET ( node_id)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, bt_hci_quirks), \
(DT_FOREACH_PROP_ELEM_SEP(node_id, \
                          bt_hci_quirks, \
                          BT_DT_HCI_QUIRK_OR, \
                          (|))), \
(0))
```

<a id="ga9e97337a538670bbc2dde4b35a6c8a25"></a>

### `BT_DT_HCI_QUIRKS_INST_GET`

```c
#define BT_DT_HCI_QUIRKS_INST_GET ( inst)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

展开值（Value）：

```c
BT_DT_HCI_QUIRKS_GET(DT_DRV_INST(inst))
```

<a id="gaa9e7164af99dba0d6e8d409d79249e65"></a>

### `BT_PRIV_HCI_BUS_DEFAULT`

```c
#define BT_PRIV_HCI_BUS_DEFAULT (0)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

<a id="ga687e88a53cddde1d7cbf3057678e66c5"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/drivers/bluetooth.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HCI_QUIRK_NO_RESET` |  |
| `BT_HCI_QUIRK_NO_AUTO_DLE` |  |
| `BT_HCI_QUIRK_NO_FLOW_CONTROL` | 控制器声明支持控制器到主机的流量控制命令（Controller to Host Flow Control Commands），但实际不接受这些命令。主机将此特性视为不受支持。 |

<a id="ga4baab0790149536873e5d9e0cb14359f"></a>

### `bt_hci_can_close()`

```c
bool bt_hci_can_close ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

检查 HCI 传输通道（HCI Transport）是否可以关闭。

关闭传输通道是可选驱动操作（Optional Driver Operation）。此接口预先告知使用者 bt_hci_close() 能否工作，例如在执行只有随后可关闭通道才有意义的操作之前进行检查。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 驱动支持关闭传输通道（Transport）。 |
| `false` | 驱动不支持关闭传输通道（Transport）。 |

<a id="gad187f0aff959a4756b281aa33d1b4394"></a>

### `bt_hci_close()`

```c
int bt_hci_close ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

关闭 HCI 传输通道（HCI Transport）。

关闭 HCI 传输通道（Transport）。成功时，必须等通道已关闭才能返回：驱动此后不再调用 recv 回调，且通道可通过 bt_hci_open() 再次打开。失败时通道仍然打开，可继续照常使用。

不得在 bt_hci_send()、本函数的另一调用或 bt_hci_open() 正在执行时调用；执行期间也不得调用 bt_hci_send()。不得从 recv 回调内调用，以允许驱动停止用于交付数据的线程。函数可能阻塞，在线程上下文（Thread Context）调用。

传输通道必须已打开，参见 bt_hci_send()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 驱动不支持关闭传输通道（Transport）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 POSIX 错误码。

<a id="gaf2f4e86132f321c6c7f20965dd5c1f0d"></a>

### `bt_hci_get_public_addr()`

```c
const bt_addr_t * bt_hci_get_public_addr ( const struct device * dev)
```

```c
#include <zephyr/drivers/bluetooth.h>
```

获取驱动应配置的公共身份地址（Public Identity Address）。

返回 bt_hci_set_public_addr() 存储的地址，供驱动在打开传输通道时写入控制器。本函数不查询控制器。

“无地址”使用 BT_ADDR_ANY，而不是名称容易令人误解的 BT_ADDR_NONE。BT_ADDR_ANY 是 BT_ADDR_LE_ANY 的地址部分，主机用后者标记没有地址的身份。没有公共身份时，setup() 操作也通过 bt_hci_setup_params::public_addr 收到该值，因此无论以哪种方式取得地址，驱动只需做同一种检查。它还是全零地址，因此从未写入的驱动数据已表示“无地址”。本函数不会失败；驱动在使用返回地址前，应通过 bt_addr_eq() 将其与 BT_ADDR_ANY 比较。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_HCI_SET_PUBLIC_ADDR` 时可用。

**返回（Returns）**：返回值（Returns）：要配置的地址，永不为 NULL，在对此设备下次调用 bt_hci_set_public_addr() 之前有效。未设置公共地址或地址已清除时，与 BT_ADDR_ANY 比较相等。

<a id="gac744c98801cea5afd13d6774154e71c8"></a>

### `bt_hci_open()`

```c
int bt_hci_open ( const struct device * dev, bt_hci_recv_t recv )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

打开 HCI 传输通道（HCI Transport）。

打开 HCI 传输通道供操作使用。必须等到通道可用，即可以安全调用 send() 处理函数时才返回。函数可能阻塞，在线程上下文（Thread Context）调用。

失败时传输通道处于关闭状态：驱动已停止本次调用启动的操作，不再调用 recv 回调，也不会为其调用 bt_hci_close()。唯一例外是 -EALREADY：通道已经打开时，不调用驱动就返回该值，并保持通道打开。

通过 bt_hci_close() 关闭的传输通道可以再次打开。不得在本函数另一调用或 bt_hci_close() 正在执行时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |
| `recv` | HCI 驱动通过此回调向主机交付来自控制器的数据。回调预期在线程上下文（Thread Context）调用，且可能在 bt_hci_open() 返回前就被调用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | HCI 传输通道已经打开。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 POSIX 错误码。

<a id="ga407beb20238b8fe6fdbd4ef199eb1f6c"></a>

### `bt_hci_recv()`

```c
void bt_hci_recv ( const struct device * dev, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

从驱动交付 HCI 数据包（HCI Packet）。

与 bt_hci_recv_err 相同，但会在内部处理错误情况，并始终消费缓冲区引用（Buffer Reference）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |
| `buf` | 包含从控制器收到的数据的缓冲区。 |

<a id="gaad2dc7f911913468a1440fad91cb3d62"></a>

### `bt_hci_recv_err()`

```c
int bt_hci_recv_err ( const struct device * dev, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

从驱动交付 HCI 数据包（HCI Packet）。

HCI 驱动调用此函数，把从控制器收到的数据交付主机。缓冲区包含原始 HCI 数据包，包括按 H:4 格式编码的数据包类型前缀（Packet Type Prefix）。

返回 0，即成功时，buf 的引用转移给高层，例如主机协议栈。发生错误时，调用方 HCI 驱动仍拥有此引用，并负责最终调用 net_buf_unref。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |
| `buf` | 包含从控制器收到的数据的缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTCONN` | HCI 传输通道未打开。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 POSIX 错误码。

<a id="ga64079b6f03479561c1c7d09b3af81ede"></a>

### `bt_hci_send()`

```c
int bt_hci_send ( const struct device * dev, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

向控制器（Controller）发送 HCI 缓冲区。

向控制器发送 HCI 数据包。数据包类型按 H:4，即 UART 传输编码（UART Transport Encoding），作为实际载荷之前的前缀。因此原生使用 H:4 编码的 HCI 驱动无需额外处理数据包类型。

返回 0，即成功时，buf 的引用转移给 HCI 驱动。发生错误时，调用方仍拥有此引用，并负责最终调用 net_buf_unref。

传输通道必须已打开：仅可在 bt_hci_open() 成功返回后调用，不得在 bt_hci_close() 正在执行或已成功关闭之后调用。没有用于查询此状态的接口；传输通道的唯一使用者应从自身调用得知状态。对未打开的通道调用属于调用方错误，结果未定义，驱动不必检测。也不得在本函数另一调用正在执行时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |
| `buf` | 包含待发送给控制器的数据的缓冲区。 |

**说明（Note）**：注意（Note）：此函数只能从协作式线程（Cooperative Thread）调用。

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 POSIX 错误码。

<a id="ga9df830679cdec440f96e37b608c7fdf7"></a>

### `bt_hci_set_public_addr()`

```c
void bt_hci_set_public_addr ( const struct device * dev, const bt_addr_t * addr )
```

```c
#include <zephyr/drivers/bluetooth.h>
```

设置控制器的公共身份地址（Public Identity Address）。

存储驱动应配置到控制器中的公共地址（Public Address）。

应用通过 bt_id_create() 创建公共身份（Public Identity）后，蓝牙主机在 bt_hci_open() 之前调用此函数。仅包含控制器的应用也可在打开传输通道前调用。

驱动通过 bt_hci_get_public_addr() 读取地址，并在打开传输通道时或在 setup() 实现中应用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备（Device） |
| `addr` | 公共地址（Public Address）；传 BT_ADDR_ANY 清除先前设置的地址。BT_ADDR_NONE 不会清除地址，参见 bt_hci_get_public_addr()。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_HCI_SET_PUBLIC_ADDR` 时可用。

<a id="ga45ce7bf5fe86f5fff3d8838d247b1d47"></a>

### `bt_hci_setup()`

```c
int bt_hci_setup ( const struct device * dev, struct bt_hci_setup_params * params )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/bluetooth.h>
```

HCI 厂商专有设置（Vendor-specific Setup）。

在蓝牙主机执行复位序列（Reset Sequence）之前，执行厂商专有命令序列初始化蓝牙控制器。通常紧接 bt_hci_open() 调用。

**说明（Note）**：注意：必须选择 CONFIG_BT_HCI_SETUP，才能使用此字段。

**已弃用（Deprecated）**：已弃用（Deprecated）：驱动在 open() 内通过自己的传输通道执行厂商专有初始化。参见 4.5 迁移指南（Migration Guide）。

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负 POSIX 错误码。


## 5.8\_原页交叉引用（Cross References）

- [蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。](../api_connection_topic_reference/P003_蓝牙H_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。.md)
- [蓝牙 HCI 驱动后端 API](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md)
- [蓝牙HCI锁步命令（Lockstep Command）的辅助接口。](../api_radio_permission_topic_reference/P003_蓝牙HCI锁步命令（Lockstep Command）的辅助接口。.md)
- [bluetooth.h](../api_file_audio_gateway_reference/P003_zephyr__drivers__bluetooth.h_文件参考.md)
- [bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)
- [bt_hci_driver_config](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hci_recv_t](../api_vector_pipeline_topic_reference/P003_蓝牙 HCI 驱动后端 API.md#ga79b12569871b2b6c8420c245e9505aed)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [DT_ENUM_IDX_OR](../dt_property_reference/P001_设备树属性读取宏.md#gac3616e3aa1a025235032786de8d31576)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_STRING_UPPER_TOKEN_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga73105b3402fbd6f82274a8b4a2ca6b35)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_FOREACH_PROP_ELEM_SEP](../dt_foreach_reference/P001_设备树遍历宏.md#ga72d0b6859b4fc61cde518aee118d9ed8)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [BT_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40ddc9769e38b7537bbb4e8002de592a)
- [BT_ADDR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gacb24d83ded350176fc96dfc0f5dde6be)
- [BT_ADDR_LE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga17e9efacd50c682b2f709c217e920d48)
- [bt_hci_setup_params::public_addr](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md#a6aea62826eeab39e6af40f9005548f3f)
- [bt_addr_eq()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadecf8fe8e183a11a4ff569bc0d673ec1)
- [CONFIG_BT_HCI_SET_PUBLIC_ADDR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SET_PUBLIC_ADDR)
- [send()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [bt_id_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae11eb8ad254418c38a0e8689df25a159)
- [CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)
- [Deprecated](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000004)
- [open()](../api_file_reference/P112_zephyr__posix__fcntl.h_文件参考.md#ac843f2e35e60c3bbf1da47d84306f29b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__hci__api_html_gaa9e7164af99dba0d6e8d409d79249e65"></a>
<a id="agroup__devicetree-generic-prop_html_gac3616e3aa1a025235032786de8d31576"></a>
<a id="agroup__bt__hci__api_html_ga766eaafe5d88d9d1efa0b3f09a334fc8"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__bt__hci__api_html_ga73fc76e779a3dd45a680b09063471887"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__bt__hci__api_html_ga3c8d5a12ea0c52d0934ee57c213f1fbe"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__bt__hci__api_html_gaf66891071ade556e5906e71f0f0d2678"></a>
<a id="agroup__devicetree-generic-prop_html_ga73105b3402fbd6f82274a8b4a2ca6b35"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__bt__hci__api_html_ga5e61116282ab2555f1dcd93c2858157e"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-foreach_html_ga72d0b6859b4fc61cde518aee118d9ed8"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1"></a>
<a id="gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2"></a>
<a id="gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_BAP 广播源 API（Broadcast Source APIs）.md) · [返回大纲](大纲.md) · [下一章](P006_免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）.md)
