---
id: learning.zephyr-docs.api-source-supplement-reference.page-118
title: mqtt_sn.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_mqtt\_sn.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h.html)。

## 118.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00060"></a>
<a id="l00067"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
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
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00274"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__mqtt__sn__socket_html_ga0850d89af7dd6b5d3ec2b1e1abe01d19"></a>
<a id="agroup__mqtt__sn__socket_html_ga1a6b39984ef047f0089cea43f5378d0f"></a>
<a id="agroup__mqtt__sn__socket_html_ga1bcd2a0f52610708bebb4b3b6d6cbf35"></a>
<a id="agroup__mqtt__sn__socket_html_ga434c3626ceaf3a9b60c5ffb75e9b5b56"></a>
<a id="agroup__mqtt__sn__socket_html_ga67d69e4e3f00b31b5ea3b37fb6d653b1"></a>
<a id="agroup__mqtt__sn__socket_html_ga8072226d2d96e184137ef40775389786"></a>
<a id="agroup__mqtt__sn__socket_html_ga8c2a525f1c30e5d5ff37180d33a76d4d"></a>
<a id="agroup__mqtt__sn__socket_html_ga90ced79565deb9a92be8cd3a99d808b7"></a>
<a id="agroup__mqtt__sn__socket_html_ga9b481db6d39dee05e2c58d4c721fe0a5"></a>
<a id="agroup__mqtt__sn__socket_html_gaa52518be4aa308dda9552e14d0045c42"></a>
<a id="agroup__mqtt__sn__socket_html_gaab8c9d8ddbaa2af542fdcd3e4178ea9e"></a>
<a id="agroup__mqtt__sn__socket_html_gab9cba16f8ce06f606ee81e0d34deb862"></a>
<a id="agroup__mqtt__sn__socket_html_gabca9262da31b09086b0f802d15eea3fd"></a>
<a id="agroup__mqtt__sn__socket_html_gadd0a809d7e451df55540fb7ea227fd50"></a>
<a id="agroup__mqtt__sn__socket_html_gadd38840ebc78217a692748afb704b42b"></a>
<a id="agroup__mqtt__sn__socket_html_gade962a4da5311a403893ba24714dc332"></a>
<a id="agroup__mqtt__sn__socket_html_gae6a3f7a7762653474df97364ef69fc74"></a>
<a id="agroup__mqtt__sn__socket_html_gaecd8b966f3e2112261993f8a2cd5c94a"></a>
<a id="agroup__mqtt__sn__socket_html_gaf29a6339419ea02052fe53a18bb8e5ee"></a>
<a id="agroup__mqtt__sn__socket_html_gafa1f81168d44152ad72c5f3d1c744b49"></a>
<a id="agroup__mqtt__sn__socket_html_gafdf80b1de5d1b069b2f75b2bd688416f"></a>
<a id="agroup__mqtt__sn__socket_html_gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9"></a>
<a id="agroup__mqtt__sn__socket_html_gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4"></a>
<a id="agroup__mqtt__sn__socket_html_gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da"></a>
<a id="agroup__mqtt__sn__socket_html_gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a"></a>
<a id="agroup__mqtt__sn__socket_html_ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83"></a>
<a id="agroup__mqtt__sn__socket_html_ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c"></a>
<a id="agroup__mqtt__sn__socket_html_ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7"></a>
<a id="agroup__mqtt__sn__socket_html_ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5"></a>
<a id="agroup__mqtt__sn__socket_html_ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3"></a>
<a id="agroup__mqtt__sn__socket_html_ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b"></a>
<a id="agroup__mqtt__sn__socket_html_ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b"></a>
<a id="agroup__mqtt__sn__socket_html_ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="anet__buf_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructmqtt__sn__client_html"></a>
<a id="astructmqtt__sn__client_html_a02a38427caa60c51f85661efe58813f6"></a>
<a id="astructmqtt__sn__client_html_a05b83c732ed9199dac0110cfb1e56563"></a>
<a id="astructmqtt__sn__client_html_a1b2ceae7b3fe37ebd2f3ecd8387565d3"></a>
<a id="astructmqtt__sn__client_html_a2be2f7d041f325dda14007864e03fb70"></a>
<a id="astructmqtt__sn__client_html_a306887539a950e2f0b3ad6da40519ba3"></a>
<a id="astructmqtt__sn__client_html_a32efbccbf7b1820ff5092896130e6b7e"></a>
<a id="astructmqtt__sn__client_html_a3802bd92a42e421a5d733c64b53473db"></a>
<a id="astructmqtt__sn__client_html_a42d76db9cbcc9770246241283bb65486"></a>
<a id="astructmqtt__sn__client_html_a65bb52c8a5ecbd81e743fdc7c213b43a"></a>
<a id="astructmqtt__sn__client_html_a7d5aa6955be3c30a5569cf9730a2f3f3"></a>
<a id="astructmqtt__sn__client_html_a96748b082edf64987a867f9a2e32dca2"></a>
<a id="astructmqtt__sn__client_html_a9cbf86052061b55a93356346cae75e8b"></a>
<a id="astructmqtt__sn__client_html_a9d2397f5ff59a51630f5b82f94c92327"></a>
<a id="astructmqtt__sn__client_html_a9ec4ff19f5cfef074ad9f5a34dd35eff"></a>
<a id="astructmqtt__sn__client_html_aa1501b32ef99547d99a1c03a29433748"></a>
<a id="astructmqtt__sn__client_html_aa47e6426ca7e8434734377a85f586b84"></a>
<a id="astructmqtt__sn__client_html_ac2b8e9d7d4c246c5d5538922a1e9887b"></a>
<a id="astructmqtt__sn__client_html_ad8f5b3b7815033cfecda7519ca657724"></a>
<a id="astructmqtt__sn__client_html_ae79d55b3148233cf44afe97e810f9fad"></a>
<a id="astructmqtt__sn__client_html_aec0d4d3f436d7c7d40e2548d7c6575c1"></a>
<a id="astructmqtt__sn__client_html_aec40ceeac5a4160b058ee6a7676ec68f"></a>
<a id="astructmqtt__sn__client_html_af400a2f993c27e0f25a4325daeacee28"></a>
<a id="astructmqtt__sn__client_html_af6e609481e40f4382898b53d12b4aa88"></a>
<a id="astructmqtt__sn__client_html_af70196b9800123e2f9c36362cfb8b6be"></a>
<a id="astructmqtt__sn__connect__retry_html"></a>
<a id="astructmqtt__sn__connect__retry_html_a0bc18dbe3eeb1d0f40df40c7043e30dd"></a>
<a id="astructmqtt__sn__connect__retry_html_a5224c27cbd657bae4e1dbbbc01bac2bd"></a>
<a id="astructmqtt__sn__connect__retry_html_a63ad57a516060561cdb8368fc39b95bf"></a>
<a id="astructmqtt__sn__connect__retry_html_ad863eef56bb80ea87a3924d4b00995a6"></a>
<a id="astructmqtt__sn__connect__retry_html_adc9e9a043233d291ce6a5cd02e22e16f"></a>
<a id="astructmqtt__sn__data_html"></a>
<a id="astructmqtt__sn__data_html_a3ceba49fc5a2a1cafe2d8dc0a2b56dae"></a>
<a id="astructmqtt__sn__data_html_ae3726684337ee8175224d11dfcf4a7c6"></a>
<a id="astructmqtt__sn__evt_html"></a>
<a id="astructmqtt__sn__evt_html_a8e75d71d1b38e1b84bf1ad20063ec4e8"></a>
<a id="astructmqtt__sn__evt_html_aef636c6acdc17831acb44095fbef1885"></a>
<a id="astructmqtt__sn__transport_html"></a>
<a id="astructmqtt__sn__transport_html_a1a94f8c7facf9997d1bff237ef2f2503"></a>
<a id="astructmqtt__sn__transport_html_a3486cb5d56fb42db4c1f62ef9a6bb75b"></a>
<a id="astructmqtt__sn__transport_html_a700e8b1f1d541b90da76f050d492fb7a"></a>
<a id="astructmqtt__sn__transport_html_af51e433970bed12b5217c63416d0ec4c"></a>
<a id="astructmqtt__sn__transport_html_af6f8c4904857664d14a578a9ead178e4"></a>
<a id="astructmqtt__sn__will__update_html"></a>
<a id="astructmqtt__sn__will__update_html_a329934f8b34ccea260e429c815fe8ea6"></a>
<a id="astructmqtt__sn__will__update_html_a4d154a06ee21a2ac606642443b8aab98"></a>
<a id="astructmqtt__sn__will__update_html_a5563460ce89861a00f4f2a8056c67068"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="aunionmqtt__sn__evt__param_html"></a>
<a id="aunionmqtt__sn__evt__param_html_a2440375957dae427bb61526331052567"></a>
<a id="aunionmqtt__sn__evt__param_html_ab7930bb48e91a24a79593e375f17cdf1"></a>
<a id="aunionmqtt__sn__evt__param_html_ae79e9793f8fc70cc781c4527d8f8496d"></a>
<a id="aunionmqtt__sn__evt__param_html_afa0ea7d03a7ffdc95c68848af4c9f3ae"></a>

