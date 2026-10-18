---
id: learning.zephyr-docs.api-source-device-reference.page-27
title: net_pkt_filter.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_net\_pkt\_filter.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html)。

## 27.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00026"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
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
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
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
<a id="l00074"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
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
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="foldopen00287"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="foldopen00302"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="foldopen00332"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="foldopen00359"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="foldopen00392"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="foldopen00451"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00471"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="foldopen00497"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="foldopen00517"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="foldopen00537"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="foldopen00578"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="foldopen00599"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00623"></a>
<a id="foldopen00630"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="foldopen00645"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="foldopen00661"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="foldopen00677"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00710"></a>
<a id="foldopen00718"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="foldopen00729"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__ip__4__6_html_gae87ef466e77ded673ed7e593d3eddffd"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__pkt__filter_html_ga3b2a85558b6756e76760d9a40c780e28"></a>
<a id="agroup__net__pkt__filter_html_ga4d7426db901debff35e1de5805e06c71"></a>
<a id="agroup__net__pkt__filter_html_ga54916eb4943e4b47cd31eb23827d0dd5"></a>
<a id="agroup__net__pkt__filter_html_ga571e9fb34eb4e3cbf38f885b5e786021"></a>
<a id="agroup__net__pkt__filter_html_ga8017a041d3168c76e39bdfac011b9315"></a>
<a id="agroup__net__pkt__filter_html_ga8fc592feedeceb5172f8747a29697dd7"></a>
<a id="agroup__net__pkt__filter_html_ga9714529658625e906264a46ad1a9be6f"></a>
<a id="agroup__net__pkt__filter_html_gaac489d75c023952243589cba7ff7367a"></a>
<a id="agroup__net__pkt__filter_html_gab91ca81aab2da48066538d72caf0c8ae"></a>
<a id="agroup__net__pkt__filter_html_gad521d7ac3270970833aec48d8a517d85"></a>
<a id="agroup__net__pkt__filter_html_gadfa956e4af3c45460846fc22f863e697"></a>
<a id="agroup__npf__eth__cond_html_ga188b9d73f47a77ce05d728250606e7ec"></a>
<a id="agroup__npf__eth__cond_html_ga673493f74227912cf8f5827a77af012f"></a>
<a id="agroup__npf__eth__cond_html_ga7522a5a2188f7afbdc1a0528782ce0ef"></a>
<a id="agroup__npf__eth__cond_html_gaad4624a8e6c9491572e2a89739304530"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc"></a>
<a id="agroup__npf__eth__cond_html_ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_gae67ffe50e848951dbde309ed569ea925"></a>
<a id="alimits_8h_html"></a>
<a id="aminmax_8h_html_ac6afabdc09a49a433ee19d8a9486056d"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>
<a id="anet__core_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructnet__eth__addr_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnpf__rule__list_html"></a>
<a id="astructnpf__rule__list_html_ab6aadf2d3479853c28e94972e7862931"></a>
<a id="astructnpf__rule__list_html_af4d539d930acb257b1496761219d26cd"></a>
<a id="astructnpf__rule_html"></a>
<a id="astructnpf__rule_html_a06045c693cf06e6ebfc5a74b8c3f5ef7"></a>
<a id="astructnpf__rule_html_a3691e7be04a2948f0c979305f48fbb2c"></a>
<a id="astructnpf__rule_html_a72c032c55535c82f365b2cd1229cb1e0"></a>
<a id="astructnpf__rule_html_a872daf53310dd8e20477eafd6808481f"></a>
<a id="astructnpf__rule_html_ad5ae58fbcee5112e2defde1d7f4320dc"></a>
<a id="astructnpf__test_html"></a>
<a id="astructnpf__test_html_ac49921514690a71986ca4d07245cfe7d"></a>

