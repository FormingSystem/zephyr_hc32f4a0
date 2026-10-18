---
id: learning.zephyr-docs.api-source-runtime-reference.page-34
title: intc_mchp_xec_ecia.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_intc\_mchp\_xec\_ecia.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html)。

## 34.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="adevice_8h_html"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a042b0afeb07493d13b068b26bc20c4f3"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a1b75b3213eace2931bfee965bb2bc1b9"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a363949f5b133f05b94dd8f17d572bbac"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a38ce7498c75d5f8c44facc3a625edbe9"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a4335e0f409723ffef63198b4ec026fe7"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a44d6bffbe40f09fc063580f9bb936cd8"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a4dab0aa1c6f77906ecd618d4269cf764"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a5a4b9d83a396438e22f1c694b7e7c82a"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a61c65d98a3781449fcb2363029fa0856"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a636a559083647193d154076c8d901bb5"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a6432ee01ae43598bc7ee8387f38ce5de"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a65d91d241885c1b8ff7bdc7bd92e2a13"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a73c19286d1f406aef34a4bda562d933b"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a756f04d2ad6680d4324326244f0b84b0"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a9026ff2f7a60f8e244537cbab4a0e891"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a91e7ab27d1b62f72a392ebbb5c38a4d8"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a946f876915453dd27eccc24d3e39210a"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a94b5aa34aaacb1e59ba2dffd625b200c"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a96a9db2c2a7e650c87457a1f5b1b395a"></a>
<a id="aintc__mchp__xec__ecia_8h_html_a980dfa5d5751cdefd5c911e6cac6075d"></a>
<a id="aintc__mchp__xec__ecia_8h_html_aa0acc2a2f6fe2c21e385aeb650d4e195"></a>
<a id="aintc__mchp__xec__ecia_8h_html_ab6d12794d0c1762efc2fdeb1a337580b"></a>
<a id="aintc__mchp__xec__ecia_8h_html_ac563ac5fcc47e2b3b375ce4d3ade897b"></a>
<a id="aintc__mchp__xec__ecia_8h_html_af90b2ce499b8109bae272d5bac444f51"></a>
<a id="aintc__mchp__xec__ecia_8h_html_afce3bbeeb977efc4349d58e676c17fbe"></a>
<a id="airq_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2021 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_XEC_ECIA_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_XEC_ECIA_H_

#include <zephyr/device.h>
#include <zephyr/irq.h>

int mchp_xec_ecia_enable(int girq_id, int src);

int mchp_xec_ecia_info_enable(int ecia_info);

int mchp_xec_ecia_disable(int girq_id, int src);

int mchp_xec_ecia_info_disable(int ecia_info);


/* callback for ECIA GIRQ interrupt source */
typedef void (*mchp_xec_ecia_callback_t) (int girq_id, int src, void *user);

int mchp_xec_ecia_set_callback(int girq_id, int src,
                               mchp_xec_ecia_callback_t cb, void *data);

int mchp_xec_ecia_info_set_callback(int ecia_info, mchp_xec_ecia_callback_t cb,
                                    void *data);

int mchp_xec_ecia_set_callback_by_dev(const struct device *dev_girq, int src,
                                      mchp_xec_ecia_callback_t cb, void *data);

int mchp_ecia_unset_callback(int girq_id, int src);

int mchp_ecia_unset_callback_by_dev(const struct device *dev_girq, int src);

/* platform specific */
void mchp_xec_ecia_girq_aggr_en(uint8_t girq_id, uint8_t enable);

void mchp_xec_ecia_girq_src_clr(uint8_t girq_id, uint8_t src_bit);

void mchp_xec_ecia_girq_src_en(uint8_t girq_id, uint8_t src_bit);

void mchp_xec_ecia_girq_src_dis(uint8_t girq_id, uint8_t src_bit);

void mchp_xec_ecia_girq_src_clr_bitmap(uint8_t girq_id, uint32_t bitmap);

void mchp_xec_ecia_girq_src_en_bitmap(uint8_t girq_id, uint32_t bitmap);

void mchp_xec_ecia_girq_src_dis_bitmap(uint8_t girq_id, uint32_t bitmap);

