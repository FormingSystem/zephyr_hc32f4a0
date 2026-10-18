---
id: learning.zephyr-docs.api-file-interface-reference.page-58
title: zephyr__bluetooth__audio__tmap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_zephyr\_\_bluetooth\_\_audio\_\_tmap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙电话与媒体音频配置文件（TMAP）的头文件。

<a id="details"></a>

```c
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙电话与媒体音频配置文件（Bluetooth Telephony and Media Audio Profile，TMAP）头文件。版权（Copyright）2023 NXP；© 2024–2025 Nordic Semiconductor ASA。SPDX 许可证标识（License Identifier）：`Apache-2.0`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 58.1\_数据结构（Data Structures）

<a id="r_bt_5Ftmap_5Fcb"></a>

```c
struct bt_tmap_cb
```

相关声明：[bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)。

电话与媒体音频配置文件（TMAP）的回调结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 58.2\_枚举（Enumerations）

<a id="r_ga4ef8a550bb374a5f257860082e1411d4"></a>

```c
enum bt_tmap_role { BT_TMAP_ROLE_CG = (1UL << (0U)) , BT_TMAP_ROLE_CT = (1UL << (1U)) , BT_TMAP_ROLE_UMS = (1UL << (2U)) , BT_TMAP_ROLE_UMR = (1UL << (3U)) , BT_TMAP_ROLE_BMS = (1UL << (4U)) , BT_TMAP_ROLE_BMR = (1UL << (5U)) }
```

相关声明：[bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)、[BT_TMAP_ROLE_CG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)、[BT_TMAP_ROLE_CT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)、[BT_TMAP_ROLE_UMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)、[BT_TMAP_ROLE_UMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)、[BT_TMAP_ROLE_BMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)、[BT_TMAP_ROLE_BMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)。

TMAP 角色（TMAP Role）特征。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 58.3\_函数（Functions）

<a id="r_ga2c93d1bce7db000cef76c42e5cab48cb"></a>

```c
int bt_tmap_register (enum bt_tmap_role role)
```

相关声明：[bt_tmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga2c93d1bce7db000cef76c42e5cab48cb)、[bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)。

向数据库添加电话与媒体音频服务（TMAS）实例，并设置接收到的一个或多个 TMAP 角色。

<a id="r_gacb52c3e4c56f6b042398ac992628d521"></a>

```c
int bt_tmap_discover (struct bt_conn *conn, const struct bt_tmap_cb *tmap_cb)
```

相关声明：[bt_tmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gacb52c3e4c56f6b042398ac992628d521)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)。

以 TMAP 客户端身份执行服务发现（service discovery）。

<a id="r_ga0b51b305d5a5d87df9f4082951bd28a5"></a>

```c
void bt_tmap_set_role (enum bt_tmap_role role)
```

相关声明：[bt_tmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga0b51b305d5a5d87df9f4082951bd28a5)、[bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)。

动态设置一个或多个 TMAP 角色。


## 58.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P871_tmap.h_源码浏览.md)
- [bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)
- [bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)
- [BT_TMAP_ROLE_CG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)
- [BT_TMAP_ROLE_CT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)
- [BT_TMAP_ROLE_UMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)
- [BT_TMAP_ROLE_UMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)
- [BT_TMAP_ROLE_BMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)
- [BT_TMAP_ROLE_BMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)
- [bt_tmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga2c93d1bce7db000cef76c42e5cab48cb)
- [bt_tmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gacb52c3e4c56f6b042398ac992628d521)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_tmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga0b51b305d5a5d87df9f4082951bd28a5)

<a id="header-details"></a>

---

[上一章](P057_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store__settings.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P059_zephyr__drivers__sensor__tmp108.h_文件参考.md)