```c


/*
 * Copyright (c) 2021 BayLibre SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_PKT_FILTER_H_
#define ZEPHYR_INCLUDE_NET_NET_PKT_FILTER_H_

#include <limits.h>
#include <stdbool.h>
#include <zephyr/sys/slist.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/ethernet.h>

#ifdef __cplusplus
extern "C" {
#endif



struct npf_test;

typedef bool (npf_test_fn_t)(struct npf_test *test, struct net_pkt *pkt);

enum npf_test_type {
        NPF_TEST_TYPE_UNKNOWN = 0,
        NPF_TEST_TYPE_IFACE_MATCH,
        NPF_TEST_TYPE_IFACE_UNMATCH,
        NPF_TEST_TYPE_ORIG_IFACE_MATCH,
        NPF_TEST_TYPE_ORIG_IFACE_UNMATCH,
        NPF_TEST_TYPE_SIZE_MIN,
        NPF_TEST_TYPE_SIZE_MAX,
        NPF_TEST_TYPE_SIZE_BOUNDS,
        NPF_TEST_TYPE_IP_SRC_ADDR_ALLOWLIST,
        NPF_TEST_TYPE_IP_SRC_ADDR_BLOCKLIST,
        NPF_TEST_TYPE_ETH_SRC_ADDR_MATCH,
        NPF_TEST_TYPE_ETH_SRC_ADDR_UNMATCH,
        NPF_TEST_TYPE_ETH_DST_ADDR_MATCH,
        NPF_TEST_TYPE_ETH_DST_ADDR_UNMATCH,
        NPF_TEST_TYPE_ETH_SRC_ADDR_MASK_MATCH,
        NPF_TEST_TYPE_ETH_DST_ADDR_MASK_MATCH,
        NPF_TEST_TYPE_ETH_TYPE_MATCH,
        NPF_TEST_TYPE_ETH_TYPE_UNMATCH,
        NPF_TEST_TYPE_ETH_VLAN_TYPE_MATCH,
        NPF_TEST_TYPE_ETH_VLAN_TYPE_UNMATCH,
        NPF_TEST_TYPE_LOCAL_IN_MATCH,
};

#if defined(CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG) || \
        defined(CONFIG_NET_SHELL_PKT_FILTER_SUPPORTED)
#define NPF_TEST_ENABLE_NAME 1
#elif defined(NPF_TEST_ENABLE_NAME)
#undef NPF_TEST_ENABLE_NAME
#endif


struct npf_test {
        npf_test_fn_t *fn;

        IF_ENABLED(NPF_TEST_ENABLE_NAME,
                   (const char *name;))
        IF_ENABLED(NPF_TEST_ENABLE_NAME,
                   (enum npf_test_type type;))
};

struct npf_rule {
        sys_snode_t node;
        enum net_verdict result;
        enum net_priority priority;
        uint32_t nb_tests;
        struct npf_test *tests[];
};

extern struct npf_rule npf_default_ok;
extern struct npf_rule npf_default_drop;

struct npf_rule_list {
        sys_slist_t rule_head;
        struct k_spinlock lock;
};

extern struct npf_rule_list npf_send_rules;
extern struct npf_rule_list npf_recv_rules;
extern struct npf_rule_list npf_local_in_recv_rules;
extern struct npf_rule_list npf_ipv4_recv_rules;
extern struct npf_rule_list npf_ipv6_recv_rules;

void npf_insert_rule(struct npf_rule_list *rules, struct npf_rule *rule);

void npf_append_rule(struct npf_rule_list *rules, struct npf_rule *rule);

bool npf_remove_rule(struct npf_rule_list *rules, struct npf_rule *rule);

bool npf_remove_all_rules(struct npf_rule_list *rules);


/* convenience shortcuts */
#define npf_insert_send_rule(rule) npf_insert_rule(&npf_send_rules, rule)
#define npf_insert_recv_rule(rule) npf_insert_rule(&npf_recv_rules, rule)
#define npf_append_send_rule(rule) npf_append_rule(&npf_send_rules, rule)
#define npf_append_recv_rule(rule) npf_append_rule(&npf_recv_rules, rule)
#define npf_remove_send_rule(rule) npf_remove_rule(&npf_send_rules, rule)
#define npf_remove_recv_rule(rule) npf_remove_rule(&npf_recv_rules, rule)
#define npf_remove_all_send_rules() npf_remove_all_rules(&npf_send_rules)
#define npf_remove_all_recv_rules() npf_remove_all_rules(&npf_recv_rules)

#ifdef CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK
#define npf_insert_local_in_recv_rule(rule) npf_insert_rule(&npf_local_in_recv_rules, rule)
#define npf_append_local_in_recv_rule(rule) npf_append_rule(&npf_local_in_recv_rules, rule)
#define npf_remove_local_in_recv_rule(rule) npf_remove_rule(&npf_local_in_recv_rules, rule)
#define npf_remove_all_local_in_recv_rules() npf_remove_all_rules(&npf_local_in_recv_rules)
#endif /* CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK */

#ifdef CONFIG_NET_PKT_FILTER_IPV4_HOOK
#define npf_insert_ipv4_recv_rule(rule) npf_insert_rule(&npf_ipv4_recv_rules, rule)
#define npf_append_ipv4_recv_rule(rule) npf_append_rule(&npf_ipv4_recv_rules, rule)
#define npf_remove_ipv4_recv_rule(rule) npf_remove_rule(&npf_ipv4_recv_rules, rule)
#define npf_remove_all_ipv4_recv_rules() npf_remove_all_rules(&npf_ipv4_recv_rules)
#endif /* CONFIG_NET_PKT_FILTER_IPV4_HOOK */

#ifdef CONFIG_NET_PKT_FILTER_IPV6_HOOK
#define npf_insert_ipv6_recv_rule(rule) npf_insert_rule(&npf_ipv6_recv_rules, rule)
#define npf_append_ipv6_recv_rule(rule) npf_append_rule(&npf_ipv6_recv_rules, rule)
#define npf_remove_ipv6_recv_rule(rule) npf_remove_rule(&npf_ipv6_recv_rules, rule)
#define npf_remove_all_ipv6_recv_rules() npf_remove_all_rules(&npf_ipv6_recv_rules)
#endif /* CONFIG_NET_PKT_FILTER_IPV6_HOOK */


#define NPF_RULE(_name, _result, ...)                                     \
        struct npf_rule _name = {                                         \
                .result = (_result),                                      \
                .nb_tests = NUM_VA_ARGS_LESS_1(__VA_ARGS__) + 1,          \
                .tests = { FOR_EACH(Z_NPF_TEST_ADDR, (,), __VA_ARGS__) }, \
        }

#define NPF_PRIORITY(_name, _priority, ...)                             \
        struct npf_rule _name = {                                       \
                .result = NET_CONTINUE,                                 \
                .priority = (_priority),                                \
                .nb_tests = NUM_VA_ARGS_LESS_1(__VA_ARGS__) + 1,        \
                .tests = {FOR_EACH(Z_NPF_TEST_ADDR, (,), __VA_ARGS__)}, \
        }

#define Z_NPF_TEST_ADDR(arg) &arg.test




struct npf_test_iface {
        struct npf_test test;
        struct net_if *iface;
};

extern npf_test_fn_t npf_iface_match;
extern npf_test_fn_t npf_iface_unmatch;
extern npf_test_fn_t npf_orig_iface_match;
extern npf_test_fn_t npf_orig_iface_unmatch;


#define NPF_IFACE_MATCH(_name, _iface)                                  \
        struct npf_test_iface _name = {                                 \
                .iface = (_iface),                                      \
                .test.fn = npf_iface_match,                             \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "iface",                       \
                            .test.type = NPF_TEST_TYPE_IFACE_MATCH,))   \
        }

#define NPF_IFACE_UNMATCH(_name, _iface)                                \
        struct npf_test_iface _name = {                                 \
                .iface = (_iface),                                      \
                .test.fn = npf_iface_unmatch,                           \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!iface",                      \
                            .test.type = NPF_TEST_TYPE_IFACE_UNMATCH,)) \
        }

#define NPF_ORIG_IFACE_MATCH(_name, _iface)                             \
        struct npf_test_iface _name = {                                 \
                .iface = (_iface),                                      \
                .test.fn = npf_orig_iface_match,                        \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "orig iface",                  \
                            .test.type = NPF_TEST_TYPE_ORIG_IFACE_MATCH,)) \
        }

#define NPF_ORIG_IFACE_UNMATCH(_name, _iface)                           \
        struct npf_test_iface _name = {                                 \
                .iface = (_iface),                                      \
                .test.fn = npf_orig_iface_unmatch,                      \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!orig iface",                 \
                            .test.type = NPF_TEST_TYPE_ORIG_IFACE_UNMATCH,)) \
        }


struct npf_test_size_bounds {
        struct npf_test test;
        size_t min;
        size_t max;
};

extern npf_test_fn_t npf_size_inbounds;


#define NPF_SIZE_MIN(_name, _size)                                 \
        struct npf_test_size_bounds _name = {                      \
                .min = (_size),                                    \
                .max = SIZE_MAX,                                   \
                .test.fn = npf_size_inbounds,                      \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                   \
                           (.test.name = "size min",               \
                            .test.type = NPF_TEST_TYPE_SIZE_MIN,)) \
        }

#define NPF_SIZE_MAX(_name, _size)                                 \
        struct npf_test_size_bounds _name = {                      \
                .min = 0,                                          \
                .max = (_size),                                    \
                .test.fn = npf_size_inbounds,                      \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                   \
                           (.test.name = "size max",               \
                            .test.type = NPF_TEST_TYPE_SIZE_MAX,)) \
        }

#define NPF_SIZE_BOUNDS(_name, _min_size, _max_size)                  \
        struct npf_test_size_bounds _name = {                         \
                .min = (_min_size),                                   \
                .max = (_max_size),                                   \
                .test.fn = npf_size_inbounds,                         \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                      \
                           (.test.name = "size bounds",               \
                            .test.type = NPF_TEST_TYPE_SIZE_BOUNDS,)) \
        }


struct npf_test_ip {
        struct npf_test test;
        uint8_t addr_family;
        void *ipaddr;
        uint32_t ipaddr_num;
};

extern npf_test_fn_t npf_ip_src_addr_match;
extern npf_test_fn_t npf_ip_src_addr_unmatch;


#define NPF_IP_SRC_ADDR_ALLOWLIST(_name, _ip_addr_array, _ip_addr_num, _af) \
        struct npf_test_ip _name = {                                    \
                .addr_family = _af,                                     \
                .ipaddr = (_ip_addr_array),                             \
                .ipaddr_num = _ip_addr_num,                             \
                .test.fn = npf_ip_src_addr_match,                       \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "ip src allow",                \
                            .test.type = NPF_TEST_TYPE_IP_SRC_ADDR_ALLOWLIST,)) \
        }

#define NPF_IP_SRC_ADDR_BLOCKLIST(_name, _ip_addr_array, _ip_addr_num, _af) \
        struct npf_test_ip _name = {                                    \
                .addr_family = _af,                                     \
                .ipaddr = (_ip_addr_array),                             \
                .ipaddr_num = _ip_addr_num,                             \
                .test.fn = npf_ip_src_addr_unmatch,                     \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "ip src block",                \
                            .test.type = NPF_TEST_TYPE_IP_SRC_ADDR_BLOCKLIST,)) \
        }




struct npf_test_eth_addr {
        struct npf_test test;
        unsigned int nb_addresses;
        struct net_eth_addr *addresses;
        struct net_eth_addr mask;
};

extern npf_test_fn_t npf_eth_src_addr_match;
extern npf_test_fn_t npf_eth_src_addr_unmatch;
extern npf_test_fn_t npf_eth_dst_addr_match;
extern npf_test_fn_t npf_eth_dst_addr_unmatch;


#define NPF_ETH_SRC_ADDR_MATCH(_name, _addr_array)                      \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .test.fn = npf_eth_src_addr_match,                      \
                .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth src",                     \
                            .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_MATCH,)) \
        }

#define NPF_ETH_SRC_ADDR_UNMATCH(_name, _addr_array)                    \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .test.fn = npf_eth_src_addr_unmatch,                    \
                .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!eth src",                    \
                            .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_UNMATCH,)) \
        }

#define NPF_ETH_DST_ADDR_MATCH(_name, _addr_array)                      \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .test.fn = npf_eth_dst_addr_match,                      \
                .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth dst",                     \
                            .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_MATCH,)) \
        }

#define NPF_ETH_DST_ADDR_UNMATCH(_name, _addr_array)                    \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .test.fn = npf_eth_dst_addr_unmatch,                    \
                .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!eth dst",                    \
                            .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_UNMATCH,)) \
        }

#define NPF_ETH_SRC_ADDR_MASK_MATCH(_name, _addr_array, ...)            \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .mask.addr = { __VA_ARGS__ },                           \
                .test.fn = npf_eth_src_addr_match,                      \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth src mask",                \
                            .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_MASK_MATCH,)) \
        }

#define NPF_ETH_DST_ADDR_MASK_MATCH(_name, _addr_array, ...)            \
        struct npf_test_eth_addr _name = {                              \
                .addresses = (_addr_array),                             \
                .nb_addresses = ARRAY_SIZE(_addr_array),                \
                .mask.addr = { __VA_ARGS__ },                           \
                .test.fn = npf_eth_dst_addr_match,                      \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth dst mask",                \
                            .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_MASK_MATCH,)) \
        }


struct npf_test_eth_type {
        struct npf_test test;
        uint16_t type;                  /* type in network order */
};

extern npf_test_fn_t npf_eth_type_match;
extern npf_test_fn_t npf_eth_type_unmatch;
extern npf_test_fn_t npf_eth_vlan_type_match;
extern npf_test_fn_t npf_eth_vlan_type_unmatch;


#define NPF_ETH_TYPE_MATCH(_name, _type)                                \
        struct npf_test_eth_type _name = {                              \
                .type = net_htons(_type),                               \
                .test.fn = npf_eth_type_match,                          \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth type",                    \
                            .test.type = NPF_TEST_TYPE_ETH_TYPE_MATCH,)) \
        }

#define NPF_ETH_TYPE_UNMATCH(_name, _type)                              \
        struct npf_test_eth_type _name = {                              \
                .type = net_htons(_type),                               \
                .test.fn = npf_eth_type_unmatch,                        \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!eth type",                   \
                            .test.type = NPF_TEST_TYPE_ETH_TYPE_UNMATCH,)) \
        }

#define NPF_ETH_VLAN_TYPE_MATCH(_name, _type)                           \
        struct npf_test_eth_type _name = {                              \
                .type = net_htons(_type),                               \
                .test.fn = npf_eth_vlan_type_match,                     \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "eth vlan type",               \
                            .test.type = NPF_TEST_TYPE_ETH_VLAN_TYPE_MATCH,)) \
        }

#define NPF_ETH_VLAN_TYPE_UNMATCH(_name, _type)                         \
        struct npf_test_eth_type _name = {                              \
                .type = net_htons(_type),                               \
                .test.fn = npf_eth_vlan_type_unmatch,                   \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "!eth vlan type",              \
                            .test.type = NPF_TEST_TYPE_ETH_VLAN_TYPE_UNMATCH,)) \
        }

typedef bool (npf_local_in_fn_t)(struct net_pkt *pkt, void *user_data);


extern npf_test_fn_t npf_local_in_match;

struct npf_test_local_in {
        struct npf_test test;
        npf_local_in_fn_t *fn; /* local_in hook function */
        void *user_data;       /* optional user data */
};


#define NPF_LOCAL_IN_MATCH(_name, _handler, _user_data)                 \
        struct npf_test_local_in _name = {                              \
                .test.fn = npf_local_in_match,                          \
                .fn = (_handler),                                       \
                .user_data = (_user_data),                              \
                IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                           (.test.name = "local_in",                    \
                            .test.type = NPF_TEST_TYPE_LOCAL_IN_MATCH,)) \
        }

enum npf_rule_type {
        NPF_RULE_TYPE_UNKNOWN = 0,
        NPF_RULE_TYPE_SEND,
        NPF_RULE_TYPE_RECV,
        NPF_RULE_TYPE_LOCAL_IN_RECV,
        NPF_RULE_TYPE_IPV4_RECV,
        NPF_RULE_TYPE_IPV6_RECV,
};

typedef void (*npf_rule_cb_t)(struct npf_rule *rule,
                              enum npf_rule_type type,
                              void *user_data);

void npf_rules_foreach(npf_rule_cb_t cb, void *user_data);

const char *npf_test_get_str(struct npf_test *test, char *buf,
                             size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_PKT_FILTER_H_ */
```

