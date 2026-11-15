---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-11
title: zephyr__drivers__sip_svc__sip_svc_proto.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_sip\_svc\_\_sip\_svc\_proto.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务提供者与客户端之间的Arm SiP服务通信协议（Communication Protocol）。

查看此文件的源码。

<a id="details"></a>

服务提供方与客户端之间的 Arm SiP 服务通信协议（Communication Protocol）。客户端通过 send 函数请求 SMC/HVC 服务时，须按 struct sip_svc_request 格式填写输入数据。服务按 struct sip_svc_response 格式填写 SMC/HVC 返回值，并通过回调（Callback）传递给客户端。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_sip_5Fsvc_5Frequest"></a>

```c
struct sip_svc_request
```

相关声明：[sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)。

SiP服务（SiP Service）通信协议的请求格式。

<a id="r_sip_5Fsvc_5Fresponse"></a>

```c
struct sip_svc_response
```

相关声明：[sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)。

SiP服务（SiP Services）通信协议的响应格式。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ad1cb9509a40e51809b13f1fccf0f35ba"></a>

```c
#define SIP_SVC_ID_INVALID 0xFFFFFFFF
```

相关声明：[SIP_SVC_ID_INVALID](#ad1cb9509a40e51809b13f1fccf0f35ba)。

无效的 ID 值（Invalid ID Value）。

<a id="r_a5544d9131eef67538c3a36bdfec5482e"></a>

```c
#define SIP_SVC_PROTO_VER 0x0
```

相关声明：[SIP_SVC_PROTO_VER](#a5544d9131eef67538c3a36bdfec5482e)。

头部格式（Header Format）。

<a id="r_a218d17af00117be8baf393e6b95cd9b2"></a>

```c
#define SIP_SVC_PROTO_HEADER_CODE_OFFSET 0
```

相关声明：[SIP_SVC_PROTO_HEADER_CODE_OFFSET](#a218d17af00117be8baf393e6b95cd9b2)。

<a id="r_aa8dbe689b3b375f72d049a89389ff591"></a>

```c
#define SIP_SVC_PROTO_HEADER_CODE_MASK 0xFFFF
```

相关声明：[SIP_SVC_PROTO_HEADER_CODE_MASK](#aa8dbe689b3b375f72d049a89389ff591)。

<a id="r_a4f147d26b354026e01225395e3f074ce"></a>

```c
#define SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET 16
```

相关声明：[SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET](#a4f147d26b354026e01225395e3f074ce)。

<a id="r_a2da7d9fd032cf43814b535f7b9ff9028"></a>

```c
#define SIP_SVC_PROTO_HEADER_TRANS_ID_MASK 0xFF
```

相关声明：[SIP_SVC_PROTO_HEADER_TRANS_ID_MASK](#a2da7d9fd032cf43814b535f7b9ff9028)。

<a id="r_a10ce84feaee4a6454c36dc3daf4f7722"></a>

```c
#define SIP_SVC_PROTO_HEADER_VER_OFFSET 30
```

相关声明：[SIP_SVC_PROTO_HEADER_VER_OFFSET](#a10ce84feaee4a6454c36dc3daf4f7722)。

<a id="r_a8ffae8b2e3adb78378308944fb38601e"></a>

```c
#define SIP_SVC_PROTO_HEADER_VER_MASK 0x3
```

相关声明：[SIP_SVC_PROTO_HEADER_VER_MASK](#a8ffae8b2e3adb78378308944fb38601e)。

<a id="r_a8ad11e26b133a65a94877930e74afa90"></a>

```c
#define SIP_SVC_PROTO_HEADER(code, trans_id)
```

相关声明：[SIP_SVC_PROTO_HEADER](#a8ad11e26b133a65a94877930e74afa90)。

<a id="r_a365877f6f62717cb3f271666fa392d8e"></a>

```c
#define SIP_SVC_PROTO_HEADER_GET_CODE(header)
```

相关声明：[SIP_SVC_PROTO_HEADER_GET_CODE](#a365877f6f62717cb3f271666fa392d8e)。

<a id="r_a4badc2fa72b4d5ae55c9b6503e3d2f41"></a>

```c
#define SIP_SVC_PROTO_HEADER_GET_TRANS_ID(header)
```

相关声明：[SIP_SVC_PROTO_HEADER_GET_TRANS_ID](#a4badc2fa72b4d5ae55c9b6503e3d2f41)。

<a id="r_a57124f787454b1253737bdde7ad04c6f"></a>

```c
#define SIP_SVC_PROTO_HEADER_SET_TRANS_ID(header, trans_id)
```

相关声明：[SIP_SVC_PROTO_HEADER_SET_TRANS_ID](#a57124f787454b1253737bdde7ad04c6f)。

<a id="r_a6ea30874bbe6393807ccc8c02038cc30"></a>

```c
#define SIP_SVC_PROTO_CMD_SYNC 0x0
```

相关声明：[SIP_SVC_PROTO_CMD_SYNC（同步命令）](#a6ea30874bbe6393807ccc8c02038cc30)。

请求头部中的 Arm SiP 服务命令码（Command Code）。

<a id="r_a8bc75a10006e42097f74edf990fa1f16"></a>

```c
#define SIP_SVC_PROTO_CMD_ASYNC 0x1
```

相关声明：[SIP_SVC_PROTO_CMD_ASYNC（异步命令）](#a8bc75a10006e42097f74edf990fa1f16)。

<a id="r_a8d7c4970ff149584080532c7bfa0cd51"></a>

```c
#define SIP_SVC_PROTO_CMD_MAX SIP_SVC_PROTO_CMD_ASYNC
```

相关声明：[SIP_SVC_PROTO_CMD_MAX](#a8d7c4970ff149584080532c7bfa0cd51)、[SIP_SVC_PROTO_CMD_ASYNC（异步命令）](#a8bc75a10006e42097f74edf990fa1f16)。

<a id="r_af4153e73a6024d7d4355e9373f10388b"></a>

```c
#define SIP_SVC_PROTO_STATUS_OK 0x0
```

相关声明：[SIP_SVC_PROTO_STATUS_OK（成功状态）](#af4153e73a6024d7d4355e9373f10388b)。

响应头部中的错误码（Error Code）。

<a id="r_a1c7567c532ab25d3d21ed76c655b9680"></a>

```c
#define SIP_SVC_PROTO_STATUS_UNKNOWN 0xFFFF
```

相关声明：[SIP_SVC_PROTO_STATUS_UNKNOWN（未知状态）](#a1c7567c532ab25d3d21ed76c655b9680)。

<a id="r_aeae6b273da4e3e91f0a6ee2558a7585f"></a>

```c
#define SIP_SVC_PROTO_STATUS_BUSY 0x1
```

相关声明：[SIP_SVC_PROTO_STATUS_BUSY（忙状态）](#aeae6b273da4e3e91f0a6ee2558a7585f)。

<a id="r_aa777087a721423e0e65cac4949813aaf"></a>

```c
#define SIP_SVC_PROTO_STATUS_REJECT 0x2
```

相关声明：[SIP_SVC_PROTO_STATUS_REJECT（拒绝状态）](#aa777087a721423e0e65cac4949813aaf)。

<a id="r_afba704d63c783fdd3d143045ca260706"></a>

```c
#define SIP_SVC_PROTO_STATUS_NO_RESPONSE 0x3
```

相关声明：[SIP_SVC_PROTO_STATUS_NO_RESPONSE（无响应状态）](#afba704d63c783fdd3d143045ca260706)。

<a id="r_a0d92a17202ff227476277500f539fd51"></a>

```c
#define SIP_SVC_PROTO_STATUS_ERROR 0x4
```

相关声明：[SIP_SVC_PROTO_STATUS_ERROR（错误状态）](#a0d92a17202ff227476277500f539fd51)。

## 11.3\_详细说明（Detailed Documentation）

<a id="ad1cb9509a40e51809b13f1fccf0f35ba"></a>

### `SIP_SVC_ID_INVALID`

```c
#define SIP_SVC_ID_INVALID 0xFFFFFFFF
```

无效的 ID 值（Invalid ID Value）。

<a id="a8bc75a10006e42097f74edf990fa1f16"></a>

### `SIP_SVC_PROTO_CMD_ASYNC`

```c
#define SIP_SVC_PROTO_CMD_ASYNC 0x1
```

<a id="a8d7c4970ff149584080532c7bfa0cd51"></a>

### `SIP_SVC_PROTO_CMD_MAX`

```c
#define SIP_SVC_PROTO_CMD_MAX SIP_SVC_PROTO_CMD_ASYNC
```

<a id="a6ea30874bbe6393807ccc8c02038cc30"></a>

### `SIP_SVC_PROTO_CMD_SYNC`

```c
#define SIP_SVC_PROTO_CMD_SYNC 0x0
```

请求头部中的 Arm SiP 服务命令码（Command Code）。

SIP_SVC_PROTO_CMD_SYNC（同步命令）

- 典型流程为同步请求（Synchronous Request）。服务期望 EL3/EL2 固件在 SMC/HVC 调用期间立即返回结果。

SIP_SVC_PROTO_CMD_ASYNC（异步命令）

- 异步请求（Asynchronous Request）。服务必须通过单独的 SMC/HVC 调用轮询响应。若请求需要在 EL3/EL2 中进行较长时间处理，则使用此方法。

<a id="a8ad11e26b133a65a94877930e74afa90"></a>

### `SIP_SVC_PROTO_HEADER`

```c
#define SIP_SVC_PROTO_HEADER ( code, trans_id )
```

展开值（Value）：

```c
((((code)&SIP_SVC_PROTO_HEADER_CODE_MASK) << SIP_SVC_PROTO_HEADER_CODE_OFFSET) |           \
 (((trans_id)&SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)                                          \
  << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET) |                                               \
 ((SIP_SVC_PROTO_VER & SIP_SVC_PROTO_HEADER_VER_MASK) << SIP_SVC_PROTO_HEADER_VER_OFFSET))
```

<a id="aa8dbe689b3b375f72d049a89389ff591"></a>

### `SIP_SVC_PROTO_HEADER_CODE_MASK`

```c
#define SIP_SVC_PROTO_HEADER_CODE_MASK 0xFFFF
```

<a id="a218d17af00117be8baf393e6b95cd9b2"></a>

### `SIP_SVC_PROTO_HEADER_CODE_OFFSET`

```c
#define SIP_SVC_PROTO_HEADER_CODE_OFFSET 0
```

<a id="a365877f6f62717cb3f271666fa392d8e"></a>

### `SIP_SVC_PROTO_HEADER_GET_CODE`

```c
#define SIP_SVC_PROTO_HEADER_GET_CODE ( header)
```

展开值（Value）：

```c
(((header) >> SIP_SVC_PROTO_HEADER_CODE_OFFSET) & SIP_SVC_PROTO_HEADER_CODE_MASK)
```

<a id="a4badc2fa72b4d5ae55c9b6503e3d2f41"></a>

### `SIP_SVC_PROTO_HEADER_GET_TRANS_ID`

```c
#define SIP_SVC_PROTO_HEADER_GET_TRANS_ID ( header)
```

展开值（Value）：

```c
(((header) >> SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET) & SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)
```

<a id="a57124f787454b1253737bdde7ad04c6f"></a>

### `SIP_SVC_PROTO_HEADER_SET_TRANS_ID`

```c
#define SIP_SVC_PROTO_HEADER_SET_TRANS_ID ( header, trans_id )
```

展开值（Value）：

```c
(header) &= ~(SIP_SVC_PROTO_HEADER_TRANS_ID_MASK << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET); \
(header) |= (((trans_id)&SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)                               \
             << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET);
```

<a id="a2da7d9fd032cf43814b535f7b9ff9028"></a>

### `SIP_SVC_PROTO_HEADER_TRANS_ID_MASK`

```c
#define SIP_SVC_PROTO_HEADER_TRANS_ID_MASK 0xFF
```

<a id="a4f147d26b354026e01225395e3f074ce"></a>

### `SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET`

```c
#define SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET 16
```

<a id="a8ffae8b2e3adb78378308944fb38601e"></a>

### `SIP_SVC_PROTO_HEADER_VER_MASK`

```c
#define SIP_SVC_PROTO_HEADER_VER_MASK 0x3
```

<a id="a10ce84feaee4a6454c36dc3daf4f7722"></a>

### `SIP_SVC_PROTO_HEADER_VER_OFFSET`

```c
#define SIP_SVC_PROTO_HEADER_VER_OFFSET 30
```

<a id="aeae6b273da4e3e91f0a6ee2558a7585f"></a>

### `SIP_SVC_PROTO_STATUS_BUSY`

```c
#define SIP_SVC_PROTO_STATUS_BUSY 0x1
```

<a id="a0d92a17202ff227476277500f539fd51"></a>

### `SIP_SVC_PROTO_STATUS_ERROR`

```c
#define SIP_SVC_PROTO_STATUS_ERROR 0x4
```

<a id="afba704d63c783fdd3d143045ca260706"></a>

### `SIP_SVC_PROTO_STATUS_NO_RESPONSE`

```c
#define SIP_SVC_PROTO_STATUS_NO_RESPONSE 0x3
```

<a id="af4153e73a6024d7d4355e9373f10388b"></a>

### `SIP_SVC_PROTO_STATUS_OK`

```c
#define SIP_SVC_PROTO_STATUS_OK 0x0
```

响应头部中的错误码（Error Code）。

SIP_SVC_PROTO_STATUS_OK（成功状态）

- 成功执行请求。

SIP_SVC_PROTO_STATUS_UNKNOWN（未知状态）

- 无法识别的 SMC/HVC 功能 ID（Function ID）。

SIP_SVC_PROTO_STATUS_BUSY（忙状态）

- 请求仍在处理中，请重试。

SIP_SVC_PROTO_STATUS_REJECT（拒绝状态）

- 请求因输入数据不当而被拒绝。

SIP_SVC_PROTO_STATUS_NO_RESPONSE（无响应状态）

- 目标硬件尚未响应。

SIP_SVC_PROTO_STATUS_ERROR（错误状态）

- 执行请求时发生错误。

SIP_SVC_PROTO_STATUS_NOT_SUPPORT（不支持状态）

- 不支持的 Arm SiP 服务命令码（Command Code）。

<a id="aa777087a721423e0e65cac4949813aaf"></a>

### `SIP_SVC_PROTO_STATUS_REJECT`

```c
#define SIP_SVC_PROTO_STATUS_REJECT 0x2
```

<a id="a1c7567c532ab25d3d21ed76c655b9680"></a>

### `SIP_SVC_PROTO_STATUS_UNKNOWN`

```c
#define SIP_SVC_PROTO_STATUS_UNKNOWN 0xFFFF
```

<a id="a5544d9131eef67538c3a36bdfec5482e"></a>

### `SIP_SVC_PROTO_VER`

```c
#define SIP_SVC_PROTO_VER 0x0
```

头部格式（Header Format）。


## 11.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P790_sip_svc_proto.h_源码浏览.md)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asip__svc__proto_8h_html_a10ce84feaee4a6454c36dc3daf4f7722"></a>
<a id="asip__svc__proto_8h_html_a218d17af00117be8baf393e6b95cd9b2"></a>
<a id="asip__svc__proto_8h_html_a2da7d9fd032cf43814b535f7b9ff9028"></a>
<a id="asip__svc__proto_8h_html_a4f147d26b354026e01225395e3f074ce"></a>
<a id="asip__svc__proto_8h_html_a5544d9131eef67538c3a36bdfec5482e"></a>
<a id="asip__svc__proto_8h_html_a8ffae8b2e3adb78378308944fb38601e"></a>
<a id="asip__svc__proto_8h_html_aa8dbe689b3b375f72d049a89389ff591"></a>

---

[上一章](P010_zephyr__drivers__interrupt_controller__riscv_aia.h_文件参考.md) · [返回大纲](大纲.md)
