---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-200
title: bt_hci_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第200章\_bt\_hci\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：蓝牙 HCI 驱动操作。

```c
#include <zephyr/drivers/bluetooth.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：蓝牙 HCI 驱动操作。所有蓝牙 HCI 驱动都需要定义此驱动 API 结构体。它包含指向驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员则是可选项。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。这些操作为此 API 的所有使用者服务，蓝牙主机（Bluetooth Host）只是其中之一：仅含控制器的应用或测试也以相同方式执行打开、关闭和发送操作。因此，除 `setup()` 之外，这些操作不会使用主机的 HCI 命令 API（`bt_hci_cmd_alloc()`、`bt_hci_cmd_send()`、`bt_hci_cmd_send_sync()`）。缓冲区 API 的分配器、`bt_hci_recv()` 和 `bt_hci_recv_err()` 是驱动交付数据所用的接口，不在上述限制所指的范围内。如果驱动自身需要与控制器交换 HCI 命令，应通过自己的传输通道完成；为此提供了蓝牙 HCI 数据包辅助接口和蓝牙 HCI 锁步命令辅助接口（Lockstep Command Helper）。此类交换只能在 `open()` 和 `close()` 内进行，即传输通道尚未由其使用者掌控时。对于同一个设备，不能并发调用 `bt_hci_open()`、`bt_hci_close()` 和 `bt_hci_send()`：在其中任意一次调用进行期间，既不能调用其他函数，也不能再次调用同一个函数。传输通道只有一个使用者，即打开它的使用者；该使用者是蓝牙主机，或在未构建蓝牙主机时由应用担任。使用者应逐次调用，并遵守这三个函数各自说明的限制；驱动无需防御超出这些约定的其他行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 200.1\_数据成员（Data Fields）

<a id="r_a889d9a3553c4dd04595198dcfaf61d23"></a>

```c
bt_hci_api_open_t open
```

相关声明：[bt_hci_api_open_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gad45ae0f5e6f085f7a787257f1315df86)、[open](#a889d9a3553c4dd04595198dcfaf61d23)。

必需（REQ）：打开 HCI 传输通道（Transport）。

<a id="r_a03aecef9fea90013ffe2ca5df63a5b2f"></a>

```c
bt_hci_api_close_t close
```

相关声明：[bt_hci_api_close_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga93b2a7f403463aa7a1eaf94d7f17c01c)、[close](#a03aecef9fea90013ffe2ca5df63a5b2f)。

可选（OPT）：关闭 HCI 传输通道。

<a id="r_a3e87eb7758c2782f024cee1421ebd1fc"></a>

```c
bt_hci_api_send_t send
```

相关声明：[bt_hci_api_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga29f6af67c9ba45d0945c6de1424ea617)、[send](#a3e87eb7758c2782f024cee1421ebd1fc)。

必需（REQ）：向控制器发送 HCI 缓冲区。

<a id="r_acc2ac1f8ec536465eae4500fe972f3af"></a>

```c
bt_hci_api_setup_t setup
```

相关声明：[bt_hci_api_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gaa3205fd69fa1e7f00ea94a492fa9140f)、[setup](#acc2ac1f8ec536465eae4500fe972f3af)。

可选（OPT）：执行 HCI 厂商专用设置（Vendor-specific Setup）。

## 200.2\_详细说明（Detailed Documentation）

<a id="a03aecef9fea90013ffe2ca5df63a5b2f"></a>

### `close`

```c
bt_hci_api_close_t bt_hci_driver_api::close
```

可选（OPT）：关闭 HCI 传输通道。

<a id="a889d9a3553c4dd04595198dcfaf61d23"></a>

### `open`

```c
bt_hci_api_open_t bt_hci_driver_api::open
```

必需（REQ）：打开 HCI 传输通道（Transport）。

<a id="a3e87eb7758c2782f024cee1421ebd1fc"></a>

### `send`

```c
bt_hci_api_send_t bt_hci_driver_api::send
```

必需（REQ）：向控制器发送 HCI 缓冲区。

<a id="acc2ac1f8ec536465eae4500fe972f3af"></a>

### `setup`

```c
bt_hci_api_setup_t bt_hci_driver_api::setup
```

可选（OPT）：执行 HCI 厂商专用设置（Vendor-specific Setup）。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_HCI_SETUP` 时可用。

**已弃用（Deprecated）**：已弃用（Deprecated）：参见 `bt_hci_setup()`。

本结构体文档由以下文件生成：

- `zephyr/drivers/bluetooth.h`

## 200.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html)
- [bt_hci_api_open_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gad45ae0f5e6f085f7a787257f1315df86)
- [bt_hci_api_close_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga93b2a7f403463aa7a1eaf94d7f17c01c)
- [bt_hci_api_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga29f6af67c9ba45d0945c6de1424ea617)
- [bt_hci_api_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gaa3205fd69fa1e7f00ea94a492fa9140f)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [bt_hci_cmd_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)
- [bt_hci_cmd_send()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#af2eed9d93da45185aad9c2edc0001a54)
- [bt_hci_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8d306b5b56afdece1cadbbf0eecfe5a7)
- [缓冲区API（Buffer API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html)
- [bt_hci_recv()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)
- [bt_hci_recv_err()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)
- [蓝牙HCI数据包辅助接口（Packet Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html)
- [蓝牙HCI锁步命令辅助接口（Lockstep Command Helper）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html)
- [bt_hci_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)
- [bt_hci_close()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)
- [bt_hci_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)
- [CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000005)
- [bt_hci_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P199_bt_hci_cp_write_ssp_mode_结构体.md) · [返回大纲](大纲.md) · [下一章](P201_bt_hci_driver_config_结构体.md)
