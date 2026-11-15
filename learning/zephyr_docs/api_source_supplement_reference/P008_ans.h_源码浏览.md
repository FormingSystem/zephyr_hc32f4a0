---
id: learning.zephyr-docs.api-source-supplement-reference.page-8
title: ans.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ans_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ans.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ans_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ans_8h.html)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="agroup__bt__ans_html_ga8bb3734efe19c4f15d3c070909ba1442"></a>
<a id="agroup__bt__ans_html_gabef875dbfb676f2b2cd84f518d844631"></a>
<a id="agroup__bt__ans_html_gacaf562a77286729b9d2a0399fbdf5075"></a>
<a id="agroup__bt__ans_html_gad25bb27a24ce597a574ed5f40378c259"></a>
<a id="agroup__bt__ans_html_gaea0397ea43a9dc459bf571296ba376c0"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a107526cabd50986ee00169790c7d5dc1"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a1f506ac9612fd93be667a6a3c68bd0ae"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a2a9634d82ddab3a1e230c13d48c91b86"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a2e20c55899c5a8328b9d16dae9a054a2"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a2f7bd18799ea02f7da301924434af9a3"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259a73c69f707354c33b42f974aa359150ae"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259aa57b53f99a1b498e6bf491bc9bf906e5"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259aaba90c2c3f80e72eebb912c18d4bd5b9"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259ad14d2a7619607c973efd2253b97412b4"></a>
<a id="agroup__bt__ans_html_ggad25bb27a24ce597a574ed5f40378c259ae4fc8a56cff201b9e99fbefc9f422fe7"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>

```c
/*
 * Copyright (c) 2025 Sean Kyer
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ANS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ANS_H_


#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_ANS_ERR_CMD_NOT_SUP 0xa0

#define BT_ANS_MAX_TEXT_STR_SIZE 18

enum bt_ans_cat {
        BT_ANS_CAT_SIMPLE_ALERT,
        BT_ANS_CAT_EMAIL,
        BT_ANS_CAT_NEWS,
        BT_ANS_CAT_CALL,
        BT_ANS_CAT_MISSED_CALL,
        BT_ANS_CAT_SMS_MMS,
        BT_ANS_CAT_VOICE_MAIL,
        BT_ANS_CAT_SCHEDULE,
        BT_ANS_CAT_HIGH_PRI_ALERT,
        BT_ANS_CAT_INSTANT_MESSAGE,

        BT_ANS_CAT_NUM,

        /* 10–15 reserved for future use */
};

int bt_ans_set_new_alert_support_category(uint16_t mask);

int bt_ans_set_unread_support_category(uint16_t mask);

int bt_ans_notify_new_alert(struct bt_conn *conn, enum bt_ans_cat category, uint8_t num_new,
                            const char *text);

int bt_ans_set_unread_count(struct bt_conn *conn, enum bt_ans_cat category, uint8_t unread);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ANS_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Sean Kyer。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 65 行

10–15 保留供将来使用。

### 注释 3：原第 136 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ANS_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ans_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
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
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_ans_set_unread_support_category](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#ga8bb3734efe19c4f15d3c070909ba1442)
- [bt_ans_notify_new_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gaea0397ea43a9dc459bf571296ba376c0)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ans_set_unread_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html#gacaf562a77286729b9d2a0399fbdf5075)

---

[上一章](P007_ameba_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_cpu.h_源码浏览.md)
