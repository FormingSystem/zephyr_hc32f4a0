---
id: learning.zephyr-docs.spi-driver-reference.page-2
title: SPI驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2spi_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_SPI驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2spi_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_SPI驱动头文件参考.md)和[公共API](../hardware/P318_SPI公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00132"></a>
<a id="foldopen00165"></a>
<a id="foldopen00174"></a>
<a id="foldopen00260"></a>
<a id="foldopen00332"></a>
<a id="foldopen00345"></a>
<a id="foldopen00407"></a>
<a id="foldopen00428"></a>
<a id="foldopen00449"></a>
<a id="foldopen00529"></a>
<a id="foldopen00554"></a>
<a id="foldopen00560"></a>
<a id="foldopen00582"></a>
<a id="foldopen00597"></a>
<a id="foldopen00623"></a>
<a id="foldopen00643"></a>
<a id="foldopen00661"></a>
<a id="foldopen00679"></a>
<a id="foldopen00885"></a>
<a id="foldopen00896"></a>
<a id="foldopen00955"></a>
<a id="foldopen00990"></a>
<a id="foldopen01002"></a>
<a id="foldopen01015"></a>
<a id="foldopen01098"></a>
<a id="foldopen01124"></a>
<a id="foldopen01143"></a>
<a id="foldopen01167"></a>
<a id="foldopen01186"></a>
<a id="foldopen01234"></a>
<a id="foldopen01280"></a>
<a id="foldopen01316"></a>
<a id="foldopen01348"></a>
<a id="foldopen01378"></a>
<a id="foldopen01400"></a>
<a id="foldopen01415"></a>
<a id="foldopen01426"></a>
<a id="foldopen01475"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="adt-bindings_2spi_2spi_8h_html"></a>
<a id="agroup__clock__apis_html_ga0501e82515b2bdf36453c4cc80f5e0cc"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__gpio__interface_html_gaaec9ad17c08a0d527d66445fe82d8327"></a>
<a id="agroup__spi__interface__backend_html_ga03be7f33032ac479153616bbe26848e7"></a>
<a id="agroup__spi__interface__backend_html_ga1db2a410f482d0f26c49f96352aa606d"></a>
<a id="agroup__spi__interface__backend_html_ga3fc669f866b03cfdad98754de69cda13"></a>
<a id="agroup__spi__interface__backend_html_gac651ff7cd3dde7abe2525e20ef2e9e7d"></a>
<a id="agroup__spi__interface__backend_html_gae274c0d704e8fd8993631fc1b91bfcb1"></a>
<a id="agroup__spi__interface_html_ga0c4f4f0a93bb83a4f58d551a7491164e"></a>
<a id="agroup__spi__interface_html_ga292d6d1fe82f3f1ce0d9a2aa5437201b"></a>
<a id="agroup__spi__interface_html_ga37b4e5079ed18b70b0c5a260f4c36403"></a>
<a id="agroup__spi__interface_html_ga398a8ae1c4799e77fb6c067b6d47294a"></a>
<a id="agroup__spi__interface_html_ga41b8a541257c0d45575fdc4593417edc"></a>
<a id="agroup__spi__interface_html_ga41f771785a4fa9ca0954125d1e97959e"></a>
<a id="agroup__spi__interface_html_ga52c017066736414b31ff709ddc67c4ff"></a>
<a id="agroup__spi__interface_html_ga6114e63ca23b82f9be0ac70e372b878b"></a>
<a id="agroup__spi__interface_html_ga6f69e68a79afbbe016aecc515f14de3a"></a>
<a id="agroup__spi__interface_html_ga7a1d7ebd37d2861b169c265cb90015bf"></a>
<a id="agroup__spi__interface_html_ga7e7c4460670ec1c0433ba19accd97796"></a>
<a id="agroup__spi__interface_html_ga829b59767c51b20b546eee8a9cc84b69"></a>
<a id="agroup__spi__interface_html_ga8b23855bdc7dab7d02b8f7daa7db651b"></a>
<a id="agroup__spi__interface_html_ga9a1ceadb217368232af5b688c12169c5"></a>
<a id="agroup__spi__interface_html_gaa13f0da1f28cffa0da4677987db0c9c5"></a>
<a id="agroup__spi__interface_html_gad51054c1ba259db5a64619788506a6f5"></a>
<a id="agroup__spi__interface_html_gad7d1058f600d6aef4fc4e2bdff5d55f3"></a>
<a id="agroup__spi__interface_html_gadcb19d43461ef88e31f6b382cc87fd0b"></a>
<a id="agroup__spi__interface_html_gae1156a4ee1b5909c321811045566d888"></a>
<a id="agroup__spi__interface_html_gafea78af1fe1fa49fdc5459ab3a2d5f73"></a>
<a id="agroup__stats__apis_html_ga4124f8c0a9ffb78d8be608a780676785"></a>
<a id="agroup__stats__apis_html_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>
<a id="agroup__stats__apis_html_ga592329613cc77cfa5dee3e1d3b16dd93"></a>
<a id="agroup__stats__apis_html_ga5fba46e743c05b4f36df91a86c37e30d"></a>
<a id="agroup__stats__apis_html_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>
<a id="agroup__stats__apis_html_gae8e85c3ce2d901f4668d7237b19999fe"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="astats_2stats_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3ea490c9b3617d4479bd80ef93cd5602"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice__state_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructk__poll__signal_html"></a>
<a id="astructrtio__iodev__api_html"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev__sqe_html_a2bd98599678909c0ddb22f879affa12b"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio__iodev_html_af0f3a27fe8dea2161c9a73cb838bdeec"></a>
<a id="astructrtio__sqe_html_a6c784702f011592c84feacd57915bbfc"></a>
<a id="astructspi__buf__set_html"></a>
<a id="astructspi__buf__set_html_a2b88917ca29487b2d0b5b63d2083db67"></a>
<a id="astructspi__buf__set_html_abc7c37cffebb7873aaba2e524c9a23dc"></a>
<a id="astructspi__buf_html"></a>
<a id="astructspi__buf_html_a9755deadff0dd01a886f22e41099b8ba"></a>
<a id="astructspi__buf_html_aeaf52d3ff5af10545b2d6904ed452cba"></a>
<a id="astructspi__config_html"></a>
<a id="astructspi__config_html_a020ca853537483b9641c37be70ab6ca0"></a>
<a id="astructspi__config_html_a537dbfe323fafedaa219de1be2097dde"></a>
<a id="astructspi__config_html_a71a02ea548e187e6511abf10fdfa4829"></a>
<a id="astructspi__config_html_aa1ec6933fe66f91653c5be488e4c9b2a"></a>
<a id="astructspi__config_html_ae952e508c8e719098b15edf665c4eb81"></a>
<a id="astructspi__config_html_af55961609841e6f42fb20bf807710a5d"></a>
<a id="astructspi__cs__control_html"></a>
<a id="astructspi__cs__control_html_a04569d78ac7d6022ffee0c28f5d3b629"></a>
<a id="astructspi__cs__control_html_a5bb1c6185fe550f6cbc20d95bda6abab"></a>
<a id="astructspi__cs__control_html_a8614da6ccc73ce2a2a457fbd7a0882e2"></a>
<a id="astructspi__cs__control_html_a8ad907e168666c2ddca77e89f9b9f47f"></a>
<a id="astructspi__cs__control_html_ab3d5a48c9e725070cf72a42365222bff"></a>
<a id="astructspi__driver__api_html"></a>
<a id="astructspi__driver__api_html_abeb852d35e4772dcec716cf63ef307bb"></a>
<a id="astructspi__driver__api_html_ae15944912ece9f736fd935184e8a184d"></a>
<a id="astructspi__driver__api_html_af067daa58e79b9067a59fedcfd61034b"></a>
<a id="astructspi__driver__api_html_af88a1a6b823d5742b099170eb3b2e38a"></a>
<a id="astructspi__dt__spec_html"></a>
<a id="astructspi__dt__spec_html_a37519633ae787ffaa1026e6867d7007a"></a>
<a id="astructspi__dt__spec_html_a88372c17ede2e9dfb0c09c49abebf87e"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2015 Intel Corporation
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_SPI_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_DRIVERS_SPI_H_
<a id="l00015"></a>
<a id="l00025"></a>
<a id="l00026"></a>#include &lt;zephyr/types.h&gt;
<a id="l00027"></a>#include &lt;stddef.h&gt;
<a id="l00028"></a>#include &lt;zephyr/device.h&gt;
<a id="l00029"></a>#include &lt;zephyr/dt-bindings/spi/spi.h&gt;
<a id="l00030"></a>#include &lt;zephyr/drivers/gpio.h&gt;
<a id="l00031"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00032"></a>#include &lt;zephyr/sys/__assert.h&gt;
<a id="l00033"></a>#include &lt;zephyr/rtio/rtio.h&gt;
<a id="l00034"></a>#include &lt;zephyr/stats/stats.h&gt;
<a id="l00035"></a>
<a id="l00036"></a>#ifdef __cplusplus
<a id="l00037"></a>extern "C" {
<a id="l00038"></a>#endif
<a id="l00039"></a>
<a id="l00044"></a>
<a id="l00052"></a>#define SPI_OP_MODE_CONTROLLER  0U
<a id="l00053"></a>
<a id="l00062"></a>#define SPI_OP_MODE_PERIPHERAL  BIT(0)
<a id="l00063"></a>
<a id="l00068"></a>#define SPI_OP_MODE_MASTER      SPI_OP_MODE_CONTROLLER __DEPRECATED_MACRO
<a id="l00069"></a>
<a id="l00074"></a>#define SPI_OP_MODE_SLAVE       SPI_OP_MODE_PERIPHERAL __DEPRECATED_MACRO
<a id="l00075"></a>
<a id="l00077"></a>#define SPI_OP_MODE_MASK        0x1U
<a id="l00079"></a>
<a id="l00083"></a>#define SPI_OP_MODE_GET(_operation_) ((_operation_) &amp; SPI_OP_MODE_MASK)
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00091"></a>
<a id="l00101"></a>#define SPI_MODE_CPOL           BIT(1)
<a id="l00102"></a>
<a id="l00112"></a>#define SPI_MODE_CPHA           BIT(2)
<a id="l00113"></a>
<a id="l00123"></a>#define SPI_MODE_LOOP           BIT(3)
<a id="l00124"></a>
<a id="l00126"></a>#define SPI_MODE_MASK           (0xEU)
<a id="l00128"></a>
<a id="l00132"></a>#define SPI_MODE_GET(_mode_)                    \
<a id="l00133"></a>        ((_mode_) &amp; SPI_MODE_MASK)
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00148"></a>
<a id="l00150"></a>#define SPI_TRANSFER_MSB        (0U)
<a id="l00152"></a>#define SPI_TRANSFER_LSB        BIT(4)
<a id="l00153"></a>
<a id="l00155"></a>#define SPI_WORD_SIZE_SHIFT     (5U)
<a id="l00156"></a>#define SPI_WORD_SIZE_MASK      (0x3FU &lt;&lt; SPI_WORD_SIZE_SHIFT)
<a id="l00158"></a>
<a id="l00165"></a>#define SPI_WORD_SIZE_GET(operation)                                    \
<a id="l00166"></a>        (((operation) &amp; SPI_WORD_SIZE_MASK) &gt;&gt; SPI_WORD_SIZE_SHIFT)
<a id="l00167"></a>
<a id="l00174"></a>#define SPI_WORD_SET(word_size)                 \
<a id="l00175"></a>        ((word_size) &lt;&lt; SPI_WORD_SIZE_SHIFT)
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00184"></a>
<a id="l00192"></a>#define SPI_HOLD_ON_CS          BIT(12)
<a id="l00193"></a>
<a id="l00211"></a>#define SPI_LOCK_ON             BIT(13)
<a id="l00212"></a>
<a id="l00224"></a>#define SPI_CS_ACTIVE_HIGH      BIT(14)
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00239"></a>#define SPI_LINES_SINGLE        (0U &lt;&lt; 16)
<a id="l00240"></a>#define SPI_LINES_DUAL          (1U &lt;&lt; 16)
<a id="l00241"></a>#define SPI_LINES_QUAD          (2U &lt;&lt; 16)
<a id="l00242"></a>#define SPI_LINES_OCTAL         (3U &lt;&lt; 16)
<a id="l00243"></a>
<a id="l00244"></a>#define SPI_LINES_MASK          (0x3U &lt;&lt; 16)
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00252"></a>
<a id="l00260"></a>struct spi_cs_control {
<a id="l00261"></a>        union {
<a id="l00262"></a>                struct {
<a id="l00270"></a>                        struct gpio_dt_spec gpio;
<a id="l00275"></a>                        uint32_t delay;
<a id="l00276"></a>                };
<a id="l00277"></a>                struct {
<a id="l00282"></a>                        uint32_t setup_ns;
<a id="l00288"></a>                        uint32_t hold_ns;
<a id="l00289"></a>                };
<a id="l00290"></a>        };
<a id="l00291"></a>        /* To keep track of which form of this struct is valid */
<a id="l00292"></a>        bool cs_is_gpio;
<a id="l00293"></a>};
<a id="l00294"></a>
<a id="l00332"></a>#define SPI_CS_GPIOS_DT_SPEC_GET(spi_dev)                       \
<a id="l00333"></a>        GPIO_DT_SPEC_GET_BY_IDX_OR(DT_BUS(spi_dev), cs_gpios,   \
<a id="l00334"></a>                                   DT_REG_ADDR_RAW(spi_dev), {})
<a id="l00335"></a>
<a id="l00345"></a>#define SPI_CS_GPIOS_DT_SPEC_INST_GET(inst) \
<a id="l00346"></a>        SPI_CS_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))
<a id="l00347"></a>
<a id="l00349"></a>#define SPI_CS_CONTROL_MAX_DELAY(node_id)                       \
<a id="l00350"></a>        MAX(DT_PROP_OR(node_id, spi_cs_setup_delay_ns, 0),      \
<a id="l00351"></a>            DT_PROP_OR(node_id, spi_cs_hold_delay_ns, 0))
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>#define SPI_CS_CONTROL_INIT_GPIO(node_id)                                               \
<a id="l00355"></a>        .gpio = SPI_CS_GPIOS_DT_SPEC_GET(node_id),                                      \
<a id="l00356"></a>        .delay = DIV_ROUND_UP(SPI_CS_CONTROL_MAX_DELAY(node_id), 1000),
<a id="l00357"></a>
<a id="l00358"></a>#define SPI_CS_CONTROL_INIT_NATIVE(node_id)                                             \
<a id="l00359"></a>        .setup_ns = DT_PROP_OR(node_id, spi_cs_setup_delay_ns, 0),                      \
<a id="l00360"></a>        .hold_ns = DT_PROP_OR(node_id, spi_cs_hold_delay_ns, 0),
<a id="l00362"></a>
<a id="l00407"></a>#define SPI_CS_CONTROL_INIT(node_id)                                            \
<a id="l00408"></a>{                                                                               \
<a id="l00409"></a>        COND_CODE_1(DT_SPI_DEV_HAS_CS_GPIOS(node_id),                           \
<a id="l00410"></a>                        (SPI_CS_CONTROL_INIT_GPIO(node_id)),                    \
<a id="l00411"></a>                        (SPI_CS_CONTROL_INIT_NATIVE(node_id)))                  \
<a id="l00412"></a>        .cs_is_gpio = DT_SPI_DEV_HAS_CS_GPIOS(node_id),                         \
<a id="l00413"></a>}
<a id="l00414"></a>
<a id="l00428"></a>#define SPI_CS_CONTROL_INIT_INST(inst)                  \
<a id="l00429"></a>        SPI_CS_CONTROL_INIT(DT_DRV_INST(inst))
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00436"></a>#if defined(CONFIG_SPI_EXTENDED_MODES)
<a id="l00437"></a>typedef uint32_t spi_operation_t;
<a id="l00438"></a>#else
<a id="l00439"></a>typedef uint16_t spi_operation_t;
<a id="l00440"></a>#endif
<a id="l00441"></a>
<a id="l00449"></a>struct spi_config {
<a id="l00451"></a>        uint32_t frequency;
<a id="l00472"></a>        spi_operation_t operation;
<a id="l00474"></a>        union {
<a id="l00476"></a>                uint16_t peripheral;
<a id="l00481"></a>                __deprecated uint16_t slave;
<a id="l00482"></a>        };
<a id="l00487"></a>        struct spi_cs_control cs;
<a id="l00492"></a>        uint16_t word_delay;
<a id="l00493"></a>};
<a id="l00494"></a>
<a id="l00496"></a>/* converts from the special DT zero value to half of the frequency, for drivers usage mostly */
<a id="l00497"></a>static inline uint16_t spi_get_word_delay(const struct spi_config *cfg)
<a id="l00498"></a>{
<a id="l00499"></a>        uint32_t freq = cfg-&gt;frequency;
<a id="l00500"></a>
<a id="l00501"></a>        if (cfg-&gt;word_delay != 0) {
<a id="l00502"></a>                return cfg-&gt;word_delay;
<a id="l00503"></a>        }
<a id="l00504"></a>
<a id="l00505"></a>        if (freq == 0) {
<a id="l00506"></a>                return 0;
<a id="l00507"></a>        }
<a id="l00508"></a>
<a id="l00509"></a>        uint64_t period_ns = NSEC_PER_SEC / freq;
<a id="l00510"></a>
<a id="l00511"></a>        period_ns = MIN(period_ns, UINT16_MAX);
<a id="l00512"></a>        period_ns /= 2;
<a id="l00513"></a>
<a id="l00514"></a>        return (uint16_t)period_ns;
<a id="l00515"></a>}
<a id="l00517"></a>
<a id="l00529"></a>#define SPI_CONFIG_DT(node_id, operation_)                              \
<a id="l00530"></a>        {                                                               \
<a id="l00531"></a>                .frequency = DT_PROP(node_id, spi_max_frequency),       \
<a id="l00532"></a>                .operation = (operation_) |                             \
<a id="l00533"></a>                        DT_PROP(node_id, duplex) |                      \
<a id="l00534"></a>                        DT_PROP(node_id, frame_format) |                        \
<a id="l00535"></a>                        COND_CODE_1(DT_PROP(node_id, spi_cpol), SPI_MODE_CPOL, (0)) |   \
<a id="l00536"></a>                        COND_CODE_1(DT_PROP(node_id, spi_cpha), SPI_MODE_CPHA, (0)) |   \
<a id="l00537"></a>                        COND_CODE_1(DT_PROP(node_id, spi_hold_cs), SPI_HOLD_ON_CS, (0)) | \
<a id="l00538"></a>                        COND_CODE_1(DT_PROP(node_id, spi_lsb_first), SPI_TRANSFER_LSB, (0)) |   \
<a id="l00539"></a>                        COND_CODE_1(DT_PROP(node_id, spi_cs_high), SPI_CS_ACTIVE_HIGH, (0)),    \
<a id="l00540"></a>                .peripheral = DT_REG_ADDR(node_id),                     \
<a id="l00541"></a>                .cs = SPI_CS_CONTROL_INIT(node_id),                     \
<a id="l00542"></a>                .word_delay = DT_PROP(node_id, spi_interframe_delay_ns),\
<a id="l00543"></a>        }
<a id="l00544"></a>
<a id="l00554"></a>#define SPI_CONFIG_DT_INST(inst, operation_)                    \
<a id="l00555"></a>        SPI_CONFIG_DT(DT_DRV_INST(inst), operation_)
<a id="l00556"></a>
<a id="l00560"></a>struct spi_dt_spec {
<a id="l00562"></a>        const struct device *bus;
<a id="l00564"></a>        struct spi_config config;
<a id="l00565"></a>};
<a id="l00566"></a>
<a id="l00582"></a>#define SPI_DT_SPEC_GET(node_id, operation_)                                    \
<a id="l00583"></a>        {                                                                       \
<a id="l00584"></a>                .bus = DEVICE_DT_GET(DT_BUS(node_id)),                          \
<a id="l00585"></a>                .config = SPI_CONFIG_DT(node_id, operation_),                   \
<a id="l00586"></a>        }
<a id="l00587"></a>
<a id="l00597"></a>#define SPI_DT_SPEC_INST_GET(inst, operation_) \
<a id="l00598"></a>        SPI_DT_SPEC_GET(DT_DRV_INST(inst), operation_)
<a id="l00599"></a>
<a id="l00603"></a>#define SPI_SDO_OVERRUN_UNKNOWN 0x100
<a id="l00604"></a>
<a id="l00609"></a>#define SPI_MOSI_OVERRUN_UNKNOWN SPI_SDO_OVERRUN_UNKNOWN __DEPRECATED_MACRO
<a id="l00610"></a>
<a id="l00623"></a>#define SPI_SDO_OVERRUN_DT(node_id) \
<a id="l00624"></a>        DT_PROP_OR(node_id, overrun_character, SPI_SDO_OVERRUN_UNKNOWN)
<a id="l00625"></a>
<a id="l00630"></a>#define SPI_MOSI_OVERRUN_DT(node_id) SPI_SDO_OVERRUN_DT(node_id) __DEPRECATED_MACRO
<a id="l00631"></a>
<a id="l00643"></a>#define SPI_SDO_OVERRUN_DT_INST(inst) \
<a id="l00644"></a>        DT_INST_PROP_OR(inst, overrun_character, SPI_SDO_OVERRUN_UNKNOWN)
<a id="l00645"></a>
<a id="l00650"></a>#define SPI_MOSI_OVERRUN_DT_INST(inst) SPI_SDO_OVERRUN_DT_INST(inst) __DEPRECATED_MACRO
<a id="l00651"></a>
<a id="l00661"></a>struct spi_buf {
<a id="l00663"></a>        void *buf;
<a id="l00665"></a>        size_t len;
<a id="l00666"></a>};
<a id="l00667"></a>
<a id="l00679"></a>struct spi_buf_set {
<a id="l00681"></a>        const struct spi_buf *buffers;
<a id="l00683"></a>        size_t count;
<a id="l00684"></a>};
<a id="l00685"></a>
<a id="l00690"></a>#if defined(CONFIG_SPI_STATS)
<a id="l00691"></a>STATS_SECT_START(spi)
<a id="l00692"></a>STATS_SECT_ENTRY32(rx_bytes)
<a id="l00693"></a>STATS_SECT_ENTRY32(tx_bytes)
<a id="l00694"></a>STATS_SECT_ENTRY32(transfer_error)
<a id="l00695"></a>STATS_SECT_END;
<a id="l00696"></a>
<a id="l00697"></a>STATS_NAME_START(spi)
<a id="l00698"></a>STATS_NAME(spi, rx_bytes)
<a id="l00699"></a>STATS_NAME(spi, tx_bytes)
<a id="l00700"></a>STATS_NAME(spi, transfer_error)
<a id="l00701"></a>STATS_NAME_END(spi);
<a id="l00702"></a>
<a id="l00706"></a>struct spi_device_state {
<a id="l00707"></a>        struct device_state devstate;
<a id="l00708"></a>        struct stats_spi stats;
<a id="l00709"></a>};
<a id="l00710"></a>
<a id="l00714"></a>#define Z_SPI_GET_STATS(dev_)                           \
<a id="l00715"></a>        CONTAINER_OF(dev_-&gt;state, struct spi_device_state, devstate)-&gt;stats
<a id="l00716"></a>
<a id="l00722"></a>#define SPI_STATS_RX_BYTES_INCN(dev_, n)                        \
<a id="l00723"></a>        STATS_INCN(Z_SPI_GET_STATS(dev_), rx_bytes, n)
<a id="l00724"></a>
<a id="l00730"></a>#define SPI_STATS_TX_BYTES_INCN(dev_, n)                        \
<a id="l00731"></a>        STATS_INCN(Z_SPI_GET_STATS(dev_), tx_bytes, n)
<a id="l00732"></a>
<a id="l00740"></a>#define SPI_STATS_TRANSFER_ERROR_INC(dev_)                      \
<a id="l00741"></a>        STATS_INC(Z_SPI_GET_STATS(dev_), transfer_error)
<a id="l00742"></a>
<a id="l00747"></a>#define Z_SPI_DEVICE_STATE_DEFINE(dev_id)       \
<a id="l00748"></a>        static struct spi_device_state Z_DEVICE_STATE_NAME(dev_id)      \
<a id="l00749"></a>        __attribute__((__section__(".z_devstate")));
<a id="l00750"></a>
<a id="l00757"></a>#define Z_SPI_INIT_FN(dev_id, init_fn)                                  \
<a id="l00758"></a>        static inline int UTIL_CAT(dev_id, _init)(const struct device *dev) \
<a id="l00759"></a>        {                                                               \
<a id="l00760"></a>                struct spi_device_state *state =                        \
<a id="l00761"></a>                        CONTAINER_OF(dev-&gt;state, struct spi_device_state, devstate); \
<a id="l00762"></a>                stats_init(&amp;state-&gt;stats.s_hdr, STATS_SIZE_32, 3,       \
<a id="l00763"></a>                           STATS_NAME_INIT_PARMS(spi));                 \
<a id="l00764"></a>                stats_register(dev-&gt;name, &amp;(state-&gt;stats.s_hdr));       \
<a id="l00765"></a>                return init_fn(dev);                                    \
<a id="l00766"></a>        }
<a id="l00768"></a>
<a id="l00769"></a>#define SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, deinit_fn,        \
<a id="l00770"></a>                                    pm_device, data_ptr, cfg_ptr,       \
<a id="l00771"></a>                                    level, prio, api_ptr, ...)          \
<a id="l00772"></a>        Z_SPI_DEVICE_STATE_DEFINE(Z_DEVICE_DT_DEV_ID(node_id));         \
<a id="l00773"></a>        Z_SPI_INIT_FN(Z_DEVICE_DT_DEV_ID(node_id), init_fn)             \
<a id="l00774"></a>        Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id),           \
<a id="l00775"></a>                        DEVICE_DT_NAME(node_id),                        \
<a id="l00776"></a>                        &amp;UTIL_CAT(Z_DEVICE_DT_DEV_ID(node_id), _init),  \
<a id="l00777"></a>                        deinit_fn, Z_DEVICE_DT_FLAGS(node_id),          \
<a id="l00778"></a>                        pm_device, data_ptr, cfg_ptr, level, prio,      \
<a id="l00779"></a>                        api_ptr,                                        \
<a id="l00780"></a>                        &amp;(Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_ID(node_id)).devstate), \
<a id="l00781"></a>                        __VA_ARGS__)
<a id="l00782"></a>
<a id="l00783"></a>static inline void spi_transceive_stats(const struct device *dev, int error,
<a id="l00784"></a>                                        const struct spi_buf_set *tx_bufs,
<a id="l00785"></a>                                        const struct spi_buf_set *rx_bufs)
<a id="l00786"></a>{
<a id="l00787"></a>        uint32_t tx_bytes;
<a id="l00788"></a>        uint32_t rx_bytes;
<a id="l00789"></a>
<a id="l00790"></a>        if (error) {
<a id="l00791"></a>                SPI_STATS_TRANSFER_ERROR_INC(dev);
<a id="l00792"></a>        }
<a id="l00793"></a>
<a id="l00794"></a>        if (tx_bufs) {
<a id="l00795"></a>                tx_bytes = tx_bufs-&gt;count ? tx_bufs-&gt;buffers-&gt;len : 0;
<a id="l00796"></a>                SPI_STATS_TX_BYTES_INCN(dev, tx_bytes);
<a id="l00797"></a>        }
<a id="l00798"></a>
<a id="l00799"></a>        if (rx_bufs) {
<a id="l00800"></a>                rx_bytes = rx_bufs-&gt;count ? rx_bufs-&gt;buffers-&gt;len : 0;
<a id="l00801"></a>                SPI_STATS_RX_BYTES_INCN(dev, rx_bytes);
<a id="l00802"></a>        }
<a id="l00803"></a>}
<a id="l00805"></a>
<a id="l00806"></a>#else /*CONFIG_SPI_STATS*/
<a id="l00807"></a>
<a id="l00812"></a>
<a id="l00833"></a>#define SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, deinit_fn, pm, data,      \
<a id="l00834"></a>                                    config, level, prio, api, ...)              \
<a id="l00835"></a>        Z_DEVICE_STATE_DEFINE(Z_DEVICE_DT_DEV_ID(node_id));                     \
<a id="l00836"></a>        Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id),                   \
<a id="l00837"></a>                        DEVICE_DT_NAME(node_id), init_fn, deinit_fn,            \
<a id="l00838"></a>                        Z_DEVICE_DT_FLAGS(node_id), pm, data, config,           \
<a id="l00839"></a>                        level, prio, api,                                       \
<a id="l00840"></a>                        &amp;Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_ID(node_id)),      \
<a id="l00841"></a>                        __VA_ARGS__)
<a id="l00842"></a>
<a id="l00844"></a>
<a id="l00845"></a>#define SPI_STATS_RX_BYTES_INC(dev_)
<a id="l00846"></a>#define SPI_STATS_TX_BYTES_INC(dev_)
<a id="l00847"></a>#define SPI_STATS_TRANSFER_ERROR_INC(dev_)
<a id="l00848"></a>
<a id="l00849"></a>#define spi_transceive_stats(dev, error, tx_bufs, rx_bufs)
<a id="l00850"></a>
<a id="l00851"></a>#endif /*CONFIG_SPI_STATS*/
<a id="l00852"></a>
<a id="l00872"></a>#define SPI_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio,   \
<a id="l00873"></a>                             api, ...)                                          \
<a id="l00874"></a>        SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, NULL, pm, data, config,   \
<a id="l00875"></a>                                    level, prio, api, __VA_ARGS__)
<a id="l00876"></a>
<a id="l00885"></a>#define SPI_DEVICE_DT_INST_DEINIT_DEFINE(inst, ...) \
<a id="l00886"></a>        SPI_DEVICE_DT_DEINIT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
<a id="l00887"></a>
<a id="l00896"></a>#define SPI_DEVICE_DT_INST_DEFINE(inst, ...)                                       \
<a id="l00897"></a>        SPI_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
<a id="l00898"></a>
<a id="l00903"></a>
<a id="l00909"></a>typedef int (*spi_api_io)(const struct device *dev,
<a id="l00910"></a>                          const struct spi_config *config,
<a id="l00911"></a>                          const struct spi_buf_set *tx_bufs,
<a id="l00912"></a>                          const struct spi_buf_set *rx_bufs);
<a id="l00913"></a>
<a id="l00921"></a>typedef void (*spi_callback_t)(const struct device *dev, int result, void *data);
<a id="l00922"></a>
<a id="l00928"></a>typedef int (*spi_api_io_async)(const struct device *dev,
<a id="l00929"></a>                                const struct spi_config *config,
<a id="l00930"></a>                                const struct spi_buf_set *tx_bufs,
<a id="l00931"></a>                                const struct spi_buf_set *rx_bufs,
<a id="l00932"></a>                                spi_callback_t cb,
<a id="l00933"></a>                                void *userdata);
<a id="l00934"></a>
<a id="l00935"></a>#if defined(CONFIG_SPI_RTIO) || defined(__DOXYGEN__)
<a id="l00936"></a>
<a id="l00940"></a>typedef void (*spi_api_iodev_submit)(const struct device *dev,
<a id="l00941"></a>                                     struct rtio_iodev_sqe *iodev_sqe);
<a id="l00942"></a>#endif /* CONFIG_SPI_RTIO */
<a id="l00943"></a>
<a id="l00948"></a>typedef int (*spi_api_release)(const struct device *dev,
<a id="l00949"></a>                               const struct spi_config *config);
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00955"></a>__subsystem struct spi_driver_api {
<a id="l00959"></a>        spi_api_io transceive;
<a id="l00960"></a>#if defined(CONFIG_SPI_ASYNC) || defined(__DOXYGEN__)
<a id="l00965"></a>        spi_api_io_async transceive_async;
<a id="l00966"></a>#endif /* CONFIG_SPI_ASYNC */
<a id="l00967"></a>#if defined(CONFIG_SPI_RTIO) || defined(__DOXYGEN__)
<a id="l00972"></a>        spi_api_iodev_submit iodev_submit;
<a id="l00973"></a>#endif /* CONFIG_SPI_RTIO */
<a id="l00977"></a>        spi_api_release release;
<a id="l00978"></a>};
<a id="l00979"></a>
<a id="l00982"></a>
<a id="l00990"></a>static inline bool spi_cs_is_gpio(const struct spi_config *config)
<a id="l00991"></a>{
<a id="l00992"></a>        return config-&gt;cs.cs_is_gpio;
<a id="l00993"></a>}
<a id="l00994"></a>
<a id="l01002"></a>static inline bool spi_cs_is_gpio_dt(const struct spi_dt_spec *spec)
<a id="l01003"></a>{
<a id="l01004"></a>        return spi_cs_is_gpio(&amp;spec-&gt;config);
<a id="l01005"></a>}
<a id="l01006"></a>
<a id="l01015"></a>static inline bool spi_is_ready_dt(const struct spi_dt_spec *spec)
<a id="l01016"></a>{
<a id="l01017"></a>        /* Validate bus is ready */
<a id="l01018"></a>        if (!device_is_ready(spec-&gt;bus)) {
<a id="l01019"></a>                return false;
<a id="l01020"></a>        }
<a id="l01021"></a>        /* Validate CS gpio port is ready, if it is used */
<a id="l01022"></a>        if (spi_cs_is_gpio_dt(spec) &amp;&amp;
<a id="l01023"></a>            !gpio_is_ready_dt(&amp;spec-&gt;config.cs.gpio)) {
<a id="l01024"></a>                return false;
<a id="l01025"></a>        }
<a id="l01026"></a>        return true;
<a id="l01027"></a>}
<a id="l01028"></a>
<a id="l01036"></a>
<a id="l01066"></a>__syscall int spi_transceive(const struct device *dev,
<a id="l01067"></a>                             const struct spi_config *config,
<a id="l01068"></a>                             const struct spi_buf_set *tx_bufs,
<a id="l01069"></a>                             const struct spi_buf_set *rx_bufs);
<a id="l01070"></a>
<a id="l01071"></a>static inline int z_impl_spi_transceive(const struct device *dev,
<a id="l01072"></a>                                        const struct spi_config *config,
<a id="l01073"></a>                                        const struct spi_buf_set *tx_bufs,
<a id="l01074"></a>                                        const struct spi_buf_set *rx_bufs)
<a id="l01075"></a>{
<a id="l01076"></a>        int ret = DEVICE_API_GET(spi, dev)-&gt;transceive(dev, config, tx_bufs, rx_bufs);
<a id="l01077"></a>
<a id="l01078"></a>        spi_transceive_stats(dev, ret, tx_bufs, rx_bufs);
<a id="l01079"></a>
<a id="l01080"></a>        return ret;
<a id="l01081"></a>}
<a id="l01082"></a>
<a id="l01098"></a>static inline int spi_transceive_dt(const struct spi_dt_spec *spec,
<a id="l01099"></a>                                    const struct spi_buf_set *tx_bufs,
<a id="l01100"></a>                                    const struct spi_buf_set *rx_bufs)
<a id="l01101"></a>{
<a id="l01102"></a>        return spi_transceive(spec-&gt;bus, &amp;spec-&gt;config, tx_bufs, rx_bufs);
<a id="l01103"></a>}
<a id="l01104"></a>
<a id="l01124"></a>static inline int spi_read(const struct device *dev,
<a id="l01125"></a>                           const struct spi_config *config,
<a id="l01126"></a>                           const struct spi_buf_set *rx_bufs)
<a id="l01127"></a>{
<a id="l01128"></a>        return spi_transceive(dev, config, NULL, rx_bufs);
<a id="l01129"></a>}
<a id="l01130"></a>
<a id="l01143"></a>static inline int spi_read_dt(const struct spi_dt_spec *spec,
<a id="l01144"></a>                              const struct spi_buf_set *rx_bufs)
<a id="l01145"></a>{
<a id="l01146"></a>        return spi_read(spec-&gt;bus, &amp;spec-&gt;config, rx_bufs);
<a id="l01147"></a>}
<a id="l01148"></a>
<a id="l01167"></a>static inline int spi_write(const struct device *dev,
<a id="l01168"></a>                            const struct spi_config *config,
<a id="l01169"></a>                            const struct spi_buf_set *tx_bufs)
<a id="l01170"></a>{
<a id="l01171"></a>        return spi_transceive(dev, config, tx_bufs, NULL);
<a id="l01172"></a>}
<a id="l01173"></a>
<a id="l01186"></a>static inline int spi_write_dt(const struct spi_dt_spec *spec,
<a id="l01187"></a>                               const struct spi_buf_set *tx_bufs)
<a id="l01188"></a>{
<a id="l01189"></a>        return spi_write(spec-&gt;bus, &amp;spec-&gt;config, tx_bufs);
<a id="l01190"></a>}
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>#if defined(CONFIG_SPI_ASYNC) || defined(__DOXYGEN__)
<a id="l01205"></a>
<a id="l01234"></a>static inline int spi_transceive_cb(const struct device *dev,
<a id="l01235"></a>                                    const struct spi_config *config,
<a id="l01236"></a>                                    const struct spi_buf_set *tx_bufs,
<a id="l01237"></a>                                    const struct spi_buf_set *rx_bufs,
<a id="l01238"></a>                                    spi_callback_t callback,
<a id="l01239"></a>                                    void *userdata)
<a id="l01240"></a>{
<a id="l01241"></a>        return DEVICE_API_GET(spi, dev)-&gt;transceive_async(dev, config, tx_bufs, rx_bufs, callback,
<a id="l01242"></a>                                                          userdata);
<a id="l01243"></a>}
<a id="l01244"></a>
<a id="l01245"></a>#if defined(CONFIG_POLL) || defined(__DOXYGEN__)
<a id="l01246"></a>
<a id="l01248"></a>void z_spi_transfer_signal_cb(const struct device *dev, int result, void *userdata);
<a id="l01250"></a>
<a id="l01280"></a>static inline int spi_transceive_signal(const struct device *dev,
<a id="l01281"></a>                                       const struct spi_config *config,
<a id="l01282"></a>                                       const struct spi_buf_set *tx_bufs,
<a id="l01283"></a>                                       const struct spi_buf_set *rx_bufs,
<a id="l01284"></a>                                       struct k_poll_signal *sig)
<a id="l01285"></a>{
<a id="l01286"></a>        spi_callback_t cb = (sig == NULL) ? NULL : z_spi_transfer_signal_cb;
<a id="l01287"></a>
<a id="l01288"></a>        return DEVICE_API_GET(spi, dev)-&gt;transceive_async(dev, config, tx_bufs, rx_bufs, cb, sig);
<a id="l01289"></a>}
<a id="l01290"></a>
<a id="l01316"></a>static inline int spi_read_signal(const struct device *dev,
<a id="l01317"></a>                                 const struct spi_config *config,
<a id="l01318"></a>                                 const struct spi_buf_set *rx_bufs,
<a id="l01319"></a>                                 struct k_poll_signal *sig)
<a id="l01320"></a>{
<a id="l01321"></a>        return spi_transceive_signal(dev, config, NULL, rx_bufs, sig);
<a id="l01322"></a>}
<a id="l01323"></a>
<a id="l01348"></a>static inline int spi_write_signal(const struct device *dev,
<a id="l01349"></a>                                  const struct spi_config *config,
<a id="l01350"></a>                                  const struct spi_buf_set *tx_bufs,
<a id="l01351"></a>                                  struct k_poll_signal *sig)
<a id="l01352"></a>{
<a id="l01353"></a>        return spi_transceive_signal(dev, config, tx_bufs, NULL, sig);
<a id="l01354"></a>}
<a id="l01355"></a>
<a id="l01356"></a>#endif /* CONFIG_POLL */
<a id="l01357"></a>
<a id="l01359"></a>#endif /* CONFIG_SPI_ASYNC */
<a id="l01360"></a>
<a id="l01361"></a>
<a id="l01362"></a>#if defined(CONFIG_SPI_RTIO) || defined(__DOXYGEN__)
<a id="l01363"></a>
<a id="l01378"></a>static inline void spi_iodev_submit(struct rtio_iodev_sqe *iodev_sqe)
<a id="l01379"></a>{
<a id="l01380"></a>        const struct spi_dt_spec *dt_spec = (const struct spi_dt_spec *)iodev_sqe-&gt;sqe.iodev-&gt;data;
<a id="l01381"></a>        const struct device *dev = dt_spec-&gt;bus;
<a id="l01382"></a>
<a id="l01383"></a>        DEVICE_API_GET(spi, dev)-&gt;iodev_submit(dev, iodev_sqe);
<a id="l01384"></a>}
<a id="l01385"></a>
<a id="l01387"></a>extern const struct rtio_iodev_api spi_iodev_api;
<a id="l01389"></a>
<a id="l01400"></a>#define SPI_DT_IODEV_DEFINE(name, node_id, operation_)                          \
<a id="l01401"></a>        const struct spi_dt_spec _spi_dt_spec_##name =                          \
<a id="l01402"></a>                SPI_DT_SPEC_GET(node_id, operation_);                           \
<a id="l01403"></a>        RTIO_IODEV_DEFINE(name, &amp;spi_iodev_api, (void *)&amp;_spi_dt_spec_##name)
<a id="l01404"></a>
<a id="l01415"></a>#define SPI_DT_INST_IODEV_DEFINE(name, inst, operation_)                        \
<a id="l01416"></a>        SPI_DT_IODEV_DEFINE(name, DT_DRV_INST(inst), operation_)
<a id="l01417"></a>
<a id="l01426"></a>static inline bool spi_is_ready_iodev(const struct rtio_iodev *spi_iodev)
<a id="l01427"></a>{
<a id="l01428"></a>        struct spi_dt_spec *spec = (struct spi_dt_spec *)spi_iodev-&gt;data;
<a id="l01429"></a>
<a id="l01430"></a>        return spi_is_ready_dt(spec);
<a id="l01431"></a>}
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01434"></a>#endif /* CONFIG_SPI_RTIO */
<a id="l01435"></a>
<a id="l01455"></a>__syscall int spi_release(const struct device *dev,
<a id="l01456"></a>                          const struct spi_config *config);
<a id="l01457"></a>
<a id="l01458"></a>static inline int z_impl_spi_release(const struct device *dev,
<a id="l01459"></a>                                     const struct spi_config *config)
<a id="l01460"></a>{
<a id="l01461"></a>        return DEVICE_API_GET(spi, dev)-&gt;release(dev, config);
<a id="l01462"></a>}
<a id="l01463"></a>
<a id="l01475"></a>static inline int spi_release_dt(const struct spi_dt_spec *spec)
<a id="l01476"></a>{
<a id="l01477"></a>        return spi_release(spec-&gt;bus, &amp;spec-&gt;config);
<a id="l01478"></a>}
<a id="l01479"></a>
<a id="l01480"></a>#ifdef __cplusplus
<a id="l01481"></a>}
<a id="l01482"></a>#endif
<a id="l01483"></a>
<a id="l01487"></a>
<a id="l01488"></a>#include &lt;zephyr/syscalls/spi.h&gt;
<a id="l01489"></a>
<a id="l01493"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_SPI_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2015 Intel Corporation；Apache-2.0许可证原文保留。

