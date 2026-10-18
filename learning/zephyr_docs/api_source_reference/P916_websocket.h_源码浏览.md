---
id: learning.zephyr-docs.api-source-reference.page-916
title: websocket.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第916章\_websocket.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html)。

## 916.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="agroup__http__client_html_ga34a431c54c52b86618ca0e27ce3862b4"></a>
<a id="agroup__websocket_html_ga0fb118f84b7631d12c1b742b75593ba6"></a>
<a id="agroup__websocket_html_ga207402575311103c75906143724e8c35"></a>
<a id="agroup__websocket_html_ga71a43ec629929d2eb1baba4e3f13a615"></a>
<a id="agroup__websocket_html_gaa3131d2599c8c69ab95c55c2e38e28e0"></a>
<a id="agroup__websocket_html_gaabfd7aa30ce659214b990eabb0b6d591"></a>
<a id="agroup__websocket_html_gabc2556e62f001f8109bf6ae9f50f3952"></a>
<a id="agroup__websocket_html_gac23c351e5020d0fc9e936933d399b187"></a>
<a id="agroup__websocket_html_gacc2f06e2c361317ff48f171abc3d1209"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69"></a>
<a id="agroup__websocket_html_gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709"></a>
<a id="ahttp_2client_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aparser_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructhttp__parser__settings_html"></a>
<a id="astructhttp__request_html"></a>
<a id="astructwebsocket__request_html"></a>
<a id="astructwebsocket__request_html_a09bb3c708b51d8f86de244b3fc4a9f57"></a>
<a id="astructwebsocket__request_html_a38315d0c37bdc8cfe22cdbc6d2c8af4a"></a>
<a id="astructwebsocket__request_html_a49ef6c2f4201beeb3af8992ded2bd4a3"></a>
<a id="astructwebsocket__request_html_a4cea74d6094325b218b6bbed4005b912"></a>
<a id="astructwebsocket__request_html_a8769d50f1a6168dc6518f2dd0c74b62a"></a>
<a id="astructwebsocket__request_html_a939ed8e980af4bc98f30d1bad835a2d2"></a>
<a id="astructwebsocket__request_html_a96936b68fec07f077d9e9569ef1411d1"></a>
<a id="astructwebsocket__request_html_ab7a281fff2a27a52f7ec346643f55b71"></a>

```c


/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_WEBSOCKET_H_
#define ZEPHYR_INCLUDE_NET_WEBSOCKET_H_

#include <zephyr/kernel.h>

#include <zephyr/net/net_ip.h>
#include <zephyr/net/http/parser.h>
#include <zephyr/net/http/client.h>

#ifdef __cplusplus
extern "C" {
#endif


#define WEBSOCKET_FLAG_FINAL  0x00000001
#define WEBSOCKET_FLAG_TEXT   0x00000002
#define WEBSOCKET_FLAG_BINARY 0x00000004
#define WEBSOCKET_FLAG_CLOSE  0x00000008
#define WEBSOCKET_FLAG_PING   0x00000010
#define WEBSOCKET_FLAG_PONG   0x00000020

enum websocket_opcode  {
        WEBSOCKET_OPCODE_CONTINUE     = 0x00,
        WEBSOCKET_OPCODE_DATA_TEXT    = 0x01,
        WEBSOCKET_OPCODE_DATA_BINARY  = 0x02,
        WEBSOCKET_OPCODE_CLOSE        = 0x08,
        WEBSOCKET_OPCODE_PING         = 0x09,
        WEBSOCKET_OPCODE_PONG         = 0x0A,
};

typedef int (*websocket_connect_cb_t)(int ws_sock, struct http_request *req,
                                      void *user_data);

struct websocket_request {
        const char *host;

        const char *url;

        http_header_cb_t optional_headers_cb;

        const char **optional_headers;

        websocket_connect_cb_t cb;

        const struct http_parser_settings *http_cb;

        uint8_t *tmp_buf;

        size_t tmp_buf_len;
};

int websocket_connect(int http_sock, struct websocket_request *req,
                      int32_t timeout, void *user_data);

int websocket_send_msg(int ws_sock, const uint8_t *payload, size_t payload_len,
                       enum websocket_opcode opcode, bool mask, bool final,
                       int32_t timeout);

int websocket_recv_msg(int ws_sock, uint8_t *buf, size_t buf_len,
                       uint32_t *message_type, uint64_t *remaining,
                       int32_t timeout);

int websocket_disconnect(int ws_sock);

int websocket_register(int http_sock, uint8_t *recv_buf, size_t recv_buf_len);

int websocket_unregister(int ws_sock);


#if defined(CONFIG_WEBSOCKET_CLIENT)
void websocket_init(void);
#else
static inline void websocket_init(void)
{
}
#endif


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_WEBSOCKET_H_ */
```

