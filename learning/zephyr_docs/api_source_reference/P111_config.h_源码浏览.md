---
id: learning.zephyr-docs.api-source-reference.page-111
title: config.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/config_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_config.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/config_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/config_8h.html)。

## 111.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00114"></a>
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
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00154"></a>
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
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00202"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="agroup__hawkbit__config_html_ga0ca5f633e902137ecda068ab312d52db"></a>
<a id="agroup__hawkbit__config_html_ga2c6aa606a003b34538b521fda77af903"></a>
<a id="agroup__hawkbit__config_html_ga3674fc406aa20fe4770ff0c729817b7c"></a>
<a id="agroup__hawkbit__config_html_ga46c56cee1a89abd81a328ef3f91648bb"></a>
<a id="agroup__hawkbit__config_html_ga5c73e9ba4dd9788e22fdb11f1f2b81ee"></a>
<a id="agroup__hawkbit__config_html_ga5e6a1e2e49b75a44a9f13f059ed7d3f6"></a>
<a id="agroup__hawkbit__config_html_ga694e5f4fbcae451eb90a019f6d1f3b81"></a>
<a id="agroup__hawkbit__config_html_ga78ef6a168132940040ad04498f0b462d"></a>
<a id="agroup__hawkbit__config_html_gaa2799669246cc817bb8e294a8fbfb3d2"></a>
<a id="agroup__hawkbit__config_html_gaa49efdafe94e1d36a537aff962df41d5"></a>
<a id="agroup__hawkbit__config_html_gaae46014585251b53afe726d42475d739"></a>
<a id="agroup__hawkbit__config_html_gacbbaed38e2ace7d8dcc78e40b286b5e9"></a>
<a id="agroup__hawkbit__config_html_gadc4aea2dac4915a434a10e6e055f54f7"></a>
<a id="agroup__hawkbit__config_html_gafd9f30b2acab65c34bcb5edaa3da8738"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhawkbit__runtime__config_html"></a>
<a id="astructhawkbit__runtime__config_html_a1fb0307aaeb6107428ae279108057af3"></a>
<a id="astructhawkbit__runtime__config_html_a33343e076372adca50c1bab528881565"></a>
<a id="astructhawkbit__runtime__config_html_a3efc42d340461934b96a55ec6d5b91d2"></a>
<a id="astructhawkbit__runtime__config_html_a519e5dbc87d0b472b87cb3dbf01a7807"></a>
<a id="astructhawkbit__runtime__config_html_aee3966a3387498d726ca960663b0b291"></a>
<a id="atls__credentials_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Vogl Electronic GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_MGMT_HAWKBIT_CONFIG_H_
#define ZEPHYR_INCLUDE_MGMT_HAWKBIT_CONFIG_H_

#include <stdint.h>
#include <zephyr/net/tls_credentials.h>

struct hawkbit_runtime_config {
        char *server_addr;
        char *server_domain;
        uint16_t server_port;
        char *auth_token;
        sec_tag_t tls_tag;
};

int hawkbit_set_config(struct hawkbit_runtime_config *config);

struct hawkbit_runtime_config hawkbit_get_config(void);

static inline int hawkbit_set_server_domain(char *domain_str)
{
        struct hawkbit_runtime_config set_config = {
                .server_addr = NULL,
                .server_domain = domain_str,
                .server_port = 0,
                .auth_token = NULL,
                .tls_tag = 0,
        };

        return hawkbit_set_config(&set_config);
}

static inline int hawkbit_set_server_addr(char *addr_str)
{
        struct hawkbit_runtime_config set_config = {
                .server_addr = addr_str,
                .server_domain = NULL,
                .server_port = 0,
                .auth_token = NULL,
                .tls_tag = 0,
        };

        return hawkbit_set_config(&set_config);
}

