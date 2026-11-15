---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-437
title: bt_hci_setup_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__setup__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第437章\_bt\_hci\_setup\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__setup__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

驱动 API 操作 `setup()` 的参数。

```c
#include <zephyr/drivers/bluetooth.h>
```

<a id="details"></a>

驱动 API 操作 `setup()` 的参数。已弃用（Deprecated）：此参数结构与该操作本身一并弃用，参见 `bt_hci_setup()`。驱动应改用 `bt_hci_get_public_addr()` 获取公共地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 437.1\_数据成员（Data Fields）

<a id="r_a6aea62826eeab39e6af40f9005548f3f"></a>

```c
bt_addr_t public_addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[public_addr](#a6aea62826eeab39e6af40f9005548f3f)。

要提供给控制器的公共身份地址（Public Identity Address）。

## 437.2\_详细说明（Detailed Documentation）

<a id="a6aea62826eeab39e6af40f9005548f3f"></a>

### `public_addr`

```c
bt_addr_t bt_hci_setup_params::public_addr
```

要提供给控制器的公共身份地址（Public Identity Address）。

当驱动选择 `CONFIG_BT_HCI_SET_PUBLIC_ADDR`，以表明它支持设置控制器公共地址时，使用此字段。如果应用尚未创建公共身份，则该值为 `BT_ADDR_ANY`。

本结构体文档由以下文件生成：

- `zephyr/drivers/bluetooth.h`

## 437.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000002)
- [bt_hci_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)
- [bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)
- [CONFIG_BT_HCI_SET_PUBLIC_ADDR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SET_PUBLIC_ADDR)
- [BT_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40ddc9769e38b7537bbb4e8002de592a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P436_bt_hci_sco_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P438_bt_hci_std_codec_info_结构体.md)