## 916.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 238 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WEBSOCKET_H_`。

## 916.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [zephyr/net/http/client.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html)
- [websocket_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga207402575311103c75906143724e8c35)
- [WEBSOCKET_OPCODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35)
- [WEBSOCKET_OPCODE_DATA_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c)
- [WEBSOCKET_OPCODE_DATA_BINARY](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69)
- [WEBSOCKET_OPCODE_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191)
- [WEBSOCKET_OPCODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709)
- [WEBSOCKET_OPCODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90)
- [websocket_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaabfd7aa30ce659214b990eabb0b6d591)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [websocket_request](../network_application_model_reference/P089_websocket_request_结构体.md)
- [host](../network_application_model_reference/P089_websocket_request_结构体.md#a8769d50f1a6168dc6518f2dd0c74b62a)
- [url](../network_application_model_reference/P089_websocket_request_结构体.md#a49ef6c2f4201beeb3af8992ded2bd4a3)
- [http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)
- [optional_headers_cb](../network_application_model_reference/P089_websocket_request_结构体.md#ab7a281fff2a27a52f7ec346643f55b71)
- [optional_headers](../network_application_model_reference/P089_websocket_request_结构体.md#a4cea74d6094325b218b6bbed4005b912)
- [cb](../network_application_model_reference/P089_websocket_request_结构体.md#a96936b68fec07f077d9e9569ef1411d1)
- [http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)
- [http_cb](../network_application_model_reference/P089_websocket_request_结构体.md#a38315d0c37bdc8cfe22cdbc6d2c8af4a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [tmp_buf](../network_application_model_reference/P089_websocket_request_结构体.md#a939ed8e980af4bc98f30d1bad835a2d2)
- [tmp_buf_len](../network_application_model_reference/P089_websocket_request_结构体.md#a09bb3c708b51d8f86de244b3fc4a9f57)
- [websocket_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga71a43ec629929d2eb1baba4e3f13a615)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [websocket_send_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gac23c351e5020d0fc9e936933d399b187)
- [websocket_recv_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#ga0fb118f84b7631d12c1b742b75593ba6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [websocket_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gacc2f06e2c361317ff48f171abc3d1209)
- [websocket_register](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gabc2556e62f001f8109bf6ae9f50f3952)
- [websocket_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaa3131d2599c8c69ab95c55c2e38e28e0)
- [client.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [websocket_request::tmp_buf_len](../network_application_model_reference/P089_websocket_request_结构体.md#a09bb3c708b51d8f86de244b3fc4a9f57)
- [websocket_request::http_cb](../network_application_model_reference/P089_websocket_request_结构体.md#a38315d0c37bdc8cfe22cdbc6d2c8af4a)
- [websocket_request::url](../network_application_model_reference/P089_websocket_request_结构体.md#a49ef6c2f4201beeb3af8992ded2bd4a3)
- [websocket_request::optional_headers](../network_application_model_reference/P089_websocket_request_结构体.md#a4cea74d6094325b218b6bbed4005b912)
- [websocket_request::host](../network_application_model_reference/P089_websocket_request_结构体.md#a8769d50f1a6168dc6518f2dd0c74b62a)
- [websocket_request::tmp_buf](../network_application_model_reference/P089_websocket_request_结构体.md#a939ed8e980af4bc98f30d1bad835a2d2)
- [websocket_request::cb](../network_application_model_reference/P089_websocket_request_结构体.md#a96936b68fec07f077d9e9569ef1411d1)
- [websocket_request::optional_headers_cb](../network_application_model_reference/P089_websocket_request_结构体.md#ab7a281fff2a27a52f7ec346643f55b71)

---

[上一章](P915_w1_sensor.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P917_wifi_certs.h_源码浏览.md)
