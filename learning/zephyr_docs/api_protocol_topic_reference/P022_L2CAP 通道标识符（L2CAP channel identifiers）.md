---
id: learning.zephyr-docs.api-protocol-topic-reference.page-22
title: L2CAP 通道标识符（L2CAP channel identifiers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__l2cap__cid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_L2CAP 通道标识符（L2CAP channel identifiers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__l2cap__cid.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

标准 L2CAP 通道标识符。

<a id="details"></a>

标准 L2CAP 通道标识符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_gacff77dc842b18b2d10c29183be72db77"></a>

```c
#define BT_L2CAP_CID_BR_SIG 0x0001
```

相关声明：[BT_L2CAP_CID_BR_SIG](#gacff77dc842b18b2d10c29183be72db77)。

蓝牙基本速率（BR）信令通道（signaling channel）。

<a id="r_gac463a009cf61bcb7cf23ba19885ea16d"></a>

```c
#define BT_L2CAP_CID_ATT 0x0004
```

相关声明：[BT_L2CAP_CID_ATT](#gac463a009cf61bcb7cf23ba19885ea16d)。

属性协议（Attribute Protocol，ATT）通道。

<a id="r_ga4d09da498948b233713f833900ee2d1f"></a>

```c
#define BT_L2CAP_CID_LE_SIG 0x0005
```

相关声明：[BT_L2CAP_CID_LE_SIG](#ga4d09da498948b233713f833900ee2d1f)。

蓝牙低功耗（LE）信令通道。

<a id="r_gae72ebddd803464009967c1f4e6683f25"></a>

```c
#define BT_L2CAP_CID_SMP 0x0006
```

相关声明：[BT_L2CAP_CID_SMP](#gae72ebddd803464009967c1f4e6683f25)。

安全管理协议（Security Manager Protocol，SMP）通道。

<a id="r_ga225fc18663e6a0c0e1c8f420ef0688e3"></a>

```c
#define BT_L2CAP_CID_BR_SMP 0x0007
```

相关声明：[BT_L2CAP_CID_BR_SMP](#ga225fc18663e6a0c0e1c8f420ef0688e3)。

BR 安全管理协议通道。

## 22.2\_详细说明（Detailed Documentation）

<a id="gac463a009cf61bcb7cf23ba19885ea16d"></a>

### `BT_L2CAP_CID_ATT`

```c
#define BT_L2CAP_CID_ATT 0x0004
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

属性协议（Attribute Protocol，ATT）通道。

<a id="gacff77dc842b18b2d10c29183be72db77"></a>

### `BT_L2CAP_CID_BR_SIG`

```c
#define BT_L2CAP_CID_BR_SIG 0x0001
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

蓝牙基本速率（BR）信令通道（signaling channel）。

<a id="ga225fc18663e6a0c0e1c8f420ef0688e3"></a>

### `BT_L2CAP_CID_BR_SMP`

```c
#define BT_L2CAP_CID_BR_SMP 0x0007
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

BR 安全管理协议通道。

<a id="ga4d09da498948b233713f833900ee2d1f"></a>

### `BT_L2CAP_CID_LE_SIG`

```c
#define BT_L2CAP_CID_LE_SIG 0x0005
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

蓝牙低功耗（LE）信令通道。

<a id="gae72ebddd803464009967c1f4e6683f25"></a>

### `BT_L2CAP_CID_SMP`

```c
#define BT_L2CAP_CID_SMP 0x0006
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

安全管理协议（Security Manager Protocol，SMP）通道。


## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P021_HX711 API主题.md) · [返回大纲](大纲.md) · [下一章](P023_轻量级M2M（LwM2M）的路径辅助宏。.md)