```c
/*
 * Copyright (c) 2022 René Beckmann
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MQTT_SN_H_
#define ZEPHYR_INCLUDE_NET_MQTT_SN_H_

#include <stddef.h>

#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/types.h>

#include <sys/types.h>

#ifdef CONFIG_MQTT_SN_TRANSPORT_UDP
#include <zephyr/net/net_ip.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif

enum mqtt_sn_qos {
        MQTT_SN_QOS_0,
        MQTT_SN_QOS_1,
        MQTT_SN_QOS_2,
        MQTT_SN_QOS_M1
};

enum mqtt_sn_topic_type {
        MQTT_SN_TOPIC_TYPE_NORMAL,
        MQTT_SN_TOPIC_TYPE_PREDEF,
        MQTT_SN_TOPIC_TYPE_SHORT
};

enum mqtt_sn_return_code {
        MQTT_SN_CODE_ACCEPTED = 0x00,
        MQTT_SN_CODE_REJECTED_CONGESTION = 0x01,
        MQTT_SN_CODE_REJECTED_TOPIC_ID = 0x02,
        MQTT_SN_CODE_REJECTED_NOTSUP = 0x03,
};

struct mqtt_sn_data {
        const uint8_t *data;
        size_t size;
};

#define MQTT_SN_DATA_STRING_LITERAL(literal) ((struct mqtt_sn_data){literal, sizeof(literal) - 1})

#define MQTT_SN_DATA_BYTES(...)                                                                    \
        ((struct mqtt_sn_data){(uint8_t[]){__VA_ARGS__}, sizeof((uint8_t[]){__VA_ARGS__})})

enum mqtt_sn_evt_type {
        MQTT_SN_EVT_CONNECTED,
        MQTT_SN_EVT_DISCONNECTED,
        MQTT_SN_EVT_ASLEEP,
        MQTT_SN_EVT_AWAKE,
        MQTT_SN_EVT_PUBLISH,
        MQTT_SN_EVT_PINGRESP,
        MQTT_SN_EVT_ADVERTISE,
        MQTT_SN_EVT_GWINFO,
        MQTT_SN_EVT_SEARCHGW
};

union mqtt_sn_evt_param {
        struct {
                struct mqtt_sn_data data;
                enum mqtt_sn_topic_type topic_type;
                uint16_t topic_id;
        } publish;
};

struct mqtt_sn_evt {
        enum mqtt_sn_evt_type type;
        union mqtt_sn_evt_param param;
};

struct mqtt_sn_client;

typedef void (*mqtt_sn_evt_cb_t)(struct mqtt_sn_client *client, const struct mqtt_sn_evt *evt);

struct mqtt_sn_transport {
        int (*init)(struct mqtt_sn_transport *transport);

        void (*deinit)(struct mqtt_sn_transport *transport);

        int (*sendto)(struct mqtt_sn_transport *transport, void *buf, size_t sz,
                      const void *dest_addr, size_t addrlen);

        ssize_t (*recvfrom)(struct mqtt_sn_transport *transport, void *rx_buf, size_t rx_len,
                            void *src_addr, size_t *addrlen);

        int (*poll)(struct mqtt_sn_transport *transport);
};

#ifdef CONFIG_MQTT_SN_TRANSPORT_UDP
struct mqtt_sn_transport_udp {
        struct mqtt_sn_transport tp;

        int sock;

        union {
                struct net_sockaddr_storage bcaddr_storage;
                /* Use the bcaddr_storage instead of this one. */
                struct net_sockaddr bcaddr;
        };
        net_socklen_t bcaddrlen;
};

#define UDP_TRANSPORT(transport) CONTAINER_OF(transport, struct mqtt_sn_transport_udp, tp)

int mqtt_sn_transport_udp_init(struct mqtt_sn_transport_udp *udp, struct net_sockaddr *gwaddr,
                               net_socklen_t addrlen);
#endif

struct mqtt_sn_will_update {
        bool in_progress;

        uint8_t retries;

        int64_t last_attempt;
};

struct mqtt_sn_connect_retry {
        atomic_t state;

        uint8_t retries;

        int64_t last_attempt;

        bool will;

        bool clean_session;
};

struct mqtt_sn_client {
        struct mqtt_sn_data client_id;

        struct mqtt_sn_data will_topic;

        struct mqtt_sn_data will_msg;

        enum mqtt_sn_qos will_qos;

        bool will_retain;

        struct mqtt_sn_transport *transport;

        struct net_buf_simple tx;

        struct net_buf_simple rx;

        struct net_buf_simple rx_addr;

        mqtt_sn_evt_cb_t evt_cb;

        uint16_t next_msg_id;

        sys_slist_t publish;

        sys_slist_t topic;

        sys_slist_t gateways;

        int state;

        int64_t last_ping;

        uint8_t ping_retries;

        int64_t ts_searchgw;

        int64_t ts_gwinfo;

        uint8_t radius_gwinfo;

        struct mqtt_sn_connect_retry connect;

        struct mqtt_sn_will_update will_topic_update;

        struct mqtt_sn_will_update will_message_update;

        struct k_work_delayable process_work;
};

int mqtt_sn_client_init(struct mqtt_sn_client *client, const struct mqtt_sn_data *client_id,
                        struct mqtt_sn_transport *transport, mqtt_sn_evt_cb_t evt_cb, void *tx,
                        size_t txsz, void *rx, size_t rxsz);

void mqtt_sn_client_deinit(struct mqtt_sn_client *client);

int mqtt_sn_add_gw(struct mqtt_sn_client *client, uint8_t gw_id, struct mqtt_sn_data gw_addr);

int mqtt_sn_search(struct mqtt_sn_client *client, uint8_t radius);

int mqtt_sn_connect(struct mqtt_sn_client *client, bool will, bool clean_session);

int mqtt_sn_disconnect(struct mqtt_sn_client *client);

int mqtt_sn_sleep(struct mqtt_sn_client *client, uint16_t duration);

int mqtt_sn_subscribe(struct mqtt_sn_client *client, enum mqtt_sn_qos qos,
                      struct mqtt_sn_data *topic_name);

int mqtt_sn_unsubscribe(struct mqtt_sn_client *client, enum mqtt_sn_qos qos,
                        struct mqtt_sn_data *topic_name);

int mqtt_sn_publish(struct mqtt_sn_client *client, enum mqtt_sn_qos qos,
                    struct mqtt_sn_data *topic_name, bool retain, struct mqtt_sn_data *data);

int mqtt_sn_input(struct mqtt_sn_client *client);

int mqtt_sn_get_topic_name(struct mqtt_sn_client *client, uint16_t id,
                           struct mqtt_sn_data *topic_name);

int mqtt_sn_predefine_topic(struct mqtt_sn_client *client, uint16_t topic_id,
                            struct mqtt_sn_data *topic_name);

int mqtt_sn_define_short_topic(struct mqtt_sn_client *client, struct mqtt_sn_data *topic_name);

int mqtt_sn_update_will_topic(struct mqtt_sn_client *client);

int mqtt_sn_update_will_message(struct mqtt_sn_client *client);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_MQTT_SN_H_ */

```

