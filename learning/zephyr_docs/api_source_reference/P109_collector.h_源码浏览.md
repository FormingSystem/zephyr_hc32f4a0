---
id: learning.zephyr-docs.api-source-reference.page-109
title: collector.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/collector_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_collector.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html)。

## 109.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00076"></a>
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
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
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
<a id="l00135"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="agroup__prometheus_html_ga1bbdd8d5447144b21d3cda1ddac38ff0"></a>
<a id="agroup__prometheus_html_ga1c70215409029bbe163bdfdb03bfba43"></a>
<a id="agroup__prometheus_html_ga4e2541cb094915187157d44a29e2d6b5"></a>
<a id="agroup__prometheus_html_ga757252a9157538870b1360924b16d0e0"></a>
<a id="agroup__prometheus_html_ga976b9e82d747570cde631b03ee805a26"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="akernel_8h_html"></a>
<a id="ametric_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__mutex_html"></a>
<a id="astructprometheus__collector_html"></a>
<a id="astructprometheus__collector_html_a050b6094f92369225dce734ef9f50476"></a>
<a id="astructprometheus__collector_html_a389528dad4e2ada62ca85650b6be5972"></a>
<a id="astructprometheus__collector_html_a43e08aa447c0388d80771c33f59992b7"></a>
<a id="astructprometheus__collector_html_acd2c684c0c920f75e86d2560b4bb29e2"></a>
<a id="astructprometheus__collector_html_ae131dcdd35fbacd30a210b547718c6be"></a>
<a id="astructprometheus__metric_html"></a>
<a id="astructprometheus__metric_html_a1138f189a5bdd44639dace426ef8f55a"></a>
<a id="astructprometheus__metric_html_a67e8d38a696f2b20a076b8da6b1250e3"></a>
<a id="astructprometheus__metric_html_ae2db853cae2c49634fda25eb23b825da"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_COLLECTOR_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_COLLECTOR_H_


#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>

#include <stddef.h>

struct prometheus_collector;

typedef int (*prometheus_scrape_cb_t)(struct prometheus_collector *collector,
                                      struct prometheus_metric *metric,
                                      void *user_data);

struct prometheus_collector {
        const char *name;
        sys_slist_t metrics;
        struct k_mutex lock;
        prometheus_scrape_cb_t user_cb;
        void *user_data;
};

#define PROMETHEUS_COLLECTOR_DEFINE(_name, ...) \
        STRUCT_SECTION_ITERABLE(prometheus_collector, _name) = {        \
                .name = STRINGIFY(_name),                               \
                .metrics = SYS_SLIST_STATIC_INIT(&_name.metrics),       \
                .lock = Z_MUTEX_INITIALIZER(_name.lock),                \
                .user_cb = COND_CODE_0(                                 \
                        NUM_VA_ARGS_LESS_1(                             \
                                LIST_DROP_EMPTY(__VA_ARGS__, _)),       \
                        (NULL),                                         \
                        (GET_ARG_N(1, __VA_ARGS__))),                   \
                .user_data = COND_CODE_0(                               \
                        NUM_VA_ARGS_LESS_1(__VA_ARGS__), (NULL),        \
                        (GET_ARG_N(1,                                   \
                                   GET_ARGS_LESS_N(1, __VA_ARGS__)))),  \
        }

int prometheus_collector_register_metric(struct prometheus_collector *collector,
                                         struct prometheus_metric *metric);

const void *prometheus_collector_get_metric(struct prometheus_collector *collector,
                                            const char *name);


enum prometheus_walk_state {
        PROMETHEUS_WALK_START,
        PROMETHEUS_WALK_CONTINUE,
        PROMETHEUS_WALK_STOP,
};

struct prometheus_collector_walk_context {
        struct prometheus_collector *collector;
        struct prometheus_metric *metric;
        struct prometheus_metric *tmp;
        enum prometheus_walk_state state;
};


int prometheus_collector_walk_metrics(struct prometheus_collector_walk_context *ctx,
                                      uint8_t *buffer, size_t buffer_size);

static inline int prometheus_collector_walk_init(struct prometheus_collector_walk_context *ctx,
                                                 struct prometheus_collector *collector)
{
        if (collector == NULL) {
                return -EINVAL;
        }

        ctx->collector = collector;
        ctx->state = PROMETHEUS_WALK_START;
        ctx->metric = NULL;
        ctx->tmp = NULL;

        return 0;
}


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_COLLECTOR_H_ */
```

## 109.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 177 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_COLLECTOR_H_`。

## 109.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [prometheus_scrape_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga4e2541cb094915187157d44a29e2d6b5)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [metric](../network_service_model_reference/P051_prometheus_metric_结构体.md#a67e8d38a696f2b20a076b8da6b1250e3)
- [user_data](../network_service_model_reference/P051_prometheus_metric_结构体.md#ae2db853cae2c49634fda25eb23b825da)
- [name](../network_service_model_reference/P045_prometheus_collector_结构体.md#a050b6094f92369225dce734ef9f50476)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [metrics](../network_service_model_reference/P045_prometheus_collector_结构体.md#a389528dad4e2ada62ca85650b6be5972)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [lock](../network_service_model_reference/P045_prometheus_collector_结构体.md#a43e08aa447c0388d80771c33f59992b7)
- [user_cb](../network_service_model_reference/P045_prometheus_collector_结构体.md#ae131dcdd35fbacd30a210b547718c6be)
- [user_data](../network_service_model_reference/P045_prometheus_collector_结构体.md#acd2c684c0c920f75e86d2560b4bb29e2)
- [prometheus_collector_register_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga976b9e82d747570cde631b03ee805a26)
- [prometheus_collector_get_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga757252a9157538870b1360924b16d0e0)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [prometheus_collector_walk_metrics](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1bbdd8d5447144b21d3cda1ddac38ff0)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [prometheus_collector_walk_init](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1c70215409029bbe163bdfdb03bfba43)
- [collector](../network_service_model_reference/P051_prometheus_metric_结构体.md#a1138f189a5bdd44639dace426ef8f55a)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_collector::name](../network_service_model_reference/P045_prometheus_collector_结构体.md#a050b6094f92369225dce734ef9f50476)
- [prometheus_collector::metrics](../network_service_model_reference/P045_prometheus_collector_结构体.md#a389528dad4e2ada62ca85650b6be5972)
- [prometheus_collector::lock](../network_service_model_reference/P045_prometheus_collector_结构体.md#a43e08aa447c0388d80771c33f59992b7)
- [prometheus_collector::user_data](../network_service_model_reference/P045_prometheus_collector_结构体.md#acd2c684c0c920f75e86d2560b4bb29e2)
- [prometheus_collector::user_cb](../network_service_model_reference/P045_prometheus_collector_结构体.md#ae131dcdd35fbacd30a210b547718c6be)
- [prometheus_metric::collector](../network_service_model_reference/P051_prometheus_metric_结构体.md#a1138f189a5bdd44639dace426ef8f55a)
- [prometheus_metric::metric](../network_service_model_reference/P051_prometheus_metric_结构体.md#a67e8d38a696f2b20a076b8da6b1250e3)
- [prometheus_metric::user_data](../network_service_model_reference/P051_prometheus_metric_结构体.md#ae2db853cae2c49634fda25eb23b825da)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P108_coap_oscore.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P110_common-dma.h_源码浏览.md)
