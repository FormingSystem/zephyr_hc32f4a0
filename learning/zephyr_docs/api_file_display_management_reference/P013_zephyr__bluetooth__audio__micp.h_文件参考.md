---
id: learning.zephyr-docs.api-file-display-management-reference.page-13
title: zephyr__bluetooth__audio__micp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/micp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_bluetooth\_\_audio\_\_micp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙麦克风控制配置文件（Microphone Control Profile，MICP）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/bluetooth/audio/aics.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙麦克风控制配置文件（Microphone Control Profile，MICP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_bt_5Fmicp_5Fmic_5Fdev_5Fregister_5Fparam"></a>

```c
struct bt_micp_mic_dev_register_param
```

相关声明：[bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)。

麦克风控制服务（Microphone Control Service）的注册参数结构。

<a id="r_bt_5Fmicp_5Fincluded"></a>

```c
struct bt_micp_included
```

相关声明：[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

麦克风控制配置文件（Microphone Control Profile）包含的服务。

<a id="r_bt_5Fmicp_5Fmic_5Fdev_5Fcb"></a>

```c
struct bt_micp_mic_dev_cb
```

相关声明：[bt_micp_mic_dev_cb](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md)。

保存麦克风设备（Microphone Device）回调的结构。

<a id="r_bt_5Fmicp_5Fmic_5Fctlr_5Fcb"></a>

```c
struct bt_micp_mic_ctlr_cb
```

相关声明：[bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)。

保存麦克风控制器（Microphone Controller）回调的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_ga46cc0362c55cd9bdaf331de834a5fef5"></a>

```c
#define BT_MICP_MIC_DEV_AICS_CNT 0U
```

相关声明：[BT_MICP_MIC_DEV_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga46cc0362c55cd9bdaf331de834a5fef5)。

定义麦克风控制配置文件（Microphone Control Profile）中麦克风设备（Microphone Device）可具有的麦克风控制服务（Microphone Control Service）实例最大数量。

<a id="define-members-0"></a>

### 应用错误码（Application Error Codes）

<a id="r_ga31ce5cce4aa28662de82735241ee49d8"></a>

```c
#define BT_MICP_ERR_MUTE_DISABLED 0x80U
```

相关声明：[BT_MICP_ERR_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga31ce5cce4aa28662de82735241ee49d8)。

静音／取消静音命令（Mute/Unmute Commands）已禁用。

<a id="define-members-1"></a>

### 麦克风控制配置文件静音状态（Microphone Control Profile Mute States）

<a id="r_gaaf0327be66ebf4b0dd23282d4a46aa54"></a>

```c
#define BT_MICP_MUTE_UNMUTED 0x00U
```

相关声明：[BT_MICP_MUTE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#gaaf0327be66ebf4b0dd23282d4a46aa54)。

麦克风处于非静音状态（Unmuted）。

<a id="r_ga5718e29fefc336fbee1875aa5b81f233"></a>

```c
#define BT_MICP_MUTE_MUTED 0x01U
```

相关声明：[BT_MICP_MUTE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5718e29fefc336fbee1875aa5b81f233)。

麦克风处于静音状态（Muted）。

<a id="r_gafc7ed719d471ca27aeb96aaa638c05cb"></a>

```c
#define BT_MICP_MUTE_DISABLED 0x02U
```

相关声明：[BT_MICP_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#gafc7ed719d471ca27aeb96aaa638c05cb)。

麦克风状态为禁用（Disabled），无法静音或取消静音。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.3\_函数（Functions）

<a id="r_ga5dee6c7a1115bffbea39ba0575f369fc"></a>

```c
int bt_micp_mic_dev_register (struct bt_micp_mic_dev_register_param *param)
```

相关声明：[bt_micp_mic_dev_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5dee6c7a1115bffbea39ba0575f369fc)、[bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)。

初始化麦克风控制配置文件（Microphone Control Profile）的麦克风设备（Microphone Device）。

<a id="r_ga0541a36655024d9eadcff2d3e0c877f6"></a>

```c
int bt_micp_mic_dev_included_get (struct bt_micp_included *included)
```

相关声明：[bt_micp_mic_dev_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga0541a36655024d9eadcff2d3e0c877f6)、[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

获取麦克风设备的包含服务（Included Services）。

<a id="r_ga19ec08afa7784b80fce039fe84a4e33c"></a>

```c
int bt_micp_mic_dev_unmute (void)
```

相关声明：[bt_micp_mic_dev_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga19ec08afa7784b80fce039fe84a4e33c)。

取消麦克风设备的静音（Unmute）。

<a id="r_ga47f971c9c259e43504d586a55cf22c4e"></a>

```c
int bt_micp_mic_dev_mute (void)
```

相关声明：[bt_micp_mic_dev_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga47f971c9c259e43504d586a55cf22c4e)。

将麦克风设备静音（Mute）。

<a id="r_ga525c5d694f7d510d33f088e848733af6"></a>

```c
int bt_micp_mic_dev_mute_disable (void)
```

相关声明：[bt_micp_mic_dev_mute_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga525c5d694f7d510d33f088e848733af6)。

禁用麦克风设备的静音功能（Mute Functionality）。

<a id="r_ga263bf5cf51e4ef8d7e6986f0d8358da3"></a>

```c
int bt_micp_mic_dev_mute_get (void)
```

相关声明：[bt_micp_mic_dev_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga263bf5cf51e4ef8d7e6986f0d8358da3)。

读取麦克风设备的静音状态（Mute State）。

<a id="r_ga21e04942da32b15e75a0b0de3fb84167"></a>

```c
int bt_micp_mic_ctlr_included_get (struct bt_micp_mic_ctlr *mic_ctlr, struct bt_micp_included *included)
```

相关声明：[bt_micp_mic_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga21e04942da32b15e75a0b0de3fb84167)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)。

获取麦克风控制配置文件（Microphone Control Profile）的包含服务（Included Services）。

<a id="r_ga4b564e6b315a3861f1c3ba6098eabfe1"></a>

```c
int bt_micp_mic_ctlr_conn_get (const struct bt_micp_mic_ctlr *mic_ctlr, struct bt_conn **conn)
```

相关声明：[bt_micp_mic_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga4b564e6b315a3861f1c3ba6098eabfe1)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取麦克风控制端实例（Microphone Controller Instance）的连接指针。

<a id="r_ga863030e1b836c01a1be964bce0c72025"></a>

```c
struct bt_micp_mic_ctlr * bt_micp_mic_ctlr_get_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)、[bt_micp_mic_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga863030e1b836c01a1be964bce0c72025)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

从连接指针获取麦克风控制端（Microphone Controller）。

<a id="r_ga26187007ebf35ba2a5c57a076a3a7212"></a>

```c
int bt_micp_mic_ctlr_discover (struct bt_conn *conn, struct bt_micp_mic_ctlr **mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga26187007ebf35ba2a5c57a076a3a7212)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

发现麦克风控制服务（Microphone Control Service）。

<a id="r_ga6248c90bb94cd138c5bf9c68cffda4fe"></a>

```c
int bt_micp_mic_ctlr_unmute (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga6248c90bb94cd138c5bf9c68cffda4fe)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

取消远端麦克风设备的静音（Unmute）。

<a id="r_ga2d50f432703233c0f03cb139b6119faa"></a>

```c
int bt_micp_mic_ctlr_mute (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga2d50f432703233c0f03cb139b6119faa)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

将远端麦克风设备静音（Mute）。

<a id="r_ga5148e78053a3052d27677a1fa24e3847"></a>

```c
int bt_micp_mic_ctlr_mute_get (struct bt_micp_mic_ctlr *mic_ctlr)
```

相关声明：[bt_micp_mic_ctlr_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5148e78053a3052d27677a1fa24e3847)、[bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)。

读取远端麦克风设备的静音状态（Mute State）。

<a id="r_ga148ffcd0672adff9ccfaf35c522897c4"></a>

```c
int bt_micp_mic_ctlr_cb_register (struct bt_micp_mic_ctlr_cb *cb)
```

相关声明：[bt_micp_mic_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga148ffcd0672adff9ccfaf35c522897c4)、[bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)。

注册麦克风控制端（Microphone Controller）所用的回调。


## 13.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/audio/aics.h](../api_source_reference/P018_aics.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P524_micp.h_源码浏览.md)
- [bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)
- [bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)
- [bt_micp_mic_dev_cb](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md)
- [bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)
- [BT_MICP_MIC_DEV_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga46cc0362c55cd9bdaf331de834a5fef5)
- [BT_MICP_ERR_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga31ce5cce4aa28662de82735241ee49d8)
- [BT_MICP_MUTE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#gaaf0327be66ebf4b0dd23282d4a46aa54)
- [BT_MICP_MUTE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5718e29fefc336fbee1875aa5b81f233)
- [BT_MICP_MUTE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#gafc7ed719d471ca27aeb96aaa638c05cb)
- [bt_micp_mic_dev_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5dee6c7a1115bffbea39ba0575f369fc)
- [bt_micp_mic_dev_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga0541a36655024d9eadcff2d3e0c877f6)
- [bt_micp_mic_dev_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga19ec08afa7784b80fce039fe84a4e33c)
- [bt_micp_mic_dev_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga47f971c9c259e43504d586a55cf22c4e)
- [bt_micp_mic_dev_mute_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga525c5d694f7d510d33f088e848733af6)
- [bt_micp_mic_dev_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga263bf5cf51e4ef8d7e6986f0d8358da3)
- [bt_micp_mic_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga21e04942da32b15e75a0b0de3fb84167)
- [bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)
- [bt_micp_mic_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga4b564e6b315a3861f1c3ba6098eabfe1)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_micp_mic_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga863030e1b836c01a1be964bce0c72025)
- [bt_micp_mic_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga26187007ebf35ba2a5c57a076a3a7212)
- [bt_micp_mic_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga6248c90bb94cd138c5bf9c68cffda4fe)
- [bt_micp_mic_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga2d50f432703233c0f03cb139b6119faa)
- [bt_micp_mic_ctlr_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5148e78053a3052d27677a1fa24e3847)
- [bt_micp_mic_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga148ffcd0672adff9ccfaf35c522897c4)

<a id="header-details"></a>

---

[上一章](P012_zephyr__mgmt__mcumgr__transport__smp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__mpipe__mpipe_structure.h_文件参考.md)