2. 记录此结构当前使用哪一种有效形式。

3. 将设备树中的特殊零值转换为“频率的一半”，主要供驱动使用。（此处按原注释翻译；实际代码计算半周期，详见源码跟踪译注。）

4. 进入未启用CONFIG_SPI_STATS时的替代分支。

5. 结束CONFIG_SPI_STATS相关统计功能条件编译。

6. 结束CONFIG_SPI_RTIO相关提交类型的条件编译。

7. 结束CONFIG_SPI_ASYNC相关异步操作成员的条件编译。

8. 结束CONFIG_SPI_RTIO相关提交操作成员的条件编译。

9. 验证总线是否就绪（Ready）。

10. 如果使用片选GPIO，则验证其端口是否就绪。

11. 结束CONFIG_POLL相关轮询信号接口的条件编译。

12. 结束CONFIG_SPI_ASYNC相关异步接口的条件编译。

13. 结束CONFIG_SPI_RTIO相关实时I/O接口的条件编译。

14. 结束SPI驱动头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_SPI_H_。

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

GPIO（通用输入／输出，General-Purpose Input/Output）驱动API的主头文件。

符号定位：[gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)。

### `spi.h`

符号定位：[spi.h](../dt_bus_binding_reference/P003_SPI绑定常量头文件参考.md)。

