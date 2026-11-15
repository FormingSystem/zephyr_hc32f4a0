---
id: learning.zephyr-docs.api-source-architecture-reference.page-10
title: common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)。

## 10.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00140"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="foldopen00164"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__ssh__common_html_ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e"></a>
<a id="agroup__ssh__common_html_ga1e8ec722a451a466904d077fd4b22a16"></a>
<a id="agroup__ssh__common_html_ga3f29b8eb5acf4b91aeb07873b2df7d56"></a>
<a id="agroup__ssh__common_html_ga41ef319c12ce50fe226152eb654a6d56"></a>
<a id="agroup__ssh__common_html_ga52f058c2b51df404b9399f8188dcfe8d"></a>
<a id="agroup__ssh__common_html_ga578aed0a10600bc7a248dbb64ca13cc2"></a>
<a id="agroup__ssh__common_html_ga5832386d60c9fdd46c2198b45905be73"></a>
<a id="agroup__ssh__common_html_ga5e0d58687f17df1f5c2480ceadcbde72"></a>
<a id="agroup__ssh__common_html_ga6205c8f8d3fd6f0c457261d6cf355940"></a>
<a id="agroup__ssh__common_html_ga658c9f84ec08797b50fb57e2415f7e3d"></a>
<a id="agroup__ssh__common_html_ga691a9ba0d4c2bb1cf637990a4aa91f26"></a>
<a id="agroup__ssh__common_html_ga6c8271f6fe11a5779a7f05a232c28d84"></a>
<a id="agroup__ssh__common_html_ga7c510e44353e7e791c8f13af3a554739"></a>
<a id="agroup__ssh__common_html_ga7fa2613a763415d19c9c6e7926ead074"></a>
<a id="agroup__ssh__common_html_ga9341ecffa2ca568ed8312b7c7bd5b416"></a>
<a id="agroup__ssh__common_html_ga9f6f03ef86ffee24da6e7fb6adc82878"></a>
<a id="agroup__ssh__common_html_gaa3b9133aff9d5be3b258db48ba99b601"></a>
<a id="agroup__ssh__common_html_gaba3db037a1fbeca22f2c3c30063788b9"></a>
<a id="agroup__ssh__common_html_gaed450ebb53a676fafc58bb6cfe82a448"></a>
<a id="agroup__ssh__common_html_gaf53f661268138d4a36875fb079983c2a"></a>
<a id="agroup__ssh__common_html_gafb6780adc3007639184e634f1a7ec73a"></a>
<a id="agroup__ssh__common_html_gaff36f18836543d259ee7420bdb757e1f"></a>
<a id="agroup__ssh__common_html_gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a"></a>
<a id="agroup__ssh__common_html_gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3"></a>
<a id="agroup__ssh__common_html_gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8"></a>
<a id="agroup__ssh__common_html_gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9"></a>
<a id="agroup__ssh__common_html_gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd"></a>
<a id="agroup__ssh__common_html_gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe"></a>
<a id="agroup__ssh__common_html_gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5"></a>
<a id="agroup__ssh__common_html_gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e"></a>
<a id="agroup__ssh__common_html_ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32"></a>
<a id="akernel_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructssh__channel__event__channel__request__result_html"></a>
<a id="astructssh__channel__event__channel__request__result_html_aa613a72ee7051b656fbfee2cb7bba465"></a>
<a id="astructssh__channel__event__channel__request_html"></a>
<a id="astructssh__channel__event__channel__request_html_a34c82071311d8c41cbecd387bece4620"></a>
<a id="astructssh__channel__event__channel__request_html_a36caf063cc61ad622c74d9a7d3c8053c"></a>
<a id="astructssh__channel__event_html"></a>
<a id="astructssh__channel__event_html_a3d6ac4601d29b26a437866f5c58360c8"></a>
<a id="astructssh__channel__event_html_a5177c6f41210417205ceaab1c366390b"></a>
<a id="astructssh__channel__event_html_ac66cc9b82e394c6b51c4e54620351f1b"></a>
<a id="astructssh__transport__conf_html"></a>
<a id="astructssh__transport__conf_html_a00639f5bd1d033d60279f32026293b33"></a>
<a id="astructssh__transport__conf_html_a769d50cabe9a88cc14df0cb47203fd32"></a>
<a id="astructssh__transport__conf_html_a84db4c215eed55af55cf9a8d95a08599"></a>
<a id="astructssh__transport__event__authenticate__result_html"></a>
<a id="astructssh__transport__event__authenticate__result_html_a2cd0258828b4c18155fde2c502fff46c"></a>
<a id="astructssh__transport__event__channel__open_html"></a>
<a id="astructssh__transport__event__channel__open_html_aa996fe128fd859c73e4125311e7f436c"></a>
<a id="astructssh__transport__event_html"></a>
<a id="astructssh__transport__event_html_a2a244666ec5be86351c7099fabc2f7b5"></a>
<a id="astructssh__transport__event_html_abb671e903a0e2d6492719f2cff1b29fd"></a>
<a id="astructssh__transport__event_html_afa47dba4ec00ab1a2dfb6ae6c57fe498"></a>

