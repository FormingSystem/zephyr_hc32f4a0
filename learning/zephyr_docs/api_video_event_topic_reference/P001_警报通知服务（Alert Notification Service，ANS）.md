---
id: learning.zephyr-docs.api-video-event-topic-reference.page-1
title: 警报通知服务（Alert Notification Service，ANS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_警报通知服务（Alert Notification Service，ANS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

警报通知服务（Alert Notification Service，ANS）

<a id="details"></a>

告警通知服务（Alert Notification Service，ANS）。自 4.4 起提供，版本 0.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga05cbfd7c2ea24b273ac7ddc87b7a322e"></a>

```c
#define BT_ANS_ERR_CMD_NOT_SUP 0xa0
```

相关声明：[BT_ANS_ERR_CMD_NOT_SUP](#ga05cbfd7c2ea24b273ac7ddc87b7a322e)。

命令不受支持的错误码（command not supported error code）。

<a id="r_ga631fbf5ea057ce058d280565bd2afe1a"></a>

```c
#define BT_ANS_MAX_TEXT_STR_SIZE 18
```

相关声明：[BT_ANS_MAX_TEXT_STR_SIZE](#ga631fbf5ea057ce058d280565bd2afe1a)。

警报通知服务（ANS）的最大文本字符串长度，单位为八位组（octets）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_gad25bb27a24ce597a574ed5f40378c259"></a>

```c
enum bt_ans_cat { BT_ANS_CAT_SIMPLE_ALERT , BT_ANS_CAT_EMAIL , BT_ANS_CAT_NEWS , BT_ANS_CAT_CALL , BT_ANS_CAT_MISSED_CALL , BT_ANS_CAT_SMS_MMS , BT_ANS_CAT_VOICE_MAIL , BT_ANS_CAT_SCHEDULE , BT_ANS_CAT_HIGH_PRI_ALERT , BT_ANS_CAT_INSTANT_MESSAGE }
```

相关声明：[bt_ans_cat](#gad25bb27a24ce597a574ed5f40378c259)、[BT_ANS_CAT_SIMPLE_ALERT](#ggad25bb27a24ce597a574ed5f40378c259a2e20c55899c5a8328b9d16dae9a054a2)、[BT_ANS_CAT_EMAIL](#ggad25bb27a24ce597a574ed5f40378c259a73c69f707354c33b42f974aa359150ae)、[BT_ANS_CAT_NEWS](#ggad25bb27a24ce597a574ed5f40378c259a2f7bd18799ea02f7da301924434af9a3)、[BT_ANS_CAT_CALL](#ggad25bb27a24ce597a574ed5f40378c259a107526cabd50986ee00169790c7d5dc1)、[BT_ANS_CAT_MISSED_CALL](#ggad25bb27a24ce597a574ed5f40378c259aa57b53f99a1b498e6bf491bc9bf906e5)、[BT_ANS_CAT_SMS_MMS](#ggad25bb27a24ce597a574ed5f40378c259a1f506ac9612fd93be667a6a3c68bd0ae)、[BT_ANS_CAT_VOICE_MAIL](#ggad25bb27a24ce597a574ed5f40378c259aaba90c2c3f80e72eebb912c18d4bd5b9)、[BT_ANS_CAT_SCHEDULE](#ggad25bb27a24ce597a574ed5f40378c259ae4fc8a56cff201b9e99fbefc9f422fe7)、[BT_ANS_CAT_HIGH_PRI_ALERT](#ggad25bb27a24ce597a574ed5f40378c259ad14d2a7619607c973efd2253b97412b4)、[BT_ANS_CAT_INSTANT_MESSAGE](#ggad25bb27a24ce597a574ed5f40378c259a2a9634d82ddab3a1e230c13d48c91b86)。

ANS 类别标识符（Category ID）枚举。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gabef875dbfb676f2b2cd84f518d844631"></a>

```c
int bt_ans_set_new_alert_support_category (uint16_t mask)
```

相关声明：[bt_ans_set_new_alert_support_category](#gabef875dbfb676f2b2cd84f518d844631)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置对指定新警报类别（new alert category）的支持。

<a id="r_ga8bb3734efe19c4f15d3c070909ba1442"></a>

```c
int bt_ans_set_unread_support_category (uint16_t mask)
```

相关声明：[bt_ans_set_unread_support_category](#ga8bb3734efe19c4f15d3c070909ba1442)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置对指定未读新警报类别（unread new alert category）的支持。

<a id="r_gaea0397ea43a9dc459bf571296ba376c0"></a>

```c
int bt_ans_notify_new_alert (struct bt_conn *conn, enum bt_ans_cat category, uint8_t num_new, const char *text)
```

相关声明：[bt_ans_notify_new_alert](#gaea0397ea43a9dc459bf571296ba376c0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ans_cat](#gad25bb27a24ce597a574ed5f40378c259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向远端设备发送新警报（new alert）。

<a id="r_gacaf562a77286729b9d2a0399fbdf5075"></a>

```c
int bt_ans_set_unread_count (struct bt_conn *conn, enum bt_ans_cat category, uint8_t unread)
```

相关声明：[bt_ans_set_unread_count](#gacaf562a77286729b9d2a0399fbdf5075)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ans_cat](#gad25bb27a24ce597a574ed5f40378c259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置指定类别的未读总数。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga05cbfd7c2ea24b273ac7ddc87b7a322e"></a>

### `BT_ANS_ERR_CMD_NOT_SUP`

```c
#define BT_ANS_ERR_CMD_NOT_SUP 0xa0
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

命令不受支持的错误码（command not supported error code）。

<a id="ga631fbf5ea057ce058d280565bd2afe1a"></a>

### `BT_ANS_MAX_TEXT_STR_SIZE`

```c
#define BT_ANS_MAX_TEXT_STR_SIZE 18
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

警报通知服务（ANS）的最大文本字符串长度，单位为八位组（octets）。

保存到新告警（New Alert）中的字符串最大大小，单位为字节（Octets）。超过最大长度的文本会被截断。

参见 [GATT 规范补充文档（GATT Specification Supplement）](https://btprodspecificationrefs.blob.core.windows.net/gatt-specification-supplement/GATT_Specification_Supplement.pdf) 第 3.165 节。

<a id="gad25bb27a24ce597a574ed5f40378c259"></a>

### `bt_ans_cat`

```c
enum bt_ans_cat
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

ANS 类别标识符（Category ID）枚举。

表示是否支持该类别（Category）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ANS_CAT_SIMPLE_ALERT` | 简单告警（Simple Alerts），即一般通知。 |
| `BT_ANS_CAT_EMAIL` | 电子邮件消息（Email Messages）。 |
| `BT_ANS_CAT_NEWS` | 新闻更新（News Updates）。 |
| `BT_ANS_CAT_CALL` | 来电告警（Incoming Call Alerts）。 |
| `BT_ANS_CAT_MISSED_CALL` | 未接来电告警（Missed Call Alerts）。 |
| `BT_ANS_CAT_SMS_MMS` | 短信／彩信消息（SMS/MMS Text Messages）。 |
| `BT_ANS_CAT_VOICE_MAIL` | 语音邮件通知（Voicemail Notifications）。 |
| `BT_ANS_CAT_SCHEDULE` | 日历或日程告警（Calendar or Schedule Alerts）。 |
| `BT_ANS_CAT_HIGH_PRI_ALERT` | 高优先级告警（High-priority Alerts）。 |
| `BT_ANS_CAT_INSTANT_MESSAGE` | 即时通信告警（Instant Messaging Alerts）。 |

<a id="gaea0397ea43a9dc459bf571296ba376c0"></a>

### `bt_ans_notify_new_alert()`

```c
int bt_ans_notify_new_alert ( struct bt_conn * conn, enum bt_ans_cat category, uint8_t num_new, const char * text )
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

向远端设备发送新警报（new alert）。

若已启用通知（Notifications），新告警将发送给远端设备。每个类别都会保存此函数最近一次调用的数据，以便通过 ANS 控制点（Control Point）请求立即重发时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要向其发送告警的连接对象（Connection Object）。 |
| `category` | 此通知对应的类别（Category）。 |
| `num_new` | 自上一次告警以来的新告警数量（Number of New Alerts）。 |
| `text` | 以空字符结尾的告警简述文本（Null-terminated Text）。 |

**说明（Note）**：注意：此函数以 `K_FOREVER` 等待互斥锁（Mutex），确保通知结构体的更新具有原子性（Atomic Updates）。为避免死锁，不要在蓝牙接收（BT RX）线程或系统工作队列（System Workqueue）线程中调用。

**返回（Returns）**：返回值：成功返回 0，失败返回负错误码。

<a id="gabef875dbfb676f2b2cd84f518d844631"></a>

### `bt_ans_set_new_alert_support_category()`

```c
int bt_ans_set_new_alert_support_category ( uint16_t mask)
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

设置对指定新警报类别（new alert category）的支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mask` | 受支持类别的位掩码（Category Bitmask）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回负错误码。

<a id="gacaf562a77286729b9d2a0399fbdf5075"></a>

### `bt_ans_set_unread_count()`

```c
int bt_ans_set_unread_count ( struct bt_conn * conn, enum bt_ans_cat category, uint8_t unread )
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

设置指定类别的未读总数。

若已启用通知（Notifications），未读数量将发送给远端设备。每个类别都会保存此函数最近一次调用的数据，以便通过 ANS 控制点（Control Point）请求立即重发时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要向其发送告警的连接对象（Connection Object）。 |
| `category` | 此未读数量对应的类别（Category）。 |
| `unread` | 未读告警总数（Total Number of Unread Alerts）。 |

**说明（Note）**：注意：此函数以 `K_FOREVER` 等待互斥锁（Mutex），确保通知结构体的更新具有原子性（Atomic Updates）。为避免死锁，不要在蓝牙接收（BT RX）线程或系统工作队列（System Workqueue）线程中调用。

**返回（Returns）**：返回值：成功返回 0，失败返回负错误码。

<a id="ga8bb3734efe19c4f15d3c070909ba1442"></a>

### `bt_ans_set_unread_support_category()`

```c
int bt_ans_set_unread_support_category ( uint16_t mask)
```

```c
#include <zephyr/bluetooth/services/ans.h>
```

设置对指定未读新警报类别（unread new alert category）的支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mask` | 受支持类别的位掩码（Category Bitmask）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回负错误码。


## 1.5\_原页交叉引用（Cross References）

- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/services/ans.h](../api_file_system_device_reference/P002_zephyr__bluetooth__services__ans.h_文件参考.md)
- [https://btprodspecificationrefs.blob.core.windows.net/gatt-specification-supplement/GATT_Specification_Supplement.pdf](https://btprodspecificationrefs.blob.core.windows.net/gatt-specification-supplement/GATT_Specification_Supplement.pdf)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a2e20c55899c5a8328b9d16dae9a054a2"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a73c69f707354c33b42f974aa359150ae"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a2f7bd18799ea02f7da301924434af9a3"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a107526cabd50986ee00169790c7d5dc1"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259aa57b53f99a1b498e6bf491bc9bf906e5"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a1f506ac9612fd93be667a6a3c68bd0ae"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259aaba90c2c3f80e72eebb912c18d4bd5b9"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259ae4fc8a56cff201b9e99fbefc9f422fe7"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259ad14d2a7619607c973efd2253b97412b4"></a>
<a id="ggad25bb27a24ce597a574ed5f40378c259a2a9634d82ddab3a1e230c13d48c91b86"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_BAP 单播服务器 API（Unicast Server APIs）.md)
