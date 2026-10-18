---
id: learning.zephyr-docs.api-source-supplement-reference.page-145
title: pipe.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第145章\_pipe.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)。

## 145.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00025"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
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
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00231"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00271"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="afcntl_8h_html_ac843f2e35e60c3bbf1da47d84306f29b"></a>
<a id="agroup__modem__pipe_html_ga0a7312eadaa76b433fe8a319d8c9ec74"></a>
<a id="agroup__modem__pipe_html_ga4f5d30e87bb252c4e38ce2e3b10e78c5"></a>
<a id="agroup__modem__pipe_html_ga68674becf672b1009d629813c041b868"></a>
<a id="agroup__modem__pipe_html_ga7521ac0aeda8027c47741237e8312bf0"></a>
<a id="agroup__modem__pipe_html_ga9814c9a1a5da33b2787ac058a6a037f5"></a>
<a id="agroup__modem__pipe_html_gab030b4040725ad4dab2399840ef73fde"></a>
<a id="agroup__modem__pipe_html_gab1f1a3a37779900730c5ffad1aea3c7c"></a>
<a id="agroup__modem__pipe_html_gab9dd98d92d6446dd43852d280574f67a"></a>
<a id="agroup__modem__pipe_html_gad181c9ee83b2294fb3fd16b690660926"></a>
<a id="agroup__modem__pipe_html_gad1a9fa3dba49a86c187328b7ee022293"></a>
<a id="agroup__modem__pipe_html_gaf64941177c179cb9086a5736d1ea56f1"></a>
<a id="agroup__modem__pipe_html_ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4"></a>
<a id="agroup__modem__pipe_html_ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891"></a>
<a id="agroup__modem__pipe_html_ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4"></a>
<a id="agroup__modem__pipe_html_ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmodem__pipe__data__fragment_html"></a>
<a id="astructmodem__pipe__data__fragment_html_a15f0c5d1e9838a583e66da62bf42bb96"></a>
<a id="astructmodem__pipe__data__fragment_html_a74684f59922bbd7f6a75da01c1558661"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/types.h>
#include <zephyr/kernel.h>

#ifndef ZEPHYR_INCLUDE_MODEM_PIPE_H_
#define ZEPHYR_INCLUDE_MODEM_PIPE_H_

#ifdef __cplusplus
extern "C" {
#endif


enum modem_pipe_event {
        MODEM_PIPE_EVENT_OPENED = 0,
        MODEM_PIPE_EVENT_RECEIVE_READY,
        MODEM_PIPE_EVENT_TRANSMIT_IDLE,
        MODEM_PIPE_EVENT_CLOSED,
};

struct modem_pipe_data_fragment {
        const uint8_t *data;
        size_t size;
};


struct modem_pipe;


typedef void (*modem_pipe_api_callback)(struct modem_pipe *pipe, enum modem_pipe_event event,
                                        void *user_data);


typedef int (*modem_pipe_api_open)(void *data);

typedef int (*modem_pipe_api_transmit)(void *data, const uint8_t *buf, size_t size);

typedef int (*modem_pipe_api_transmit_chain)(void *data,
                                             const struct modem_pipe_data_fragment *frags,
                                             size_t num_frags);

typedef int (*modem_pipe_api_receive)(void *data, uint8_t *buf, size_t size);

typedef int (*modem_pipe_api_close)(void *data);

struct modem_pipe_api {
        modem_pipe_api_open open;
        /* Only one of 'transmit' and 'transmit_chain' needs to be implemented */
        modem_pipe_api_transmit transmit;
        modem_pipe_api_transmit_chain transmit_chain;
        modem_pipe_api_receive receive;
        modem_pipe_api_close close;
};

struct modem_pipe {
        void *data;
        const struct modem_pipe_api *api;
        modem_pipe_api_callback callback;
        void *user_data;
        struct k_spinlock spinlock;
        struct k_event event;
};

void modem_pipe_init(struct modem_pipe *pipe, void *data, const struct modem_pipe_api *api);


int modem_pipe_open(struct modem_pipe *pipe, k_timeout_t timeout);

int modem_pipe_open_async(struct modem_pipe *pipe);

void modem_pipe_attach(struct modem_pipe *pipe, modem_pipe_api_callback callback, void *user_data);

int modem_pipe_transmit_chain(struct modem_pipe *pipe, const struct modem_pipe_data_fragment *frags,
                              size_t num_frags);

static inline int modem_pipe_transmit(struct modem_pipe *pipe, const uint8_t *buf, size_t size)
{
        const struct modem_pipe_data_fragment frag = {
                .data = buf,
                .size = size,
        };

        return modem_pipe_transmit_chain(pipe, &frag, 1);
}

int modem_pipe_receive(struct modem_pipe *pipe, uint8_t *buf, size_t size);

void modem_pipe_release(struct modem_pipe *pipe);

int modem_pipe_close(struct modem_pipe *pipe, k_timeout_t timeout);

int modem_pipe_close_async(struct modem_pipe *pipe);


void modem_pipe_notify_opened(struct modem_pipe *pipe);

void modem_pipe_notify_closed(struct modem_pipe *pipe);

void modem_pipe_notify_receive_ready(struct modem_pipe *pipe);

void modem_pipe_notify_transmit_idle(struct modem_pipe *pipe);



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_PIPE_H_ */
```

## 145.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

只需实现 `transmit` 和 `transmit_chain` 中的一个。

### 注释 3：原第 280 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_PIPE_H_`。

## 145.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [modem_pipe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab9dd98d92d6446dd43852d280574f67a)
- [MODEM_PIPE_EVENT_OPENED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891)
- [MODEM_PIPE_EVENT_RECEIVE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4)
- [MODEM_PIPE_EVENT_TRANSMIT_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4)
- [MODEM_PIPE_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f)
- [modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md#a15f0c5d1e9838a583e66da62bf42bb96)
- [size](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md#a74684f59922bbd7f6a75da01c1558661)
- [modem_pipe_api_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gaf64941177c179cb9086a5736d1ea56f1)
- [open](https://docs.zephyrproject.org/latest/doxygen/html/fcntl_8h.html#ac843f2e35e60c3bbf1da47d84306f29b)
- [modem_pipe_open](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga7521ac0aeda8027c47741237e8312bf0)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [modem_pipe_open_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga0a7312eadaa76b433fe8a319d8c9ec74)
- [modem_pipe_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga68674becf672b1009d629813c041b868)
- [modem_pipe_transmit_chain](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad181c9ee83b2294fb3fd16b690660926)
- [modem_pipe_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab1f1a3a37779900730c5ffad1aea3c7c)
- [modem_pipe_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab030b4040725ad4dab2399840ef73fde)
- [modem_pipe_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad1a9fa3dba49a86c187328b7ee022293)
- [modem_pipe_close](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga4f5d30e87bb252c4e38ce2e3b10e78c5)
- [modem_pipe_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga9814c9a1a5da33b2787ac058a6a037f5)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [modem_pipe_data_fragment::data](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md#a15f0c5d1e9838a583e66da62bf42bb96)
- [modem_pipe_data_fragment::size](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md#a74684f59922bbd7f6a75da01c1558661)

---

[上一章](P144_pinctrl-rzt-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P146_policy.h_源码浏览.md)
