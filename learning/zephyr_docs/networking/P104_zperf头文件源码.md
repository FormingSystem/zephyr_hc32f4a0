---
id: learning.zephyr-docs.networking.api-104
title: zperf头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zperf_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_zperf头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/zperf_8h_source.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 104.1\_阅读说明与来源

译注：先读[zperf指南](P096_zperf网络流量生成器.md)、[示例](P097_zperf网络流量生成器示例.md)和[回环吞吐量测试](P098_zperf确定性回环吞吐量.md)，再查本组接口。

本组：[完整API参考](P102_zperf完整API参考.md) · [头文件参考](P103_zperf头文件参考.md) · [头文件源码](P104_zperf头文件源码.md)。

下方保留官方Doxygen源码浏览页展示的全部代码、标识符及版权／许可注释。仅移除网页行号，将展示用不换行空格还原为普通空格，并清除行尾空白。原页面省略了部分生成API文档的注释，原行号因此存在跳跃；此展示不能替代完整原始头文件。接口注释译文见本组API页。

## 104.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="agroup__zperf_html_ga07704e0bd701c0f2da2b74b9a83d6b35"></a>
<a id="agroup__zperf_html_ga24c061ea0dcd44b94c2ad79dfa264e44"></a>
<a id="agroup__zperf_html_ga394e3a10550cf9d0a435f5d217dfbbdf"></a>
<a id="agroup__zperf_html_ga6f2704914a9a577dac119a11f98c0e8e"></a>
<a id="agroup__zperf_html_ga9ac136e27fc87f85ddb66cbd2f78256d"></a>
<a id="agroup__zperf_html_gaae9e5669a76da0cde7454bbd7b491a4a"></a>
<a id="agroup__zperf_html_gac29193fb02ccb159b7adc3c8de64895a"></a>
<a id="agroup__zperf_html_gacf57dcebd09cae8ecf61b553baf6b2cd"></a>
<a id="agroup__zperf_html_gaffeb2d7cbca61021984e784f7ba4595b"></a>
<a id="anet_2socket_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructzperf__results_html"></a>
<a id="astructzperf__results_html_a517ba180a6414a2f2d1484e698d57650"></a>
<a id="astructzperf__results_html_a550158fd641799c2a6b2d25617ac9a6c"></a>
<a id="astructzperf__results_html_a5fcccf6747c449418c246ac1d945a1f8"></a>
<a id="astructzperf__results_html_a8aedf97a8eeace1f4b9cda7e07e17e28"></a>
<a id="astructzperf__results_html_a9253d70cca70d2b8112bac31cca6ea2f"></a>
<a id="astructzperf__results_html_aa1e3c86bcab447bc888bba0bbaa057d1"></a>
<a id="astructzperf__results_html_aafb7f2c221c91c59ab0d6936ebc6ce2a"></a>
<a id="astructzperf__results_html_ac9ad68ef3b6081b64f290720ad9b5bc8"></a>
<a id="astructzperf__results_html_acf312d831d8e6707f7e769da92f8eb70"></a>
<a id="astructzperf__results_html_adfd2738991c8bea53f20079421da6d96"></a>
<a id="astructzperf__results_html_af4a5ce512fb37ddae8e2c12a0b67c3a2"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_ZPERF_H_
#define ZEPHYR_INCLUDE_NET_ZPERF_H_

#include <zephyr/net/net_ip.h>
#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif


enum zperf_status {
        ZPERF_SESSION_STARTED,
        ZPERF_SESSION_PERIODIC_RESULT,
        ZPERF_SESSION_FINISHED,
        ZPERF_SESSION_ERROR
} __packed;

typedef int (*zperf_data_load_custom)(void *user_ctx, uint64_t offset,
                                      uint8_t *data, uint32_t len);

struct zperf_upload_params {
        uint64_t unix_offset_us;
        zperf_data_load_custom data_loader;
        void *data_loader_ctx;
        union {
                struct net_sockaddr_storage peer_addr_storage;
                /* Use the peer_addr_storage instead of this one. */
                struct net_sockaddr peer_addr;
        };
        uint32_t duration_ms;
        uint32_t rate_kbps;
        uint16_t packet_size;
        char if_name[NET_IFNAMSIZ];
        struct {
                uint8_t tos;
                int tcp_nodelay;
                int priority;
#ifdef CONFIG_ZPERF_SESSION_PER_THREAD
                int thread_priority;
                bool wait_for_start;
#endif
                uint32_t report_interval_ms;
        } options;
};

struct zperf_download_params {
        uint16_t port;
        union {
                struct net_sockaddr_storage addr_storage;
                /* Use the addr_storage instead of this one. */
                struct net_sockaddr addr;
        };
        char if_name[NET_IFNAMSIZ];
};

#ifdef CONFIG_NET_ZPERF_RAW_TX
struct zperf_raw_upload_params {
        uint32_t duration_ms;
        uint32_t rate_kbps;
        uint16_t packet_size;
        uint8_t *hdr;
        uint16_t hdr_len;
        int if_index;
};
#endif /* CONFIG_NET_ZPERF_RAW_TX */


struct zperf_results {
        uint32_t nb_packets_sent;
        uint32_t nb_packets_rcvd;
        uint32_t nb_packets_lost;
        uint32_t nb_packets_outorder;
        uint64_t total_len;
        uint64_t time_in_us;
        uint32_t jitter_in_us;
        uint64_t client_time_in_us;
        uint32_t packet_size;
        uint32_t nb_packets_errors;
        bool is_multicast;
};

