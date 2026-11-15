---
id: learning.zephyr-docs.stmesp-source-reference.page-2
title: STMESP日志解复用头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp__demux_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_STMESP日志解复用头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp__demux_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](../observability/P048_STMESP日志解复用头文件.md)和[公共接口](../observability/P032_STMESP日志解复用接口.md)；访问语义和生命周期见本页译注。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00062"></a>
<a id="foldopen00080"></a>
<a id="foldopen00089"></a>
<a id="foldopen00101"></a>
<a id="foldopen00125"></a>
<a id="foldopen00155"></a>
<a id="foldopen00173"></a>
<a id="foldopen00194"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga10621a1e4c5b875650b3ff89b3e97297"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga184cc4d266a010aa094a45aba0fad638"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga1d693b8936666f7b352fd7e25535ac16"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga235c0d680cb674b6e99d886497f257d5"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga33581c39a57eca7f96fea9c29386a3e3"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga38e05a234824b0adbeca16cb3e21cc75"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga487c9163e6477a879136350d4c109641"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga4ac8c23bbf2eaf23a73698e3e36a9594"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga4f86c0cfb38fa05389462045019a6650"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga56ad2b8067d56b9ccedefd57ad5aa0c2"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga6a25dd796a8759009e14b5770f7653a9"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga7be93bc9ad1ecfe37f5af64adf029f39"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga7c692b9d84aedfb30673a58959465ccf"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga8be4ca332fa9145fad72a6b45245a9ff"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_ga97f9ac1d7b459e9d3d715b5367e29a31"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gaa624af8e67b4be013f0ec1507d805c34"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gad9c13b59d1e09a240ed35b03b04b1a96"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gae5925a640c401cc09dd744945eafd51c"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gaeaf76dcb74836740115c9b6e3fece73b"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gaed29a1869e710cd95c19c48c67a36aa8"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gaf2b7019394d33a082fec5ab2d2785257"></a>
<a id="agroup__log__frontend__stmesp__demux__apis_html_gaf7b66578311278e6d58312ea239c9c0c"></a>
<a id="akernel_8h_html"></a>
<a id="ampsc__packet_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructlog__frontend__stmesp__demux__config_html"></a>
<a id="astructlog__frontend__stmesp__demux__config_html_a643b5bd780342bf1944e5a63274aa305"></a>
<a id="astructlog__frontend__stmesp__demux__config_html_aca85e1b671127e8803423f22b2d45a33"></a>
<a id="astructlog__frontend__stmesp__demux__config_html_ad248eabec1eee58f5ef689004d5c7017"></a>
<a id="astructlog__frontend__stmesp__demux__config_html_ada2f243b112324e99a53b831211cabce"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html_a0766f3aa6163ea1a197d674eac00305b"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html_a090039b38d646812a292510476d16644"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html_a5a781f1b681ef2499bf9ba2635261d4f"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html_a6a060e7fbda81c47eaa8088f3e45052a"></a>
<a id="astructlog__frontend__stmesp__demux__hw__event_html_ae6872dcd7e11eeb431e3d990ccdad243"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html_a0a378b7740a3def454bf34fe54927aa1"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html_a138b653d76c50c0454210b7a1d7ec60b"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html_a3b1474632ab446d8c9d590fb4bd8e420"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html_acec1720948196deb1f09ab1ea443ecb9"></a>
<a id="astructlog__frontend__stmesp__demux__log__header_html_ae18c81e29011d48e548a7daec2a3f9ba"></a>
<a id="astructlog__frontend__stmesp__demux__log_html"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_a84cf9f64d96e87cfd2bb9d859fed3886"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_aa5b7175e05dbdcc41d75c5412ce30b15"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_ab063e3ed4d81cbdb4ec417508c55bd13"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_ad25f0378c2c3ba3d153a58a843704033"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_adb1b61bdca3a97df2c8ba2b34fc2ebff"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_ae8c62ffd8a11fbcebce29ed934f52597"></a>
<a id="astructlog__frontend__stmesp__demux__log_html_af2b9820efce6f58d655b08a306c8d8d1"></a>
<a id="astructlog__frontend__stmesp__demux__packet__generic_html"></a>
<a id="astructlog__frontend__stmesp__demux__packet__generic_html_a42d6b5192e0f9ba897a2986d645c6a6c"></a>
<a id="astructlog__frontend__stmesp__demux__packet__generic_html_a7a86c5de5e5b33830d963add116c1feb"></a>
<a id="astructlog__frontend__stmesp__demux__packet__generic_html_ac202cf6bc5bc8699a858e10de2c0c492"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_a0bdc2a3e1afb5748e08e68617f2ccbb6"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_a0ca97d4ffd9bae1d640b8f99c8bd5ace"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_a300adc8bd0882810ae4a5759a76857ce"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_a6e1892f15fa3149f8161a1792420ba73"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_ab250b6782df720df3d1cdb37ab25a024"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_acfa056769b9ba00b945e1ff7d1e4cdb9"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_ada954ed2971c2fc720a1d1f2634c0e2a"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_ae3e776e4a470ccb3abd8f6a73ce7b21b"></a>
<a id="astructlog__frontend__stmesp__demux__trace__point_html_aeb86bfae01245a4778d08ac9c1ee138a"></a>
<a id="aunionlog__frontend__stmesp__demux__header_html"></a>
<a id="aunionlog__frontend__stmesp__demux__header_html_ae868e8f2e8b0623781d3f9377490c72a"></a>
<a id="aunionlog__frontend__stmesp__demux__header_html_ae94bab609a4f5c51eef7886db712420d"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html_a30d3cfc6071bebc1614f2f67c8a950c7"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html_aa68b1022f97c8806ee430a541190fc82"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html_ac712f4dc2ca645e2ba6f6c638b41bf10"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html_ac75deeb2f665aeb5dcfd94090aa1a1cf"></a>
<a id="aunionlog__frontend__stmesp__demux__packet_html_ae764f7a3b04e66af22c52aa1d52a441e"></a>
<a id="aunionmpsc__pbuf__generic_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_DEMUX_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_DEMUX_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00017"></a>#include &lt;zephyr/sys/mpsc_packet.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00033"></a>
<a id="l00035"></a>#define LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS 3
<a id="l00036"></a>
<a id="l00038"></a>#define LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS 3
<a id="l00039"></a>
<a id="l00041"></a>#define LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS 15
<a id="l00042"></a>
<a id="l00044"></a>#define LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS 10
<a id="l00045"></a>
<a id="l00047"></a>#define LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS 1
<a id="l00048"></a>
<a id="l00050"></a>#define LOG_FRONTEND_STMESP_DEMUX_MAJOR_MAX BIT(LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS)
<a id="l00051"></a>
<a id="l00053"></a>#define LOG_FRONTEND_STMESP_DEMUX_TYPE_LOG 0
<a id="l00054"></a>
<a id="l00056"></a>#define LOG_FRONTEND_STMESP_DEMUX_TYPE_TRACE_POINT 1
<a id="l00057"></a>
<a id="l00059"></a>#define LOG_FRONTEND_STMESP_DEMUX_TYPE_HW_EVENT 2
<a id="l00060"></a>
<a id="l00062"></a>struct log_frontend_stmesp_demux_log_header {
<a id="l00064"></a>        uint32_t major : LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS;
<a id="l00065"></a>
<a id="l00067"></a>        uint32_t level : LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS;
<a id="l00068"></a>
<a id="l00070"></a>        uint32_t total_len : LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS;
<a id="l00071"></a>
<a id="l00073"></a>        uint32_t package_len : LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS;
<a id="l00074"></a>
<a id="l00076"></a>        uint32_t has_data: LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS;
<a id="l00077"></a>};
<a id="l00078"></a>
<a id="l00080"></a>union log_frontend_stmesp_demux_header {
<a id="l00082"></a>        struct log_frontend_stmesp_demux_log_header log;
<a id="l00083"></a>
<a id="l00085"></a>        uint32_t raw;
<a id="l00086"></a>};
<a id="l00087"></a>
<a id="l00089"></a>struct log_frontend_stmesp_demux_packet_generic {
<a id="l00091"></a>        MPSC_PBUF_HDR;
<a id="l00092"></a>
<a id="l00094"></a>        uint64_t type: 2;
<a id="l00095"></a>
<a id="l00097"></a>        uint64_t content_invalid: 1;
<a id="l00098"></a>};
<a id="l00099"></a>
<a id="l00101"></a>struct log_frontend_stmesp_demux_log {
<a id="l00103"></a>        MPSC_PBUF_HDR;
<a id="l00104"></a>
<a id="l00106"></a>        uint64_t type: 2;
<a id="l00107"></a>
<a id="l00109"></a>        uint64_t content_invalid: 1;
<a id="l00110"></a>
<a id="l00112"></a>        uint64_t timestamp: 59;
<a id="l00113"></a>
<a id="l00115"></a>        struct log_frontend_stmesp_demux_log_header hdr;
<a id="l00116"></a>
<a id="l00118"></a>        uint32_t padding;
<a id="l00119"></a>
<a id="l00121"></a>        uint8_t data[];
<a id="l00122"></a>};
<a id="l00123"></a>
<a id="l00125"></a>struct log_frontend_stmesp_demux_trace_point {
<a id="l00127"></a>        MPSC_PBUF_HDR;
<a id="l00128"></a>
<a id="l00130"></a>        uint64_t type: 2;
<a id="l00131"></a>
<a id="l00133"></a>        uint64_t content_invalid: 1;
<a id="l00134"></a>
<a id="l00136"></a>        uint64_t has_data: 1;
<a id="l00137"></a>
<a id="l00139"></a>        uint64_t timestamp: 54;
<a id="l00140"></a>
<a id="l00142"></a>        uint64_t major: 4;
<a id="l00143"></a>
<a id="l00145"></a>        uint16_t source_id;
<a id="l00146"></a>
<a id="l00148"></a>        uint16_t id;
<a id="l00149"></a>
<a id="l00151"></a>        uint32_t data;
<a id="l00152"></a>};
<a id="l00153"></a>
<a id="l00155"></a>struct log_frontend_stmesp_demux_hw_event {
<a id="l00157"></a>        MPSC_PBUF_HDR;
<a id="l00158"></a>
<a id="l00160"></a>        uint64_t type: 2;
<a id="l00161"></a>
<a id="l00163"></a>        uint64_t content_invalid: 1;
<a id="l00164"></a>
<a id="l00166"></a>        uint64_t timestamp: 59;
<a id="l00167"></a>
<a id="l00169"></a>        uint8_t evt;
<a id="l00170"></a>};
<a id="l00171"></a>
<a id="l00173"></a>union log_frontend_stmesp_demux_packet {
<a id="l00175"></a>        const union mpsc_pbuf_generic *rgeneric;
<a id="l00176"></a>
<a id="l00178"></a>        union mpsc_pbuf_generic *generic;
<a id="l00179"></a>
<a id="l00181"></a>        struct log_frontend_stmesp_demux_log *log;
<a id="l00182"></a>
<a id="l00184"></a>        struct log_frontend_stmesp_demux_trace_point *trace_point;
<a id="l00185"></a>
<a id="l00187"></a>        struct log_frontend_stmesp_demux_hw_event *hw_event;
<a id="l00188"></a>
<a id="l00190"></a>        struct log_frontend_stmesp_demux_packet_generic *generic_packet;
<a id="l00191"></a>};
<a id="l00192"></a>
<a id="l00194"></a>struct log_frontend_stmesp_demux_config {
<a id="l00196"></a>        const uint16_t *m_ids;
<a id="l00197"></a>
<a id="l00199"></a>        uint32_t m_ids_cnt;
<a id="l00200"></a>
<a id="l00202"></a>        uint32_t *source_id_buf;
<a id="l00203"></a>
<a id="l00205"></a>        size_t source_id_buf_len;
<a id="l00206"></a>};
<a id="l00207"></a>
<a id="l00215"></a>int log_frontend_stmesp_demux_init(const struct log_frontend_stmesp_demux_config *config);
<a id="l00216"></a>
<a id="l00221"></a>void log_frontend_stmesp_demux_major(uint16_t id);
<a id="l00222"></a>
<a id="l00227"></a>void log_frontend_stmesp_demux_channel(uint16_t id);
<a id="l00228"></a>
<a id="l00234"></a>int log_frontend_stmesp_demux_packet_start(uint32_t *data, uint64_t *ts);
<a id="l00235"></a>
<a id="l00241"></a>int log_frontend_stmesp_demux_log0(uint16_t source_id, uint64_t *ts);
<a id="l00242"></a>
<a id="l00247"></a>void log_frontend_stmesp_demux_source_id(uint16_t source_id);
<a id="l00248"></a>
<a id="l00256"></a>void log_frontend_stmesp_demux_timestamp(uint64_t ts);
<a id="l00257"></a>
<a id="l00263"></a>void log_frontend_stmesp_demux_data(uint8_t *data, size_t len);
<a id="l00264"></a>
<a id="l00266"></a>void log_frontend_stmesp_demux_packet_end(void);
<a id="l00267"></a>
<a id="l00274"></a>uint32_t log_frontend_stmesp_demux_get_dropped(void);
<a id="l00275"></a>
<a id="l00283"></a>union log_frontend_stmesp_demux_packet log_frontend_stmesp_demux_claim(void);
<a id="l00284"></a>
<a id="l00291"></a>void log_frontend_stmesp_demux_free(union log_frontend_stmesp_demux_packet packet);
<a id="l00292"></a>
<a id="l00306"></a>const char *log_frontend_stmesp_demux_sname_get(uint32_t m_id, uint16_t s_id);
<a id="l00307"></a>
<a id="l00320"></a>const char *log_frontend_stmesp_demux_str_get(uint32_t m_id, uint16_t s_id);
<a id="l00321"></a>
<a id="l00327"></a>bool log_frontend_stmesp_demux_is_idle(void);
<a id="l00328"></a>
<a id="l00330"></a>void log_frontend_stmesp_demux_reset(void);
<a id="l00331"></a>
<a id="l00337"></a>int log_frontend_stmesp_demux_max_utilization(void);
<a id="l00338"></a>
<a id="l00342"></a>
<a id="l00343"></a>#ifdef __cplusplus
<a id="l00344"></a>}
<a id="l00345"></a>#endif
<a id="l00346"></a>
<a id="l00347"></a>#endif /* ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_DEMUX_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_DEMUX_H_头文件包含保护结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `log_frontend_stmesp_demux_sname_get`

