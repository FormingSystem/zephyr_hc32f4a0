---
id: learning.zephyr-docs.api-source-supplement-reference.page-123
title: net_config.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_net\_config.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h.html)。

## 123.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00281"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__net__config_html_ga02a2b4fbac3eba68a175630293c91484"></a>
<a id="agroup__net__config_html_ga49c6b4cd9d338f1b3d76225a9872c84c"></a>
<a id="agroup__net__config_html_ga4d71cd03a40db9155b29fab43f7d5ec5"></a>
<a id="agroup__net__config_html_ga99750f4c2ede644821d00b399f0a1a9f"></a>
<a id="agroup__net__config_html_gab19ec1b3411f38d9bee5abcb25926ea0"></a>
<a id="agroup__net__config_html_gad1c288429f1178e165ed1429f87b3b81"></a>
<a id="agroup__ssh__keygen_html_ga233f6b99069e88b2fd16dd0fda0a25d2"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akeygen_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructnet__config__ssh__key_html"></a>
<a id="astructnet__config__ssh__key_html_a0c657f31a4d81cd74a86c6792372309a"></a>
<a id="astructnet__config__ssh__key_html_a38c70f14300a67b42bc452f219d35f69"></a>
<a id="astructnet__config__ssh__key_html_a823de7fc7e367493d8d9047cceda820a"></a>
<a id="astructnet__config__ssh__key_html_acacf33b3c455cf690a7eee7279facb27"></a>
<a id="astructnet__config__ssh__key_html_ad076498fe79bb8ecad52a78b694b17cb"></a>
<a id="astructnet__config__ssh__key_html_aed44f6ce3979e24a064f26eb71186733"></a>
<a id="astructnet__config__ssh__key_html_af44b05c8460c0657ea5c55e8860dee7e"></a>
<a id="astructnet__config__ssh__password__auth_html"></a>
<a id="astructnet__config__ssh__password__auth_html_a3fda745e9cc9696f301e2cd08c08786a"></a>
<a id="astructnet__config__ssh__password__auth_html_ae1e2e6c1ddafd2139effc4905f759119"></a>
<a id="astructnet__if_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_CONFIG_H_
#define ZEPHYR_INCLUDE_NET_NET_CONFIG_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/shell/shell.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/ssh/keygen.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Flags that tell what kind of functionality is needed by the client. */
#define NET_CONFIG_NEED_ROUTER 0x00000001

#define NET_CONFIG_NEED_IPV6   0x00000002

#define NET_CONFIG_NEED_IPV4   0x00000004

int net_config_init(const char *app_info, uint32_t flags, int32_t timeout);

int net_config_init_by_iface(struct net_if *iface, const char *app_info,
                             uint32_t flags, int32_t timeout);

int net_config_init_app(const struct device *dev, const char *app_info);

struct net_config_ssh_password_auth {
        const char *username;

        const char *password;
};

struct net_config_ssh_key {
        const char *key_name;

        uint8_t *key_buf;

        size_t key_buf_len;

        int key_id;

        enum ssh_host_key_type key_type;

        int key_bits;

        bool is_private;
};

#define NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC(name, key_bits)            \
        static uint8_t name[key_bits]

#define NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC(name, user_name, pwd) \
        static struct net_config_ssh_password_auth name = {             \
                .username = user_name,                                  \
                .password = pwd,                                        \
        }

#define NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC(name,                     \
                                              _key_buf_name,            \
                                              _key_buf_len,             \
                                              _key_name,                \
                                              _key_id,                  \
                                              _key_type,                \
                                              _key_bits)                \
        static struct net_config_ssh_key name = {                       \
                .key_buf = _key_buf_name,                               \
                .key_buf_len = _key_buf_len,                            \
                .key_name = _key_name,                                  \
                .key_id = _key_id,                                      \
                .key_type = _key_type,                                  \
                .key_bits = _key_bits,                                  \
                .is_private = true,                                     \
        }

#define NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC(name,                      \
                                             _key_buf_name,             \
                                             _key_buf_len,              \
                                             _key_name,                 \
                                             _key_id)                   \
        static struct net_config_ssh_key name = {                       \
                .key_buf = _key_buf_name,                               \
                .key_buf_len = _key_buf_len,                            \
                .key_name = _key_name,                                  \
                .key_id = _key_id,                                      \
                .key_bits = 0,                                          \
                .is_private = false,                                    \
        }