static inline int hawkbit_set_server_port(uint16_t port)
{
        struct hawkbit_runtime_config set_config = {
                .server_addr = NULL,
                .server_domain = NULL,
                .server_port = port,
                .auth_token = NULL,
                .tls_tag = 0,
        };

        return hawkbit_set_config(&set_config);
}

static inline int hawkbit_set_ddi_security_token(char *token)
{
        struct hawkbit_runtime_config set_config = {
                .server_addr = NULL,
                .server_domain = NULL,
                .server_port = 0,
                .auth_token = token,
                .tls_tag = 0,
        };

        return hawkbit_set_config(&set_config);
}

static inline int hawkbit_set_tls_tag(sec_tag_t tag)
{
        struct hawkbit_runtime_config set_config = {
                .server_addr = NULL,
                .server_domain = NULL,
                .server_port = 0,
                .auth_token = NULL,
                .tls_tag = tag,
        };

        return hawkbit_set_config(&set_config);
}

static inline char *hawkbit_get_server_addr(void)
{
        return hawkbit_get_config().server_addr;
}

static inline char *hawkbit_get_server_domain(void)
{
        return hawkbit_get_config().server_domain;
}

static inline uint16_t hawkbit_get_server_port(void)
{
        return hawkbit_get_config().server_port;
}

static inline char *hawkbit_get_ddi_security_token(void)
{
        return hawkbit_get_config().auth_token;
}

static inline sec_tag_t hawkbit_get_tls_tag(void)
{
        return hawkbit_get_config().tls_tag;
}

int32_t hawkbit_get_action_id(void);

uint32_t hawkbit_get_poll_interval(void);


#endif /* ZEPHYR_INCLUDE_MGMT_HAWKBIT_CONFIG_H_ */
```

## 111.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Vogl Electronic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 235 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_HAWKBIT_CONFIG_H_`。

## 111.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/config_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/net/tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [hawkbit_runtime_config](../firmware_update/P032_hawkBit运行时配置结构.md)
- [server_addr](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#aee3966a3387498d726ca960663b0b291)
- [server_domain](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a3efc42d340461934b96a55ec6d5b91d2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [server_port](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a33343e076372adca50c1bab528881565)
- [auth_token](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a519e5dbc87d0b472b87cb3dbf01a7807)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a1fb0307aaeb6107428ae279108057af3)
- [hawkbit_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)
- [hawkbit_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaae46014585251b53afe726d42475d739)
- [hawkbit_set_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga2c6aa606a003b34538b521fda77af903)
- [hawkbit_set_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa49efdafe94e1d36a537aff962df41d5)
- [hawkbit_set_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga78ef6a168132940040ad04498f0b462d)
- [hawkbit_set_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa2799669246cc817bb8e294a8fbfb3d2)
- [hawkbit_set_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)
- [hawkbit_get_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gacbbaed38e2ace7d8dcc78e40b286b5e9)
- [hawkbit_get_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gafd9f30b2acab65c34bcb5edaa3da8738)
- [hawkbit_get_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga3674fc406aa20fe4770ff0c729817b7c)
- [hawkbit_get_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gadc4aea2dac4915a434a10e6e055f54f7)
- [hawkbit_get_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga694e5f4fbcae451eb90a019f6d1f3b81)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [hawkbit_get_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga0ca5f633e902137ecda068ab312d52db)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hawkbit_get_poll_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga46c56cee1a89abd81a328ef3f91648bb)
- [hawkbit_runtime_config::tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a1fb0307aaeb6107428ae279108057af3)
- [hawkbit_runtime_config::server_port](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a33343e076372adca50c1bab528881565)
- [hawkbit_runtime_config::server_domain](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a3efc42d340461934b96a55ec6d5b91d2)
- [hawkbit_runtime_config::auth_token](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a519e5dbc87d0b472b87cb3dbf01a7807)
- [hawkbit_runtime_config::server_addr](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#aee3966a3387498d726ca960663b0b291)
- [tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)

---

[上一章](P110_common-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P112_confstr.h_源码浏览.md)