uint32_t mchp_xec_ecia_girq_result(uint8_t girq_id);

void mchp_xec_ecia_nvic_clr_pend(uint32_t nvic_num);

/* API using GIRQ parameters encoded with MCHP_XEC_ECIA */

void mchp_xec_ecia_info_girq_aggr_en(int ecia_info, uint8_t enable);

void mchp_xec_ecia_info_girq_src_clr(int ecia_info);

void mchp_xec_ecia_info_girq_src_en(int ecia_info);

void mchp_xec_ecia_info_girq_src_dis(int ecia_info);

uint32_t mchp_xec_ecia_info_girq_result(int ecia_info);

void mchp_xec_ecia_info_nvic_clr_pend(int ecia_info);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_XEC_ECIA_H_ */
```

## 34.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

ECIA GIRQ 中断源的回调（Callback）。

### 注释 3：原第 107 行

平台专用（Platform specific）。

### 注释 4：原第 170 行

使用由 `MCHP_XEC_ECIA` 编码的 GIRQ 参数的 API。

### 注释 5：原第 210 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_XEC_ECIA_H_`。

## 34.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)
- [mchp_xec_ecia_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a91e7ab27d1b62f72a392ebbb5c38a4d8)
- [mchp_xec_ecia_info_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a9026ff2f7a60f8e244537cbab4a0e891)
- [mchp_xec_ecia_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a6432ee01ae43598bc7ee8387f38ce5de)
- [mchp_xec_ecia_info_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a363949f5b133f05b94dd8f17d572bbac)
- [mchp_xec_ecia_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a946f876915453dd27eccc24d3e39210a)
- [mchp_xec_ecia_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a980dfa5d5751cdefd5c911e6cac6075d)
- [mchp_xec_ecia_info_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a1b75b3213eace2931bfee965bb2bc1b9)
- [mchp_xec_ecia_set_callback_by_dev](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a65d91d241885c1b8ff7bdc7bd92e2a13)
- [device](../device_reference/P002_设备对象结构.md)
- [mchp_ecia_unset_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a636a559083647193d154076c8d901bb5)
- [mchp_ecia_unset_callback_by_dev](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a756f04d2ad6680d4324326244f0b84b0)
- [mchp_xec_ecia_girq_aggr_en](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#aa0acc2a2f6fe2c21e385aeb650d4e195)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mchp_xec_ecia_girq_src_clr](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a042b0afeb07493d13b068b26bc20c4f3)
- [mchp_xec_ecia_girq_src_en](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#afce3bbeeb977efc4349d58e676c17fbe)
- [mchp_xec_ecia_girq_src_dis](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a4335e0f409723ffef63198b4ec026fe7)
- [mchp_xec_ecia_girq_src_clr_bitmap](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a61c65d98a3781449fcb2363029fa0856)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mchp_xec_ecia_girq_src_en_bitmap](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#ab6d12794d0c1762efc2fdeb1a337580b)
- [mchp_xec_ecia_girq_src_dis_bitmap](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a44d6bffbe40f09fc063580f9bb936cd8)
- [mchp_xec_ecia_girq_result](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a96a9db2c2a7e650c87457a1f5b1b395a)
- [mchp_xec_ecia_nvic_clr_pend](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#ac563ac5fcc47e2b3b375ce4d3ade897b)
- [mchp_xec_ecia_info_girq_aggr_en](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a4dab0aa1c6f77906ecd618d4269cf764)
- [mchp_xec_ecia_info_girq_src_clr](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a73c19286d1f406aef34a4bda562d933b)
- [mchp_xec_ecia_info_girq_src_en](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a5a4b9d83a396438e22f1c694b7e7c82a)
- [mchp_xec_ecia_info_girq_src_dis](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#af90b2ce499b8109bae272d5bac444f51)
- [mchp_xec_ecia_info_girq_result](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a38ce7498c75d5f8c44facc3a625edbe9)
- [mchp_xec_ecia_info_nvic_clr_pend](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html#a94b5aa34aaacb1e59ba2dffd625b200c)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)

---

[上一章](P033_input-event-codes.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P035_it8xxx2_pwm.h_源码浏览.md)
