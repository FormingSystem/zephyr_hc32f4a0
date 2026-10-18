---
id: learning.zephyr-docs.pwm-driver-reference.page-2
title: PWM驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pwm_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_PWM驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pwm_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_PWM驱动头文件参考.md)和[公共API](../hardware/P255_PWM公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00069"></a>
<a id="foldopen00141"></a>
<a id="foldopen00196"></a>
<a id="foldopen00216"></a>
<a id="foldopen00237"></a>
<a id="foldopen00256"></a>
<a id="foldopen00301"></a>
<a id="foldopen00320"></a>
<a id="foldopen00340"></a>
<a id="foldopen00358"></a>
<a id="foldopen00397"></a>
<a id="foldopen00412"></a>
<a id="foldopen00471"></a>
<a id="foldopen00542"></a>
<a id="foldopen00660"></a>
<a id="foldopen00706"></a>
<a id="foldopen00727"></a>
<a id="foldopen00745"></a>
<a id="foldopen00777"></a>
<a id="foldopen00827"></a>
<a id="foldopen00966"></a>
<a id="foldopen01021"></a>
<a id="foldopen01059"></a>
<a id="foldopen01084"></a>
<a id="foldopen01107"></a>
<a id="foldopen01128"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adevicetree_8h_html"></a>
<a id="adt-bindings_2pwm_2pwm_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__clock__apis_html_ga0501e82515b2bdf36453c4cc80f5e0cc"></a>
<a id="agroup__clock__apis_html_ga6a69d6cbdab5f24c2e66959293f210c1"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__math__extras_html_ga366f6606874071677bf9079647d9abce"></a>
<a id="agroup__pwm__interface__backend_html_ga284f0aa783ab2f457b2239a87a9c1671"></a>
<a id="agroup__pwm__interface__backend_html_ga471b1f0ed9992e372f1f01683b68f456"></a>
<a id="agroup__pwm__interface__backend_html_ga6330ac4e97604ab4510c16a3c4d0437f"></a>
<a id="agroup__pwm__interface__backend_html_ga70ab8cd3c6d7b43890655405b3e6db3f"></a>
<a id="agroup__pwm__interface__backend_html_ga8dedee6071801685cb618bacd8b51c57"></a>
<a id="agroup__pwm__interface__backend_html_gaae83bb7862c019492c8bc154015f8e8c"></a>
<a id="agroup__pwm__interface_html_ga09767ae3c8d970675dbf9e3e50291743"></a>
<a id="agroup__pwm__interface_html_ga09d1b358df32e798e0345cd647450d54"></a>
<a id="agroup__pwm__interface_html_ga1df2bb40af2fa3ce945cc9cd67edc2bf"></a>
<a id="agroup__pwm__interface_html_ga225ce58ceb3de3d76df3e03439d655b9"></a>
<a id="agroup__pwm__interface_html_ga2395ef29b77674d9f1b56d8091b8695a"></a>
<a id="agroup__pwm__interface_html_ga310d416087a619f90e946222668135af"></a>
<a id="agroup__pwm__interface_html_ga3a1552ea924eeec21477396da6d3890b"></a>
<a id="agroup__pwm__interface_html_ga5bc9607de7643cb78476ed354c51560b"></a>
<a id="agroup__pwm__interface_html_ga6489095d890224d23c5ed05bc884d24a"></a>
<a id="agroup__pwm__interface_html_ga6f0281398611dd876386c66a63373a2e"></a>
<a id="agroup__pwm__interface_html_ga70aad0d88e8041c880499e7cdaa9ae57"></a>
<a id="agroup__pwm__interface_html_ga83d9ec60d3fef69c97602365b979aece"></a>
<a id="agroup__pwm__interface_html_ga8ff263177143d33c6d0a284b837bc4da"></a>
<a id="agroup__pwm__interface_html_ga9603146d7f9c2690c1e1983113d6c6bb"></a>
<a id="agroup__pwm__interface_html_gad14ca53862a465d1789e8936ce394f9a"></a>
<a id="agroup__pwm__interface_html_gadd9049c9a56cd9419736b3514e42dc01"></a>
<a id="agroup__pwm__interface_html_gae1dcfb878163da76041efcedf0960fa0"></a>
<a id="agroup__pwm__interface_html_gae57fb205e43dde82d96abe79966539a9"></a>
<a id="agroup__pwm__interface_html_gaedacc300332a9c01da48671f92bf0097"></a>
<a id="agroup__pwm__interface_html_gaf87ef431d50a482910e77e49d52a2e13"></a>
<a id="agroup__pwm__interface_html_gaff280789f7b45fdefc354b3f841fe3ef"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__system__errno_html_gaa1591a4f3a86360108de5b9ba34980ca"></a>
<a id="amath__extras_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ab5eb23180f7cc12b7d6c04a8ec067fdd"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructpwm__driver__api_html"></a>
<a id="astructpwm__driver__api_html_a365761817898baf5ea52eb1ad63d67a6"></a>
<a id="astructpwm__driver__api_html_a4d4b8080814e092e2bc5ac0a47baa182"></a>
<a id="astructpwm__driver__api_html_a5d4e7cb7f3610fcc7a9981baf4ec3654"></a>
<a id="astructpwm__driver__api_html_a6b210f5e68353aef9594c2c585360e47"></a>
<a id="astructpwm__driver__api_html_aa97c7710a29e69af934e3b0f259c11b8"></a>
<a id="astructpwm__driver__api_html_afedf4abee4341fde838eedb962d34368"></a>
<a id="astructpwm__dt__spec_html"></a>
<a id="astructpwm__dt__spec_html_a2ddb45cbde80314a5a50dffe2e43921b"></a>
<a id="astructpwm__dt__spec_html_a739a2672afa1d56ec1d865d6d5be47b2"></a>
<a id="astructpwm__dt__spec_html_a935c72595e2248ab75ce0c43a394c0b3"></a>
<a id="astructpwm__dt__spec_html_ad9f2991bcf978940e638d17c5e17311e"></a>
<a id="astructpwm__event__callback_html"></a>
<a id="astructpwm__event__callback_html_a0f14cc1f7e4735e88f28ff4cfecbcec5"></a>
<a id="astructpwm__event__callback_html_a304e9ea24d4eb8f5d618aea8c3600223"></a>
<a id="astructpwm__event__callback_html_a56f5f3b2589dffb88a8d893fe7d259ab"></a>
<a id="atoolchain_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2016 Intel Corporation.
<a id="l00003"></a> * Copyright (c) 2020-2021 Vestas Wind Systems A/S
<a id="l00004"></a> * Copyright (c) 2025 Basalte bv
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_PWM_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_DRIVERS_PWM_H_
<a id="l00017"></a>
<a id="l00031"></a>
<a id="l00032"></a>#include &lt;errno.h&gt;
<a id="l00033"></a>#include &lt;stdint.h&gt;
<a id="l00034"></a>
<a id="l00035"></a>#include &lt;zephyr/device.h&gt;
<a id="l00036"></a>#include &lt;zephyr/devicetree.h&gt;
<a id="l00037"></a>#include &lt;zephyr/sys/clock.h&gt;
<a id="l00038"></a>#include &lt;zephyr/sys/math_extras.h&gt;
<a id="l00039"></a>#include &lt;zephyr/sys/slist.h&gt;
<a id="l00040"></a>#include &lt;zephyr/toolchain.h&gt;
<a id="l00041"></a>
<a id="l00042"></a>#include &lt;zephyr/dt-bindings/pwm/pwm.h&gt;
<a id="l00043"></a>
<a id="l00044"></a>#ifdef __cplusplus
<a id="l00045"></a>extern "C" {
<a id="l00046"></a>#endif
<a id="l00047"></a>
<a id="l00053"></a>
<a id="l00055"></a>/* Bit 0 is used for PWM_POLARITY_NORMAL/PWM_POLARITY_INVERTED */
<a id="l00056"></a>#define PWM_CAPTURE_TYPE_SHIFT          1U
<a id="l00057"></a>#define PWM_CAPTURE_TYPE_MASK           (3U &lt;&lt; PWM_CAPTURE_TYPE_SHIFT)
<a id="l00058"></a>#define PWM_CAPTURE_MODE_SHIFT          3U
<a id="l00059"></a>#define PWM_CAPTURE_MODE_MASK           (1U &lt;&lt; PWM_CAPTURE_MODE_SHIFT)
<a id="l00061"></a>
<a id="l00063"></a>#define PWM_CAPTURE_TYPE_PERIOD         (1U &lt;&lt; PWM_CAPTURE_TYPE_SHIFT)
<a id="l00064"></a>
<a id="l00066"></a>#define PWM_CAPTURE_TYPE_PULSE          (2U &lt;&lt; PWM_CAPTURE_TYPE_SHIFT)
<a id="l00067"></a>
<a id="l00069"></a>#define PWM_CAPTURE_TYPE_BOTH           (PWM_CAPTURE_TYPE_PERIOD | \
<a id="l00070"></a>                                         PWM_CAPTURE_TYPE_PULSE)
<a id="l00071"></a>
<a id="l00073"></a>#define PWM_CAPTURE_MODE_SINGLE         (0U &lt;&lt; PWM_CAPTURE_MODE_SHIFT)
<a id="l00074"></a>
<a id="l00076"></a>#define PWM_CAPTURE_MODE_CONTINUOUS     (1U &lt;&lt; PWM_CAPTURE_MODE_SHIFT)
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00085"></a>
<a id="l00086"></a>#define PWM_EVENT_TYPE_SHIFT            0U
<a id="l00087"></a>
<a id="l00089"></a>#define PWM_EVENT_TYPE_PERIOD           (1U &lt;&lt; PWM_EVENT_TYPE_SHIFT)
<a id="l00090"></a>
<a id="l00097"></a>#define PWM_EVENT_TYPE_FAULT            (2U &lt;&lt; PWM_EVENT_TYPE_SHIFT)
<a id="l00098"></a>
<a id="l00103"></a>#define PWM_EVENT_TYPE_COMPARE_CAPTURE  (4U &lt;&lt; PWM_EVENT_TYPE_SHIFT)
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>typedef uint16_t pwm_flags_t;
<a id="l00117"></a>
<a id="l00123"></a>
<a id="l00124"></a>typedef uint16_t pwm_events_t;
<a id="l00125"></a>
<a id="l00141"></a>struct pwm_dt_spec {
<a id="l00143"></a>        const struct device *dev;
<a id="l00145"></a>        uint32_t channel;
<a id="l00147"></a>        uint32_t period;
<a id="l00149"></a>        pwm_flags_t flags;
<a id="l00150"></a>};
<a id="l00151"></a>
<a id="l00196"></a>#define PWM_DT_SPEC_GET_BY_NAME(node_id, name)                                 \
<a id="l00197"></a>        {                                                                      \
<a id="l00198"></a>                .dev = DEVICE_DT_GET(DT_PWMS_CTLR_BY_NAME(node_id, name)),     \
<a id="l00199"></a>                .channel = DT_PWMS_CHANNEL_BY_NAME(node_id, name),             \
<a id="l00200"></a>                .period = DT_PWMS_PERIOD_BY_NAME(node_id, name),               \
<a id="l00201"></a>                .flags = DT_PWMS_FLAGS_BY_NAME(node_id, name),                 \
<a id="l00202"></a>        }
<a id="l00203"></a>
<a id="l00216"></a>#define PWM_DT_SPEC_INST_GET_BY_NAME(inst, name)                               \
<a id="l00217"></a>        PWM_DT_SPEC_GET_BY_NAME(DT_DRV_INST(inst), name)
<a id="l00218"></a>
<a id="l00237"></a>#define PWM_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)               \
<a id="l00238"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, pwms),                           \
<a id="l00239"></a>                    (PWM_DT_SPEC_GET_BY_NAME(node_id, name)),                  \
<a id="l00240"></a>                    (default_value))
<a id="l00241"></a>
<a id="l00256"></a>#define PWM_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)             \
<a id="l00257"></a>        PWM_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
<a id="l00258"></a>
<a id="l00301"></a>#define PWM_DT_SPEC_GET_BY_IDX(node_id, idx)                                   \
<a id="l00302"></a>        {                                                                      \
<a id="l00303"></a>                .dev = DEVICE_DT_GET(DT_PWMS_CTLR_BY_IDX(node_id, idx)),       \
<a id="l00304"></a>                .channel = DT_PWMS_CHANNEL_BY_IDX(node_id, idx),               \
<a id="l00305"></a>                .period = DT_PWMS_PERIOD_BY_IDX(node_id, idx),                 \
<a id="l00306"></a>                .flags = DT_PWMS_FLAGS_BY_IDX(node_id, idx),                   \
<a id="l00307"></a>        }
<a id="l00308"></a>
<a id="l00320"></a>#define PWM_DT_SPEC_INST_GET_BY_IDX(inst, idx)                                 \
<a id="l00321"></a>        PWM_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)
<a id="l00322"></a>
<a id="l00340"></a>#define PWM_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)                 \
<a id="l00341"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, pwms),                           \
<a id="l00342"></a>                    (PWM_DT_SPEC_GET_BY_IDX(node_id, idx)),                    \
<a id="l00343"></a>                    (default_value))
<a id="l00344"></a>
<a id="l00358"></a>#define PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)               \
<a id="l00359"></a>        PWM_DT_SPEC_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
<a id="l00360"></a>
<a id="l00371"></a>#define PWM_DT_SPEC_GET(node_id) PWM_DT_SPEC_GET_BY_IDX(node_id, 0)
<a id="l00372"></a>
<a id="l00383"></a>#define PWM_DT_SPEC_INST_GET(inst) PWM_DT_SPEC_GET(DT_DRV_INST(inst))
<a id="l00384"></a>
<a id="l00397"></a>#define PWM_DT_SPEC_GET_OR(node_id, default_value)                             \
<a id="l00398"></a>        PWM_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)
<a id="l00399"></a>
<a id="l00412"></a>#define PWM_DT_SPEC_INST_GET_OR(inst, default_value)                           \
<a id="l00413"></a>        PWM_DT_SPEC_GET_OR(DT_DRV_INST(inst), default_value)
<a id="l00414"></a>
<a id="l00434"></a>typedef void (*pwm_capture_callback_handler_t)(const struct device *dev,
<a id="l00435"></a>                                               uint32_t channel,
<a id="l00436"></a>                                               uint32_t period_cycles,
<a id="l00437"></a>                                               uint32_t pulse_cycles,
<a id="l00438"></a>                                               int status, void *user_data);
<a id="l00439"></a>
<a id="l00440"></a>struct pwm_event_callback;
<a id="l00441"></a>
<a id="l00456"></a>typedef void (*pwm_event_callback_handler_t)(const struct device *dev,
<a id="l00457"></a>                                             struct pwm_event_callback *callback, uint32_t channel,
<a id="l00458"></a>                                             pwm_events_t events);
<a id="l00459"></a>
<a id="l00471"></a>struct pwm_event_callback {
<a id="l00473"></a>        sys_snode_t node;
<a id="l00475"></a>
<a id="l00477"></a>        pwm_event_callback_handler_t handler;
<a id="l00478"></a>
<a id="l00480"></a>        uint32_t channel;
<a id="l00481"></a>
<a id="l00483"></a>        pwm_events_t event_mask;
<a id="l00484"></a>};
<a id="l00485"></a>
<a id="l00490"></a>
<a id="l00495"></a>typedef int (*pwm_set_cycles_t)(const struct device *dev, uint32_t channel,
<a id="l00496"></a>                                uint32_t period_cycles, uint32_t pulse_cycles,
<a id="l00497"></a>                                pwm_flags_t flags);
<a id="l00498"></a>
<a id="l00503"></a>typedef int (*pwm_get_cycles_per_sec_t)(const struct device *dev,
<a id="l00504"></a>                                        uint32_t channel, uint64_t *cycles);
<a id="l00505"></a>
<a id="l00506"></a>#if defined(CONFIG_PWM_CAPTURE) || defined(__DOXYGEN__)
<a id="l00511"></a>typedef int (*pwm_configure_capture_t)(const struct device *dev,
<a id="l00512"></a>                                       uint32_t channel, pwm_flags_t flags,
<a id="l00513"></a>                                       pwm_capture_callback_handler_t cb,
<a id="l00514"></a>                                       void *user_data);
<a id="l00515"></a>
<a id="l00520"></a>typedef int (*pwm_enable_capture_t)(const struct device *dev, uint32_t channel);
<a id="l00521"></a>
<a id="l00526"></a>typedef int (*pwm_disable_capture_t)(const struct device *dev,
<a id="l00527"></a>                                     uint32_t channel);
<a id="l00528"></a>#endif /* CONFIG_PWM_CAPTURE */
<a id="l00529"></a>
<a id="l00530"></a>#if defined(CONFIG_PWM_EVENT) || defined(__DOXYGEN__)
<a id="l00535"></a>typedef int (*pwm_manage_event_callback_t)(const struct device *dev,
<a id="l00536"></a>                                           struct pwm_event_callback *callback, bool set);
<a id="l00537"></a>#endif /* CONFIG_PWM_EVENT */
<a id="l00538"></a>
<a id="l00542"></a>__subsystem struct pwm_driver_api {
<a id="l00546"></a>        pwm_set_cycles_t set_cycles;
<a id="l00550"></a>        pwm_get_cycles_per_sec_t get_cycles_per_sec;
<a id="l00551"></a>#if defined(CONFIG_PWM_CAPTURE) || defined(__DOXYGEN__)
<a id="l00556"></a>        pwm_configure_capture_t configure_capture;
<a id="l00561"></a>        pwm_enable_capture_t enable_capture;
<a id="l00566"></a>        pwm_disable_capture_t disable_capture;
<a id="l00567"></a>#endif /* CONFIG_PWM_CAPTURE */
<a id="l00568"></a>#if defined(CONFIG_PWM_EVENT) || defined(__DOXYGEN__)
<a id="l00573"></a>        pwm_manage_event_callback_t manage_event_callback;
<a id="l00574"></a>#endif /* CONFIG_PWM_EVENT */
<a id="l00575"></a>};
<a id="l00576"></a>
<a id="l00580"></a>
<a id="l00610"></a>__syscall int pwm_set_cycles(const struct device *dev, uint32_t channel,
<a id="l00611"></a>                             uint32_t period, uint32_t pulse,
<a id="l00612"></a>                             pwm_flags_t flags);
<a id="l00613"></a>
<a id="l00614"></a>static inline int z_impl_pwm_set_cycles(const struct device *dev,
<a id="l00615"></a>                                        uint32_t channel, uint32_t period,
<a id="l00616"></a>                                        uint32_t pulse, pwm_flags_t flags)
<a id="l00617"></a>{
<a id="l00618"></a>        if (pulse &gt; period) {
<a id="l00619"></a>                return -EINVAL;
<a id="l00620"></a>        }
<a id="l00621"></a>
<a id="l00622"></a>        return DEVICE_API_GET(pwm, dev)-&gt;set_cycles(dev, channel, period, pulse, flags);
<a id="l00623"></a>}
<a id="l00624"></a>
<a id="l00635"></a>__syscall int pwm_get_cycles_per_sec(const struct device *dev, uint32_t channel,
<a id="l00636"></a>                                     uint64_t *cycles);
<a id="l00637"></a>
<a id="l00638"></a>static inline int z_impl_pwm_get_cycles_per_sec(const struct device *dev,
<a id="l00639"></a>                                                uint32_t channel,
<a id="l00640"></a>                                                uint64_t *cycles)
<a id="l00641"></a>{
<a id="l00642"></a>        return DEVICE_API_GET(pwm, dev)-&gt;get_cycles_per_sec(dev, channel, cycles);
<a id="l00643"></a>}
<a id="l00644"></a>
<a id="l00660"></a>static inline int pwm_set(const struct device *dev, uint32_t channel,
<a id="l00661"></a>                          uint32_t period, uint32_t pulse, pwm_flags_t flags)
<a id="l00662"></a>{
<a id="l00663"></a>        int err;
<a id="l00664"></a>        uint64_t pulse_cycles;
<a id="l00665"></a>        uint64_t period_cycles;
<a id="l00666"></a>        uint64_t cycles_per_sec;
<a id="l00667"></a>
<a id="l00668"></a>        err = pwm_get_cycles_per_sec(dev, channel, &amp;cycles_per_sec);
<a id="l00669"></a>        if (err &lt; 0) {
<a id="l00670"></a>                return err;
<a id="l00671"></a>        }
<a id="l00672"></a>
<a id="l00673"></a>        period_cycles = (period * cycles_per_sec) / NSEC_PER_SEC;
<a id="l00674"></a>        if (period_cycles &gt; UINT32_MAX) {
<a id="l00675"></a>                return -ENOTSUP;
<a id="l00676"></a>        }
<a id="l00677"></a>
<a id="l00678"></a>        pulse_cycles = (pulse * cycles_per_sec) / NSEC_PER_SEC;
<a id="l00679"></a>        if (pulse_cycles &gt; UINT32_MAX) {
<a id="l00680"></a>                return -ENOTSUP;
<a id="l00681"></a>        }
<a id="l00682"></a>
<a id="l00683"></a>        return pwm_set_cycles(dev, channel, (uint32_t)period_cycles,
<a id="l00684"></a>                              (uint32_t)pulse_cycles, flags);
<a id="l00685"></a>}
<a id="l00686"></a>
<a id="l00706"></a>static inline int pwm_set_dt(const struct pwm_dt_spec *spec, uint32_t period,
<a id="l00707"></a>                             uint32_t pulse)
<a id="l00708"></a>{
<a id="l00709"></a>        return pwm_set(spec-&gt;dev, spec-&gt;channel, period, pulse, spec-&gt;flags);
<a id="l00710"></a>}
<a id="l00711"></a>
<a id="l00727"></a>static inline int pwm_set_pulse_dt(const struct pwm_dt_spec *spec,
<a id="l00728"></a>                                   uint32_t pulse)
<a id="l00729"></a>{
<a id="l00730"></a>        return pwm_set(spec-&gt;dev, spec-&gt;channel, spec-&gt;period, pulse,
<a id="l00731"></a>                       spec-&gt;flags);
<a id="l00732"></a>}
<a id="l00733"></a>
<a id="l00745"></a>static inline int pwm_cycles_to_usec(const struct device *dev, uint32_t channel,
<a id="l00746"></a>                                     uint32_t cycles, uint64_t *usec)
<a id="l00747"></a>{
<a id="l00748"></a>        int err;
<a id="l00749"></a>        uint64_t temp;
<a id="l00750"></a>        uint64_t cycles_per_sec;
<a id="l00751"></a>
<a id="l00752"></a>        err = pwm_get_cycles_per_sec(dev, channel, &amp;cycles_per_sec);
<a id="l00753"></a>        if (err &lt; 0) {
<a id="l00754"></a>                return err;
<a id="l00755"></a>        }
<a id="l00756"></a>
<a id="l00757"></a>        if (u64_mul_overflow(cycles, (uint64_t)USEC_PER_SEC, &amp;temp)) {
<a id="l00758"></a>                return -ERANGE;
<a id="l00759"></a>        }
<a id="l00760"></a>
<a id="l00761"></a>        *usec = temp / cycles_per_sec;
<a id="l00762"></a>
<a id="l00763"></a>        return 0;
<a id="l00764"></a>}
<a id="l00765"></a>
<a id="l00777"></a>static inline int pwm_cycles_to_nsec(const struct device *dev, uint32_t channel,
<a id="l00778"></a>                                     uint32_t cycles, uint64_t *nsec)
<a id="l00779"></a>{
<a id="l00780"></a>        int err;
<a id="l00781"></a>        uint64_t temp;
<a id="l00782"></a>        uint64_t cycles_per_sec;
<a id="l00783"></a>
<a id="l00784"></a>        err = pwm_get_cycles_per_sec(dev, channel, &amp;cycles_per_sec);
<a id="l00785"></a>        if (err &lt; 0) {
<a id="l00786"></a>                return err;
<a id="l00787"></a>        }
<a id="l00788"></a>
<a id="l00789"></a>        if (u64_mul_overflow(cycles, (uint64_t)NSEC_PER_SEC, &amp;temp)) {
<a id="l00790"></a>                return -ERANGE;
<a id="l00791"></a>        }
<a id="l00792"></a>
<a id="l00793"></a>        *nsec = temp / cycles_per_sec;
<a id="l00794"></a>
<a id="l00795"></a>        return 0;
<a id="l00796"></a>}
<a id="l00797"></a>
<a id="l00798"></a>#if defined(CONFIG_PWM_CAPTURE) || defined(__DOXYGEN__)
<a id="l00827"></a>static inline int pwm_configure_capture(const struct device *dev,
<a id="l00828"></a>                                        uint32_t channel, pwm_flags_t flags,
<a id="l00829"></a>                                        pwm_capture_callback_handler_t cb,
<a id="l00830"></a>                                        void *user_data)
<a id="l00831"></a>{
<a id="l00832"></a>        const struct pwm_driver_api *api = DEVICE_API_GET(pwm, dev);
<a id="l00833"></a>
<a id="l00834"></a>        if (api-&gt;configure_capture == NULL) {
<a id="l00835"></a>                return -ENOSYS;
<a id="l00836"></a>        }
<a id="l00837"></a>
<a id="l00838"></a>        return api-&gt;configure_capture(dev, channel, flags, cb,
<a id="l00839"></a>                                              user_data);
<a id="l00840"></a>}
<a id="l00841"></a>#endif /* CONFIG_PWM_CAPTURE */
<a id="l00842"></a>
<a id="l00861"></a>__syscall int pwm_enable_capture(const struct device *dev, uint32_t channel);
<a id="l00862"></a>
<a id="l00863"></a>#ifdef CONFIG_PWM_CAPTURE
<a id="l00864"></a>static inline int z_impl_pwm_enable_capture(const struct device *dev,
<a id="l00865"></a>                                            uint32_t channel)
<a id="l00866"></a>{
<a id="l00867"></a>        const struct pwm_driver_api *api = DEVICE_API_GET(pwm, dev);
<a id="l00868"></a>
<a id="l00869"></a>        if (api-&gt;enable_capture == NULL) {
<a id="l00870"></a>                return -ENOSYS;
<a id="l00871"></a>        }
<a id="l00872"></a>
<a id="l00873"></a>        return api-&gt;enable_capture(dev, channel);
<a id="l00874"></a>}
<a id="l00875"></a>#endif /* CONFIG_PWM_CAPTURE */
<a id="l00876"></a>
<a id="l00890"></a>__syscall int pwm_disable_capture(const struct device *dev, uint32_t channel);
<a id="l00891"></a>
<a id="l00892"></a>#ifdef CONFIG_PWM_CAPTURE
<a id="l00893"></a>static inline int z_impl_pwm_disable_capture(const struct device *dev,
<a id="l00894"></a>                                             uint32_t channel)
<a id="l00895"></a>{
<a id="l00896"></a>        const struct pwm_driver_api *api = DEVICE_API_GET(pwm, dev);
<a id="l00897"></a>
<a id="l00898"></a>        if (api-&gt;disable_capture == NULL) {
<a id="l00899"></a>                return -ENOSYS;
<a id="l00900"></a>        }
<a id="l00901"></a>
<a id="l00902"></a>        return api-&gt;disable_capture(dev, channel);
<a id="l00903"></a>}
<a id="l00904"></a>#endif /* CONFIG_PWM_CAPTURE */
<a id="l00905"></a>
<a id="l00934"></a>__syscall int pwm_capture_cycles(const struct device *dev, uint32_t channel,
<a id="l00935"></a>                                 pwm_flags_t flags, uint32_t *period,
<a id="l00936"></a>                                 uint32_t *pulse, k_timeout_t timeout);
<a id="l00937"></a>
<a id="l00966"></a>static inline int pwm_capture_usec(const struct device *dev, uint32_t channel,
<a id="l00967"></a>                                   pwm_flags_t flags, uint64_t *period,
<a id="l00968"></a>                                   uint64_t *pulse, k_timeout_t timeout)
<a id="l00969"></a>{
<a id="l00970"></a>        int err;
<a id="l00971"></a>        uint32_t pulse_cycles;
<a id="l00972"></a>        uint32_t period_cycles;
<a id="l00973"></a>
<a id="l00974"></a>        err = pwm_capture_cycles(dev, channel, flags, &amp;period_cycles,
<a id="l00975"></a>                                 &amp;pulse_cycles, timeout);
<a id="l00976"></a>        if (err &lt; 0) {
<a id="l00977"></a>                return err;
<a id="l00978"></a>        }
<a id="l00979"></a>
<a id="l00980"></a>        err = pwm_cycles_to_usec(dev, channel, period_cycles, period);
<a id="l00981"></a>        if (err &lt; 0) {
<a id="l00982"></a>                return err;
<a id="l00983"></a>        }
<a id="l00984"></a>
<a id="l00985"></a>        err = pwm_cycles_to_usec(dev, channel, pulse_cycles, pulse);
<a id="l00986"></a>        if (err &lt; 0) {
<a id="l00987"></a>                return err;
<a id="l00988"></a>        }
<a id="l00989"></a>
<a id="l00990"></a>        return 0;
<a id="l00991"></a>}
<a id="l00992"></a>
<a id="l01021"></a>static inline int pwm_capture_nsec(const struct device *dev, uint32_t channel,
<a id="l01022"></a>                                   pwm_flags_t flags, uint64_t *period,
<a id="l01023"></a>                                   uint64_t *pulse, k_timeout_t timeout)
<a id="l01024"></a>{
<a id="l01025"></a>        int err;
<a id="l01026"></a>        uint32_t pulse_cycles;
<a id="l01027"></a>        uint32_t period_cycles;
<a id="l01028"></a>
<a id="l01029"></a>        err = pwm_capture_cycles(dev, channel, flags, &amp;period_cycles,
<a id="l01030"></a>                                 &amp;pulse_cycles, timeout);
<a id="l01031"></a>        if (err &lt; 0) {
<a id="l01032"></a>                return err;
<a id="l01033"></a>        }
<a id="l01034"></a>
<a id="l01035"></a>        err = pwm_cycles_to_nsec(dev, channel, period_cycles, period);
<a id="l01036"></a>        if (err &lt; 0) {
<a id="l01037"></a>                return err;
<a id="l01038"></a>        }
<a id="l01039"></a>
<a id="l01040"></a>        err = pwm_cycles_to_nsec(dev, channel, pulse_cycles, pulse);
<a id="l01041"></a>        if (err &lt; 0) {
<a id="l01042"></a>                return err;
<a id="l01043"></a>        }
<a id="l01044"></a>
<a id="l01045"></a>        return 0;
<a id="l01046"></a>}
<a id="l01047"></a>
<a id="l01048"></a>#if defined(CONFIG_PWM_EVENT) || defined(__DOXYGEN__)
<a id="l01059"></a>static inline void pwm_init_event_callback(struct pwm_event_callback *callback,
<a id="l01060"></a>                                           pwm_event_callback_handler_t handler, uint32_t channel,
<a id="l01061"></a>                                           pwm_events_t event_mask)
<a id="l01062"></a>{
<a id="l01063"></a>        __ASSERT_NO_MSG(callback != NULL);
<a id="l01064"></a>        __ASSERT_NO_MSG(handler != NULL);
<a id="l01065"></a>
<a id="l01066"></a>        callback-&gt;handler = handler;
<a id="l01067"></a>        callback-&gt;channel = channel;
<a id="l01068"></a>        callback-&gt;event_mask = event_mask;
<a id="l01069"></a>}
<a id="l01070"></a>
<a id="l01084"></a>static inline int pwm_add_event_callback(const struct device *dev,
<a id="l01085"></a>                                         struct pwm_event_callback *callback)
<a id="l01086"></a>{
<a id="l01087"></a>        const struct pwm_driver_api *api = DEVICE_API_GET(pwm, dev);
<a id="l01088"></a>
<a id="l01089"></a>        if (api-&gt;manage_event_callback == NULL) {
<a id="l01090"></a>                return -ENOSYS;
<a id="l01091"></a>        }
<a id="l01092"></a>
<a id="l01093"></a>        return api-&gt;manage_event_callback(dev, callback, true);
<a id="l01094"></a>}
<a id="l01095"></a>
<a id="l01107"></a>static inline int pwm_remove_event_callback(const struct device *dev,
<a id="l01108"></a>                                            struct pwm_event_callback *callback)
<a id="l01109"></a>{
<a id="l01110"></a>        const struct pwm_driver_api *api = DEVICE_API_GET(pwm, dev);
<a id="l01111"></a>
<a id="l01112"></a>        if (api-&gt;manage_event_callback == NULL) {
<a id="l01113"></a>                return -ENOSYS;
<a id="l01114"></a>        }
<a id="l01115"></a>
<a id="l01116"></a>        return api-&gt;manage_event_callback(dev, callback, false);
<a id="l01117"></a>}
<a id="l01118"></a>#endif /* defined(CONFIG_PWM_EVENT) || defined(__DOXYGEN__) */
<a id="l01119"></a>
<a id="l01128"></a>static inline bool pwm_is_ready_dt(const struct pwm_dt_spec *spec)
<a id="l01129"></a>{
<a id="l01130"></a>        return device_is_ready(spec-&gt;dev);
<a id="l01131"></a>}
<a id="l01132"></a>
<a id="l01133"></a>#ifdef __cplusplus
<a id="l01134"></a>}
<a id="l01135"></a>#endif
<a id="l01136"></a>
<a id="l01140"></a>
<a id="l01141"></a>#include &lt;zephyr/syscalls/pwm.h&gt;
<a id="l01142"></a>
<a id="l01143"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_PWM_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2016 Intel Corporation.；Copyright (c) 2020-2021 Vestas Wind Systems A/S；Copyright (c) 2025 Basalte bv。Apache-2.0许可证原文保留。

