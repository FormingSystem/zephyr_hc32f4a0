---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-18
title: 网络配置库（Network Configuration Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_网络配置库（Network Configuration Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络配置库（Network configuration library）

<a id="details"></a>

网络配置库（Network Configuration Library）。引入版本（Since）：1.8；API 版本（Version）：0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

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

## 18.2\_宏定义（Macros）

<a id="r_ga5c1a321477ce072a964bc610aef805f1"></a>

```c
#define NET_CONFIG_NEED_ROUTER 0x00000001
```

相关声明：[NET_CONFIG_NEED_ROUTER](#ga5c1a321477ce072a964bc610aef805f1)。

应用需要设置路由器（Routers），才能连接远程网络（Remote Network）。

<a id="r_ga469731c167f97b5df40b51ee0c87313c"></a>

```c
#define NET_CONFIG_NEED_IPV6 0x00000002
```

相关声明：[NET_CONFIG_NEED_IPV6](#ga469731c167f97b5df40b51ee0c87313c)。

应用需要完成 IPv6 子系统（Subsystem）的配置和初始化。

<a id="r_ga4312efaa62093c93968c0ae81efc36dd"></a>

```c
#define NET_CONFIG_NEED_IPV4 0x00000004
```

相关声明：[NET_CONFIG_NEED_IPV4](#ga4312efaa62093c93968c0ae81efc36dd)。

应用需要完成 IPv4 子系统（Subsystem）的配置和初始化。

<a id="r_ga9b1afb4b698aa62758ce396d742e4aaa"></a>

```c
#define NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC(name, key_bits)
```

相关声明：[NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC](#ga9b1afb4b698aa62758ce396d742e4aaa)。

加载和保存密钥（Keys）所需的临时密钥缓冲区（Temporary Key Buffer）。

<a id="r_ga1eca6e2fc04e527d65b1f01407afc101"></a>

```c
#define NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC(name, user_name, pwd)
```

相关声明：[NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC](#ga1eca6e2fc04e527d65b1f01407afc101)。

为 SSH 服务器配置静态定义用户名和密码（Username and Password）。

<a id="r_ga17bfc65d63f9d5353231c83f3b782e05"></a>

```c
#define NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC(name, _key_buf_name, _key_buf_len, _key_name, _key_id, _key_type, _key_bits)
```

相关声明：[NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC](#ga17bfc65d63f9d5353231c83f3b782e05)。

为 SSH 服务器配置静态定义私钥（Private Key）。

<a id="r_ga7246b19c7bff6991f73dffda982e2932"></a>

```c
#define NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC(name, _key_buf_name, _key_buf_len, _key_name, _key_id)
```

相关声明：[NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC](#ga7246b19c7bff6991f73dffda982e2932)。

为 SSH 服务器配置静态定义公钥（Public Key）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.3\_函数（Functions）

<a id="r_ga02a2b4fbac3eba68a175630293c91484"></a>

```c
int net_config_init (const char *app_info, uint32_t flags, int32_t timeout)
```

相关声明：[net_config_init](#ga02a2b4fbac3eba68a175630293c91484)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

初始化此网络应用（Network Application）。

<a id="r_gab19ec1b3411f38d9bee5abcb25926ea0"></a>

```c
int net_config_init_by_iface (struct net_if *iface, const char *app_info, uint32_t flags, int32_t timeout)
```

相关声明：[net_config_init_by_iface](#gab19ec1b3411f38d9bee5abcb25926ea0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使用指定网络接口（Network Interface）初始化此网络应用。

<a id="r_ga49c6b4cd9d338f1b3d76225a9872c84c"></a>

```c
int net_config_init_app (const struct device *dev, const char *app_info)
```

相关声明：[net_config_init_app](#ga49c6b4cd9d338f1b3d76225a9872c84c)、[device](../device_reference/P002_设备对象结构.md)。

初始化此网络应用（Network Application）。

<a id="r_ga99750f4c2ede644821d00b399f0a1a9f"></a>

```c
static int net_config_init_sshd (struct net_if *iface, const struct net_config_ssh_key *priv_key_config, const struct net_config_ssh_key *pub_key_config, const struct net_config_ssh_password_auth *password_auth_config, int sshd_instance)
```

相关声明：[net_config_init_sshd](#ga99750f4c2ede644821d00b399f0a1a9f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)、[net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)、[net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)。

初始化设备上的 SSH 服务器（Server）。

<a id="r_gad1c288429f1178e165ed1429f87b3b81"></a>

```c
static int net_config_init_clock_via_sntp (void)
```

相关声明：[net_config_init_clock_via_sntp](#gad1c288429f1178e165ed1429f87b3b81)。

使用 SNTP 初始化系统时钟（System Clock）。

<a id="r_ga4d71cd03a40db9155b29fab43f7d5ec5"></a>

```c
static int net_config_sntp_set_server (const char *server)
```

相关声明：[net_config_sntp_set_server](#ga4d71cd03a40db9155b29fab43f7d5ec5)。

设置初始化系统时钟（System Clock）所用的 SNTP 服务器。

## 18.4\_详细说明（Detailed Documentation）

<a id="ga4312efaa62093c93968c0ae81efc36dd"></a>

### `NET_CONFIG_NEED_IPV4`

```c
#define NET_CONFIG_NEED_IPV4 0x00000004
```

```c
#include <zephyr/net/net_config.h>
```

应用需要完成 IPv4 子系统（Subsystem）的配置和初始化。

通常表示设备已设置 IPv4 地址。

<a id="ga469731c167f97b5df40b51ee0c87313c"></a>

### `NET_CONFIG_NEED_IPV6`

```c
#define NET_CONFIG_NEED_IPV6 0x00000002
```

```c
#include <zephyr/net/net_config.h>
```

应用需要完成 IPv6 子系统（Subsystem）的配置和初始化。

通常表示设备已设置 IPv6 地址。

<a id="ga5c1a321477ce072a964bc610aef805f1"></a>

### `NET_CONFIG_NEED_ROUTER`

```c
#define NET_CONFIG_NEED_ROUTER 0x00000001
```

```c
#include <zephyr/net/net_config.h>
```

应用需要设置路由器（Routers），才能连接远程网络（Remote Network）。

对于 IPv6 网络，表示设备应在继续之前收到 IPv6 路由器通告（Router Advertisement）消息。

<a id="ga9b1afb4b698aa62758ce396d742e4aaa"></a>

### `NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC`

```c
#define NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC ( name, key_bits )
```

```c
#include <zephyr/net/net_config.h>
```

展开值（Value）：

```c
static uint8_t name[key_bits]
```

加载和保存密钥（Keys）所需的临时密钥缓冲区（Temporary Key Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | SSH 服务器配置实例的名称，用于标识实例；定义多个实例时必须唯一。 |
| `key_bits` | SSH 密钥大小（Key Size），单位为位。 |

<a id="ga1eca6e2fc04e527d65b1f01407afc101"></a>

### `NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC`

```c
#define NET_CONFIG_SSH_PASSWORD_AUTH_DEFINE_STATIC ( name, user_name, pwd )
```

```c
#include <zephyr/net/net_config.h>
```

展开值（Value）：

```c
static struct net_config_ssh_password_auth name = {             \
        .username = user_name,                                  \
        .password = pwd,                                        \
}
```

为 SSH 服务器配置静态定义用户名和密码（Username and Password）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | SSH 服务器配置实例的名称，用于标识实例；定义多个实例时必须唯一。 |
| `user_name` | 密码认证（Password Authentication）使用的用户名；为 NULL 或空字符串时不使用用户名。用户名不得包含空格。 |
| `pwd` | 密码认证（Password Authentication）使用的密码；为 NULL 或空字符串时禁用密码认证，仅允许公钥认证（Public Key Authentication）。 |

<a id="ga17bfc65d63f9d5353231c83f3b782e05"></a>

### `NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC`

```c
#define NET_CONFIG_SSH_PRIV_KEY_DEFINE_STATIC ( name, _key_buf_name, _key_buf_len, _key_name, _key_id, _key_type, _key_bits )
```

```c
#include <zephyr/net/net_config.h>
```

展开值（Value）：

```c
static struct net_config_ssh_key name = {                       \
        .key_buf = _key_buf_name,                               \
        .key_buf_len = _key_buf_len,                            \
        .key_name = _key_name,                                  \
        .key_id = _key_id,                                      \
        .key_type = _key_type,                                  \
        .key_bits = _key_bits,                                  \
        .is_private = true,                                     \
}
```

为 SSH 服务器配置静态定义私钥（Private Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | SSH 服务器配置实例的名称，用于标识实例；定义多个实例时必须唯一。 |
| `_key_buf_name` | 使用 NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC() 宏定义的临时密钥缓冲区名称。加载和保存密钥需要该缓冲区。私钥和公钥配置可按需共享缓冲区，但大小必须足以容纳两种配置各自的密钥数据。 |
| `_key_buf_len` | 密钥缓冲区（Key Buffer）的大小，单位为字节。 |
| `_key_name` | SSH 密钥名称（Key Name），保存或加载密钥时用于标识密钥，不得包含空格。 |
| `_key_id` | 密钥 ID（Key ID），用于标识密钥。 |
| `_key_type` | SSH 密钥类型（Key Type），例如 RSA 密钥等。 |
| `_key_bits` | SSH 密钥大小（Key Size），单位为位，用于确定加载及保存密钥所需的缓冲区大小。 |

<a id="ga7246b19c7bff6991f73dffda982e2932"></a>

### `NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC`

```c
#define NET_CONFIG_SSH_PUB_KEY_DEFINE_STATIC ( name, _key_buf_name, _key_buf_len, _key_name, _key_id )
```

```c
#include <zephyr/net/net_config.h>
```

展开值（Value）：

```c
static struct net_config_ssh_key name = {                       \
        .key_buf = _key_buf_name,                               \
        .key_buf_len = _key_buf_len,                            \
        .key_name = _key_name,                                  \
        .key_id = _key_id,                                      \
        .key_bits = 0,                                          \
        .is_private = false,                                    \
}
```

为 SSH 服务器配置静态定义公钥（Public Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | SSH 服务器配置实例的名称，用于标识实例；定义多个实例时必须唯一。 |
| `_key_buf_name` | 使用 NET_CONFIG_SSH_KEY_BUF_DEFINE_STATIC() 宏定义的临时密钥缓冲区名称。加载和保存密钥需要该缓冲区。私钥和公钥配置可按需共享缓冲区，但大小必须足以容纳两种配置各自的密钥数据。 |
| `_key_buf_len` | 密钥缓冲区（Key Buffer）的大小，单位为字节。 |
| `_key_name` | SSH 密钥名称（Key Name），保存或加载密钥时用于标识密钥，不得包含空格。 |
| `_key_id` | 密钥 ID（Key ID），用于标识密钥。 |

<a id="ga02a2b4fbac3eba68a175630293c91484"></a>

### `net_config_init()`

```c
int net_config_init ( const char * app_info, uint32_t flags, int32_t timeout )
```

```c
#include <zephyr/net/net_config.h>
```

初始化此网络应用（Network Application）。

调用 net_config_init_by_iface()，传入 NULL 网络接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_info` | 描述此应用的字符串。 |
| `flags` | 与客户端所需服务相关的标志（Flags）。 |
| `timeout` | 继续启动之前，等待网络设置（Network Setup）的时长。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga49c6b4cd9d338f1b3d76225a9872c84c"></a>

### `net_config_init_app()`

```c
int net_config_init_app ( const struct device * dev, const char * app_info )
```

```c
#include <zephyr/net/net_config.h>
```

初始化此网络应用（Network Application）。

设置 CONFIG_NET_CONFIG_AUTO_INIT 后，设备启动时自动调用此函数。若不希望自动调用，应取消此配置，在应用启动时手动调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要使用的网络设备（Network Device）。函数根据设备确定网络接口；device 为 NULL 时使用默认网络接口。 |
| `app_info` | 描述此应用的字符串。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gab19ec1b3411f38d9bee5abcb25926ea0"></a>

### `net_config_init_by_iface()`

```c
int net_config_init_by_iface ( struct net_if * iface, const char * app_info, uint32_t flags, int32_t timeout )
```

```c
#include <zephyr/net/net_config.h>
```

使用指定网络接口（Network Interface）初始化此网络应用。

网络接口为 NULL 时，配置使用默认接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 使用此网络接口（Network Interface）初始化网络。 |
| `app_info` | 描述此应用的字符串。 |
| `flags` | 与客户端所需服务相关的标志（Flags）。 |
| `timeout` | 继续启动之前，等待网络设置（Network Setup）的时长。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gad1c288429f1178e165ed1429f87b3b81"></a>

### `net_config_init_clock_via_sntp()`

```c
int net_config_init_clock_via_sntp ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_config.h>
```

使用 SNTP 初始化系统时钟（System Clock）。

查询配置的简单网络时间协议（SNTP）服务器，并根据响应设置系统实时时钟（Realtime Clock）；也可选择设置 RTC 设备，参见 CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC。调用最多阻塞 CONFIG_NET_CONFIG_SNTP_INIT_TIMEOUT 毫秒。

待查询服务器按以下优先级选择：

- 启用 CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME 时，通过 net_config_sntp_set_server() 设置的服务器；
- 启用 CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION 时，通过 DHCPv4 NTP 服务器选项收到的服务器；
- 在 CONFIG_NET_CONFIG_SNTP_INIT_SERVER 中设置的服务器。

除非使用连接管理器（Connection Manager）驱动 SNTP 客户端，否则由 net_config_init_app 调用此函数；参见 CONFIG_NET_CONFIG_SNTP_INIT_USE_CONNECTION_MANAGER。

**返回（Returns）**：返回值（Returns）：已设置时钟返回 0，错误返回小于 0 的值。

<a id="ga99750f4c2ede644821d00b399f0a1a9f"></a>

### `net_config_init_sshd()`

```c
int net_config_init_sshd ( struct net_if * iface, const struct net_config_ssh_key * priv_key_config, const struct net_config_ssh_key * pub_key_config, const struct net_config_ssh_password_auth * password_auth_config, int sshd_instance )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_config.h>
```

初始化设备上的 SSH 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | SSH 服务器使用的网络接口（Network Interface）；为 NULL 时绑定通配地址（Wildcard Address），可通过所有网络接口访问。 |
| `priv_key_config` | SSH 服务器的私钥配置（Private Key Configuration）。 |
| `pub_key_config` | SSH 服务器的公钥配置（Public Key Configuration）。 |
| `password_auth_config` | SSH 服务器的密码认证配置（Password Authentication Configuration）。使用公钥认证时，可设为 NULL，或令 username 和 password 为 NULL。公钥认证优先于密码认证；两者均配置时，只有公钥认证失败才使用密码认证。若希望为公钥认证指定用户名，即使不使用密码认证，也须在 password_auth_config 结构体中设置 username，因为 SSH 服务器需要该用户名来关联公钥。 |
| `sshd_instance` | SSH 服务器实例编号（Instance Number），用于标识实例；定义多个实例时必须唯一。 |

**返回（Returns）**：返回值（Returns）：成功初始化 SSH 服务器返回 0，错误返回小于 0 的值。

<a id="ga4d71cd03a40db9155b29fab43f7d5ec5"></a>

### `net_config_sntp_set_server()`

```c
int net_config_sntp_set_server ( const char * server)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_config.h>
```

设置初始化系统时钟（System Clock）所用的 SNTP 服务器。

此函数设置的服务器优先于 DHCP 获取的服务器（启用 CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION 时），也优先于 CONFIG_NET_CONFIG_SNTP_INIT_SERVER 设置的服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 要使用的服务器主机名（Hostname）或 IP 地址；传 NULL 或空字符串取消先前设置的服务器。 |

**返回（Returns）**：返回值（Returns）：成功设置 SNTP 服务器返回 0，错误返回小于 0 的值。


## 18.5\_原页交叉引用（Cross References）

- [net_config_ssh_password_auth](../network_core_model_reference/P054_net_config_ssh_password_auth_结构体.md)
- [net_config_ssh_key](../network_core_model_reference/P053_net_config_ssh_key_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [zephyr/net/net_config.h](../api_file_system_power_reference/P029_zephyr__net__net_config.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC)
- [CONFIG_NET_CONFIG_SNTP_INIT_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_TIMEOUT)
- [CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME)
- [CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION)
- [CONFIG_NET_CONFIG_SNTP_INIT_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_SERVER)
- [CONFIG_NET_CONFIG_SNTP_INIT_USE_CONNECTION_MANAGER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_USE_CONNECTION_MANAGER)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__config__ssh__password__auth_html"></a>
<a id="astructnet__config__ssh__key_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_MAX30210 API主题.md) · [返回大纲](大纲.md) · [下一章](P019_Renesas 事件链接控制器（ELC）.md)