typedef void (*zperf_callback)(enum zperf_status status,
                               struct zperf_results *result,
                               void *user_data);

int zperf_udp_upload(const struct zperf_upload_params *param,
                     struct zperf_results *result);

int zperf_tcp_upload(const struct zperf_upload_params *param,
                     struct zperf_results *result);

int zperf_udp_upload_async(const struct zperf_upload_params *param,
                           zperf_callback callback, void *user_data);

int zperf_tcp_upload_async(const struct zperf_upload_params *param,
                           zperf_callback callback, void *user_data);

int zperf_udp_download(const struct zperf_download_params *param,
                       zperf_callback callback, void *user_data);

int zperf_tcp_download(const struct zperf_download_params *param,
                       zperf_callback callback, void *user_data);

int zperf_udp_download_stop(void);

int zperf_tcp_download_stop(void);

#ifdef CONFIG_NET_ZPERF_RAW_TX
int zperf_raw_upload(const struct zperf_raw_upload_params *param,
                     struct zperf_results *result);

int zperf_raw_upload_async(const struct zperf_raw_upload_params *param,
                           zperf_callback callback, void *user_data);
#endif /* CONFIG_NET_ZPERF_RAW_TX */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_ZPERF_H_ */
```

## 104.3\_源码注释译文

版权：2016年Intel Corporation、2022年Nordic Semiconductor ASA；许可标识为`Apache-2.0`。上传参数的联合体注释为：“使用`peer_addr_storage`，不要使用此成员（`peer_addr`）”；下载参数中相应注释为：“使用`addr_storage`，不要使用此成员（`addr`）”。条件编译结束注释标明`CONFIG_NET_ZPERF_RAW_TX`分支；末尾`#endif`结束包含保护`ZEPHYR_INCLUDE_NET_ZPERF_H_`。

## 104.4\_译注：源码中展示但API索引隐藏的参数

本节是明确标注的源码译注，补充[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/zperf.h)中的注释。该头文件使用`INTERNAL_HIDDEN`隐藏了一部分Doxygen条目，所以本次官方页面清单没有对应的独立参数结构页；这里不把它们另计为已完成页面。

### 自定义数据加载回调（Custom Data Load Callback）

`zperf_data_load_custom`用于加载待上传的自定义数据，其声明已完整保留在上方源码中。

| 参数 | 原始注释译文 |
| --- | --- |
| `user_ctx` | 数据加载使用的用户上下文（User Context）。 |
| `offset` | 自定义数据的当前偏移量（Current Offset）。 |
| `data` | 指向待填充数据区的指针。 |
| `len` | 要加载的数据长度，单位字节。 |

成功加载数据返回`0`；返回`-errno`表示加载失败，并终止数据上传。

### 上传和下载地址

`zperf_upload_params`中的匿名联合体（Anonymous Union）保存对端地址，`peer_addr_storage`是要上传到的对端地址（Peer Address）。`zperf_download_params`的匿名联合体保存本地地址，`addr_storage`是本地绑定地址（Local Bind Address）。两个结构均保留`if_name[NET_IFNAMSIZ]`，其余字段和条件编译布局见原始声明。

译注：对没有原始字段说明的成员，不在此补造默认值或可选规则。`duration_ms`、`rate_kbps`等成员的实际使用可对照所选协议版本的实现；`options.thread_priority`和`options.wait_for_start`仅在`CONFIG_ZPERF_SESSION_PER_THREAD`启用时存在。

### 原始发送参数（Raw TX Upload Parameters）

此结构在`CONFIG_NET_ZPERF_RAW_TX`下定义。传给驱动的缓冲区结构为“用户提供的报头（User-provided Header）＋字符`z`有效载荷（Payload）”。用户把厂商元数据、802.11／以太网等帧报头全部放入一个连续报头块，zperf再追加`z`字节，使总长度达到所需`packet_size`。此方式不绑定特定帧格式。

报头字节按提供时的内容原样发送，**不会进行字节序转换（Byte Order Conversion）**；用户必须提供目标驱动／硬件期望的格式。

| 成员 | 原始注释译文 |
| --- | --- |
| `duration_ms` | 测试持续时间，单位毫秒。 |
| `rate_kbps` | 目标速率，单位千比特每秒。 |
| `packet_size` | 总数据包大小，包含报头和有效载荷。 |
| `hdr` | 报头字节，包含厂商元数据和帧报头。 |
| `hdr_len` | 报头长度，单位字节。 |
| `if_index` | 网络接口索引（Network Interface Index）。 |

### 原始发送接口注释

`zperf_raw_upload()`执行同步原始包发送上传（Synchronous Raw Packet TX Upload），阻塞到上传完成。`param`为上传参数，包含自定义报头和目标MAC地址；`result`保存会话结果。会话成功完成返回0，否则返回负错误码。

`zperf_raw_upload_async()`执行异步原始包发送上传（Asynchronous Raw Packet TX Upload），同一时间只能有一次异步原始发送。`param`同上，`callback`是会话结果回调，`user_data`指向随回调传入的用户数据。成功安排执行返回0，否则返回负错误码。

译注：原注释中的“目标MAC地址”不是一个独立结构体成员，而是由调用者按所用帧格式放入`hdr`内容。当前[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/zperf_raw_uploader.c)会检查接口索引和报头上限；异步入口把有效的报头内容复制到内部存储，但`user_data`所指对象仍由调用者管理。使用流程见[原始发送模式](P096_zperf网络流量生成器.md#raw-tx-mode)。


[上一章](P103_zperf头文件参考.md) · [返回大纲](大纲.md) · [下一章](P105_zperf测量结果.md)