## 118.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 René Beckmann。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 237 行

请使用 `bcaddr_storage` 代替此项。

### 注释 3：原第 588 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MQTT_SN_H_`。

## 118.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [mqtt_sn_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8072226d2d96e184137ef40775389786)
- [MQTT_SN_QOS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)
- [MQTT_SN_QOS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)
- [MQTT_SN_QOS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)
- [MQTT_SN_QOS_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)
- [mqtt_sn_topic_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gabca9262da31b09086b0f802d15eea3fd)
- [MQTT_SN_TOPIC_TYPE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)
- [MQTT_SN_TOPIC_TYPE_PREDEF](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)
- [MQTT_SN_TOPIC_TYPE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)
- [mqtt_sn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)
- [MQTT_SN_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)
- [MQTT_SN_CODE_REJECTED_CONGESTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)
- [MQTT_SN_CODE_REJECTED_TOPIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)
- [MQTT_SN_CODE_REJECTED_NOTSUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)
- [mqtt_sn_data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md#ae3726684337ee8175224d11dfcf4a7c6)
- [size](../network_application_model_reference/P069_mqtt_sn_data_结构体.md#a3ceba49fc5a2a1cafe2d8dc0a2b56dae)
- [mqtt_sn_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaa52518be4aa308dda9552e14d0045c42)
- [MQTT_SN_EVT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)
- [MQTT_SN_EVT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)
- [MQTT_SN_EVT_ASLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)
- [MQTT_SN_EVT_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)
- [MQTT_SN_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)
- [MQTT_SN_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)
- [MQTT_SN_EVT_ADVERTISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672)
- [MQTT_SN_EVT_GWINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a)
- [MQTT_SN_EVT_SEARCHGW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ggaa52518be4aa308dda9552e14d0045c42af22b276f7d74a04bfef13cdcd36c9b83)
- [mqtt_sn_evt_param](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md)
- [data](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#a2440375957dae427bb61526331052567)
- [topic_type](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#ab7930bb48e91a24a79593e375f17cdf1)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [topic_id](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#ae79e9793f8fc70cc781c4527d8f8496d)
- [publish](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#afa0ea7d03a7ffdc95c68848af4c9f3ae)
- [mqtt_sn_evt](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md)
- [type](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md#aef636c6acdc17831acb44095fbef1885)
- [param](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md#a8e75d71d1b38e1b84bf1ad20063ec4e8)
- [mqtt_sn_client](../network_application_model_reference/P067_mqtt_sn_client_结构体.md)
- [mqtt_sn_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaecd8b966f3e2112261993f8a2cd5c94a)
- [mqtt_sn_transport](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md)
- [init](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a3486cb5d56fb42db4c1f62ef9a6bb75b)
- [deinit](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#af51e433970bed12b5217c63416d0ec4c)
- [sendto](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a700e8b1f1d541b90da76f050d492fb7a)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [recvfrom](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a1a94f8c7facf9997d1bff237ef2f2503)
- [poll](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#af6f8c4904857664d14a578a9ead178e4)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [mqtt_sn_will_update](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md)
- [in_progress](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a4d154a06ee21a2ac606642443b8aab98)
- [retries](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a5563460ce89861a00f4f2a8056c67068)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [last_attempt](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a329934f8b34ccea260e429c815fe8ea6)
- [mqtt_sn_connect_retry](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a63ad57a516060561cdb8368fc39b95bf)
- [retries](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a0bc18dbe3eeb1d0f40df40c7043e30dd)
- [last_attempt](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#adc9e9a043233d291ce6a5cd02e22e16f)
- [will](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a5224c27cbd657bae4e1dbbbc01bac2bd)
- [clean_session](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#ad863eef56bb80ea87a3924d4b00995a6)
- [client_id](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9cbf86052061b55a93356346cae75e8b)
- [will_topic](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af70196b9800123e2f9c36362cfb8b6be)
- [will_msg](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9d2397f5ff59a51630f5b82f94c92327)
- [will_qos](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a42d76db9cbcc9770246241283bb65486)
- [will_retain](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ad8f5b3b7815033cfecda7519ca657724)
- [transport](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aec0d4d3f436d7c7d40e2548d7c6575c1)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [tx](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a3802bd92a42e421a5d733c64b53473db)
- [rx](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aec40ceeac5a4160b058ee6a7676ec68f)
- [rx_addr](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a306887539a950e2f0b3ad6da40519ba3)
- [evt_cb](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ac2b8e9d7d4c246c5d5538922a1e9887b)
- [next_msg_id](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a05b83c732ed9199dac0110cfb1e56563)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [publish](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a32efbccbf7b1820ff5092896130e6b7e)
- [topic](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aa47e6426ca7e8434734377a85f586b84)
- [gateways](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a96748b082edf64987a867f9a2e32dca2)
- [state](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a02a38427caa60c51f85661efe58813f6)
- [last_ping](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af400a2f993c27e0f25a4325daeacee28)
- [ping_retries](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a2be2f7d041f325dda14007864e03fb70)
- [ts_searchgw](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aa1501b32ef99547d99a1c03a29433748)
- [ts_gwinfo](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a1b2ceae7b3fe37ebd2f3ecd8387565d3)
- [radius_gwinfo](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9ec4ff19f5cfef074ad9f5a34dd35eff)
- [connect](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ae79d55b3148233cf44afe97e810f9fad)
- [will_topic_update](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af6e609481e40f4382898b53d12b4aa88)
- [will_message_update](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a7d5aa6955be3c30a5569cf9730a2f3f3)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [process_work](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a65bb52c8a5ecbd81e743fdc7c213b43a)
- [mqtt_sn_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gae6a3f7a7762653474df97364ef69fc74)
- [mqtt_sn_client_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga67d69e4e3f00b31b5ea3b37fb6d653b1)
- [mqtt_sn_add_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd38840ebc78217a692748afb704b42b)
- [mqtt_sn_search](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafdf80b1de5d1b069b2f75b2bd688416f)
- [mqtt_sn_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga8c2a525f1c30e5d5ff37180d33a76d4d)
- [mqtt_sn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gab9cba16f8ce06f606ee81e0d34deb862)
- [mqtt_sn_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gaf29a6339419ea02052fe53a18bb8e5ee)
- [mqtt_sn_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga9b481db6d39dee05e2c58d4c721fe0a5)
- [mqtt_sn_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1bcd2a0f52610708bebb4b3b6d6cbf35)
- [mqtt_sn_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga434c3626ceaf3a9b60c5ffb75e9b5b56)
- [mqtt_sn_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gafa1f81168d44152ad72c5f3d1c744b49)
- [mqtt_sn_get_topic_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gade962a4da5311a403893ba24714dc332)
- [mqtt_sn_predefine_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd0a809d7e451df55540fb7ea227fd50)
- [mqtt_sn_define_short_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1a6b39984ef047f0089cea43f5378d0f)
- [mqtt_sn_update_will_topic](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga90ced79565deb9a92be8cd3a99d808b7)
- [mqtt_sn_update_will_message](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga0850d89af7dd6b5d3ec2b1e1abe01d19)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [mqtt_sn_client::state](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a02a38427caa60c51f85661efe58813f6)
- [mqtt_sn_client::next_msg_id](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a05b83c732ed9199dac0110cfb1e56563)
- [mqtt_sn_client::ts_gwinfo](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a1b2ceae7b3fe37ebd2f3ecd8387565d3)
- [mqtt_sn_client::ping_retries](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a2be2f7d041f325dda14007864e03fb70)
- [mqtt_sn_client::rx_addr](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a306887539a950e2f0b3ad6da40519ba3)
- [mqtt_sn_client::publish](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a32efbccbf7b1820ff5092896130e6b7e)
- [mqtt_sn_client::tx](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a3802bd92a42e421a5d733c64b53473db)
- [mqtt_sn_client::will_qos](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a42d76db9cbcc9770246241283bb65486)
- [mqtt_sn_client::process_work](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a65bb52c8a5ecbd81e743fdc7c213b43a)
- [mqtt_sn_client::will_message_update](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a7d5aa6955be3c30a5569cf9730a2f3f3)
- [mqtt_sn_client::gateways](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a96748b082edf64987a867f9a2e32dca2)
- [mqtt_sn_client::client_id](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9cbf86052061b55a93356346cae75e8b)
- [mqtt_sn_client::will_msg](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9d2397f5ff59a51630f5b82f94c92327)
- [mqtt_sn_client::radius_gwinfo](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#a9ec4ff19f5cfef074ad9f5a34dd35eff)
- [mqtt_sn_client::ts_searchgw](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aa1501b32ef99547d99a1c03a29433748)
- [mqtt_sn_client::topic](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aa47e6426ca7e8434734377a85f586b84)
- [mqtt_sn_client::evt_cb](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ac2b8e9d7d4c246c5d5538922a1e9887b)
- [mqtt_sn_client::will_retain](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ad8f5b3b7815033cfecda7519ca657724)
- [mqtt_sn_client::connect](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#ae79d55b3148233cf44afe97e810f9fad)
- [mqtt_sn_client::transport](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aec0d4d3f436d7c7d40e2548d7c6575c1)
- [mqtt_sn_client::rx](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#aec40ceeac5a4160b058ee6a7676ec68f)
- [mqtt_sn_client::last_ping](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af400a2f993c27e0f25a4325daeacee28)
- [mqtt_sn_client::will_topic_update](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af6e609481e40f4382898b53d12b4aa88)
- [mqtt_sn_client::will_topic](../network_application_model_reference/P067_mqtt_sn_client_结构体.md#af70196b9800123e2f9c36362cfb8b6be)
- [mqtt_sn_connect_retry::retries](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a0bc18dbe3eeb1d0f40df40c7043e30dd)
- [mqtt_sn_connect_retry::will](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a5224c27cbd657bae4e1dbbbc01bac2bd)
- [mqtt_sn_connect_retry::state](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#a63ad57a516060561cdb8368fc39b95bf)
- [mqtt_sn_connect_retry::clean_session](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#ad863eef56bb80ea87a3924d4b00995a6)
- [mqtt_sn_connect_retry::last_attempt](../network_application_model_reference/P068_mqtt_sn_connect_retry_结构体.md#adc9e9a043233d291ce6a5cd02e22e16f)
- [mqtt_sn_data::size](../network_application_model_reference/P069_mqtt_sn_data_结构体.md#a3ceba49fc5a2a1cafe2d8dc0a2b56dae)
- [mqtt_sn_data::data](../network_application_model_reference/P069_mqtt_sn_data_结构体.md#ae3726684337ee8175224d11dfcf4a7c6)
- [mqtt_sn_evt::param](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md#a8e75d71d1b38e1b84bf1ad20063ec4e8)
- [mqtt_sn_evt::type](../network_application_model_reference/P070_mqtt_sn_evt_结构体.md#aef636c6acdc17831acb44095fbef1885)
- [mqtt_sn_transport::recvfrom](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a1a94f8c7facf9997d1bff237ef2f2503)
- [mqtt_sn_transport::init](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a3486cb5d56fb42db4c1f62ef9a6bb75b)
- [mqtt_sn_transport::sendto](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#a700e8b1f1d541b90da76f050d492fb7a)
- [mqtt_sn_transport::deinit](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#af51e433970bed12b5217c63416d0ec4c)
- [mqtt_sn_transport::poll](../network_application_model_reference/P071_mqtt_sn_transport_结构体.md#af6f8c4904857664d14a578a9ead178e4)
- [mqtt_sn_will_update::last_attempt](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a329934f8b34ccea260e429c815fe8ea6)
- [mqtt_sn_will_update::in_progress](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a4d154a06ee21a2ac606642443b8aab98)
- [mqtt_sn_will_update::retries](../network_application_model_reference/P072_mqtt_sn_will_update_结构体.md#a5563460ce89861a00f4f2a8056c67068)
- [mqtt_sn_evt_param::data](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#a2440375957dae427bb61526331052567)
- [mqtt_sn_evt_param::topic_type](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#ab7930bb48e91a24a79593e375f17cdf1)
- [mqtt_sn_evt_param::topic_id](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#ae79e9793f8fc70cc781c4527d8f8496d)
- [mqtt_sn_evt_param::publish](../network_application_model_reference/P092_mqtt_sn_evt_param_联合体.md#afa0ea7d03a7ffdc95c68848af4c9f3ae)

---

[上一章](P117_mpipe_player.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P119_mqueue.h_源码浏览.md)
