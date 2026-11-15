---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-94
title: bt_ias_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ias__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_bt\_ias\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ias__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

即时警报服务（Immediate Alert Service）的回调结构。

```c
#include <zephyr/bluetooth/services/ias.h>
```

<a id="details"></a>

即时警报服务（Immediate Alert Service）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_ae0719b1f44f094ff0bbd3abea2bfdf15"></a>

```c
void(* no_alert )(void)
```

相关声明：[no_alert](#ae0719b1f44f094ff0bbd3abea2bfdf15)。

停止警报（alert）的回调函数。

<a id="r_aeffe89f9e5a9b87efbdd0af471de980d"></a>

```c
void(* mild_alert )(void)
```

相关声明：[mild_alert](#aeffe89f9e5a9b87efbdd0af471de980d)。

警报级别（alert level）值的回调函数。

<a id="r_ad2974bbd16e8d4425370a57f62601af5"></a>

```c
void(* high_alert )(void)
```

相关声明：[high_alert](#ad2974bbd16e8d4425370a57f62601af5)。

警报级别（alert level）值的回调函数。

## 94.2\_详细说明（Detailed Documentation）

<a id="ad2974bbd16e8d4425370a57f62601af5"></a>

### `high_alert`

```c
void(* bt_ias_cb::high_alert) (void)
```

警报级别（alert level）值的回调函数。

对端要求以最强方式发出警报时，调用此回调。

<a id="aeffe89f9e5a9b87efbdd0af471de980d"></a>

### `mild_alert`

```c
void(* bt_ias_cb::mild_alert) (void)
```

警报级别（alert level）值的回调函数。

对端要求发出警报时，调用此回调。

<a id="ae0719b1f44f094ff0bbd3abea2bfdf15"></a>

### `no_alert`

```c
void(* bt_ias_cb::no_alert) (void)
```

停止警报（alert）的回调函数。

对端要求禁用警报时，调用此回调。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ias.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ias.h](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_bt_hrs_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_bt_ias_client_cb_结构体.md)
