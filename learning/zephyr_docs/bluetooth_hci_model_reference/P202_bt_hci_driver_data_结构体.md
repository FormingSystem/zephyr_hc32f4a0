---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-202
title: bt_hci_driver_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第202章\_bt\_hci\_driver\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 HCI 驱动通用数据（Common Driver Data）。

```c
#include <zephyr/drivers/bluetooth.h>
```

<a id="details"></a>

蓝牙 HCI 驱动通用数据（Common Driver Data）。此结构体由所有蓝牙 HCI 驱动共用，必须是驱动数据结构体的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 202.1\_数据成员（Data Fields）

<a id="r_a7213640520b14fc3368e1d7354370d93"></a>

```c
bt_hci_recv_t recv
```

相关声明：[bt_hci_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga79b12569871b2b6c8420c245e9505aed)、[recv](#a7213640520b14fc3368e1d7354370d93)。

驱动用于将从控制器收到的数据交付给主机的回调。

<a id="r_a60b09de82502158b7e09d6850d2c1ec3"></a>

```c
bt_addr_t public_addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[public_addr](#a60b09de82502158b7e09d6850d2c1ec3)。

要在控制器中配置的公共身份地址（Public Identity Address）。

## 202.2\_详细说明（Detailed Documentation）

<a id="a60b09de82502158b7e09d6850d2c1ec3"></a>

### `public_addr`

```c
bt_addr_t bt_hci_driver_data::public_addr
```

要在控制器中配置的公共身份地址（Public Identity Address）。

没有地址时为 `BT_ADDR_ANY`，这也是零初始化驱动数据的初始值；不是 `BT_ADDR_NONE`，参见 `bt_hci_get_public_addr()`。

使用 `bt_hci_set_public_addr()` 设置，使用 `bt_hci_get_public_addr()` 读取。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_HCI_SET_PUBLIC_ADDR` 时可用。

<a id="a7213640520b14fc3368e1d7354370d93"></a>

### `recv`

```c
bt_hci_recv_t bt_hci_driver_data::recv
```

驱动用于将从控制器收到的数据交付给主机的回调。

本结构体文档由以下文件生成：

- `zephyr/drivers/bluetooth.h`

## 202.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html)
- [bt_hci_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga79b12569871b2b6c8420c245e9505aed)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [BT_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40ddc9769e38b7537bbb4e8002de592a)
- [BT_ADDR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gacb24d83ded350176fc96dfc0f5dde6be)
- [bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)
- [bt_hci_set_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9df830679cdec440f96e37b608c7fdf7)
- [CONFIG_BT_HCI_SET_PUBLIC_ADDR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SET_PUBLIC_ADDR)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P201_bt_hci_driver_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P203_bt_hci_evt_auth_complete_结构体.md)