```c
/*
 * Copyright (c) 2024 Grant Ramsay <grant.ramsay@hotmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SSH_COMMON_H_
#define ZEPHYR_INCLUDE_NET_SSH_COMMON_H_


#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif


struct ssh_transport;
struct ssh_channel;
struct ssh_client;
struct ssh_server;


enum ssh_auth_type {
        SSH_AUTH_NONE,
        SSH_AUTH_PASSWORD,
        SSH_AUTH_PUBKEY
};

enum ssh_channel_request_type {
        SSH_CHANNEL_REQUEST_UNKNOWN,
        SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL,
        SSH_CHANNEL_REQUEST_X11_FORWARD,
        SSH_CHANNEL_REQUEST_ENV_VAR,
        SSH_CHANNEL_REQUEST_SHELL,
        SSH_CHANNEL_REQUEST_EXEC,
        SSH_CHANNEL_REQUEST_SUBSYSTEM,
        SSH_CHANNEL_REQUEST_WINDOW_CHANGE,
        SSH_CHANNEL_REQUEST_FLOW_CONTROL,
        SSH_CHANNEL_REQUEST_SIGNAL,
        SSH_CHANNEL_REQUEST_EXIT_STATUS,
        SSH_CHANNEL_REQUEST_EXIT_SIGNAL
};

enum ssh_channel_event_type {
        SSH_CHANNEL_EVENT_OPEN_RESULT,          /* Client only */
        SSH_CHANNEL_EVENT_REQUEST,              /* Server only */
        SSH_CHANNEL_EVENT_REQUEST_RESULT,       /* Client only */
        SSH_CHANNEL_EVENT_RX_DATA_READY,
        SSH_CHANNEL_EVENT_TX_DATA_READY,
        SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY,
        SSH_CHANNEL_EVENT_EOF,
        SSH_CHANNEL_EVENT_CLOSED
};

struct ssh_channel_event_channel_request {
        enum ssh_channel_request_type type;
        bool want_reply;
        /* TODO: Union of request type data */
};

struct ssh_channel_event_channel_request_result {
        bool success;
};

struct ssh_channel_event {
        enum ssh_channel_event_type type;

        union {
                struct ssh_channel_event_channel_request channel_request;

                struct ssh_channel_event_channel_request_result channel_request_result;
        };
};

typedef int (*ssh_channel_event_callback_t)(struct ssh_channel *channel,
                                            const struct ssh_channel_event *event,
                                            void *user_data);

enum ssh_transport_event_type {
        SSH_TRANSPORT_EVENT_CLOSED,                     /* Server and client */
        SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED,           /* Client only */
        SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT,        /* Client only */
        SSH_TRANSPORT_EVENT_CHANNEL_OPEN,               /* Server only */
};

struct ssh_transport_event_authenticate_result {
        bool success;
};

struct ssh_transport_event_channel_open {
        struct ssh_channel *channel;
};

struct ssh_transport_event {
        enum ssh_transport_event_type type;

        union {
                struct ssh_transport_event_authenticate_result authenticate_result;

                struct ssh_transport_event_channel_open channel_open;
        };
};

typedef int (*ssh_transport_event_callback_t)(struct ssh_transport *transport,
                                              const struct ssh_transport_event *event,
                                              void *user_data);

struct ssh_transport_conf {
        sys_snode_t node;

        ssh_transport_event_callback_t cb;

        void *user_data;
};

#define SSH_EXTENDED_DATA_STDERR 1

#if defined(CONFIG_SSH_CLIENT) || defined(__DOXYGEN__)
const char *ssh_transport_client_user_name(struct ssh_transport *transport);

int ssh_transport_auth_password(struct ssh_transport *transport, const char *user_name,
                                const char *password);

int ssh_transport_channel_open(struct ssh_transport *transport,
                               ssh_channel_event_callback_t callback, void *user_data);

#endif /* CONFIG_SSH_CLIENT || __DOXYGEN__ */

#if defined(CONFIG_SSH_SERVER) || defined(__DOXYGEN__)
int ssh_channel_open_result(struct ssh_channel *channel, bool success,
                            ssh_channel_event_callback_t callback, void *user_data);

#endif /* CONFIG_SSH_SERVER || __DOXYGEN__ */

int ssh_channel_request_result(struct ssh_channel *channel, bool success);

#if defined(CONFIG_SSH_CLIENT) || defined(__DOXYGEN__)
int ssh_channel_request_shell(struct ssh_channel *channel);

#endif /* CONFIG_SSH_CLIENT || __DOXYGEN__ */

int ssh_channel_read(struct ssh_channel *channel, void *data, uint32_t len);

int ssh_channel_write(struct ssh_channel *channel, const void *data, uint32_t len);

int ssh_channel_read_stderr(struct ssh_channel *channel, void *data, uint32_t len);

int ssh_channel_write_stderr(struct ssh_channel *channel, const void *data, uint32_t len);

int ssh_channel_close(struct ssh_channel *channel);

typedef void (*ssh_service_client_cb_t)(struct ssh_client *ssh,
                                        int instance,
                                        void *user_data);

void ssh_client_foreach(ssh_service_client_cb_t cb, void *user_data);

typedef void (*ssh_service_server_cb_t)(struct ssh_server *sshd,
                                        int instance,
                                        void *user_data);

void ssh_server_foreach(ssh_service_server_cb_t cb, void *user_data);

int ssh_transport_traverse_callbacks(bool is_server, struct ssh_transport *transport,
                                     const struct ssh_transport_event *event);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SSH_COMMON_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Grant Ramsay <grant.ramsay@hotmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

仅客户端（Client Only）。

### 注释 3：原第 81 行

仅服务器（Server Only）。

### 注释 4：原第 83 行

仅客户端（Client Only）。

### 注释 5：原第 102 行

待办（TODO）：请求类型数据的联合体（Union of Request Type Data）。

### 注释 6：原第 142 行

服务器和客户端（Server and Client）。

### 注释 7：原第 144 行

仅客户端（Client Only）。

### 注释 8：原第 146 行

仅客户端（Client Only）。

### 注释 9：原第 148 行

仅服务器（Server Only）。

### 注释 10：原第 242 行

条件编译（Conditional Compilation）：`CONFIG_SSH_CLIENT || __DOXYGEN__`。

### 注释 11：原第 258 行

条件编译（Conditional Compilation）：`CONFIG_SSH_SERVER || __DOXYGEN__`。

### 注释 12：原第 280 行

条件编译（Conditional Compilation）：`CONFIG_SSH_CLIENT || __DOXYGEN__`。

### 注释 13：原第 410 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SSH_COMMON_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [ssh_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6c8271f6fe11a5779a7f05a232c28d84)
- [SSH_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a4c56e47dd4c89942b806e7184b48c8fd)
- [SSH_AUTH_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84a7d995a7868d2d2f81e9dd2f898b206fe)
- [SSH_AUTH_PUBKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga6c8271f6fe11a5779a7f05a232c28d84aeec2aef5993361fe298ffd92d9563314)
- [ssh_channel_request_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9341ecffa2ca568ed8312b7c7bd5b416)
- [SSH_CHANNEL_REQUEST_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a0046e239fac55753a05147c155f4cf1f)
- [SSH_CHANNEL_REQUEST_PSEUDO_TERMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a37f4ebcc1e59b7413458b75838460622)
- [SSH_CHANNEL_REQUEST_X11_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a75809ff887a0373b86d1a49cb81d02db)
- [SSH_CHANNEL_REQUEST_ENV_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ada3d5d495a62cf99c27bb3e2f6360de5)
- [SSH_CHANNEL_REQUEST_SHELL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416aca5d52bf516565bc9fb2666a3d6c0b40)
- [SSH_CHANNEL_REQUEST_EXEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ab78296fe37945413a2727372c76e768c)
- [SSH_CHANNEL_REQUEST_SUBSYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a964401cae19320cf49318962b77aa06d)
- [SSH_CHANNEL_REQUEST_WINDOW_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416adb526a7c5e497b51c72942232e9f1952)
- [SSH_CHANNEL_REQUEST_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a1119c7871d2b156a9f47bda89eb9c1b0)
- [SSH_CHANNEL_REQUEST_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416acf84906e04b17ae6430cbfb96b14e2a0)
- [SSH_CHANNEL_REQUEST_EXIT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416a4be192de45eb272824567a72f9fd9378)
- [SSH_CHANNEL_REQUEST_EXIT_SIGNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga9341ecffa2ca568ed8312b7c7bd5b416ac6e508f3566f55dce5fe0d20e5d046a0)
- [ssh_channel_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaba3db037a1fbeca22f2c3c30063788b9)
- [SSH_CHANNEL_EVENT_OPEN_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5875ec98eac3ac29781f6f2471986ced)
- [SSH_CHANNEL_EVENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a5ab7f59edd7506de92fb67f279b6d611)
- [SSH_CHANNEL_EVENT_REQUEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a547182e5e03c4f931f81ba4945515330)
- [SSH_CHANNEL_EVENT_RX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a8f12e0a3a5193c5e5cba331074abff1f)
- [SSH_CHANNEL_EVENT_TX_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9ae7617ba17f2cc708b3c8f7e7fc4eaf32)
- [SSH_CHANNEL_EVENT_RX_STDERR_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9a3ceced60c0d06e5f9df4f54b002d5249)
- [SSH_CHANNEL_EVENT_EOF](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9abc5159ae9d6dc4f6ce9e446d4c82aba2)
- [SSH_CHANNEL_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ggaba3db037a1fbeca22f2c3c30063788b9acc6034514b2221d95b0943925816165e)
- [ssh_channel_event_channel_request](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md)
- [type](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md#a36caf063cc61ad622c74d9a7d3c8053c)
- [want_reply](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md#a34c82071311d8c41cbecd387bece4620)
- [ssh_channel_event_channel_request_result](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md)
- [success](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md#aa613a72ee7051b656fbfee2cb7bba465)
- [ssh_channel_event](../network_service_model_reference/P058_ssh_channel_event_结构体.md)
- [type](../network_service_model_reference/P058_ssh_channel_event_结构体.md#a3d6ac4601d29b26a437866f5c58360c8)
- [channel_request](../network_service_model_reference/P058_ssh_channel_event_结构体.md#ac66cc9b82e394c6b51c4e54620351f1b)
- [channel_request_result](../network_service_model_reference/P058_ssh_channel_event_结构体.md#a5177c6f41210417205ceaab1c366390b)
- [ssh_channel_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga3f29b8eb5acf4b91aeb07873b2df7d56)
- [ssh_transport_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga578aed0a10600bc7a248dbb64ca13cc2)
- [SSH_TRANSPORT_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a75fcdde91f09ec0599575054300d90e8)
- [SSH_TRANSPORT_EVENT_SERVICE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a72f7351ace863e48a150a67daee364f3)
- [SSH_TRANSPORT_EVENT_AUTHENTICATE_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2a2264e7a3cafd2a7e90e61232e8b9604a)
- [SSH_TRANSPORT_EVENT_CHANNEL_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gga578aed0a10600bc7a248dbb64ca13cc2afb8adfb3fd445e92d74a93f3ec0663c9)
- [ssh_transport_event_authenticate_result](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md)
- [success](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md#a2cd0258828b4c18155fde2c502fff46c)
- [ssh_transport_event_channel_open](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md)
- [channel](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md#aa996fe128fd859c73e4125311e7f436c)
- [ssh_transport_event](../network_service_model_reference/P065_ssh_transport_event_结构体.md)
- [type](../network_service_model_reference/P065_ssh_transport_event_结构体.md#afa47dba4ec00ab1a2dfb6ae6c57fe498)
- [authenticate_result](../network_service_model_reference/P065_ssh_transport_event_结构体.md#abb671e903a0e2d6492719f2cff1b29fd)
- [channel_open](../network_service_model_reference/P065_ssh_transport_event_结构体.md#a2a244666ec5be86351c7099fabc2f7b5)
- [ssh_transport_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaed450ebb53a676fafc58bb6cfe82a448)
- [ssh_transport_conf](../network_service_model_reference/P064_ssh_transport_conf_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a84db4c215eed55af55cf9a8d95a08599)
- [cb](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a769d50cabe9a88cc14df0cb47203fd32)
- [user_data](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a00639f5bd1d033d60279f32026293b33)
- [ssh_transport_client_user_name](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga691a9ba0d4c2bb1cf637990a4aa91f26)
- [ssh_transport_auth_password](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaa3b9133aff9d5be3b258db48ba99b601)
- [ssh_transport_channel_open](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga1e8ec722a451a466904d077fd4b22a16)
- [ssh_channel_open_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga0b5e3b8f5deb399aa8d94b1e1f1e0c3e)
- [ssh_channel_request_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5832386d60c9fdd46c2198b45905be73)
- [ssh_channel_request_shell](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga52f058c2b51df404b9399f8188dcfe8d)
- [ssh_channel_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga6205c8f8d3fd6f0c457261d6cf355940)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ssh_channel_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga658c9f84ec08797b50fb57e2415f7e3d)
- [ssh_channel_read_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga5e0d58687f17df1f5c2480ceadcbde72)
- [ssh_channel_write_stderr](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7fa2613a763415d19c9c6e7926ead074)
- [ssh_channel_close](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7c510e44353e7e791c8f13af3a554739)
- [ssh_service_client_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga9f6f03ef86ffee24da6e7fb6adc82878)
- [ssh_client_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gafb6780adc3007639184e634f1a7ec73a)
- [ssh_service_server_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaf53f661268138d4a36875fb079983c2a)
- [ssh_server_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaff36f18836543d259ee7420bdb757e1f)
- [ssh_transport_traverse_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga41ef319c12ce50fe226152eb654a6d56)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [ssh_channel_event_channel_request_result::success](../network_service_model_reference/P060_ssh_channel_event_channel_request_result_结构体.md#aa613a72ee7051b656fbfee2cb7bba465)
- [ssh_channel_event_channel_request::want_reply](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md#a34c82071311d8c41cbecd387bece4620)
- [ssh_channel_event_channel_request::type](../network_service_model_reference/P059_ssh_channel_event_channel_request_结构体.md#a36caf063cc61ad622c74d9a7d3c8053c)
- [ssh_channel_event::type](../network_service_model_reference/P058_ssh_channel_event_结构体.md#a3d6ac4601d29b26a437866f5c58360c8)
- [ssh_channel_event::channel_request_result](../network_service_model_reference/P058_ssh_channel_event_结构体.md#a5177c6f41210417205ceaab1c366390b)
- [ssh_channel_event::channel_request](../network_service_model_reference/P058_ssh_channel_event_结构体.md#ac66cc9b82e394c6b51c4e54620351f1b)
- [ssh_transport_conf::user_data](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a00639f5bd1d033d60279f32026293b33)
- [ssh_transport_conf::cb](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a769d50cabe9a88cc14df0cb47203fd32)
- [ssh_transport_conf::node](../network_service_model_reference/P064_ssh_transport_conf_结构体.md#a84db4c215eed55af55cf9a8d95a08599)
- [ssh_transport_event_authenticate_result::success](../network_service_model_reference/P066_ssh_transport_event_authenticate_result_结构体.md#a2cd0258828b4c18155fde2c502fff46c)
- [ssh_transport_event_channel_open::channel](../network_service_model_reference/P067_ssh_transport_event_channel_open_结构体.md#aa996fe128fd859c73e4125311e7f436c)
- [ssh_transport_event::channel_open](../network_service_model_reference/P065_ssh_transport_event_结构体.md#a2a244666ec5be86351c7099fabc2f7b5)
- [ssh_transport_event::authenticate_result](../network_service_model_reference/P065_ssh_transport_event_结构体.md#abb671e903a0e2d6492719f2cff1b29fd)
- [ssh_transport_event::type](../network_service_model_reference/P065_ssh_transport_event_结构体.md#afa47dba4ec00ab1a2dfb6ae6c57fe498)

---

[上一章](P009_grove_lcd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_mm.h_源码浏览.md)
