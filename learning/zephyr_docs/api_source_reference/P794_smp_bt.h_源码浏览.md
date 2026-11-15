---
id: learning.zephyr-docs.api-source-reference.page-794
title: smp_bt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第794章\_smp\_bt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h.html)。

## 794.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="agroup__mcumgr__transport__bt_html_ga8f52f0fda08b308dd7f1272b5ce5ba84"></a>
<a id="agroup__mcumgr__transport__bt_html_ga9ceedfe6c84f194ff103356a4c30331f"></a>
<a id="agroup__mcumgr__transport__bt_html_gad19e1e1ba3ed59f13b5953bfda53ac15"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_BT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_BT_H_


#include <zephyr/bluetooth/uuid.h>
#include <zephyr/types.h>
struct bt_conn;

#ifdef __cplusplus
extern "C" {
#endif

#define SMP_BT_SVC_UUID_VAL \
        BT_UUID_128_ENCODE(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84)

#define SMP_BT_SVC_UUID \
        BT_UUID_DECLARE_128(SMP_BT_SVC_UUID_VAL)

#define SMP_BT_CHR_UUID_VAL \
        BT_UUID_128_ENCODE(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48)

#define SMP_BT_CHR_UUID \
        BT_UUID_DECLARE_128(SMP_BT_CHR_UUID_VAL)

int smp_bt_register(void);

int smp_bt_unregister(void);

int smp_bt_notify(struct bt_conn *conn, const void *data, uint16_t len);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_BT_H_ */
```

## 794.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 83 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_BT_H_`。

## 794.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [smp_bt_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga9ceedfe6c84f194ff103356a4c30331f)
- [smp_bt_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gad19e1e1ba3ed59f13b5953bfda53ac15)
- [smp_bt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga8f52f0fda08b308dd7f1272b5ce5ba84)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P793_smartbond_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P795_smp_client.h_源码浏览.md)
