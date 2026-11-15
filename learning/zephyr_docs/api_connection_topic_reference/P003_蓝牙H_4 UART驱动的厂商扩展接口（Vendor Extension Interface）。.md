---
id: learning.zephyr-docs.api-connection-topic-reference.page-3
title: 蓝牙H_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙H\_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。

<a id="details"></a>

蓝牙 H:4 UART 驱动厂商扩展接口（vendor extension interface）。自 Zephyr 4.5 起提供；API 版本为 0.1.0。这些函数由 H:4 UART 驱动的厂商扩展实现；此外，任何开发板或扩展均可实现 `bt_hci_transport_setup()` 和 `bt_hci_transport_teardown()`。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.1\_函数（Functions）

<a id="r_ga4ac11c5a18b0891a04bb791e2f7c15bd"></a>

```c
int bt_h4_vnd_open (const struct device *dev, const struct device *uart, struct bt_hci_lockstep *ls)
```

相关声明：[bt_h4_vnd_open](#ga4ac11c5a18b0891a04bb791e2f7c15bd)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

在 H:4 传输通道（H:4 Transport）打开期间配置控制器（Controller）。

## 3.2\_详细说明（Detailed Documentation）

<a id="ga4ac11c5a18b0891a04bb791e2f7c15bd"></a>

### `bt_h4_vnd_open()`

```c
int bt_h4_vnd_open ( const struct device * dev, const struct device * uart, struct bt_hci_lockstep * ls )
```

```c
#include <zephyr/drivers/bluetooth/h4.h>
```

在 H:4 传输通道（H:4 Transport）打开期间配置控制器（Controller）。

由选择 `CONFIG_BT_H4_VND_OPEN` 的厂商扩展实现。H:4 驱动在其 `open()` 的最后调用此函数，此时驱动已经能够通过 UART 收发，并恢复了 `ls` 的初始命令额度（command allowance）。如果此函数返回失败，驱动就用该返回值使 `open()` 失败。

扩展在 `ls` 上使用 `bt_hci_lockstep_cmd_send_sync()` 发送命令；驱动将收到的每个数据包交给锁步辅助器（lockstep helper），使响应能够到达扩展。一条命令最多携带 `CONFIG_BT_BUF_CMD_TX_SIZE` 个参数字节，更长的命令会以 `-EMSGSIZE` 失败，因此需要发送长命令的扩展必须增大该选项，例如通过 Kconfig 默认值设置。扩展使用 `bt_hci_get_public_addr()` 读取要配置的公共地址（public address），并可在控制器已确认波特率变化后重新配置 UART。非 HCI 操作，例如通过原始 UART 上传固件映像，应放在 `bt_hci_transport_setup()` 中，该函数在驱动接管 UART 之前运行。

失败时，驱动撤销自身的 `open()` 操作；扩展也必须确保自身没有留下仍在运行、会干扰后续 `open()` 的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | HCI 设备，供 `bt_hci_get_public_addr()` 使用。 |
| `uart` | 传输层的 UART 设备，用于重新配置。 |
| `ls` | 传输层的锁步辅助器（lockstep helper）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 控制器已完成配置。 |

**返回（Returns）**：返回值：失败时返回负 `errno` 值，由 `bt_hci_open()` 返回给调用方。


## 3.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)
- [bt_hci_transport_setup()](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#add813c1343955a7bb95135eb0fbe9cd5)
- [bt_hci_transport_teardown()](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#ae29dbf165252ddf9085c7387706fd09c)
- [zephyr/drivers/bluetooth/h4.h](../api_file_supplement_reference/P041_zephyr__drivers__bluetooth__h4.h_文件参考.md)
- [CONFIG_BT_H4_VND_OPEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_H4_VND_OPEN)
- [open()](../api_file_reference/P112_zephyr__posix__fcntl.h_文件参考.md#ac843f2e35e60c3bbf1da47d84306f29b)
- [bt_hci_lockstep_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)
- [CONFIG_BT_BUF_CMD_TX_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BUF_CMD_TX_SIZE)
- [bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)
- [bt_hci_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_蓝牙内容控制标识符（Bluetooth Content Control Identifier）.md) · [返回大纲](大纲.md) · [下一章](P004_心率服务（Heart Rate Service，HRS）.md)
