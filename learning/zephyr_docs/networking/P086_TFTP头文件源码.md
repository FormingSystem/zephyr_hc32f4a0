---
id: learning.zephyr-docs.networking.api-86
title: TFTP头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tftp_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_TFTP头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tftp_8h_source.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 86.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

下方保留官方源码浏览页展示的全部代码、标识符、声明及版权／许可注释。仅移除网页行号，将展示用不换行空格还原为普通空格，并清除行尾空白。原页面已省略部分生成API文档的注释，因此行号原本存在跳跃；这不是完整原始头文件的替代品。接口注释译文见本组API及结构体页。

## 86.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00058"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="agroup__tftp__client_html_ga067de19b4089fbd2c2e49e925b73cfb0"></a>
<a id="agroup__tftp__client_html_ga1ee3d814c6fbaf5570eb5fd9605af7ea"></a>
<a id="agroup__tftp__client_html_ga4387f92c6327823d655d8aa4f1c65beb"></a>
<a id="agroup__tftp__client_html_ga692f6a51f2ecd5c3d673ff64f59294b9"></a>
<a id="agroup__tftp__client_html_gafc2d0fd730046b0d3781362263e68ddc"></a>
<a id="agroup__tftp__client_html_gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3"></a>
<a id="agroup__tftp__client_html_gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d"></a>
<a id="akernel_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructtftp__data__param_html"></a>
<a id="astructtftp__data__param_html_a704c20ab3177a3d53df21fc9ef64d084"></a>
<a id="astructtftp__data__param_html_a93f666944e8f20bd3a0e1320452913db"></a>
<a id="astructtftp__error__param_html"></a>
<a id="astructtftp__error__param_html_a725f1d2b8b8848febacf4888a0b55611"></a>
<a id="astructtftp__error__param_html_aa8766ec6c9e92c9383b0dbbafe8a0f43"></a>
<a id="astructtftp__evt_html"></a>
<a id="astructtftp__evt_html_a2d622d9eb3ee0547b47a1330ad9cc412"></a>
<a id="astructtftp__evt_html_a37154f19c66ae09a200f4d8d6c2941ca"></a>
<a id="astructtftpc_html"></a>
<a id="astructtftpc_html_a23f6f3d19493edbdc050df6d75441f92"></a>
<a id="astructtftpc_html_a39a04978a6cf3826ef19993989400b60"></a>
<a id="astructtftpc_html_af3791441bbcaaaad3c701fc62909bfa7"></a>
<a id="auniontftp__evt__param_html"></a>
<a id="auniontftp__evt__param_html_a489485b84fa3e559b3065258cabfb205"></a>
<a id="auniontftp__evt__param_html_a7bec7cd5512f25699fe6b733458e9128"></a>

```c
/*
 * Copyright (c) 2020 InnBlue
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_TFTP_H_
#define ZEPHYR_INCLUDE_NET_TFTP_H_

#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif

#define TFTP_BLOCK_SIZE          512

#define TFTP_HEADER_SIZE         4

#define TFTPC_MAX_BUF_SIZE       (TFTP_BLOCK_SIZE + TFTP_HEADER_SIZE)

#define TFTPC_SUCCESS             0
#define TFTPC_DUPLICATE_DATA     -1
#define TFTPC_BUFFER_OVERFLOW    -2
#define TFTPC_UNKNOWN_FAILURE    -3
#define TFTPC_REMOTE_ERROR       -4
#define TFTPC_RETRIES_EXHAUSTED  -5

enum tftp_evt_type {
        TFTP_EVT_DATA,

        TFTP_EVT_ERROR
};

struct tftp_data_param {
        uint8_t *data_ptr;
        uint32_t len;
};

struct tftp_error_param {
        char *msg;
        int code;
};

union tftp_evt_param {
        struct tftp_data_param data;

        struct tftp_error_param error;
};

struct tftp_evt {
        enum tftp_evt_type type;

        union tftp_evt_param param;
};

typedef void (*tftp_callback_t)(const struct tftp_evt *evt);

struct tftpc {
        union {
                struct net_sockaddr_storage server_addr;
                /* Do not access this directly, use server_addr instead */
                struct net_sockaddr server;
        };

        tftp_callback_t callback;

        uint8_t tftp_buf[TFTPC_MAX_BUF_SIZE];
};

int tftp_get(struct tftpc *client,
             const char *remote_file, const char *mode);

int tftp_put(struct tftpc *client,
             const char *remote_file, const char *mode,
             const uint8_t *user_buf, uint32_t user_buf_size);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_TFTP_H_ */
```

## 86.3\_源码注释译文

版权：2020年InnBlue；许可证标识为`Apache-2.0`。`struct tftpc`中`server`成员前的注释是：“不要直接访问此成员，改用`server_addr`。”

末尾`#endif`注释标明结束对应的头文件包含保护（Header Include Guard）。原始法律署名与许可证标识保持原样。

[上一章](P085_TFTP头文件参考.md) · [返回大纲](大纲.md) · [下一章](P087_TFTP客户端上下文.md)
