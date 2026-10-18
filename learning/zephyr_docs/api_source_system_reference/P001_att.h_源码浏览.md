---
id: learning.zephyr-docs.api-source-system-reference.page-1
title: att.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/att_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_att.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/att_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__att_html_ga2edca82fff038f16e6f7d09bc1db59a8"></a>
<a id="agroup__bt__att_html_ga3cabc05e8f5c0418ff02dd7122b7565e"></a>
<a id="agroup__bt__att_html_ga653a0fc8803d7deebb0be93c8cf7910a"></a>
<a id="agroup__bt__att_html_ga748194cbbd54a3336d3c788f08e3de99"></a>
<a id="agroup__bt__att_html_gac593a27ecf029f33f50f990b2947562c"></a>
<a id="agroup__bt__att_html_gad2305f28744276d97aefd26bdb79023c"></a>
<a id="agroup__bt__att_html_ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739"></a>
<a id="agroup__bt__att_html_ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4"></a>
<a id="agroup__bt__att_html_ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_ATT_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_ATT_H_


#include <stdint.h>
#include <stddef.h>

#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Error codes for Error response PDU
 *
 * Defined by The Bluetooth Core Specification, Version 5.4, Vol 3, Part F, Section 3.4.1.1
 */
#define BT_ATT_ERR_SUCCESS                      0x00
#define BT_ATT_ERR_INVALID_HANDLE               0x01
#define BT_ATT_ERR_READ_NOT_PERMITTED           0x02
#define BT_ATT_ERR_WRITE_NOT_PERMITTED          0x03
#define BT_ATT_ERR_INVALID_PDU                  0x04
#define BT_ATT_ERR_AUTHENTICATION               0x05
#define BT_ATT_ERR_NOT_SUPPORTED                0x06
#define BT_ATT_ERR_INVALID_OFFSET               0x07
#define BT_ATT_ERR_AUTHORIZATION                0x08
#define BT_ATT_ERR_PREPARE_QUEUE_FULL           0x09
#define BT_ATT_ERR_ATTRIBUTE_NOT_FOUND          0x0a
#define BT_ATT_ERR_ATTRIBUTE_NOT_LONG           0x0b
#define BT_ATT_ERR_ENCRYPTION_KEY_SIZE          0x0c
#define BT_ATT_ERR_INVALID_ATTRIBUTE_LEN        0x0d
#define BT_ATT_ERR_UNLIKELY                     0x0e
#define BT_ATT_ERR_INSUFFICIENT_ENCRYPTION      0x0f
#define BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE       0x10
#define BT_ATT_ERR_INSUFFICIENT_RESOURCES       0x11
#define BT_ATT_ERR_DB_OUT_OF_SYNC               0x12
#define BT_ATT_ERR_VALUE_NOT_ALLOWED            0x13

/* Common Profile Error Codes
 *
 * Defined by the Supplement to the Bluetooth Core Specification (CSS), v11, Part B, Section 1.2.
 */
#define BT_ATT_ERR_WRITE_REQ_REJECTED           0xfc
#define BT_ATT_ERR_CCC_IMPROPER_CONF            0xfd
#define BT_ATT_ERR_PROCEDURE_IN_PROGRESS        0xfe
#define BT_ATT_ERR_OUT_OF_RANGE                 0xff

/* Version 5.2, Vol 3, Part F, 3.2.9 defines maximum attribute length to 512 */
#define BT_ATT_MAX_ATTRIBUTE_LEN                512

/* Handle 0x0000 is reserved for future use */
#define BT_ATT_FIRST_ATTRIBUTE_HANDLE           0x0001
/* 0xffff is defined as the maximum, and thus last, valid attribute handle */
#define BT_ATT_LAST_ATTRIBUTE_HANDLE            0xffff

#if defined(CONFIG_BT_ATT_ERR_TO_STR)
const char *bt_att_err_to_str(uint8_t att_err);
#else
#include <zephyr/toolchain.h>

static inline const char *bt_att_err_to_str(uint8_t att_err)
{
        ARG_UNUSED(att_err);

        return "";
}
#endif

int bt_eatt_disconnect_one(struct bt_conn *conn);

int bt_eatt_reconfigure(struct bt_conn *conn, uint16_t mtu);

int bt_eatt_connect(struct bt_conn *conn, size_t num_channels);

size_t bt_eatt_count(struct bt_conn *conn);

enum bt_att_chan_opt {
        BT_ATT_CHAN_OPT_NONE = 0x0,
        BT_ATT_CHAN_OPT_UNENHANCED_ONLY = BIT(0),
        BT_ATT_CHAN_OPT_ENHANCED_ONLY = BIT(1),
};

int bt_att_get_max_notify_size(struct bt_conn *conn, enum bt_att_chan_opt chan_opt);

static inline int bt_att_get_max_indicate_size(struct bt_conn *conn, enum bt_att_chan_opt chan_opt)
{
        return bt_att_get_max_notify_size(conn, chan_opt);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_ATT_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

错误响应协议数据单元（Error Response PDU）的错误码（Error Codes）。

定义见《蓝牙核心规范》（Bluetooth Core Specification）5.4 版，第 3 卷 F 部分 3.4.1.1 节。

### 注释 3：原第 87 行

公共配置文件错误码（Common Profile Error Codes）。

定义见《蓝牙核心规范补充》（Supplement to the Bluetooth Core Specification，CSS）v11，B 部分 1.2 节。

### 注释 4：原第 100 行

5.2 版规范第 3 卷 F 部分 3.2.9 节将最大属性长度（Maximum Attribute Length）定义为 512。

### 注释 5：原第 103 行

句柄（Handle）`0x0000` 保留供未来使用。

### 注释 6：原第 105 行

`0xffff` 被定义为最大的有效属性句柄（Valid Attribute Handle），因此也是最后一个有效句柄。

### 注释 7：原第 265 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_ATT_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_att_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad2305f28744276d97aefd26bdb79023c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_eatt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga748194cbbd54a3336d3c788f08e3de99)
- [bt_eatt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga3cabc05e8f5c0418ff02dd7122b7565e)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [BT_ATT_CHAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)
- [BT_ATT_CHAN_OPT_UNENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_ATT_CHAN_OPT_ENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6)
- [bt_att_get_max_notify_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga653a0fc8803d7deebb0be93c8cf7910a)
- [bt_att_get_max_indicate_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2edca82fff038f16e6f7d09bc1db59a8)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_blob_io_flash.h_源码浏览.md)
