---
id: learning.zephyr-docs.api-source-reference.page-787
title: sip_svc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第787章\_sip\_svc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html)。

## 787.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="akernel_8h_html"></a>
<a id="asip__svc_8h_html_a217c518c046cd1d716d803175b4cd99e"></a>
<a id="asip__svc_8h_html_a73d836f58dd466241f5ba50955468b4c"></a>
<a id="asip__svc_8h_html_a754649a7ad55281bc0059036b0e5c7e9"></a>
<a id="asip__svc_8h_html_a7f5a7116667f4904d128935e3a0fcc58"></a>
<a id="asip__svc_8h_html_aaafe385fe1dd0b13fe6dbffd2f01bd16"></a>
<a id="asip__svc_8h_html_ab3774b372ddba3d3c4dd6e0a80082b9e"></a>
<a id="asip__svc_8h_html_ac1991768d256e5260542c544859c5bca"></a>
<a id="asip__svc_8h_html_afd71f6da58b4e8df3fbcf3b985226e74"></a>
<a id="asip__svc__proto_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructsip__svc__request_html"></a>
<a id="astructsip__svc__response_html"></a>
<a id="astructsip__svc__response_html_a992b3f936866852633569f9c8d37d6a0"></a>

```c
/*
 * Copyright (c) 2022-2023, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_H_
#define ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_H_


#include <zephyr/kernel.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>

#define SIP_SVC_CLIENT_ST_INVALID 0
#define SIP_SVC_CLIENT_ST_IDLE    1
#define SIP_SVC_CLIENT_ST_OPEN    2
#define SIP_SVC_CLIENT_ST_ABORT   3

typedef void (*sip_svc_cb_fn)(uint32_t c_token, struct sip_svc_response *res);

uint32_t sip_svc_register(void *ctrl, void *priv_data);

int sip_svc_unregister(void *ctrl, uint32_t c_token);

int sip_svc_open(void *ctrl, uint32_t c_token, k_timeout_t k_timeout);

int sip_svc_close(void *ctrl, uint32_t c_token, struct sip_svc_request *pre_close_req);

int sip_svc_send(void *ctrl, uint32_t c_token, struct sip_svc_request *req, sip_svc_cb_fn cb);

void *sip_svc_get_priv_data(void *ctrl, uint32_t c_token);

void *sip_svc_get_controller(char *method);

#endif /* ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_H_ */
```

## 787.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 188 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_H_`。

## 787.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/drivers/sip_svc/sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)
- [sip_svc_cb_fn](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#a73d836f58dd466241f5ba50955468b4c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)
- [sip_svc_register](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#a7f5a7116667f4904d128935e3a0fcc58)
- [priv_data](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a992b3f936866852633569f9c8d37d6a0)
- [sip_svc_unregister](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#aaafe385fe1dd0b13fe6dbffd2f01bd16)
- [sip_svc_open](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#ac1991768d256e5260542c544859c5bca)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [sip_svc_close](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#ab3774b372ddba3d3c4dd6e0a80082b9e)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [sip_svc_send](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#afd71f6da58b4e8df3fbcf3b985226e74)
- [sip_svc_get_priv_data](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#a754649a7ad55281bc0059036b0e5c7e9)
- [sip_svc_get_controller](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc_8h.html#a217c518c046cd1d716d803175b4cd99e)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)
- [sip_svc_response::priv_data](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a992b3f936866852633569f9c8d37d6a0)

---

[上一章](P786_simcom-sim7080.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P788_sip_svc_agilex_mailbox.h_源码浏览.md)
