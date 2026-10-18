---
id: learning.zephyr-docs.api-source-reference.page-681
title: ptp_time.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第681章\_ptp\_time.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)。

## 681.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
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
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="agroup__clock__apis_html_ga0501e82515b2bdf36453c4cc80f5e0cc"></a>
<a id="agroup__net__time_html_ga38c90d968fc905093de2db057e6fa199"></a>
<a id="agroup__net__time_html_gabcd93249b790bea7ed6f8aab9ebe568a"></a>
<a id="agroup__net__time_html_gaf1da332e3909fca30de991cc2f950e56"></a>
<a id="agroup__ptp__time_html_gaf9f253990e644e161e1b3cc317e8e9e9"></a>
<a id="agroup__ptp__time_html_gafd9d45cca3d630ce51109537165d53df"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__time_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructnet__ptp__extended__time_html"></a>
<a id="astructnet__ptp__extended__time_html_a94ec079b5d38fcd12ec54baf707ec587"></a>
<a id="astructnet__ptp__extended__time_html_a97b1711e17fa229bab129da4148c3e55"></a>
<a id="astructnet__ptp__time_html"></a>
<a id="astructnet__ptp__time_html_a31af3f0b8f924336c17585ee1b15ee0e"></a>
<a id="astructnet__ptp__time_html_a8d61359ca53147d2da761edeb9e1ab04"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_PTP_TIME_H_
#define ZEPHYR_INCLUDE_NET_PTP_TIME_H_


#include <zephyr/net/net_core.h>
#include <zephyr/net/net_time.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

struct net_ptp_time {
        union {

                struct {
#ifdef CONFIG_LITTLE_ENDIAN
                        uint32_t low;
                        uint16_t high;
                        uint16_t unused;
#else
                        uint16_t unused;
                        uint16_t high;
                        uint32_t low;
#endif
                } _sec;

                uint64_t second;
        };

        uint32_t nanosecond;
};

#ifdef __cplusplus
}
#endif

struct net_ptp_extended_time {
        union {

                struct {
#ifdef CONFIG_LITTLE_ENDIAN
                        uint32_t low;
                        uint16_t high;
                        uint16_t unused;
#else
                        uint16_t unused;
                        uint16_t high;
                        uint32_t low;
#endif
                } _sec;

                uint64_t second;
        };

        union {

                struct {
#ifdef CONFIG_LITTLE_ENDIAN
                        uint32_t low;
                        uint16_t high;
                        uint16_t unused;
#else
                        uint16_t unused;
                        uint16_t high;
                        uint32_t low;
#endif
                } _fns;

                uint64_t fract_nsecond;
        };
} __packed;

static inline net_time_t net_ptp_time_to_ns(struct net_ptp_time *ts)
{
        if (!ts) {
                return 0;
        }

        if (ts->second >= NET_TIME_SEC_MAX) {
                return NET_TIME_MAX;
        }

        return ((int64_t)ts->second * NSEC_PER_SEC) + ts->nanosecond;
}

static inline struct net_ptp_time ns_to_net_ptp_time(net_time_t nsec)
{
        struct net_ptp_time ts;

        __ASSERT_NO_MSG(nsec >= 0);

        ts.second = nsec / NSEC_PER_SEC;
        ts.nanosecond = nsec % NSEC_PER_SEC;
        return ts;
}


#endif /* ZEPHYR_INCLUDE_NET_PTP_TIME_H_ */
```

## 681.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 246 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PTP_TIME_H_`。

## 681.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [zephyr/net/net_time.h](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [second](../network_core_model_reference/P116_net_ptp_time_结构体.md#a8d61359ca53147d2da761edeb9e1ab04)
- [nanosecond](../network_core_model_reference/P116_net_ptp_time_结构体.md#a31af3f0b8f924336c17585ee1b15ee0e)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [second](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md#a97b1711e17fa229bab129da4148c3e55)
- [fract_nsecond](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md#a94ec079b5d38fcd12ec54baf707ec587)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [net_ptp_time_to_ns](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gaf9f253990e644e161e1b3cc317e8e9e9)
- [NET_TIME_SEC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gabcd93249b790bea7ed6f8aab9ebe568a)
- [NET_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga38c90d968fc905093de2db057e6fa199)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [ns_to_net_ptp_time](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gafd9d45cca3d630ce51109537165d53df)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [net_time.h](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)
- [net_ptp_extended_time::fract_nsecond](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md#a94ec079b5d38fcd12ec54baf707ec587)
- [net_ptp_extended_time::second](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md#a97b1711e17fa229bab129da4148c3e55)
- [net_ptp_time::nanosecond](../network_core_model_reference/P116_net_ptp_time_结构体.md#a31af3f0b8f924336c17585ee1b15ee0e)
- [net_ptp_time::second](../network_core_model_reference/P116_net_ptp_time_结构体.md#a8d61359ca53147d2da761edeb9e1ab04)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P680_ptp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P682_max2221x.h_源码浏览.md)
