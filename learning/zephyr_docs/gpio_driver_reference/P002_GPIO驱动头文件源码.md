---
id: learning.zephyr-docs.gpio-driver-reference.page-2
title: GPIO驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2gpio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GPIO驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2gpio_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_GPIO驱动头文件参考.md)和[公共API](../hardware/P266_GPIO公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00081"></a>
<a id="foldopen00085"></a>
<a id="foldopen00168"></a>
<a id="foldopen00175"></a>
<a id="foldopen00182"></a>
<a id="foldopen00190"></a>
<a id="foldopen00196"></a>
<a id="foldopen00202"></a>
<a id="foldopen00210"></a>
<a id="foldopen00218"></a>
<a id="foldopen00225"></a>
<a id="foldopen00296"></a>
<a id="foldopen00339"></a>
<a id="foldopen00363"></a>
<a id="foldopen00376"></a>
<a id="foldopen00389"></a>
<a id="foldopen00402"></a>
<a id="foldopen00416"></a>
<a id="foldopen00429"></a>
<a id="foldopen00442"></a>
<a id="foldopen00574"></a>
<a id="foldopen00591"></a>
<a id="foldopen00603"></a>
<a id="foldopen00614"></a>
<a id="foldopen00665"></a>
<a id="foldopen00685"></a>
<a id="foldopen00708"></a>
<a id="foldopen00722"></a>
<a id="foldopen00735"></a>
<a id="foldopen00771"></a>
<a id="foldopen00801"></a>
<a id="foldopen00825"></a>
<a id="foldopen00934"></a>
<a id="foldopen00982"></a>
<a id="foldopen01106"></a>
<a id="foldopen01208"></a>
<a id="foldopen01270"></a>
<a id="foldopen01298"></a>
<a id="foldopen01315"></a>
<a id="foldopen01343"></a>
<a id="foldopen01405"></a>
<a id="foldopen01796"></a>
<a id="foldopen01887"></a>
<a id="foldopen01924"></a>
<a id="foldopen01935"></a>
<a id="foldopen01963"></a>
<a id="foldopen01992"></a>
<a id="foldopen02015"></a>
<a id="foldopen02044"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adt-bindings_2gpio_2gpio_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__gpio__interface__backend_html_ga0b30055e6722031df85b712b6b151710"></a>
<a id="agroup__gpio__interface__backend_html_ga2a4ec98edb4dfb38cde49ab796fcbff3"></a>
<a id="agroup__gpio__interface__backend_html_ga2aaa71c0dd3728fdd2f8bd111245c456"></a>
<a id="agroup__gpio__interface__backend_html_ga43e339579ea19b4cc7d90a04c208e587"></a>
<a id="agroup__gpio__interface__backend_html_ga4ea6fd78423e6e3004702b599bc7b12d"></a>
<a id="agroup__gpio__interface__backend_html_ga5d175c3355e88ee78b08539b61fc84fd"></a>
<a id="agroup__gpio__interface__backend_html_ga6e7f6f2052ba10b6482445faaef4245f"></a>
<a id="agroup__gpio__interface__backend_html_ga82f0562c44cf0f76cc7e16d606a975db"></a>
<a id="agroup__gpio__interface__backend_html_ga8486f9d9925531757b49e745ca7fdab2"></a>
<a id="agroup__gpio__interface__backend_html_gab3d809d4ffbba78cfad45bcdb8f5ce5a"></a>
<a id="agroup__gpio__interface__backend_html_gabca79087ebe1c21911ef9a80eaaee43e"></a>
<a id="agroup__gpio__interface__backend_html_gad31b73d23fa7f6c96ec2f4a2523d61fb"></a>
<a id="agroup__gpio__interface__backend_html_gafa0e73e50f77890699cfe1a04ed9f155"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134"></a>
<a id="agroup__gpio__interface__backend_html_gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6"></a>
<a id="agroup__gpio__interface__backend_html_gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e"></a>
<a id="agroup__gpio__interface__backend_html_gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0"></a>
<a id="agroup__gpio__interface__backend_html_gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3"></a>
<a id="agroup__gpio__interface__backend_html_gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688"></a>
<a id="agroup__gpio__interface__backend_html_gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9"></a>
<a id="agroup__gpio__interface_html_ga05fd15af20386d69f9332354285b0cca"></a>
<a id="agroup__gpio__interface_html_ga08824e05ea87c4ad2e48edaa13aad30a"></a>
<a id="agroup__gpio__interface_html_ga0c5ddbec7eb194ffed6cf12ae235ae04"></a>
<a id="agroup__gpio__interface_html_ga0db9fe8a278e6ab7c5c6f14fe58e5eb1"></a>
<a id="agroup__gpio__interface_html_ga133284b60a13c6dc50b87c1d04259f5e"></a>
<a id="agroup__gpio__interface_html_ga1449ba90eaec5e6144fe4faae21f2e3f"></a>
<a id="agroup__gpio__interface_html_ga1454bc223fc2200aff3c4aab7d747da2"></a>
<a id="agroup__gpio__interface_html_ga18e6ca0df95566fecc0633efb04a075a"></a>
<a id="agroup__gpio__interface_html_ga1a06f729e76d39937d0572b6c531e038"></a>
<a id="agroup__gpio__interface_html_ga2255c5681d17952ab89a4b6016d8e80d"></a>
<a id="agroup__gpio__interface_html_ga24f0b4ad30e6a8c81f51a2813478c793"></a>
<a id="agroup__gpio__interface_html_ga2c9f8fee2addfc0aeeeeb011d534f304"></a>
<a id="agroup__gpio__interface_html_ga3272e866489da6c2e12c48f803c59e81"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="agroup__gpio__interface_html_ga3b854d759180e222299ea445b401acc1"></a>
<a id="agroup__gpio__interface_html_ga3f9e45de172a27f49c31a072c0c241e1"></a>
<a id="agroup__gpio__interface_html_ga423db4f985098ddcaa504ec430e91913"></a>
<a id="agroup__gpio__interface_html_ga45172f2b1bb09e8f3c89fa951cdefc14"></a>
<a id="agroup__gpio__interface_html_ga496cd45fd6a2826c75d70c71f967234b"></a>
<a id="agroup__gpio__interface_html_ga541064fb9e575c0c559c101754466fa8"></a>
<a id="agroup__gpio__interface_html_ga54845eb95bc9636c3e6ff285300b6979"></a>
<a id="agroup__gpio__interface_html_ga5f5cb5e7dae6d58e072bb450af029d2e"></a>
<a id="agroup__gpio__interface_html_ga62cea8989df2425e5e5e712217d65f46"></a>
<a id="agroup__gpio__interface_html_ga635975f1df6157c7e8a6c67bac55fbc0"></a>
<a id="agroup__gpio__interface_html_ga644109ce84c8feffe1226b9b50122a96"></a>
<a id="agroup__gpio__interface_html_ga7a7dd7c1f3a2135a9f378e1c34b6232c"></a>
<a id="agroup__gpio__interface_html_ga7aaec28a83cac63bd87fc94cc72664b1"></a>
<a id="agroup__gpio__interface_html_ga7be6a0cc9aa65da1d4ee5751b4085853"></a>
<a id="agroup__gpio__interface_html_ga7c7a53371834c7646dc7f41ca0bb7921"></a>
<a id="agroup__gpio__interface_html_ga7f40ed51f14fd8000e9b52ab347b273f"></a>
<a id="agroup__gpio__interface_html_ga820448aa4be8b14839bc6a00c9f34bb4"></a>
<a id="agroup__gpio__interface_html_ga82977d8706fb9f464db455bd0e9ac2e4"></a>
<a id="agroup__gpio__interface_html_ga91657faac28f9b213105dd61a419dd5a"></a>
<a id="agroup__gpio__interface_html_ga9318c349663568f1fb9400b9458765dc"></a>
<a id="agroup__gpio__interface_html_ga9618f254365381063439a0e9c5e787cb"></a>
<a id="agroup__gpio__interface_html_ga9d2c9daeec7ce127fc786ead566ad27f"></a>
<a id="agroup__gpio__interface_html_ga9e7b50d720fda362941acc1e3b3b2922"></a>
<a id="agroup__gpio__interface_html_gaa761788e22a185db227dce7c24915154"></a>
<a id="agroup__gpio__interface_html_gaaa7921da231fd2b96575fa522e2c1970"></a>
<a id="agroup__gpio__interface_html_gaabeb2d0d98856c7ff78be36651d6bbc1"></a>
<a id="agroup__gpio__interface_html_gaaec9ad17c08a0d527d66445fe82d8327"></a>
<a id="agroup__gpio__interface_html_gab7465c5401aa9d47d68980455847be9f"></a>
<a id="agroup__gpio__interface_html_gabcebe24c93486896e1dfc2459ec25693"></a>
<a id="agroup__gpio__interface_html_gac1e94ba8faac79f469447e9b5d2f8c06"></a>
<a id="agroup__gpio__interface_html_gad2b2945dbe6987ac425e000721a894c4"></a>
<a id="agroup__gpio__interface_html_gad435719dccdc37c05852960a7218fbd2"></a>
<a id="agroup__gpio__interface_html_gadac09ef40fc1ba5d8bb40965efde0fda"></a>
<a id="agroup__gpio__interface_html_gadec1802e074f3021d464da09cd66c7cf"></a>
<a id="agroup__gpio__interface_html_gae2a49b36cae2e17fc665a3bd844f50b4"></a>
<a id="agroup__gpio__interface_html_gae450ff904686aa4b8fd81bc0dbbafdb5"></a>
<a id="agroup__gpio__interface_html_gaed4a2051d76db7eead8ed1719ce2ba33"></a>
<a id="agroup__gpio__interface_html_gaf0aa40279d32b1b8332f2f23a39510af"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__subsys__tracing__macros_html_ga445bcac4cec53d560ddca757de17e1e3"></a>
<a id="agroup__subsys__tracing__macros_html_gab0350eef3ed26733e57505ee2d0487cb"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructgpio__callback_html"></a>
<a id="astructgpio__callback_html_ab60e7093072964bd818d536c746211e4"></a>
<a id="astructgpio__callback_html_ace5c2b83f1d51f73877a1f2c54ba8c67"></a>
<a id="astructgpio__callback_html_af89dc41cbd610d81ac03cae7ab764ceb"></a>
<a id="astructgpio__driver__api_html"></a>
<a id="astructgpio__driver__api_html_a12abf1e8eaa9e92af931b1045fe0e377"></a>
<a id="astructgpio__driver__api_html_a1c66d09d500fbed09cf9c85973dc9bcf"></a>
<a id="astructgpio__driver__api_html_a2663c69ada10dd209cc2f266b733c97c"></a>
<a id="astructgpio__driver__api_html_a676651f5ef63de226e244ffe7a6c0ece"></a>
<a id="astructgpio__driver__api_html_a6b79f508317faa0f2959fe63449534c5"></a>
<a id="astructgpio__driver__api_html_a77fbd18d3c4d7f48f3f640a80d8b0555"></a>
<a id="astructgpio__driver__api_html_a7e4adc56ec0cb667cf4d4f711de52be4"></a>
<a id="astructgpio__driver__api_html_a92cdd5aeab396e756773cb00dbe87c33"></a>
<a id="astructgpio__driver__api_html_abdc60c3175e972aef218978ea5ad6c38"></a>
<a id="astructgpio__driver__api_html_ad8ceab5ca80067db8d7c8be884ac9de1"></a>
<a id="astructgpio__driver__api_html_af1d1268ef57bcedce138c64b95ba2878"></a>
<a id="astructgpio__driver__config_html"></a>
<a id="astructgpio__driver__config_html_af73c0d9d433b86b9d0e0c6703e737052"></a>
<a id="astructgpio__driver__data_html"></a>
<a id="astructgpio__driver__data_html_ab62038a3c7c341cafda6665dfab3f169"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructgpio__dt__spec_html_a5d617d47e2f568c7a4402a8f5a40ed4f"></a>
<a id="astructgpio__dt__spec_html_ad7e6fbb0cba0be94a47d4f2add056c84"></a>
<a id="astructgpio__dt__spec_html_ae3b90e7e22708798c67da94f72ad1ab0"></a>
<a id="atracing_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019-2020 Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2019 Piotr Mienkowski
<a id="l00004"></a> * Copyright (c) 2017 ARM Ltd
<a id="l00005"></a> * Copyright (c) 2015-2016 Intel Corporation.
<a id="l00006"></a> *
<a id="l00007"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00008"></a> */
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_H_
<a id="l00017"></a>#define ZEPHYR_INCLUDE_DRIVERS_GPIO_H_
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;errno.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#include &lt;zephyr/sys/__assert.h&gt;
<a id="l00022"></a>#include &lt;zephyr/sys/slist.h&gt;
<a id="l00023"></a>#include &lt;zephyr/tracing/tracing.h&gt;
<a id="l00024"></a>
<a id="l00025"></a>#include &lt;zephyr/types.h&gt;
<a id="l00026"></a>#include &lt;stddef.h&gt;
<a id="l00027"></a>#include &lt;zephyr/device.h&gt;
<a id="l00028"></a>#include &lt;zephyr/dt-bindings/gpio/gpio.h&gt;
<a id="l00029"></a>
<a id="l00030"></a>#ifdef __cplusplus
<a id="l00031"></a>extern "C" {
<a id="l00032"></a>#endif
<a id="l00033"></a>
<a id="l00048"></a>
<a id="l00053"></a>
<a id="l00055"></a>#define GPIO_INPUT              BIT(16)
<a id="l00056"></a>
<a id="l00058"></a>#define GPIO_OUTPUT             BIT(17)
<a id="l00059"></a>
<a id="l00061"></a>#define GPIO_DISCONNECTED       0
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>/* Initializes output to a low state. */
<a id="l00066"></a>#define GPIO_OUTPUT_INIT_LOW    BIT(18)
<a id="l00067"></a>
<a id="l00068"></a>/* Initializes output to a high state. */
<a id="l00069"></a>#define GPIO_OUTPUT_INIT_HIGH   BIT(19)
<a id="l00070"></a>
<a id="l00071"></a>/* Initializes output based on logic level */
<a id="l00072"></a>#define GPIO_OUTPUT_INIT_LOGICAL BIT(20)
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>#define GPIO_OUTPUT_LOW         (GPIO_OUTPUT | GPIO_OUTPUT_INIT_LOW)
<a id="l00079"></a>#define GPIO_OUTPUT_HIGH        (GPIO_OUTPUT | GPIO_OUTPUT_INIT_HIGH)
<a id="l00081"></a>#define GPIO_OUTPUT_INACTIVE    (GPIO_OUTPUT |                  \
<a id="l00082"></a>                                 GPIO_OUTPUT_INIT_LOW |         \
<a id="l00083"></a>                                 GPIO_OUTPUT_INIT_LOGICAL)
<a id="l00084"></a>
<a id="l00085"></a>#define GPIO_OUTPUT_ACTIVE      (GPIO_OUTPUT |                  \
<a id="l00086"></a>                                 GPIO_OUTPUT_INIT_HIGH |        \
<a id="l00087"></a>                                 GPIO_OUTPUT_INIT_LOGICAL)
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00106"></a>
<a id="l00108"></a>#define GPIO_INT_DISABLE               BIT(21)
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>/* Enables GPIO pin interrupt. */
<a id="l00113"></a>#define GPIO_INT_ENABLE                BIT(22)
<a id="l00114"></a>
<a id="l00115"></a>/* GPIO interrupt is sensitive to logical levels.
<a id="l00116"></a> *
<a id="l00117"></a> * This is a component flag that should be combined with other
<a id="l00118"></a> * `GPIO_INT_*` flags to produce a meaningful configuration.
<a id="l00119"></a> */
<a id="l00120"></a>#define GPIO_INT_LEVELS_LOGICAL        BIT(23)
<a id="l00121"></a>
<a id="l00122"></a>/* GPIO interrupt is edge sensitive.
<a id="l00123"></a> *
<a id="l00124"></a> * Note: by default interrupts are level sensitive.
<a id="l00125"></a> *
<a id="l00126"></a> * This is a component flag that should be combined with other
<a id="l00127"></a> * `GPIO_INT_*` flags to produce a meaningful configuration.
<a id="l00128"></a> */
<a id="l00129"></a>#define GPIO_INT_EDGE                  BIT(24)
<a id="l00130"></a>
<a id="l00131"></a>/* Trigger detection when input state is (or transitions to) physical low or
<a id="l00132"></a> * logical 0 level.
<a id="l00133"></a> *
<a id="l00134"></a> * This is a component flag that should be combined with other
<a id="l00135"></a> * `GPIO_INT_*` flags to produce a meaningful configuration.
<a id="l00136"></a> */
<a id="l00137"></a>#define GPIO_INT_LOW_0                 BIT(25)
<a id="l00138"></a>
<a id="l00139"></a>/* Trigger detection on input state is (or transitions to) physical high or
<a id="l00140"></a> * logical 1 level.
<a id="l00141"></a> *
<a id="l00142"></a> * This is a component flag that should be combined with other
<a id="l00143"></a> * `GPIO_INT_*` flags to produce a meaningful configuration.
<a id="l00144"></a> */
<a id="l00145"></a>#define GPIO_INT_HIGH_1                BIT(26)
<a id="l00146"></a>
<a id="l00147"></a>#ifdef CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT
<a id="l00148"></a>/* Disable/Enable interrupt functionality without changing other interrupt
<a id="l00149"></a> * related register, such as clearing the pending register.
<a id="l00150"></a> *
<a id="l00151"></a> * This is a component flag that should be combined with `GPIO_INT_ENABLE` or
<a id="l00152"></a> * `GPIO_INT_DISABLE` flags to produce a meaningful configuration.
<a id="l00153"></a> */
<a id="l00154"></a>#define GPIO_INT_ENABLE_DISABLE_ONLY   BIT(27)
<a id="l00155"></a>#endif /* CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT */
<a id="l00156"></a>
<a id="l00157"></a>#define GPIO_INT_MASK                  (GPIO_INT_DISABLE | \
<a id="l00158"></a>                                        GPIO_INT_ENABLE | \
<a id="l00159"></a>                                        GPIO_INT_LEVELS_LOGICAL | \
<a id="l00160"></a>                                        GPIO_INT_EDGE | \
<a id="l00161"></a>                                        GPIO_INT_LOW_0 | \
<a id="l00162"></a>                                        GPIO_INT_HIGH_1)
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00168"></a>#define GPIO_INT_EDGE_RISING           (GPIO_INT_ENABLE | \
<a id="l00169"></a>                                        GPIO_INT_EDGE | \
<a id="l00170"></a>                                        GPIO_INT_HIGH_1)
<a id="l00171"></a>
<a id="l00175"></a>#define GPIO_INT_EDGE_FALLING          (GPIO_INT_ENABLE | \
<a id="l00176"></a>                                        GPIO_INT_EDGE | \
<a id="l00177"></a>                                        GPIO_INT_LOW_0)
<a id="l00178"></a>
<a id="l00182"></a>#define GPIO_INT_EDGE_BOTH             (GPIO_INT_ENABLE | \
<a id="l00183"></a>                                        GPIO_INT_EDGE | \
<a id="l00184"></a>                                        GPIO_INT_LOW_0 | \
<a id="l00185"></a>                                        GPIO_INT_HIGH_1)
<a id="l00186"></a>
<a id="l00190"></a>#define GPIO_INT_LEVEL_LOW             (GPIO_INT_ENABLE | \
<a id="l00191"></a>                                        GPIO_INT_LOW_0)
<a id="l00192"></a>
<a id="l00196"></a>#define GPIO_INT_LEVEL_HIGH            (GPIO_INT_ENABLE | \
<a id="l00197"></a>                                        GPIO_INT_HIGH_1)
<a id="l00198"></a>
<a id="l00202"></a>#define GPIO_INT_EDGE_TO_INACTIVE      (GPIO_INT_ENABLE | \
<a id="l00203"></a>                                        GPIO_INT_LEVELS_LOGICAL | \
<a id="l00204"></a>                                        GPIO_INT_EDGE | \
<a id="l00205"></a>                                        GPIO_INT_LOW_0)
<a id="l00206"></a>
<a id="l00210"></a>#define GPIO_INT_EDGE_TO_ACTIVE        (GPIO_INT_ENABLE | \
<a id="l00211"></a>                                        GPIO_INT_LEVELS_LOGICAL | \
<a id="l00212"></a>                                        GPIO_INT_EDGE | \
<a id="l00213"></a>                                        GPIO_INT_HIGH_1)
<a id="l00214"></a>
<a id="l00218"></a>#define GPIO_INT_LEVEL_INACTIVE        (GPIO_INT_ENABLE | \
<a id="l00219"></a>                                        GPIO_INT_LEVELS_LOGICAL | \
<a id="l00220"></a>                                        GPIO_INT_LOW_0)
<a id="l00221"></a>
<a id="l00225"></a>#define GPIO_INT_LEVEL_ACTIVE          (GPIO_INT_ENABLE | \
<a id="l00226"></a>                                        GPIO_INT_LEVELS_LOGICAL | \
<a id="l00227"></a>                                        GPIO_INT_HIGH_1)
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>#define GPIO_DIR_MASK           (GPIO_INPUT | GPIO_OUTPUT)
<a id="l00234"></a>
<a id="l00241"></a>typedef uint32_t gpio_port_pins_t;
<a id="l00242"></a>
<a id="l00254"></a>typedef uint32_t gpio_port_value_t;
<a id="l00255"></a>
<a id="l00262"></a>typedef uint8_t gpio_pin_t;
<a id="l00263"></a>
<a id="l00274"></a>typedef uint16_t gpio_dt_flags_t;
<a id="l00275"></a>
<a id="l00282"></a>typedef uint32_t gpio_flags_t;
<a id="l00283"></a>
<a id="l00296"></a>struct gpio_dt_spec {
<a id="l00298"></a>        const struct device *port;
<a id="l00300"></a>        gpio_pin_t pin;
<a id="l00302"></a>        gpio_dt_flags_t dt_flags;
<a id="l00303"></a>};
<a id="l00304"></a>
<a id="l00339"></a>#define GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)                            \
<a id="l00340"></a>        {                                                                      \
<a id="l00341"></a>                .port = DEVICE_DT_GET(DT_GPIO_CTLR_BY_IDX(node_id, prop, idx)),\
<a id="l00342"></a>                .pin = DT_GPIO_PIN_BY_IDX(node_id, prop, idx),                 \
<a id="l00343"></a>                .dt_flags = DT_GPIO_FLAGS_BY_IDX(node_id, prop, idx),          \
<a id="l00344"></a>        }
<a id="l00345"></a>
<a id="l00363"></a>#define GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, idx, default_value)   \
<a id="l00364"></a>        COND_CODE_1(DT_PROP_HAS_IDX(node_id, prop, idx),                \
<a id="l00365"></a>                    (GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)),      \
<a id="l00366"></a>                    (default_value))
<a id="l00367"></a>
<a id="l00376"></a>#define GPIO_DT_SPEC_GET(node_id, prop) \
<a id="l00377"></a>        GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, 0)
<a id="l00378"></a>
<a id="l00389"></a>#define GPIO_DT_SPEC_GET_OR(node_id, prop, default_value) \
<a id="l00390"></a>        GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, 0, default_value)
<a id="l00391"></a>
<a id="l00402"></a>#define GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, idx) \
<a id="l00403"></a>        GPIO_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), prop, idx)
<a id="l00404"></a>
<a id="l00416"></a>#define GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, idx, default_value)         \
<a id="l00417"></a>        COND_CODE_1(DT_PROP_HAS_IDX(DT_DRV_INST(inst), prop, idx),              \
<a id="l00418"></a>                    (GPIO_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), prop, idx)),    \
<a id="l00419"></a>                    (default_value))
<a id="l00420"></a>
<a id="l00429"></a>#define GPIO_DT_SPEC_INST_GET(inst, prop) \
<a id="l00430"></a>        GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, 0)
<a id="l00431"></a>
<a id="l00442"></a>#define GPIO_DT_SPEC_INST_GET_OR(inst, prop, default_value) \
<a id="l00443"></a>        GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, 0, default_value)
<a id="l00444"></a>
<a id="l00445"></a>/*
<a id="l00446"></a> * @cond INTERNAL_HIDDEN
<a id="l00447"></a> */
<a id="l00448"></a>
<a id="l00459"></a>#define Z_GPIO_GEN_BITMASK_COND(node_id, prop, off_idx, sz_idx)              \
<a id="l00460"></a>        COND_CODE_1(DT_PROP_HAS_IDX(node_id, prop, off_idx),                 \
<a id="l00461"></a>                (COND_CODE_0(DT_PROP_BY_IDX(node_id, prop, sz_idx),          \
<a id="l00462"></a>                        (0),                                                 \
<a id="l00463"></a>                        (GENMASK64(DT_PROP_BY_IDX(node_id, prop, off_idx) +  \
<a id="l00464"></a>                                DT_PROP_BY_IDX(node_id, prop, sz_idx) - 1,   \
<a id="l00465"></a>                                DT_PROP_BY_IDX(node_id, prop, off_idx))))    \
<a id="l00466"></a>                ), (0))
<a id="l00467"></a>
<a id="l00475"></a>#define Z_GPIO_GEN_RESERVED_RANGES_COND(odd_it, node_id)                      \
<a id="l00476"></a>        COND_CODE_1(DT_PROP_HAS_IDX(node_id, gpio_reserved_ranges, odd_it),   \
<a id="l00477"></a>                (Z_GPIO_GEN_BITMASK_COND(node_id,                             \
<a id="l00478"></a>                        gpio_reserved_ranges,                                 \
<a id="l00479"></a>                        GET_ARG_N(odd_it, Z_SPARSE_LIST_EVEN_NUMBERS),        \
<a id="l00480"></a>                        odd_it)),                                             \
<a id="l00481"></a>                (0))
<a id="l00482"></a>
<a id="l00486"></a>
<a id="l00574"></a>#define GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, ngpios)                        \
<a id="l00575"></a>        ((gpio_port_pins_t)                                                    \
<a id="l00576"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, gpio_reserved_ranges),           \
<a id="l00577"></a>                (GENMASK64(BITS_PER_LONG_LONG - 1, ngpios)                     \
<a id="l00578"></a>                | FOR_EACH_FIXED_ARG(Z_GPIO_GEN_RESERVED_RANGES_COND,          \
<a id="l00579"></a>                        (|),                                                   \
<a id="l00580"></a>                        node_id,                                               \
<a id="l00581"></a>                        LIST_DROP_EMPTY(Z_SPARSE_LIST_ODD_NUMBERS))),          \
<a id="l00582"></a>                (0)))
<a id="l00583"></a>
<a id="l00591"></a>#define GPIO_DT_RESERVED_RANGES(node_id)                                       \
<a id="l00592"></a>        GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, DT_PROP(node_id, ngpios))
<a id="l00593"></a>
<a id="l00603"></a>#define GPIO_DT_INST_RESERVED_RANGES_NGPIOS(inst, ngpios)                      \
<a id="l00604"></a>                GPIO_DT_RESERVED_RANGES_NGPIOS(DT_DRV_INST(inst), ngpios)
<a id="l00605"></a>
<a id="l00614"></a>#define GPIO_DT_INST_RESERVED_RANGES(inst)                                     \
<a id="l00615"></a>                GPIO_DT_RESERVED_RANGES(DT_DRV_INST(inst))
<a id="l00616"></a>
<a id="l00665"></a>#define GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(node_id, ngpios)                      \
<a id="l00666"></a>        ((gpio_port_pins_t)                                                    \
<a id="l00667"></a>        COND_CODE_0(ngpios,                                                    \
<a id="l00668"></a>                (0),                                                           \
<a id="l00669"></a>                (COND_CODE_1(DT_NODE_HAS_PROP(node_id, gpio_reserved_ranges),  \
<a id="l00670"></a>                        ((GENMASK64(ngpios - 1, 0) &amp;                           \
<a id="l00671"></a>                        ~GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, ngpios))),    \
<a id="l00672"></a>                        (GENMASK64(ngpios - 1, 0)))                            \
<a id="l00673"></a>                )                                                              \
<a id="l00674"></a>        ))
<a id="l00675"></a>
<a id="l00685"></a>#define GPIO_DT_INST_PORT_PIN_MASK_NGPIOS_EXC(inst, ngpios)     \
<a id="l00686"></a>                GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(DT_DRV_INST(inst), ngpios)
<a id="l00687"></a>
<a id="l00691"></a>#define GPIO_MAX_PINS_PER_PORT (sizeof(gpio_port_pins_t) * __CHAR_BIT__)
<a id="l00692"></a>
<a id="l00708"></a>static inline bool gpio_port_pin_is_supported(gpio_port_pins_t port_pin_mask, gpio_pin_t pin)
<a id="l00709"></a>{
<a id="l00710"></a>        if (pin &gt;= GPIO_MAX_PINS_PER_PORT) {
<a id="l00711"></a>                return false;
<a id="l00712"></a>        }
<a id="l00713"></a>
<a id="l00714"></a>        return (port_pin_mask &amp; (gpio_port_pins_t)BIT(pin)) != 0U;
<a id="l00715"></a>}
<a id="l00716"></a>
<a id="l00722"></a>struct gpio_driver_config {
<a id="l00728"></a>        gpio_port_pins_t port_pin_mask;
<a id="l00729"></a>};
<a id="l00730"></a>
<a id="l00735"></a>struct gpio_driver_data {
<a id="l00741"></a>        gpio_port_pins_t invert;
<a id="l00742"></a>};
<a id="l00743"></a>
<a id="l00744"></a>struct gpio_callback;
<a id="l00745"></a>
<a id="l00757"></a>typedef void (*gpio_callback_handler_t)(const struct device *port,
<a id="l00758"></a>                                        struct gpio_callback *cb,
<a id="l00759"></a>                                        gpio_port_pins_t pins);
<a id="l00760"></a>
<a id="l00771"></a>struct gpio_callback {
<a id="l00775"></a>        sys_snode_t node;
<a id="l00776"></a>
<a id="l00778"></a>        gpio_callback_handler_t handler;
<a id="l00779"></a>
<a id="l00786"></a>        gpio_port_pins_t pin_mask;
<a id="l00787"></a>};
<a id="l00788"></a>
<a id="l00793"></a>
<a id="l00801"></a>enum gpio_int_mode {
<a id="l00803"></a>        GPIO_INT_MODE_DISABLED = GPIO_INT_DISABLE,
<a id="l00805"></a>        GPIO_INT_MODE_LEVEL = GPIO_INT_ENABLE,
<a id="l00807"></a>        GPIO_INT_MODE_EDGE = GPIO_INT_ENABLE | GPIO_INT_EDGE,
<a id="l00808"></a>#if defined(CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT) || defined(__DOXYGEN__)
<a id="l00813"></a>        GPIO_INT_MODE_DISABLE_ONLY = GPIO_INT_DISABLE | GPIO_INT_ENABLE_DISABLE_ONLY,
<a id="l00818"></a>        GPIO_INT_MODE_ENABLE_ONLY = GPIO_INT_ENABLE | GPIO_INT_ENABLE_DISABLE_ONLY,
<a id="l00819"></a>#endif /* CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT */
<a id="l00820"></a>};
<a id="l00821"></a>
<a id="l00825"></a>enum gpio_int_trig {
<a id="l00829"></a>        GPIO_INT_TRIG_LOW = GPIO_INT_LOW_0,
<a id="l00832"></a>        GPIO_INT_TRIG_HIGH = GPIO_INT_HIGH_1,
<a id="l00834"></a>        GPIO_INT_TRIG_BOTH = GPIO_INT_LOW_0 | GPIO_INT_HIGH_1,
<a id="l00836"></a>        GPIO_INT_TRIG_WAKE = GPIO_INT_WAKEUP,
<a id="l00840"></a>        GPIO_INT_TRIG_WAKE_LOW = GPIO_INT_LOW_0 | GPIO_INT_WAKEUP,
<a id="l00844"></a>        GPIO_INT_TRIG_WAKE_HIGH = GPIO_INT_HIGH_1 | GPIO_INT_WAKEUP,
<a id="l00846"></a>        GPIO_INT_TRIG_WAKE_BOTH = GPIO_INT_LOW_0 | GPIO_INT_HIGH_1 | GPIO_INT_WAKEUP,
<a id="l00847"></a>};
<a id="l00848"></a>
<a id="l00853"></a>typedef int (*gpio_api_pin_configure_t)(const struct device *port, gpio_pin_t pin,
<a id="l00854"></a>                                        gpio_flags_t flags);
<a id="l00855"></a>
<a id="l00860"></a>typedef int (*gpio_api_pin_get_config_t)(const struct device *port, gpio_pin_t pin,
<a id="l00861"></a>                                         gpio_flags_t *flags);
<a id="l00862"></a>
<a id="l00867"></a>typedef int (*gpio_api_port_get_raw_t)(const struct device *port,
<a id="l00868"></a>                                       gpio_port_value_t *value);
<a id="l00869"></a>
<a id="l00874"></a>typedef int (*gpio_api_port_set_masked_raw_t)(const struct device *port,
<a id="l00875"></a>                                              gpio_port_pins_t mask,
<a id="l00876"></a>                                              gpio_port_value_t value);
<a id="l00877"></a>
<a id="l00882"></a>typedef int (*gpio_api_port_set_bits_raw_t)(const struct device *port,
<a id="l00883"></a>                                            gpio_port_pins_t pins);
<a id="l00884"></a>
<a id="l00889"></a>typedef int (*gpio_api_port_clear_bits_raw_t)(const struct device *port,
<a id="l00890"></a>                                              gpio_port_pins_t pins);
<a id="l00891"></a>
<a id="l00896"></a>typedef int (*gpio_api_port_toggle_bits_t)(const struct device *port,
<a id="l00897"></a>                                           gpio_port_pins_t pins);
<a id="l00898"></a>
<a id="l00905"></a>typedef int (*gpio_api_pin_interrupt_configure_t)(const struct device *port,
<a id="l00906"></a>                                                  gpio_pin_t pin,
<a id="l00907"></a>                                                  enum gpio_int_mode mode,
<a id="l00908"></a>                                                  enum gpio_int_trig trig);
<a id="l00909"></a>
<a id="l00914"></a>typedef int (*gpio_api_manage_callback_t)(const struct device *port,
<a id="l00915"></a>                                          struct gpio_callback *cb,
<a id="l00916"></a>                                          bool set);
<a id="l00917"></a>
<a id="l00922"></a>typedef uint32_t (*gpio_api_get_pending_int_t)(const struct device *dev);
<a id="l00923"></a>
<a id="l00928"></a>typedef int (*gpio_api_port_get_direction_t)(const struct device *port, gpio_port_pins_t map,
<a id="l00929"></a>                                             gpio_port_pins_t *inputs, gpio_port_pins_t *outputs);
<a id="l00930"></a>
<a id="l00934"></a>__subsystem struct gpio_driver_api {
<a id="l00936"></a>        gpio_api_pin_configure_t pin_configure;
<a id="l00937"></a>#if defined(CONFIG_GPIO_GET_CONFIG) || defined(__DOXYGEN__)
<a id="l00942"></a>        gpio_api_pin_get_config_t pin_get_config;
<a id="l00943"></a>#endif /* CONFIG_GPIO_GET_CONFIG */
<a id="l00945"></a>        gpio_api_port_get_raw_t port_get_raw;
<a id="l00947"></a>        gpio_api_port_set_masked_raw_t port_set_masked_raw;
<a id="l00949"></a>        gpio_api_port_set_bits_raw_t port_set_bits_raw;
<a id="l00951"></a>        gpio_api_port_clear_bits_raw_t port_clear_bits_raw;
<a id="l00953"></a>        gpio_api_port_toggle_bits_t port_toggle_bits;
<a id="l00955"></a>        gpio_api_pin_interrupt_configure_t pin_interrupt_configure;
<a id="l00960"></a>        gpio_api_manage_callback_t manage_callback;
<a id="l00962"></a>        gpio_api_get_pending_int_t get_pending_int;
<a id="l00963"></a>#if defined(CONFIG_GPIO_GET_DIRECTION) || defined(__DOXYGEN__)
<a id="l00968"></a>        gpio_api_port_get_direction_t port_get_direction;
<a id="l00969"></a>#endif /* CONFIG_GPIO_GET_DIRECTION */
<a id="l00970"></a>};
<a id="l00971"></a>
<a id="l00973"></a>
<a id="l00982"></a>static inline bool gpio_is_ready_dt(const struct gpio_dt_spec *spec)
<a id="l00983"></a>{
<a id="l00984"></a>        /* Validate port is ready */
<a id="l00985"></a>        return device_is_ready(spec-&gt;port);
<a id="l00986"></a>}
<a id="l00987"></a>
<a id="l01011"></a>__syscall int gpio_pin_interrupt_configure(const struct device *port,
<a id="l01012"></a>                                           gpio_pin_t pin,
<a id="l01013"></a>                                           gpio_flags_t flags);
<a id="l01014"></a>
<a id="l01015"></a>static inline int z_impl_gpio_pin_interrupt_configure(const struct device *port,
<a id="l01016"></a>                                                      gpio_pin_t pin,
<a id="l01017"></a>                                                      gpio_flags_t flags)
<a id="l01018"></a>{
<a id="l01019"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01020"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01021"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01022"></a>        const struct gpio_driver_data *const data =
<a id="l01023"></a>                (const struct gpio_driver_data *)port-&gt;data;
<a id="l01024"></a>        enum gpio_int_trig trig;
<a id="l01025"></a>        enum gpio_int_mode mode;
<a id="l01026"></a>        int ret;
<a id="l01027"></a>
<a id="l01028"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_pin, interrupt_configure, port, pin, flags);
<a id="l01029"></a>
<a id="l01030"></a>        if (api-&gt;pin_interrupt_configure == NULL) {
<a id="l01031"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, interrupt_configure, port, pin, -ENOSYS);
<a id="l01032"></a>                return -ENOSYS;
<a id="l01033"></a>        }
<a id="l01034"></a>
<a id="l01035"></a>        __ASSERT((flags &amp; (GPIO_INT_DISABLE | GPIO_INT_ENABLE))
<a id="l01036"></a>                 != (GPIO_INT_DISABLE | GPIO_INT_ENABLE),
<a id="l01037"></a>                 "Cannot both enable and disable interrupts");
<a id="l01038"></a>
<a id="l01039"></a>        __ASSERT((flags &amp; (GPIO_INT_DISABLE | GPIO_INT_ENABLE)) != 0U,
<a id="l01040"></a>                 "Must either enable or disable interrupts");
<a id="l01041"></a>
<a id="l01042"></a>        __ASSERT(((flags &amp; GPIO_INT_ENABLE) == 0) ||
<a id="l01043"></a>                 ((flags &amp; GPIO_INT_EDGE) != 0) ||
<a id="l01044"></a>                 ((flags &amp; (GPIO_INT_LOW_0 | GPIO_INT_HIGH_1)) !=
<a id="l01045"></a>                  (GPIO_INT_LOW_0 | GPIO_INT_HIGH_1)),
<a id="l01046"></a>                 "Only one of GPIO_INT_LOW_0, GPIO_INT_HIGH_1 can be "
<a id="l01047"></a>                 "enabled for a level interrupt.");
<a id="l01048"></a>
<a id="l01050"></a>#ifdef CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT
<a id="l01051"></a>#define GPIO_INT_ENABLE_DISABLE_ONLY_VALUE  GPIO_INT_ENABLE_DISABLE_ONLY
<a id="l01052"></a>#else
<a id="l01053"></a>#define GPIO_INT_ENABLE_DISABLE_ONLY_VALUE  0
<a id="l01054"></a>#endif /* CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT */
<a id="l01056"></a>
<a id="l01057"></a>        __ASSERT(((flags &amp; GPIO_INT_ENABLE) == 0) ||
<a id="l01058"></a>                         ((flags &amp; (GPIO_INT_LOW_0 | GPIO_INT_HIGH_1)) != 0) ||
<a id="l01059"></a>                         (flags &amp; GPIO_INT_ENABLE_DISABLE_ONLY_VALUE) != 0,
<a id="l01060"></a>                 "At least one of GPIO_INT_LOW_0, GPIO_INT_HIGH_1 has to be enabled.");
<a id="l01061"></a>#undef GPIO_INT_ENABLE_DISABLE_ONLY_VALUE
<a id="l01062"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01063"></a>
<a id="l01064"></a>        /* See the note in z_impl_gpio_pin_configure(). */
<a id="l01065"></a>        if (pin &gt;= GPIO_MAX_PINS_PER_PORT) {
<a id="l01066"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, interrupt_configure, port, pin, -EINVAL);
<a id="l01067"></a>                return -EINVAL;
<a id="l01068"></a>        }
<a id="l01069"></a>
<a id="l01070"></a>        if (((flags &amp; GPIO_INT_LEVELS_LOGICAL) != 0) &amp;&amp;
<a id="l01071"></a>            ((data-&gt;invert &amp; (gpio_port_pins_t)BIT(pin)) != 0)) {
<a id="l01072"></a>                /* Invert signal bits */
<a id="l01073"></a>                flags ^= (GPIO_INT_LOW_0 | GPIO_INT_HIGH_1);
<a id="l01074"></a>        }
<a id="l01075"></a>
<a id="l01076"></a>        trig = (enum gpio_int_trig)(flags &amp; (GPIO_INT_LOW_0 | GPIO_INT_HIGH_1 | GPIO_INT_WAKEUP));
<a id="l01077"></a>#ifdef CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT
<a id="l01078"></a>        mode = (enum gpio_int_mode)(flags &amp; (GPIO_INT_EDGE | GPIO_INT_DISABLE | GPIO_INT_ENABLE |
<a id="l01079"></a>                                             GPIO_INT_ENABLE_DISABLE_ONLY));
<a id="l01080"></a>#else
<a id="l01081"></a>        mode = (enum gpio_int_mode)(flags &amp; (GPIO_INT_EDGE | GPIO_INT_DISABLE | GPIO_INT_ENABLE));
<a id="l01082"></a>#endif /* CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT */
<a id="l01083"></a>
<a id="l01084"></a>        ret = api-&gt;pin_interrupt_configure(port, pin, mode, trig);
<a id="l01085"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, interrupt_configure, port, pin, ret);
<a id="l01086"></a>        return ret;
<a id="l01087"></a>}
<a id="l01088"></a>
<a id="l01106"></a>static inline int gpio_pin_interrupt_configure_dt(const struct gpio_dt_spec *spec,
<a id="l01107"></a>                                                  gpio_flags_t flags)
<a id="l01108"></a>{
<a id="l01109"></a>        return gpio_pin_interrupt_configure(spec-&gt;port, spec-&gt;pin,
<a id="l01110"></a>                                            flags | (spec-&gt;dt_flags &amp; GPIO_INT_WAKEUP));
<a id="l01111"></a>}
<a id="l01112"></a>
<a id="l01128"></a>__syscall int gpio_pin_configure(const struct device *port,
<a id="l01129"></a>                                 gpio_pin_t pin,
<a id="l01130"></a>                                 gpio_flags_t flags);
<a id="l01131"></a>
<a id="l01132"></a>static inline int z_impl_gpio_pin_configure(const struct device *port,
<a id="l01133"></a>                                            gpio_pin_t pin,
<a id="l01134"></a>                                            gpio_flags_t flags)
<a id="l01135"></a>{
<a id="l01136"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01137"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01138"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01139"></a>        struct gpio_driver_data *data =
<a id="l01140"></a>                (struct gpio_driver_data *)port-&gt;data;
<a id="l01141"></a>        int ret;
<a id="l01142"></a>
<a id="l01143"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_pin, configure, port, pin, flags);
<a id="l01144"></a>
<a id="l01145"></a>        __ASSERT((flags &amp; GPIO_INT_MASK) == 0,
<a id="l01146"></a>                 "Interrupt flags are not supported");
<a id="l01147"></a>
<a id="l01148"></a>        __ASSERT((flags &amp; (GPIO_PULL_UP | GPIO_PULL_DOWN)) !=
<a id="l01149"></a>                 (GPIO_PULL_UP | GPIO_PULL_DOWN),
<a id="l01150"></a>                 "Pull Up and Pull Down should not be enabled simultaneously");
<a id="l01151"></a>
<a id="l01152"></a>        __ASSERT(!((flags &amp; GPIO_INPUT) &amp;&amp; !(flags &amp; GPIO_OUTPUT) &amp;&amp; (flags &amp; GPIO_SINGLE_ENDED)),
<a id="l01153"></a>                 "Input cannot be enabled for 'Open Drain', 'Open Source' modes without Output");
<a id="l01154"></a>
<a id="l01155"></a>        __ASSERT_NO_MSG((flags &amp; GPIO_SINGLE_ENDED) != 0 ||
<a id="l01156"></a>                        (flags &amp; GPIO_LINE_OPEN_DRAIN) == 0);
<a id="l01157"></a>
<a id="l01158"></a>        __ASSERT((flags &amp; (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH)) == 0
<a id="l01159"></a>                 || (flags &amp; GPIO_OUTPUT) != 0,
<a id="l01160"></a>                 "Output needs to be enabled to be initialized low or high");
<a id="l01161"></a>
<a id="l01162"></a>        __ASSERT((flags &amp; (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH))
<a id="l01163"></a>                 != (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH),
<a id="l01164"></a>                 "Output cannot be initialized low and high");
<a id="l01165"></a>
<a id="l01166"></a>        if (((flags &amp; GPIO_OUTPUT_INIT_LOGICAL) != 0)
<a id="l01167"></a>            &amp;&amp; ((flags &amp; (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH)) != 0)
<a id="l01168"></a>            &amp;&amp; ((flags &amp; GPIO_ACTIVE_LOW) != 0)) {
<a id="l01169"></a>                flags ^= GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH;
<a id="l01170"></a>        }
<a id="l01171"></a>
<a id="l01172"></a>        flags &amp;= ~GPIO_OUTPUT_INIT_LOGICAL;
<a id="l01173"></a>
<a id="l01174"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01175"></a>
<a id="l01176"></a>        /*
<a id="l01177"></a>         * pin is passed on to the driver as-is, where it is commonly used as an
<a id="l01178"></a>         * array index, so it must be range checked even when assertions are
<a id="l01179"></a>         * compiled out.
<a id="l01180"></a>         */
<a id="l01181"></a>        if (pin &gt;= GPIO_MAX_PINS_PER_PORT) {
<a id="l01182"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, configure, port, pin, -EINVAL);
<a id="l01183"></a>                return -EINVAL;
<a id="l01184"></a>        }
<a id="l01185"></a>
<a id="l01186"></a>        if ((flags &amp; GPIO_ACTIVE_LOW) != 0) {
<a id="l01187"></a>                data-&gt;invert |= (gpio_port_pins_t)BIT(pin);
<a id="l01188"></a>        } else {
<a id="l01189"></a>                data-&gt;invert &amp;= ~(gpio_port_pins_t)BIT(pin);
<a id="l01190"></a>        }
<a id="l01191"></a>
<a id="l01192"></a>        ret = api-&gt;pin_configure(port, pin, flags);
<a id="l01193"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, configure, port, pin, ret);
<a id="l01194"></a>        return ret;
<a id="l01195"></a>}
<a id="l01196"></a>
<a id="l01208"></a>static inline int gpio_pin_configure_dt(const struct gpio_dt_spec *spec,
<a id="l01209"></a>                                        gpio_flags_t extra_flags)
<a id="l01210"></a>{
<a id="l01211"></a>        return gpio_pin_configure(spec-&gt;port,
<a id="l01212"></a>                                  spec-&gt;pin,
<a id="l01213"></a>                                  spec-&gt;dt_flags | extra_flags);
<a id="l01214"></a>}
<a id="l01215"></a>
<a id="l01234"></a>__syscall int gpio_port_get_direction(const struct device *port, gpio_port_pins_t map,
<a id="l01235"></a>                                      gpio_port_pins_t *inputs, gpio_port_pins_t *outputs);
<a id="l01236"></a>
<a id="l01237"></a>#ifdef CONFIG_GPIO_GET_DIRECTION
<a id="l01238"></a>static inline int z_impl_gpio_port_get_direction(const struct device *port, gpio_port_pins_t map,
<a id="l01239"></a>                                                 gpio_port_pins_t *inputs,
<a id="l01240"></a>                                                 gpio_port_pins_t *outputs)
<a id="l01241"></a>{
<a id="l01242"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01243"></a>        int ret;
<a id="l01244"></a>
<a id="l01245"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, get_direction, port, map, inputs, outputs);
<a id="l01246"></a>
<a id="l01247"></a>        if (api-&gt;port_get_direction == NULL) {
<a id="l01248"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_port, get_direction, port, -ENOSYS);
<a id="l01249"></a>                return -ENOSYS;
<a id="l01250"></a>        }
<a id="l01251"></a>
<a id="l01252"></a>        ret = api-&gt;port_get_direction(port, map, inputs, outputs);
<a id="l01253"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, get_direction, port, ret);
<a id="l01254"></a>        return ret;
<a id="l01255"></a>}
<a id="l01256"></a>#endif /* CONFIG_GPIO_GET_DIRECTION */
<a id="l01257"></a>
<a id="l01270"></a>static inline int gpio_pin_is_input(const struct device *port, gpio_pin_t pin)
<a id="l01271"></a>{
<a id="l01272"></a>        int rv;
<a id="l01273"></a>        gpio_port_pins_t pins;
<a id="l01274"></a>        __unused const struct gpio_driver_config *cfg =
<a id="l01275"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01276"></a>
<a id="l01277"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01278"></a>
<a id="l01279"></a>        rv = gpio_port_get_direction(port, BIT(pin), &amp;pins, NULL);
<a id="l01280"></a>        if (rv &lt; 0) {
<a id="l01281"></a>                return rv;
<a id="l01282"></a>        }
<a id="l01283"></a>
<a id="l01284"></a>        return (int)!!((gpio_port_pins_t)BIT(pin) &amp; pins);
<a id="l01285"></a>}
<a id="l01286"></a>
<a id="l01298"></a>static inline int gpio_pin_is_input_dt(const struct gpio_dt_spec *spec)
<a id="l01299"></a>{
<a id="l01300"></a>        return gpio_pin_is_input(spec-&gt;port, spec-&gt;pin);
<a id="l01301"></a>}
<a id="l01302"></a>
<a id="l01315"></a>static inline int gpio_pin_is_output(const struct device *port, gpio_pin_t pin)
<a id="l01316"></a>{
<a id="l01317"></a>        int rv;
<a id="l01318"></a>        gpio_port_pins_t pins;
<a id="l01319"></a>        __unused const struct gpio_driver_config *cfg =
<a id="l01320"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01321"></a>
<a id="l01322"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01323"></a>
<a id="l01324"></a>        rv = gpio_port_get_direction(port, BIT(pin), NULL, &amp;pins);
<a id="l01325"></a>        if (rv &lt; 0) {
<a id="l01326"></a>                return rv;
<a id="l01327"></a>        }
<a id="l01328"></a>
<a id="l01329"></a>        return (int)!!((gpio_port_pins_t)BIT(pin) &amp; pins);
<a id="l01330"></a>}
<a id="l01331"></a>
<a id="l01343"></a>static inline int gpio_pin_is_output_dt(const struct gpio_dt_spec *spec)
<a id="l01344"></a>{
<a id="l01345"></a>        return gpio_pin_is_output(spec-&gt;port, spec-&gt;pin);
<a id="l01346"></a>}
<a id="l01347"></a>
<a id="l01363"></a>__syscall int gpio_pin_get_config(const struct device *port, gpio_pin_t pin,
<a id="l01364"></a>                                  gpio_flags_t *flags);
<a id="l01365"></a>
<a id="l01366"></a>#ifdef CONFIG_GPIO_GET_CONFIG
<a id="l01367"></a>static inline int z_impl_gpio_pin_get_config(const struct device *port,
<a id="l01368"></a>                                             gpio_pin_t pin,
<a id="l01369"></a>                                             gpio_flags_t *flags)
<a id="l01370"></a>{
<a id="l01371"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01372"></a>        int ret;
<a id="l01373"></a>
<a id="l01374"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_pin, get_config, port, pin, *flags);
<a id="l01375"></a>
<a id="l01376"></a>        if (api-&gt;pin_get_config == NULL) {
<a id="l01377"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, get_config, port, pin, -ENOSYS);
<a id="l01378"></a>                return -ENOSYS;
<a id="l01379"></a>        }
<a id="l01380"></a>
<a id="l01381"></a>        /* See the note in z_impl_gpio_pin_configure(). */
<a id="l01382"></a>        if (pin &gt;= GPIO_MAX_PINS_PER_PORT) {
<a id="l01383"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, get_config, port, pin, -EINVAL);
<a id="l01384"></a>                return -EINVAL;
<a id="l01385"></a>        }
<a id="l01386"></a>
<a id="l01387"></a>        ret = api-&gt;pin_get_config(port, pin, flags);
<a id="l01388"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_pin, get_config, port, pin, ret);
<a id="l01389"></a>        return ret;
<a id="l01390"></a>}
<a id="l01391"></a>#endif
<a id="l01392"></a>
<a id="l01405"></a>static inline int gpio_pin_get_config_dt(const struct gpio_dt_spec *spec,
<a id="l01406"></a>                                        gpio_flags_t *flags)
<a id="l01407"></a>{
<a id="l01408"></a>        return gpio_pin_get_config(spec-&gt;port, spec-&gt;pin, flags);
<a id="l01409"></a>}
<a id="l01410"></a>
<a id="l01428"></a>__syscall int gpio_port_get_raw(const struct device *port,
<a id="l01429"></a>                                gpio_port_value_t *value);
<a id="l01430"></a>
<a id="l01431"></a>static inline int z_impl_gpio_port_get_raw(const struct device *port, gpio_port_value_t *value)
<a id="l01432"></a>{
<a id="l01433"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01434"></a>        int ret;
<a id="l01435"></a>
<a id="l01436"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, get_raw, port, value);
<a id="l01437"></a>
<a id="l01438"></a>        ret = api-&gt;port_get_raw(port, value);
<a id="l01439"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, get_raw, port, ret);
<a id="l01440"></a>        return ret;
<a id="l01441"></a>}
<a id="l01442"></a>
<a id="l01461"></a>__syscall int gpio_port_get(const struct device *port,
<a id="l01462"></a>                            gpio_port_value_t *value);
<a id="l01463"></a>
<a id="l01464"></a>static inline int z_impl_gpio_port_get(const struct device *port,
<a id="l01465"></a>                                       gpio_port_value_t *value)
<a id="l01466"></a>{
<a id="l01467"></a>        const struct gpio_driver_data *const data =
<a id="l01468"></a>                        (const struct gpio_driver_data *)port-&gt;data;
<a id="l01469"></a>        int ret;
<a id="l01470"></a>
<a id="l01471"></a>        ret = z_impl_gpio_port_get_raw(port, value);
<a id="l01472"></a>        if (ret == 0) {
<a id="l01473"></a>                *value ^= data-&gt;invert;
<a id="l01474"></a>        }
<a id="l01475"></a>
<a id="l01476"></a>        return ret;
<a id="l01477"></a>}
<a id="l01478"></a>
<a id="l01496"></a>__syscall int gpio_port_set_masked_raw(const struct device *port,
<a id="l01497"></a>                                       gpio_port_pins_t mask,
<a id="l01498"></a>                                       gpio_port_value_t value);
<a id="l01499"></a>
<a id="l01500"></a>static inline int z_impl_gpio_port_set_masked_raw(const struct device *port,
<a id="l01501"></a>                                                  gpio_port_pins_t mask,
<a id="l01502"></a>                                                  gpio_port_value_t value)
<a id="l01503"></a>{
<a id="l01504"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01505"></a>        int ret;
<a id="l01506"></a>
<a id="l01507"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, set_masked_raw, port, mask, value);
<a id="l01508"></a>
<a id="l01509"></a>        ret = api-&gt;port_set_masked_raw(port, mask, value);
<a id="l01510"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, set_masked_raw, port, ret);
<a id="l01511"></a>        return ret;
<a id="l01512"></a>}
<a id="l01513"></a>
<a id="l01534"></a>__syscall int gpio_port_set_masked(const struct device *port,
<a id="l01535"></a>                                   gpio_port_pins_t mask,
<a id="l01536"></a>                                   gpio_port_value_t value);
<a id="l01537"></a>
<a id="l01538"></a>static inline int z_impl_gpio_port_set_masked(const struct device *port,
<a id="l01539"></a>                                              gpio_port_pins_t mask,
<a id="l01540"></a>                                              gpio_port_value_t value)
<a id="l01541"></a>{
<a id="l01542"></a>        const struct gpio_driver_data *const data =
<a id="l01543"></a>                        (const struct gpio_driver_data *)port-&gt;data;
<a id="l01544"></a>
<a id="l01545"></a>        value ^= data-&gt;invert;
<a id="l01546"></a>
<a id="l01547"></a>        return z_impl_gpio_port_set_masked_raw(port, mask, value);
<a id="l01548"></a>}
<a id="l01549"></a>
<a id="l01560"></a>__syscall int gpio_port_set_bits_raw(const struct device *port,
<a id="l01561"></a>                                     gpio_port_pins_t pins);
<a id="l01562"></a>
<a id="l01563"></a>static inline int z_impl_gpio_port_set_bits_raw(const struct device *port,
<a id="l01564"></a>                                                gpio_port_pins_t pins)
<a id="l01565"></a>{
<a id="l01566"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01567"></a>        int ret;
<a id="l01568"></a>
<a id="l01569"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, set_bits_raw, port, pins);
<a id="l01570"></a>
<a id="l01571"></a>        ret = api-&gt;port_set_bits_raw(port, pins);
<a id="l01572"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, set_bits_raw, port, ret);
<a id="l01573"></a>        return ret;
<a id="l01574"></a>}
<a id="l01575"></a>
<a id="l01586"></a>__syscall int gpio_port_set_bits(const struct device *port,
<a id="l01587"></a>                                 gpio_port_pins_t pins);
<a id="l01588"></a>
<a id="l01589"></a>static inline int z_impl_gpio_port_set_bits(const struct device *port,
<a id="l01590"></a>                                            gpio_port_pins_t pins)
<a id="l01591"></a>{
<a id="l01592"></a>        return z_impl_gpio_port_set_masked(port, pins, pins);
<a id="l01593"></a>}
<a id="l01594"></a>
<a id="l01605"></a>__syscall int gpio_port_clear_bits_raw(const struct device *port,
<a id="l01606"></a>                                       gpio_port_pins_t pins);
<a id="l01607"></a>
<a id="l01608"></a>static inline int z_impl_gpio_port_clear_bits_raw(const struct device *port,
<a id="l01609"></a>                                                  gpio_port_pins_t pins)
<a id="l01610"></a>{
<a id="l01611"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01612"></a>        int ret;
<a id="l01613"></a>
<a id="l01614"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, clear_bits_raw, port, pins);
<a id="l01615"></a>
<a id="l01616"></a>        ret = api-&gt;port_clear_bits_raw(port, pins);
<a id="l01617"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, clear_bits_raw, port, ret);
<a id="l01618"></a>        return ret;
<a id="l01619"></a>}
<a id="l01620"></a>
<a id="l01631"></a>__syscall int gpio_port_clear_bits(const struct device *port,
<a id="l01632"></a>                                   gpio_port_pins_t pins);
<a id="l01633"></a>
<a id="l01634"></a>static inline int z_impl_gpio_port_clear_bits(const struct device *port,
<a id="l01635"></a>                                              gpio_port_pins_t pins)
<a id="l01636"></a>{
<a id="l01637"></a>        return z_impl_gpio_port_set_masked(port, pins, 0);
<a id="l01638"></a>}
<a id="l01639"></a>
<a id="l01650"></a>__syscall int gpio_port_toggle_bits(const struct device *port,
<a id="l01651"></a>                                    gpio_port_pins_t pins);
<a id="l01652"></a>
<a id="l01653"></a>static inline int z_impl_gpio_port_toggle_bits(const struct device *port,
<a id="l01654"></a>                                               gpio_port_pins_t pins)
<a id="l01655"></a>{
<a id="l01656"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01657"></a>        int ret;
<a id="l01658"></a>
<a id="l01659"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio_port, toggle_bits, port, pins);
<a id="l01660"></a>
<a id="l01661"></a>        ret = api-&gt;port_toggle_bits(port, pins);
<a id="l01662"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio_port, toggle_bits, port, ret);
<a id="l01663"></a>        return ret;
<a id="l01664"></a>}
<a id="l01665"></a>
<a id="l01677"></a>__syscall int gpio_port_set_clr_bits_raw(const struct device *port,
<a id="l01678"></a>                                         gpio_port_pins_t set_pins,
<a id="l01679"></a>                                         gpio_port_pins_t clear_pins);
<a id="l01680"></a>
<a id="l01681"></a>static inline int z_impl_gpio_port_set_clr_bits_raw(const struct device *port,
<a id="l01682"></a>                                                    gpio_port_pins_t set_pins,
<a id="l01683"></a>                                                    gpio_port_pins_t clear_pins)
<a id="l01684"></a>{
<a id="l01685"></a>        __ASSERT((set_pins &amp; clear_pins) == 0, "Set and Clear pins overlap");
<a id="l01686"></a>
<a id="l01687"></a>        return z_impl_gpio_port_set_masked_raw(port, set_pins | clear_pins, set_pins);
<a id="l01688"></a>}
<a id="l01689"></a>
<a id="l01701"></a>__syscall int gpio_port_set_clr_bits(const struct device *port,
<a id="l01702"></a>                                     gpio_port_pins_t set_pins,
<a id="l01703"></a>                                     gpio_port_pins_t clear_pins);
<a id="l01704"></a>
<a id="l01705"></a>static inline int z_impl_gpio_port_set_clr_bits(const struct device *port,
<a id="l01706"></a>                                                gpio_port_pins_t set_pins,
<a id="l01707"></a>                                                gpio_port_pins_t clear_pins)
<a id="l01708"></a>{
<a id="l01709"></a>        __ASSERT((set_pins &amp; clear_pins) == 0, "Set and Clear pins overlap");
<a id="l01710"></a>
<a id="l01711"></a>        return z_impl_gpio_port_set_masked(port, set_pins | clear_pins, set_pins);
<a id="l01712"></a>}
<a id="l01713"></a>
<a id="l01729"></a>__syscall int gpio_pin_get_raw(const struct device *port, gpio_pin_t pin);
<a id="l01730"></a>
<a id="l01731"></a>static inline int z_impl_gpio_pin_get_raw(const struct device *port, gpio_pin_t pin)
<a id="l01732"></a>{
<a id="l01733"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01734"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01735"></a>        gpio_port_value_t value;
<a id="l01736"></a>        int ret;
<a id="l01737"></a>
<a id="l01738"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01739"></a>
<a id="l01740"></a>        ret = z_impl_gpio_port_get_raw(port, &amp;value);
<a id="l01741"></a>        if (ret == 0) {
<a id="l01742"></a>                ret = (value &amp; (gpio_port_pins_t)BIT(pin)) != 0 ? 1 : 0;
<a id="l01743"></a>        }
<a id="l01744"></a>
<a id="l01745"></a>        return ret;
<a id="l01746"></a>}
<a id="l01747"></a>
<a id="l01767"></a>__syscall int gpio_pin_get(const struct device *port, gpio_pin_t pin);
<a id="l01768"></a>
<a id="l01769"></a>static inline int z_impl_gpio_pin_get(const struct device *port, gpio_pin_t pin)
<a id="l01770"></a>{
<a id="l01771"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01772"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01773"></a>        gpio_port_value_t value;
<a id="l01774"></a>        int ret;
<a id="l01775"></a>
<a id="l01776"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01777"></a>
<a id="l01778"></a>        ret = z_impl_gpio_port_get(port, &amp;value);
<a id="l01779"></a>        if (ret == 0) {
<a id="l01780"></a>                ret = (value &amp; (gpio_port_pins_t)BIT(pin)) != 0 ? 1 : 0;
<a id="l01781"></a>        }
<a id="l01782"></a>
<a id="l01783"></a>        return ret;
<a id="l01784"></a>}
<a id="l01785"></a>
<a id="l01796"></a>static inline int gpio_pin_get_dt(const struct gpio_dt_spec *spec)
<a id="l01797"></a>{
<a id="l01798"></a>        return gpio_pin_get(spec-&gt;port, spec-&gt;pin);
<a id="l01799"></a>}
<a id="l01800"></a>
<a id="l01816"></a>__syscall int gpio_pin_set_raw(const struct device *port, gpio_pin_t pin, int value);
<a id="l01817"></a>
<a id="l01818"></a>static inline int z_impl_gpio_pin_set_raw(const struct device *port, gpio_pin_t pin,
<a id="l01819"></a>                                          int value)
<a id="l01820"></a>{
<a id="l01821"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01822"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01823"></a>        int ret;
<a id="l01824"></a>
<a id="l01825"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01826"></a>
<a id="l01827"></a>        if (value != 0) {
<a id="l01828"></a>                ret = z_impl_gpio_port_set_bits_raw(port, (gpio_port_pins_t)BIT(pin));
<a id="l01829"></a>        } else {
<a id="l01830"></a>                ret = z_impl_gpio_port_clear_bits_raw(port, (gpio_port_pins_t)BIT(pin));
<a id="l01831"></a>        }
<a id="l01832"></a>
<a id="l01833"></a>        return ret;
<a id="l01834"></a>}
<a id="l01835"></a>
<a id="l01857"></a>__syscall int gpio_pin_set(const struct device *port, gpio_pin_t pin, int value);
<a id="l01858"></a>
<a id="l01859"></a>static inline int z_impl_gpio_pin_set(const struct device *port, gpio_pin_t pin,
<a id="l01860"></a>                                      int value)
<a id="l01861"></a>{
<a id="l01862"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01863"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01864"></a>        const struct gpio_driver_data *const data =
<a id="l01865"></a>                        (const struct gpio_driver_data *)port-&gt;data;
<a id="l01866"></a>
<a id="l01867"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01868"></a>
<a id="l01869"></a>        if (data-&gt;invert &amp; (gpio_port_pins_t)BIT(pin)) {
<a id="l01870"></a>                value = (value != 0) ? 0 : 1;
<a id="l01871"></a>        }
<a id="l01872"></a>
<a id="l01873"></a>        return z_impl_gpio_pin_set_raw(port, pin, value);
<a id="l01874"></a>}
<a id="l01875"></a>
<a id="l01887"></a>static inline int gpio_pin_set_dt(const struct gpio_dt_spec *spec, int value)
<a id="l01888"></a>{
<a id="l01889"></a>        return gpio_pin_set(spec-&gt;port, spec-&gt;pin, value);
<a id="l01890"></a>}
<a id="l01891"></a>
<a id="l01902"></a>__syscall int gpio_pin_toggle(const struct device *port, gpio_pin_t pin);
<a id="l01903"></a>
<a id="l01904"></a>static inline int z_impl_gpio_pin_toggle(const struct device *port, gpio_pin_t pin)
<a id="l01905"></a>{
<a id="l01906"></a>        __unused const struct gpio_driver_config *const cfg =
<a id="l01907"></a>                (const struct gpio_driver_config *)port-&gt;config;
<a id="l01908"></a>
<a id="l01909"></a>        __ASSERT(gpio_port_pin_is_supported(cfg-&gt;port_pin_mask, pin), "Unsupported pin");
<a id="l01910"></a>
<a id="l01911"></a>        return z_impl_gpio_port_toggle_bits(port, (gpio_port_pins_t)BIT(pin));
<a id="l01912"></a>}
<a id="l01913"></a>
<a id="l01924"></a>static inline int gpio_pin_toggle_dt(const struct gpio_dt_spec *spec)
<a id="l01925"></a>{
<a id="l01926"></a>        return gpio_pin_toggle(spec-&gt;port, spec-&gt;pin);
<a id="l01927"></a>}
<a id="l01928"></a>
<a id="l01935"></a>static inline void gpio_init_callback(struct gpio_callback *callback,
<a id="l01936"></a>                                      gpio_callback_handler_t handler,
<a id="l01937"></a>                                      gpio_port_pins_t pin_mask)
<a id="l01938"></a>{
<a id="l01939"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio, init_callback, callback, handler, pin_mask);
<a id="l01940"></a>
<a id="l01941"></a>        __ASSERT(callback, "Callback pointer should not be NULL");
<a id="l01942"></a>        __ASSERT(handler, "Callback handler pointer should not be NULL");
<a id="l01943"></a>
<a id="l01944"></a>        callback-&gt;handler = handler;
<a id="l01945"></a>        callback-&gt;pin_mask = pin_mask;
<a id="l01946"></a>
<a id="l01947"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio, init_callback, callback);
<a id="l01948"></a>}
<a id="l01949"></a>
<a id="l01963"></a>static inline int gpio_add_callback(const struct device *port,
<a id="l01964"></a>                                    struct gpio_callback *callback)
<a id="l01965"></a>{
<a id="l01966"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l01967"></a>        int ret;
<a id="l01968"></a>
<a id="l01969"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio, add_callback, port, callback);
<a id="l01970"></a>
<a id="l01971"></a>        if (api-&gt;manage_callback == NULL) {
<a id="l01972"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio, add_callback, port, -ENOSYS);
<a id="l01973"></a>                return -ENOSYS;
<a id="l01974"></a>        }
<a id="l01975"></a>
<a id="l01976"></a>        ret = api-&gt;manage_callback(port, callback, true);
<a id="l01977"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio, add_callback, port, ret);
<a id="l01978"></a>        return ret;
<a id="l01979"></a>}
<a id="l01980"></a>
<a id="l01992"></a>static inline int gpio_add_callback_dt(const struct gpio_dt_spec *spec,
<a id="l01993"></a>                                       struct gpio_callback *callback)
<a id="l01994"></a>{
<a id="l01995"></a>        return gpio_add_callback(spec-&gt;port, callback);
<a id="l01996"></a>}
<a id="l01997"></a>
<a id="l02015"></a>static inline int gpio_remove_callback(const struct device *port,
<a id="l02016"></a>                                       struct gpio_callback *callback)
<a id="l02017"></a>{
<a id="l02018"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, port);
<a id="l02019"></a>        int ret;
<a id="l02020"></a>
<a id="l02021"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio, remove_callback, port, callback);
<a id="l02022"></a>
<a id="l02023"></a>        if (api-&gt;manage_callback == NULL) {
<a id="l02024"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio, remove_callback, port, -ENOSYS);
<a id="l02025"></a>                return -ENOSYS;
<a id="l02026"></a>        }
<a id="l02027"></a>
<a id="l02028"></a>        ret = api-&gt;manage_callback(port, callback, false);
<a id="l02029"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio, remove_callback, port, ret);
<a id="l02030"></a>        return ret;
<a id="l02031"></a>}
<a id="l02032"></a>
<a id="l02044"></a>static inline int gpio_remove_callback_dt(const struct gpio_dt_spec *spec,
<a id="l02045"></a>                                          struct gpio_callback *callback)
<a id="l02046"></a>{
<a id="l02047"></a>        return gpio_remove_callback(spec-&gt;port, callback);
<a id="l02048"></a>}
<a id="l02049"></a>
<a id="l02064"></a>__syscall int gpio_get_pending_int(const struct device *dev);
<a id="l02065"></a>
<a id="l02066"></a>static inline int z_impl_gpio_get_pending_int(const struct device *dev)
<a id="l02067"></a>{
<a id="l02068"></a>        const struct gpio_driver_api *api = DEVICE_API_GET(gpio, dev);
<a id="l02069"></a>        int ret;
<a id="l02070"></a>
<a id="l02071"></a>        SYS_PORT_TRACING_FUNC_ENTER(gpio, get_pending_int, dev);
<a id="l02072"></a>
<a id="l02073"></a>        if (api-&gt;get_pending_int == NULL) {
<a id="l02074"></a>                SYS_PORT_TRACING_FUNC_EXIT(gpio, get_pending_int, dev, -ENOSYS);
<a id="l02075"></a>                return -ENOSYS;
<a id="l02076"></a>        }
<a id="l02077"></a>
<a id="l02078"></a>        ret = api-&gt;get_pending_int(dev);
<a id="l02079"></a>        SYS_PORT_TRACING_FUNC_EXIT(gpio, get_pending_int, dev, ret);
<a id="l02080"></a>        return ret;
<a id="l02081"></a>}
<a id="l02082"></a>
<a id="l02086"></a>
<a id="l02087"></a>#ifdef __cplusplus
<a id="l02088"></a>}
<a id="l02089"></a>#endif
<a id="l02090"></a>
<a id="l02091"></a>#include &lt;zephyr/syscalls/gpio.h&gt;
<a id="l02092"></a>
<a id="l02093"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2019-2020 Nordic Semiconductor ASA；Copyright (c) 2019 Piotr Mienkowski；Copyright (c) 2017 ARM Ltd；Copyright (c) 2015-2016 Intel Corporation.；Apache-2.0许可证原文保留。

