---
id: learning.zephyr-docs.api-file-system-device-reference.page-46
title: zephyr__mgmt__mcumgr__transport__smp_bt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_smp\_bt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smp__bt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

mcumgr简单管理协议（SMP）的蓝牙传输。

<a id="details"></a>

```c
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/types.h>
```

查看此文件的源码。

mcumgr简单管理协议（SMP）的蓝牙传输。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 46.1\_宏定义（Macros）

<a id="r_ga35a151d8a3e9fb6f5e2e355c0c23f17c"></a>

```c
#define SMP_BT_SVC_UUID_VAL BT_UUID_128_ENCODE(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84)
```

相关声明：[SMP_BT_SVC_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga35a151d8a3e9fb6f5e2e355c0c23f17c)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

简单管理协议（SMP）服务的通用唯一标识符（UUID）值。

<a id="r_gafa04c341a4ed3b5a10c07d268266acc3"></a>

```c
#define SMP_BT_SVC_UUID BT_UUID_DECLARE_128(SMP_BT_SVC_UUID_VAL)
```

相关声明：[SMP_BT_SVC_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gafa04c341a4ed3b5a10c07d268266acc3)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[SMP_BT_SVC_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga35a151d8a3e9fb6f5e2e355c0c23f17c)。

SMP 服务 UUID。

<a id="r_ga3f75f06a2f437008ecbe87474971a4ec"></a>

```c
#define SMP_BT_CHR_UUID_VAL BT_UUID_128_ENCODE(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48)
```

相关声明：[SMP_BT_CHR_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga3f75f06a2f437008ecbe87474971a4ec)、[BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)。

SMP 特征（characteristic）的 UUID 值。

<a id="r_gaa42455942e31ddafc6174c5eca6f85ac"></a>

```c
#define SMP_BT_CHR_UUID BT_UUID_DECLARE_128(SMP_BT_CHR_UUID_VAL)
```

相关声明：[SMP_BT_CHR_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gaa42455942e31ddafc6174c5eca6f85ac)、[BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)、[SMP_BT_CHR_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga3f75f06a2f437008ecbe87474971a4ec)。

SMP 特征 UUID，同时用于请求和响应。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.2\_函数（Functions）

<a id="r_ga9ceedfe6c84f194ff103356a4c30331f"></a>

```c
int smp_bt_register (void)
```

相关声明：[smp_bt_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga9ceedfe6c84f194ff103356a4c30331f)。

注册 SMP 蓝牙服务。

<a id="r_gad19e1e1ba3ed59f13b5953bfda53ac15"></a>

```c
int smp_bt_unregister (void)
```

相关声明：[smp_bt_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gad19e1e1ba3ed59f13b5953bfda53ac15)。

注销 SMP 蓝牙服务。

<a id="r_ga8f52f0fda08b308dd7f1272b5ce5ba84"></a>

```c
int smp_bt_notify (struct bt_conn *conn, const void *data, uint16_t len)
```

相关声明：[smp_bt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga8f52f0fda08b308dd7f1272b5ce5ba84)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过指定蓝牙连接，以通知（notification）形式传输 SMP 命令／响应。


## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P794_smp_bt.h_源码浏览.md)
- [SMP_BT_SVC_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga35a151d8a3e9fb6f5e2e355c0c23f17c)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [SMP_BT_SVC_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gafa04c341a4ed3b5a10c07d268266acc3)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [SMP_BT_CHR_UUID_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga3f75f06a2f437008ecbe87474971a4ec)
- [SMP_BT_CHR_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gaa42455942e31ddafc6174c5eca6f85ac)
- [smp_bt_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga9ceedfe6c84f194ff103356a4c30331f)
- [smp_bt_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#gad19e1e1ba3ed59f13b5953bfda53ac15)
- [smp_bt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__bt.html#ga8f52f0fda08b308dd7f1272b5ce5ba84)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P045_zephyr__dt-bindings__clock__sf32lb-clocks-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__net__socket_select.h_文件参考.md)
