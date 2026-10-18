---
id: learning.zephyr-docs.api-file-supplement-reference.page-112
title: zephyr__drivers__sip_svc__sip_svc_agilex_mailbox.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__mailbox_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_zephyr\_\_drivers\_\_sip\_svc\_\_sip\_svc\_agilex\_mailbox.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__mailbox_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Intel SoC FPGA Agilex定制的安全设备管理器（SDM）邮箱通信协议处理程序。

查看此文件的源码。

<a id="details"></a>

Intel SoC FPGA Agilex 定制的安全设备管理器邮箱通信协议处理器（SDM Mailbox Communication Protocol Handler）。SDM 邮箱协议将嵌入 Arm SiP 服务的安全监视器调用协议（Arm SiP Services SMC Protocol），并通过 Arm SiP 服务与 SDM 收发。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 112.1\_宏定义（Macros）

<a id="r_aa56d732f7a2de4298a5dda992b1405de"></a>

```c
#define SIP_SVP_MB_MAX_WORD_SIZE 1024
```

相关声明：[SIP_SVP_MB_MAX_WORD_SIZE](#aa56d732f7a2de4298a5dda992b1405de)。

<a id="r_afccd6d2a8364c2273de2b31a448f5de3"></a>

```c
#define SIP_SVP_MB_HEADER_TRANS_ID_OFFSET 24
```

相关声明：[SIP_SVP_MB_HEADER_TRANS_ID_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3)。

<a id="r_a3532db48b21765fb2aa419522a794a94"></a>

```c
#define SIP_SVP_MB_HEADER_TRANS_ID_MASK 0xFF
```

相关声明：[SIP_SVP_MB_HEADER_TRANS_ID_MASK](#a3532db48b21765fb2aa419522a794a94)。

<a id="r_a6c24e3a782d918ebc001fca12ba8321a"></a>

```c
#define SIP_SVP_MB_HEADER_LENGTH_OFFSET 12
```

相关声明：[SIP_SVP_MB_HEADER_LENGTH_OFFSET](#a6c24e3a782d918ebc001fca12ba8321a)。

<a id="r_a66f47d95a199a02038c3d25f49e46b37"></a>

```c
#define SIP_SVP_MB_HEADER_LENGTH_MASK 0x7FF
```

相关声明：[SIP_SVP_MB_HEADER_LENGTH_MASK](#a66f47d95a199a02038c3d25f49e46b37)。

<a id="r_a6a29fa9f750979dce255ee2b56b0a953"></a>

```c
#define SIP_SVC_MB_HEADER_GET_CLIENT_ID(header)
```

相关声明：[SIP_SVC_MB_HEADER_GET_CLIENT_ID](#a6a29fa9f750979dce255ee2b56b0a953)。

<a id="r_abb0c7166d5c2ae113ba20315c0eb44ea"></a>

```c
#define SIP_SVC_MB_HEADER_GET_TRANS_ID(header)
```

相关声明：[SIP_SVC_MB_HEADER_GET_TRANS_ID](#abb0c7166d5c2ae113ba20315c0eb44ea)。

<a id="r_ad960abd8b2e9acb4d78da132d1481705"></a>

```c
#define SIP_SVC_MB_HEADER_SET_TRANS_ID(header, id)
```

相关声明：[SIP_SVC_MB_HEADER_SET_TRANS_ID](#ad960abd8b2e9acb4d78da132d1481705)。

<a id="r_af6e53a9a4c1e4cad501a541cf0a82e48"></a>

```c
#define SIP_SVC_MB_HEADER_GET_LENGTH(header)
```

相关声明：[SIP_SVC_MB_HEADER_GET_LENGTH](#af6e53a9a4c1e4cad501a541cf0a82e48)。

## 112.2\_详细说明（Detailed Documentation）

<a id="a6a29fa9f750979dce255ee2b56b0a953"></a>

### `SIP_SVC_MB_HEADER_GET_CLIENT_ID`

```c
#define SIP_SVC_MB_HEADER_GET_CLIENT_ID ( header)
```

展开值（Value）：

```c
((header) >> SIP_SVP_MB_HEADER_CLIENT_ID_OFFSET & \
        SIP_SVP_MB_HEADER_CLIENT_ID_MASK)
```

<a id="af6e53a9a4c1e4cad501a541cf0a82e48"></a>

### `SIP_SVC_MB_HEADER_GET_LENGTH`

```c
#define SIP_SVC_MB_HEADER_GET_LENGTH ( header)
```

展开值（Value）：

```c
((header) >> SIP_SVP_MB_HEADER_LENGTH_OFFSET & \
        SIP_SVP_MB_HEADER_LENGTH_MASK)
```

<a id="abb0c7166d5c2ae113ba20315c0eb44ea"></a>

### `SIP_SVC_MB_HEADER_GET_TRANS_ID`

```c
#define SIP_SVC_MB_HEADER_GET_TRANS_ID ( header)
```

展开值（Value）：

```c
((header) >> SIP_SVP_MB_HEADER_TRANS_ID_OFFSET & \
        SIP_SVP_MB_HEADER_TRANS_ID_MASK)
```

<a id="ad960abd8b2e9acb4d78da132d1481705"></a>

### `SIP_SVC_MB_HEADER_SET_TRANS_ID`

```c
#define SIP_SVC_MB_HEADER_SET_TRANS_ID ( header, id )
```

展开值（Value）：

```c
(header) &= ~(SIP_SVP_MB_HEADER_TRANS_ID_MASK << \
        SIP_SVP_MB_HEADER_TRANS_ID_OFFSET); \
(header) |= (((id) & SIP_SVP_MB_HEADER_TRANS_ID_MASK) << \
        SIP_SVP_MB_HEADER_TRANS_ID_OFFSET);
```

<a id="a66f47d95a199a02038c3d25f49e46b37"></a>

### `SIP_SVP_MB_HEADER_LENGTH_MASK`

```c
#define SIP_SVP_MB_HEADER_LENGTH_MASK 0x7FF
```

<a id="a6c24e3a782d918ebc001fca12ba8321a"></a>

### `SIP_SVP_MB_HEADER_LENGTH_OFFSET`

```c
#define SIP_SVP_MB_HEADER_LENGTH_OFFSET 12
```

<a id="a3532db48b21765fb2aa419522a794a94"></a>

### `SIP_SVP_MB_HEADER_TRANS_ID_MASK`

```c
#define SIP_SVP_MB_HEADER_TRANS_ID_MASK 0xFF
```

<a id="afccd6d2a8364c2273de2b31a448f5de3"></a>

### `SIP_SVP_MB_HEADER_TRANS_ID_OFFSET`

```c
#define SIP_SVP_MB_HEADER_TRANS_ID_OFFSET 24
```

<a id="aa56d732f7a2de4298a5dda992b1405de"></a>

### `SIP_SVP_MB_MAX_WORD_SIZE`

```c
#define SIP_SVP_MB_MAX_WORD_SIZE 1024
```


## 112.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P788_sip_svc_agilex_mailbox.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asip__svc__agilex__mailbox_8h_html_a66f47d95a199a02038c3d25f49e46b37"></a>
<a id="asip__svc__agilex__mailbox_8h_html_a6c24e3a782d918ebc001fca12ba8321a"></a>
<a id="asip__svc__agilex__mailbox_8h_html_a3532db48b21765fb2aa419522a794a94"></a>
<a id="asip__svc__agilex__mailbox_8h_html_afccd6d2a8364c2273de2b31a448f5de3"></a>

---

[上一章](P111_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt_callbacks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P113_zephyr__sip_svc__sip_svc_controller.h_文件参考.md)