```c
const char * log_frontend_stmesp_demux_sname_get(uint32_t m_id, uint16_t s_id)
```

取得Turbo日志消息的源名称（Source Name）。

符号定位：[log_frontend_stmesp_demux_sname_get](../observability/P032_STMESP日志解复用接口.md#ga10621a1e4c5b875650b3ff89b3e97297)。

### `log_frontend_stmesp_demux_timestamp`

```c
void log_frontend_stmesp_demux_timestamp(uint64_t ts)
```

传入时间戳（Timestamp）。

符号定位：[log_frontend_stmesp_demux_timestamp](../observability/P032_STMESP日志解复用接口.md#ga184cc4d266a010aa094a45aba0fad638)。

### `log_frontend_stmesp_demux_is_idle`

```c
bool log_frontend_stmesp_demux_is_idle(void)
```

检查是否存在已开始但尚未完成的日志消息。

符号定位：[log_frontend_stmesp_demux_is_idle](../observability/P032_STMESP日志解复用接口.md#ga1d693b8936666f7b352fd7e25535ac16)。

### `log_frontend_stmesp_demux_data`

```c
void log_frontend_stmesp_demux_data(uint8_t *data, size_t len)
```

传入数据（Data）。

符号定位：[log_frontend_stmesp_demux_data](../observability/P032_STMESP日志解复用接口.md#ga235c0d680cb674b6e99d886497f257d5)。

### `LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS`

```c
#define LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS
```

存储Major索引所用的位数。

定义位置（Definition）：log_frontend_stmesp_demux.h:35。

符号定位：[LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS](../observability/P032_STMESP日志解复用接口.md#ga33581c39a57eca7f96fea9c29386a3e3)。

### `log_frontend_stmesp_demux_packet_end`

```c
void log_frontend_stmesp_demux_packet_end(void)
```

传入数据包结束标志（Flag）。

符号定位：[log_frontend_stmesp_demux_packet_end](../observability/P032_STMESP日志解复用接口.md#ga38e05a234824b0adbeca16cb3e21cc75)。

### `log_frontend_stmesp_demux_reset`

```c
void log_frontend_stmesp_demux_reset(void)
```

关闭所有尚未完成的消息，并将其标记为无效。

符号定位：[log_frontend_stmesp_demux_reset](../observability/P032_STMESP日志解复用接口.md#ga487c9163e6477a879136350d4c109641)。

### `LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS`

```c
#define LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS
```

表示是否含十六进制转储（Hexdump）的位数。

定义位置（Definition）：log_frontend_stmesp_demux.h:47。

符号定位：[LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS](../observability/P032_STMESP日志解复用接口.md#ga4ac8c23bbf2eaf23a73698e3e36a9594)。

### `log_frontend_stmesp_demux_channel`

```c
void log_frontend_stmesp_demux_channel(uint16_t id)
```

传入STPv2流中的通道操作码（Channel Opcode）。

符号定位：[log_frontend_stmesp_demux_channel](../observability/P032_STMESP日志解复用接口.md#ga4f86c0cfb38fa05389462045019a6650)。

### `LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS`

```c
#define LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS
```

存储包长度（Package Length）所用的位数。

定义位置（Definition）：log_frontend_stmesp_demux.h:44。

符号定位：[LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS](../observability/P032_STMESP日志解复用接口.md#ga56ad2b8067d56b9ccedefd57ad5aa0c2)。

### `log_frontend_stmesp_demux_log0`

```c
int log_frontend_stmesp_demux_log0(uint16_t source_id, uint64_t *ts)
```

传入无参数的优化日志消息（Optimized Log Message）。

符号定位：[log_frontend_stmesp_demux_log0](../observability/P032_STMESP日志解复用接口.md#ga6a25dd796a8759009e14b5770f7653a9)。

### `log_frontend_stmesp_demux_max_utilization`

```c
int log_frontend_stmesp_demux_max_utilization(void)
```

取得缓冲区最大利用量（Maximum Buffer Utilization）。

符号定位：[log_frontend_stmesp_demux_max_utilization](../observability/P032_STMESP日志解复用接口.md#ga7be93bc9ad1ecfe37f5af64adf029f39)。

### `log_frontend_stmesp_demux_str_get`

```c
const char * log_frontend_stmesp_demux_str_get(uint32_t m_id, uint16_t s_id)
```

取得Turbo日志消息的格式字符串（Format String）。

符号定位：[log_frontend_stmesp_demux_str_get](../observability/P032_STMESP日志解复用接口.md#ga7c692b9d84aedfb30673a58959465ccf)。

### `log_frontend_stmesp_demux_major`

```c
void log_frontend_stmesp_demux_major(uint16_t id)
```

传入STPv2流中的Major操作码。

符号定位：[log_frontend_stmesp_demux_major](../observability/P032_STMESP日志解复用接口.md#ga8be4ca332fa9145fad72a6b45245a9ff)。

### `log_frontend_stmesp_demux_init`

```c
int log_frontend_stmesp_demux_init(const struct log_frontend_stmesp_demux_config *config)
```

初始化解复用器（Demultiplexer）。

符号定位：[log_frontend_stmesp_demux_init](../observability/P032_STMESP日志解复用接口.md#ga97f9ac1d7b459e9d3d715b5367e29a31)。

### `log_frontend_stmesp_demux_get_dropped`

```c
uint32_t log_frontend_stmesp_demux_get_dropped(void)
```

取得丢弃消息数（Dropped Messages），并重置计数器。

符号定位：[log_frontend_stmesp_demux_get_dropped](../observability/P032_STMESP日志解复用接口.md#gaa624af8e67b4be013f0ec1507d805c34)。

### `log_frontend_stmesp_demux_free`

```c
void log_frontend_stmesp_demux_free(union log_frontend_stmesp_demux_packet packet)
```

释放先前领取（Claim）的数据包。

符号定位：[log_frontend_stmesp_demux_free](../observability/P032_STMESP日志解复用接口.md#gad9c13b59d1e09a240ed35b03b04b1a96)。

### `log_frontend_stmesp_demux_source_id`

```c
void log_frontend_stmesp_demux_source_id(uint16_t source_id)
```

传入源编号（Source ID）。

符号定位：[log_frontend_stmesp_demux_source_id](../observability/P032_STMESP日志解复用接口.md#gae5925a640c401cc09dd744945eafd51c)。

### `LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS`

```c
#define LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS
```

存储总长度（Total Length）所用的位数。

定义位置（Definition）：log_frontend_stmesp_demux.h:41。

符号定位：[LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS](../observability/P032_STMESP日志解复用接口.md#gaeaf76dcb74836740115c9b6e3fece73b)。

### `log_frontend_stmesp_demux_packet_start`

```c
int log_frontend_stmesp_demux_packet_start(uint32_t *data, uint64_t *ts)
```

传入检测到的数据包起始事件（DMTS）。

符号定位：[log_frontend_stmesp_demux_packet_start](../observability/P032_STMESP日志解复用接口.md#gaed29a1869e710cd95c19c48c67a36aa8)。

### `LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS`

```c
#define LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS
```

存储严重性级别（Severity Level）所用的位数。

定义位置（Definition）：log_frontend_stmesp_demux.h:38。

符号定位：[LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS](../observability/P032_STMESP日志解复用接口.md#gaf2b7019394d33a082fec5ab2d2785257)。

### `log_frontend_stmesp_demux_claim`

```c
union log_frontend_stmesp_demux_packet log_frontend_stmesp_demux_claim(void)
```

领取数据包（Claim Packet）。

符号定位：[log_frontend_stmesp_demux_claim](../observability/P032_STMESP日志解复用接口.md#gaf7b66578311278e6d58312ea239c9c0c)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `mpsc_packet.h`

符号定位：[mpsc_packet.h](../intercore_reference/P176_MPSC数据包描述头文件参考.md)。

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

### `log_frontend_stmesp_demux_config`

解复用器配置（Demultiplexer Configuration）。

定义位置（Definition）：log_frontend_stmesp_demux.h:194。

符号定位：[log_frontend_stmesp_demux_config](../observability/P043_STMESP解复用配置.md)。

### `log_frontend_stmesp_demux_config::source_id_buf_len`

```c
size_t source_id_buf_len
```

它必须是Major ID数量的整数倍。

定义位置（Definition）：log_frontend_stmesp_demux.h:205。

符号定位：[log_frontend_stmesp_demux_config::source_id_buf_len](../observability/P043_STMESP解复用配置.md#a643b5bd780342bf1944e5a63274aa305)。

### `log_frontend_stmesp_demux_config::source_id_buf`

```c
uint32_t * source_id_buf
```

用于存储源编号（Source ID）的缓冲区。

定义位置（Definition）：log_frontend_stmesp_demux.h:202。

符号定位：[log_frontend_stmesp_demux_config::source_id_buf](../observability/P043_STMESP解复用配置.md#aca85e1b671127e8803423f22b2d45a33)。

### `log_frontend_stmesp_demux_config::m_ids_cnt`

```c
uint32_t m_ids_cnt
```

数组长度（Array Length）。

定义位置（Definition）：log_frontend_stmesp_demux.h:199。

符号定位：[log_frontend_stmesp_demux_config::m_ids_cnt](../observability/P043_STMESP解复用配置.md#ad248eabec1eee58f5ef689004d5c7017)。

### `log_frontend_stmesp_demux_config::m_ids`

```c
const uint16_t * m_ids
```

包含预期Major ID的数组。

定义位置（Definition）：log_frontend_stmesp_demux.h:196。

符号定位：[log_frontend_stmesp_demux_config::m_ids](../observability/P043_STMESP解复用配置.md#ada2f243b112324e99a53b831211cabce)。

### `log_frontend_stmesp_demux_hw_event`

携带硬件事件（HW Event）的数据包。

定义位置（Definition）：log_frontend_stmesp_demux.h:155。

符号定位：[log_frontend_stmesp_demux_hw_event](../observability/P041_STMESP硬件事件数据包.md)。

### `log_frontend_stmesp_demux_hw_event::timestamp`

```c
uint64_t timestamp
```

时间戳（Timestamp）。

定义位置（Definition）：log_frontend_stmesp_demux.h:166。

符号定位：[log_frontend_stmesp_demux_hw_event::timestamp](../observability/P041_STMESP硬件事件数据包.md#a0766f3aa6163ea1a197d674eac00305b)。

### `log_frontend_stmesp_demux_hw_event::evt`

```c
uint8_t evt
```

硬件事件编号（HW Event ID）。

定义位置（Definition）：log_frontend_stmesp_demux.h:169。

符号定位：[log_frontend_stmesp_demux_hw_event::evt](../observability/P041_STMESP硬件事件数据包.md#a090039b38d646812a292510476d16644)。

### `log_frontend_stmesp_demux_hw_event::type`

```c
uint64_t type
```

类型（Type）。

定义位置（Definition）：log_frontend_stmesp_demux.h:160。

符号定位：[log_frontend_stmesp_demux_hw_event::type](../observability/P041_STMESP硬件事件数据包.md#a5a781f1b681ef2499bf9ba2635261d4f)。

### `log_frontend_stmesp_demux_hw_event::MPSC_PBUF_HDR`

```c
MPSC_PBUF_HDR
```

用于多生产者单消费者（MPSC）数据包处理的数据。

定义位置（Definition）：log_frontend_stmesp_demux.h:157。

符号定位：[log_frontend_stmesp_demux_hw_event::MPSC_PBUF_HDR](../observability/P041_STMESP硬件事件数据包.md#a6a060e7fbda81c47eaa8088f3e45052a)。

### `log_frontend_stmesp_demux_hw_event::content_invalid`

```c
uint64_t content_invalid
```

表示数据包是否有效的标志（Validity Flag）。

定义位置（Definition）：log_frontend_stmesp_demux.h:163。

符号定位：[log_frontend_stmesp_demux_hw_event::content_invalid](../observability/P041_STMESP硬件事件数据包.md#ae6872dcd7e11eeb431e3d990ccdad243)。

### `log_frontend_stmesp_demux_log_header`

日志消息头（Logging Message Header）。

定义位置（Definition）：log_frontend_stmesp_demux.h:62。

符号定位：[log_frontend_stmesp_demux_log_header](../observability/P036_STMESP日志消息头.md)。

### `log_frontend_stmesp_demux_log_header::package_len`

```c
uint32_t package_len
```

包数据长度（Package Data Length）。

定义位置（Definition）：log_frontend_stmesp_demux.h:73。

符号定位：[log_frontend_stmesp_demux_log_header::package_len](../observability/P036_STMESP日志消息头.md#a0a378b7740a3def454bf34fe54927aa1)。

### `log_frontend_stmesp_demux_log_header::total_len`

```c
uint32_t total_len
```

不含此头部的总长度（Total Length）。

定义位置（Definition）：log_frontend_stmesp_demux.h:70。

符号定位：[log_frontend_stmesp_demux_log_header::total_len](../observability/P036_STMESP日志消息头.md#a138b653d76c50c0454210b7a1d7ec60b)。

### `log_frontend_stmesp_demux_log_header::level`

```c
uint32_t level
```

严重性级别（Severity Level）。

定义位置（Definition）：log_frontend_stmesp_demux.h:67。

符号定位：[log_frontend_stmesp_demux_log_header::level](../observability/P036_STMESP日志消息头.md#a3b1474632ab446d8c9d590fb4bd8e420)。

### `log_frontend_stmesp_demux_log_header::major`

```c
uint32_t major
```

Major索引（Major Index）。

定义位置（Definition）：log_frontend_stmesp_demux.h:64。

符号定位：[log_frontend_stmesp_demux_log_header::major](../observability/P036_STMESP日志消息头.md#acec1720948196deb1f09ab1ea443ecb9)。

### `log_frontend_stmesp_demux_log_header::has_data`

```c
uint32_t has_data
```

含有十六进制转储数据（Hexdump Data）。

定义位置（Definition）：log_frontend_stmesp_demux.h:76。

符号定位：[log_frontend_stmesp_demux_log_header::has_data](../observability/P036_STMESP日志消息头.md#ae18c81e29011d48e548a7daec2a3f9ba)。

### `log_frontend_stmesp_demux_log`

携带日志消息（Logging Message）的数据包。

定义位置（Definition）：log_frontend_stmesp_demux.h:101。

符号定位：[log_frontend_stmesp_demux_log](../observability/P039_STMESP日志数据包.md)。

### `log_frontend_stmesp_demux_log::content_invalid`

```c
uint64_t content_invalid
```

表示数据包是否有效的标志（Validity Flag）。

定义位置（Definition）：log_frontend_stmesp_demux.h:109。

符号定位：[log_frontend_stmesp_demux_log::content_invalid](../observability/P039_STMESP日志数据包.md#a84cf9f64d96e87cfd2bb9d859fed3886)。

### `log_frontend_stmesp_demux_log::hdr`

```c
struct log_frontend_stmesp_demux_log_header hdr
```

日志头（Logging Header）。

定义位置（Definition）：log_frontend_stmesp_demux.h:115。

符号定位：[log_frontend_stmesp_demux_log::hdr](../observability/P039_STMESP日志数据包.md#aa5b7175e05dbdcc41d75c5412ce30b15)。

### `log_frontend_stmesp_demux_log::padding`

```c
uint32_t padding
```

使数据按8字节对齐的填充（Padding）。

定义位置（Definition）：log_frontend_stmesp_demux.h:118。

符号定位：[log_frontend_stmesp_demux_log::padding](../observability/P039_STMESP日志数据包.md#ab063e3ed4d81cbdb4ec417508c55bd13)。

### `log_frontend_stmesp_demux_log::MPSC_PBUF_HDR`

```c
MPSC_PBUF_HDR
```

用于多生产者单消费者（MPSC）数据包处理的数据。

定义位置（Definition）：log_frontend_stmesp_demux.h:103。

符号定位：[log_frontend_stmesp_demux_log::MPSC_PBUF_HDR](../observability/P039_STMESP日志数据包.md#ad25f0378c2c3ba3d153a58a843704033)。

### `log_frontend_stmesp_demux_log::type`

```c
uint64_t type
```

类型（Type）。

定义位置（Definition）：log_frontend_stmesp_demux.h:106。

符号定位：[log_frontend_stmesp_demux_log::type](../observability/P039_STMESP日志数据包.md#adb1b61bdca3a97df2c8ba2b34fc2ebff)。

### `log_frontend_stmesp_demux_log::data`

```c
uint8_t data[]
```

内容（Content）。

定义位置（Definition）：log_frontend_stmesp_demux.h:121。

符号定位：[log_frontend_stmesp_demux_log::data](../observability/P039_STMESP日志数据包.md#ae8c62ffd8a11fbcebce29ed934f52597)。

### `log_frontend_stmesp_demux_log::timestamp`

```c
uint64_t timestamp
```

时间戳（Timestamp）。

定义位置（Definition）：log_frontend_stmesp_demux.h:112。

符号定位：[log_frontend_stmesp_demux_log::timestamp](../observability/P039_STMESP日志数据包.md#af2b9820efce6f58d655b08a306c8d8d1)。

### `log_frontend_stmesp_demux_packet_generic`

通用STP解复用数据包（Generic STP Demux Packet）。

定义位置（Definition）：log_frontend_stmesp_demux.h:89。

符号定位：[log_frontend_stmesp_demux_packet_generic](../observability/P038_STMESP通用数据包.md)。

### `log_frontend_stmesp_demux_packet_generic::content_invalid`

```c
uint64_t content_invalid
```

表示数据包是否有效的标志（Validity Flag）。

定义位置（Definition）：log_frontend_stmesp_demux.h:97。

符号定位：[log_frontend_stmesp_demux_packet_generic::content_invalid](../observability/P038_STMESP通用数据包.md#a42d6b5192e0f9ba897a2986d645c6a6c)。

### `log_frontend_stmesp_demux_packet_generic::type`

```c
uint64_t type
```

类型（Type）。

定义位置（Definition）：log_frontend_stmesp_demux.h:94。

符号定位：[log_frontend_stmesp_demux_packet_generic::type](../observability/P038_STMESP通用数据包.md#a7a86c5de5e5b33830d963add116c1feb)。

### `log_frontend_stmesp_demux_packet_generic::MPSC_PBUF_HDR`

```c
MPSC_PBUF_HDR
```

用于多生产者单消费者（MPSC）数据包处理的数据。

定义位置（Definition）：log_frontend_stmesp_demux.h:91。

符号定位：[log_frontend_stmesp_demux_packet_generic::MPSC_PBUF_HDR](../observability/P038_STMESP通用数据包.md#ac202cf6bc5bc8699a858e10de2c0c492)。

### `log_frontend_stmesp_demux_trace_point`

携带跟踪点（Trace Point）的数据包。

定义位置（Definition）：log_frontend_stmesp_demux.h:125。

符号定位：[log_frontend_stmesp_demux_trace_point](../observability/P040_STMESP跟踪点数据包.md)。

### `log_frontend_stmesp_demux_trace_point::has_data`

```c
uint64_t has_data
```

表示跟踪点是否携带数据的标志。

定义位置（Definition）：log_frontend_stmesp_demux.h:136。

符号定位：[log_frontend_stmesp_demux_trace_point::has_data](../observability/P040_STMESP跟踪点数据包.md#a0bdc2a3e1afb5748e08e68617f2ccbb6)。

### `log_frontend_stmesp_demux_trace_point::source_id`

```c
uint16_t source_id
```

源编号（Source ID），用于压缩日志（Compressed Logging）。

定义位置（Definition）：log_frontend_stmesp_demux.h:145。

符号定位：[log_frontend_stmesp_demux_trace_point::source_id](../observability/P040_STMESP跟踪点数据包.md#a0ca97d4ffd9bae1d640b8f99c8bd5ace)。

### `log_frontend_stmesp_demux_trace_point::content_invalid`

```c
uint64_t content_invalid
```

表示数据包是否有效的标志（Validity Flag）。

定义位置（Definition）：log_frontend_stmesp_demux.h:133。

符号定位：[log_frontend_stmesp_demux_trace_point::content_invalid](../observability/P040_STMESP跟踪点数据包.md#a300adc8bd0882810ae4a5759a76857ce)。

### `log_frontend_stmesp_demux_trace_point::timestamp`

```c
uint64_t timestamp
```

时间戳（Timestamp）。

定义位置（Definition）：log_frontend_stmesp_demux.h:139。

符号定位：[log_frontend_stmesp_demux_trace_point::timestamp](../observability/P040_STMESP跟踪点数据包.md#a6e1892f15fa3149f8161a1792420ba73)。

### `log_frontend_stmesp_demux_trace_point::type`

```c
uint64_t type
```

类型（Type）。

定义位置（Definition）：log_frontend_stmesp_demux.h:130。

符号定位：[log_frontend_stmesp_demux_trace_point::type](../observability/P040_STMESP跟踪点数据包.md#ab250b6782df720df3d1cdb37ab25a024)。

### `log_frontend_stmesp_demux_trace_point::major`

```c
uint64_t major
```

Major编号（Major ID）。

定义位置（Definition）：log_frontend_stmesp_demux.h:142。

符号定位：[log_frontend_stmesp_demux_trace_point::major](../observability/P040_STMESP跟踪点数据包.md#acfa056769b9ba00b945e1ff7d1e4cdb9)。

### `log_frontend_stmesp_demux_trace_point::data`

```c
uint32_t data
```

内容（Content）。

定义位置（Definition）：log_frontend_stmesp_demux.h:151。

符号定位：[log_frontend_stmesp_demux_trace_point::data](../observability/P040_STMESP跟踪点数据包.md#ada954ed2971c2fc720a1d1f2634c0e2a)。

### `log_frontend_stmesp_demux_trace_point::MPSC_PBUF_HDR`

```c
MPSC_PBUF_HDR
```

用于多生产者单消费者（MPSC）数据包处理的数据。

定义位置（Definition）：log_frontend_stmesp_demux.h:127。

符号定位：[log_frontend_stmesp_demux_trace_point::MPSC_PBUF_HDR](../observability/P040_STMESP跟踪点数据包.md#ae3e776e4a470ccb3abd8f6a73ce7b21b)。

### `log_frontend_stmesp_demux_trace_point::id`

```c
uint16_t id
```

编号（ID）。

定义位置（Definition）：log_frontend_stmesp_demux.h:148。

符号定位：[log_frontend_stmesp_demux_trace_point::id](../observability/P040_STMESP跟踪点数据包.md#aeb86bfae01245a4778d08ac9c1ee138a)。

### `log_frontend_stmesp_demux_header`

用于向日志消息头写入原始数据的联合体（Union）。

定义位置（Definition）：log_frontend_stmesp_demux.h:80。

符号定位：[log_frontend_stmesp_demux_header](../observability/P037_STMESP消息头联合体.md)。

### `log_frontend_stmesp_demux_header::raw`

```c
uint32_t raw
```

原始字（Raw Word）。

定义位置（Definition）：log_frontend_stmesp_demux.h:85。

符号定位：[log_frontend_stmesp_demux_header::raw](../observability/P037_STMESP消息头联合体.md#ae868e8f2e8b0623781d3f9377490c72a)。

### `log_frontend_stmesp_demux_header::log`

```c
struct log_frontend_stmesp_demux_log_header log
```

日志头结构（Log Header Structure）。

定义位置（Definition）：log_frontend_stmesp_demux.h:82。

符号定位：[log_frontend_stmesp_demux_header::log](../observability/P037_STMESP消息头联合体.md#ae94bab609a4f5c51eef7886db712420d)。

### `log_frontend_stmesp_demux_packet`

包含所有数据包类型的联合体（Union）。

定义位置（Definition）：log_frontend_stmesp_demux.h:173。

符号定位：[log_frontend_stmesp_demux_packet](../observability/P042_STMESP数据包联合体.md)。

### `log_frontend_stmesp_demux_packet::generic_packet`

```c
struct log_frontend_stmesp_demux_packet_generic * generic_packet
```

指向通用log_frontend_stmesp_demux数据包的指针。

定义位置（Definition）：log_frontend_stmesp_demux.h:190。

符号定位：[log_frontend_stmesp_demux_packet::generic_packet](../observability/P042_STMESP数据包联合体.md#a30d3cfc6071bebc1614f2f67c8a950c7)。

### `log_frontend_stmesp_demux_packet::trace_point`

```c
struct log_frontend_stmesp_demux_trace_point * trace_point
```

指向跟踪点消息（Trace Point Message）的指针。

定义位置（Definition）：log_frontend_stmesp_demux.h:184。

符号定位：[log_frontend_stmesp_demux_packet::trace_point](../observability/P042_STMESP数据包联合体.md#aa68b1022f97c8806ee430a541190fc82)。

### `log_frontend_stmesp_demux_packet::rgeneric`

```c
const union mpsc_pbuf_generic * rgeneric
```

指向通用mpsc_pbuf只读数据包的指针。

定义位置（Definition）：log_frontend_stmesp_demux.h:175。

符号定位：[log_frontend_stmesp_demux_packet::rgeneric](../observability/P042_STMESP数据包联合体.md#ac712f4dc2ca645e2ba6f6c638b41bf10)。

### `log_frontend_stmesp_demux_packet::log`

```c
struct log_frontend_stmesp_demux_log * log
```

指向日志消息（Log Message）的指针。

定义位置（Definition）：log_frontend_stmesp_demux.h:181。

符号定位：[log_frontend_stmesp_demux_packet::log](../observability/P042_STMESP数据包联合体.md#ac75deeb2f665aeb5dcfd94090aa1a1cf)。

### `log_frontend_stmesp_demux_packet::hw_event`

```c
struct log_frontend_stmesp_demux_hw_event * hw_event
```

指向硬件事件消息（HW Event Message）的指针。

定义位置（Definition）：log_frontend_stmesp_demux.h:187。

符号定位：[log_frontend_stmesp_demux_packet::hw_event](../observability/P042_STMESP数据包联合体.md#ae764f7a3b04e66af22c52aa1d52a441e)。

### `mpsc_pbuf_generic`

通用数据包头（Generic Packet Header）。

定义位置（Definition）：mpsc_packet.h:49。

符号定位：[mpsc_pbuf_generic](../intercore_reference/P175_MPSC数据包通用联合体.md)。

## 2.4\_源码跟踪译注

> 译注——解复用器（Demultiplexer）接收STPv2流中已识别的Major、Channel、数据、时间戳和Flag事件，并组装日志、跟踪点或硬件事件包。数据结构中的Major索引与原始Master ID需要结合配置映射理解。

> 译注——claim返回借用的数据包，消费者处理结束后用free归还。当前实现会自动释放并跳过content_invalid置位的包；无可领取包时联合体中的指针为空。原字段说明写作有效性标志，源码中1实际表示内容无效。

> 译注——reset把尚未完成的消息标记为无效并提交，增加丢弃计数，释放活动条目并清除当前Major/Channel状态；它不等价于重新初始化全部状态。get_dropped读取计数后会清零。

> 译注——源码初始化用source_id_buf_len除以m_ids_cnt来计算每个Major的来源缓存长度；调用方必须提供有效、非零的Major数量及满足接口倍数要求的缓冲配置。不要仅依据返回-EINVAL的声明推断实现已检查所有无效输入。

头文件定位：[include/zephyr/logging/log_frontend_stmesp_demux.h](../../../include/zephyr/logging/log_frontend_stmesp_demux.h)，关联实现／接口：[subsys/logging/frontends/log_frontend_stmesp_demux.c](../../../subsys/logging/frontends/log_frontend_stmesp_demux.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_frontend_stmesp_demux.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/log_frontend_stmesp_demux.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../observability/P048_STMESP日志解复用头文件.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/mpsc_packet.h](../intercore_reference/P176_MPSC数据包描述头文件参考.md)
- [log_frontend_stmesp_demux_log_header](../observability/P036_STMESP日志消息头.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [major](../observability/P036_STMESP日志消息头.md#acec1720948196deb1f09ab1ea443ecb9)
- [LOG_FRONTEND_STMESP_DEMUX_MAJOR_BITS](../observability/P032_STMESP日志解复用接口.md#ga33581c39a57eca7f96fea9c29386a3e3)
- [level](../observability/P036_STMESP日志消息头.md#a3b1474632ab446d8c9d590fb4bd8e420)
- [LOG_FRONTEND_STMESP_DEMUX_LEVEL_BITS](../observability/P032_STMESP日志解复用接口.md#gaf2b7019394d33a082fec5ab2d2785257)
- [total_len](../observability/P036_STMESP日志消息头.md#a138b653d76c50c0454210b7a1d7ec60b)
- [LOG_FRONTEND_STMESP_DEMUX_TLENGTH_BITS](../observability/P032_STMESP日志解复用接口.md#gaeaf76dcb74836740115c9b6e3fece73b)
- [package_len](../observability/P036_STMESP日志消息头.md#a0a378b7740a3def454bf34fe54927aa1)
- [LOG_FRONTEND_STMESP_DEMUX_PLENGTH_BITS](../observability/P032_STMESP日志解复用接口.md#ga56ad2b8067d56b9ccedefd57ad5aa0c2)
- [has_data](../observability/P036_STMESP日志消息头.md#ae18c81e29011d48e548a7daec2a3f9ba)
- [LOG_FRONTEND_STMESP_DEMUX_HAS_DATA_BITS](../observability/P032_STMESP日志解复用接口.md#ga4ac8c23bbf2eaf23a73698e3e36a9594)
- [log_frontend_stmesp_demux_header](../observability/P037_STMESP消息头联合体.md)
- [log](../observability/P037_STMESP消息头联合体.md#ae94bab609a4f5c51eef7886db712420d)
- [raw](../observability/P037_STMESP消息头联合体.md#ae868e8f2e8b0623781d3f9377490c72a)
- [log_frontend_stmesp_demux_packet_generic](../observability/P038_STMESP通用数据包.md)
- [MPSC_PBUF_HDR](../observability/P038_STMESP通用数据包.md#ac202cf6bc5bc8699a858e10de2c0c492)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [type](../observability/P038_STMESP通用数据包.md#a7a86c5de5e5b33830d963add116c1feb)
- [content_invalid](../observability/P038_STMESP通用数据包.md#a42d6b5192e0f9ba897a2986d645c6a6c)
- [log_frontend_stmesp_demux_log](../observability/P039_STMESP日志数据包.md)
- [MPSC_PBUF_HDR](../observability/P039_STMESP日志数据包.md#ad25f0378c2c3ba3d153a58a843704033)
- [type](../observability/P039_STMESP日志数据包.md#adb1b61bdca3a97df2c8ba2b34fc2ebff)
- [content_invalid](../observability/P039_STMESP日志数据包.md#a84cf9f64d96e87cfd2bb9d859fed3886)
- [timestamp](../observability/P039_STMESP日志数据包.md#af2b9820efce6f58d655b08a306c8d8d1)
- [hdr](../observability/P039_STMESP日志数据包.md#aa5b7175e05dbdcc41d75c5412ce30b15)
- [padding](../observability/P039_STMESP日志数据包.md#ab063e3ed4d81cbdb4ec417508c55bd13)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../observability/P039_STMESP日志数据包.md#ae8c62ffd8a11fbcebce29ed934f52597)
- [log_frontend_stmesp_demux_trace_point](../observability/P040_STMESP跟踪点数据包.md)
- [MPSC_PBUF_HDR](../observability/P040_STMESP跟踪点数据包.md#ae3e776e4a470ccb3abd8f6a73ce7b21b)
- [type](../observability/P040_STMESP跟踪点数据包.md#ab250b6782df720df3d1cdb37ab25a024)
- [content_invalid](../observability/P040_STMESP跟踪点数据包.md#a300adc8bd0882810ae4a5759a76857ce)
- [has_data](../observability/P040_STMESP跟踪点数据包.md#a0bdc2a3e1afb5748e08e68617f2ccbb6)
- [timestamp](../observability/P040_STMESP跟踪点数据包.md#a6e1892f15fa3149f8161a1792420ba73)
- [major](../observability/P040_STMESP跟踪点数据包.md#acfa056769b9ba00b945e1ff7d1e4cdb9)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [source_id](../observability/P040_STMESP跟踪点数据包.md#a0ca97d4ffd9bae1d640b8f99c8bd5ace)
- [id](../observability/P040_STMESP跟踪点数据包.md#aeb86bfae01245a4778d08ac9c1ee138a)
- [data](../observability/P040_STMESP跟踪点数据包.md#ada954ed2971c2fc720a1d1f2634c0e2a)
- [log_frontend_stmesp_demux_hw_event](../observability/P041_STMESP硬件事件数据包.md)
- [MPSC_PBUF_HDR](../observability/P041_STMESP硬件事件数据包.md#a6a060e7fbda81c47eaa8088f3e45052a)
- [type](../observability/P041_STMESP硬件事件数据包.md#a5a781f1b681ef2499bf9ba2635261d4f)
- [content_invalid](../observability/P041_STMESP硬件事件数据包.md#ae6872dcd7e11eeb431e3d990ccdad243)
- [timestamp](../observability/P041_STMESP硬件事件数据包.md#a0766f3aa6163ea1a197d674eac00305b)
- [evt](../observability/P041_STMESP硬件事件数据包.md#a090039b38d646812a292510476d16644)
- [log_frontend_stmesp_demux_packet](../observability/P042_STMESP数据包联合体.md)
- [mpsc_pbuf_generic](../intercore_reference/P175_MPSC数据包通用联合体.md)
- [rgeneric](../observability/P042_STMESP数据包联合体.md#ac712f4dc2ca645e2ba6f6c638b41bf10)
- [log](../observability/P042_STMESP数据包联合体.md#ac75deeb2f665aeb5dcfd94090aa1a1cf)
- [trace_point](../observability/P042_STMESP数据包联合体.md#aa68b1022f97c8806ee430a541190fc82)
- [hw_event](../observability/P042_STMESP数据包联合体.md#ae764f7a3b04e66af22c52aa1d52a441e)
- [generic_packet](../observability/P042_STMESP数据包联合体.md#a30d3cfc6071bebc1614f2f67c8a950c7)
- [log_frontend_stmesp_demux_config](../observability/P043_STMESP解复用配置.md)
- [m_ids](../observability/P043_STMESP解复用配置.md#ada2f243b112324e99a53b831211cabce)
- [m_ids_cnt](../observability/P043_STMESP解复用配置.md#ad248eabec1eee58f5ef689004d5c7017)
- [source_id_buf](../observability/P043_STMESP解复用配置.md#aca85e1b671127e8803423f22b2d45a33)
- [source_id_buf_len](../observability/P043_STMESP解复用配置.md#a643b5bd780342bf1944e5a63274aa305)
- [log_frontend_stmesp_demux_init](../observability/P032_STMESP日志解复用接口.md#ga97f9ac1d7b459e9d3d715b5367e29a31)
- [log_frontend_stmesp_demux_major](../observability/P032_STMESP日志解复用接口.md#ga8be4ca332fa9145fad72a6b45245a9ff)
- [log_frontend_stmesp_demux_channel](../observability/P032_STMESP日志解复用接口.md#ga4f86c0cfb38fa05389462045019a6650)
- [log_frontend_stmesp_demux_packet_start](../observability/P032_STMESP日志解复用接口.md#gaed29a1869e710cd95c19c48c67a36aa8)
- [log_frontend_stmesp_demux_log0](../observability/P032_STMESP日志解复用接口.md#ga6a25dd796a8759009e14b5770f7653a9)
- [log_frontend_stmesp_demux_source_id](../observability/P032_STMESP日志解复用接口.md#gae5925a640c401cc09dd744945eafd51c)
- [log_frontend_stmesp_demux_timestamp](../observability/P032_STMESP日志解复用接口.md#ga184cc4d266a010aa094a45aba0fad638)
- [log_frontend_stmesp_demux_data](../observability/P032_STMESP日志解复用接口.md#ga235c0d680cb674b6e99d886497f257d5)
- [log_frontend_stmesp_demux_packet_end](../observability/P032_STMESP日志解复用接口.md#ga38e05a234824b0adbeca16cb3e21cc75)
- [log_frontend_stmesp_demux_get_dropped](../observability/P032_STMESP日志解复用接口.md#gaa624af8e67b4be013f0ec1507d805c34)
- [log_frontend_stmesp_demux_claim](../observability/P032_STMESP日志解复用接口.md#gaf7b66578311278e6d58312ea239c9c0c)
- [log_frontend_stmesp_demux_free](../observability/P032_STMESP日志解复用接口.md#gad9c13b59d1e09a240ed35b03b04b1a96)
- [log_frontend_stmesp_demux_sname_get](../observability/P032_STMESP日志解复用接口.md#ga10621a1e4c5b875650b3ff89b3e97297)
- [log_frontend_stmesp_demux_str_get](../observability/P032_STMESP日志解复用接口.md#ga7c692b9d84aedfb30673a58959465ccf)
- [log_frontend_stmesp_demux_is_idle](../observability/P032_STMESP日志解复用接口.md#ga1d693b8936666f7b352fd7e25535ac16)
- [log_frontend_stmesp_demux_reset](../observability/P032_STMESP日志解复用接口.md#ga487c9163e6477a879136350d4c109641)
- [log_frontend_stmesp_demux_max_utilization](../observability/P032_STMESP日志解复用接口.md#ga7be93bc9ad1ecfe37f5af64adf029f39)

---

[上一章](P001_STMESP日志前端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P003_STMESP底层头文件参考.md)