2. 将输出初始化为低电平。

3. 将输出初始化为高电平。

4. 根据逻辑电平初始化输出。

5. 使能GPIO引脚中断。

6. GPIO中断响应逻辑电平。这是组合用的标志，需要与其他GPIO_INT_*标志结合，形成有意义的配置。

7. GPIO中断响应边沿。注意，默认中断响应电平。这是组合用的标志，需要与其他GPIO_INT_*标志结合，形成有意义的配置。

8. 输入处于或转变为物理低电平／逻辑0时触发检测。这是组合用的标志，需要与其他GPIO_INT_*标志结合，形成有意义的配置。

9. 输入处于或转变为物理高电平／逻辑1时触发检测。这是组合用的标志，需要与其他GPIO_INT_*标志结合，形成有意义的配置。

10. 禁用或使能中断功能而不改变其他中断相关寄存器，例如不清除待处理寄存器。这是组合用的标志，需要与GPIO_INT_ENABLE或GPIO_INT_DISABLE结合，形成有意义的配置。

11. 结束CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT条件分支。

12. 开始INTERNAL_HIDDEN内部文档隐藏区域。

13. 结束CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT条件分支。

14. 结束CONFIG_GPIO_GET_CONFIG条件分支。

15. 结束CONFIG_GPIO_GET_DIRECTION条件分支。