## 27.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2021 BayLibre SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 153 行

便利简写（Convenience Shortcuts）。

### 注释 3：原第 168 行

条件编译配置（Configuration）标记：`CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK`。

### 注释 4：原第 175 行

条件编译配置（Configuration）标记：`CONFIG_NET_PKT_FILTER_IPV4_HOOK`。

### 注释 5：原第 182 行

条件编译配置（Configuration）标记：`CONFIG_NET_PKT_FILTER_IPV6_HOOK`。

### 注释 6：原第 614 行

采用网络字节序（Network Order）的类型（Type）。

### 注释 7：原第 705 行

`local_in` 钩子函数（Hook Function）。

### 注释 8：原第 706 行

可选用户数据（Optional User Data）。

### 注释 9：原第 770 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_PKT_FILTER_H_`。

## 27.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html)
- [limits.h](../api_file_reference/P189_____w__zephyr__zephyr__lib__libc__minimal__include__limits.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [npf_test](../network_service_model_reference/P037_npf_test_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [fn](../network_service_model_reference/P037_npf_test_结构体.md#ac49921514690a71986ca4d07245cfe7d)
- [IF_ENABLED](../util_reference/P001_通用工具公共接口.md#gae67ffe50e848951dbde309ed569ea925)
- [npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P035_npf_rule_结构体.md#ad5ae58fbcee5112e2defde1d7f4320dc)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [result](../network_service_model_reference/P035_npf_rule_结构体.md#a872daf53310dd8e20477eafd6808481f)
- [net_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae87ef466e77ded673ed7e593d3eddffd)
- [priority](../network_service_model_reference/P035_npf_rule_结构体.md#a3691e7be04a2948f0c979305f48fbb2c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [nb_tests](../network_service_model_reference/P035_npf_rule_结构体.md#a06045c693cf06e6ebfc5a74b8c3f5ef7)
- [tests](../network_service_model_reference/P035_npf_rule_结构体.md#a72c032c55535c82f365b2cd1229cb1e0)
- [npf_default_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#gaac489d75c023952243589cba7ff7367a)
- [npf_default_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga8fc592feedeceb5172f8747a29697dd7)
- [npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [rule_head](../network_service_model_reference/P036_npf_rule_list_结构体.md#ab6aadf2d3479853c28e94972e7862931)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [lock](../network_service_model_reference/P036_npf_rule_list_结构体.md#af4d539d930acb257b1496761219d26cd)
- [npf_send_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga8017a041d3168c76e39bdfac011b9315)
- [npf_recv_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga9714529658625e906264a46ad1a9be6f)
- [npf_local_in_recv_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga571e9fb34eb4e3cbf38f885b5e786021)
- [npf_ipv4_recv_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#gad521d7ac3270970833aec48d8a517d85)
- [npf_ipv6_recv_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#gab91ca81aab2da48066538d72caf0c8ae)
- [npf_insert_rule](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga3b2a85558b6756e76760d9a40c780e28)
- [npf_append_rule](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#gadfa956e4af3c45460846fc22f863e697)
- [npf_remove_rule](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga4d7426db901debff35e1de5805e06c71)
- [npf_remove_all_rules](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga54916eb4943e4b47cd31eb23827d0dd5)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [npf_local_in_fn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga673493f74227912cf8f5827a77af012f)
- [npf_rule_type](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gaad4624a8e6c9491572e2a89739304530)
- [NPF_RULE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca)
- [NPF_RULE_TYPE_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81)
- [NPF_RULE_TYPE_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f)
- [NPF_RULE_TYPE_LOCAL_IN_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b)
- [NPF_RULE_TYPE_IPV4_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc)
- [NPF_RULE_TYPE_IPV6_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)
- [npf_rule_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7522a5a2188f7afbdc1a0528782ce0ef)
- [npf_rules_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga188b9d73f47a77ce05d728250606e7ec)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [npf_rule_list::rule_head](../network_service_model_reference/P036_npf_rule_list_结构体.md#ab6aadf2d3479853c28e94972e7862931)
- [npf_rule_list::lock](../network_service_model_reference/P036_npf_rule_list_结构体.md#af4d539d930acb257b1496761219d26cd)
- [npf_rule::nb_tests](../network_service_model_reference/P035_npf_rule_结构体.md#a06045c693cf06e6ebfc5a74b8c3f5ef7)
- [npf_rule::priority](../network_service_model_reference/P035_npf_rule_结构体.md#a3691e7be04a2948f0c979305f48fbb2c)
- [npf_rule::tests](../network_service_model_reference/P035_npf_rule_结构体.md#a72c032c55535c82f365b2cd1229cb1e0)
- [npf_rule::result](../network_service_model_reference/P035_npf_rule_结构体.md#a872daf53310dd8e20477eafd6808481f)
- [npf_rule::node](../network_service_model_reference/P035_npf_rule_结构体.md#ad5ae58fbcee5112e2defde1d7f4320dc)
- [npf_test::fn](../network_service_model_reference/P037_npf_test_结构体.md#ac49921514690a71986ca4d07245cfe7d)

---

[上一章](P026_net_compat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P028_npcx_fiu_qspi.h_源码浏览.md)
