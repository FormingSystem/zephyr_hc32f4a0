---
id: learning.zephyr-docs.api-source-reference.page-261
title: fido2_transport.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第261章\_fido2\_transport.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html)。

## 261.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00147"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="afido2__transport_8h_html_a081a49ee568a0939254bc640b509c3f8"></a>
<a id="afido2__transport_8h_html_a7d65ad137d8ce67f9af03a6f37d1720b"></a>
<a id="afido2__transport_8h_html_a7d65ad137d8ce67f9af03a6f37d1720ba5106b64cfc0b02d2beeae5e2d84d0049"></a>
<a id="afido2__transport_8h_html_a7d65ad137d8ce67f9af03a6f37d1720baaa077f7facef9bf040cd0173f3e3cc61"></a>
<a id="afido2__transport_8h_html_a7d65ad137d8ce67f9af03a6f37d1720bab4d2bd4f1f2c898cf706afbb12c43b8a"></a>
<a id="afido2__transport_8h_html_af8365317181d301d3f44fd3eb9416475"></a>
<a id="afido2__types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfido2__transport__api_html"></a>
<a id="astructfido2__transport__api_html_a79bd5f4a1556c5ee451b8b62f674a861"></a>
<a id="astructfido2__transport__api_html_aade11fc3660d148850816f7de6f6810d"></a>
<a id="astructfido2__transport__api_html_abd7cdffe93a80e3f0ac16550b6edf4d3"></a>
<a id="astructfido2__transport__api_html_af9ded3aefb0c8c43337ba3d133a34555"></a>
<a id="astructfido2__transport_html"></a>
<a id="astructfido2__transport_html_a90ea57f7cc443a41bbd9d879bc5f652a"></a>
<a id="astructfido2__transport_html_acda0c8702b378196f0ef1c86d1c56b44"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TRANSPORT_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TRANSPORT_H_

#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/authentication/fido2/fido2_types.h>
#include <stddef.h>
#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif

struct fido2_transport;

#define FIDO2_BLE_SERVICE_UUID_VAL 0xFFFDU

#define FIDO2_BLE_SERVICE_DATA_PAIRING_MODE BIT(7)

enum fido2_wire_status {
        FIDO2_WIRE_STATUS_UP_NEEDED,
        FIDO2_WIRE_STATUS_PROCESSING,
        FIDO2_WIRE_STATUS_DONE
};

typedef int (*fido2_transport_recv_cb_t)(const struct fido2_transport *transport, uint32_t cid,
                                         const uint8_t *buf, size_t len);

typedef void (*fido2_transport_cancel_cb_t)(const struct fido2_transport *transport);

struct fido2_transport_api {
        int (*init)(fido2_transport_recv_cb_t cb, fido2_transport_cancel_cb_t cancel_cb);

        int (*send)(uint32_t cid, const uint8_t *data, size_t len);

        void (*notify)(uint32_t cid, enum fido2_wire_status status);

        void (*shutdown)(void);
};

struct fido2_transport {
        const char *name;
        const struct fido2_transport_api *api;
};

#define FIDO2_TRANSPORT_DEFINE(_name, _label, _api)                                                \
        STRUCT_SECTION_ITERABLE(fido2_transport, _name) = {                                        \
                .name = _label,                                                                    \
                .api = _api,                                                                       \
        }


int fido2_transport_init_all(fido2_transport_recv_cb_t cb, fido2_transport_cancel_cb_t cancel_cb);

void fido2_transport_shutdown_all(void);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TRANSPORT_H_ */
```

## 261.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 174 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TRANSPORT_H_`。

## 261.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/authentication/fido2/fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [fido2_transport](../platform_security_model_reference/P010_fido2_transport_结构体.md)
- [fido2_wire_status](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720b)
- [FIDO2_WIRE_STATUS_UP_NEEDED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720baaa077f7facef9bf040cd0173f3e3cc61)
- [FIDO2_WIRE_STATUS_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720ba5106b64cfc0b02d2beeae5e2d84d0049)
- [FIDO2_WIRE_STATUS_DONE](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a7d65ad137d8ce67f9af03a6f37d1720bab4d2bd4f1f2c898cf706afbb12c43b8a)
- [fido2_transport_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#af8365317181d301d3f44fd3eb9416475)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fido2_transport_cancel_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a081a49ee568a0939254bc640b509c3f8)
- [fido2_transport_api](../platform_security_model_reference/P011_fido2_transport_api_结构体.md)
- [init](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#abd7cdffe93a80e3f0ac16550b6edf4d3)
- [send](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#a79bd5f4a1556c5ee451b8b62f674a861)
- [notify](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#af9ded3aefb0c8c43337ba3d133a34555)
- [shutdown](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#aade11fc3660d148850816f7de6f6810d)
- [name](../platform_security_model_reference/P010_fido2_transport_结构体.md#a90ea57f7cc443a41bbd9d879bc5f652a)
- [api](../platform_security_model_reference/P010_fido2_transport_结构体.md#acda0c8702b378196f0ef1c86d1c56b44)
- [fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fido2_transport_api::send](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#a79bd5f4a1556c5ee451b8b62f674a861)
- [fido2_transport_api::shutdown](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#aade11fc3660d148850816f7de6f6810d)
- [fido2_transport_api::init](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#abd7cdffe93a80e3f0ac16550b6edf4d3)
- [fido2_transport_api::notify](../platform_security_model_reference/P011_fido2_transport_api_结构体.md#af9ded3aefb0c8c43337ba3d133a34555)
- [fido2_transport::name](../platform_security_model_reference/P010_fido2_transport_结构体.md#a90ea57f7cc443a41bbd9d879bc5f652a)
- [fido2_transport::api](../platform_security_model_reference/P010_fido2_transport_结构体.md#acda0c8702b378196f0ef1c86d1c56b44)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P260_fido2_storage.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P262_fido2_types.h_源码浏览.md)
