---
id: learning.zephyr-docs.api-file-system-device-reference.page-2
title: zephyr__bluetooth__services__ans.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ans_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_services\_\_ans.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ans_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga05cbfd7c2ea24b273ac7ddc87b7a322e"></a>

```c
#define BT_ANS_ERR_CMD_NOT_SUP 0xa0
```

相关声明：[BT_ANS_ERR_CMD_NOT_SUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga05cbfd7c2ea24b273ac7ddc87b7a322e)。

命令不受支持的错误码（command not supported error code）。

<a id="r_ga631fbf5ea057ce058d280565bd2afe1a"></a>

```c
#define BT_ANS_MAX_TEXT_STR_SIZE 18
```

相关声明：[BT_ANS_MAX_TEXT_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga631fbf5ea057ce058d280565bd2afe1a)。

警报通知服务（ANS）的最大文本字符串长度，单位为八位组（octets）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_gad25bb27a24ce597a574ed5f40378c259"></a>

```c
enum bt_ans_cat { BT_ANS_CAT_SIMPLE_ALERT , BT_ANS_CAT_EMAIL , BT_ANS_CAT_NEWS , BT_ANS_CAT_CALL , BT_ANS_CAT_MISSED_CALL , BT_ANS_CAT_SMS_MMS , BT_ANS_CAT_VOICE_MAIL , BT_ANS_CAT_SCHEDULE , BT_ANS_CAT_HIGH_PRI_ALERT , BT_ANS_CAT_INSTANT_MESSAGE }
```

相关声明：[bt_ans_cat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gad25bb27a24ce597a574ed5f40378c259)、[BT_ANS_CAT_SIMPLE_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2e20c55899c5a8328b9d16dae9a054a2)、[BT_ANS_CAT_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a73c69f707354c33b42f974aa359150ae)、[BT_ANS_CAT_NEWS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2f7bd18799ea02f7da301924434af9a3)、[BT_ANS_CAT_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a107526cabd50986ee00169790c7d5dc1)、[BT_ANS_CAT_MISSED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259aa57b53f99a1b498e6bf491bc9bf906e5)、[BT_ANS_CAT_SMS_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a1f506ac9612fd93be667a6a3c68bd0ae)、[BT_ANS_CAT_VOICE_MAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259aaba90c2c3f80e72eebb912c18d4bd5b9)、[BT_ANS_CAT_SCHEDULE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259ae4fc8a56cff201b9e99fbefc9f422fe7)、[BT_ANS_CAT_HIGH_PRI_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259ad14d2a7619607c973efd2253b97412b4)、[BT_ANS_CAT_INSTANT_MESSAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2a9634d82ddab3a1e230c13d48c91b86)。

ANS 类别标识符（Category ID）枚举。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gabef875dbfb676f2b2cd84f518d844631"></a>

```c
int bt_ans_set_new_alert_support_category (uint16_t mask)
```

相关声明：[bt_ans_set_new_alert_support_category](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gabef875dbfb676f2b2cd84f518d844631)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置对指定新警报类别（new alert category）的支持。

<a id="r_ga8bb3734efe19c4f15d3c070909ba1442"></a>

```c
int bt_ans_set_unread_support_category (uint16_t mask)
```

相关声明：[bt_ans_set_unread_support_category](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga8bb3734efe19c4f15d3c070909ba1442)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置对指定未读新警报类别（unread new alert category）的支持。

<a id="r_gaea0397ea43a9dc459bf571296ba376c0"></a>

```c
int bt_ans_notify_new_alert (struct bt_conn *conn, enum bt_ans_cat category, uint8_t num_new, const char *text)
```

相关声明：[bt_ans_notify_new_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gaea0397ea43a9dc459bf571296ba376c0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ans_cat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gad25bb27a24ce597a574ed5f40378c259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向远端设备发送新警报（new alert）。

<a id="r_gacaf562a77286729b9d2a0399fbdf5075"></a>

```c
int bt_ans_set_unread_count (struct bt_conn *conn, enum bt_ans_cat category, uint8_t unread)
```

相关声明：[bt_ans_set_unread_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gacaf562a77286729b9d2a0399fbdf5075)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ans_cat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gad25bb27a24ce597a574ed5f40378c259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置指定类别的未读总数。


## 2.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P008_ans.h_源码浏览.md)
- [BT_ANS_ERR_CMD_NOT_SUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga05cbfd7c2ea24b273ac7ddc87b7a322e)
- [BT_ANS_MAX_TEXT_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga631fbf5ea057ce058d280565bd2afe1a)
- [bt_ans_cat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gad25bb27a24ce597a574ed5f40378c259)
- [BT_ANS_CAT_SIMPLE_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2e20c55899c5a8328b9d16dae9a054a2)
- [BT_ANS_CAT_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a73c69f707354c33b42f974aa359150ae)
- [BT_ANS_CAT_NEWS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2f7bd18799ea02f7da301924434af9a3)
- [BT_ANS_CAT_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a107526cabd50986ee00169790c7d5dc1)
- [BT_ANS_CAT_MISSED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259aa57b53f99a1b498e6bf491bc9bf906e5)
- [BT_ANS_CAT_SMS_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a1f506ac9612fd93be667a6a3c68bd0ae)
- [BT_ANS_CAT_VOICE_MAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259aaba90c2c3f80e72eebb912c18d4bd5b9)
- [BT_ANS_CAT_SCHEDULE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259ae4fc8a56cff201b9e99fbefc9f422fe7)
- [BT_ANS_CAT_HIGH_PRI_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259ad14d2a7619607c973efd2253b97412b4)
- [BT_ANS_CAT_INSTANT_MESSAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ggad25bb27a24ce597a574ed5f40378c259a2a9634d82ddab3a1e230c13d48c91b86)
- [bt_ans_set_new_alert_support_category](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gabef875dbfb676f2b2cd84f518d844631)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_ans_set_unread_support_category](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga8bb3734efe19c4f15d3c070909ba1442)
- [bt_ans_notify_new_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gaea0397ea43a9dc459bf571296ba376c0)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ans_set_unread_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gacaf562a77286729b9d2a0399fbdf5075)

---

[上一章](P001_zephyr__dt-bindings__sensor__adxl345.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__firmware__scmi__base.h_文件参考.md)