16. 验证端口是否就绪。

17. 结束CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT条件分支。

18. 参见z_impl_gpio_pin_configure()中的说明。

19. 反转信号位。

20. 结束CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT条件分支。

21. pin按原值传给驱动，通常被用作数组索引，所以即使断言被编译移除，也必须检查其范围。

22. 结束CONFIG_GPIO_GET_DIRECTION条件分支。

23. 参见z_impl_gpio_pin_configure()中的说明。

24. 结束GPIO头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_GPIO_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

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

### `gpio.h`

符号定位：[gpio.h](../dt_bus_binding_reference/P001_GPIO绑定常量头文件参考.md)。

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `device_is_ready`

```c
bool device_is_ready(const struct device *dev)
```

验证设备是否已就绪、可以使用。

符号定位：[device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。

### `gpio_api_pin_get_config_t`

```c
int(* gpio_api_pin_get_config_t)(const struct device *port, gpio_pin_t pin, gpio_flags_t *flags)
```

获取单个引脚配置的回调API。

定义位置（Definition）：gpio.h:860。

符号定位：[gpio_api_pin_get_config_t](../hardware/P271_GPIO驱动后端.md#ga0b30055e6722031df85b712b6b151710)。

### `gpio_api_get_pending_int_t`

```c
uint32_t(* gpio_api_get_pending_int_t)(const struct device *dev)
```

获取待处理中断（Pending Interrupts）的回调API。

定义位置（Definition）：gpio.h:922。

符号定位：[gpio_api_get_pending_int_t](../hardware/P271_GPIO驱动后端.md#ga2a4ec98edb4dfb38cde49ab796fcbff3)。

### `gpio_api_manage_callback_t`

```c
int(* gpio_api_manage_callback_t)(const struct device *port, struct gpio_callback *cb, bool set)
```

添加或移除应用回调的回调API。

定义位置（Definition）：gpio.h:914。

符号定位：[gpio_api_manage_callback_t](../hardware/P271_GPIO驱动后端.md#ga2aaa71c0dd3728fdd2f8bd111245c456)。

### `gpio_api_port_clear_bits_raw_t`

```c
int(* gpio_api_port_clear_bits_raw_t)(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚物理电平置低的回调API。

定义位置（Definition）：gpio.h:889。

符号定位：[gpio_api_port_clear_bits_raw_t](../hardware/P271_GPIO驱动后端.md#ga43e339579ea19b4cc7d90a04c208e587)。

### `gpio_int_trig`

```c
gpio_int_trig
```

供pin_interrupt_configure驱动操作使用的中断触发条件（Interrupt Triggers）。

定义位置（Definition）：gpio.h:825。

符号定位：[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)。

### `gpio_api_port_get_direction_t`

```c
int(* gpio_api_port_get_direction_t)(const struct device *port, gpio_port_pins_t map, gpio_port_pins_t *inputs, gpio_port_pins_t *outputs)
```

获取端口中选定引脚方向（Direction）的回调API。

定义位置（Definition）：gpio.h:928。

符号定位：[gpio_api_port_get_direction_t](../hardware/P271_GPIO驱动后端.md#ga5d175c3355e88ee78b08539b61fc84fd)。

### `gpio_api_pin_configure_t`

```c
int(* gpio_api_pin_configure_t)(const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

配置单个引脚的回调API。

定义位置（Definition）：gpio.h:853。

符号定位：[gpio_api_pin_configure_t](../hardware/P271_GPIO驱动后端.md#ga6e7f6f2052ba10b6482445faaef4245f)。

### `gpio_int_mode`

```c
gpio_int_mode
```

供pin_interrupt_configure驱动操作使用的中断模式（Interrupt Modes）。

定义位置（Definition）：gpio.h:801。

符号定位：[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)。

### `gpio_api_port_toggle_bits_t`

```c
int(* gpio_api_port_toggle_bits_t)(const struct device *port, gpio_port_pins_t pins)
```

翻转选定输出引脚电平的回调API。

定义位置（Definition）：gpio.h:896。

符号定位：[gpio_api_port_toggle_bits_t](../hardware/P271_GPIO驱动后端.md#ga8486f9d9925531757b49e745ca7fdab2)。

### `gpio_api_port_set_masked_raw_t`

```c
int(* gpio_api_port_set_masked_raw_t)(const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

设置端口中选定输出引脚物理电平的回调API。

定义位置（Definition）：gpio.h:874。

符号定位：[gpio_api_port_set_masked_raw_t](../hardware/P271_GPIO驱动后端.md#gab3d809d4ffbba78cfad45bcdb8f5ce5a)。

### `gpio_api_port_set_bits_raw_t`

```c
int(* gpio_api_port_set_bits_raw_t)(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚物理电平置高的回调API。

定义位置（Definition）：gpio.h:882。

符号定位：[gpio_api_port_set_bits_raw_t](../hardware/P271_GPIO驱动后端.md#gabca79087ebe1c21911ef9a80eaaee43e)。

### `gpio_api_port_get_raw_t`

```c
int(* gpio_api_port_get_raw_t)(const struct device *port, gpio_port_value_t *value)
```

获取端口中全部输入引脚物理电平的回调API。

定义位置（Definition）：gpio.h:867。

符号定位：[gpio_api_port_get_raw_t](../hardware/P271_GPIO驱动后端.md#gad31b73d23fa7f6c96ec2f4a2523d61fb)。

### `gpio_api_pin_interrupt_configure_t`

```c
int(* gpio_api_pin_interrupt_configure_t)(const struct device *port, gpio_pin_t pin, enum gpio_int_mode mode, enum gpio_int_trig trig)
```

配置引脚中断的回调API。

定义位置（Definition）：gpio.h:905。

符号定位：[gpio_api_pin_interrupt_configure_t](../hardware/P271_GPIO驱动后端.md#gafa0e73e50f77890699cfe1a04ed9f155)。

### `GPIO_INT_TRIG_WAKE_HIGH`

```c
@ GPIO_INT_TRIG_WAKE_HIGH
```

输入处于物理高电平或转变为物理高电平时触发系统唤醒（System Wakeup）。

定义位置（Definition）：gpio.h:844。

符号定位：[GPIO_INT_TRIG_WAKE_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4)。

### `GPIO_INT_TRIG_WAKE`

```c
@ GPIO_INT_TRIG_WAKE
```

触发系统唤醒。

定义位置（Definition）：gpio.h:836。

符号定位：[GPIO_INT_TRIG_WAKE](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223)。

### `GPIO_INT_TRIG_HIGH`

```c
@ GPIO_INT_TRIG_HIGH
```

输入处于物理高电平或转变为物理高电平时触发检测。

定义位置（Definition）：gpio.h:832。

符号定位：[GPIO_INT_TRIG_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1)。

### `GPIO_INT_TRIG_BOTH`

```c
@ GPIO_INT_TRIG_BOTH
```

在引脚上升沿或下降沿触发检测。

定义位置（Definition）：gpio.h:834。

符号定位：[GPIO_INT_TRIG_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8)。

### `GPIO_INT_TRIG_WAKE_BOTH`

```c
@ GPIO_INT_TRIG_WAKE_BOTH
```

在引脚上升沿或下降沿触发系统唤醒。

定义位置（Definition）：gpio.h:846。

符号定位：[GPIO_INT_TRIG_WAKE_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5)。

### `GPIO_INT_TRIG_LOW`

```c
@ GPIO_INT_TRIG_LOW
```

输入处于物理低电平或转变为物理低电平时触发检测。

定义位置（Definition）：gpio.h:829。

符号定位：[GPIO_INT_TRIG_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134)。

### `GPIO_INT_TRIG_WAKE_LOW`

```c
@ GPIO_INT_TRIG_WAKE_LOW
```

输入处于物理低电平或转变为物理低电平时触发系统唤醒。

定义位置（Definition）：gpio.h:840。

符号定位：[GPIO_INT_TRIG_WAKE_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6)。

### `GPIO_INT_MODE_DISABLE_ONLY`

```c
@ GPIO_INT_MODE_DISABLE_ONLY
```

禁用之前配置的引脚中断，但不撤销其配置。

定义位置（Definition）：gpio.h:813。

符号定位：[GPIO_INT_MODE_DISABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e)。

### `GPIO_INT_MODE_EDGE`

```c
@ GPIO_INT_MODE_EDGE
```

使能边沿触发（Edge-triggered）的引脚中断。

定义位置（Definition）：gpio.h:807。

符号定位：[GPIO_INT_MODE_EDGE](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0)。

### `GPIO_INT_MODE_DISABLED`

```c
@ GPIO_INT_MODE_DISABLED
```

禁用引脚中断。

定义位置（Definition）：gpio.h:803。

符号定位：[GPIO_INT_MODE_DISABLED](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3)。

### `GPIO_INT_MODE_ENABLE_ONLY`

```c
@ GPIO_INT_MODE_ENABLE_ONLY
```

重新使能之前配置的引脚中断。

定义位置（Definition）：gpio.h:818。

符号定位：[GPIO_INT_MODE_ENABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688)。

### `GPIO_INT_MODE_LEVEL`

```c
@ GPIO_INT_MODE_LEVEL
```

使能电平触发（Level-triggered）的引脚中断。

定义位置（Definition）：gpio.h:805。

符号定位：[GPIO_INT_MODE_LEVEL](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9)。

### `gpio_add_callback`

```c
static int gpio_add_callback(const struct device *port, struct gpio_callback *callback)
```

添加应用回调。

定义位置（Definition）：gpio.h:1963。

符号定位：[gpio_add_callback](../hardware/P266_GPIO公共接口.md#ga05fd15af20386d69f9332354285b0cca)。

### `gpio_pin_set_raw`

```c
int gpio_pin_set_raw(const struct device *port, gpio_pin_t pin, int value)
```

设置输出引脚的物理电平。

符号定位：[gpio_pin_set_raw](../hardware/P266_GPIO公共接口.md#ga08824e05ea87c4ad2e48edaa13aad30a)。

### `gpio_port_set_masked`

```c
int gpio_port_set_masked(const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

设置端口中输出引脚的逻辑电平。

符号定位：[gpio_port_set_masked](../hardware/P266_GPIO公共接口.md#ga0c5ddbec7eb194ffed6cf12ae235ae04)。

### `GPIO_OUTPUT`

```c
#define GPIO_OUTPUT
```

将引脚使能为输出（Output），不改变输出状态。

定义位置（Definition）：gpio.h:58。

符号定位：[GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)。

### `gpio_pin_get_config`

```c
int gpio_pin_get_config(const struct device *port, gpio_pin_t pin, gpio_flags_t *flags)
```

获取单个引脚的配置。

符号定位：[gpio_pin_get_config](../hardware/P266_GPIO公共接口.md#ga133284b60a13c6dc50b87c1d04259f5e)。

### `GPIO_MAX_PINS_PER_PORT`

```c
#define GPIO_MAX_PINS_PER_PORT
```

gpio_port_pins_t能够支持的最大引脚数量。

定义位置（Definition）：gpio.h:691。

符号定位：[GPIO_MAX_PINS_PER_PORT](../hardware/P266_GPIO公共接口.md#ga1449ba90eaec5e6144fe4faae21f2e3f)。

### `gpio_pin_is_input`

```c
static int gpio_pin_is_input(const struct device *port, gpio_pin_t pin)
```

检查引脚是否配置为输入。

定义位置（Definition）：gpio.h:1270。

符号定位：[gpio_pin_is_input](../hardware/P266_GPIO公共接口.md#ga1454bc223fc2200aff3c4aab7d747da2)。

### `gpio_port_set_bits_raw`

```c
int gpio_port_set_bits_raw(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚的物理电平置高。

符号定位：[gpio_port_set_bits_raw](../hardware/P266_GPIO公共接口.md#ga18e6ca0df95566fecc0633efb04a075a)。

### `gpio_port_set_clr_bits_raw`

```c
int gpio_port_set_clr_bits_raw(const struct device *port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins)
```

设置选定输出引脚的物理电平。

符号定位：[gpio_port_set_clr_bits_raw](../hardware/P266_GPIO公共接口.md#ga1a06f729e76d39937d0572b6c531e038)。

### `gpio_pin_is_output_dt`

```c
static int gpio_pin_is_output_dt(const struct gpio_dt_spec *spec)
```

检查gpio_dt_spec指定的单个引脚是否配置为输出。

定义位置（Definition）：gpio.h:1343。

符号定位：[gpio_pin_is_output_dt](../hardware/P266_GPIO公共接口.md#ga2255c5681d17952ab89a4b6016d8e80d)。

### `gpio_pin_interrupt_configure_dt`

```c
static int gpio_pin_interrupt_configure_dt(const struct gpio_dt_spec *spec, gpio_flags_t flags)
```

根据gpio_dt_spec配置引脚中断。

定义位置（Definition）：gpio.h:1106。

符号定位：[gpio_pin_interrupt_configure_dt](../hardware/P266_GPIO公共接口.md#ga24f0b4ad30e6a8c81f51a2813478c793)。

### `gpio_remove_callback_dt`

```c
static int gpio_remove_callback_dt(const struct gpio_dt_spec *spec, struct gpio_callback *callback)
```

移除应用回调。

定义位置（Definition）：gpio.h:2044。

符号定位：[gpio_remove_callback_dt](../hardware/P266_GPIO公共接口.md#ga2c9f8fee2addfc0aeeeeb011d534f304)。

### `gpio_pin_toggle_dt`

```c
static int gpio_pin_toggle_dt(const struct gpio_dt_spec *spec)
```

翻转gpio_dt_spec指定的引脚电平。

定义位置（Definition）：gpio.h:1924。

符号定位：[gpio_pin_toggle_dt](../hardware/P266_GPIO公共接口.md#ga3272e866489da6c2e12c48f803c59e81)。

### `gpio_pin_t`

```c
uint8_t gpio_pin_t
```

用于保存GPIO引脚索引（Pin Index）的类型。

定义位置（Definition）：gpio.h:262。

符号定位：[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

### `gpio_pin_is_output`

```c
static int gpio_pin_is_output(const struct device *port, gpio_pin_t pin)
```

检查引脚是否配置为输出。

定义位置（Definition）：gpio.h:1315。

符号定位：[gpio_pin_is_output](../hardware/P266_GPIO公共接口.md#ga3b854d759180e222299ea445b401acc1)。

### `gpio_get_pending_int`

```c
int gpio_get_pending_int(const struct device *dev)
```

获取待处理中断的函数。

符号定位：[gpio_get_pending_int](../hardware/P266_GPIO公共接口.md#ga3f9e45de172a27f49c31a072c0c241e1)。

### `gpio_pin_configure_dt`

```c
static int gpio_pin_configure_dt(const struct gpio_dt_spec *spec, gpio_flags_t extra_flags)
```

根据gpio_dt_spec及附加标志配置单个引脚。

定义位置（Definition）：gpio.h:1208。

符号定位：[gpio_pin_configure_dt](../hardware/P266_GPIO公共接口.md#ga423db4f985098ddcaa504ec430e91913)。

### `gpio_port_set_clr_bits`

```c
int gpio_port_set_clr_bits(const struct device *port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins)
```

设置选定输出引脚的逻辑电平。

符号定位：[gpio_port_set_clr_bits](../hardware/P266_GPIO公共接口.md#ga45172f2b1bb09e8f3c89fa951cdefc14)。

### `gpio_pin_get`

```c
int gpio_pin_get(const struct device *port, gpio_pin_t pin)
```

获取输入引脚的逻辑电平。

符号定位：[gpio_pin_get](../hardware/P266_GPIO公共接口.md#ga496cd45fd6a2826c75d70c71f967234b)。

### `gpio_pin_set_dt`

```c
static int gpio_pin_set_dt(const struct gpio_dt_spec *spec, int value)
```

设置gpio_dt_spec指定的输出引脚的逻辑电平。

定义位置（Definition）：gpio.h:1887。

符号定位：[gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)。

### `gpio_add_callback_dt`

```c
static int gpio_add_callback_dt(const struct gpio_dt_spec *spec, struct gpio_callback *callback)
```

添加应用回调。

定义位置（Definition）：gpio.h:1992。

符号定位：[gpio_add_callback_dt](../hardware/P266_GPIO公共接口.md#ga54845eb95bc9636c3e6ff285300b6979)。

### `gpio_flags_t`

```c
uint32_t gpio_flags_t
```

用于保存GPIO配置标志（Configuration Flags）的类型。

定义位置（Definition）：gpio.h:282。

符号定位：[gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)。

### `GPIO_ACTIVE_LOW`

```c
#define GPIO_ACTIVE_LOW
```

GPIO引脚处于低电平时有效，即逻辑值为1。

定义位置（Definition）：gpio.h:24。

符号定位：[GPIO_ACTIVE_LOW](../hardware/P266_GPIO公共接口.md#ga62cea8989df2425e5e5e712217d65f46)。

### `gpio_pin_get_raw`

```c
int gpio_pin_get_raw(const struct device *port, gpio_pin_t pin)
```

获取输入引脚的物理电平。

符号定位：[gpio_pin_get_raw](../hardware/P266_GPIO公共接口.md#ga635975f1df6157c7e8a6c67bac55fbc0)。

### `GPIO_INT_WAKEUP`

```c
#define GPIO_INT_WAKEUP
```

将GPIO中断配置为从低功耗模式（Low Power Mode）唤醒系统。

定义位置（Definition）：gpio.h:83。

符号定位：[GPIO_INT_WAKEUP](../hardware/P266_GPIO公共接口.md#ga644109ce84c8feffe1226b9b50122a96)。

### `gpio_init_callback`

```c
static void gpio_init_callback(struct gpio_callback *callback, gpio_callback_handler_t handler, gpio_port_pins_t pin_mask)
```

用于正确初始化struct gpio_callback的辅助函数。

定义位置（Definition）：gpio.h:1935。

符号定位：[gpio_init_callback](../hardware/P266_GPIO公共接口.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)。

### `gpio_pin_is_input_dt`

```c
static int gpio_pin_is_input_dt(const struct gpio_dt_spec *spec)
```

检查gpio_dt_spec指定的单个引脚是否配置为输入。

定义位置（Definition）：gpio.h:1298。

符号定位：[gpio_pin_is_input_dt](../hardware/P266_GPIO公共接口.md#ga7aaec28a83cac63bd87fc94cc72664b1)。

### `GPIO_INPUT`

```c
#define GPIO_INPUT
```

将引脚使能为输入（Input）。

定义位置（Definition）：gpio.h:55。

符号定位：[GPIO_INPUT](../hardware/P266_GPIO公共接口.md#ga7be6a0cc9aa65da1d4ee5751b4085853)。

### `gpio_port_get`

```c
int gpio_port_get(const struct device *port, gpio_port_value_t *value)
```

获取端口中全部输入引脚的逻辑电平（Logical Level）。

符号定位：[gpio_port_get](../hardware/P266_GPIO公共接口.md#ga7c7a53371834c7646dc7f41ca0bb7921)。

### `gpio_port_pins_t`

```c
uint32_t gpio_port_pins_t
```

标识某个端口（Port）关联的一组引脚。

定义位置（Definition）：gpio.h:241。

符号定位：[gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)。

### `gpio_pin_get_config_dt`

```c
static int gpio_pin_get_config_dt(const struct gpio_dt_spec *spec, gpio_flags_t *flags)
```

获取gpio_dt_spec指定的单个引脚的配置。

定义位置（Definition）：gpio.h:1405。

符号定位：[gpio_pin_get_config_dt](../hardware/P266_GPIO公共接口.md#ga820448aa4be8b14839bc6a00c9f34bb4)。

### `gpio_port_toggle_bits`

```c
int gpio_port_toggle_bits(const struct device *port, gpio_port_pins_t pins)
```

翻转选定输出引脚的电平。

符号定位：[gpio_port_toggle_bits](../hardware/P266_GPIO公共接口.md#ga82977d8706fb9f464db455bd0e9ac2e4)。

### `GPIO_INT_DISABLE`

```c
#define GPIO_INT_DISABLE
```

禁用GPIO引脚中断（Interrupt）。

定义位置（Definition）：gpio.h:108。

符号定位：[GPIO_INT_DISABLE](../hardware/P266_GPIO公共接口.md#ga91657faac28f9b213105dd61a419dd5a)。

### `gpio_port_clear_bits`

```c
int gpio_port_clear_bits(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚的逻辑电平置为无效（Inactive）。

符号定位：[gpio_port_clear_bits](../hardware/P266_GPIO公共接口.md#ga9318c349663568f1fb9400b9458765dc)。

### `gpio_pin_interrupt_configure`

```c
int gpio_pin_interrupt_configure(const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

配置引脚中断。

符号定位：[gpio_pin_interrupt_configure](../hardware/P266_GPIO公共接口.md#ga9618f254365381063439a0e9c5e787cb)。

### `gpio_port_clear_bits_raw`

```c
int gpio_port_clear_bits_raw(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚的物理电平置低。

符号定位：[gpio_port_clear_bits_raw](../hardware/P266_GPIO公共接口.md#ga9d2c9daeec7ce127fc786ead566ad27f)。

### `gpio_port_set_masked_raw`

```c
int gpio_port_set_masked_raw(const struct device *port, gpio_port_pins_t mask, gpio_port_value_t value)
```

设置端口中输出引脚的物理电平。

符号定位：[gpio_port_set_masked_raw](../hardware/P266_GPIO公共接口.md#ga9e7b50d720fda362941acc1e3b3b2922)。

### `gpio_pin_toggle`

```c
int gpio_pin_toggle(const struct device *port, gpio_pin_t pin)
```

翻转引脚电平。

符号定位：[gpio_pin_toggle](../hardware/P266_GPIO公共接口.md#gaa761788e22a185db227dce7c24915154)。

### `GPIO_PULL_UP`

```c
#define GPIO_PULL_UP
```

使能GPIO引脚上拉（Pull-up）。

定义位置（Definition）：gpio.h:73。

符号定位：[GPIO_PULL_UP](../hardware/P266_GPIO公共接口.md#gaaa7921da231fd2b96575fa522e2c1970)。

### `gpio_pin_get_dt`

```c
static int gpio_pin_get_dt(const struct gpio_dt_spec *spec)
```

获取gpio_dt_spec指定的输入引脚的逻辑电平。

定义位置（Definition）：gpio.h:1796。

符号定位：[gpio_pin_get_dt](../hardware/P266_GPIO公共接口.md#gaabeb2d0d98856c7ff78be36651d6bbc1)。

### `gpio_is_ready_dt`

```c
static bool gpio_is_ready_dt(const struct gpio_dt_spec *spec)
```

验证GPIO端口是否就绪（Ready）。

定义位置（Definition）：gpio.h:982。

符号定位：[gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)。

### `gpio_port_pin_is_supported`

```c
static bool gpio_port_pin_is_supported(gpio_port_pins_t port_pin_mask, gpio_pin_t pin)
```

检查引脚是否在有效范围内，并且受GPIO控制器支持。

定义位置（Definition）：gpio.h:708。

符号定位：[gpio_port_pin_is_supported](../hardware/P266_GPIO公共接口.md#gab7465c5401aa9d47d68980455847be9f)。

### `gpio_port_value_t`

```c
uint32_t gpio_port_value_t
```

提供某个端口关联的一组引脚的值。

定义位置（Definition）：gpio.h:254。

符号定位：[gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)。

### `gpio_remove_callback`

```c
static int gpio_remove_callback(const struct device *port, struct gpio_callback *callback)
```

移除应用回调。

定义位置（Definition）：gpio.h:2015。

符号定位：[gpio_remove_callback](../hardware/P266_GPIO公共接口.md#gac1e94ba8faac79f469447e9b5d2f8c06)。

### `gpio_port_get_direction`

```c
int gpio_port_get_direction(const struct device *port, gpio_port_pins_t map, gpio_port_pins_t *inputs, gpio_port_pins_t *outputs)
```

获取端口中选定引脚的方向。

符号定位：[gpio_port_get_direction](../hardware/P266_GPIO公共接口.md#gad2b2945dbe6987ac425e000721a894c4)。

### `gpio_dt_flags_t`

```c
uint16_t gpio_dt_flags_t
```

用于保存GPIO设备树标志（Devicetree Flags）的类型。

定义位置（Definition）：gpio.h:274。

符号定位：[gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)。

### `gpio_pin_set`

```c
int gpio_pin_set(const struct device *port, gpio_pin_t pin, int value)
```

设置输出引脚的逻辑电平。

符号定位：[gpio_pin_set](../hardware/P266_GPIO公共接口.md#gadac09ef40fc1ba5d8bb40965efde0fda)。

### `GPIO_PULL_DOWN`

```c
#define GPIO_PULL_DOWN
```

使能GPIO引脚下拉（Pull-down）。

定义位置（Definition）：gpio.h:76。

符号定位：[GPIO_PULL_DOWN](../hardware/P266_GPIO公共接口.md#gadec1802e074f3021d464da09cd66c7cf)。

### `gpio_port_get_raw`

```c
int gpio_port_get_raw(const struct device *port, gpio_port_value_t *value)
```

获取端口中全部输入引脚的物理电平（Physical Level）。

符号定位：[gpio_port_get_raw](../hardware/P266_GPIO公共接口.md#gae2a49b36cae2e17fc665a3bd844f50b4)。

### `gpio_port_set_bits`

```c
int gpio_port_set_bits(const struct device *port, gpio_port_pins_t pins)
```

将选定输出引脚的逻辑电平置为有效（Active）。

符号定位：[gpio_port_set_bits](../hardware/P266_GPIO公共接口.md#gae450ff904686aa4b8fd81bc0dbbafdb5)。

### `gpio_pin_configure`

```c
int gpio_pin_configure(const struct device *port, gpio_pin_t pin, gpio_flags_t flags)
```

配置单个引脚。

符号定位：[gpio_pin_configure](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)。

### `gpio_callback_handler_t`

```c
void(* gpio_callback_handler_t)(const struct device *port, struct gpio_callback *cb, gpio_port_pins_t pins)
```

定义应用回调处理函数（Callback Handler）的签名。

定义位置（Definition）：gpio.h:757。

符号定位：[gpio_callback_handler_t](../hardware/P266_GPIO公共接口.md#gaf0aa40279d32b1b8332f2f23a39510af)。

### `sys_snode_t`

```c
struct _snode sys_snode_t
```

单向链表节点（Singly Linked List Node）结构。

定义位置（Definition）：slist.h:44。

符号定位：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)。

### `SYS_PORT_TRACING_FUNC_ENTER`

```c
#define SYS_PORT_TRACING_FUNC_ENTER(type, func,...)
```

用于函数入口的跟踪宏（Tracing Macro），函数可以有返回值或没有返回值。

定义位置（Definition）：tracing_macros.h:246。

符号定位：[SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)。

### `SYS_PORT_TRACING_FUNC_EXIT`

```c
#define SYS_PORT_TRACING_FUNC_EXIT(type, func,...)
```

用于函数执行结束时的跟踪宏。

定义位置（Definition）：tracing_macros.h:272。

符号定位：[SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)。

### `BIT`

```c
#define BIT(n)
```

将第n位设为1的无符号整数；在汇编语言中为有符号数。

定义位置（Definition）：util_macro.h:44。

符号定位：[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

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

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `flags`

```c
flags
```

定义位置（Definition）：parser.h:86。

符号定位：[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

### `slist.h`

单向链表API头文件。

符号定位：[slist.h](../slist_reference/P002_单向链表头文件参考.md)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `device::data`

```c
void * data
```

设备实例私有数据的地址。

定义位置（Definition）：device.h:553。

符号定位：[device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)。

### `device::config`

```c
const void * config
```

设备实例配置信息的地址。

定义位置（Definition）：device.h:547。

符号定位：[device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)。

### `gpio_callback`

GPIO回调结构（Callback Structure）。

定义位置（Definition）：gpio.h:771。

符号定位：[gpio_callback](../hardware/P270_GPIO回调结构.md)。

### `gpio_callback::node`

```c
sys_snode_t node
```

供驱动内部使用，用户不应修改它；参见drivers/gpio/gpio_ut……（原符号提示在此截断）。

定义位置（Definition）：gpio.h:775。

符号定位：[gpio_callback::node](../hardware/P270_GPIO回调结构.md#ab60e7093072964bd818d536c746211e4)。

### `gpio_callback::pin_mask`

```c
gpio_port_pins_t pin_mask
```

回调关注的引脚掩码；为0时永远不会调用此回调。

定义位置（Definition）：gpio.h:786。

符号定位：[gpio_callback::pin_mask](../hardware/P270_GPIO回调结构.md#ace5c2b83f1d51f73877a1f2c54ba8c67)。

### `gpio_callback::handler`

```c
gpio_callback_handler_t handler
```

条件符合时实际调用的回调函数。

定义位置（Definition）：gpio.h:778。

符号定位：[gpio_callback::handler](../hardware/P270_GPIO回调结构.md#af89dc41cbd610d81ac03cae7ab764ceb)。

### `gpio_driver_api`

驱动操作（Driver Operations）：GPIO驱动操作；原提示含有格式标签。

定义位置（Definition）：gpio.h:934。

符号定位：[gpio_driver_api](../hardware/P272_GPIO驱动函数表.md)。

### `gpio_driver_api::port_set_bits_raw`

```c
gpio_api_port_set_bits_raw_t port_set_bits_raw
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:949。

符号定位：[gpio_driver_api::port_set_bits_raw](../hardware/P272_GPIO驱动函数表.md#a12abf1e8eaa9e92af931b1045fe0e377)。

### `gpio_driver_api::get_pending_int`

```c
gpio_api_get_pending_int_t get_pending_int
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:962。

符号定位：[gpio_driver_api::get_pending_int](../hardware/P272_GPIO驱动函数表.md#a1c66d09d500fbed09cf9c85973dc9bcf)。

### `gpio_driver_api::port_get_raw`

```c
gpio_api_port_get_raw_t port_get_raw
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:945。

符号定位：[gpio_driver_api::port_get_raw](../hardware/P272_GPIO驱动函数表.md#a2663c69ada10dd209cc2f266b733c97c)。

### `gpio_driver_api::port_toggle_bits`

```c
gpio_api_port_toggle_bits_t port_toggle_bits
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:953。

符号定位：[gpio_driver_api::port_toggle_bits](../hardware/P272_GPIO驱动函数表.md#a676651f5ef63de226e244ffe7a6c0ece)。

### `gpio_driver_api::pin_configure`

```c
gpio_api_pin_configure_t pin_configure
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:936。

符号定位：[gpio_driver_api::pin_configure](../hardware/P272_GPIO驱动函数表.md#a6b79f508317faa0f2959fe63449534c5)。

### `gpio_driver_api::pin_interrupt_configure`

```c
gpio_api_pin_interrupt_configure_t pin_interrupt_configure
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:955。

符号定位：[gpio_driver_api::pin_interrupt_configure](../hardware/P272_GPIO驱动函数表.md#a77fbd18d3c4d7f48f3f640a80d8b0555)。

### `gpio_driver_api::port_get_direction`

```c
gpio_api_port_get_direction_t port_get_direction
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:968。

符号定位：[gpio_driver_api::port_get_direction](../hardware/P272_GPIO驱动函数表.md#a7e4adc56ec0cb667cf4d4f711de52be4)。

### `gpio_driver_api::manage_callback`

```c
gpio_api_manage_callback_t manage_callback
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:960。

符号定位：[gpio_driver_api::manage_callback](../hardware/P272_GPIO驱动函数表.md#a92cdd5aeab396e756773cb00dbe87c33)。

### `gpio_driver_api::pin_get_config`

```c
gpio_api_pin_get_config_t pin_get_config
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:942。

符号定位：[gpio_driver_api::pin_get_config](../hardware/P272_GPIO驱动函数表.md#abdc60c3175e972aef218978ea5ad6c38)。

### `gpio_driver_api::port_clear_bits_raw`

```c
gpio_api_port_clear_bits_raw_t port_clear_bits_raw
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:951。

符号定位：[gpio_driver_api::port_clear_bits_raw](../hardware/P272_GPIO驱动函数表.md#ad8ceab5ca80067db8d7c8be884ac9de1)。

### `gpio_driver_api::port_set_masked_raw`

```c
gpio_api_port_set_masked_raw_t port_set_masked_raw
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：gpio.h:947。

符号定位：[gpio_driver_api::port_set_masked_raw](../hardware/P272_GPIO驱动函数表.md#af1d1268ef57bcedce138c64b95ba2878)。

### `gpio_driver_config`

所有GPIO驱动共用此结构；它应当是所指向对象的第一个成员……（原符号提示在此截断）。

定义位置（Definition）：gpio.h:722。

符号定位：[gpio_driver_config](../hardware/P268_GPIO公共驱动配置.md)。

### `gpio_driver_config::port_pin_mask`

```c
gpio_port_pins_t port_pin_mask
```

标识控制器支持哪些引脚的掩码。

定义位置（Definition）：gpio.h:728。

符号定位：[gpio_driver_config::port_pin_mask](../hardware/P268_GPIO公共驱动配置.md#af73c0d9d433b86b9d0e0c6703e737052)。

### `gpio_driver_data`

所有GPIO驱动共用此结构；它应当是驱动的……中的第一个成员（原符号提示在此截断）。

定义位置（Definition）：gpio.h:735。

符号定位：[gpio_driver_data](../hardware/P269_GPIO公共驱动数据.md)。

### `gpio_driver_data::invert`

```c
gpio_port_pins_t invert
```

标识配置为低有效（Active Low）的引脚的掩码。

定义位置（Definition）：gpio.h:741。

符号定位：[gpio_driver_data::invert](../hardware/P269_GPIO公共驱动数据.md#ab62038a3c7c341cafda6665dfab3f169)。

### `gpio_dt_spec`

保存设备树（Devicetree）中指定的GPIO引脚信息的容器。

定义位置（Definition）：gpio.h:296。

符号定位：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

### `gpio_dt_spec::port`

```c
const struct device * port
```

控制此引脚的GPIO设备。

定义位置（Definition）：gpio.h:298。

符号定位：[gpio_dt_spec::port](../hardware/P267_GPIO设备树描述.md#a5d617d47e2f568c7a4402a8f5a40ed4f)。

### `gpio_dt_spec::pin`

```c
gpio_pin_t pin
```

引脚在设备上的编号。

定义位置（Definition）：gpio.h:300。

符号定位：[gpio_dt_spec::pin](../hardware/P267_GPIO设备树描述.md#ad7e6fbb0cba0be94a47d4f2add056c84)。

### `gpio_dt_spec::dt_flags`

```c
gpio_dt_flags_t dt_flags
```

设备树指定的引脚配置标志。

定义位置（Definition）：gpio.h:302。

符号定位：[gpio_dt_spec::dt_flags](../hardware/P267_GPIO设备树描述.md#ae3b90e7e22708798c67da94f72ad1ab0)。

### `tracing.h`

跟踪子系统（Tracing Subsystem）API的主头文件。

符号定位：[tracing.h](../tracing_core_reference/P007_跟踪公共头文件参考.md)。

## 2.4\_源码跟踪译注

> 译注——设备树描述与运行配置：gpio_dt_spec保存端口设备指针、引脚编号及16位设备树标志；GPIO_DT_SPEC_GET_*展开为结构初始化器，不是动态申请的对象。带_OR的宏按属性索引是否存在选择回退值；gpio_is_ready_dt只检查端口设备就绪，不检查引脚范围、配置、电气连接或回退对象是否完整。gpio_pin_configure_dt才把dt_flags与extra_flags合并后执行配置。

> 译注——物理与逻辑电平：raw接口使用物理电平，逻辑接口依据gpio_driver_data.invert转换。GPIO_OUTPUT_HIGH／LOW指定物理初始值，GPIO_OUTPUT_ACTIVE／INACTIVE指定逻辑初始值；低有效引脚的逻辑1对应物理低电平。读取失败时先处理负错误码，不能直接把任何非零返回都当高电平。gpio_pin_get_dt／set_dt只传端口与引脚，实际极性来自已经配置的驱动数据，而非每次直接读取spec->dt_flags。

> 译注——配置失败的边界：gpio_pin_configure先转换逻辑初始值，并在调用驱动pin_configure之前修改invert掩码；当前包装在驱动失败后不恢复该掩码。因此错误返回不能证明硬件状态与软件极性都保持原状。配置、成功读回和引脚实际电平分别需要证据。

> 译注——引脚索引与位掩码：gpio_port_pins_t和gpio_port_value_t是32位，gpio_pin_t是8位索引；BIT(pin)才是端口位掩码，二者不能互换。gpio_port_pin_is_supported先检查索引上限再检查port_pin_mask。配置、查询配置及中断配置保留运行期索引上限检查；许多其他内核包装仅通过断言检查支持范围，不能将所有入口都视为始终返回-EINVAL的参数校验器。用户态系统调用另有对象、支持范围与输出缓冲区访问检查。

> 译注——保留引脚：gpio-reserved-ranges由起始偏移与长度成对组成，ngpios包含槽位范围内可能存在的空洞。GPIO_DT_RESERVED_RANGES_NGPIOS在不存在保留范围属性时返回0，不能单靠它表示所有允许引脚；GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC另外限制ngpios范围并排除保留位，ngpios为0时返回0。控制器掩码不能替代实际芯片封装和板级连接核对。

> 译注——中断极性：GPIO_INT_EDGE_RISING／FALLING和GPIO_INT_LEVEL_HIGH／LOW使用物理电平，TO_ACTIVE／TO_INACTIVE及LEVEL_ACTIVE／INACTIVE使用已保存的低有效极性。中断_dt包装仅从dt_flags合入GPIO_INT_WAKEUP，没有重新应用GPIO_ACTIVE_LOW；应先正确配置引脚。GPIO_INT_EDGE_BOTH同时设置低／高触发位，但不设置GPIO_INT_LEVELS_LOGICAL，因此不会进入逻辑极性转换分支。普通配置中断可能清状态；保留配置的ENABLE_ONLY／DISABLE_ONLY另受CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT和驱动支持约束。

> 译注——驱动能力与配置：CONFIG_GPIO_GET_CONFIG、CONFIG_GPIO_GET_DIRECTION以及仅使能／禁用中断的选项在本次Kconfig中标为实验性（Experimental）。启用选项不等于驱动实现对应操作。查询配置、查询方向、中断配置、回调管理与待处理中断查询的相关包装检查可选操作指针并可返回-ENOSYS；基础端口读写等包装直接调用操作，不能统一假定都有空指针回退。

> 译注——回调不是中断开关：gpio_init_callback只写入handler和pin_mask，gpio_add_callback委托驱动管理回调，两者都不代替引脚中断配置。通用gpio_manage_callback移除再前插已有节点，删除不存在节点返回-EINVAL；gpio_fire_callbacks向处理函数传入触发引脚与关注掩码的交集。回调对象应在注册期间保持有效；辅助函数自身没有增加锁，安全遍历宏也不代表任意并发修改均安全。

> 译注——端口批量操作：set／clear逻辑接口通过带掩码写入路径完成极性转换，set_clr要求两组掩码不重叠。toggle调用驱动翻转操作，物理与逻辑翻转方向一致；公共包装不执行读后再写。具体驱动如何实现、是否支持目标引脚以及实际电气结果，不能从公共函数签名单独推定。

> 译注——版本边界：本批核对GPIO公共头文件、GPIO工具辅助头文件、设备树标志定义、系统调用处理、Kconfig及控制器绑定共六份官方源码并记录摘要。源码页的非注释代码与读取的官方头文件一致；latest、滚动main与仓库版本不自动相同。仓库定位使用相对链接，本次未构建固件、配置实板引脚或操作硬件。

头文件相对定位：[include/zephyr/drivers/gpio.h](../../../include/zephyr/drivers/gpio.h)，关联实现／接口：[include/zephyr/drivers/gpio/gpio_utils.h](../../../include/zephyr/drivers/gpio/gpio_utils.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/gpio.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/gpio/gpio_utils.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_GPIO驱动头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/tracing/tracing.h](../tracing_core_reference/P007_跟踪公共头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/dt-bindings/gpio/gpio.h](../dt_bus_binding_reference/P001_GPIO绑定常量头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [gpio_port_value_t](../hardware/P266_GPIO公共接口.md#gabcebe24c93486896e1dfc2459ec25693)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [device](../device_reference/P002_设备对象结构.md)
- [port](../hardware/P267_GPIO设备树描述.md#a5d617d47e2f568c7a4402a8f5a40ed4f)
- [pin](../hardware/P267_GPIO设备树描述.md#ad7e6fbb0cba0be94a47d4f2add056c84)
- [dt_flags](../hardware/P267_GPIO设备树描述.md#ae3b90e7e22708798c67da94f72ad1ab0)
- [gpio_port_pin_is_supported](../hardware/P266_GPIO公共接口.md#gab7465c5401aa9d47d68980455847be9f)
- [GPIO_MAX_PINS_PER_PORT](../hardware/P266_GPIO公共接口.md#ga1449ba90eaec5e6144fe4faae21f2e3f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [gpio_driver_config](../hardware/P268_GPIO公共驱动配置.md)
- [port_pin_mask](../hardware/P268_GPIO公共驱动配置.md#af73c0d9d433b86b9d0e0c6703e737052)
- [gpio_driver_data](../hardware/P269_GPIO公共驱动数据.md)
- [invert](../hardware/P269_GPIO公共驱动数据.md#ab62038a3c7c341cafda6665dfab3f169)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [gpio_callback_handler_t](../hardware/P266_GPIO公共接口.md#gaf0aa40279d32b1b8332f2f23a39510af)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../hardware/P270_GPIO回调结构.md#ab60e7093072964bd818d536c746211e4)
- [handler](../hardware/P270_GPIO回调结构.md#af89dc41cbd610d81ac03cae7ab764ceb)
- [pin_mask](../hardware/P270_GPIO回调结构.md#ace5c2b83f1d51f73877a1f2c54ba8c67)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [GPIO_INT_MODE_DISABLED](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbabc4f473bdaf0845f77b3c89c2d135dd3)
- [GPIO_INT_DISABLE](../hardware/P266_GPIO公共接口.md#ga91657faac28f9b213105dd61a419dd5a)
- [GPIO_INT_MODE_LEVEL](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaf2fa5b12b76cc4f2968f55096cae63f9)
- [GPIO_INT_MODE_EDGE](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba18e29c81401bd9f28b0ef8767baccbf0)
- [GPIO_INT_MODE_DISABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dba00014847912546193ab9fb34c339299e)
- [GPIO_INT_MODE_ENABLE_ONLY](../hardware/P271_GPIO驱动后端.md#gga82f0562c44cf0f76cc7e16d606a975dbaec41f93d5707ebb4e4d151dbfec0d688)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [GPIO_INT_TRIG_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da7a73d6c4e1c7ec16d28d8d8825a0c134)
- [GPIO_INT_TRIG_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5351b6c2d6167f5cdf5e50ca267243c1)
- [GPIO_INT_TRIG_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da5e5b92f415141cd2bc80d26230e82ca8)
- [GPIO_INT_TRIG_WAKE](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da31c46bda610132a2bc1fde39217ec223)
- [GPIO_INT_WAKEUP](../hardware/P266_GPIO公共接口.md#ga644109ce84c8feffe1226b9b50122a96)
- [GPIO_INT_TRIG_WAKE_LOW](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da944ca13beced64344ea4683d75e7ffd6)
- [GPIO_INT_TRIG_WAKE_HIGH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da018303c2b295f4572d3653cef5150ac4)
- [GPIO_INT_TRIG_WAKE_BOTH](../hardware/P271_GPIO驱动后端.md#gga4ea6fd78423e6e3004702b599bc7b12da71128b71696754e029c200b10797dca5)
- [gpio_api_pin_configure_t](../hardware/P271_GPIO驱动后端.md#ga6e7f6f2052ba10b6482445faaef4245f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [gpio_api_pin_get_config_t](../hardware/P271_GPIO驱动后端.md#ga0b30055e6722031df85b712b6b151710)
- [gpio_api_port_get_raw_t](../hardware/P271_GPIO驱动后端.md#gad31b73d23fa7f6c96ec2f4a2523d61fb)
- [gpio_api_port_set_masked_raw_t](../hardware/P271_GPIO驱动后端.md#gab3d809d4ffbba78cfad45bcdb8f5ce5a)
- [gpio_api_port_set_bits_raw_t](../hardware/P271_GPIO驱动后端.md#gabca79087ebe1c21911ef9a80eaaee43e)
- [gpio_api_port_clear_bits_raw_t](../hardware/P271_GPIO驱动后端.md#ga43e339579ea19b4cc7d90a04c208e587)
- [gpio_api_port_toggle_bits_t](../hardware/P271_GPIO驱动后端.md#ga8486f9d9925531757b49e745ca7fdab2)
- [gpio_api_pin_interrupt_configure_t](../hardware/P271_GPIO驱动后端.md#gafa0e73e50f77890699cfe1a04ed9f155)
- [gpio_api_manage_callback_t](../hardware/P271_GPIO驱动后端.md#ga2aaa71c0dd3728fdd2f8bd111245c456)
- [gpio_api_get_pending_int_t](../hardware/P271_GPIO驱动后端.md#ga2a4ec98edb4dfb38cde49ab796fcbff3)
- [gpio_api_port_get_direction_t](../hardware/P271_GPIO驱动后端.md#ga5d175c3355e88ee78b08539b61fc84fd)
- [gpio_driver_api](../hardware/P272_GPIO驱动函数表.md)
- [pin_configure](../hardware/P272_GPIO驱动函数表.md#a6b79f508317faa0f2959fe63449534c5)
- [pin_get_config](../hardware/P272_GPIO驱动函数表.md#abdc60c3175e972aef218978ea5ad6c38)
- [port_get_raw](../hardware/P272_GPIO驱动函数表.md#a2663c69ada10dd209cc2f266b733c97c)
- [port_set_masked_raw](../hardware/P272_GPIO驱动函数表.md#af1d1268ef57bcedce138c64b95ba2878)
- [port_set_bits_raw](../hardware/P272_GPIO驱动函数表.md#a12abf1e8eaa9e92af931b1045fe0e377)
- [port_clear_bits_raw](../hardware/P272_GPIO驱动函数表.md#ad8ceab5ca80067db8d7c8be884ac9de1)
- [port_toggle_bits](../hardware/P272_GPIO驱动函数表.md#a676651f5ef63de226e244ffe7a6c0ece)
- [pin_interrupt_configure](../hardware/P272_GPIO驱动函数表.md#a77fbd18d3c4d7f48f3f640a80d8b0555)
- [manage_callback](../hardware/P272_GPIO驱动函数表.md#a92cdd5aeab396e756773cb00dbe87c33)
- [get_pending_int](../hardware/P272_GPIO驱动函数表.md#a1c66d09d500fbed09cf9c85973dc9bcf)
- [port_get_direction](../hardware/P272_GPIO驱动函数表.md#a7e4adc56ec0cb667cf4d4f711de52be4)
- [gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [gpio_pin_interrupt_configure](../hardware/P266_GPIO公共接口.md#ga9618f254365381063439a0e9c5e787cb)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)
- [SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [gpio_pin_interrupt_configure_dt](../hardware/P266_GPIO公共接口.md#ga24f0b4ad30e6a8c81f51a2813478c793)
- [gpio_pin_configure](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)
- [GPIO_PULL_UP](../hardware/P266_GPIO公共接口.md#gaaa7921da231fd2b96575fa522e2c1970)
- [GPIO_PULL_DOWN](../hardware/P266_GPIO公共接口.md#gadec1802e074f3021d464da09cd66c7cf)
- [GPIO_INPUT](../hardware/P266_GPIO公共接口.md#ga7be6a0cc9aa65da1d4ee5751b4085853)
- [GPIO_OUTPUT](../hardware/P266_GPIO公共接口.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)
- [GPIO_ACTIVE_LOW](../hardware/P266_GPIO公共接口.md#ga62cea8989df2425e5e5e712217d65f46)
- [gpio_pin_configure_dt](../hardware/P266_GPIO公共接口.md#ga423db4f985098ddcaa504ec430e91913)
- [gpio_port_get_direction](../hardware/P266_GPIO公共接口.md#gad2b2945dbe6987ac425e000721a894c4)
- [gpio_pin_is_input](../hardware/P266_GPIO公共接口.md#ga1454bc223fc2200aff3c4aab7d747da2)
- [gpio_pin_is_input_dt](../hardware/P266_GPIO公共接口.md#ga7aaec28a83cac63bd87fc94cc72664b1)
- [gpio_pin_is_output](../hardware/P266_GPIO公共接口.md#ga3b854d759180e222299ea445b401acc1)
- [gpio_pin_is_output_dt](../hardware/P266_GPIO公共接口.md#ga2255c5681d17952ab89a4b6016d8e80d)
- [gpio_pin_get_config](../hardware/P266_GPIO公共接口.md#ga133284b60a13c6dc50b87c1d04259f5e)
- [gpio_pin_get_config_dt](../hardware/P266_GPIO公共接口.md#ga820448aa4be8b14839bc6a00c9f34bb4)
- [gpio_port_get_raw](../hardware/P266_GPIO公共接口.md#gae2a49b36cae2e17fc665a3bd844f50b4)
- [gpio_port_get](../hardware/P266_GPIO公共接口.md#ga7c7a53371834c7646dc7f41ca0bb7921)
- [gpio_port_set_masked_raw](../hardware/P266_GPIO公共接口.md#ga9e7b50d720fda362941acc1e3b3b2922)
- [gpio_port_set_masked](../hardware/P266_GPIO公共接口.md#ga0c5ddbec7eb194ffed6cf12ae235ae04)
- [gpio_port_set_bits_raw](../hardware/P266_GPIO公共接口.md#ga18e6ca0df95566fecc0633efb04a075a)
- [gpio_port_set_bits](../hardware/P266_GPIO公共接口.md#gae450ff904686aa4b8fd81bc0dbbafdb5)
- [gpio_port_clear_bits_raw](../hardware/P266_GPIO公共接口.md#ga9d2c9daeec7ce127fc786ead566ad27f)
- [gpio_port_clear_bits](../hardware/P266_GPIO公共接口.md#ga9318c349663568f1fb9400b9458765dc)
- [gpio_port_toggle_bits](../hardware/P266_GPIO公共接口.md#ga82977d8706fb9f464db455bd0e9ac2e4)
- [gpio_port_set_clr_bits_raw](../hardware/P266_GPIO公共接口.md#ga1a06f729e76d39937d0572b6c531e038)
- [gpio_port_set_clr_bits](../hardware/P266_GPIO公共接口.md#ga45172f2b1bb09e8f3c89fa951cdefc14)
- [gpio_pin_get_raw](../hardware/P266_GPIO公共接口.md#ga635975f1df6157c7e8a6c67bac55fbc0)
- [gpio_pin_get](../hardware/P266_GPIO公共接口.md#ga496cd45fd6a2826c75d70c71f967234b)
- [gpio_pin_get_dt](../hardware/P266_GPIO公共接口.md#gaabeb2d0d98856c7ff78be36651d6bbc1)
- [gpio_pin_set_raw](../hardware/P266_GPIO公共接口.md#ga08824e05ea87c4ad2e48edaa13aad30a)
- [gpio_pin_set](../hardware/P266_GPIO公共接口.md#gadac09ef40fc1ba5d8bb40965efde0fda)
- [gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)
- [gpio_pin_toggle](../hardware/P266_GPIO公共接口.md#gaa761788e22a185db227dce7c24915154)
- [gpio_pin_toggle_dt](../hardware/P266_GPIO公共接口.md#ga3272e866489da6c2e12c48f803c59e81)
- [gpio_init_callback](../hardware/P266_GPIO公共接口.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)
- [gpio_add_callback](../hardware/P266_GPIO公共接口.md#ga05fd15af20386d69f9332354285b0cca)
- [gpio_add_callback_dt](../hardware/P266_GPIO公共接口.md#ga54845eb95bc9636c3e6ff285300b6979)
- [gpio_remove_callback](../hardware/P266_GPIO公共接口.md#gac1e94ba8faac79f469447e9b5d2f8c06)
- [gpio_remove_callback_dt](../hardware/P266_GPIO公共接口.md#ga2c9f8fee2addfc0aeeeeb011d534f304)
- [gpio_get_pending_int](../hardware/P266_GPIO公共接口.md#ga3f9e45de172a27f49c31a072c0c241e1)

---

[上一章](P001_GPIO驱动头文件参考.md) · [返回大纲](大纲.md)