### `NSEC_PER_SEC`

```c
#define NSEC_PER_SEC
```

每秒包含的纳秒（Nanosecond）数。

定义位置（Definition）：clock.h:113。

符号定位：[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

### `device_is_ready`

```c
bool device_is_ready(const struct device *dev)
```

验证设备是否已就绪、可以使用。

符号定位：[device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。

### `gpio_is_ready_dt`

```c
static bool gpio_is_ready_dt(const struct gpio_dt_spec *spec)
```

验证GPIO端口是否就绪。

定义位置（Definition）：gpio.h:982。

符号定位：[gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)。

### `spi_api_io_async`

```c
int(* spi_api_io_async)(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, spi_callback_t cb, void *userdata)
```

异步I/O回调API。

定义位置（Definition）：spi.h:928。

符号定位：[spi_api_io_async](../hardware/P324_SPI驱动后端接口.md#ga03be7f33032ac479153616bbe26848e7)。

### `spi_callback_t`

```c
void(* spi_callback_t)(const struct device *dev, int result, void *data)
```

用于异步传输请求（Asynchronous Transfer Requests）的SPI回调。

定义位置（Definition）：spi.h:921。

符号定位：[spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)。

### `spi_api_io`

```c
int(* spi_api_io)(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

I/O回调API（Callback API）。

定义位置（Definition）：spi.h:909。

符号定位：[spi_api_io](../hardware/P324_SPI驱动后端接口.md#ga3fc669f866b03cfdad98754de69cda13)。

### `spi_api_release`

```c
int(* spi_api_release)(const struct device *dev, const struct spi_config *config)
```

用于解锁SPI设备的回调API。

定义位置（Definition）：spi.h:948。

符号定位：[spi_api_release](../hardware/P324_SPI驱动后端接口.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)。

### `spi_api_iodev_submit`

```c
void(* spi_api_iodev_submit)(const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
```

通过实时I/O（Real-Time I/O，RTIO）向SPI设备提交工作的回调API。

定义位置（Definition）：spi.h:940。

符号定位：[spi_api_iodev_submit](../hardware/P324_SPI驱动后端接口.md#gae274c0d704e8fd8993631fc1b91bfcb1)。

### `spi_release`

```c
int spi_release(const struct device *dev, const struct spi_config *config)
```

释放当前配置所锁定的SPI设备和／或片选。

符号定位：[spi_release](../hardware/P318_SPI公共接口.md#ga0c4f4f0a93bb83a4f58d551a7491164e)。

### `spi_write_dt`

```c
static int spi_write_dt(const struct spi_dt_spec *spec, const struct spi_buf_set *tx_bufs)
```

向spi_dt_spec指定的SPI总线写入数据。

定义位置（Definition）：spi.h:1186。

符号定位：[spi_write_dt](../hardware/P318_SPI公共接口.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)。

### `spi_is_ready_dt`

```c
static bool spi_is_ready_dt(const struct spi_dt_spec *spec)
```

验证SPI总线以及已定义的片选GPIO是否就绪（Ready）。

定义位置（Definition）：spi.h:1015。

符号定位：[spi_is_ready_dt](../hardware/P318_SPI公共接口.md#ga37b4e5079ed18b70b0c5a260f4c36403)。

### `spi_operation_t`

```c
uint16_t spi_operation_t
```

保存SPI操作标志的抽象类型（Opaque Type）。

定义位置（Definition）：spi.h:439。

符号定位：[spi_operation_t](../hardware/P318_SPI公共接口.md#ga398a8ae1c4799e77fb6c067b6d47294a)。

### `spi_transceive_signal`

```c
static int spi_transceive_signal(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, struct k_poll_signal *sig)
```

通过SPI驱动读／写指定数量的数据。

定义位置（Definition）：spi.h:1280。

符号定位：[spi_transceive_signal](../hardware/P318_SPI公共接口.md#ga41b8a541257c0d45575fdc4593417edc)。

### `spi_read`

```c
static int spi_read(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *rx_bufs)
```

通过SPI驱动读取指定数量的数据。

定义位置（Definition）：spi.h:1124。

符号定位：[spi_read](../hardware/P318_SPI公共接口.md#ga41f771785a4fa9ca0954125d1e97959e)。

### `spi_transceive_dt`

```c
static int spi_transceive_dt(const struct spi_dt_spec *spec, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

在spi_dt_spec指定的SPI总线上读／写数据。

定义位置（Definition）：spi.h:1098。

符号定位：[spi_transceive_dt](../hardware/P318_SPI公共接口.md#ga52c017066736414b31ff709ddc67c4ff)。

### `spi_transceive_cb`

```c
static int spi_transceive_cb(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, spi_callback_t callback, void *userdata)
```

通过SPI驱动异步读／写指定数量的数据。

定义位置（Definition）：spi.h:1234。

符号定位：[spi_transceive_cb](../hardware/P318_SPI公共接口.md#ga6114e63ca23b82f9be0ac70e372b878b)。

### `SPI_STATS_TRANSFER_ERROR_INC`

```c
#define SPI_STATS_TRANSFER_ERROR_INC(dev_)
```

定义位置（Definition）：spi.h:847。

符号定位：[SPI_STATS_TRANSFER_ERROR_INC](../hardware/P318_SPI公共接口.md#ga6f69e68a79afbbe016aecc515f14de3a)。

### `spi_read_dt`

```c
static int spi_read_dt(const struct spi_dt_spec *spec, const struct spi_buf_set *rx_bufs)
```

从spi_dt_spec指定的SPI总线读取数据。

定义位置（Definition）：spi.h:1143。

符号定位：[spi_read_dt](../hardware/P318_SPI公共接口.md#ga7a1d7ebd37d2861b169c265cb90015bf)。

### `spi_write`

```c
static int spi_write(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs)
```

通过SPI驱动写入指定数量的数据。

定义位置（Definition）：spi.h:1167。

符号定位：[spi_write](../hardware/P318_SPI公共接口.md#ga7e7c4460670ec1c0433ba19accd97796)。

### `spi_release_dt`

```c
static int spi_release_dt(const struct spi_dt_spec *spec)
```

释放spi_dt_spec指定的SPI设备。

定义位置（Definition）：spi.h:1475。

符号定位：[spi_release_dt](../hardware/P318_SPI公共接口.md#ga829b59767c51b20b546eee8a9cc84b69)。

### `spi_iodev_submit`

```c
static void spi_iodev_submit(struct rtio_iodev_sqe *iodev_sqe)
```

向SPI设备提交请求。

定义位置（Definition）：spi.h:1378。

符号定位：[spi_iodev_submit](../hardware/P318_SPI公共接口.md#ga8b23855bdc7dab7d02b8f7daa7db651b)。

### `spi_read_signal`

```c
static int spi_read_signal(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *rx_bufs, struct k_poll_signal *sig)
```

通过SPI驱动读取指定数量的数据。

定义位置（Definition）：spi.h:1316。

符号定位：[spi_read_signal](../hardware/P318_SPI公共接口.md#ga9a1ceadb217368232af5b688c12169c5)。

### `spi_cs_is_gpio_dt`

```c
static bool spi_cs_is_gpio_dt(const struct spi_dt_spec *spec)
```

检查spi_dt_spec中的SPI片选是否通过GPIO控制。

定义位置（Definition）：spi.h:1002。

符号定位：[spi_cs_is_gpio_dt](../hardware/P318_SPI公共接口.md#gaa13f0da1f28cffa0da4677987db0c9c5)。

### `spi_transceive`

```c
int spi_transceive(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

通过SPI驱动读／写指定数量的数据。

符号定位：[spi_transceive](../hardware/P318_SPI公共接口.md#gad51054c1ba259db5a64619788506a6f5)。

### `spi_transceive_stats`

```c
#define spi_transceive_stats(dev, error, tx_bufs, rx_bufs)
```

定义位置（Definition）：spi.h:849。

符号定位：[spi_transceive_stats](../hardware/P318_SPI公共接口.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)。

### `spi_write_signal`

```c
static int spi_write_signal(const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, struct k_poll_signal *sig)
```

通过SPI驱动写入指定数量的数据。

定义位置（Definition）：spi.h:1348。

符号定位：[spi_write_signal](../hardware/P318_SPI公共接口.md#gadcb19d43461ef88e31f6b382cc87fd0b)。

### `spi_cs_is_gpio`

```c
static bool spi_cs_is_gpio(const struct spi_config *config)
```

检查SPI片选是否通过通用输入／输出（General-Purpose Input/Output，GPIO）控制。

定义位置（Definition）：spi.h:990。

符号定位：[spi_cs_is_gpio](../hardware/P318_SPI公共接口.md#gae1156a4ee1b5909c321811045566d888)。

### `spi_is_ready_iodev`

```c
static bool spi_is_ready_iodev(const struct rtio_iodev *spi_iodev)
```

验证SPI总线以及已定义的片选GPIO是否就绪（Ready）。

定义位置（Definition）：spi.h:1426。

符号定位：[spi_is_ready_iodev](../hardware/P318_SPI公共接口.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)。

### `STATS_SECT_END`

```c
#define STATS_SECT_END
```

结束统计组结构定义。

定义位置（Definition）：stats.h:169。

符号定位：[STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)。

### `STATS_NAME`

```c
#define STATS_NAME(sectname__, entry__)
```

向统计条目名称映射添加一个条目名称。

定义位置（Definition）：stats.h:519。

符号定位：[STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)。

### `STATS_SECT_ENTRY32`

```c
#define STATS_SECT_ENTRY32(var__)
```

在统计组结构内声明一个32位统计条目。

定义位置（Definition）：stats.h:204。

符号定位：[STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)。

### `STATS_NAME_START`

```c
#define STATS_NAME_START(sectname__)
```

开始统计条目名称映射。

定义位置（Definition）：stats.h:510。

符号定位：[STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)。

### `STATS_NAME_END`

```c
#define STATS_NAME_END(sectname__)
```

结束统计条目名称映射。

定义位置（Definition）：stats.h:527。

符号定位：[STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)。

### `STATS_SECT_START`

```c
#define STATS_SECT_START(group__)
```

开始统计组结构定义。

定义位置（Definition）：stats.h:181。

符号定位：[STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)。

### `MIN`

```c
#define MIN(a, b)
```

取得两个值中的较小值。

定义位置（Definition）：util.h:406。

符号定位：[MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `kernel.h`

公共内核API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `rtio.h`

以较低开销传送字节的实时I/O设备API（Real-Time I/O）。

符号定位：[rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)。

### `stats.h`

统计信息（Statistics）。

符号定位：[stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)。

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

### `UINT16_MAX`

```c
#define UINT16_MAX
```

定义位置（Definition）：stdint.h:28。

符号定位：[UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `device_state`

每个驱动实例的运行时设备动态结构，位于随机存取存储器（RAM）中。

定义位置（Definition）：device.h:488。

符号定位：[device_state](../device_reference/P003_设备运行状态结构.md)。

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

### `gpio_dt_spec`

保存设备树指定的GPIO引脚信息的容器。

定义位置（Definition）：gpio.h:296。

符号定位：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

### `k_poll_signal`

轮询信号对象（Poll Signal Object）。

定义位置（Definition）：kernel.h:6798。

符号定位：[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

### `rtio_iodev_api`

RTIO的I/O设备应实现的API。

定义位置（Definition）：iodev.h:34。

符号定位：[rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)。

### `rtio_iodev_sqe`

I/O设备提交队列项（Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_iodev_sqe::sqe`

```c
struct rtio_sqe sqe
```

此队列项携带的提交内容。

定义位置（Definition）：sqe.h:404。

符号定位：[rtio_iodev_sqe::sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)。

### `rtio_iodev`

具有请求提交函数表的I/O设备。

定义位置（Definition）：iodev.h:49。

符号定位：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

### `rtio_iodev::data`

```c
void * data
```

与此iodev关联的数据。

定义位置（Definition）：iodev.h:54。

符号定位：[rtio_iodev::data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)。

### `rtio_sqe::iodev`

```c
const struct rtio_iodev * iodev
```

操作所针对的设备。

定义位置（Definition）：sqe.h:319。

符号定位：[rtio_sqe::iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)。

### `spi_buf_set`

SPI分散／聚集（Scatter-Gather）缓冲区数组结构。

定义位置（Definition）：spi.h:679。

符号定位：[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

### `spi_buf_set::buffers`

```c
const struct spi_buf * buffers
```

指向spi_buf数组的指针，或者NULL。

定义位置（Definition）：spi.h:681。

符号定位：[spi_buf_set::buffers](../hardware/P323_SPI缓冲区集合结构.md#a2b88917ca29487b2d0b5b63d2083db67)。

### `spi_buf_set::count`

```c
size_t count
```

buffers所指数组中的缓冲区数量。

定义位置（Definition）：spi.h:683。

符号定位：[spi_buf_set::count](../hardware/P323_SPI缓冲区集合结构.md#abc7c37cffebb7873aaba2e524c9a23dc)。

### `spi_buf`

SPI缓冲区（Buffer）结构。

定义位置（Definition）：spi.h:661。

符号定位：[spi_buf](../hardware/P322_SPI缓冲区结构.md)。

### `spi_buf::len`

```c
size_t len
```

缓冲区buf的字节长度，或者空操作（NOP）的长度。

定义位置（Definition）：spi.h:665。

符号定位：[spi_buf::len](../hardware/P322_SPI缓冲区结构.md#a9755deadff0dd01a886f22e41099b8ba)。

### `spi_buf::buf`

```c
void * buf
```

指向数据缓冲区的有效指针，或者用NULL指示空操作（NOP）。

定义位置（Definition）：spi.h:663。

符号定位：[spi_buf::buf](../hardware/P322_SPI缓冲区结构.md#aeaf52d3ff5af10545b2d6904ed452cba)。

### `spi_config`

SPI控制器（Controller）配置结构。

定义位置（Definition）：spi.h:449。

符号定位：[spi_config](../hardware/P320_SPI控制器配置结构.md)。

### `spi_config::slave`

```c
uint16_t slave
```

外设编号（Peripheral Number）。

定义位置（Definition）：spi.h:481。

符号定位：[spi_config::slave](../hardware/P320_SPI控制器配置结构.md#a020ca853537483b9641c37be70ab6ca0)。

### `spi_config::cs`

```c
struct spi_cs_control cs
```

GPIO片选线；此项可选，不使用时必须初始化为零。

定义位置（Definition）：spi.h:487。

符号定位：[spi_config::cs](../hardware/P320_SPI控制器配置结构.md#a537dbfe323fafedaa219de1be2097dde)。

### `spi_config::operation`

```c
spi_operation_t operation
```

操作标志（Operation Flags）。

定义位置（Definition）：spi.h:472。

符号定位：[spi_config::operation](../hardware/P320_SPI控制器配置结构.md#a71a02ea548e187e6511abf10fdfa4829)。

### `spi_config::frequency`

```c
uint32_t frequency
```

总线频率，单位为赫兹（Hertz，Hz）。

定义位置（Definition）：spi.h:451。

符号定位：[spi_config::frequency](../hardware/P320_SPI控制器配置结构.md#aa1ec6933fe66f91653c5be488e4c9b2a)。

### `spi_config::peripheral`

```c
uint16_t peripheral
```

外设编号（Peripheral Number）。

定义位置（Definition）：spi.h:476。

符号定位：[spi_config::peripheral](../hardware/P320_SPI控制器配置结构.md#ae952e508c8e719098b15edf665c4eb81)。

### `spi_config::word_delay`

```c
uint16_t word_delay
```

在硬件支持的情况下，SCK线上SPI数据字之间的延时，单位为纳秒。

定义位置（Definition）：spi.h:492。

符号定位：[spi_config::word_delay](../hardware/P320_SPI控制器配置结构.md#af55961609841e6f42fb20bf807710a5d)。

### `spi_cs_control`

SPI片选（Chip Select，CS）控制结构。

定义位置（Definition）：spi.h:260。

符号定位：[spi_cs_control](../hardware/P319_SPI片选控制结构.md)。

### `spi_cs_control::delay`

```c
uint32_t delay
```

开始传输之前以及释放片选线之前等待的延时，单位为微秒。

定义位置（Definition）：spi.h:275。

符号定位：[spi_cs_control::delay](../hardware/P319_SPI片选控制结构.md#a04569d78ac7d6022ffee0c28f5d3b629)。

### `spi_cs_control::hold_ns`

```c
uint32_t hold_ns
```

片选使能滞后时间（CS Enable Lag Time），即……（原符号提示在此截断）。

定义位置（Definition）：spi.h:288。

符号定位：[spi_cs_control::hold_ns](../hardware/P319_SPI片选控制结构.md#a5bb1c6185fe550f6cbc20d95bda6abab)。

### `spi_cs_control::cs_is_gpio`

```c
bool cs_is_gpio
```

定义位置（Definition）：spi.h:292。

符号定位：[spi_cs_control::cs_is_gpio](../hardware/P319_SPI片选控制结构.md#a8614da6ccc73ce2a2a457fbd7a0882e2)。

### `spi_cs_control::gpio`

```c
struct gpio_dt_spec gpio
```

片选GPIO的GPIO设备树描述。

定义位置（Definition）：spi.h:270。

符号定位：[spi_cs_control::gpio](../hardware/P319_SPI片选控制结构.md#a8ad907e168666c2ddca77e89f9b9f47f)。

### `spi_cs_control::setup_ns`

```c
uint32_t setup_ns
```

片选使能提前时间（CS Enable Lead Time），即……（原符号提示在此截断）。

定义位置（Definition）：spi.h:282。

符号定位：[spi_cs_control::setup_ns](../hardware/P319_SPI片选控制结构.md#ab3d5a48c9e725070cf72a42365222bff)。

### `spi_driver_api`

驱动操作（Driver Operations）：SPI驱动操作；原提示含有格式标签。

定义位置（Definition）：spi.h:955。

符号定位：[spi_driver_api](../hardware/P325_SPI驱动函数表.md)。

### `spi_driver_api::transceive`

```c
spi_api_io transceive
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：spi.h:959。

符号定位：[spi_driver_api::transceive](../hardware/P325_SPI驱动函数表.md#abeb852d35e4772dcec716cf63ef307bb)。

### `spi_driver_api::release`

```c
spi_api_release release
```

驱动必需操作（Required Operation）：驱动必须实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：spi.h:977。

符号定位：[spi_driver_api::release](../hardware/P325_SPI驱动函数表.md#ae15944912ece9f736fd935184e8a184d)。

### `spi_driver_api::transceive_async`

```c
spi_api_io_async transceive_async
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：spi.h:965。

符号定位：[spi_driver_api::transceive_async](../hardware/P325_SPI驱动函数表.md#af067daa58e79b9067a59fedcfd61034b)。

### `spi_driver_api::iodev_submit`

```c
spi_api_iodev_submit iodev_submit
```

驱动可选操作（Optional Operation）：驱动可以选择实现此操作……（原符号提示中的标签文本在此截断）。

定义位置（Definition）：spi.h:972。

符号定位：[spi_driver_api::iodev_submit](../hardware/P325_SPI驱动函数表.md#af88a1a6b823d5742b099170eb3b2e38a)。

### `spi_dt_spec`

完整的SPI设备树（Devicetree，DT）信息。

定义位置（Definition）：spi.h:560。

符号定位：[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)。

### `spi_dt_spec::bus`

```c
const struct device * bus
```

SPI总线（Bus）。

定义位置（Definition）：spi.h:562。

符号定位：[spi_dt_spec::bus](../hardware/P321_SPI设备树描述结构.md#a37519633ae787ffaa1026e6867d7007a)。

### `spi_dt_spec::config`

```c
struct spi_config config
```

特定外设的配置。

定义位置（Definition）：spi.h:564。

符号定位：[spi_dt_spec::config](../hardware/P321_SPI设备树描述结构.md#a88372c17ede2e9dfb0c09c49abebf87e)。

## 2.4\_源码跟踪译注

> 译注——操作位与类型：SPI_OP_MODE_CONTROLLER为0，PERIPHERAL占位0；旧MASTER／SLAVE名称为弃用别名（Deprecated Alias）。SPI_MODE_MASK为0xE，实际同时包含CPOL、CPHA和LOOP，不能只按摘要措辞理解为极性与相位。SPI_WORD_SIZE_GET取出位5至10的6位字段，SPI_WORD_SET仅左移，不做取值范围检查。多线选择位于位16至17，spi_operation_t在CONFIG_SPI_EXTENDED_MODES启用时为uint32_t，否则为uint16_t；类型和标志存在不表示具体驱动具备相应硬件能力。

> 译注——片选初始化形式：原文将SPI_CS_CONTROL_INIT及其实例版描述为“取得指针”，但本次读取的实现展开为花括号结构初始化器（Structure Initializer），并非指针表达式；spi_config.cs也按值保存结构。cs_is_gpio区分GPIO与原生片选（Native Chip Select）的联合体分支。GPIO分支把setup与hold纳秒延时的较大值向上取整转换为微秒delay，原生分支分别保留setup_ns与hold_ns，不能混用字段或单位。

> 译注——字间延时：word_delay非零时直接返回其纳秒数；为零且frequency非零时，以整数除法计算1秒纳秒数除以频率，先将整个周期限制到UINT16_MAX，再除以2。因此结果是经上述限幅与截断后的半周期，最大32767纳秒；frequency为零则返回0。原注释写作“频率的一半（half of the frequency）”，代码与绑定定义对应的是周期的一半（Half Period），这里保留原注释并明确单位差异。

> 译注——设备树配置与就绪：SPI_CONFIG_DT把调用方operation_与duplex、frame-format、极性、相位、位序、保持片选及片选高有效属性按位或（Bitwise OR）合并；值为0的参数不能清除其他来源已置位的选项。spi_is_ready_dt只检查总线设备以及确实采用GPIO片选时的GPIO端口是否就绪，并不向外设发送探测事务。SPI_SDO_OVERRUN_UNKNOWN为0x100，是无法与有效8位填充值相等的哨兵值（Sentinel）。

> 译注——同步、异步与对象生存期：spi_read／spi_write通过spi_transceive分别传入空TX／RX集合；设备树包装传递同一配置的地址。异步函数启动传输后通过回调或信号报告完成，但总线忙时启动调用本身仍可能阻塞。配置、缓冲区描述符、数据及用户上下文应保持有效至相关操作完成，不能把提交返回当作完成。当前回调和信号包装直接调用transceive_async，不检查空函数指针；信号参数为NULL时不提供完成通知。配置选项SPI_ASYNC依赖多线程并选择POLL，网页中的__DOXYGEN__分支不意味着固件已启用这些能力。

> 译注——片选保持与总线锁：SPI_HOLD_ON_CS请求在支持且可行时保持片选，SPI_LOCK_ON保留软件所有权，二者不是同一个状态。锁的身份使用传入的spi_config指针，继续事务或调用spi_release时要使用相同配置对象，不能仅复制相同字段后换一个地址。原始主头文件建议通过RTIO提交路径串联异步事务，避免从可能位于中断服务程序（Interrupt Service Routine，ISR）上下文的完成回调重新进入transceive。

> 译注——RTIO提交边界：当前spi_iodev_submit直接调用设备API中的iodev_submit，不在此包装中检查NULL或自动选择回退（Fallback）。官方spi_rtio.c另有默认提交函数，将工作交给RTIO工作队列并转换为同步spi_transceive_dt调用；实际采用哪个入口取决于驱动函数表。默认处理支持RX、TX、TINY_TX与TXRX，事务中的提交数量超过CONFIG_SPI_RTIO_FALLBACK_MSGS时报告-ENOMEM，工作请求分配失败也报告-ENOMEM。不能把存在默认实现等同于任意驱动自动支持RTIO。

> 译注——统计范围：当前spi_transceive_stats在error非零时增加错误计数，并在每个非空TX／RX集合的count非零时只取第一个缓冲区的len，没有遍历数组求和；无论成功与否都会执行这些长度计数。因此它既不是完整分散／聚集请求的字节总量，也不是实际成功传输字节数。回调和信号包装没有经过这一同步统计调用；具体驱动若有额外统计需另行核对。

> 译注——版本边界：本批核对主头文件、SPI绑定常量、设备树SPI宏、RTIO实现、Kconfig与两个公共绑定，共七份官方源码并记录摘要。源码页非注释代码与读取的官方主头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接总线、收发数据或操作硬件。

头文件相对定位：[include/zephyr/drivers/spi.h](../../../include/zephyr/drivers/spi.h)，关联实现／接口：[drivers/spi/spi_rtio.c](../../../drivers/spi/spi_rtio.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/spi.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_rtio.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、连接SPI总线、收发数据或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_SPI驱动头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/dt-bindings/spi/spi.h](../dt_bus_binding_reference/P003_SPI绑定常量头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)
- [spi_cs_control](../hardware/P319_SPI片选控制结构.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [gpio](../hardware/P319_SPI片选控制结构.md#a8ad907e168666c2ddca77e89f9b9f47f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [delay](../hardware/P319_SPI片选控制结构.md#a04569d78ac7d6022ffee0c28f5d3b629)
- [setup_ns](../hardware/P319_SPI片选控制结构.md#ab3d5a48c9e725070cf72a42365222bff)
- [hold_ns](../hardware/P319_SPI片选控制结构.md#a5bb1c6185fe550f6cbc20d95bda6abab)
- [cs_is_gpio](../hardware/P319_SPI片选控制结构.md#a8614da6ccc73ce2a2a457fbd7a0882e2)
- [spi_operation_t](../hardware/P318_SPI公共接口.md#ga398a8ae1c4799e77fb6c067b6d47294a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [spi_config](../hardware/P320_SPI控制器配置结构.md)
- [frequency](../hardware/P320_SPI控制器配置结构.md#aa1ec6933fe66f91653c5be488e4c9b2a)
- [operation](../hardware/P320_SPI控制器配置结构.md#a71a02ea548e187e6511abf10fdfa4829)
- [peripheral](../hardware/P320_SPI控制器配置结构.md#ae952e508c8e719098b15edf665c4eb81)
- [slave](../hardware/P320_SPI控制器配置结构.md#a020ca853537483b9641c37be70ab6ca0)
- [cs](../hardware/P320_SPI控制器配置结构.md#a537dbfe323fafedaa219de1be2097dde)
- [word_delay](../hardware/P320_SPI控制器配置结构.md#af55961609841e6f42fb20bf807710a5d)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)
- [spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bus](../hardware/P321_SPI设备树描述结构.md#a37519633ae787ffaa1026e6867d7007a)
- [config](../hardware/P321_SPI设备树描述结构.md#a88372c17ede2e9dfb0c09c49abebf87e)
- [spi_buf](../hardware/P322_SPI缓冲区结构.md)
- [buf](../hardware/P322_SPI缓冲区结构.md#aeaf52d3ff5af10545b2d6904ed452cba)
- [len](../hardware/P322_SPI缓冲区结构.md#a9755deadff0dd01a886f22e41099b8ba)
- [spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)
- [buffers](../hardware/P323_SPI缓冲区集合结构.md#a2b88917ca29487b2d0b5b63d2083db67)
- [count](../hardware/P323_SPI缓冲区集合结构.md#abc7c37cffebb7873aaba2e524c9a23dc)
- [STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)
- [STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)
- [STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)
- [STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)
- [STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)
- [STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)
- [device_state](../device_reference/P003_设备运行状态结构.md)
- [spi_transceive_stats](../hardware/P318_SPI公共接口.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)
- [SPI_STATS_TRANSFER_ERROR_INC](../hardware/P318_SPI公共接口.md#ga6f69e68a79afbbe016aecc515f14de3a)
- [spi_api_io](../hardware/P324_SPI驱动后端接口.md#ga3fc669f866b03cfdad98754de69cda13)
- [spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [spi_api_io_async](../hardware/P324_SPI驱动后端接口.md#ga03be7f33032ac479153616bbe26848e7)
- [spi_api_iodev_submit](../hardware/P324_SPI驱动后端接口.md#gae274c0d704e8fd8993631fc1b91bfcb1)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [spi_api_release](../hardware/P324_SPI驱动后端接口.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)
- [spi_driver_api](../hardware/P325_SPI驱动函数表.md)
- [transceive](../hardware/P325_SPI驱动函数表.md#abeb852d35e4772dcec716cf63ef307bb)
- [transceive_async](../hardware/P325_SPI驱动函数表.md#af067daa58e79b9067a59fedcfd61034b)
- [iodev_submit](../hardware/P325_SPI驱动函数表.md#af88a1a6b823d5742b099170eb3b2e38a)
- [release](../hardware/P325_SPI驱动函数表.md#ae15944912ece9f736fd935184e8a184d)
- [spi_cs_is_gpio](../hardware/P318_SPI公共接口.md#gae1156a4ee1b5909c321811045566d888)
- [spi_cs_is_gpio_dt](../hardware/P318_SPI公共接口.md#gaa13f0da1f28cffa0da4677987db0c9c5)
- [spi_is_ready_dt](../hardware/P318_SPI公共接口.md#ga37b4e5079ed18b70b0c5a260f4c36403)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [gpio_is_ready_dt](../hardware/P266_GPIO公共接口.md#gaaec9ad17c08a0d527d66445fe82d8327)
- [spi_transceive](../hardware/P318_SPI公共接口.md#gad51054c1ba259db5a64619788506a6f5)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [spi_transceive_dt](../hardware/P318_SPI公共接口.md#ga52c017066736414b31ff709ddc67c4ff)
- [spi_read](../hardware/P318_SPI公共接口.md#ga41f771785a4fa9ca0954125d1e97959e)
- [spi_read_dt](../hardware/P318_SPI公共接口.md#ga7a1d7ebd37d2861b169c265cb90015bf)
- [spi_write](../hardware/P318_SPI公共接口.md#ga7e7c4460670ec1c0433ba19accd97796)
- [spi_write_dt](../hardware/P318_SPI公共接口.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)
- [spi_transceive_cb](../hardware/P318_SPI公共接口.md#ga6114e63ca23b82f9be0ac70e372b878b)
- [spi_transceive_signal](../hardware/P318_SPI公共接口.md#ga41b8a541257c0d45575fdc4593417edc)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [spi_read_signal](../hardware/P318_SPI公共接口.md#ga9a1ceadb217368232af5b688c12169c5)
- [spi_write_signal](../hardware/P318_SPI公共接口.md#gadcb19d43461ef88e31f6b382cc87fd0b)
- [spi_iodev_submit](../hardware/P318_SPI公共接口.md#ga8b23855bdc7dab7d02b8f7daa7db651b)
- [sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)
- [iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)
- [data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [spi_is_ready_iodev](../hardware/P318_SPI公共接口.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [spi_release](../hardware/P318_SPI公共接口.md#ga0c4f4f0a93bb83a4f58d551a7491164e)
- [spi_release_dt](../hardware/P318_SPI公共接口.md#ga829b59767c51b20b546eee8a9cc84b69)

---

[上一章](P001_SPI驱动头文件参考.md) · [返回大纲](大纲.md)