2. 位0用于PWM_POLARITY_NORMAL／PWM_POLARITY_INVERTED极性标志。

3. 结束CONFIG_PWM_CAPTURE相关捕获回调类型的条件编译。

4. 结束CONFIG_PWM_EVENT相关事件回调类型的条件编译。

5. 结束驱动API结构内CONFIG_PWM_CAPTURE相关成员的条件编译。

6. 结束驱动API结构内CONFIG_PWM_EVENT相关成员的条件编译。

7. 结束CONFIG_PWM_CAPTURE相关捕获配置函数的条件编译。

8. 结束CONFIG_PWM_CAPTURE相关捕获启用实现的条件编译。

9. 结束CONFIG_PWM_CAPTURE相关捕获禁用实现的条件编译。

10. 结束CONFIG_PWM_EVENT或__DOXYGEN__启用时的事件回调接口条件编译。

11. 结束PWM驱动头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_PWM_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

### `clock.h`

系统时钟API（System Clock APIs）。

符号定位：[clock.h](../timer_reference/P090_系统时钟头文件参考.md)。

### `device.h`

Zephyr设备模型（Device Model）的API与宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `DEVICE_API_GET`

```c
#define DEVICE_API_GET(_class, _dev)
```

展开为指定设备类别的设备API指针。

