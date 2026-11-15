---
id: learning.zephyr-docs.uart-driver-reference.page-2
title: UART驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2uart_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_UART驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2uart_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_UART驱动头文件参考.md)和[公共API](../hardware/P330_UART公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00036"></a>
<a id="foldopen00050"></a>
<a id="foldopen00080"></a>
<a id="foldopen00089"></a>
<a id="foldopen00097"></a>
<a id="foldopen00112"></a>
<a id="foldopen00122"></a>
<a id="foldopen00201"></a>
<a id="foldopen00256"></a>
<a id="foldopen00269"></a>
<a id="foldopen00279"></a>
<a id="foldopen00285"></a>
<a id="foldopen00293"></a>
<a id="foldopen00297"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__uart__async_html_ga00b7c98a4da3ea3675d0a40c5dacb136"></a>
<a id="agroup__uart__async_html_ga12d91846133351a85fa471fa90f2a0fd"></a>
<a id="agroup__uart__async_html_ga3970fe2818e214b0814ea8b73a816a6a"></a>
<a id="agroup__uart__async_html_ga778bcfc30be853c8d320f295b34c17c0"></a>
<a id="agroup__uart__async_html_ga902e18c2a727ed2988e1b6caa6a444b8"></a>
<a id="agroup__uart__async_html_gaa8a26d3ea685fb98030ea03613be6280"></a>
<a id="agroup__uart__async_html_gab0ea611cd072fa459a6f1780ce62c9e3"></a>
<a id="agroup__uart__async_html_gad33e627ed8729409b14e92453e53459c"></a>
<a id="agroup__uart__async_html_gaf0c9513cbafa36d86b4c83f2b6a03dcd"></a>
<a id="agroup__uart__async_html_gaf99f32ce2e2d9beb32a2f2e5a26320dc"></a>
<a id="agroup__uart__async_html_gafd4753bee51b230091a3c6ddb26ea734"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203"></a>
<a id="agroup__uart__async_html_ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48"></a>
<a id="agroup__uart__interface_html_ga02552532e171e789efc1b000917a9be0"></a>
<a id="agroup__uart__interface_html_ga22ea20fd8e07153b3b71cc9416f5462f"></a>
<a id="agroup__uart__interface_html_ga81dfc5f2134de8e4acb5f063512cf703"></a>
<a id="agroup__uart__interface_html_ga8e2f1b4a8d60d7a6c24835d1b26f99e8"></a>
<a id="agroup__uart__interface_html_gaa0b75777b879af10543f7e8f463ff9a2"></a>
<a id="agroup__uart__interface_html_gaa8683398e5d709b513509d08841ed51b"></a>
<a id="agroup__uart__interface_html_gab039414b41145dc8d31349836da91263"></a>
<a id="agroup__uart__interface_html_gab2ab6aacb6e3c43bb26d4274157e5711"></a>
<a id="agroup__uart__interface_html_gab9f7de744a68a311330576d7da02c44a"></a>
<a id="agroup__uart__interface_html_gadeba6c5485e01dfc1c8a6e1c21668a88"></a>
<a id="agroup__uart__interface_html_gafc1aecb863e2456d73b78a49fcbad72e"></a>
<a id="agroup__uart__interface_html_gafda8a550284a54c8e1d6b6638de978e5"></a>
<a id="agroup__uart__interface_html_gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23"></a>
<a id="agroup__uart__interface_html_gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d"></a>
<a id="agroup__uart__interface_html_gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b"></a>
<a id="agroup__uart__interface_html_gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97"></a>
<a id="agroup__uart__interface_html_gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c"></a>
<a id="agroup__uart__interface_html_gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f"></a>
<a id="agroup__uart__interface_html_gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973"></a>
<a id="agroup__uart__interface_html_gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c"></a>
<a id="agroup__uart__interface_html_gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86"></a>
<a id="agroup__uart__interface_html_ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca"></a>
<a id="agroup__uart__interface_html_ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d"></a>
<a id="agroup__uart__interface_html_ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed"></a>
<a id="agroup__uart__interface_html_ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c"></a>
<a id="agroup__uart__interface_html_ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba"></a>
<a id="agroup__uart__interface_html_ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27"></a>
<a id="agroup__uart__interface_html_ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97"></a>
<a id="agroup__uart__interface_html_ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913"></a>
<a id="agroup__uart__interface_html_ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4"></a>
<a id="agroup__uart__interface_html_ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786"></a>
<a id="agroup__uart__interface_html_ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b"></a>
<a id="agroup__uart__interface_html_ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad"></a>
<a id="agroup__uart__interface_html_ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af"></a>
<a id="agroup__uart__interface_html_ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58"></a>
<a id="agroup__uart__interface_html_ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6"></a>
<a id="agroup__uart__interrupt_html_ga20cf50f53fb9e09e760c6499fd156ff2"></a>
<a id="agroup__uart__interrupt_html_ga4a3c25dad2290f1f40e4b847e3b83f64"></a>
<a id="agroup__uart__interrupt_html_ga4ec3ae3974da2b3ab94ae7b835d17bad"></a>
<a id="agroup__uart__interrupt_html_ga5e126b5f19549eb7f5b785b98ebe7638"></a>
<a id="agroup__uart__interrupt_html_ga5f7af3f7f0d9155349ea3b4fad78956c"></a>
<a id="agroup__uart__interrupt_html_ga7c24daae3326bc2959ea13a2be79969f"></a>
<a id="agroup__uart__interrupt_html_ga917935a13bf6a5d1e32ef34339e96455"></a>
<a id="agroup__uart__interrupt_html_ga9cbd6e33dce6a5b06233cf10077e19cc"></a>
<a id="agroup__uart__interrupt_html_gaa759d7935fdd9ab6ca0761f161389a29"></a>
<a id="agroup__uart__interrupt_html_gaa89f58818d8428ad6a11abf692c54c0d"></a>
<a id="agroup__uart__interrupt_html_gaaf8a88361807e204f7227fbd1d0e75b2"></a>
<a id="agroup__uart__interrupt_html_gab10942076ac47ecff29e924098049398"></a>
<a id="agroup__uart__interrupt_html_gacd8c2978e0f1316dd79bb42baad1c5a7"></a>
<a id="agroup__uart__interrupt_html_gad04073b1b8e3de13b43ae1194561377b"></a>
<a id="agroup__uart__interrupt_html_gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>
<a id="agroup__uart__interrupt_html_gaf469966a56d1fc9f50108201597ee0a0"></a>
<a id="agroup__uart__interrupt_html_gaf8a5bc26cd7c32e7bc6516c6f873c45a"></a>
<a id="agroup__uart__interrupt_html_gafe42e4719eada7e25904bc9ebfe87791"></a>
<a id="agroup__uart__polling_html_ga06ba27ba772a7a18462b8cdbc7f9353c"></a>
<a id="agroup__uart__polling_html_ga8faa3f58b9098c97e288e9c5f3367fd9"></a>
<a id="agroup__uart__polling_html_gaad39c1358019bfdcb919da7982743553"></a>
<a id="agroup__uart__polling_html_gae81ac8cc976a20d774cfbda09e9c983d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructuart__config_html"></a>
<a id="astructuart__config_html_a7b98cd63c531110dc3dc99e94db73642"></a>
<a id="astructuart__config_html_a9371728729252797880de052aae01089"></a>
<a id="astructuart__config_html_a93ee24cf6669fb4cfece78a53d3ec6c5"></a>
<a id="astructuart__config_html_ab532159a689e8f38c2465ce2d1fef354"></a>
<a id="astructuart__config_html_af259c5efab532920b5cce7ae57f6af5e"></a>
<a id="astructuart__event__rx__buf_html"></a>
<a id="astructuart__event__rx__buf_html_a2547c84b742f454cfedf1de6d433297b"></a>
<a id="astructuart__event__rx__stop_html"></a>
<a id="astructuart__event__rx__stop_html_a1b361c8b7e17d1304a475235e734db48"></a>
<a id="astructuart__event__rx__stop_html_a96fbae85208d9b3ea0382e7e236a932d"></a>
<a id="astructuart__event__rx_html"></a>
<a id="astructuart__event__rx_html_a2d9dfa9d9b25ff976cf2e937c72eb245"></a>
<a id="astructuart__event__rx_html_a96414b96e63503336f8cf0d2249cd3bd"></a>
<a id="astructuart__event__rx_html_aa483e719298c30b9f5e6c57d3d161281"></a>
<a id="astructuart__event__tx_html"></a>
<a id="astructuart__event__tx_html_a314a676a4050b2438b6f41485656bdbd"></a>
<a id="astructuart__event__tx_html_a7d844b2c0833d24accf82d58ee3408ff"></a>
<a id="astructuart__event_html"></a>
<a id="astructuart__event_html_a07e3eebb7642ab52c73baba514704c69"></a>
<a id="astructuart__event_html_a2fb82a30e414a74943067cd0784f4b44"></a>
<a id="auart__internal_8h_html"></a>
<a id="aunionuart__event_1_1uart__event__data_html"></a>
<a id="aunionuart__event_1_1uart__event__data_html_a79fb6b799d5574c6aa38a211e020035f"></a>
<a id="aunionuart__event_1_1uart__event__data_html_aad7488a2a3d91cea0ea874a08d7b88f6"></a>
<a id="aunionuart__event_1_1uart__event__data_html_ac03cdaeccba5f693337fa19299101863"></a>
<a id="aunionuart__event_1_1uart__event__data_html_afac00624290b8fe5cf7b59516567b972"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018-2019 Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2015 Wind River Systems, Inc.
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_UART_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_DRIVERS_UART_H_
<a id="l00016"></a>
<a id="l00026"></a>
<a id="l00027"></a>#include &lt;stddef.h&gt;
<a id="l00028"></a>
<a id="l00029"></a>#include &lt;zephyr/device.h&gt;
<a id="l00030"></a>
<a id="l00031"></a>#ifdef __cplusplus
<a id="l00032"></a>extern "C" {
<a id="l00033"></a>#endif
<a id="l00034"></a>
<a id="l00036"></a>enum uart_line_ctrl {
<a id="l00037"></a>        UART_LINE_CTRL_BAUD_RATE = BIT(0),
<a id="l00038"></a>        UART_LINE_CTRL_RTS = BIT(1),
<a id="l00039"></a>        UART_LINE_CTRL_DTR = BIT(2),
<a id="l00040"></a>        UART_LINE_CTRL_DCD = BIT(3),
<a id="l00041"></a>        UART_LINE_CTRL_DSR = BIT(4),
<a id="l00042"></a>};
<a id="l00043"></a>
<a id="l00050"></a>enum uart_rx_stop_reason {
<a id="l00052"></a>        UART_ERROR_OVERRUN = (1 &lt;&lt; 0),
<a id="l00054"></a>        UART_ERROR_PARITY  = (1 &lt;&lt; 1),
<a id="l00056"></a>        UART_ERROR_FRAMING = (1 &lt;&lt; 2),
<a id="l00064"></a>        UART_BREAK = (1 &lt;&lt; 3),
<a id="l00074"></a>        UART_ERROR_COLLISION = (1 &lt;&lt; 4),
<a id="l00076"></a>        UART_ERROR_NOISE = (1 &lt;&lt; 5),
<a id="l00077"></a>};
<a id="l00078"></a>
<a id="l00080"></a>enum uart_config_parity {
<a id="l00081"></a>        UART_CFG_PARITY_NONE,
<a id="l00082"></a>        UART_CFG_PARITY_ODD,
<a id="l00083"></a>        UART_CFG_PARITY_EVEN,
<a id="l00084"></a>        UART_CFG_PARITY_MARK,
<a id="l00085"></a>        UART_CFG_PARITY_SPACE,
<a id="l00086"></a>};
<a id="l00087"></a>
<a id="l00089"></a>enum uart_config_stop_bits {
<a id="l00090"></a>        UART_CFG_STOP_BITS_0_5,
<a id="l00091"></a>        UART_CFG_STOP_BITS_1,
<a id="l00092"></a>        UART_CFG_STOP_BITS_1_5,
<a id="l00093"></a>        UART_CFG_STOP_BITS_2,
<a id="l00094"></a>};
<a id="l00095"></a>
<a id="l00097"></a>enum uart_config_data_bits {
<a id="l00098"></a>        UART_CFG_DATA_BITS_5,
<a id="l00099"></a>        UART_CFG_DATA_BITS_6,
<a id="l00100"></a>        UART_CFG_DATA_BITS_7,
<a id="l00101"></a>        UART_CFG_DATA_BITS_8,
<a id="l00102"></a>        UART_CFG_DATA_BITS_9,
<a id="l00103"></a>};
<a id="l00104"></a>
<a id="l00112"></a>enum uart_config_flow_control {
<a id="l00113"></a>        UART_CFG_FLOW_CTRL_NONE,
<a id="l00114"></a>        UART_CFG_FLOW_CTRL_RTS_CTS,
<a id="l00115"></a>        UART_CFG_FLOW_CTRL_DTR_DSR,
<a id="l00116"></a>        UART_CFG_FLOW_CTRL_RS485,
<a id="l00117"></a>};
<a id="l00118"></a>
<a id="l00122"></a>struct uart_config {
<a id="l00123"></a>        uint32_t baudrate;
<a id="l00124"></a>        uint8_t parity;
<a id="l00125"></a>        uint8_t stop_bits;
<a id="l00126"></a>        uint8_t data_bits;
<a id="l00127"></a>        uint8_t flow_ctrl;
<a id="l00128"></a>};
<a id="l00129"></a>
<a id="l00134"></a>
<a id="l00142"></a>typedef void (*uart_irq_callback_user_data_t)(const struct device *dev,
<a id="l00143"></a>                                              void *user_data);
<a id="l00144"></a>
<a id="l00153"></a>
<a id="l00201"></a>enum uart_event_type {
<a id="l00203"></a>        UART_TX_DONE,
<a id="l00211"></a>        UART_TX_ABORTED,
<a id="l00222"></a>        UART_RX_RDY,
<a id="l00234"></a>        UART_RX_BUF_REQUEST,
<a id="l00238"></a>        UART_RX_BUF_RELEASED,
<a id="l00246"></a>        UART_RX_DISABLED,
<a id="l00252"></a>        UART_RX_STOPPED,
<a id="l00253"></a>};
<a id="l00254"></a>
<a id="l00256"></a>struct uart_event_tx {
<a id="l00258"></a>        const uint8_t *buf;
<a id="l00260"></a>        size_t len;
<a id="l00261"></a>};
<a id="l00262"></a>
<a id="l00269"></a>struct uart_event_rx {
<a id="l00271"></a>        uint8_t *buf;
<a id="l00273"></a>        size_t offset;
<a id="l00275"></a>        size_t len;
<a id="l00276"></a>};
<a id="l00277"></a>
<a id="l00279"></a>struct uart_event_rx_buf {
<a id="l00281"></a>        uint8_t *buf;
<a id="l00282"></a>};
<a id="l00283"></a>
<a id="l00285"></a>struct uart_event_rx_stop {
<a id="l00287"></a>        enum uart_rx_stop_reason reason;
<a id="l00289"></a>        struct uart_event_rx data;
<a id="l00290"></a>};
<a id="l00291"></a>
<a id="l00293"></a>struct uart_event {
<a id="l00295"></a>        enum uart_event_type type;
<a id="l00297"></a>        union uart_event_data {
<a id="l00299"></a>                struct uart_event_tx tx;
<a id="l00301"></a>                struct uart_event_rx rx;
<a id="l00303"></a>                struct uart_event_rx_buf rx_buf;
<a id="l00305"></a>                struct uart_event_rx_stop rx_stop;
<a id="l00306"></a>        } data;
<a id="l00307"></a>};
<a id="l00308"></a>
<a id="l00317"></a>typedef void (*uart_callback_t)(const struct device *dev,
<a id="l00318"></a>                                struct uart_event *evt, void *user_data);
<a id="l00319"></a>
<a id="l00323"></a>
<a id="l00333"></a>__syscall int uart_err_check(const struct device *dev);
<a id="l00334"></a>
<a id="l00339"></a>
<a id="l00358"></a>__syscall int uart_poll_in(const struct device *dev, unsigned char *p_char);
<a id="l00359"></a>
<a id="l00379"></a>__syscall int uart_poll_in_u16(const struct device *dev, uint16_t *p_u16);
<a id="l00380"></a>
<a id="l00396"></a>__syscall void uart_poll_out(const struct device *dev,
<a id="l00397"></a>                             unsigned char out_char);
<a id="l00398"></a>
<a id="l00413"></a>__syscall void uart_poll_out_u16(const struct device *dev, uint16_t out_u16);
<a id="l00414"></a>
<a id="l00418"></a>
<a id="l00432"></a>__syscall int uart_configure(const struct device *dev,
<a id="l00433"></a>                             const struct uart_config *cfg);
<a id="l00434"></a>
<a id="l00448"></a>__syscall int uart_config_get(const struct device *dev,
<a id="l00449"></a>                              struct uart_config *cfg);
<a id="l00450"></a>
<a id="l00455"></a>
<a id="l00476"></a>static inline int uart_fifo_fill(const struct device *dev, const uint8_t *tx_data, int size);
<a id="l00477"></a>
<a id="l00498"></a>static inline int uart_fifo_fill_u16(const struct device *dev, const uint16_t *tx_data, int size);
<a id="l00499"></a>
<a id="l00521"></a>static inline int uart_fifo_read(const struct device *dev, uint8_t *rx_data, const int size);
<a id="l00522"></a>
<a id="l00544"></a>static inline int uart_fifo_read_u16(const struct device *dev, uint16_t *rx_data, const int size);
<a id="l00545"></a>
<a id="l00551"></a>__syscall void uart_irq_tx_enable(const struct device *dev);
<a id="l00552"></a>
<a id="l00558"></a>__syscall void uart_irq_tx_disable(const struct device *dev);
<a id="l00559"></a>
<a id="l00578"></a>static inline int uart_irq_tx_ready(const struct device *dev);
<a id="l00579"></a>
<a id="l00585"></a>__syscall void uart_irq_rx_enable(const struct device *dev);
<a id="l00586"></a>
<a id="l00592"></a>__syscall void uart_irq_rx_disable(const struct device *dev);
<a id="l00593"></a>
<a id="l00613"></a>static inline int uart_irq_tx_complete(const struct device *dev);
<a id="l00614"></a>
<a id="l00635"></a>static inline int uart_irq_rx_ready(const struct device *dev);
<a id="l00636"></a>
<a id="l00642"></a>__syscall void uart_irq_err_enable(const struct device *dev);
<a id="l00643"></a>
<a id="l00649"></a>__syscall void uart_irq_err_disable(const struct device *dev);
<a id="l00650"></a>
<a id="l00666"></a>static inline int uart_irq_is_pending(const struct device *dev);
<a id="l00667"></a>
<a id="l00689"></a>static inline void uart_irq_update(const struct device *dev);
<a id="l00690"></a>
<a id="l00706"></a>static inline int uart_irq_callback_user_data_set(const struct device *dev,
<a id="l00707"></a>                                                  uart_irq_callback_user_data_t cb,
<a id="l00708"></a>                                                  void *user_data);
<a id="l00709"></a>
<a id="l00723"></a>static inline int uart_irq_callback_set(const struct device *dev,
<a id="l00724"></a>                                         uart_irq_callback_user_data_t cb);
<a id="l00725"></a>
<a id="l00729"></a>
<a id="l00734"></a>
<a id="l00750"></a>static inline int uart_callback_set(const struct device *dev,
<a id="l00751"></a>                                    uart_callback_t callback,
<a id="l00752"></a>                                    void *user_data);
<a id="l00753"></a>
<a id="l00770"></a>__syscall int uart_tx(const struct device *dev, const uint8_t *buf,
<a id="l00771"></a>                      size_t len,
<a id="l00772"></a>                      int32_t timeout);
<a id="l00773"></a>
<a id="l00790"></a>__syscall int uart_tx_u16(const struct device *dev, const uint16_t *buf,
<a id="l00791"></a>                          size_t len, int32_t timeout);
<a id="l00792"></a>
<a id="l00804"></a>__syscall int uart_tx_abort(const struct device *dev);
<a id="l00805"></a>
<a id="l00825"></a>__syscall int uart_rx_enable(const struct device *dev, uint8_t *buf,
<a id="l00826"></a>                             size_t len,
<a id="l00827"></a>                             int32_t timeout);
<a id="l00828"></a>
<a id="l00848"></a>__syscall int uart_rx_enable_u16(const struct device *dev, uint16_t *buf,
<a id="l00849"></a>                                 size_t len, int32_t timeout);
<a id="l00850"></a>
<a id="l00870"></a>static inline int uart_rx_buf_rsp(const struct device *dev, uint8_t *buf,
<a id="l00871"></a>                                  size_t len);
<a id="l00872"></a>
<a id="l00893"></a>static inline int uart_rx_buf_rsp_u16(const struct device *dev, uint16_t *buf,
<a id="l00894"></a>                                      size_t len);
<a id="l00895"></a>
<a id="l00910"></a>__syscall int uart_rx_disable(const struct device *dev);
<a id="l00911"></a>
<a id="l00915"></a>
<a id="l00927"></a>__syscall int uart_line_ctrl_set(const struct device *dev,
<a id="l00928"></a>                                 uint32_t ctrl, uint32_t val);
<a id="l00929"></a>
<a id="l00941"></a>__syscall int uart_line_ctrl_get(const struct device *dev, uint32_t ctrl,
<a id="l00942"></a>                                 uint32_t *val);
<a id="l00943"></a>
<a id="l00958"></a>__syscall int uart_drv_cmd(const struct device *dev, uint32_t cmd, uint32_t p);
<a id="l00959"></a>
<a id="l00960"></a>#ifdef __cplusplus
<a id="l00961"></a>}
<a id="l00962"></a>#endif
<a id="l00963"></a>
<a id="l00967"></a>
<a id="l00968"></a>#include &lt;zephyr/drivers/uart/uart_internal.h&gt;
<a id="l00969"></a>#include &lt;zephyr/syscalls/uart.h&gt;
<a id="l00970"></a>
<a id="l00971"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_UART_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2018-2019 Nordic Semiconductor ASA；Copyright (c) 2015 Wind River Systems, Inc.；Apache-2.0许可证原文保留。

2. 结束UART驱动主头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_UART_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API与宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `cmd`

```c
static void cmd(uint32_t command)
```

由协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

定义位置（Definition）：ft8xx_reference_api.h:153。

符号定位：[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

### `BIT`

```c
#define BIT(n)
```

将第n位设为1的无符号整数；在汇编语言中为有符号数。

定义位置（Definition）：util_macro.h:44。

符号定位：[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

### `uart_callback_t`

```c
void(* uart_callback_t)(const struct device *dev, struct uart_event *evt, void *user_data)
```

定义供uart_callback_set()使用的应用程序回调函数签名。

定义位置（Definition）：uart.h:317。

符号定位：[uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)。

### `uart_rx_enable_u16`

```c
int uart_rx_enable_u16(const struct device *dev, uint16_t *buf, size_t len, int32_t timeout)
```

开始通过UART接收宽数据。

符号定位：[uart_rx_enable_u16](../hardware/P334_UART异步接口.md#ga12d91846133351a85fa471fa90f2a0fd)。

### `uart_rx_buf_rsp`

```c
static int uart_rx_buf_rsp(const struct device *dev, uint8_t *buf, size_t len)
```

响应UART_RX_BUF_REQUEST事件，提供接收缓冲区。

符号定位：[uart_rx_buf_rsp](../hardware/P334_UART异步接口.md#ga3970fe2818e214b0814ea8b73a816a6a)。

### `uart_rx_buf_rsp_u16`

```c
static int uart_rx_buf_rsp_u16(const struct device *dev, uint16_t *buf, size_t len)
```

响应UART_RX_BUF_REQUEST事件，提供宽数据接收缓冲区。

符号定位：[uart_rx_buf_rsp_u16](../hardware/P334_UART异步接口.md#ga778bcfc30be853c8d320f295b34c17c0)。

### `uart_rx_enable`

```c
int uart_rx_enable(const struct device *dev, uint8_t *buf, size_t len, int32_t timeout)
```

开始通过UART接收数据。

符号定位：[uart_rx_enable](../hardware/P334_UART异步接口.md#ga902e18c2a727ed2988e1b6caa6a444b8)。

### `uart_tx_abort`

```c
int uart_tx_abort(const struct device *dev)
```

中止当前TX传输（Abort）。

符号定位：[uart_tx_abort](../hardware/P334_UART异步接口.md#gaa8a26d3ea685fb98030ea03613be6280)。

### `uart_tx_u16`

```c
int uart_tx_u16(const struct device *dev, const uint16_t *buf, size_t len, int32_t timeout)
```

通过UART发送缓冲区中指定数量的数据项。

符号定位：[uart_tx_u16](../hardware/P334_UART异步接口.md#gab0ea611cd072fa459a6f1780ce62c9e3)。

### `uart_callback_set`

```c
static int uart_callback_set(const struct device *dev, uart_callback_t callback, void *user_data)
```

设置事件处理函数（Event Handler）。

符号定位：[uart_callback_set](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)。

### `uart_event_type`

```c
uart_event_type
```

UART_ASYNC_API中传给回调函数的事件类型（Event Types）。

定义位置（Definition）：uart.h:201。

符号定位：[uart_event_type](../hardware/P334_UART异步接口.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)。

### `uart_tx`

```c
int uart_tx(const struct device *dev, const uint8_t *buf, size_t len, int32_t timeout)
```

通过UART发送缓冲区中指定数量的字节。

符号定位：[uart_tx](../hardware/P334_UART异步接口.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)。

### `uart_rx_disable`

```c
int uart_rx_disable(const struct device *dev)
```

禁用RX。

符号定位：[uart_rx_disable](../hardware/P334_UART异步接口.md#gafd4753bee51b230091a3c6ddb26ea734)。

### `UART_RX_STOPPED`

```c
@ UART_RX_STOPPED
```

接收因外部事件停止。

定义位置（Definition）：uart.h:252。

符号定位：[UART_RX_STOPPED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)。

### `UART_TX_ABORTED`

```c
@ UART_TX_ABORTED
```

发送因超时或调用uart_tx_abort而中止。

定义位置（Definition）：uart.h:211。

符号定位：[UART_TX_ABORTED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)。

### `UART_RX_BUF_REQUEST`

```c
@ UART_RX_BUF_REQUEST
```

驱动请求下一个缓冲区，以便连续接收。

定义位置（Definition）：uart.h:234。

符号定位：[UART_RX_BUF_REQUEST](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)。

### `UART_TX_DONE`

```c
@ UART_TX_DONE
```

整个发送缓冲区均已传输。

定义位置（Definition）：uart.h:203。

符号定位：[UART_TX_DONE](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)。

### `UART_RX_RDY`

```c
@ UART_RX_RDY
```

接收到的数据已就绪，可以处理。

定义位置（Definition）：uart.h:222。

符号定位：[UART_RX_RDY](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)。

### `UART_RX_DISABLED`

```c
@ UART_RX_DISABLED
```

接收已禁用，可以再次使能。

定义位置（Definition）：uart.h:246。

符号定位：[UART_RX_DISABLED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)。

### `UART_RX_BUF_RELEASED`

```c
@ UART_RX_BUF_RELEASED
```

UART驱动不再使用此缓冲区。

定义位置（Definition）：uart.h:238。

符号定位：[UART_RX_BUF_RELEASED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)。

### `uart_line_ctrl`

```c
uart_line_ctrl
```

线路控制信号（Line Control Signals）。

定义位置（Definition）：uart.h:36。

符号定位：[uart_line_ctrl](../hardware/P330_UART公共接口.md#ga02552532e171e789efc1b000917a9be0)。

### `uart_err_check`

```c
int uart_err_check(const struct device *dev)
```

检查是否检测到错误。

符号定位：[uart_err_check](../hardware/P330_UART公共接口.md#ga22ea20fd8e07153b3b71cc9416f5462f)。

### `uart_config_get`

```c
int uart_config_get(const struct device *dev, struct uart_config *cfg)
```

取得UART配置。

符号定位：[uart_config_get](../hardware/P330_UART公共接口.md#ga81dfc5f2134de8e4acb5f063512cf703)。

### `uart_config_flow_control`

```c
uart_config_flow_control
```

硬件流控制（Hardware Flow Control）选项。

定义位置（Definition）：uart.h:112。

符号定位：[uart_config_flow_control](../hardware/P330_UART公共接口.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)。

### `uart_configure`

```c
int uart_configure(const struct device *dev, const struct uart_config *cfg)
```

设置UART配置。

符号定位：[uart_configure](../hardware/P330_UART公共接口.md#gaa0b75777b879af10543f7e8f463ff9a2)。

### `uart_drv_cmd`

```c
int uart_drv_cmd(const struct device *dev, uint32_t cmd, uint32_t p)
```

向驱动发送额外命令（Driver Command）。

符号定位：[uart_drv_cmd](../hardware/P330_UART公共接口.md#gaa8683398e5d709b513509d08841ed51b)。

### `uart_line_ctrl_set`

```c
int uart_line_ctrl_set(const struct device *dev, uint32_t ctrl, uint32_t val)
```

设置UART线路控制。

符号定位：[uart_line_ctrl_set](../hardware/P330_UART公共接口.md#gab039414b41145dc8d31349836da91263)。

### `uart_config_parity`

```c
uart_config_parity
```

奇偶校验模式（Parity Modes）。

定义位置（Definition）：uart.h:80。

符号定位：[uart_config_parity](../hardware/P330_UART公共接口.md#gab2ab6aacb6e3c43bb26d4274157e5711)。

### `uart_config_data_bits`

```c
uart_config_data_bits
```

数据位数量（Number of Data Bits）。

定义位置（Definition）：uart.h:97。

符号定位：[uart_config_data_bits](../hardware/P330_UART公共接口.md#gab9f7de744a68a311330576d7da02c44a)。

### `uart_rx_stop_reason`

```c
uart_rx_stop_reason
```

接收停止原因（Reception Stop Reasons）。

定义位置（Definition）：uart.h:50。

符号定位：[uart_rx_stop_reason](../hardware/P330_UART公共接口.md#gadeba6c5485e01dfc1c8a6e1c21668a88)。

### `uart_config_stop_bits`

```c
uart_config_stop_bits
```

停止位数量（Number of Stop Bits）。

定义位置（Definition）：uart.h:89。

符号定位：[uart_config_stop_bits](../hardware/P330_UART公共接口.md#gafc1aecb863e2456d73b78a49fcbad72e)。

### `uart_line_ctrl_get`

```c
int uart_line_ctrl_get(const struct device *dev, uint32_t ctrl, uint32_t *val)
```

读取UART线路控制。

符号定位：[uart_line_ctrl_get](../hardware/P330_UART公共接口.md#gafda8a550284a54c8e1d6b6638de978e5)。

### `UART_LINE_CTRL_DTR`

```c
@ UART_LINE_CTRL_DTR
```

数据终端就绪（Data Terminal Ready，DTR）。

定义位置（Definition）：uart.h:39。

符号定位：[UART_LINE_CTRL_DTR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)。

### `UART_LINE_CTRL_RTS`

```c
@ UART_LINE_CTRL_RTS
```

请求发送（Request To Send，RTS）。

定义位置（Definition）：uart.h:38。

符号定位：[UART_LINE_CTRL_RTS](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)。

### `UART_LINE_CTRL_BAUD_RATE`

```c
@ UART_LINE_CTRL_BAUD_RATE
```

波特率（Baud Rate）。

定义位置（Definition）：uart.h:37。

符号定位：[UART_LINE_CTRL_BAUD_RATE](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)。

### `UART_LINE_CTRL_DCD`

```c
@ UART_LINE_CTRL_DCD
```

数据载波检测（Data Carrier Detect，DCD）。

定义位置（Definition）：uart.h:40。

符号定位：[UART_LINE_CTRL_DCD](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)。

### `UART_LINE_CTRL_DSR`

```c
@ UART_LINE_CTRL_DSR
```

数据设备就绪（Data Set Ready，DSR）。

定义位置（Definition）：uart.h:41。

符号定位：[UART_LINE_CTRL_DSR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)。

### `UART_CFG_FLOW_CTRL_DTR_DSR`

```c
@ UART_CFG_FLOW_CTRL_DTR_DSR
```

DTR／DSR流控制（Flow Control）。

定义位置（Definition）：uart.h:115。

符号定位：[UART_CFG_FLOW_CTRL_DTR_DSR](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)。

### `UART_CFG_FLOW_CTRL_NONE`

```c
@ UART_CFG_FLOW_CTRL_NONE
```

无流控制。

定义位置（Definition）：uart.h:113。

符号定位：[UART_CFG_FLOW_CTRL_NONE](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)。

### `UART_CFG_FLOW_CTRL_RS485`

```c
@ UART_CFG_FLOW_CTRL_RS485
```

RS-485流控制。

定义位置（Definition）：uart.h:116。

符号定位：[UART_CFG_FLOW_CTRL_RS485](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)。

### `UART_CFG_FLOW_CTRL_RTS_CTS`

```c
@ UART_CFG_FLOW_CTRL_RTS_CTS
```

RTS／CTS流控制。

定义位置（Definition）：uart.h:114。

符号定位：[UART_CFG_FLOW_CTRL_RTS_CTS](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)。

### `UART_CFG_PARITY_MARK`

```c
@ UART_CFG_PARITY_MARK
```

传号校验（Mark Parity，校验位固定为1）。

定义位置（Definition）：uart.h:84。

符号定位：[UART_CFG_PARITY_MARK](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)。

### `UART_CFG_PARITY_NONE`

```c
@ UART_CFG_PARITY_NONE
```

无奇偶校验（No Parity）。

定义位置（Definition）：uart.h:81。

符号定位：[UART_CFG_PARITY_NONE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)。

### `UART_CFG_PARITY_ODD`

```c
@ UART_CFG_PARITY_ODD
```

奇校验（Odd Parity）。

定义位置（Definition）：uart.h:82。

符号定位：[UART_CFG_PARITY_ODD](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)。

### `UART_CFG_PARITY_SPACE`

```c
@ UART_CFG_PARITY_SPACE
```

空号校验（Space Parity，校验位固定为0）。

定义位置（Definition）：uart.h:85。

符号定位：[UART_CFG_PARITY_SPACE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)。

### `UART_CFG_PARITY_EVEN`

```c
@ UART_CFG_PARITY_EVEN
```

偶校验（Even Parity）。

定义位置（Definition）：uart.h:83。

符号定位：[UART_CFG_PARITY_EVEN](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)。

### `UART_CFG_DATA_BITS_5`

```c
@ UART_CFG_DATA_BITS_5
```

5个数据位。

定义位置（Definition）：uart.h:98。

符号定位：[UART_CFG_DATA_BITS_5](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)。

### `UART_CFG_DATA_BITS_8`

```c
@ UART_CFG_DATA_BITS_8
```

8个数据位。

定义位置（Definition）：uart.h:101。

符号定位：[UART_CFG_DATA_BITS_8](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)。

### `UART_CFG_DATA_BITS_7`

```c
@ UART_CFG_DATA_BITS_7
```

7个数据位。

定义位置（Definition）：uart.h:100。

符号定位：[UART_CFG_DATA_BITS_7](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)。

### `UART_CFG_DATA_BITS_6`

```c
@ UART_CFG_DATA_BITS_6
```

6个数据位。

定义位置（Definition）：uart.h:99。

符号定位：[UART_CFG_DATA_BITS_6](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)。

### `UART_CFG_DATA_BITS_9`

```c
@ UART_CFG_DATA_BITS_9
```

9个数据位。

定义位置（Definition）：uart.h:102。

符号定位：[UART_CFG_DATA_BITS_9](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)。

### `UART_ERROR_NOISE`

```c
@ UART_ERROR_NOISE
```

噪声错误（Noise Error）。

定义位置（Definition）：uart.h:76。

符号定位：[UART_ERROR_NOISE](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)。

### `UART_ERROR_OVERRUN`

```c
@ UART_ERROR_OVERRUN
```

溢出错误（Overrun Error）。

定义位置（Definition）：uart.h:52。

符号定位：[UART_ERROR_OVERRUN](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)。

### `UART_BREAK`

```c
@ UART_BREAK
```

断线中断（Break Interrupt）。

定义位置（Definition）：uart.h:64。

符号定位：[UART_BREAK](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)。

### `UART_ERROR_PARITY`

```c
@ UART_ERROR_PARITY
```

奇偶校验错误（Parity Error）。

定义位置（Definition）：uart.h:54。

符号定位：[UART_ERROR_PARITY](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)。

### `UART_ERROR_COLLISION`

```c
@ UART_ERROR_COLLISION
```

冲突错误（Collision Error）。

定义位置（Definition）：uart.h:74。

符号定位：[UART_ERROR_COLLISION](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)。

### `UART_ERROR_FRAMING`

```c
@ UART_ERROR_FRAMING
```

帧格式错误（Framing Error）。

定义位置（Definition）：uart.h:56。

符号定位：[UART_ERROR_FRAMING](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)。

### `UART_CFG_STOP_BITS_1_5`

```c
@ UART_CFG_STOP_BITS_1_5
```

1.5个停止位。

定义位置（Definition）：uart.h:92。

符号定位：[UART_CFG_STOP_BITS_1_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)。

### `UART_CFG_STOP_BITS_0_5`

```c
@ UART_CFG_STOP_BITS_0_5
```

0.5个停止位。

定义位置（Definition）：uart.h:90。

符号定位：[UART_CFG_STOP_BITS_0_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)。

### `UART_CFG_STOP_BITS_1`

```c
@ UART_CFG_STOP_BITS_1
```

1个停止位。

定义位置（Definition）：uart.h:91。

符号定位：[UART_CFG_STOP_BITS_1](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)。

### `UART_CFG_STOP_BITS_2`

```c
@ UART_CFG_STOP_BITS_2
```

2个停止位。

定义位置（Definition）：uart.h:93。

符号定位：[UART_CFG_STOP_BITS_2](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)。

### `uart_irq_update`

```c
static void uart_irq_update(const struct device *dev)
```

在中断服务程序（Interrupt Service Routine，ISR）中开始处理中断。

符号定位：[uart_irq_update](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)。

### `uart_fifo_read_u16`

```c
static int uart_fifo_read_u16(const struct device *dev, uint16_t *rx_data, const int size)
```

从FIFO读取宽数据。

符号定位：[uart_fifo_read_u16](../hardware/P333_UART中断驱动接口.md#ga4a3c25dad2290f1f40e4b847e3b83f64)。

### `uart_irq_rx_enable`

```c
void uart_irq_rx_enable(const struct device *dev)
```

使能RX中断。

符号定位：[uart_irq_rx_enable](../hardware/P333_UART中断驱动接口.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)。

### `uart_irq_tx_ready`

```c
static int uart_irq_tx_ready(const struct device *dev)
```

检查UART发送缓冲区是否能够接受字节。

符号定位：[uart_irq_tx_ready](../hardware/P333_UART中断驱动接口.md#ga5e126b5f19549eb7f5b785b98ebe7638)。

### `uart_irq_callback_set`

```c
static int uart_irq_callback_set(const struct device *dev, uart_irq_callback_user_data_t cb)
```

设置IRQ回调函数指针的旧式接口（Legacy）。

符号定位：[uart_irq_callback_set](../hardware/P333_UART中断驱动接口.md#ga5f7af3f7f0d9155349ea3b4fad78956c)。

### `uart_irq_err_enable`

```c
void uart_irq_err_enable(const struct device *dev)
```

使能错误中断（Error Interrupt）。

符号定位：[uart_irq_err_enable](../hardware/P333_UART中断驱动接口.md#ga7c24daae3326bc2959ea13a2be79969f)。

### `uart_irq_tx_complete`

```c
static int uart_irq_tx_complete(const struct device *dev)
```

检查UART发送模块是否已完成传输。

符号定位：[uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)。

### `uart_irq_tx_enable`

```c
void uart_irq_tx_enable(const struct device *dev)
```

在中断使能寄存器（Interrupt Enable Register，IER）中使能TX中断。

符号定位：[uart_irq_tx_enable](../hardware/P333_UART中断驱动接口.md#ga9cbd6e33dce6a5b06233cf10077e19cc)。

### `uart_irq_rx_disable`

```c
void uart_irq_rx_disable(const struct device *dev)
```

禁用RX中断。

符号定位：[uart_irq_rx_disable](../hardware/P333_UART中断驱动接口.md#gaa759d7935fdd9ab6ca0761f161389a29)。

### `uart_fifo_fill_u16`

```c
static int uart_fifo_fill_u16(const struct device *dev, const uint16_t *tx_data, int size)
```

向FIFO填充宽数据（Wide Data）。

符号定位：[uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)。

### `uart_irq_err_disable`

```c
void uart_irq_err_disable(const struct device *dev)
```

禁用错误中断。

符号定位：[uart_irq_err_disable](../hardware/P333_UART中断驱动接口.md#gaaf8a88361807e204f7227fbd1d0e75b2)。

### `uart_fifo_read`

```c
static int uart_fifo_read(const struct device *dev, uint8_t *rx_data, const int size)
```

从FIFO读取数据。

符号定位：[uart_fifo_read](../hardware/P333_UART中断驱动接口.md#gab10942076ac47ecff29e924098049398)。

### `uart_irq_is_pending`

```c
static int uart_irq_is_pending(const struct device *dev)
```

检查是否存在待处理的中断请求（Interrupt Request，IRQ）。

符号定位：[uart_irq_is_pending](../hardware/P333_UART中断驱动接口.md#gacd8c2978e0f1316dd79bb42baad1c5a7)。

### `uart_irq_rx_ready`

```c
static int uart_irq_rx_ready(const struct device *dev)
```

检查UART接收缓冲区是否已有接收到的字符。

符号定位：[uart_irq_rx_ready](../hardware/P333_UART中断驱动接口.md#gad04073b1b8e3de13b43ae1194561377b)。

### `uart_irq_callback_user_data_t`

```c
void(* uart_irq_callback_user_data_t)(const struct device *dev, void *user_data)
```

定义供uart_irq_callback_user_data_set()使用的应用程序回调函数签名（Callback Function Signature）。

定义位置（Definition）：uart.h:142。

符号定位：[uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)。

### `uart_irq_callback_user_data_set`

```c
static int uart_irq_callback_user_data_set(const struct device *dev, uart_irq_callback_user_data_t cb, void *user_data)
```

设置IRQ回调函数指针。

符号定位：[uart_irq_callback_user_data_set](../hardware/P333_UART中断驱动接口.md#gaf469966a56d1fc9f50108201597ee0a0)。

### `uart_irq_tx_disable`

```c
void uart_irq_tx_disable(const struct device *dev)
```

在IER中禁用TX中断。

符号定位：[uart_irq_tx_disable](../hardware/P333_UART中断驱动接口.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)。

### `uart_fifo_fill`

```c
static int uart_fifo_fill(const struct device *dev, const uint8_t *tx_data, int size)
```

向先进先出队列（First In, First Out，FIFO）填充数据。

符号定位：[uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)。

### `uart_poll_out`

```c
void uart_poll_out(const struct device *dev, unsigned char out_char)
```

向设备写入一个字符作为输出。

符号定位：[uart_poll_out](../hardware/P332_UART轮询接口.md#ga06ba27ba772a7a18462b8cdbc7f9353c)。

### `uart_poll_out_u16`

```c
void uart_poll_out_u16(const struct device *dev, uint16_t out_u16)
```

向设备写入一个16位数据项作为输出。

符号定位：[uart_poll_out_u16](../hardware/P332_UART轮询接口.md#ga8faa3f58b9098c97e288e9c5f3367fd9)。

### `uart_poll_in_u16`

```c
int uart_poll_in_u16(const struct device *dev, uint16_t *p_u16)
```

从设备读取一个16位数据项作为输入。

符号定位：[uart_poll_in_u16](../hardware/P332_UART轮询接口.md#gaad39c1358019bfdcb919da7982743553)。

### `uart_poll_in`

```c
int uart_poll_in(const struct device *dev, unsigned char *p_char)
```

从设备读取一个字符作为输入。

符号定位：[uart_poll_in](../hardware/P332_UART轮询接口.md#gae81ac8cc976a20d774cfbda09e9c983d)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `int32_t`

```c
__INT32_TYPE__ int32_t
```

定义位置（Definition）：stdint.h:74。

符号定位：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

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

### `uart_config`

UART控制器（Controller）配置结构。

定义位置（Definition）：uart.h:122。

符号定位：[uart_config](../hardware/P331_UART配置结构.md)。

### `uart_config::stop_bits`

```c
uint8_t stop_bits
```

停止位，使用uart_config_stop_bits。

定义位置（Definition）：uart.h:125。

符号定位：[uart_config::stop_bits](../hardware/P331_UART配置结构.md#a7b98cd63c531110dc3dc99e94db73642)。

### `uart_config::parity`

```c
uint8_t parity
```

奇偶校验位，使用uart_config_parity。

定义位置（Definition）：uart.h:124。

符号定位：[uart_config::parity](../hardware/P331_UART配置结构.md#a9371728729252797880de052aae01089)。

### `uart_config::data_bits`

```c
uint8_t data_bits
```

数据位，使用uart_config_data_bits。

定义位置（Definition）：uart.h:126。

符号定位：[uart_config::data_bits](../hardware/P331_UART配置结构.md#a93ee24cf6669fb4cfece78a53d3ec6c5)。

### `uart_config::baudrate`

```c
uint32_t baudrate
```

波特率设置，单位按原文为bps。

定义位置（Definition）：uart.h:123。

符号定位：[uart_config::baudrate](../hardware/P331_UART配置结构.md#ab532159a689e8f38c2465ce2d1fef354)。

### `uart_config::flow_ctrl`

```c
uint8_t flow_ctrl
```

流控制设置，使用uart_config_flow_control。

定义位置（Definition）：uart.h:127。

符号定位：[uart_config::flow_ctrl](../hardware/P331_UART配置结构.md#af259c5efab532920b5cce7ae57f6af5e)。

### `uart_event_rx_buf`

UART接收缓冲区释放（RX Buffer Released）事件数据。

定义位置（Definition）：uart.h:279。

符号定位：[uart_event_rx_buf](../hardware/P337_UART缓冲区释放事件结构.md)。

### `uart_event_rx_buf::buf`

```c
uint8_t * buf
```

指向不再被使用的缓冲区的指针。

定义位置（Definition）：uart.h:281。

符号定位：[uart_event_rx_buf::buf](../hardware/P337_UART缓冲区释放事件结构.md#a2547c84b742f454cfedf1de6d433297b)。

### `uart_event_rx_stop`

UART接收停止（RX Stopped）数据。

定义位置（Definition）：uart.h:285。

符号定位：[uart_event_rx_stop](../hardware/P338_UART接收停止事件结构.md)。

### `uart_event_rx_stop::data`

```c
struct uart_event_rx data
```

最后接收到的数据。

定义位置（Definition）：uart.h:289。

符号定位：[uart_event_rx_stop::data](../hardware/P338_UART接收停止事件结构.md#a1b361c8b7e17d1304a475235e734db48)。

### `uart_event_rx_stop::reason`

```c
enum uart_rx_stop_reason reason
```

接收停止的原因。

定义位置（Definition）：uart.h:287。

符号定位：[uart_event_rx_stop::reason](../hardware/P338_UART接收停止事件结构.md#a96fbae85208d9b3ea0382e7e236a932d)。

### `uart_event_rx`

UART接收（Receive，RX）事件数据。

定义位置（Definition）：uart.h:269。

符号定位：[uart_event_rx](../hardware/P336_UART接收事件结构.md)。

### `uart_event_rx::buf`

```c
uint8_t * buf
```

指向当前缓冲区的指针。

定义位置（Definition）：uart.h:271。

符号定位：[uart_event_rx::buf](../hardware/P336_UART接收事件结构.md#a2d9dfa9d9b25ff976cf2e937c72eb245)。

### `uart_event_rx::len`

```c
size_t len
```

新接收到的字节数。

定义位置（Definition）：uart.h:275。

符号定位：[uart_event_rx::len](../hardware/P336_UART接收事件结构.md#a96414b96e63503336f8cf0d2249cd3bd)。

### `uart_event_rx::offset`

```c
size_t offset
```

当前接收数据在缓冲区内的偏移量（Offset），单位为字节。

定义位置（Definition）：uart.h:273。

符号定位：[uart_event_rx::offset](../hardware/P336_UART接收事件结构.md#aa483e719298c30b9f5e6c57d3d161281)。

### `uart_event_tx`

UART发送（Transmit，TX）事件数据。

定义位置（Definition）：uart.h:256。

符号定位：[uart_event_tx](../hardware/P335_UART发送事件结构.md)。

### `uart_event_tx::buf`

```c
const uint8_t * buf
```

指向当前缓冲区的指针。

定义位置（Definition）：uart.h:258。

符号定位：[uart_event_tx::buf](../hardware/P335_UART发送事件结构.md#a314a676a4050b2438b6f41485656bdbd)。

### `uart_event_tx::len`

```c
size_t len
```

已发送的字节数。

定义位置（Definition）：uart.h:260。

符号定位：[uart_event_tx::len](../hardware/P335_UART发送事件结构.md#a7d844b2c0833d24accf82d58ee3408ff)。

### `uart_event`

包含当前事件（Event）信息的结构。

定义位置（Definition）：uart.h:293。

符号定位：[uart_event](../hardware/P339_UART事件联合结构.md)。

### `uart_event::data`

```c
union uart_event::uart_event_data data
```

事件数据；有效字段由type决定。

符号定位：[uart_event::data](../hardware/P339_UART事件联合结构.md#a07e3eebb7642ab52c73baba514704c69)。

### `uart_event::type`

```c
enum uart_event_type type
```

事件类型。

定义位置（Definition）：uart.h:295。

符号定位：[uart_event::type](../hardware/P339_UART事件联合结构.md#a2fb82a30e414a74943067cd0784f4b44)。

### `uart_internal.h`

UART驱动的内部API（Internal APIs）。

符号定位：[uart_internal.h](P003_UART内部头文件参考.md)。

### `uart_event::uart_event_data`

事件数据（Event Data）。

定义位置（Definition）：uart.h:297。

符号定位：[uart_event::uart_event_data](../hardware/P340_UART事件数据联合体.md)。

### `uart_event::uart_event_data::tx`

```c
struct uart_event_tx tx
```

UART_TX_DONE和UART_TX_ABORTED事件的数据。

定义位置（Definition）：uart.h:299。

符号定位：[uart_event::uart_event_data::tx](../hardware/P340_UART事件数据联合体.md#a79fb6b799d5574c6aa38a211e020035f)。

### `uart_event::uart_event_data::rx_stop`

```c
struct uart_event_rx_stop rx_stop
```

UART_RX_STOPPED事件数据。

定义位置（Definition）：uart.h:305。

符号定位：[uart_event::uart_event_data::rx_stop](../hardware/P340_UART事件数据联合体.md#aad7488a2a3d91cea0ea874a08d7b88f6)。

### `uart_event::uart_event_data::rx_buf`

```c
struct uart_event_rx_buf rx_buf
```

UART_RX_BUF_RELEASED事件数据。

定义位置（Definition）：uart.h:303。

符号定位：[uart_event::uart_event_data::rx_buf](../hardware/P340_UART事件数据联合体.md#ac03cdaeccba5f693337fa19299101863)。

### `uart_event::uart_event_data::rx`

```c
struct uart_event_rx rx
```

UART_RX_RDY事件数据。

定义位置（Definition）：uart.h:301。

符号定位：[uart_event::uart_event_data::rx](../hardware/P340_UART事件数据联合体.md#afac00624290b8fe5cf7b59516567b972)。

## 2.4\_源码跟踪译注

> 译注——公共声明与内部实现：uart.h定义配置、事件与公共接口，在末尾包含uart/uart_internal.h和生成的syscalls/uart.h。内部头文件中的uart_driver_api及z_impl_*／内联包装负责把调用转交给驱动函数表；普通应用仍以公共头文件为入口。官方内部参考页将这些内容列为INTERNAL_HIDDEN，只有文件说明与源码入口，不能把它当成缺失了公开成员说明；完整可见代码在本册内部源码页保留。

> 译注——枚举编码与配置值：UART_LINE_CTRL_*和UART_ERROR_*是位标志（Bit Flags），而数据位、停止位、奇偶校验与流控制枚举采用各自的顺序编码。UART_CFG_DATA_BITS_8不是整数8，不能直接把设备树data-bits数值赋给uart_config.data_bits；应使用对应枚举。uart_config.baudrate按原文字段说明使用bps，实际速率、格式和流控制是否可用取决于驱动及硬件。绑定中的current-speed、hw-flow-control等是初始化配置来源，不等于运行时已成功调用uart_configure。

> 译注——三种传输方式：轮询输入（Polling Input）为非阻塞接口，轮询输出（Polling Output）可能等待发送条件。中断驱动（Interrupt-driven）由IRQ回调处理FIFO，异步API（Asynchronous API）由uart_event回调报告传输进度和完成。三类入口、回调签名与配置条件不同。UART_EXCLUSIVE_API_CALLBACKS在异步与中断接口同时启用时默认使两类回调互斥，具体清除动作由相应驱动落实；不能仅因两组选项都启用就假定同一设备可以同时保留两套回调。

> 译注——中断处理顺序：官方公共约定要求先在ISR调用uart_irq_update，再查询RX／TX就绪、发送完成或挂起状态。当前uart_irq_update返回void，内部包装在驱动有irq_update操作时才调用它，不能写成依赖其整数返回值的判断。TX就绪时应填充FIFO并检查实际写入数量；RX就绪时持续读取，直至返回数量小于请求数量，避免假定中断一定按电平触发。错误返回应单独处理，不能把负errno当作成功计数或简单布尔真值。

> 译注——异步事件与缓冲区：uart_tx／uart_rx_enable返回的是启动结果，完成与数据可用通过事件通知。UART_RX_RDY给出当前缓冲区内从offset开始、长度为len的新数据，不表示缓冲区已释放，同一缓冲区可以出现多次RDY。收到UART_RX_BUF_REQUEST时可提供下一缓冲区；驱动仍在使用的缓冲区不能再次提交，要等UART_RX_BUF_RELEASED后复用。停收或错误可先通知剩余数据，再释放缓冲区，最后报告UART_RX_DISABLED。

> 译注——超时与宽数据单位：异步timeout单位为微秒（Microsecond），TX超时按原约定仅在流控制启用时有效；RX超时是至少收到一个字节后的不活动间隔，没有收到数据时不会单凭该间隔产生RDY。SYS_FOREVER_US禁用超时。带_u16接口以uint16_t容纳宽数据，FIFO与异步传输长度按数据项计；用户态校验也采用len乘sizeof(uint16_t)检查数组范围，不能把len直接当作字节数。公开事件字段的字节措辞按原文保留，宽数据场景仍须核对具体驱动的事件填充。

> 译注——错误与空操作边界：运行时配置、线路控制、驱动命令、FIFO及多数中断状态查询，在对应功能未启用时返回-ENOTSUP；已启用但所检查的操作指针为空时返回-ENOSYS。部分void中断使能／禁用包装在缺少操作时不做任何事，宽数据轮询输出在功能未启用时同样为空操作。poll_out以及异步TX、RX和缓冲区提交包装在已编译分支中直接调用相应操作，不统一执行空指针检查。应按所用入口及设备能力判断，不能把一处检查推广给所有UART API。

> 译注——用户态与回调边界：uart_handlers.c为系统调用核对设备对象／操作权限及输入输出缓冲区可访问范围；这些校验不代表内核内联包装也自动拥有相同检查。回调安装与rx_buf_rsp未提供同类系统调用入口，原注释明确回调安装不允许来自用户态，缓冲区响应用于ISR回调。自定义驱动命令的cmd是UART命令参数；原Doxygen页面将同名符号链接到显示协处理器函数，相关符号提示按原文保留，该交叉引用不意味着UART具有显示命令功能。

> 译注——版本边界：本批核对公共与内部两个头文件、UART系统调用处理、串口Kconfig和公共控制器绑定，共五份官方源码并记录摘要。两份源码浏览页的非注释代码分别与读取的官方原始头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、打开串口、发送数据或操作硬件。

头文件相对定位：[include/zephyr/drivers/uart.h](../../../include/zephyr/drivers/uart.h)，关联实现／接口：[include/zephyr/drivers/uart/uart_internal.h](../../../include/zephyr/drivers/uart/uart_internal.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/uart.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/uart/uart_internal.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、打开串口、收发数据或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_UART驱动头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uart_line_ctrl](../hardware/P330_UART公共接口.md#ga02552532e171e789efc1b000917a9be0)
- [UART_LINE_CTRL_BAUD_RATE](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [UART_LINE_CTRL_RTS](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)
- [UART_LINE_CTRL_DTR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)
- [UART_LINE_CTRL_DCD](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)
- [UART_LINE_CTRL_DSR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)
- [uart_rx_stop_reason](../hardware/P330_UART公共接口.md#gadeba6c5485e01dfc1c8a6e1c21668a88)
- [UART_ERROR_OVERRUN](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)
- [UART_ERROR_PARITY](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)
- [UART_ERROR_FRAMING](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)
- [UART_BREAK](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)
- [UART_ERROR_COLLISION](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)
- [UART_ERROR_NOISE](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)
- [uart_config_parity](../hardware/P330_UART公共接口.md#gab2ab6aacb6e3c43bb26d4274157e5711)
- [UART_CFG_PARITY_NONE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)
- [UART_CFG_PARITY_ODD](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)
- [UART_CFG_PARITY_EVEN](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)
- [UART_CFG_PARITY_MARK](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)
- [UART_CFG_PARITY_SPACE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)
- [uart_config_stop_bits](../hardware/P330_UART公共接口.md#gafc1aecb863e2456d73b78a49fcbad72e)
- [UART_CFG_STOP_BITS_0_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)
- [UART_CFG_STOP_BITS_1](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)
- [UART_CFG_STOP_BITS_1_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)
- [UART_CFG_STOP_BITS_2](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)
- [uart_config_data_bits](../hardware/P330_UART公共接口.md#gab9f7de744a68a311330576d7da02c44a)
- [UART_CFG_DATA_BITS_5](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)
- [UART_CFG_DATA_BITS_6](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)
- [UART_CFG_DATA_BITS_7](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)
- [UART_CFG_DATA_BITS_8](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)
- [UART_CFG_DATA_BITS_9](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)
- [uart_config_flow_control](../hardware/P330_UART公共接口.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)
- [UART_CFG_FLOW_CTRL_NONE](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)
- [UART_CFG_FLOW_CTRL_RTS_CTS](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)
- [UART_CFG_FLOW_CTRL_DTR_DSR](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)
- [UART_CFG_FLOW_CTRL_RS485](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)
- [uart_config](../hardware/P331_UART配置结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [baudrate](../hardware/P331_UART配置结构.md#ab532159a689e8f38c2465ce2d1fef354)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [parity](../hardware/P331_UART配置结构.md#a9371728729252797880de052aae01089)
- [stop_bits](../hardware/P331_UART配置结构.md#a7b98cd63c531110dc3dc99e94db73642)
- [data_bits](../hardware/P331_UART配置结构.md#a93ee24cf6669fb4cfece78a53d3ec6c5)
- [flow_ctrl](../hardware/P331_UART配置结构.md#af259c5efab532920b5cce7ae57f6af5e)
- [uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
- [device](../device_reference/P002_设备对象结构.md)
- [uart_event_type](../hardware/P334_UART异步接口.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)
- [UART_TX_DONE](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)
- [UART_TX_ABORTED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)
- [UART_RX_RDY](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)
- [UART_RX_BUF_REQUEST](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)
- [UART_RX_BUF_RELEASED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)
- [UART_RX_DISABLED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)
- [UART_RX_STOPPED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)
- [uart_event_tx](../hardware/P335_UART发送事件结构.md)
- [buf](../hardware/P335_UART发送事件结构.md#a314a676a4050b2438b6f41485656bdbd)
- [len](../hardware/P335_UART发送事件结构.md#a7d844b2c0833d24accf82d58ee3408ff)
- [uart_event_rx](../hardware/P336_UART接收事件结构.md)
- [buf](../hardware/P336_UART接收事件结构.md#a2d9dfa9d9b25ff976cf2e937c72eb245)
- [offset](../hardware/P336_UART接收事件结构.md#aa483e719298c30b9f5e6c57d3d161281)
- [len](../hardware/P336_UART接收事件结构.md#a96414b96e63503336f8cf0d2249cd3bd)
- [uart_event_rx_buf](../hardware/P337_UART缓冲区释放事件结构.md)
- [buf](../hardware/P337_UART缓冲区释放事件结构.md#a2547c84b742f454cfedf1de6d433297b)
- [uart_event_rx_stop](../hardware/P338_UART接收停止事件结构.md)
- [reason](../hardware/P338_UART接收停止事件结构.md#a96fbae85208d9b3ea0382e7e236a932d)
- [data](../hardware/P338_UART接收停止事件结构.md#a1b361c8b7e17d1304a475235e734db48)
- [uart_event](../hardware/P339_UART事件联合结构.md)
- [type](../hardware/P339_UART事件联合结构.md#a2fb82a30e414a74943067cd0784f4b44)
- [uart_event_data](../hardware/P340_UART事件数据联合体.md)
- [tx](../hardware/P340_UART事件数据联合体.md#a79fb6b799d5574c6aa38a211e020035f)
- [rx](../hardware/P340_UART事件数据联合体.md#afac00624290b8fe5cf7b59516567b972)
- [rx_buf](../hardware/P340_UART事件数据联合体.md#ac03cdaeccba5f693337fa19299101863)
- [rx_stop](../hardware/P340_UART事件数据联合体.md#aad7488a2a3d91cea0ea874a08d7b88f6)
- [data](../hardware/P339_UART事件联合结构.md#a07e3eebb7642ab52c73baba514704c69)
- [uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)
- [uart_err_check](../hardware/P330_UART公共接口.md#ga22ea20fd8e07153b3b71cc9416f5462f)
- [uart_poll_in](../hardware/P332_UART轮询接口.md#gae81ac8cc976a20d774cfbda09e9c983d)
- [uart_poll_in_u16](../hardware/P332_UART轮询接口.md#gaad39c1358019bfdcb919da7982743553)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uart_poll_out](../hardware/P332_UART轮询接口.md#ga06ba27ba772a7a18462b8cdbc7f9353c)
- [uart_poll_out_u16](../hardware/P332_UART轮询接口.md#ga8faa3f58b9098c97e288e9c5f3367fd9)
- [uart_configure](../hardware/P330_UART公共接口.md#gaa0b75777b879af10543f7e8f463ff9a2)
- [uart_config_get](../hardware/P330_UART公共接口.md#ga81dfc5f2134de8e4acb5f063512cf703)
- [uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)
- [uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)
- [uart_fifo_read](../hardware/P333_UART中断驱动接口.md#gab10942076ac47ecff29e924098049398)
- [uart_fifo_read_u16](../hardware/P333_UART中断驱动接口.md#ga4a3c25dad2290f1f40e4b847e3b83f64)
- [uart_irq_tx_enable](../hardware/P333_UART中断驱动接口.md#ga9cbd6e33dce6a5b06233cf10077e19cc)
- [uart_irq_tx_disable](../hardware/P333_UART中断驱动接口.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)
- [uart_irq_tx_ready](../hardware/P333_UART中断驱动接口.md#ga5e126b5f19549eb7f5b785b98ebe7638)
- [uart_irq_rx_enable](../hardware/P333_UART中断驱动接口.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)
- [uart_irq_rx_disable](../hardware/P333_UART中断驱动接口.md#gaa759d7935fdd9ab6ca0761f161389a29)
- [uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)
- [uart_irq_rx_ready](../hardware/P333_UART中断驱动接口.md#gad04073b1b8e3de13b43ae1194561377b)
- [uart_irq_err_enable](../hardware/P333_UART中断驱动接口.md#ga7c24daae3326bc2959ea13a2be79969f)
- [uart_irq_err_disable](../hardware/P333_UART中断驱动接口.md#gaaf8a88361807e204f7227fbd1d0e75b2)
- [uart_irq_is_pending](../hardware/P333_UART中断驱动接口.md#gacd8c2978e0f1316dd79bb42baad1c5a7)
- [uart_irq_update](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)
- [uart_irq_callback_user_data_set](../hardware/P333_UART中断驱动接口.md#gaf469966a56d1fc9f50108201597ee0a0)
- [uart_irq_callback_set](../hardware/P333_UART中断驱动接口.md#ga5f7af3f7f0d9155349ea3b4fad78956c)
- [uart_callback_set](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)
- [uart_tx](../hardware/P334_UART异步接口.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uart_tx_u16](../hardware/P334_UART异步接口.md#gab0ea611cd072fa459a6f1780ce62c9e3)
- [uart_tx_abort](../hardware/P334_UART异步接口.md#gaa8a26d3ea685fb98030ea03613be6280)
- [uart_rx_enable](../hardware/P334_UART异步接口.md#ga902e18c2a727ed2988e1b6caa6a444b8)
- [uart_rx_enable_u16](../hardware/P334_UART异步接口.md#ga12d91846133351a85fa471fa90f2a0fd)
- [uart_rx_buf_rsp](../hardware/P334_UART异步接口.md#ga3970fe2818e214b0814ea8b73a816a6a)
- [uart_rx_buf_rsp_u16](../hardware/P334_UART异步接口.md#ga778bcfc30be853c8d320f295b34c17c0)
- [uart_rx_disable](../hardware/P334_UART异步接口.md#gafd4753bee51b230091a3c6ddb26ea734)
- [uart_line_ctrl_set](../hardware/P330_UART公共接口.md#gab039414b41145dc8d31349836da91263)
- [uart_line_ctrl_get](../hardware/P330_UART公共接口.md#gafda8a550284a54c8e1d6b6638de978e5)
- [uart_drv_cmd](../hardware/P330_UART公共接口.md#gaa8683398e5d709b513509d08841ed51b)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [zephyr/drivers/uart/uart_internal.h](P003_UART内部头文件参考.md)

---

[上一章](P001_UART驱动头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_UART内部头文件参考.md)
