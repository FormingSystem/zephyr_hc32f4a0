---
id: learning.zephyr-docs.api-file-reference.page-395
title: zephyr__drivers__sip_svc__sip_svc_agilex_smc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__smc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第395章\_zephyr\_\_drivers\_\_sip\_svc\_\_sip\_svc\_agilex\_smc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__smc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Intel SoC FPGA Agilex定制的Arm SiP服务安全监控调用（SMC）协议。

查看此文件的源码。

<a id="details"></a>

Intel SoC FPGA Agilex定制的Arm SiP服务安全监控调用（SMC）协议。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 395.1\_宏定义（Macros）

<a id="r_abca52daa3ed42c3acacd0a2f27a64c8b"></a>

```c
#define SMC_STATUS_INVALID 0xFFFFFFFF
```

相关声明：[SMC_STATUS_INVALID](#abca52daa3ed42c3acacd0a2f27a64c8b)。

<a id="r_aff7de6199219a46e9c177557a55b20ad"></a>

```c
#define SMC_STATUS_OKAY 0
```

相关声明：[SMC_STATUS_OKAY](#aff7de6199219a46e9c177557a55b20ad)。

<a id="r_a8959eae5cbbe690922a6aa35c3e6ad19"></a>

```c
#define SMC_STATUS_BUSY 1
```

相关声明：[SMC_STATUS_BUSY](#a8959eae5cbbe690922a6aa35c3e6ad19)。

<a id="r_a2350309516a2c57ec3250a53305d0627"></a>

```c
#define SMC_STATUS_REJECT 2
```

相关声明：[SMC_STATUS_REJECT](#a2350309516a2c57ec3250a53305d0627)。

<a id="r_a1b99b2307df8b02a1f3dd36614077269"></a>

```c
#define SMC_STATUS_NO_RESPONSE 3
```

相关声明：[SMC_STATUS_NO_RESPONSE](#a1b99b2307df8b02a1f3dd36614077269)。

<a id="r_a0f21a71f1245c31ef3a3a468901a7fe3"></a>

```c
#define SMC_STATUS_ERROR 4
```

相关声明：[SMC_STATUS_ERROR](#a0f21a71f1245c31ef3a3a468901a7fe3)。

<a id="r_a149c807c9429c49b48febb7493ded05a"></a>

```c
#define SMC_PLAT_PROTO_VER 0x0
```

相关声明：[SMC_PLAT_PROTO_VER](#a149c807c9429c49b48febb7493ded05a)。

<a id="r_aaf01ecddc145b991b1437dc4ccd88854"></a>

```c
#define SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET 0
```

相关声明：[SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET](#aaf01ecddc145b991b1437dc4ccd88854)。

<a id="r_a8fe58b94720ef6bb2cb46351c9e3da8f"></a>

```c
#define SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK 0xFF
```

相关声明：[SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK](#a8fe58b94720ef6bb2cb46351c9e3da8f)。

<a id="r_ae9827c60ec0c0e0d62167672b443d136"></a>

```c
#define SMC_PLAT_PROTO_HEADER_VER_OFFSET 60
```

相关声明：[SMC_PLAT_PROTO_HEADER_VER_OFFSET](#ae9827c60ec0c0e0d62167672b443d136)。

<a id="r_a14cf7302d786ab126a18abbd0e757fed"></a>

```c
#define SMC_PLAT_PROTO_HEADER_VER_MASK 0xF
```

相关声明：[SMC_PLAT_PROTO_HEADER_VER_MASK](#a14cf7302d786ab126a18abbd0e757fed)。

<a id="r_a0ac21d31ae06d1fa1fd86253526baff2"></a>

```c
#define SMC_PLAT_PROTO_HEADER ((SMC_PLAT_PROTO_VER & SMC_PLAT_PROTO_HEADER_VER_MASK) << SMC_PLAT_PROTO_HEADER_VER_OFFSET)
```

相关声明：[SMC_PLAT_PROTO_HEADER](#a0ac21d31ae06d1fa1fd86253526baff2)、[SMC_PLAT_PROTO_VER](#a149c807c9429c49b48febb7493ded05a)、[SMC_PLAT_PROTO_HEADER_VER_MASK](#a14cf7302d786ab126a18abbd0e757fed)、[SMC_PLAT_PROTO_HEADER_VER_OFFSET](#ae9827c60ec0c0e0d62167672b443d136)。

<a id="r_aee5f5ecdeb83631a3114593e2e487a43"></a>

```c
#define SMC_PLAT_PROTO_HEADER_SET_TRANS_ID(header, trans_id)
```

相关声明：[SMC_PLAT_PROTO_HEADER_SET_TRANS_ID](#aee5f5ecdeb83631a3114593e2e487a43)。

<a id="r_afa8c0dca448e2074bfc6abeaffd26464"></a>

```c
#define SMC_FUNC_ID_GET_SVC_VERSION 0xC2000400
```

相关声明：[SMC_FUNC_ID_GET_SVC_VERSION](#afa8c0dca448e2074bfc6abeaffd26464)。

<a id="r_afcaee0b300ae5fbe475c51c1d20b8e48"></a>

```c
#define SMC_FUNC_ID_REG_READ 0xC2000401
```

相关声明：[SMC_FUNC_ID_REG_READ](#afcaee0b300ae5fbe475c51c1d20b8e48)。

<a id="r_ab619bffd89340c1d72f3786d2c8d326b"></a>

```c
#define SMC_FUNC_ID_REG_WRITE 0xC2000402
```

相关声明：[SMC_FUNC_ID_REG_WRITE](#ab619bffd89340c1d72f3786d2c8d326b)。

<a id="r_ad56834ca5734a3d105e6810cb4821406"></a>

```c
#define SMC_FUNC_ID_REG_UPDATE 0xC2000403
```

相关声明：[SMC_FUNC_ID_REG_UPDATE](#ad56834ca5734a3d105e6810cb4821406)。

<a id="r_a382037b06541eb54757b3ad9fd7df8a4"></a>

```c
#define SMC_FUNC_ID_SET_HPS_BRIDGES 0xC2000404
```

相关声明：[SMC_FUNC_ID_SET_HPS_BRIDGES](#a382037b06541eb54757b3ad9fd7df8a4)。

<a id="r_abf081ba2e3a8039b42c40f8a7135c113"></a>

```c
#define SMC_FUNC_ID_RSU_UPDATE_ADDR 0xC2000405
```

相关声明：[SMC_FUNC_ID_RSU_UPDATE_ADDR](#abf081ba2e3a8039b42c40f8a7135c113)。

<a id="r_a98d77f81a2b07bcf8305e28e0be1e4c4"></a>

```c
#define SMC_FUNC_ID_MAILBOX_SEND_COMMAND 0xC2000420
```

相关声明：[SMC_FUNC_ID_MAILBOX_SEND_COMMAND](#a98d77f81a2b07bcf8305e28e0be1e4c4)。

<a id="r_ac26572cb1321697ff33adcd471e27874"></a>

```c
#define SMC_FUNC_ID_MAILBOX_POLL_RESPONSE 0xC2000421
```

相关声明：[SMC_FUNC_ID_MAILBOX_POLL_RESPONSE](#ac26572cb1321697ff33adcd471e27874)。

<a id="r_a0a1d2a2c6a290c6b293fa71cd04975fb"></a>

```c
#define MAILBOX_CANCEL_COMMAND 0x03
```

相关声明：[MAILBOX_CANCEL_COMMAND](#a0a1d2a2c6a290c6b293fa71cd04975fb)。

## 395.2\_详细说明（Detailed Documentation）

<a id="a0a1d2a2c6a290c6b293fa71cd04975fb"></a>

### `MAILBOX_CANCEL_COMMAND`

```c
#define MAILBOX_CANCEL_COMMAND 0x03
```

<a id="afa8c0dca448e2074bfc6abeaffd26464"></a>

### `SMC_FUNC_ID_GET_SVC_VERSION`

```c
#define SMC_FUNC_ID_GET_SVC_VERSION 0xC2000400
```

<a id="ac26572cb1321697ff33adcd471e27874"></a>

### `SMC_FUNC_ID_MAILBOX_POLL_RESPONSE`

```c
#define SMC_FUNC_ID_MAILBOX_POLL_RESPONSE 0xC2000421
```

<a id="a98d77f81a2b07bcf8305e28e0be1e4c4"></a>

### `SMC_FUNC_ID_MAILBOX_SEND_COMMAND`

```c
#define SMC_FUNC_ID_MAILBOX_SEND_COMMAND 0xC2000420
```

<a id="afcaee0b300ae5fbe475c51c1d20b8e48"></a>

### `SMC_FUNC_ID_REG_READ`

```c
#define SMC_FUNC_ID_REG_READ 0xC2000401
```

<a id="ad56834ca5734a3d105e6810cb4821406"></a>

### `SMC_FUNC_ID_REG_UPDATE`

```c
#define SMC_FUNC_ID_REG_UPDATE 0xC2000403
```

<a id="ab619bffd89340c1d72f3786d2c8d326b"></a>

### `SMC_FUNC_ID_REG_WRITE`

```c
#define SMC_FUNC_ID_REG_WRITE 0xC2000402
```

<a id="abf081ba2e3a8039b42c40f8a7135c113"></a>

### `SMC_FUNC_ID_RSU_UPDATE_ADDR`

```c
#define SMC_FUNC_ID_RSU_UPDATE_ADDR 0xC2000405
```

<a id="a382037b06541eb54757b3ad9fd7df8a4"></a>

### `SMC_FUNC_ID_SET_HPS_BRIDGES`

```c
#define SMC_FUNC_ID_SET_HPS_BRIDGES 0xC2000404
```

<a id="a0ac21d31ae06d1fa1fd86253526baff2"></a>

### `SMC_PLAT_PROTO_HEADER`

```c
#define SMC_PLAT_PROTO_HEADER ((SMC_PLAT_PROTO_VER & SMC_PLAT_PROTO_HEADER_VER_MASK) << SMC_PLAT_PROTO_HEADER_VER_OFFSET)
```

<a id="aee5f5ecdeb83631a3114593e2e487a43"></a>

### `SMC_PLAT_PROTO_HEADER_SET_TRANS_ID`

```c
#define SMC_PLAT_PROTO_HEADER_SET_TRANS_ID ( header, trans_id )
```

展开值（Value）：

```c
(header) &=                                                                                \
        ~(SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK << SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET);   \
(header) |= (((trans_id)&SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK)                              \
             << SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET);
```

<a id="a8fe58b94720ef6bb2cb46351c9e3da8f"></a>

### `SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK`

```c
#define SMC_PLAT_PROTO_HEADER_TRANS_ID_MASK 0xFF
```

<a id="aaf01ecddc145b991b1437dc4ccd88854"></a>

### `SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET`

```c
#define SMC_PLAT_PROTO_HEADER_TRANS_ID_OFFSET 0
```

<a id="a14cf7302d786ab126a18abbd0e757fed"></a>

### `SMC_PLAT_PROTO_HEADER_VER_MASK`

```c
#define SMC_PLAT_PROTO_HEADER_VER_MASK 0xF
```

<a id="ae9827c60ec0c0e0d62167672b443d136"></a>

### `SMC_PLAT_PROTO_HEADER_VER_OFFSET`

```c
#define SMC_PLAT_PROTO_HEADER_VER_OFFSET 60
```

<a id="a149c807c9429c49b48febb7493ded05a"></a>

### `SMC_PLAT_PROTO_VER`

```c
#define SMC_PLAT_PROTO_VER 0x0
```

<a id="a8959eae5cbbe690922a6aa35c3e6ad19"></a>

### `SMC_STATUS_BUSY`

```c
#define SMC_STATUS_BUSY 1
```

<a id="a0f21a71f1245c31ef3a3a468901a7fe3"></a>

### `SMC_STATUS_ERROR`

```c
#define SMC_STATUS_ERROR 4
```

<a id="abca52daa3ed42c3acacd0a2f27a64c8b"></a>

### `SMC_STATUS_INVALID`

```c
#define SMC_STATUS_INVALID 0xFFFFFFFF
```

<a id="a1b99b2307df8b02a1f3dd36614077269"></a>

### `SMC_STATUS_NO_RESPONSE`

```c
#define SMC_STATUS_NO_RESPONSE 3
```

<a id="aff7de6199219a46e9c177557a55b20ad"></a>

### `SMC_STATUS_OKAY`

```c
#define SMC_STATUS_OKAY 0
```

<a id="a2350309516a2c57ec3250a53305d0627"></a>

### `SMC_STATUS_REJECT`

```c
#define SMC_STATUS_REJECT 2
```


## 395.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__agilex__smc_8h_source.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asip__svc__agilex__smc_8h_html_a8fe58b94720ef6bb2cb46351c9e3da8f"></a>
<a id="asip__svc__agilex__smc_8h_html_aaf01ecddc145b991b1437dc4ccd88854"></a>

---

[上一章](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P396_zephyr__dt-bindings__pinctrl__silabs__siwx91x-pinctrl.h_文件参考.md)