#if defined(CONFIG_SSH_SERVER)
int net_config_init_sshd(struct net_if *iface,
                         const struct net_config_ssh_key *priv_key_config,
                         const struct net_config_ssh_key *pub_key_config,
                         const struct net_config_ssh_password_auth *password_auth_config,
                         int sshd_instance);
#else
static inline int net_config_init_sshd(struct net_if *iface,
                        const struct net_config_ssh_key *priv_key_config,
                        const struct net_config_ssh_key *pub_key_config,
                        const struct net_config_ssh_password_auth *password_auth_config,
                        int sshd_instance)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(priv_key_config);
        ARG_UNUSED(pub_key_config);
        ARG_UNUSED(password_auth_config);
        ARG_UNUSED(sshd_instance);

        return -ENOTSUP;
}
#endif /* CONFIG_SSH_SERVER */

#if defined(CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)
int net_config_init_clock_via_sntp(void);
#else
static inline int net_config_init_clock_via_sntp(void)
{
        return -ENOTSUP;
}
#endif /* CONFIG_NET_CONFIG_CLOCK_SNTP_INIT */

#if defined(CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME)
int net_config_sntp_set_server(const char *server);
#else
static inline int net_config_sntp_set_server(const char *server)
{
        ARG_UNUSED(server);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_CONFIG_H_ */
```

## 123.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

指示客户端所需功能类型的标志。

### 注释 3：原第 295 行

条件编译配置（Configuration）标记：`CONFIG_SSH_SERVER`。

### 注释 4：原第 324 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`。

### 注释 5：原第 347 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME`。

### 注释 6：原第 357 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_CONFIG_H_`。

## 123.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/ssh/keygen.h](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html)
- [net_config_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga02a2b4fbac3eba68a175630293c91484)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [net_config_init_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gab19ec1b3411f38d9bee5abcb25926ea0)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_config_init_app](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga49c6b4cd9d338f1b3d76225a9872c84c)
- [device](../device_reference/P002_设备对象结构.md)
- [net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)
- [username](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md#ae1e2e6c1ddafd2139effc4905f759119)
- [password](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md#a3fda745e9cc9696f301e2cd08c08786a)
- [net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)
- [key_name](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#af44b05c8460c0657ea5c55e8860dee7e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [key_buf](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a823de7fc7e367493d8d9047cceda820a)
- [key_buf_len](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a0c657f31a4d81cd74a86c6792372309a)
- [key_id](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#acacf33b3c455cf690a7eee7279facb27)
- [ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)
- [key_type](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#aed44f6ce3979e24a064f26eb71186733)
- [key_bits](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#ad076498fe79bb8ecad52a78b694b17cb)
- [is_private](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a38c70f14300a67b42bc452f219d35f69)
- [net_config_init_sshd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga99750f4c2ede644821d00b399f0a1a9f)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_config_init_clock_via_sntp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gad1c288429f1178e165ed1429f87b3b81)
- [net_config_sntp_set_server](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4d71cd03a40db9155b29fab43f7d5ec5)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [keygen.h](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [net_config_ssh_key::key_buf_len](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a0c657f31a4d81cd74a86c6792372309a)
- [net_config_ssh_key::is_private](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a38c70f14300a67b42bc452f219d35f69)
- [net_config_ssh_key::key_buf](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#a823de7fc7e367493d8d9047cceda820a)
- [net_config_ssh_key::key_id](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#acacf33b3c455cf690a7eee7279facb27)
- [net_config_ssh_key::key_bits](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#ad076498fe79bb8ecad52a78b694b17cb)
- [net_config_ssh_key::key_type](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#aed44f6ce3979e24a064f26eb71186733)
- [net_config_ssh_key::key_name](../network_core_model_reference/P053_net_config_ssh_key_结构体.md#af44b05c8460c0657ea5c55e8860dee7e)
- [net_config_ssh_password_auth::password](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md#a3fda745e9cc9696f301e2cd08c08786a)
- [net_config_ssh_password_auth::username](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md#ae1e2e6c1ddafd2139effc4905f759119)

---

[上一章](P122_mtk_mt8188_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P124_net_log.h_源码浏览.md)