定义位置（Definition）：device.h:1486。

符号定位：[DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)。

### `devicetree.h`

设备树（Devicetree）主头文件。

符号定位：[devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)。

### `pwm.h`

符号定位：[pwm.h](../dt_pwm_binding_reference/P003_PWM绑定常量头文件参考.md)。

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `NSEC_PER_SEC`

```c
#define NSEC_PER_SEC
```

每秒的纳秒数。

定义位置（Definition）：clock.h:113。

符号定位：[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

### `USEC_PER_SEC`

```c
#define USEC_PER_SEC
```

每秒的微秒数。

定义位置（Definition）：clock.h:110。

符号定位：[USEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga6a69d6cbdab5f24c2e66959293f210c1)。

### `device_is_ready`

```c
bool device_is_ready(const struct device *dev)
```

验证设备是否已就绪、可以使用。

符号定位：[device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。

### `u64_mul_overflow`

```c
static bool u64_mul_overflow(uint64_t a, uint64_t b, uint64_t *result)
```

将两个无符号64位整数相乘。

符号定位：[u64_mul_overflow](../math_reference/P001_数学辅助公共接口.md#ga366f6606874071677bf9079647d9abce)。

### `pwm_set_cycles_t`

```c
int(* pwm_set_cycles_t)(const struct device *dev, uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles, pwm_flags_t flags)
```

配置 PWM 引脚周期与脉宽的回调 API。

定义位置（Definition）：pwm.h:495。

符号定位：[pwm_set_cycles_t](../hardware/P258_PWM驱动后端接口.md#ga284f0aa783ab2f457b2239a87a9c1671)。

### `pwm_disable_capture_t`

```c
int(* pwm_disable_capture_t)(const struct device *dev, uint32_t channel)
```

禁用 PWM 捕获功能的回调 API。

定义位置（Definition）：pwm.h:526。

符号定位：[pwm_disable_capture_t](../hardware/P258_PWM驱动后端接口.md#ga471b1f0ed9992e372f1f01683b68f456)。

### `pwm_get_cycles_per_sec_t`

```c
int(* pwm_get_cycles_per_sec_t)(const struct device *dev, uint32_t channel, uint64_t *cycles)
```

取得 PWM 每秒周期数，即时钟频率的回调 API。

定义位置（Definition）：pwm.h:503。

符号定位：[pwm_get_cycles_per_sec_t](../hardware/P258_PWM驱动后端接口.md#ga6330ac4e97604ab4510c16a3c4d0437f)。

### `pwm_manage_event_callback_t`

```c
int(* pwm_manage_event_callback_t)(const struct device *dev, struct pwm_event_callback *callback, bool set)
```

管理事件回调的回调 API。

定义位置（Definition）：pwm.h:535。

符号定位：[pwm_manage_event_callback_t](../hardware/P258_PWM驱动后端接口.md#ga70ab8cd3c6d7b43890655405b3e6db3f)。

### `pwm_configure_capture_t`

```c
int(* pwm_configure_capture_t)(const struct device *dev, uint32_t channel, pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data)
```

配置 PWM 捕获功能的回调 API。

定义位置（Definition）：pwm.h:511。

符号定位：[pwm_configure_capture_t](../hardware/P258_PWM驱动后端接口.md#ga8dedee6071801685cb618bacd8b51c57)。

### `pwm_enable_capture_t`

```c
int(* pwm_enable_capture_t)(const struct device *dev, uint32_t channel)
```

启用 PWM 捕获功能的回调 API。

定义位置（Definition）：pwm.h:520。

符号定位：[pwm_enable_capture_t](../hardware/P258_PWM驱动后端接口.md#gaae83bb7862c019492c8bc154015f8e8c)。

### `pwm_capture_cycles`

```c
int pwm_capture_cycles(const struct device *dev, uint32_t channel, pwm_flags_t flags, uint32_t *period, uint32_t *pulse, k_timeout_t timeout)
```

为单个 PWM 输入捕获一次周期／脉宽，以时钟周期数表示。

符号定位：[pwm_capture_cycles](../hardware/P255_PWM公共接口.md#ga09767ae3c8d970675dbf9e3e50291743)。

### `pwm_add_event_callback`

```c
static int pwm_add_event_callback(const struct device *dev, struct pwm_event_callback *callback)
```

添加应用事件回调。

定义位置（Definition）：pwm.h:1084。

符号定位：[pwm_add_event_callback](../hardware/P255_PWM公共接口.md#ga09d1b358df32e798e0345cd647450d54)。

### `pwm_disable_capture`

```c
int pwm_disable_capture(const struct device *dev, uint32_t channel)
```

为单个 PWM 输入禁用周期／脉宽捕获。

符号定位：[pwm_disable_capture](../hardware/P255_PWM公共接口.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)。

### `pwm_set_dt`

```c
static int pwm_set_dt(const struct pwm_dt_spec *spec, uint32_t period, uint32_t pulse)
```

根据 `struct pwm_dt_spec` 以纳秒设置周期与脉宽，其中周期由调用方自定义。

定义位置（Definition）：pwm.h:706。

符号定位：[pwm_set_dt](../hardware/P255_PWM公共接口.md#ga225ce58ceb3de3d76df3e03439d655b9)。

### `pwm_capture_callback_handler_t`

```c
void(* pwm_capture_callback_handler_t)(const struct device *dev, uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles, int status, void *user_data)
```

PWM 捕获回调处理函数（Capture Callback Handler）的签名。

定义位置（Definition）：pwm.h:434。

符号定位：[pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)。

### `pwm_get_cycles_per_sec`

```c
int pwm_get_cycles_per_sec(const struct device *dev, uint32_t channel, uint64_t *cycles)
```

取得单个 PWM 输出的时钟速率，即每秒周期数。

符号定位：[pwm_get_cycles_per_sec](../hardware/P255_PWM公共接口.md#ga310d416087a619f90e946222668135af)。

### `pwm_capture_usec`

```c
static int pwm_capture_usec(const struct device *dev, uint32_t channel, pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout)
```

为单个 PWM 输入捕获一次周期／脉宽，以微秒表示。

定义位置（Definition）：pwm.h:966。

符号定位：[pwm_capture_usec](../hardware/P255_PWM公共接口.md#ga3a1552ea924eeec21477396da6d3890b)。

### `pwm_events_t`

```c
uint16_t pwm_events_t
```

提供保存 PWM 事件的类型。

定义位置（Definition）：pwm.h:124。

符号定位：[pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)。

### `pwm_capture_nsec`

```c
static int pwm_capture_nsec(const struct device *dev, uint32_t channel, pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout)
```

为单个 PWM 输入捕获一次周期／脉宽，以纳秒表示。

定义位置（Definition）：pwm.h:1021。

符号定位：[pwm_capture_nsec](../hardware/P255_PWM公共接口.md#ga6489095d890224d23c5ed05bc884d24a)。

### `pwm_cycles_to_nsec`

```c
static int pwm_cycles_to_nsec(const struct device *dev, uint32_t channel, uint32_t cycles, uint64_t *nsec)
```

将 PWM 时钟周期数转换为纳秒。

定义位置（Definition）：pwm.h:777。

符号定位：[pwm_cycles_to_nsec](../hardware/P255_PWM公共接口.md#ga6f0281398611dd876386c66a63373a2e)。

### `pwm_is_ready_dt`

```c
static bool pwm_is_ready_dt(const struct pwm_dt_spec *spec)
```

验证 PWM 设备是否就绪（Ready）。

定义位置（Definition）：pwm.h:1128。

符号定位：[pwm_is_ready_dt](../hardware/P255_PWM公共接口.md#ga70aad0d88e8041c880499e7cdaa9ae57)。

### `pwm_remove_event_callback`

```c
static int pwm_remove_event_callback(const struct device *dev, struct pwm_event_callback *callback)
```

移除应用事件回调。

定义位置（Definition）：pwm.h:1107。

符号定位：[pwm_remove_event_callback](../hardware/P255_PWM公共接口.md#ga83d9ec60d3fef69c97602365b979aece)。

### `pwm_set_pulse_dt`

```c
static int pwm_set_pulse_dt(const struct pwm_dt_spec *spec, uint32_t pulse)
```

根据 `struct pwm_dt_spec` 以纳秒设置周期与脉宽。

定义位置（Definition）：pwm.h:727。

符号定位：[pwm_set_pulse_dt](../hardware/P255_PWM公共接口.md#ga8ff263177143d33c6d0a284b837bc4da)。

### `pwm_configure_capture`

```c
static int pwm_configure_capture(const struct device *dev, uint32_t channel, pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data)
```

为单个 PWM 输入配置周期／脉宽捕获。

定义位置（Definition）：pwm.h:827。

符号定位：[pwm_configure_capture](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)。

### `pwm_enable_capture`

```c
int pwm_enable_capture(const struct device *dev, uint32_t channel)
```

为单个 PWM 输入启用周期／脉宽捕获。

符号定位：[pwm_enable_capture](../hardware/P255_PWM公共接口.md#gad14ca53862a465d1789e8936ce394f9a)。

### `pwm_set`

```c
static int pwm_set(const struct device *dev, uint32_t channel, uint32_t period, uint32_t pulse, pwm_flags_t flags)
```

以纳秒（Nanoseconds）为单位设置单个 PWM 输出的周期与脉宽。

定义位置（Definition）：pwm.h:660。

符号定位：[pwm_set](../hardware/P255_PWM公共接口.md#gadd9049c9a56cd9419736b3514e42dc01)。

### `pwm_flags_t`

```c
uint16_t pwm_flags_t
```

提供保存 PWM 配置标志的类型。

定义位置（Definition）：pwm.h:116。

符号定位：[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)。

### `pwm_cycles_to_usec`

```c
static int pwm_cycles_to_usec(const struct device *dev, uint32_t channel, uint32_t cycles, uint64_t *usec)
```

将 PWM 时钟周期数转换为微秒（Microseconds）。

定义位置（Definition）：pwm.h:745。

符号定位：[pwm_cycles_to_usec](../hardware/P255_PWM公共接口.md#gae57fb205e43dde82d96abe79966539a9)。

### `pwm_event_callback_handler_t`

```c
void(* pwm_event_callback_handler_t)(const struct device *dev, struct pwm_event_callback *callback, uint32_t channel, pwm_events_t events)
```

PWM 事件回调处理函数的签名。

定义位置（Definition）：pwm.h:456。

符号定位：[pwm_event_callback_handler_t](../hardware/P255_PWM公共接口.md#gaedacc300332a9c01da48671f92bf0097)。

### `pwm_init_event_callback`

```c
static void pwm_init_event_callback(struct pwm_event_callback *callback, pwm_event_callback_handler_t handler, uint32_t channel, pwm_events_t event_mask)
```

帮助正确初始化 `struct pwm_event_callback` 的辅助函数。

定义位置（Definition）：pwm.h:1059。

符号定位：[pwm_init_event_callback](../hardware/P255_PWM公共接口.md#gaf87ef431d50a482910e77e49d52a2e13)。

### `pwm_set_cycles`

```c
int pwm_set_cycles(const struct device *dev, uint32_t channel, uint32_t period, uint32_t pulse, pwm_flags_t flags)
```

为单个 PWM 输出设置周期与脉宽。

符号定位：[pwm_set_cycles](../hardware/P255_PWM公共接口.md#gaff280789f7b45fdefc354b3f841fe3ef)。

### `sys_snode_t`

```c
struct _snode sys_snode_t
```

单向链表节点（Singly Linked List Node）结构。

定义位置（Definition）：slist.h:44。

符号定位：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)。

### `EINVAL`

```c
#define EINVAL
```

参数无效（Invalid Argument）。

定义位置（Definition）：errno.h:61。

符号定位：[EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)。

### `ENOSYS`

```c
#define ENOSYS
```

功能未实现（Function Not Implemented）。

定义位置（Definition）：errno.h:83。

符号定位：[ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)。

### `ENOTSUP`

```c
#define ENOTSUP
```

不支持的值（Unsupported Value）。

定义位置（Definition）：errno.h:115。

符号定位：[ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)。

### `ERANGE`

```c
#define ERANGE
```

结果过大（Result Too Large）。

定义位置（Definition）：errno.h:73。

符号定位：[ERANGE](../error_reference/P003_系统错误号公共接口.md#gaa1591a4f3a86360108de5b9ba34980ca)。

### `math_extras.h`

附加的算术与位操作函数。

符号定位：[math_extras.h](../math_reference/P002_数学辅助头文件参考.md)。

### `flags`

```c
flags
```

定义位置（Definition）：parser.h:86。

符号定位：[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

### `slist.h`

单向链表API头文件。

符号定位：[slist.h](../slist_reference/P002_单向链表头文件参考.md)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint64_t`

```c
__UINT64_TYPE__ uint64_t
```

定义位置（Definition）：stdint.h:91。

符号定位：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `UINT32_MAX`

```c
#define UINT32_MAX
```

定义位置（Definition）：stdint.h:29。

符号定位：[UINT32_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `k_timeout_t`

内核超时类型（Kernel Timeout Type）。

定义位置（Definition）：clock.h:65。

符号定位：[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

### `pwm_driver_api`

驱动操作（Driver Operations）：PWM驱动操作；原提示包含格式标签。

定义位置（Definition）：pwm.h:542。

符号定位：[pwm_driver_api](../hardware/P259_PWM驱动函数表.md)。

### `pwm_driver_api::get_cycles_per_sec`

```c
pwm_get_cycles_per_sec_t get_cycles_per_sec
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:550。

符号定位：[pwm_driver_api::get_cycles_per_sec](../hardware/P259_PWM驱动函数表.md#a365761817898baf5ea52eb1ad63d67a6)。

### `pwm_driver_api::configure_capture`

```c
pwm_configure_capture_t configure_capture
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:556。

符号定位：[pwm_driver_api::configure_capture](../hardware/P259_PWM驱动函数表.md#a4d4b8080814e092e2bc5ac0a47baa182)。

### `pwm_driver_api::set_cycles`

```c
pwm_set_cycles_t set_cycles
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:546。

符号定位：[pwm_driver_api::set_cycles](../hardware/P259_PWM驱动函数表.md#a5d4e7cb7f3610fcc7a9981baf4ec3654)。

### `pwm_driver_api::disable_capture`

```c
pwm_disable_capture_t disable_capture
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:566。

符号定位：[pwm_driver_api::disable_capture](../hardware/P259_PWM驱动函数表.md#a6b210f5e68353aef9594c2c585360e47)。

### `pwm_driver_api::manage_event_callback`

```c
pwm_manage_event_callback_t manage_event_callback
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:573。

符号定位：[pwm_driver_api::manage_event_callback](../hardware/P259_PWM驱动函数表.md#aa97c7710a29e69af934e3b0f259c11b8)。

### `pwm_driver_api::enable_capture`

```c
pwm_enable_capture_t enable_capture
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：pwm.h:561。

符号定位：[pwm_driver_api::enable_capture](../hardware/P259_PWM驱动函数表.md#afedf4abee4341fde838eedb962d34368)。

### `pwm_dt_spec`

保存设备树（Devicetree）中指定的 PWM 信息的容器。

定义位置（Definition）：pwm.h:141。

符号定位：[pwm_dt_spec](../hardware/P256_PWM设备树描述.md)。

### `pwm_dt_spec::flags`

```c
pwm_flags_t flags
```

标志（Flags）。

定义位置（Definition）：pwm.h:149。

符号定位：[pwm_dt_spec::flags](../hardware/P256_PWM设备树描述.md#a2ddb45cbde80314a5a50dffe2e43921b)。

### `pwm_dt_spec::channel`

```c
uint32_t channel
```

通道编号（Channel Number）。

定义位置（Definition）：pwm.h:145。

符号定位：[pwm_dt_spec::channel](../hardware/P256_PWM设备树描述.md#a739a2672afa1d56ec1d865d6d5be47b2)。

### `pwm_dt_spec::period`

```c
uint32_t period
```

以纳秒为单位的周期。

定义位置（Definition）：pwm.h:147。

符号定位：[pwm_dt_spec::period](../hardware/P256_PWM设备树描述.md#a935c72595e2248ab75ce0c43a394c0b3)。

### `pwm_dt_spec::dev`

```c
const struct device * dev
```

PWM设备实例（Device Instance）。

定义位置（Definition）：pwm.h:143。

符号定位：[pwm_dt_spec::dev](../hardware/P256_PWM设备树描述.md#ad9f2991bcf978940e638d17c5e17311e)。

### `pwm_event_callback`

PWM 事件回调（Event Callback）结构。

定义位置（Definition）：pwm.h:471。

符号定位：[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)。

### `pwm_event_callback::channel`

```c
uint32_t channel
```

回调关注的通道。

定义位置（Definition）：pwm.h:480。

符号定位：[pwm_event_callback::channel](../hardware/P257_PWM事件回调结构.md#a0f14cc1f7e4735e88f28ff4cfecbcec5)。

### `pwm_event_callback::event_mask`

```c
pwm_events_t event_mask
```

回调关注的事件掩码（Event Mask）。

定义位置（Definition）：pwm.h:483。

符号定位：[pwm_event_callback::event_mask](../hardware/P257_PWM事件回调结构.md#a304e9ea24d4eb8f5d618aea8c3600223)。

### `pwm_event_callback::handler`

```c
pwm_event_callback_handler_t handler
```

发生相关事件时实际调用的回调函数。

定义位置（Definition）：pwm.h:477。

符号定位：[pwm_event_callback::handler](../hardware/P257_PWM事件回调结构.md#a56f5f3b2589dffb88a8d893fe7d259ab)。

### `toolchain.h`

用于抽象工具链（Toolchain）特有能力的宏。

符号定位：[toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)。

## 2.4\_源码跟踪译注

> 译注——设备树对象与回退：pwm_dt_spec静态初始化器保存设备指针、通道、纳秒周期和标志，不启动PWM。BY_NAME_OR和BY_IDX_OR都只检查节点是否具有pwms属性；属性存在但名称或索引无效时，不会自动选择default_value。实例版静态初始化宏先转换为节点再调用节点版，flags因而经过DT_PWMS_FLAGS_BY_NAME／BY_IDX的缺省0路径，不能与直接调用DT_INST_PWMS_FLAGS系列混为一谈。

> 译注——单位与数值：pwm_set_cycles接收硬件时钟周期数，公共实现先拒绝pulse大于period。pwm_set接收纳秒，查询驱动时钟速率后做整数乘除，结果超过32位周期计数时返回-ENOTSUP；整数除法可能截断，因此最终波形受硬件分辨率约束。pwm_set_dt采用调用方周期，pwm_set_pulse_dt采用spec中的周期，二者均沿用spec标志。

> 译注——换算与错误：pwm_cycles_to_usec／nsec先查询时钟速率，再以u64_mul_overflow检查乘法，溢出返回-ERANGE，否则整数除法换算。驱动返回的时钟速率必须可用于除法；这些包装函数没有独立的零频率检查。捕获的usec／nsec包装先取得周期计数，再依次换算周期与脉宽；失败时立即返回，不保证两个输出均已更新。按当前可见实现，不应把NULL输出指针当作这些时间单位包装函数通用支持的省略方式。

> 译注——编译选项与驱动实现：捕获相关操作受CONFIG_PWM_CAPTURE约束，事件操作受CONFIG_PWM_EVENT约束；__DOXYGEN__分支让文档能展示可选接口，不代表当前固件已开启它们。当前Kconfig将PWM_EVENT标为实验功能（Experimental）。configure_capture、enable_capture、disable_capture和manage_event_callback在包装层检查空函数指针并可返回-ENOSYS；基础set_cycles和get_cycles_per_sec则按必需驱动操作直接调用。

> 译注——事件回调与就绪：pwm_init_event_callback检查回调及处理函数并写入handler、channel、event_mask，不注册回调，也不分配回调对象。添加／删除函数分别把true／false传给驱动的manage_event_callback；对象生存期和驱动行为仍需遵守完整API约定。pwm_is_ready_dt只调用device_is_ready(spec->dev)，不验证通道范围、周期可实现性、输出引脚连接或捕获支持。

> 译注——版本边界：本批记录驱动主头文件、PWM绑定常量、PWM设备树宏、驱动Kconfig及控制器公共绑定五份官方源码摘要。源码页非注释代码与读取的原始头文件一致；latest、滚动main和仓库参照版本不自动等同。仓库链接仅作相对源码定位，未构建固件、输出波形或操作硬件。

头文件相对定位：[include/zephyr/drivers/pwm.h](../../../include/zephyr/drivers/pwm.h)，关联实现／接口：[drivers/pwm/Kconfig](../../../drivers/pwm/Kconfig)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/pwm.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、输出PWM波形、捕获信号或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_PWM驱动头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/math_extras.h](../math_reference/P002_数学辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/dt-bindings/pwm/pwm.h](../dt_pwm_binding_reference/P003_PWM绑定常量头文件参考.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)
- [pwm_dt_spec](../hardware/P256_PWM设备树描述.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../hardware/P256_PWM设备树描述.md#ad9f2991bcf978940e638d17c5e17311e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [channel](../hardware/P256_PWM设备树描述.md#a739a2672afa1d56ec1d865d6d5be47b2)
- [period](../hardware/P256_PWM设备树描述.md#a935c72595e2248ab75ce0c43a394c0b3)
- [flags](../hardware/P256_PWM设备树描述.md#a2ddb45cbde80314a5a50dffe2e43921b)
- [pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)
- [pwm_event_callback](../hardware/P257_PWM事件回调结构.md)
- [pwm_event_callback_handler_t](../hardware/P255_PWM公共接口.md#gaedacc300332a9c01da48671f92bf0097)
- [channel](../hardware/P257_PWM事件回调结构.md#a0f14cc1f7e4735e88f28ff4cfecbcec5)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [handler](../hardware/P257_PWM事件回调结构.md#a56f5f3b2589dffb88a8d893fe7d259ab)
- [event_mask](../hardware/P257_PWM事件回调结构.md#a304e9ea24d4eb8f5d618aea8c3600223)
- [pwm_set_cycles_t](../hardware/P258_PWM驱动后端接口.md#ga284f0aa783ab2f457b2239a87a9c1671)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [pwm_get_cycles_per_sec_t](../hardware/P258_PWM驱动后端接口.md#ga6330ac4e97604ab4510c16a3c4d0437f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pwm_configure_capture_t](../hardware/P258_PWM驱动后端接口.md#ga8dedee6071801685cb618bacd8b51c57)
- [pwm_enable_capture_t](../hardware/P258_PWM驱动后端接口.md#gaae83bb7862c019492c8bc154015f8e8c)
- [pwm_disable_capture_t](../hardware/P258_PWM驱动后端接口.md#ga471b1f0ed9992e372f1f01683b68f456)
- [pwm_manage_event_callback_t](../hardware/P258_PWM驱动后端接口.md#ga70ab8cd3c6d7b43890655405b3e6db3f)
- [pwm_driver_api](../hardware/P259_PWM驱动函数表.md)
- [set_cycles](../hardware/P259_PWM驱动函数表.md#a5d4e7cb7f3610fcc7a9981baf4ec3654)
- [get_cycles_per_sec](../hardware/P259_PWM驱动函数表.md#a365761817898baf5ea52eb1ad63d67a6)
- [configure_capture](../hardware/P259_PWM驱动函数表.md#a4d4b8080814e092e2bc5ac0a47baa182)
- [enable_capture](../hardware/P259_PWM驱动函数表.md#afedf4abee4341fde838eedb962d34368)
- [disable_capture](../hardware/P259_PWM驱动函数表.md#a6b210f5e68353aef9594c2c585360e47)
- [manage_event_callback](../hardware/P259_PWM驱动函数表.md#aa97c7710a29e69af934e3b0f259c11b8)
- [pwm_set_cycles](../hardware/P255_PWM公共接口.md#gaff280789f7b45fdefc354b3f841fe3ef)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [pwm_get_cycles_per_sec](../hardware/P255_PWM公共接口.md#ga310d416087a619f90e946222668135af)
- [pwm_set](../hardware/P255_PWM公共接口.md#gadd9049c9a56cd9419736b3514e42dc01)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [UINT32_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [pwm_set_dt](../hardware/P255_PWM公共接口.md#ga225ce58ceb3de3d76df3e03439d655b9)
- [pwm_set_pulse_dt](../hardware/P255_PWM公共接口.md#ga8ff263177143d33c6d0a284b837bc4da)
- [pwm_cycles_to_usec](../hardware/P255_PWM公共接口.md#gae57fb205e43dde82d96abe79966539a9)
- [u64_mul_overflow](../math_reference/P001_数学辅助公共接口.md#ga366f6606874071677bf9079647d9abce)
- [USEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga6a69d6cbdab5f24c2e66959293f210c1)
- [ERANGE](../error_reference/P003_系统错误号公共接口.md#gaa1591a4f3a86360108de5b9ba34980ca)
- [pwm_cycles_to_nsec](../hardware/P255_PWM公共接口.md#ga6f0281398611dd876386c66a63373a2e)
- [pwm_configure_capture](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [pwm_enable_capture](../hardware/P255_PWM公共接口.md#gad14ca53862a465d1789e8936ce394f9a)
- [pwm_disable_capture](../hardware/P255_PWM公共接口.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)
- [pwm_capture_cycles](../hardware/P255_PWM公共接口.md#ga09767ae3c8d970675dbf9e3e50291743)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pwm_capture_usec](../hardware/P255_PWM公共接口.md#ga3a1552ea924eeec21477396da6d3890b)
- [pwm_capture_nsec](../hardware/P255_PWM公共接口.md#ga6489095d890224d23c5ed05bc884d24a)
- [pwm_init_event_callback](../hardware/P255_PWM公共接口.md#gaf87ef431d50a482910e77e49d52a2e13)
- [pwm_add_event_callback](../hardware/P255_PWM公共接口.md#ga09d1b358df32e798e0345cd647450d54)
- [pwm_remove_event_callback](../hardware/P255_PWM公共接口.md#ga83d9ec60d3fef69c97602365b979aece)
- [pwm_is_ready_dt](../hardware/P255_PWM公共接口.md#ga70aad0d88e8041c880499e7cdaa9ae57)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)

---

[上一章](P001_PWM驱动头文件参考.md) · [返回大纲](大纲.md)
