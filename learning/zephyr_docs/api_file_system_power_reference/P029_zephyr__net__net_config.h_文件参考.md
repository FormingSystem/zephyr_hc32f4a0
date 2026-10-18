---
id: learning.zephyr-docs.api-file-system-power-reference.page-29
title: zephyr__net__net_config.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_net\_\_net\_config.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络子系统初始化（Network Subsystem Initialization）的例程。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/shell/shell.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/ssh/keygen.h>
```

查看此文件的源码。

网络子系统初始化（Network Subsystem Initialization）的例程。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 29.1\_数据结构（Data Structures）

<a id="r_net_5Fconfig_5Fssh_5Fpassword_5Fauth"></a>

```c
struct net_config_ssh_password_auth
```

相关声明：[net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)。

包含设备上sshd所用的口令认证（Password Authentication）配置数据。

<a id="r_net_5Fconfig_5Fssh_5Fkey"></a>

```c
struct net_config_ssh_key
```

相关声明：[net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)。

包含设备上sshd所用的密钥配置数据（Key Configuration Data）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.2\_宏定义（Macros）

<a id="r_ga5c1a321477ce072a964bc610aef805f1"></a>

```c
#define NET_CONFIG_NEED_ROUTER 0x00000001
```

相关声明：[NET_CONFIG_NEED_ROUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga5c1a321477ce072a964bc610aef805f1)。

应用需要设置路由器（Routers），才能连接远程网络（Remote Network）。

<a id="r_ga469731c167f97b5df40b51ee0c87313c"></a>

```c
#define NET_CONFIG_NEED_IPV6 0x00000002
```

相关声明：[NET_CONFIG_NEED_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga469731c167f97b5df40b51ee0c87313c)。

应用需要完成 IPv6 子系统（Subsystem）的配置和初始化。

<a id="r_ga4312efaa62093c93968c0ae81efc36dd"></a>

```c
#define NET_CONFIG_NEED_IPV4 0x00000004
```

相关声明：[NET_CONFIG_NEED_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4312efaa62093c93968c0ae81efc36dd)。

应用需要完成 IPv4 子系统（Subsystem）的配置和初始化。

<a id="r_ga9b1afb4b698aa62758ce396d742e4aaa"></a>

```c
#define NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC(name, key_bits)
```

相关声明：[NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga9b1afb4b698aa62758ce396d742e4aaa)。

加载和保存密钥（Keys）所需的临时密钥缓冲区（Temporary Key Buffer）。

<a id="r_ga1eca6e2fc04e527d65b1f01407afc101"></a>

```c
#define NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC(name, user_name, pwd)
```

相关声明：[NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga1eca6e2fc04e527d65b1f01407afc101)。

为 SSH 服务器配置静态定义用户名和密码（Username and Password）。

<a id="r_ga17bfc65d63f9d5353231c83f3b782e05"></a>

```c
#define NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC(name, _key_buf_name, _key_buf_len, _key_name, _key_id, _key_type, _key_bits)
```

相关声明：[NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga17bfc65d63f9d5353231c83f3b782e05)。

为 SSH 服务器配置静态定义私钥（Private Key）。

<a id="r_ga7246b19c7bff6991f73dffda982e2932"></a>

```c
#define NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC(name, _key_buf_name, _key_buf_len, _key_name, _key_id)
```

相关声明：[NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga7246b19c7bff6991f73dffda982e2932)。

为 SSH 服务器配置静态定义公钥（Public Key）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.3\_函数（Functions）

<a id="r_ga02a2b4fbac3eba68a175630293c91484"></a>

```c
int net_config_init (const char *app_info, uint32_t flags, int32_t timeout)
```

相关声明：[net_config_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga02a2b4fbac3eba68a175630293c91484)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

初始化此网络应用（Network Application）。

<a id="r_gab19ec1b3411f38d9bee5abcb25926ea0"></a>

```c
int net_config_init_by_iface (struct net_if *iface, const char *app_info, uint32_t flags, int32_t timeout)
```

相关声明：[net_config_init_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gab19ec1b3411f38d9bee5abcb25926ea0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使用指定网络接口（Network Interface）初始化此网络应用。

<a id="r_ga49c6b4cd9d338f1b3d76225a9872c84c"></a>

```c
int net_config_init_app (const struct device *dev, const char *app_info)
```

相关声明：[net_config_init_app](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga49c6b4cd9d338f1b3d76225a9872c84c)、[device](../device_reference/P002_设备对象结构.md)。

初始化此网络应用（Network Application）。

<a id="r_ga99750f4c2ede644821d00b399f0a1a9f"></a>

```c
static int net_config_init_sshd (struct net_if *iface, const struct net_config_ssh_key *priv_key_config, const struct net_config_ssh_key *pub_key_config, const struct net_config_ssh_password_auth *password_auth_config, int sshd_instance)
```

相关声明：[net_config_init_sshd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga99750f4c2ede644821d00b399f0a1a9f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)、[net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)、[net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)。

初始化设备上的 SSH 服务器（Server）。

<a id="r_gad1c288429f1178e165ed1429f87b3b81"></a>

```c
static int net_config_init_clock_via_sntp (void)
```

相关声明：[net_config_init_clock_via_sntp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gad1c288429f1178e165ed1429f87b3b81)。

使用 SNTP 初始化系统时钟（System Clock）。

<a id="r_ga4d71cd03a40db9155b29fab43f7d5ec5"></a>

```c
static int net_config_sntp_set_server (const char *server)
```

相关声明：[net_config_sntp_set_server](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4d71cd03a40db9155b29fab43f7d5ec5)。

设置初始化系统时钟（System Clock）所用的 SNTP 服务器。


## 29.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/ssh/keygen.h](../api_source_reference/P430_keygen.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P123_net_config.h_源码浏览.md)
- [net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)
- [net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)
- [NET_CONFIG_NEED_ROUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga5c1a321477ce072a964bc610aef805f1)
- [NET_CONFIG_NEED_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga469731c167f97b5df40b51ee0c87313c)
- [NET_CONFIG_NEED_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4312efaa62093c93968c0ae81efc36dd)
- [NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga9b1afb4b698aa62758ce396d742e4aaa)
- [NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga1eca6e2fc04e527d65b1f01407afc101)
- [NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga17bfc65d63f9d5353231c83f3b782e05)
- [NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga7246b19c7bff6991f73dffda982e2932)
- [net_config_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga02a2b4fbac3eba68a175630293c91484)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_config_init_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gab19ec1b3411f38d9bee5abcb25926ea0)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_config_init_app](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga49c6b4cd9d338f1b3d76225a9872c84c)
- [device](../device_reference/P002_设备对象结构.md)
- [net_config_init_sshd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga99750f4c2ede644821d00b399f0a1a9f)
- [net_config_init_clock_via_sntp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gad1c288429f1178e165ed1429f87b3b81)
- [net_config_sntp_set_server](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4d71cd03a40db9155b29fab43f7d5ec5)

<a id="header-details"></a>

---

[上一章](P028_zephyr__dt-bindings__clock__mchp_xec_pcr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__gpio__nordic-nrf-gpio.h_文件参考.md)
