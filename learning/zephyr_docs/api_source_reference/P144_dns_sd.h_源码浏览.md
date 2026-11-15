---
id: learning.zephyr-docs.api-source-reference.page-144
title: dns_sd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第144章\_dns\_sd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html)。

## 144.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00070"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00239"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="agroup__dns__sd_html_ga328d71e26411460b1b329db8f1ebd37b"></a>
<a id="agroup__dns__sd_html_ga6d68e785607089df42d534c2f876c6d5"></a>
<a id="agroup__dns__sd_html_gaeba098fa6d159067c70588cb60056277"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdns__sd__rec_html"></a>
<a id="astructdns__sd__rec_html_a06a8d777d302f99a7ed8f4ddb7e3af7d"></a>
<a id="astructdns__sd__rec_html_a714f196f0d5297d511d97f88c18aa993"></a>
<a id="astructdns__sd__rec_html_a852f246f90d3608acd3b660f57a59dfb"></a>
<a id="astructdns__sd__rec_html_ad282799583cde5b60ae19d5f919c67fc"></a>
<a id="astructdns__sd__rec_html_ad79c74e22f4546826b1de6c41402aa3e"></a>
<a id="astructdns__sd__rec_html_ae0585e5a0643a483d6ad12b7ff853323"></a>
<a id="astructdns__sd__rec_html_ae944cbdafdaced49f7302292d23ea4f8"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2020 Friedt Professional Engineering Services, Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_DNS_SD_H_
#define ZEPHYR_INCLUDE_NET_DNS_SD_H_

#include <stdint.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


#define DNS_SD_INSTANCE_MIN_SIZE 1
#define DNS_SD_INSTANCE_MAX_SIZE 63
#define DNS_SD_SERVICE_MIN_SIZE 2
#define DNS_SD_SERVICE_MAX_SIZE 16
#define DNS_SD_SERVICE_PREFIX '_'
#define DNS_SD_PROTO_SIZE 4
#define DNS_SD_DOMAIN_MIN_SIZE 2
#define DNS_SD_DOMAIN_MAX_SIZE 63

#define DNS_SD_MIN_LABELS 3
#define DNS_SD_MAX_LABELS 4

#define DNS_SD_REGISTER_SERVICE(_id, _instance, _service, _proto,       \
                                _domain, _text, _port)                  \
        static const STRUCT_SECTION_ITERABLE(dns_sd_rec, _id) = {       \
                .instance = _instance,                                  \
                .service = _service,                                    \
                .proto = _proto,                                        \
                .domain = _domain,                                      \
                .text = (const char *)_text,                            \
                .text_size = sizeof(_text) - 1,                         \
                .port = _port,                                          \
        }

#define DNS_SD_REGISTER_TCP_SERVICE(id, instance, service, domain, text, \
                                    port)                                \
        static const uint16_t id ## _port = sys_cpu_to_be16(port); \
        DNS_SD_REGISTER_SERVICE(id, instance, service, "_tcp", domain,   \
                                text, &id ## _port)

#define DNS_SD_REGISTER_UDP_SERVICE(id, instance, service, domain, text, \
                                    port)                                \
        static const uint16_t id ## _port = sys_cpu_to_be16(port); \
        DNS_SD_REGISTER_SERVICE(id, instance, service, "_udp", domain,   \
                                text, &id ## _port)

#define DNS_SD_EMPTY_TXT dns_sd_empty_txt

struct dns_sd_rec {
        const char *instance;
        const char *service;
        const char *proto;
        const char *domain;
        const char *text;
        size_t text_size;
        const uint16_t *port;
};


extern const char dns_sd_empty_txt[1];
extern const uint16_t dns_sd_port_zero;


static inline size_t dns_sd_txt_size(const struct dns_sd_rec *rec)
{
        return rec->text_size;
}

bool dns_sd_is_service_type_enumeration(const struct dns_sd_rec *rec);

void dns_sd_create_wildcard_filter(struct dns_sd_rec *filter);


#ifdef __cplusplus
};
#endif

#endif /* ZEPHYR_INCLUDE_NET_DNS_SD_H_ */
```

## 144.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2020 Friedt Professional Engineering Services, Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 294 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DNS_SD_H_`。

## 144.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)
- [instance](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a06a8d777d302f99a7ed8f4ddb7e3af7d)
- [service](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ae944cbdafdaced49f7302292d23ea4f8)
- [proto](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ad79c74e22f4546826b1de6c41402aa3e)
- [domain](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ad282799583cde5b60ae19d5f919c67fc)
- [text](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ae0585e5a0643a483d6ad12b7ff853323)
- [text_size](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a852f246f90d3608acd3b660f57a59dfb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [port](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a714f196f0d5297d511d97f88c18aa993)
- [dns_sd_txt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga6d68e785607089df42d534c2f876c6d5)
- [dns_sd_is_service_type_enumeration](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#gaeba098fa6d159067c70588cb60056277)
- [dns_sd_create_wildcard_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga328d71e26411460b1b329db8f1ebd37b)
- [dns_sd_rec::instance](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a06a8d777d302f99a7ed8f4ddb7e3af7d)
- [dns_sd_rec::port](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a714f196f0d5297d511d97f88c18aa993)
- [dns_sd_rec::text_size](../network_application_model_reference/P025_dns_sd_rec_结构体.md#a852f246f90d3608acd3b660f57a59dfb)
- [dns_sd_rec::domain](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ad282799583cde5b60ae19d5f919c67fc)
- [dns_sd_rec::proto](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ad79c74e22f4546826b1de6c41402aa3e)
- [dns_sd_rec::text](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ae0585e5a0643a483d6ad12b7ff853323)
- [dns_sd_rec::service](../network_application_model_reference/P025_dns_sd_rec_结构体.md#ae944cbdafdaced49f7302292d23ea4f8)
- [byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P143_dmop.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P145_domctl.h_源码浏览.md)
