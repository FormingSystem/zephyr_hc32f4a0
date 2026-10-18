---
id: learning.zephyr-docs.uart-driver-reference.page-4
title: UART内部头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__internal_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_UART内部头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__internal_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_UART内部头文件参考.md)和[公共API](../hardware/P330_UART公共接口.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__uart__async_html_ga00b7c98a4da3ea3675d0a40c5dacb136"></a>
<a id="agroup__uart__async_html_ga3970fe2818e214b0814ea8b73a816a6a"></a>
<a id="agroup__uart__async_html_ga778bcfc30be853c8d320f295b34c17c0"></a>
<a id="agroup__uart__async_html_gad33e627ed8729409b14e92453e53459c"></a>
<a id="agroup__uart__interrupt_html_ga20cf50f53fb9e09e760c6499fd156ff2"></a>
<a id="agroup__uart__interrupt_html_ga4a3c25dad2290f1f40e4b847e3b83f64"></a>
<a id="agroup__uart__interrupt_html_ga5e126b5f19549eb7f5b785b98ebe7638"></a>
<a id="agroup__uart__interrupt_html_ga5f7af3f7f0d9155349ea3b4fad78956c"></a>
<a id="agroup__uart__interrupt_html_ga917935a13bf6a5d1e32ef34339e96455"></a>
<a id="agroup__uart__interrupt_html_gaa89f58818d8428ad6a11abf692c54c0d"></a>
<a id="agroup__uart__interrupt_html_gab10942076ac47ecff29e924098049398"></a>
<a id="agroup__uart__interrupt_html_gacd8c2978e0f1316dd79bb42baad1c5a7"></a>
<a id="agroup__uart__interrupt_html_gad04073b1b8e3de13b43ae1194561377b"></a>
<a id="agroup__uart__interrupt_html_gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>
<a id="agroup__uart__interrupt_html_gaf469966a56d1fc9f50108201597ee0a0"></a>
<a id="agroup__uart__interrupt_html_gafe42e4719eada7e25904bc9ebfe87791"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructuart__config_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018-2019 Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2015 Wind River Systems, Inc.
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_UART_UART_INTERNAL_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_DRIVERS_UART_UART_INTERNAL_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;errno.h&gt;
<a id="l00017"></a>#include &lt;stddef.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;zephyr/device.h&gt;
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00027"></a>#ifdef __cplusplus
<a id="l00028"></a>extern "C" {
<a id="l00029"></a>#endif
<a id="l00030"></a>
<a id="l00036"></a>typedef void (*uart_irq_config_func_t)(const struct device *dev);
<a id="l00037"></a>
<a id="l00039"></a>__subsystem struct uart_driver_api {
<a id="l00040"></a>
<a id="l00041"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00042"></a>
<a id="l00043"></a>        int (*callback_set)(const struct device *dev, uart_callback_t callback, void *user_data);
<a id="l00044"></a>
<a id="l00045"></a>        int (*tx)(const struct device *dev, const uint8_t *buf, size_t len, int32_t timeout);
<a id="l00046"></a>        int (*tx_abort)(const struct device *dev);
<a id="l00047"></a>
<a id="l00048"></a>        int (*rx_enable)(const struct device *dev, uint8_t *buf, size_t len, int32_t timeout);
<a id="l00049"></a>        int (*rx_buf_rsp)(const struct device *dev, uint8_t *buf, size_t len);
<a id="l00050"></a>        int (*rx_disable)(const struct device *dev);
<a id="l00051"></a>
<a id="l00052"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00053"></a>        int (*tx_u16)(const struct device *dev, const uint16_t *buf, size_t len, int32_t timeout);
<a id="l00054"></a>        int (*rx_enable_u16)(const struct device *dev, uint16_t *buf, size_t len, int32_t timeout);
<a id="l00055"></a>        int (*rx_buf_rsp_u16)(const struct device *dev, uint16_t *buf, size_t len);
<a id="l00056"></a>#endif
<a id="l00057"></a>
<a id="l00058"></a>#endif
<a id="l00059"></a>
<a id="l00061"></a>        int (*poll_in)(const struct device *dev, unsigned char *p_char);
<a id="l00062"></a>        void (*poll_out)(const struct device *dev, unsigned char out_char);
<a id="l00063"></a>
<a id="l00064"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00065"></a>        int (*poll_in_u16)(const struct device *dev, uint16_t *p_u16);
<a id="l00066"></a>        void (*poll_out_u16)(const struct device *dev, uint16_t out_u16);
<a id="l00067"></a>#endif
<a id="l00068"></a>
<a id="l00070"></a>        int (*err_check)(const struct device *dev);
<a id="l00071"></a>
<a id="l00072"></a>#ifdef CONFIG_UART_USE_RUNTIME_CONFIGURE
<a id="l00074"></a>        int (*configure)(const struct device *dev, const struct uart_config *cfg);
<a id="l00075"></a>        int (*config_get)(const struct device *dev, struct uart_config *cfg);
<a id="l00076"></a>#endif
<a id="l00077"></a>
<a id="l00078"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00079"></a>
<a id="l00081"></a>        int (*fifo_fill)(const struct device *dev, const uint8_t *tx_data, int len);
<a id="l00082"></a>
<a id="l00083"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00084"></a>        int (*fifo_fill_u16)(const struct device *dev, const uint16_t *tx_data, int len);
<a id="l00085"></a>#endif
<a id="l00086"></a>
<a id="l00088"></a>        int (*fifo_read)(const struct device *dev, uint8_t *rx_data, const int size);
<a id="l00089"></a>
<a id="l00090"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00091"></a>        int (*fifo_read_u16)(const struct device *dev, uint16_t *rx_data, const int size);
<a id="l00092"></a>#endif
<a id="l00093"></a>
<a id="l00095"></a>        void (*irq_tx_enable)(const struct device *dev);
<a id="l00096"></a>
<a id="l00098"></a>        void (*irq_tx_disable)(const struct device *dev);
<a id="l00099"></a>
<a id="l00101"></a>        int (*irq_tx_ready)(const struct device *dev);
<a id="l00102"></a>
<a id="l00104"></a>        void (*irq_rx_enable)(const struct device *dev);
<a id="l00105"></a>
<a id="l00107"></a>        void (*irq_rx_disable)(const struct device *dev);
<a id="l00108"></a>
<a id="l00110"></a>        int (*irq_tx_complete)(const struct device *dev);
<a id="l00111"></a>
<a id="l00113"></a>        int (*irq_rx_ready)(const struct device *dev);
<a id="l00114"></a>
<a id="l00116"></a>        void (*irq_err_enable)(const struct device *dev);
<a id="l00117"></a>
<a id="l00119"></a>        void (*irq_err_disable)(const struct device *dev);
<a id="l00120"></a>
<a id="l00122"></a>        int (*irq_is_pending)(const struct device *dev);
<a id="l00123"></a>
<a id="l00125"></a>        void (*irq_update)(const struct device *dev);
<a id="l00126"></a>
<a id="l00128"></a>        void (*irq_callback_set)(const struct device *dev, uart_irq_callback_user_data_t cb,
<a id="l00129"></a>                                 void *user_data);
<a id="l00130"></a>
<a id="l00131"></a>#endif /* CONFIG_UART_INTERRUPT_DRIVEN */
<a id="l00132"></a>
<a id="l00133"></a>#ifdef CONFIG_UART_LINE_CTRL
<a id="l00134"></a>        int (*line_ctrl_set)(const struct device *dev, uint32_t ctrl, uint32_t val);
<a id="l00135"></a>        int (*line_ctrl_get)(const struct device *dev, uint32_t ctrl, uint32_t *val);
<a id="l00136"></a>#endif
<a id="l00137"></a>
<a id="l00138"></a>#ifdef CONFIG_UART_DRV_CMD
<a id="l00139"></a>        int (*drv_cmd)(const struct device *dev, uint32_t cmd, uint32_t p);
<a id="l00140"></a>#endif
<a id="l00141"></a>};
<a id="l00142"></a>
<a id="l00143"></a>static inline int z_impl_uart_err_check(const struct device *dev)
<a id="l00144"></a>{
<a id="l00145"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00146"></a>
<a id="l00147"></a>        if (api-&gt;err_check == NULL) {
<a id="l00148"></a>                return -ENOSYS;
<a id="l00149"></a>        }
<a id="l00150"></a>
<a id="l00151"></a>        return api-&gt;err_check(dev);
<a id="l00152"></a>}
<a id="l00153"></a>
<a id="l00154"></a>static inline int z_impl_uart_poll_in(const struct device *dev, unsigned char *p_char)
<a id="l00155"></a>{
<a id="l00156"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00157"></a>
<a id="l00158"></a>        if (api-&gt;poll_in == NULL) {
<a id="l00159"></a>                return -ENOSYS;
<a id="l00160"></a>        }
<a id="l00161"></a>
<a id="l00162"></a>        return api-&gt;poll_in(dev, p_char);
<a id="l00163"></a>}
<a id="l00164"></a>
<a id="l00165"></a>static inline int z_impl_uart_poll_in_u16(const struct device *dev, uint16_t *p_u16)
<a id="l00166"></a>{
<a id="l00167"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00168"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00169"></a>
<a id="l00170"></a>        if (api-&gt;poll_in_u16 == NULL) {
<a id="l00171"></a>                return -ENOSYS;
<a id="l00172"></a>        }
<a id="l00173"></a>
<a id="l00174"></a>        return api-&gt;poll_in_u16(dev, p_u16);
<a id="l00175"></a>#else
<a id="l00176"></a>        ARG_UNUSED(dev);
<a id="l00177"></a>        ARG_UNUSED(p_u16);
<a id="l00178"></a>        return -ENOTSUP;
<a id="l00179"></a>#endif
<a id="l00180"></a>}
<a id="l00181"></a>
<a id="l00182"></a>static inline void z_impl_uart_poll_out(const struct device *dev, unsigned char out_char)
<a id="l00183"></a>{
<a id="l00184"></a>        DEVICE_API_GET(uart, dev)-&gt;poll_out(dev, out_char);
<a id="l00185"></a>}
<a id="l00186"></a>
<a id="l00187"></a>static inline void z_impl_uart_poll_out_u16(const struct device *dev, uint16_t out_u16)
<a id="l00188"></a>{
<a id="l00189"></a>#ifdef CONFIG_UART_WIDE_DATA
<a id="l00190"></a>        DEVICE_API_GET(uart, dev)-&gt;poll_out_u16(dev, out_u16);
<a id="l00191"></a>#else
<a id="l00192"></a>        ARG_UNUSED(dev);
<a id="l00193"></a>        ARG_UNUSED(out_u16);
<a id="l00194"></a>#endif
<a id="l00195"></a>}
<a id="l00196"></a>
<a id="l00197"></a>static inline int z_impl_uart_configure(const struct device *dev, const struct uart_config *cfg)
<a id="l00198"></a>{
<a id="l00199"></a>#ifdef CONFIG_UART_USE_RUNTIME_CONFIGURE
<a id="l00200"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00201"></a>
<a id="l00202"></a>        if (api-&gt;configure == NULL) {
<a id="l00203"></a>                return -ENOSYS;
<a id="l00204"></a>        }
<a id="l00205"></a>        return api-&gt;configure(dev, cfg);
<a id="l00206"></a>#else
<a id="l00207"></a>        ARG_UNUSED(dev);
<a id="l00208"></a>        ARG_UNUSED(cfg);
<a id="l00209"></a>        return -ENOTSUP;
<a id="l00210"></a>#endif
<a id="l00211"></a>}
<a id="l00212"></a>
<a id="l00213"></a>static inline int z_impl_uart_config_get(const struct device *dev, struct uart_config *cfg)
<a id="l00214"></a>{
<a id="l00215"></a>#ifdef CONFIG_UART_USE_RUNTIME_CONFIGURE
<a id="l00216"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00217"></a>
<a id="l00218"></a>        if (api-&gt;config_get == NULL) {
<a id="l00219"></a>                return -ENOSYS;
<a id="l00220"></a>        }
<a id="l00221"></a>
<a id="l00222"></a>        return api-&gt;config_get(dev, cfg);
<a id="l00223"></a>#else
<a id="l00224"></a>        ARG_UNUSED(dev);
<a id="l00225"></a>        ARG_UNUSED(cfg);
<a id="l00226"></a>        return -ENOTSUP;
<a id="l00227"></a>#endif
<a id="l00228"></a>}
<a id="l00229"></a>
<a id="l00230"></a>static inline int uart_fifo_fill(const struct device *dev, const uint8_t *tx_data, int size)
<a id="l00231"></a>{
<a id="l00232"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00233"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00234"></a>
<a id="l00235"></a>        if (api-&gt;fifo_fill == NULL) {
<a id="l00236"></a>                return -ENOSYS;
<a id="l00237"></a>        }
<a id="l00238"></a>
<a id="l00239"></a>        return api-&gt;fifo_fill(dev, tx_data, size);
<a id="l00240"></a>#else
<a id="l00241"></a>        ARG_UNUSED(dev);
<a id="l00242"></a>        ARG_UNUSED(tx_data);
<a id="l00243"></a>        ARG_UNUSED(size);
<a id="l00244"></a>        return -ENOTSUP;
<a id="l00245"></a>#endif
<a id="l00246"></a>}
<a id="l00247"></a>
<a id="l00248"></a>static inline int uart_fifo_fill_u16(const struct device *dev, const uint16_t *tx_data, int size)
<a id="l00249"></a>{
<a id="l00250"></a>#if defined(CONFIG_UART_INTERRUPT_DRIVEN) &amp;&amp; defined(CONFIG_UART_WIDE_DATA)
<a id="l00251"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00252"></a>
<a id="l00253"></a>        if (api-&gt;fifo_fill_u16 == NULL) {
<a id="l00254"></a>                return -ENOSYS;
<a id="l00255"></a>        }
<a id="l00256"></a>
<a id="l00257"></a>        return api-&gt;fifo_fill_u16(dev, tx_data, size);
<a id="l00258"></a>#else
<a id="l00259"></a>        ARG_UNUSED(dev);
<a id="l00260"></a>        ARG_UNUSED(tx_data);
<a id="l00261"></a>        ARG_UNUSED(size);
<a id="l00262"></a>        return -ENOTSUP;
<a id="l00263"></a>#endif
<a id="l00264"></a>}
<a id="l00265"></a>
<a id="l00266"></a>static inline int uart_fifo_read(const struct device *dev, uint8_t *rx_data, const int size)
<a id="l00267"></a>{
<a id="l00268"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00269"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00270"></a>
<a id="l00271"></a>        if (api-&gt;fifo_read == NULL) {
<a id="l00272"></a>                return -ENOSYS;
<a id="l00273"></a>        }
<a id="l00274"></a>
<a id="l00275"></a>        return api-&gt;fifo_read(dev, rx_data, size);
<a id="l00276"></a>#else
<a id="l00277"></a>        ARG_UNUSED(dev);
<a id="l00278"></a>        ARG_UNUSED(rx_data);
<a id="l00279"></a>        ARG_UNUSED(size);
<a id="l00280"></a>        return -ENOTSUP;
<a id="l00281"></a>#endif
<a id="l00282"></a>}
<a id="l00283"></a>
<a id="l00284"></a>static inline int uart_fifo_read_u16(const struct device *dev, uint16_t *rx_data, const int size)
<a id="l00285"></a>{
<a id="l00286"></a>#if defined(CONFIG_UART_INTERRUPT_DRIVEN) &amp;&amp; defined(CONFIG_UART_WIDE_DATA)
<a id="l00287"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00288"></a>
<a id="l00289"></a>        if (api-&gt;fifo_read_u16 == NULL) {
<a id="l00290"></a>                return -ENOSYS;
<a id="l00291"></a>        }
<a id="l00292"></a>
<a id="l00293"></a>        return api-&gt;fifo_read_u16(dev, rx_data, size);
<a id="l00294"></a>#else
<a id="l00295"></a>        ARG_UNUSED(dev);
<a id="l00296"></a>        ARG_UNUSED(rx_data);
<a id="l00297"></a>        ARG_UNUSED(size);
<a id="l00298"></a>        return -ENOTSUP;
<a id="l00299"></a>#endif
<a id="l00300"></a>}
<a id="l00301"></a>
<a id="l00302"></a>static inline void z_impl_uart_irq_tx_enable(const struct device *dev)
<a id="l00303"></a>{
<a id="l00304"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00305"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00306"></a>
<a id="l00307"></a>        if (api-&gt;irq_tx_enable != NULL) {
<a id="l00308"></a>                api-&gt;irq_tx_enable(dev);
<a id="l00309"></a>        }
<a id="l00310"></a>#else
<a id="l00311"></a>        ARG_UNUSED(dev);
<a id="l00312"></a>#endif
<a id="l00313"></a>}
<a id="l00314"></a>
<a id="l00315"></a>static inline void z_impl_uart_irq_tx_disable(const struct device *dev)
<a id="l00316"></a>{
<a id="l00317"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00318"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00319"></a>
<a id="l00320"></a>        if (api-&gt;irq_tx_disable != NULL) {
<a id="l00321"></a>                api-&gt;irq_tx_disable(dev);
<a id="l00322"></a>        }
<a id="l00323"></a>#else
<a id="l00324"></a>        ARG_UNUSED(dev);
<a id="l00325"></a>#endif
<a id="l00326"></a>}
<a id="l00327"></a>
<a id="l00328"></a>static inline int uart_irq_tx_ready(const struct device *dev)
<a id="l00329"></a>{
<a id="l00330"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00331"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00332"></a>
<a id="l00333"></a>        if (api-&gt;irq_tx_ready == NULL) {
<a id="l00334"></a>                return -ENOSYS;
<a id="l00335"></a>        }
<a id="l00336"></a>
<a id="l00337"></a>        return api-&gt;irq_tx_ready(dev);
<a id="l00338"></a>#else
<a id="l00339"></a>        ARG_UNUSED(dev);
<a id="l00340"></a>        return -ENOTSUP;
<a id="l00341"></a>#endif
<a id="l00342"></a>}
<a id="l00343"></a>
<a id="l00344"></a>static inline void z_impl_uart_irq_rx_enable(const struct device *dev)
<a id="l00345"></a>{
<a id="l00346"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00347"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00348"></a>
<a id="l00349"></a>        if (api-&gt;irq_rx_enable != NULL) {
<a id="l00350"></a>                api-&gt;irq_rx_enable(dev);
<a id="l00351"></a>        }
<a id="l00352"></a>#else
<a id="l00353"></a>        ARG_UNUSED(dev);
<a id="l00354"></a>#endif
<a id="l00355"></a>}
<a id="l00356"></a>
<a id="l00357"></a>static inline void z_impl_uart_irq_rx_disable(const struct device *dev)
<a id="l00358"></a>{
<a id="l00359"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00360"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00361"></a>
<a id="l00362"></a>        if (api-&gt;irq_rx_disable != NULL) {
<a id="l00363"></a>                api-&gt;irq_rx_disable(dev);
<a id="l00364"></a>        }
<a id="l00365"></a>#else
<a id="l00366"></a>        ARG_UNUSED(dev);
<a id="l00367"></a>#endif
<a id="l00368"></a>}
<a id="l00369"></a>
<a id="l00370"></a>static inline int uart_irq_tx_complete(const struct device *dev)
<a id="l00371"></a>{
<a id="l00372"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00373"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00374"></a>
<a id="l00375"></a>        if (api-&gt;irq_tx_complete == NULL) {
<a id="l00376"></a>                return -ENOSYS;
<a id="l00377"></a>        }
<a id="l00378"></a>        return api-&gt;irq_tx_complete(dev);
<a id="l00379"></a>#else
<a id="l00380"></a>        ARG_UNUSED(dev);
<a id="l00381"></a>        return -ENOTSUP;
<a id="l00382"></a>#endif
<a id="l00383"></a>}
<a id="l00384"></a>
<a id="l00385"></a>static inline int uart_irq_rx_ready(const struct device *dev)
<a id="l00386"></a>{
<a id="l00387"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00388"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00389"></a>
<a id="l00390"></a>        if (api-&gt;irq_rx_ready == NULL) {
<a id="l00391"></a>                return -ENOSYS;
<a id="l00392"></a>        }
<a id="l00393"></a>        return api-&gt;irq_rx_ready(dev);
<a id="l00394"></a>#else
<a id="l00395"></a>        ARG_UNUSED(dev);
<a id="l00396"></a>        return -ENOTSUP;
<a id="l00397"></a>#endif
<a id="l00398"></a>}
<a id="l00399"></a>
<a id="l00400"></a>static inline void z_impl_uart_irq_err_enable(const struct device *dev)
<a id="l00401"></a>{
<a id="l00402"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00403"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00404"></a>
<a id="l00405"></a>        if (api-&gt;irq_err_enable) {
<a id="l00406"></a>                api-&gt;irq_err_enable(dev);
<a id="l00407"></a>        }
<a id="l00408"></a>#else
<a id="l00409"></a>        ARG_UNUSED(dev);
<a id="l00410"></a>#endif
<a id="l00411"></a>}
<a id="l00412"></a>
<a id="l00413"></a>static inline void z_impl_uart_irq_err_disable(const struct device *dev)
<a id="l00414"></a>{
<a id="l00415"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00416"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00417"></a>
<a id="l00418"></a>        if (api-&gt;irq_err_disable) {
<a id="l00419"></a>                api-&gt;irq_err_disable(dev);
<a id="l00420"></a>        }
<a id="l00421"></a>#else
<a id="l00422"></a>        ARG_UNUSED(dev);
<a id="l00423"></a>#endif
<a id="l00424"></a>}
<a id="l00425"></a>
<a id="l00426"></a>static inline int uart_irq_is_pending(const struct device *dev)
<a id="l00427"></a>{
<a id="l00428"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00429"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00430"></a>
<a id="l00431"></a>        if (api-&gt;irq_is_pending == NULL) {
<a id="l00432"></a>                return -ENOSYS;
<a id="l00433"></a>        }
<a id="l00434"></a>        return api-&gt;irq_is_pending(dev);
<a id="l00435"></a>#else
<a id="l00436"></a>        ARG_UNUSED(dev);
<a id="l00437"></a>        return -ENOTSUP;
<a id="l00438"></a>#endif
<a id="l00439"></a>}
<a id="l00440"></a>
<a id="l00441"></a>static inline void uart_irq_update(const struct device *dev)
<a id="l00442"></a>{
<a id="l00443"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00444"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00445"></a>
<a id="l00446"></a>        if (api-&gt;irq_update != NULL) {
<a id="l00447"></a>                api-&gt;irq_update(dev);
<a id="l00448"></a>        }
<a id="l00449"></a>#endif
<a id="l00450"></a>        ARG_UNUSED(dev);
<a id="l00451"></a>}
<a id="l00452"></a>
<a id="l00453"></a>static inline int uart_irq_callback_user_data_set(const struct device *dev,
<a id="l00454"></a>                                                  uart_irq_callback_user_data_t cb, void *user_data)
<a id="l00455"></a>{
<a id="l00456"></a>#ifdef CONFIG_UART_INTERRUPT_DRIVEN
<a id="l00457"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00458"></a>
<a id="l00459"></a>        if ((api != NULL) &amp;&amp; (api-&gt;irq_callback_set != NULL)) {
<a id="l00460"></a>                api-&gt;irq_callback_set(dev, cb, user_data);
<a id="l00461"></a>                return 0;
<a id="l00462"></a>        } else {
<a id="l00463"></a>                return -ENOSYS;
<a id="l00464"></a>        }
<a id="l00465"></a>#else
<a id="l00466"></a>        ARG_UNUSED(dev);
<a id="l00467"></a>        ARG_UNUSED(cb);
<a id="l00468"></a>        ARG_UNUSED(user_data);
<a id="l00469"></a>        return -ENOTSUP;
<a id="l00470"></a>#endif
<a id="l00471"></a>}
<a id="l00472"></a>
<a id="l00473"></a>static inline int uart_irq_callback_set(const struct device *dev, uart_irq_callback_user_data_t cb)
<a id="l00474"></a>{
<a id="l00475"></a>        return uart_irq_callback_user_data_set(dev, cb, NULL);
<a id="l00476"></a>}
<a id="l00477"></a>
<a id="l00478"></a>static inline int uart_callback_set(const struct device *dev, uart_callback_t callback,
<a id="l00479"></a>                                    void *user_data)
<a id="l00480"></a>{
<a id="l00481"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00482"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00483"></a>
<a id="l00484"></a>        if (api-&gt;callback_set == NULL) {
<a id="l00485"></a>                return -ENOSYS;
<a id="l00486"></a>        }
<a id="l00487"></a>
<a id="l00488"></a>        return api-&gt;callback_set(dev, callback, user_data);
<a id="l00489"></a>#else
<a id="l00490"></a>        ARG_UNUSED(dev);
<a id="l00491"></a>        ARG_UNUSED(callback);
<a id="l00492"></a>        ARG_UNUSED(user_data);
<a id="l00493"></a>        return -ENOTSUP;
<a id="l00494"></a>#endif
<a id="l00495"></a>}
<a id="l00496"></a>
<a id="l00497"></a>static inline int z_impl_uart_tx(const struct device *dev, const uint8_t *buf, size_t len,
<a id="l00498"></a>                                 int32_t timeout)
<a id="l00499"></a>
<a id="l00500"></a>{
<a id="l00501"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00502"></a>        return DEVICE_API_GET(uart, dev)-&gt;tx(dev, buf, len, timeout);
<a id="l00503"></a>#else
<a id="l00504"></a>        ARG_UNUSED(dev);
<a id="l00505"></a>        ARG_UNUSED(buf);
<a id="l00506"></a>        ARG_UNUSED(len);
<a id="l00507"></a>        ARG_UNUSED(timeout);
<a id="l00508"></a>        return -ENOTSUP;
<a id="l00509"></a>#endif
<a id="l00510"></a>}
<a id="l00511"></a>
<a id="l00512"></a>static inline int z_impl_uart_tx_u16(const struct device *dev, const uint16_t *buf, size_t len,
<a id="l00513"></a>                                     int32_t timeout)
<a id="l00514"></a>
<a id="l00515"></a>{
<a id="l00516"></a>#if defined(CONFIG_UART_ASYNC_API) &amp;&amp; defined(CONFIG_UART_WIDE_DATA)
<a id="l00517"></a>        return DEVICE_API_GET(uart, dev)-&gt;tx_u16(dev, buf, len, timeout);
<a id="l00518"></a>#else
<a id="l00519"></a>        ARG_UNUSED(dev);
<a id="l00520"></a>        ARG_UNUSED(buf);
<a id="l00521"></a>        ARG_UNUSED(len);
<a id="l00522"></a>        ARG_UNUSED(timeout);
<a id="l00523"></a>        return -ENOTSUP;
<a id="l00524"></a>#endif
<a id="l00525"></a>}
<a id="l00526"></a>
<a id="l00527"></a>static inline int z_impl_uart_tx_abort(const struct device *dev)
<a id="l00528"></a>{
<a id="l00529"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00530"></a>        return DEVICE_API_GET(uart, dev)-&gt;tx_abort(dev);
<a id="l00531"></a>#else
<a id="l00532"></a>        ARG_UNUSED(dev);
<a id="l00533"></a>        return -ENOTSUP;
<a id="l00534"></a>#endif
<a id="l00535"></a>}
<a id="l00536"></a>
<a id="l00537"></a>static inline int z_impl_uart_rx_enable(const struct device *dev, uint8_t *buf, size_t len,
<a id="l00538"></a>                                        int32_t timeout)
<a id="l00539"></a>{
<a id="l00540"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00541"></a>        return DEVICE_API_GET(uart, dev)-&gt;rx_enable(dev, buf, len, timeout);
<a id="l00542"></a>#else
<a id="l00543"></a>        ARG_UNUSED(dev);
<a id="l00544"></a>        ARG_UNUSED(buf);
<a id="l00545"></a>        ARG_UNUSED(len);
<a id="l00546"></a>        ARG_UNUSED(timeout);
<a id="l00547"></a>        return -ENOTSUP;
<a id="l00548"></a>#endif
<a id="l00549"></a>}
<a id="l00550"></a>
<a id="l00551"></a>static inline int z_impl_uart_rx_enable_u16(const struct device *dev, uint16_t *buf, size_t len,
<a id="l00552"></a>                                            int32_t timeout)
<a id="l00553"></a>{
<a id="l00554"></a>#if defined(CONFIG_UART_ASYNC_API) &amp;&amp; defined(CONFIG_UART_WIDE_DATA)
<a id="l00555"></a>        return DEVICE_API_GET(uart, dev)-&gt;rx_enable_u16(dev, buf, len, timeout);
<a id="l00556"></a>#else
<a id="l00557"></a>        ARG_UNUSED(dev);
<a id="l00558"></a>        ARG_UNUSED(buf);
<a id="l00559"></a>        ARG_UNUSED(len);
<a id="l00560"></a>        ARG_UNUSED(timeout);
<a id="l00561"></a>        return -ENOTSUP;
<a id="l00562"></a>#endif
<a id="l00563"></a>}
<a id="l00564"></a>
<a id="l00565"></a>static inline int uart_rx_buf_rsp(const struct device *dev, uint8_t *buf, size_t len)
<a id="l00566"></a>{
<a id="l00567"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00568"></a>        return DEVICE_API_GET(uart, dev)-&gt;rx_buf_rsp(dev, buf, len);
<a id="l00569"></a>#else
<a id="l00570"></a>        ARG_UNUSED(dev);
<a id="l00571"></a>        ARG_UNUSED(buf);
<a id="l00572"></a>        ARG_UNUSED(len);
<a id="l00573"></a>        return -ENOTSUP;
<a id="l00574"></a>#endif
<a id="l00575"></a>}
<a id="l00576"></a>
<a id="l00577"></a>static inline int uart_rx_buf_rsp_u16(const struct device *dev, uint16_t *buf, size_t len)
<a id="l00578"></a>{
<a id="l00579"></a>#if defined(CONFIG_UART_ASYNC_API) &amp;&amp; defined(CONFIG_UART_WIDE_DATA)
<a id="l00580"></a>        return DEVICE_API_GET(uart, dev)-&gt;rx_buf_rsp_u16(dev, buf, len);
<a id="l00581"></a>#else
<a id="l00582"></a>        ARG_UNUSED(dev);
<a id="l00583"></a>        ARG_UNUSED(buf);
<a id="l00584"></a>        ARG_UNUSED(len);
<a id="l00585"></a>        return -ENOTSUP;
<a id="l00586"></a>#endif
<a id="l00587"></a>}
<a id="l00588"></a>
<a id="l00589"></a>static inline int z_impl_uart_rx_disable(const struct device *dev)
<a id="l00590"></a>{
<a id="l00591"></a>#ifdef CONFIG_UART_ASYNC_API
<a id="l00592"></a>        return DEVICE_API_GET(uart, dev)-&gt;rx_disable(dev);
<a id="l00593"></a>#else
<a id="l00594"></a>        ARG_UNUSED(dev);
<a id="l00595"></a>        return -ENOTSUP;
<a id="l00596"></a>#endif
<a id="l00597"></a>}
<a id="l00598"></a>
<a id="l00599"></a>static inline int z_impl_uart_line_ctrl_set(const struct device *dev, uint32_t ctrl, uint32_t val)
<a id="l00600"></a>{
<a id="l00601"></a>#ifdef CONFIG_UART_LINE_CTRL
<a id="l00602"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00603"></a>
<a id="l00604"></a>        if (api-&gt;line_ctrl_set == NULL) {
<a id="l00605"></a>                return -ENOSYS;
<a id="l00606"></a>        }
<a id="l00607"></a>        return api-&gt;line_ctrl_set(dev, ctrl, val);
<a id="l00608"></a>#else
<a id="l00609"></a>        ARG_UNUSED(dev);
<a id="l00610"></a>        ARG_UNUSED(ctrl);
<a id="l00611"></a>        ARG_UNUSED(val);
<a id="l00612"></a>        return -ENOTSUP;
<a id="l00613"></a>#endif
<a id="l00614"></a>}
<a id="l00615"></a>
<a id="l00616"></a>static inline int z_impl_uart_line_ctrl_get(const struct device *dev, uint32_t ctrl, uint32_t *val)
<a id="l00617"></a>{
<a id="l00618"></a>#ifdef CONFIG_UART_LINE_CTRL
<a id="l00619"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00620"></a>
<a id="l00621"></a>        if (api-&gt;line_ctrl_get == NULL) {
<a id="l00622"></a>                return -ENOSYS;
<a id="l00623"></a>        }
<a id="l00624"></a>        return api-&gt;line_ctrl_get(dev, ctrl, val);
<a id="l00625"></a>#else
<a id="l00626"></a>        ARG_UNUSED(dev);
<a id="l00627"></a>        ARG_UNUSED(ctrl);
<a id="l00628"></a>        ARG_UNUSED(val);
<a id="l00629"></a>        return -ENOTSUP;
<a id="l00630"></a>#endif
<a id="l00631"></a>}
<a id="l00632"></a>
<a id="l00633"></a>static inline int z_impl_uart_drv_cmd(const struct device *dev, uint32_t cmd, uint32_t p)
<a id="l00634"></a>{
<a id="l00635"></a>#ifdef CONFIG_UART_DRV_CMD
<a id="l00636"></a>        const struct uart_driver_api *api = DEVICE_API_GET(uart, dev);
<a id="l00637"></a>
<a id="l00638"></a>        if (api-&gt;drv_cmd == NULL) {
<a id="l00639"></a>                return -ENOSYS;
<a id="l00640"></a>        }
<a id="l00641"></a>        return api-&gt;drv_cmd(dev, cmd, p);
<a id="l00642"></a>#else
<a id="l00643"></a>        ARG_UNUSED(dev);
<a id="l00644"></a>        ARG_UNUSED(cmd);
<a id="l00645"></a>        ARG_UNUSED(p);
<a id="l00646"></a>        return -ENOTSUP;
<a id="l00647"></a>#endif
<a id="l00648"></a>}
<a id="l00649"></a>
<a id="l00650"></a>#ifdef __cplusplus
<a id="l00651"></a>}
<a id="l00652"></a>#endif
<a id="l00653"></a>
<a id="l00655"></a>
<a id="l00656"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_UART_UART_INTERNAL_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2018-2019 Nordic Semiconductor ASA；Copyright (c) 2015 Wind River Systems, Inc.；Apache-2.0许可证原文保留。

2. 结束CONFIG_UART_INTERRUPT_DRIVEN相关中断驱动操作成员的条件编译。

3. 结束UART内部头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_UART_UART_INTERNAL_H_。

## 4.3\_原页符号提示（Symbol Descriptions）

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

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `cmd`

```c
static void cmd(uint32_t command)
```

由协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

定义位置（Definition）：ft8xx_reference_api.h:153。

符号定位：[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

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

### `uart_callback_t`

```c
void(* uart_callback_t)(const struct device *dev, struct uart_event *evt, void *user_data)
```

定义供uart_callback_set()使用的应用程序回调函数签名。

定义位置（Definition）：uart.h:317。

符号定位：[uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)。

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

### `uart_callback_set`

```c
static int uart_callback_set(const struct device *dev, uart_callback_t callback, void *user_data)
```

设置事件处理函数（Event Handler）。

符号定位：[uart_callback_set](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)。

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

### `uart_irq_tx_complete`

```c
static int uart_irq_tx_complete(const struct device *dev)
```

检查UART发送模块是否已完成传输。

符号定位：[uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)。

### `uart_fifo_fill_u16`

```c
static int uart_fifo_fill_u16(const struct device *dev, const uint16_t *tx_data, int size)
```

向FIFO填充宽数据（Wide Data）。

符号定位：[uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)。

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

### `uart_fifo_fill`

```c
static int uart_fifo_fill(const struct device *dev, const uint8_t *tx_data, int size)
```

向先进先出队列（First In, First Out，FIFO）填充数据。

符号定位：[uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)。

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

## 4.4\_源码跟踪译注

> 译注——公共声明与内部实现：uart.h定义配置、事件与公共接口，在末尾包含uart/uart_internal.h和生成的syscalls/uart.h。内部头文件中的uart_driver_api及z_impl_*／内联包装负责把调用转交给驱动函数表；普通应用仍以公共头文件为入口。官方内部参考页将这些内容列为INTERNAL_HIDDEN，只有文件说明与源码入口，不能把它当成缺失了公开成员说明；完整可见代码在本册内部源码页保留。

> 译注——枚举编码与配置值：UART_LINE_CTRL_*和UART_ERROR_*是位标志（Bit Flags），而数据位、停止位、奇偶校验与流控制枚举采用各自的顺序编码。UART_CFG_DATA_BITS_8不是整数8，不能直接把设备树data-bits数值赋给uart_config.data_bits；应使用对应枚举。uart_config.baudrate按原文字段说明使用bps，实际速率、格式和流控制是否可用取决于驱动及硬件。绑定中的current-speed、hw-flow-control等是初始化配置来源，不等于运行时已成功调用uart_configure。

> 译注——三种传输方式：轮询输入（Polling Input）为非阻塞接口，轮询输出（Polling Output）可能等待发送条件。中断驱动（Interrupt-driven）由IRQ回调处理FIFO，异步API（Asynchronous API）由uart_event回调报告传输进度和完成。三类入口、回调签名与配置条件不同。UART_EXCLUSIVE_API_CALLBACKS在异步与中断接口同时启用时默认使两类回调互斥，具体清除动作由相应驱动落实；不能仅因两组选项都启用就假定同一设备可以同时保留两套回调。

> 译注——中断处理顺序：官方公共约定要求先在ISR调用uart_irq_update，再查询RX／TX就绪、发送完成或挂起状态。当前uart_irq_update返回void，内部包装在驱动有irq_update操作时才调用它，不能写成依赖其整数返回值的判断。TX就绪时应填充FIFO并检查实际写入数量；RX就绪时持续读取，直至返回数量小于请求数量，避免假定中断一定按电平触发。错误返回应单独处理，不能把负errno当作成功计数或简单布尔真值。

> 译注——异步事件与缓冲区：uart_tx／uart_rx_enable返回的是启动结果，完成与数据可用通过事件通知。UART_RX_RDY给出当前缓冲区内从offset开始、长度为len的新数据，不表示缓冲区已释放，同一缓冲区可以出现多次RDY。收到UART_RX_BUF_REQUEST时可提供下一缓冲区；驱动仍在使用的缓冲区不能再次提交，要等UART_RX_BUF_RELEASED后复用。停收或错误可先通知剩余数据，再释放缓冲区，最后报告UART_RX_DISABLED。

> 译注——超时与宽数据单位：异步timeout单位为微秒（Microsecond），TX超时按原约定仅在流控制启用时有效；RX超时是至少收到一个字节后的不活动间隔，没有收到数据时不会单凭该间隔产生RDY。SYS_FOREVER_US禁用超时。带_u16接口以uint16_t容纳宽数据，FIFO与异步传输长度按数据项计；用户态校验也采用len乘sizeof(uint16_t)检查数组范围，不能把len直接当作字节数。公开事件字段的字节措辞按原文保留，宽数据场景仍须核对具体驱动的事件填充。

> 译注——错误与空操作边界：运行时配置、线路控制、驱动命令、FIFO及多数中断状态查询，在对应功能未启用时返回-ENOTSUP；已启用但所检查的操作指针为空时返回-ENOSYS。部分void中断使能／禁用包装在缺少操作时不做任何事，宽数据轮询输出在功能未启用时同样为空操作。poll_out以及异步TX、RX和缓冲区提交包装在已编译分支中直接调用相应操作，不统一执行空指针检查。应按所用入口及设备能力判断，不能把一处检查推广给所有UART API。

> 译注——用户态与回调边界：uart_handlers.c为系统调用核对设备对象／操作权限及输入输出缓冲区可访问范围；这些校验不代表内核内联包装也自动拥有相同检查。回调安装与rx_buf_rsp未提供同类系统调用入口，原注释明确回调安装不允许来自用户态，缓冲区响应用于ISR回调。自定义驱动命令的cmd是UART命令参数；原Doxygen页面将同名符号链接到显示协处理器函数，相关符号提示按原文保留，该交叉引用不意味着UART具有显示命令功能。

> 译注——版本边界：本批核对公共与内部两个头文件、UART系统调用处理、串口Kconfig和公共控制器绑定，共五份官方源码并记录摘要。两份源码浏览页的非注释代码分别与读取的官方原始头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、打开串口、发送数据或操作硬件。

头文件相对定位：[include/zephyr/drivers/uart/uart_internal.h](../../../include/zephyr/drivers/uart/uart_internal.h)，关联实现／接口：[drivers/serial/uart_handlers.c](../../../drivers/serial/uart_handlers.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/uart/uart_internal.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_handlers.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、打开串口、收发数据或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_UART内部头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [uart_config](../hardware/P331_UART配置结构.md)
- [uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)
- [uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)
- [uart_fifo_read](../hardware/P333_UART中断驱动接口.md#gab10942076ac47ecff29e924098049398)
- [uart_fifo_read_u16](../hardware/P333_UART中断驱动接口.md#ga4a3c25dad2290f1f40e4b847e3b83f64)
- [uart_irq_tx_ready](../hardware/P333_UART中断驱动接口.md#ga5e126b5f19549eb7f5b785b98ebe7638)
- [uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)
- [uart_irq_rx_ready](../hardware/P333_UART中断驱动接口.md#gad04073b1b8e3de13b43ae1194561377b)
- [uart_irq_is_pending](../hardware/P333_UART中断驱动接口.md#gacd8c2978e0f1316dd79bb42baad1c5a7)
- [uart_irq_update](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)
- [uart_irq_callback_user_data_set](../hardware/P333_UART中断驱动接口.md#gaf469966a56d1fc9f50108201597ee0a0)
- [uart_irq_callback_set](../hardware/P333_UART中断驱动接口.md#ga5f7af3f7f0d9155349ea3b4fad78956c)
- [uart_callback_set](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)
- [uart_rx_buf_rsp](../hardware/P334_UART异步接口.md#ga3970fe2818e214b0814ea8b73a816a6a)
- [uart_rx_buf_rsp_u16](../hardware/P334_UART异步接口.md#ga778bcfc30be853c8d320f295b34c17c0)

---

[上一章](P003_UART内部头文件参考.md) · [返回大纲](大纲.md)
